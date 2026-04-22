# Adopting in Existing Repos

## Principle
Do not blindly force a new documentation structure onto an existing codebase.

First:
- analyze current architecture
- analyze current docs
- identify conflicts, gaps, and stale guidance
- propose a right-sized alignment plan

## Recommended Sequence
1. audit current docs, architecture, and repo topology
2. classify existing docs as keep, fix, merge, archive, or superseded
3. define a right-sized alignment plan
4. add `PROJECT_CONSTITUTION.md`, `CLAUDE.md`, and `status.md` as the new operating layer
5. map existing structure to this playbook
6. add ADRs, module specs, repo maps, and task packets incrementally

## Which audit prompt to start with
- Use `prompts/repo-audit.md` for a general existing-repo audit.
- Use `prompts/repo-docs-audit.md` when the biggest problem is agent-facing docs, onboarding flow, repeated-session usability, or workflow clarity.
- Use `prompts/monorepo-audit.md` when repo topology, ownership boundaries, or multi-subproject verification scope are the main risks.

## Rule
Align to the operating model, not necessarily to identical folder names.

## Source-of-Truth Rule
Do not let newly added governance docs silently compete with existing docs.
When a newer doc replaces an older one, mark the older doc clearly as superseded and point to the new canonical source.
