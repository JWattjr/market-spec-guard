# Security and consensus audit: MarketSpecGuard

Audit date: 2026-08-12
Scope: `contracts/MarketSpecGuard.py`
Method: manual review, GenVM AST lint, SDK schema validation, direct-mode
idempotency/URL tests, and hosted-network receipt inspection.

## Result

No unresolved critical or high-severity issue was found after remediation.
The guard is a pre-listing policy primitive; it accepts no stake and performs
no payout.

## Remediated findings

| ID | Severity | Finding | Remediation |
| --- | --- | --- | --- |
| MG-01 | Medium | The idempotency branch checked `LISTED` while stored state is `LISTABLE`. | Correct the terminal-state check and add a repeat-review regression test. |
| MG-02 | Medium | Evidence URL checks allowed local/private targets. | Require bounded public HTTPS hosts and reject loopback/private literals, internal suffixes, userinfo, and non-default ports. |
| MG-03 | Medium | Consensus closures captured storage-backed market inputs. | Snapshot question, outcomes, URLs, and times before `run_nondet_unsafe`; closures contain no `self`. |
| MG-04 | Medium | Non-consequential coverage/code variation could reject the same listing result. | Independently recompute and compare the consequential listing `decision`; store coverage and codes for audit. |
| MG-05 | Low | Decoded JSON, malformed source bytes, and loose return wrappers needed hardening. | Canonicalize decoded inputs, safely decode bounded bytes, and require `gl.vm.Return`. |

## Residual risks

- A `LISTABLE` result means the specification is operationally resolvable; it
  is not a truth guarantee or legal review.
- Policy judgments may differ for genuinely ambiguous market wording, causing
  consensus to fail rather than listing automatically.
- HTTPS reachability does not prove evidence authority.
- DNS rebinding requires reviewed domains or an explicit allowlist.

## Verification evidence

- Pinned GenVM runner; GenVM lint and SDK validation pass.
- Standalone direct suite: 5 passed, including repeat review and three private
  URL rejection cases.
- StudioNet review finalized with `SUCCESS`, 3 agree / 2 idle, and no storage
  warning.
- Live state: `LISTABLE`, both outcomes covered, no ambiguity or manipulation
  flags.
- Bradbury status is tracked independently in its deployment manifest.

This is an engineering assessment, not formal verification or a financial or
legal guarantee.
