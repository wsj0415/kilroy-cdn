#!/usr/bin/env python3
"""
Layer 5: Runtime Governance
Spend caps, volume limits, and loop detection for LLM calls.

Based on Matthew Berman's OpenClaw defense system.
"""

import time
import hashlib
from typing import Dict, Optional, Callable
from dataclasses import dataclass, field
from collections import deque


@dataclass
class GovernorConfig:
    """Configuration for runtime governance."""
    # Spend limits (USD)
    spend_warning_threshold: float = 5.0
    spend_hard_cap: float = 15.0
    spend_window_minutes: int = 5
    
    # Volume limits
    global_volume_limit: int = 200
    volume_window_minutes: int = 10
    
    # Per-caller limits
    caller_limits: Dict[str, int] = field(default_factory=lambda: {
        'email_extractor': 40,
        'frontier_scanner': 50,
        'default': 100
    })
    
    # Lifetime limit
    lifetime_limit: int = 300
    
    # Duplicate detection
    duplicate_cache_size: int = 100
    duplicate_ttl_seconds: int = 300


class CallGovernor:
    """
    Runtime governor for LLM calls.
    
    Wraps every LLM call with:
    - Spend tracking
    - Volume limiting
    - Lifetime counting
    - Duplicate detection
    """
    
    def __init__(self, config: Optional[GovernorConfig] = None):
        self.config = config or GovernorConfig()
        
        # Spend tracking
        self.spend_window: deque = deque()
        self.total_spend: float = 0.0
        
        # Volume tracking
        self.volume_window: deque = deque()
        self.caller_volumes: Dict[str, deque] = {}
        
        # Lifetime tracking
        self.lifetime_calls: int = 0
        
        # Duplicate cache: {hash: (response, timestamp)}
        self.duplicate_cache: Dict[str, tuple] = {}
        
        # Stats
        self.stats = {
            'total_calls': 0,
            'blocked_by_spend': 0,
            'blocked_by_volume': 0,
            'blocked_by_lifetime': 0,
            'duplicates_found': 0,
            'estimated_spend': 0.0
        }
    
    def call(self, 
             prompt: str, 
             llm_fn: Callable,
             caller: str = 'default',
             estimated_cost: float = 0.01,
             skip_duplicate_check: bool = False) -> Dict:
        """
        Wrap an LLM call with governance.
        
        Args:
            prompt: The prompt to send
            llm_fn: Function that makes the actual LLM call
            caller: Identifier for the calling component
            estimated_cost: Estimated USD cost of this call
            skip_duplicate_check: If True, bypass duplicate detection
            
        Returns:
            Dict with 'allowed', 'response', 'reason', 'cached'
        """
        now = time.time()
        
        # Check 1: Lifetime limit
        if self.lifetime_calls >= self.config.lifetime_limit:
            self.stats['blocked_by_lifetime'] += 1
            return {
                'allowed': False,
                'response': None,
                'reason': f'lifetime_limit_exceeded: {self.lifetime_calls}/{self.config.lifetime_limit}',
                'cached': False
            }
        
        # Check 2: Duplicate detection
        if not skip_duplicate_check:
            prompt_hash = hashlib.sha256(prompt.encode()).hexdigest()[:32]
            cached = self._check_duplicate(prompt_hash)
            if cached:
                self.stats['duplicates_found'] += 1
                return {
                    'allowed': True,
                    'response': cached,
                    'reason': 'duplicate_found',
                    'cached': True
                }
        
        # Check 3: Spend limit
        self._cleanup_spend_window(now)
        if self.total_spend >= self.config.spend_hard_cap:
            self.stats['blocked_by_spend'] += 1
            return {
                'allowed': False,
                'response': None,
                'reason': f'spend_cap_exceeded: ${self.total_spend:.2f}/${self.config.spend_hard_cap}',
                'cached': False
            }
        
        if self.total_spend >= self.config.spend_warning_threshold:
            print(f"[Governor] WARNING: Spend threshold reached: ${self.total_spend:.2f}")
        
        # Check 4: Volume limit
        self._cleanup_volume_window(now)
        if len(self.volume_window) >= self.config.global_volume_limit:
            self.stats['blocked_by_volume'] += 1
            return {
                'allowed': False,
                'response': None,
                'reason': f'volume_limit_exceeded: {len(self.volume_window)}/{self.config.global_volume_limit}',
                'cached': False
            }
        
        # Check per-caller limit
        caller_limit = self.config.caller_limits.get(caller, self.config.caller_limits['default'])
        caller_volume = len(self.caller_volumes.get(caller, deque()))
        if caller_volume >= caller_limit:
            self.stats['blocked_by_volume'] += 1
            return {
                'allowed': False,
                'response': None,
                'reason': f'caller_volume_limit_exceeded: {caller}:{caller_volume}/{caller_limit}',
                'cached': False
            }
        
        # All checks passed - make the call
        try:
            response = llm_fn(prompt)
            
            # Update tracking
            self.lifetime_calls += 1
            self.spend_window.append((now, estimated_cost))
            self.total_spend += estimated_cost
            self.volume_window.append(now)
            
            if caller not in self.caller_volumes:
                self.caller_volumes[caller] = deque()
            self.caller_volumes[caller].append(now)
            
            # Cache for duplicate detection
            if not skip_duplicate_check:
                self.duplicate_cache[prompt_hash] = (response, now)
                self._cleanup_duplicate_cache(now)
            
            self.stats['total_calls'] += 1
            self.stats['estimated_spend'] += estimated_cost
            
            return {
                'allowed': True,
                'response': response,
                'reason': 'allowed',
                'cached': False
            }
            
        except Exception as e:
            return {
                'allowed': False,
                'response': None,
                'reason': f'llm_error: {str(e)}',
                'cached': False
            }
    
    def _check_duplicate(self, prompt_hash: str) -> Optional[str]:
        """Check if this prompt was recently processed."""
        if prompt_hash in self.duplicate_cache:
            response, timestamp = self.duplicate_cache[prompt_hash]
            age = time.time() - timestamp
            if age < self.config.duplicate_ttl_seconds:
                return response
        return None
    
    def _cleanup_duplicate_cache(self, now: float):
        """Remove expired entries from duplicate cache."""
        expired = [
            h for h, (_, ts) in self.duplicate_cache.items()
            if now - ts > self.config.duplicate_ttl_seconds
        ]
        for h in expired:
            del self.duplicate_cache[h]
        
        # If still too large, remove oldest
        while len(self.duplicate_cache) > self.config.duplicate_cache_size:
            oldest = min(self.duplicate_cache.items(), key=lambda x: x[1][1])
            del self.duplicate_cache[oldest[0]]
    
    def _cleanup_spend_window(self, now: float):
        """Remove old spend entries outside the window."""
        window_seconds = self.config.spend_window_minutes * 60
        cutoff = now - window_seconds
        
        while self.spend_window and self.spend_window[0][0] < cutoff:
            old_time, old_cost = self.spend_window.popleft()
            self.total_spend -= old_cost
        
        self.total_spend = max(0.0, self.total_spend)
    
    def _cleanup_volume_window(self, now: float):
        """Remove old volume entries outside the window."""
        window_seconds = self.config.volume_window_minutes * 60
        cutoff = now - window_seconds
        
        while self.volume_window and self.volume_window[0] < cutoff:
            self.volume_window.popleft()
        
        for caller, window in self.caller_volumes.items():
            while window and window[0] < cutoff:
                window.popleft()
    
    def get_stats(self) -> Dict:
        """Get current governor statistics."""
        return {
            **self.stats,
            'current_spend_window': self.total_spend,
            'current_volume': len(self.volume_window),
            'lifetime_calls': self.lifetime_calls,
            'duplicate_cache_size': len(self.duplicate_cache)
        }
    
    def reset(self):
        """Reset all tracking (use with caution)."""
        self.spend_window.clear()
        self.volume_window.clear()
        self.caller_volumes.clear()
        self.duplicate_cache.clear()
        self.total_spend = 0.0
        self.lifetime_calls = 0


