# Implementation Reference

## Pre-Implementation Check
Before editing, state:
- files or directories likely to change
- tests or checks to add or update
- verification command
- assumptions that could affect correctness

## Implementation Sequence
Prefer:
1. inspect or add focused regression coverage
2. implement the smallest change
3. run targeted tests
4. run broader verification when cheap
5. update status, handoff, or technical debt if needed

## Verification Signals
Good verification is executable:
- unit tests
- integration tests
- build or typecheck
- lint
- validation script
- reproducible manual command when automation is unavailable

## Handoff
Include:
- objective
- scope
- files changed
- assumptions
- decisions
- blockers
- next step recommendation
