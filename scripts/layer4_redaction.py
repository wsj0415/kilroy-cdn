#!/usr/bin/env python3
"""
Layer 4: Redaction Pipeline
PII and secret redaction for outbound messages.

Based on Matthew Berman's OpenClaw defense system.
"""

import re
from typing import Dict, List, Optional, Set
from dataclasses import dataclass


@dataclass
class RedactionRule:
    """Rule for redacting sensitive data."""
    name: str
    pattern: str
    replacement: str
    description: str


class RedactionPipeline:
    """
    Pipeline for redacting sensitive data from outbound messages.
    
    Three modules:
    1. Secret redaction - API keys, tokens, passwords
    2. PII redaction - Personal information
    3. Notification pipeline - Combined pipeline for notifications
    """
    
    # Personal email providers (work emails allowed)
    PERSONAL_EMAIL_DOMAINS = {
        'gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com',
        'qq.com', '163.com', '126.com', 'sina.com',
        'icloud.com', 'me.com', 'protonmail.com', 'yandex.com',
        'mail.ru', 'naver.com', 'daum.net', 'foxmail.com'
    }
    
    def __init__(self):
        self.rules = self._build_rules()
        self.stats = {
            'secrets_redacted': 0,
            'emails_redacted': 0,
            'phones_redacted': 0,
            'amounts_redacted': 0,
            'total_redactions': 0
        }
    
    def _build_rules(self) -> List[RedactionRule]:
        """Build redaction rules."""
        return [
            # API Keys
            RedactionRule(
                'openai_api_key',
                r'sk-[a-zA-Z0-9]{48}',
                '[OPENAI_API_KEY_REDACTED]',
                'OpenAI API Key'
            ),
            RedactionRule(
                'google_api_key',
                r'AIza[0-9A-Za-z_-]{35}',
                '[GOOGLE_API_KEY_REDACTED]',
                'Google API Key'
            ),
            RedactionRule(
                'xai_api_key',
                r'xai-[a-zA-Z0-9]{32}',
                '[XAI_API_KEY_REDACTED]',
                'xAI API Key'
            ),
            RedactionRule(
                'slack_token',
                r'xox[baprs]-[0-9]{10,13}-[0-9]{10,13}-[a-zA-Z0-9]{24}',
                '[SLACK_TOKEN_REDACTED]',
                'Slack Token'
            ),
            RedactionRule(
                'github_token',
                r'ghp_[a-zA-Z0-9]{36}',
                '[GITHUB_TOKEN_REDACTED]',
                'GitHub Personal Token'
            ),
            RedactionRule(
                'telegram_bot_token',
                r'[0-9]{9}:[a-zA-Z0-9_-]{35}',
                '[TELEGRAM_BOT_TOKEN_REDACTED]',
                'Telegram Bot Token'
            ),
            RedactionRule(
                'aws_access_key',
                r'AKIA[0-9A-Z]{16}',
                '[AWS_ACCESS_KEY_REDACTED]',
                'AWS Access Key ID'
            ),
            RedactionRule(
                'stripe_key',
                r'sk_live_[0-9a-zA-Z]{24,}',
                '[STRIPE_KEY_REDACTED]',
                'Stripe Live Key'
            ),
            # Generic patterns
            RedactionRule(
                'generic_api_key',
                r'(?i)(?:api[_-]?key|apikey)["\']?\s*[:=]\s*["\']?[a-zA-Z0-9_-]{16,}["\']?',
                '[API_KEY_REDACTED]',
                'Generic API Key'
            ),
            RedactionRule(
                'generic_secret',
                r'(?i)(?:secret|private[_-]?key)["\']?\s*[:=]\s*["\']?[a-zA-Z0-9_-]{16,}["\']?',
                '[SECRET_REDACTED]',
                'Generic Secret'
            ),
            RedactionRule(
                'password',
                r'(?i)(?:password|passwd|pwd)["\']?\s*[:=]\s*["\'][^\s"\']{8,}["\']?',
                '[PASSWORD_REDACTED]',
                'Password'
            ),
            RedactionRule(
                'bearer_token',
                r'Bearer\s+[a-zA-Z0-9_\-\.]+',
                'Bearer [TOKEN_REDACTED]',
                'Bearer Token'
            ),
        ]
    
    def redact_secrets(self, text: str) -> str:
        """
        Redact API keys and secrets.
        
        Returns text with secrets replaced by placeholders.
        """
        redacted = text
        
        for rule in self.rules:
            matches = list(re.finditer(rule.pattern, redacted))
            if matches:
                self.stats['secrets_redacted'] += len(matches)
                self.stats['total_redactions'] += len(matches)
                # Replace from end to preserve positions
                for match in reversed(matches):
                    redacted = redacted[:match.start()] + rule.replacement + redacted[match.end():]
        
        return redacted
    
    def redact_pii(self, text: str, allow_work_emails: bool = True) -> str:
        """
        Redact personal identifiable information.
        
        Args:
            text: Text to redact
            allow_work_emails: If True, only redact personal emails
            
        Returns redacted text.
        """
        redacted = text
        
        # Email addresses
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = list(re.finditer(email_pattern, redacted))
        
        for match in reversed(emails):
            email = match.group()
            domain = email.split('@')[1].lower()
            
            if allow_work_emails and domain not in self.PERSONAL_EMAIL_DOMAINS:
                # Work email - keep it
                continue
            
            self.stats['emails_redacted'] += 1
            self.stats['total_redactions'] += 1
            redacted = redacted[:match.start()] + '[EMAIL_REDACTED]' + redacted[match.end():]
        
        # Phone numbers (various formats)
        phone_patterns = [
            r'\+?1?[-.\s]?\(?[0-9]{3}\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}',  # US
            r'\+?[0-9]{1,3}[-.\s]?[0-9]{3}[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}',  # International
            r'[0-9]{3}[-.\s]?[0-9]{4}[-.\s]?[0-9]{4}',  # Korean
            r'1[3-9]\d{9}',  # China mobile
        ]
        
        for pattern in phone_patterns:
            phones = list(re.finditer(pattern, redacted))
            for match in reversed(phones):
                self.stats['phones_redacted'] += 1
                self.stats['total_redactions'] += 1
                redacted = redacted[:match.start()] + '[PHONE_REDACTED]' + redacted[match.end():]
        
        return redacted
    
    def redact_financial(self, text: str, allowlisted: Optional[Set[str]] = None) -> str:
        """
        Redact financial data (dollar amounts).
        
        Args:
            text: Text to redact
            allowlisted: Set of allowed amounts (e.g., {'$99', '$199'})
            
        Returns redacted text.
        """
        allowlisted = allowlisted or set()
        redacted = text
        
        # Dollar amounts
        amount_patterns = [
            r'\$[0-9,]+(?:\.[0-9]{2})?',
            r'USD?\s*[0-9,]+(?:\.[0-9]{2})?',
        ]
        
        for pattern in amount_patterns:
            amounts = list(re.finditer(pattern, redacted, re.IGNORECASE))
            for match in reversed(amounts):
                amount = match.group()
                if amount in allowlisted:
                    continue
                
                self.stats['amounts_redacted'] += 1
                self.stats['total_redactions'] += 1
                redacted = redacted[:match.start()] + '[AMOUNT_REDACTED]' + redacted[match.end():]
        
        return redacted
    
    def notification_pipeline(
        self,
        text: str,
        allow_work_emails: bool = True,
        allowlisted_amounts: Optional[Set[str]] = None
    ) -> str:
        """
        Full notification pipeline - chains all redaction modules.
        
        Use this before sending messages to Telegram, Slack, email, etc.
        
        Args:
            text: Original message text
            allow_work_emails: Keep work emails
            allowlisted_amounts: Set of allowed dollar amounts
            
        Returns fully redacted text safe for notification channels.
        """
        # Chain: secrets -> PII -> financial
        redacted = self.redact_secrets(text)
        redacted = self.redact_pii(redacted, allow_work_emails)
        redacted = self.redact_financial(redacted, allowlisted_amounts)
        
        return redacted
    
    def get_stats(self) -> Dict:
        """Get redaction statistics."""
        return self.stats.copy()
    
    def reset_stats(self):
        """Reset statistics."""
        self.stats = {
            'secrets_redacted': 0,
            'emails_redacted': 0,
            'phones_redacted': 0,
            'amounts_redacted': 0,
            'total_redactions': 0
        }


