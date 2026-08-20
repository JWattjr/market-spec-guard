# StudioNet verification

Verification date: 2026-08-20  
Network: StudioNet (chain ID 61999)  
CLI: 0.39.2

## Contract and transactions

- Contract: `0x3923f85a0c070e5A523F689B9a200070e8617643`
- Explorer: https://explorer-studio.genlayer.com/address/0x3923f85a0c070e5A523F689B9a200070e8617643
- Deployment transaction: `0xae55234fb95c30fd3bc96693721316cda71c2f2b358e8474d2e93cca351c85cc`
- Live review transaction: `0xa84cb9095c25fe362ae1dc42062fa3d7da95b420e891be8b66aeb9c448f6a88b`

Both transactions are `FINALIZED` and executed successfully. The consensus
result is `MAJORITY_AGREE` with three agree votes; two validators became idle
after quorum was reached.

## Source and schema

- Repository source SHA-256: `2cd095e2d226c2e54a2eb1ebf4e69e2a21ecc0b80a4f97d7cf751742ab197673`
- StudioNet source SHA-256: `2cd095e2d226c2e54a2eb1ebf4e69e2a21ecc0b80a4f97d7cf751742ab197673`
- Exact source match: yes
- StudioNet schema retrieval: succeeded

## Current state

- Status: `LISTABLE`
- Attempts: 1
- Covered outcomes: `NO`, `YES`
- Ambiguity codes: none
- Manipulation flags: none

The standalone repository suite passed 5 tests on 2026-08-20. GenVM AST safety
lint passed. SDK semantic lint could not run because the current linter artifact
omits the contract's pinned runner tar; this is a toolchain packaging limitation.
