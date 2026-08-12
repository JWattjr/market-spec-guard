# GenLayer Portal submission

**Contribution type:** Builder → Intelligent Contracts  
**Title:** MarketSpec Guard  
**Contribution date:** Use the actual date of the submitted release.

## Notes / Description

Built and deployed an MIT-licensed MarketSpec Guard, a reusable pre-listing
GenLayer Intelligent Contract for prediction-market quality and safety. The
constructor freezes the question, 2-8 unique outcomes, public evidence URLs,
close time, and resolution time. Before participation begins, the leader and
validators independently review time-boundedness, outcome coverage, evidence
availability, ambiguity, resolvability, and manipulation risks. The custom
equivalence function compares LISTABLE/NEEDS_CLARIFICATION/REJECTED, covered
outcome IDs, ambiguity codes, and manipulation flags—not just response format.
Private-network evidence is rejected, unavailable sources fail closed, and
terminal review is idempotent. Includes pinned GenVM source, validator tests,
security audit, test matrix, and StudioNet/Bradbury deployment records. It is a
listing policy primitive and does not accept stakes or funds.

## Evidence to add

1. GitHub Repository — replace with the private repository URL.
2. GitHub File — `contracts/MarketSpecGuard.py`.
3. GitHub File — `tests/test_guard.py`.
4. GitHub File — `docs/SECURITY_AUDIT.md`.
5. GitHub File — `docs/TEST_MATRIX.md`.
6. GitHub File — `deployments/studionet.json`.
7. GitHub File — `deployments/bradbury.json`.
8. GenLayer Explorer Contract — replace with the finalized Bradbury address URL.