def main():
    """CLI interface for testing."""
    import sys
    
    print("Layer 4: Redaction Pipeline")
    print("=" * 50)
    
    pipeline = RedactionPipeline()
    
    test_cases = [
        ("Contact me at john@gmail.com or call 555-123-4567", "PII"),
        ("API key: sk-abc123... and password: secret123", "Secrets"),
        ("The price is $500 or $99 for premium", "Financial"),
        ("My work email is john@company.com", "Work email"),
        ("Bearer token: eyJhbGciOiJIUzI1NiIs...", "Bearer token"),
    ]
    
    for text, desc in test_cases:
        print(f"\n{desc}:")
        print(f"  Original: {text}")
        
        # Test individual modules
        secrets_redacted = pipeline.redact_secrets(text)
        pii_redacted = pipeline.redact_pii(text)
        financial_redacted = pipeline.redact_financial(text, allowlisted={'$99'})
        
        print(f"  Secrets:  {secrets_redacted}")
        print(f"  PII:      {pii_redacted}")
        print(f"  Financial: {financial_redacted}")
        
        # Test full pipeline
        pipeline.reset_stats()
        full_redacted = pipeline.notification_pipeline(text, allowlisted_amounts={'$99'})
        print(f"  Full:     {full_redacted}")
        print(f"  Stats:    {pipeline.get_stats()}")
    
    print("\n" + "=" * 50)
    print("All tests completed!")


if __name__ == '__main__':
    main()
