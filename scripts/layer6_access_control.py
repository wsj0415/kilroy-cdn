#!/usr/bin/env python3
"""
Layer 6: Access Control
Path guards and URL safety for preventing file/URL-based attacks.

Based on Matthew Berman's OpenClaw defense system.
"""

import re
import socket
import ipaddress
from typing import Dict, List, Optional, Set, Tuple
from urllib.parse import urlparse
from dataclasses import dataclass


@dataclass
class AccessResult:
    """Result of access control check."""
    allowed: bool
    reason: str
    violations: List[str]


class AccessController:
    """
    Access control layer for file paths and URLs.
    
    Prevents:
    - Reading sensitive files (.env, credentials, etc.)
    - Accessing files outside allowed directories
    - Making requests to internal/private networks
    - DNS rebinding attacks
    """
    
    # Sensitive file patterns (deny list)
    SENSITIVE_FILES = {
        '.env', '.env.local', '.env.production', '.env.development',
        'credentials.json', 'secrets.json', 'config.json',
        'id_rsa', 'id_dsa', 'id_ecdsa', 'id_ed25519',
        '.htpasswd', '.htaccess', 'shadow', 'passwd',
        'token', 'apikey', 'secret', 'password',
        'private.key', 'private.pem', 'client_secret.json',
        'aws_credentials', 'gcp_credentials', 'azure_credentials',
    }
    
    # Sensitive extensions
    SENSITIVE_EXTENSIONS = {
        '.pem', '.key', '.p12', '.pfx', '.crt', '.cer',
        '.env', '.htpasswd', '.htaccess',
    }
    
    # Private/reserved IP ranges
    PRIVATE_RANGES = [
        ipaddress.ip_network('10.0.0.0/8'),
        ipaddress.ip_network('172.16.0.0/12'),
        ipaddress.ip_network('192.168.0.0/16'),
        ipaddress.ip_network('127.0.0.0/8'),
        ipaddress.ip_network('169.254.0.0/16'),  # Link-local
        ipaddress.ip_network('0.0.0.0/8'),
        ipaddress.ip_network('fc00::/7'),  # IPv6 private
        ipaddress.ip_network('fe80::/10'),  # IPv6 link-local
    ]
    
    # Known DNS rebinding services
    DNS_REBINDING_SERVICES = {
        'xip.io', 'nip.io', 'sslip.io',
        'localtest.me', 'lvh.me', 'vcap.me',
    }
    
    def __init__(
        self,
        allowed_directories: Optional[List[str]] = None,
        additional_sensitive_files: Optional[Set[str]] = None
    ):
        """
        Initialize access controller.
        
        Args:
            allowed_directories: List of allowed base directories
            additional_sensitive_files: Additional sensitive file patterns
        """
        self.allowed_directories = allowed_directories or []
        self.sensitive_files = self.SENSITIVE_FILES.copy()
        if additional_sensitive_files:
            self.sensitive_files.update(additional_sensitive_files)
        
        self.stats = {
            'path_checks': 0,
            'path_blocked': 0,
            'url_checks': 0,
            'url_blocked': 0,
            'sensitive_files_blocked': 0,
            'path_escape_blocked': 0,
            'private_ip_blocked': 0,
            'dns_rebinding_blocked': 0,
        }
    
    def check_path(self, path: str) -> AccessResult:
        """
        Check if a file path is safe to access.
        
        Args:
            path: File path to check
            
        Returns AccessResult indicating if access is allowed.
        """
        self.stats['path_checks'] += 1
        violations = []
        
        # Normalize path
        normalized = self._normalize_path(path)
        
        # Check 1: Sensitive filename
        basename = normalized.split('/')[-1].split('\\')[-1]
        if basename in self.sensitive_files:
            self.stats['sensitive_files_blocked'] += 1
            self.stats['path_blocked'] += 1
            violations.append(f'sensitive_file: {basename}')
            return AccessResult(
                allowed=False,
                reason=f'Access to sensitive file blocked: {basename}',
                violations=violations
            )
        
        # Check 2: Sensitive extension
        for ext in self.SENSITIVE_EXTENSIONS:
            if normalized.endswith(ext):
                self.stats['sensitive_files_blocked'] += 1
                self.stats['path_blocked'] += 1
                violations.append(f'sensitive_extension: {ext}')
                return AccessResult(
                    allowed=False,
                    reason=f'Access to file with sensitive extension blocked: {ext}',
                    violations=violations
                )
        
        # Check 3: Path traversal / escape
        if self._is_path_escape(normalized):
            self.stats['path_escape_blocked'] += 1
            self.stats['path_blocked'] += 1
            violations.append('path_escape_attempt')
            return AccessResult(
                allowed=False,
                reason='Path escape attempt detected',
                violations=violations
            )
        
        # Check 4: Allowed directory constraint
        if self.allowed_directories and not self._is_in_allowed_directory(normalized):
            self.stats['path_blocked'] += 1
            violations.append('outside_allowed_directory')
            return AccessResult(
                allowed=False,
                reason='Path outside allowed directories',
                violations=violations
            )
        
        return AccessResult(
            allowed=True,
            reason='Path access allowed',
            violations=[]
        )
    
    def check_url(self, url: str, resolve_hostname: bool = True) -> AccessResult:
        """
        Check if a URL is safe to access.
        
        Args:
            url: URL to check
            resolve_hostname: Whether to resolve hostname to check IP
            
        Returns AccessResult indicating if access is allowed.
        """
        self.stats['url_checks'] += 1
        violations = []
        
        # Parse URL
        try:
            parsed = urlparse(url)
        except Exception as e:
            self.stats['url_blocked'] += 1
            return AccessResult(
                allowed=False,
                reason=f'Invalid URL: {str(e)}',
                violations=['invalid_url']
            )
        
        # Check 1: Scheme
        if parsed.scheme not in ('http', 'https'):
            self.stats['url_blocked'] += 1
            violations.append(f'unsupported_scheme: {parsed.scheme}')
            return AccessResult(
                allowed=False,
                reason=f'Unsupported URL scheme: {parsed.scheme}',
                violations=violations
            )
        
        hostname = parsed.hostname
        if not hostname:
            self.stats['url_blocked'] += 1
            violations.append('missing_hostname')
            return AccessResult(
                allowed=False,
                reason='URL missing hostname',
                violations=violations
            )
        
        # Check 2: DNS rebinding services
        for service in self.DNS_REBINDING_SERVICES:
            if service in hostname.lower():
                self.stats['dns_rebinding_blocked'] += 1
                self.stats['url_blocked'] += 1
                violations.append(f'dns_rebinding_service: {service}')
                return AccessResult(
                    allowed=False,
                    reason=f'DNS rebinding service detected: {service}',
                    violations=violations
                )
        
        # Check 3: Private IP (if resolving)
        if resolve_hostname:
            try:
                ip = self._resolve_hostname(hostname)
                if ip and self._is_private_ip(ip):
                    self.stats['private_ip_blocked'] += 1
                    self.stats['url_blocked'] += 1
                    violations.append(f'private_ip: {ip}')
                    return AccessResult(
                        allowed=False,
                        reason=f'Access to private IP blocked: {ip}',
                        violations=violations
                    )
            except Exception as e:
                # Resolution failed - allow but log
                violations.append(f'resolution_warning: {str(e)}')
        
        # Check 4: Direct IP in URL
        try:
            ip = ipaddress.ip_address(hostname)
            if self._is_private_ip(ip):
                self.stats['private_ip_blocked'] += 1
                self.stats['url_blocked'] += 1
                violations.append(f'direct_private_ip: {ip}')
                return AccessResult(
                    allowed=False,
                    reason=f'Direct private IP access blocked: {ip}',
                    violations=violations
                )
        except ValueError:
            # Not an IP address, continue
            pass
        
        return AccessResult(
            allowed=True,
            reason='URL access allowed',
            violations=violations
        )
    
    def _normalize_path(self, path: str) -> str:
        """Normalize a file path."""
        # Convert backslashes to forward slashes
        normalized = path.replace('\\', '/')
        
        # Remove redundant slashes
        normalized = re.sub(r'/+', '/', normalized)
        
        # Resolve . and ..
        parts = normalized.split('/')
        resolved = []
        for part in parts:
            if part == '..':
                if resolved:
                    resolved.pop()
            elif part != '.' and part != '':
                resolved.append(part)
        
        return '/'.join(resolved)
    
    def _is_path_escape(self, path: str) -> bool:
        """Check if path attempts directory escape."""
        # Check for .. in original path (before normalization)
        if '..' in path:
            # Count .. occurrences
            dotdot_count = path.count('..')
            # If more .. than directory depth, it's an escape attempt
            depth = len([p for p in path.split('/') if p and p != '..'])
            if dotdot_count > depth:
                return True
        
        # Check for null bytes
        if '\x00' in path:
            return True
        
        # Check for URL encoding of dangerous characters
        dangerous_patterns = ['%2e%2e', '%252e%252e', '..%2f', '%2f..']
        for pattern in dangerous_patterns:
            if pattern in path.lower():
                return True
        
        return False
    
    def _is_in_allowed_directory(self, path: str) -> bool:
        """Check if path is within allowed directories."""
        if not self.allowed_directories:
            return True
        
        for allowed in self.allowed_directories:
            allowed_normalized = self._normalize_path(allowed)
            if path.startswith(allowed_normalized):
                return True
        
        return False
    
    def _resolve_hostname(self, hostname: str) -> Optional[str]:
        """Resolve hostname to IP address."""
        try:
            ip = socket.getaddrinfo(hostname, None)[0][4][0]
            return ip
        except Exception:
            return None
    
    def _is_private_ip(self, ip_str: str) -> bool:
        """Check if IP is in private/reserved range."""
        try:
            ip = ipaddress.ip_address(ip_str)
            for network in self.PRIVATE_RANGES:
                if ip in network:
                    return True
            return False
        except ValueError:
            return False
    
    def get_stats(self) -> Dict:
        """Get access control statistics."""
        return self.stats.copy()
    
    def reset_stats(self):
        """Reset statistics."""
        self.stats = {
            'path_checks': 0,
            'path_blocked': 0,
            'url_checks': 0,
            'url_blocked': 0,
            'sensitive_files_blocked': 0,
            'path_escape_blocked': 0,
            'private_ip_blocked': 0,
            'dns_rebinding_blocked': 0,
        }


