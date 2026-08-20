# MarketSpec Guard

A pre-listing GenLayer consensus gate for prediction-market specifications.

It freezes the market question, 2-8 outcomes, evidence URLs, close time, and
resolution time. Before participation begins, validators independently review
whether the question is bounded and resolvable, outcomes are covered, public
evidence exists, and manipulation risks are absent. The result is `LISTABLE`,
`NEEDS_CLARIFICATION`, or `REJECTED`.

## GenLayer-native decision

This is an on-chain rule-enforcement primitive: no platform moderator alone can
approve a vague or manipulable market. Validators independently recompute and
compare the consequential listing decision. Outcome coverage, ambiguity codes,
and manipulation flags remain stored as audit metadata.

## Lifecycle and API

- Deploy in `PENDING` with a question, outcomes, sources, close time, and later
  resolution time.
- Call `review()` before market close. The terminal gate is `LISTABLE`,
  `NEEDS_CLARIFICATION`, or `REJECTED`; repeat review is idempotent.
- Read the decision and diagnostics with `get_state()`.
- A market platform should list only after the review transaction is final.

## Live evidence

- [StudioNet contract](https://explorer-studio.genlayer.com/address/0x3923f85a0c070e5A523F689B9a200070e8617643)
- The finalized deployment, live review, state, source-hash match, and receipt
  identifiers are recorded in `deployments/studionet.json` and
  `docs/STUDIONET_VERIFICATION.md`.

## Verify

```powershell
python -m pip install -r requirements.txt
genvm-lint check contracts/MarketSpecGuard.py
pytest tests -v
```

See `docs/SECURITY_AUDIT.md`, `docs/TEST_MATRIX.md`, and
`PORTAL_SUBMISSION.md` for reviewer evidence.
