# MarketSpec Guard

A pre-listing GenLayer consensus gate for prediction-market specifications.

It freezes the market question, 2-8 outcomes, evidence URLs, close time, and
resolution time. Before participation begins, validators independently review
whether the question is bounded and resolvable, outcomes are covered, public
evidence exists, and manipulation risks are absent. The result is `LISTABLE`,
`NEEDS_CLARIFICATION`, or `REJECTED`.

## GenLayer-native decision

This is an on-chain rule-enforcement primitive: no platform moderator alone can
approve a vague or manipulable market. Validators compare the decision,
covered-outcome set, ambiguity codes, and manipulation flags.

## Verify

```powershell
python -m pip install -r requirements.txt
genvm-lint check contracts/MarketSpecGuard.py
pytest tests -v
```

See `docs/SECURITY_AUDIT.md`, `docs/TEST_MATRIX.md`, and
`PORTAL_SUBMISSION.md` for reviewer evidence.
