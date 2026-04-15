# Task Packet: Auth Baseline

## Task ID
TASK-001

## Objective
Implement the first authentication and authorization baseline.

## Scope
- login flow skeleton
- auth guard or middleware
- basic role enforcement hooks

## Out of Scope
- SSO
- advanced org hierarchy
- audit analytics

## Required Reading
- PROJECT_CONSTITUTION.md
- CLAUDE.md
- status.md
- modules/auth.md
- ADR-001-architecture-style.md

## Constraints
- do not change architecture silently
- keep auth logic separate from core business logic

## Acceptance Criteria
- a protected route or service path exists
- unauthorized access is rejected
- tests cover the critical path
- docs are updated

## Deliverables
- code
- tests
- doc updates
- handoff
