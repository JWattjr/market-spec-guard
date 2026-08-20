# GenLayer Portal submission

**Contribution type:** Builder → Intelligent Contracts  
**Title:** MarketSpec Guard  
**Contribution date:** August 20, 2026

## Notes / Description

Built and deployed an MIT-licensed MarketSpec Guard, a reusable pre-listing
GenLayer Intelligent Contract for prediction-market quality and safety. The
constructor freezes the question, 2-8 unique outcomes, public evidence URLs,
close time, and resolution time. Before participation begins, the leader and
validators independently review time-boundedness, outcome coverage, evidence
availability, ambiguity, resolvability, and manipulation risks. The custom
equivalence function independently recomputes and compares the consequential
LISTABLE/NEEDS_CLARIFICATION/REJECTED decision—not just response format—while
coverage, ambiguity codes, and manipulation flags remain audit metadata.
Private-network evidence is rejected, unavailable sources fail closed, and
terminal review is idempotent. Includes pinned GenVM source, validator tests,
security audit, test matrix, and finalized StudioNet verification records. It is a
listing policy primitive and does not accept stakes or funds.

## Evidence to add

1. GitHub Repository — https://github.com/JWattjr/market-spec-guard
2. GitHub File — https://github.com/JWattjr/market-spec-guard/blob/main/contracts/MarketSpecGuard.py
3. GitHub File — https://github.com/JWattjr/market-spec-guard/blob/main/tests/test_guard.py
4. GitHub File — https://github.com/JWattjr/market-spec-guard/blob/main/docs/SECURITY_AUDIT.md
5. GitHub File — https://github.com/JWattjr/market-spec-guard/blob/main/docs/TEST_MATRIX.md
6. GitHub File — https://github.com/JWattjr/market-spec-guard/blob/main/deployments/studionet.json
7. GitHub File — https://github.com/JWattjr/market-spec-guard/blob/main/docs/STUDIONET_VERIFICATION.md
8. GenLayer Explorer Contract — https://explorer-studio.genlayer.com/address/0x3923f85a0c070e5A523F689B9a200070e8617643
