---
name: implementing-playbook-tasks
description: Executes one bounded AI Engineering Playbook task with implementation, tests, documentation updates when needed, and handoff. Use when a user asks to implement a task packet, continue a milestone item, or make a code change governed by status.md, roadmap.md, or handoff notes.
---

# Implementing Playbook Tasks

## Workflow
1. Confirm the selected task and current repo state.
2. Identify files to change, tests to add or update, and verification commands.
3. Make the smallest useful implementation change.
4. Update docs only when they need to reflect the implementation.
5. Run targeted verification, then broader cheap checks if available.
6. End with a handoff that names files changed, assumptions, decisions, blockers, and next step.

## Constraints
- Do not turn an implementation task into broad replanning.
- Do not do drive-by refactors.
- Do not claim completion without verification evidence.
- Do not rely on chat history as project memory.

## Reference
Read `reference.md` for implementation sequencing, verification, and handoff checks.
