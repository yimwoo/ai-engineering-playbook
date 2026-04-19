# Source of Truth and Doc Lifecycle

## Purpose
Define how documents relate to each other so humans and AI agents do not follow conflicting instructions.

## Core rule
Durable architecture and governance docs outrank temporary execution docs.

That means a stale status file, task packet, or handoff should not silently override the constitution, architecture, ADRs, or explicit module or subproject contracts.

## Recommended precedence
1. `PROJECT_CONSTITUTION.md`
2. `architecture.md`
3. ADRs in `decisions/`
4. `repo-map.md` and subproject-local contract docs
5. `roadmap.md`
6. `status.md`
7. task packets
8. handoffs
9. notes, experiments, and retros

## How to resolve conflicts
- If `status.md` conflicts with architecture or an ADR, fix `status.md`.
- If a task packet conflicts with architecture or an ADR, stop and resolve the design mismatch before coding.
- If a local subproject doc conflicts with the root constitution, the root constitution wins.
- If a local subproject doc conflicts with the root architecture outside its own boundary, update the docs before proceeding.

## Existing repo migration rule
Do not create a second source of truth by accident.

When adopting this playbook in an existing repo:
1. audit current docs first
2. classify docs as keep, fix, merge, archive, or superseded
3. add the new operating layer only after you know what it is replacing
4. mark older docs clearly if they are no longer canonical

## Superseded doc pattern
When an older doc is kept for history but should no longer guide implementation, mark it clearly near the top:

```md
> Status: Superseded by `docs/new-canonical-doc.md`
> Last reviewed: YYYY-MM-DD
> Reason: This file is retained for historical context only.
```

## Practical advice
- Prefer small canonical docs over large generated overviews.
- Do not keep two “current architecture” docs alive at the same time.
- If a doc is only exploratory, keep it in research, design, notes, or experiments rather than mixing it into the canonical layer.
