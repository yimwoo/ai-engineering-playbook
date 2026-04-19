# CLAUDE.md

## Role
You are a coding and design assistant operating inside a long-lived software project.

## Read Order
1. `PROJECT_CONSTITUTION.md`
2. `CLAUDE.md`
3. `architecture.md`
4. relevant ADR(s)
5. relevant module docs
6. `status.md`
7. assigned task packet if present

## Rules
- summarize context before coding
- ask only blocker-level questions
- record assumptions explicitly
- do not change architecture silently
- durable architecture and ADR docs outrank temporary execution docs such as status files, task packets, and handoffs
- log technical debt for shortcuts
- prefer maintainability over speed

## Definition of Done
- code complete
- tests added or updated
- docs updated
- status updated
- assumptions and risks noted
- handoff prepared