def main():
    """CLI interface for testing."""
    import sys
    
    print("Layer 6: Access Control")
    print("=" * 50)
    
    controller = AccessController(
        allowed_directories=['/home/user/projects', '/tmp']
    )
    
    # Path tests
    print("\n📁 Path Tests:")
    path_tests = [
        ('/home/user/projects/myfile.txt', 'allowed'),
        ('/etc/passwd', 'sensitive'),
        ('../../etc/shadow', 'escape'),
        ('/home/user/.env', 'sensitive_file'),
        ('/tmp/test.pem', 'sensitive_ext'),
    ]
    
    for path, expected in path_tests:
        result = controller.check_path(path)
        status = "✅" if result.allowed else "❌"
        print(f"  {status} {path}")
        print(f"     Result: {result.reason}")
    
    # URL tests
    print("\n🌐 URL Tests:")
    url_tests = [
        ('https://example.com/api', 'allowed'),
        ('http://192.168.1.1/admin', 'private_ip'),
        ('https://internal.xip.io', 'dns_rebinding'),
        ('ftp://example.com/file', 'bad_scheme'),
        ('https://10.0.0.1/config', 'private_ip'),
    ]
    
    for url, expected in url_tests:
        result = controller.check_url(url, resolve_hostname=False)
        status = "✅" if result.allowed else "❌"
        print(f"  {status} {url}")
        print(f"     Result: {result.reason}")
    
    print("\n📊 Stats:")
    stats = controller.get_stats()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    print("\n" + "=" * 50)
    print("All tests completed!")


if __name__ == '__main__':
    main()
