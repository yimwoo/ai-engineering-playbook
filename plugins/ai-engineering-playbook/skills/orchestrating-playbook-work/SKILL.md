---
name: orchestrating-playbook-work
description: Starts or resumes AI Engineering Playbook work from repo memory. Use when a user asks to continue work, check the latest handoff, select the next task, coordinate multiple agent roles, or maintain status across Claude Code, Codex, and similar code agents.
---

# Orchestrating Playbook Work

## Workflow
1. Read the repo source-of-truth files in priority order.
2. Find the latest status entry, task packet, and handoff.
3. Select exactly one bounded next action unless the user explicitly asks for broader planning.
4. Assign role responsibilities conceptually: orchestrator, architecture, implementation, and review.
5. End with a visible handoff for meaningful work.

## Source Priority
Prefer durable project artifacts over chat history or plugin memory:
1. `PROJECT_CONSTITUTION.md`
2. `AGENTS.md` and `CLAUDE.md`
3. `architecture.md`, ADRs, and module specs
4. `roadmap.md`
5. `status.md`
6. task packets
7. handoffs
8. notes and retrospectives

## Reference
Read `reference.md` for handoff discovery, role separation, and session output rules.
