---
name: adopting-playbook
description: Adds or aligns AI Engineering Playbook artifacts in a repository. Use when a user wants to adopt the playbook, choose a starter-kit level, migrate an existing repo, or set up PROJECT_CONSTITUTION.md, CLAUDE.md, status.md, roadmap.md, task packets, handoffs, or related governance docs.
---

# Adopting Playbook

## Workflow
1. Identify whether the repository is new, lightweight, standard, enterprise, or a messy existing repo.
2. Inspect current agent-facing files before proposing additions.
3. Choose the smallest adoption level that covers the repo's actual coordination needs.
4. Add or align durable repo files, not hidden tool state.
5. Leave the next agent with a visible status update or handoff.

## Constraints
- Do not introduce every playbook artifact by default.
- Do not rewrite existing project docs wholesale when a smaller alignment patch is enough.
- Keep Claude Code-specific instructions inside `CLAUDE.md`, this plugin, or adapter notes.
- Keep cross-agent rules in portable repository files.

## Reference
Read `reference.md` for adoption levels, required files, and migration checks.
