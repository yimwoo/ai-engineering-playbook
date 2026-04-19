# Monorepo and Multi-Project Adoption

## Purpose
Extend the playbook for repos with many apps, services, packages, libraries, or nested subprojects.

## When to use this guide
Use this guide when the repo has:
- multiple deployable units
- shared libraries used by many teams
- app and package workspaces
- nested instruction files or subproject-specific rules
- generated, vendored, or externally mirrored code

## Add one more core artifact
In large repos, `architecture.md` is usually not enough on its own.

Add:
- `repo-map.md`

Use `repo-map.md` to describe the repo topology, major subprojects, entrypoints, ownership boundaries, and do-not-touch areas.

## Root docs vs local docs
Use root docs for global truth:
- `PROJECT_CONSTITUTION.md`
- `architecture.md`
- `roadmap.md`
- `status.md`
- root ADRs
- `repo-map.md`

Use local docs for subproject truth:
- local module or subproject contracts
- local verification commands
- local dependency notes
- local constraints for generated or regulated areas

Local docs should refine the root model, not replace it.

## What each subproject should make explicit
For each major subproject, capture:
- purpose
- owned code and owned data
- public interfaces
- upstream dependencies
- downstream consumers
- verification entrypoints
- constraints and do-not-touch areas

## Generated, vendored, and external code
Large repos often contain code that should be read differently than first-party application code.

Mark clearly:
- generated code
- vendored code
- mirrored external repos
- git submodules

Agents should know whether those areas are:
- editable
- update-only
- read-only
- owned by another team

## Recommended rollout for existing repos
1. run `prompts/monorepo-audit.md`
2. create `repo-map.md`
3. identify the 3-5 most critical subprojects
4. add local contracts only for those areas first
5. use cross-project task packets for risky changes
6. expand coverage gradually

## Common failure mode
Do not treat a monorepo as just a bigger single-project repo.

The missing information is often not feature behavior.
It is topology, ownership, verification entrypoints, and change radius.
