# Frequently Asked Questions

## Do I need all of these docs from day one?
No.

Start with the smallest useful set:
- `PROJECT_CONSTITUTION.md`
- `CLAUDE.md`
- `architecture.md`
- `status.md`

Then add more structure only when the project complexity justifies it.

## Who should update `status.md`?
Usually the orchestrator agent or the implementation agent finishing a meaningful task.

The goal is not to keep a diary. The goal is to preserve the current operational state for the next session.

## Do I need `AGENTS.md` for solo development?
Not always.

If you are mostly using one agent session at a time, you can start without it.
Add it when:
- multiple sessions are involved
- you use parallel agent work
- you want clearer role separation between planning, implementation, and review

## Should I create architecture and roadmap at the beginning?
Yes, but only as initial versions.

They are living docs, not fixed forever. Define enough structure to guide work, then refine them as the system evolves.

## What if architecture or roadmap changes later?
Use a design-change package before making big changes.

This helps you:
- explain why change is needed
- assess impact
- compare options
- update docs intentionally
- then implement in bounded tasks

## When should I create an ADR?
Create an ADR when a decision affects:
- system boundaries
- data ownership
- API or event contracts
- security model
- deployment model
- scalability or reliability strategy

Do not create ADRs for every minor implementation detail.

## Should code agents write the docs, or should I?
Both.

A good pattern is:
1. human provides goals, constraints, and non-negotiables
2. agent drafts docs
3. human reviews important decisions
4. agent updates and maintains docs during execution

## Do I need plugins or MCP tools for this playbook?
No.

This playbook is intentionally tool-agnostic.
You can use it with Claude Code, Codex, or similar code agents.

Plugins can help, but they should not replace the repo as the source of truth.

## How do I use this in an existing codebase?
Do not blindly rewrite everything.

Start by:
- adding `PROJECT_CONSTITUTION.md`
- adding `CLAUDE.md`
- adding `status.md`
- running a repo audit
- aligning incrementally

## How much human-in-the-loop is enough?
Humans should stay involved for:
- product priorities
- major architecture decisions
- security/compliance decisions
- expensive or irreversible tradeoffs

Humans should not become a bottleneck for small local implementation decisions.

## What is the biggest mistake when using code agents on large projects?
Treating chat history as the project memory.

Large projects need repo-based memory:
- docs
- ADRs
- status
- task packets
- handoffs
- technical debt