def main():
    """CLI interface for testing."""
    import sys
    
    print("Layer 5: Runtime Governor")
    print("=" * 50)
    
    # Create governor with test config
    config = GovernorConfig(
        spend_hard_cap=1.0,  # $1 for testing
        global_volume_limit=10,
        lifetime_limit=20
    )
    
    governor = CallGovernor(config)
    
    # Mock LLM function
    def mock_llm(prompt: str) -> str:
        return f"Response to: {prompt[:30]}..."
    
    # Test calls
    print("\nTest 1: Normal call")
    result = governor.call("Hello world", mock_llm, estimated_cost=0.05)
    print(f"  Result: {result['allowed']}, Reason: {result['reason']}")
    
    print("\nTest 2: Duplicate detection")
    result = governor.call("Hello world", mock_llm, estimated_cost=0.05)
    print(f"  Result: {result['allowed']}, Cached: {result['cached']}")
    
    print("\nTest 3: Skip duplicate check")
    result = governor.call("Hello world", mock_llm, estimated_cost=0.05, skip_duplicate_check=True)
    print(f"  Result: {result['allowed']}, Cached: {result['cached']}")
    
    print("\nStats:")
    stats = governor.get_stats()
    for key, value in stats.items():
        print(f"  {key}: {value}")


if __name__ == '__main__':
    main()
