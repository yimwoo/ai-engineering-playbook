# Adoption Reference

## Adoption Levels
Use the lightest level that fits:

- lightweight: solo builders, MVPs, and small codebases
- standard: growing products with several modules or workstreams
- enterprise: long-lived systems, parallel human and AI work, architecture-sensitive delivery

## Minimum File Sets
Lightweight:
- `PROJECT_CONSTITUTION.md`
- `CLAUDE.md`
- `architecture.md`
- `status.md`

Standard:
- lightweight files
- `roadmap.md`
- `technical-debt.md`
- `modules/`
- `decisions/`

Enterprise:
- standard files
- `AGENTS.md`
- `repo-map.md`
- `task-packets/`
- `handoffs/`

## Existing Repo Migration
1. Audit current docs, source layout, and agent instructions.
2. Classify docs as keep, fix, merge, archive, or superseded.
3. Add the operating layer after the audit direction is clear.
4. Introduce module specs, ADRs, repo maps, task packets, and handoffs only where workflow complexity justifies them.
5. Update `status.md` with the current milestone and next safe action.

## Handoff Fields
For meaningful adoption work, produce:
- objective
- scope
- files changed
- assumptions
- decisions
- blockers
- next step recommendation
