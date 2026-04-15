# Codex Adapter

## Purpose
This guide explains how to use AI Engineering Playbook with Codex while keeping the workflow portable.

## Where Codex is often strong
Codex often works well for:
- direct implementation tasks
- code editing and local changes
- narrower execution loops
- fast iteration on bounded tasks
- code transformation and focused refactors

## Where to be careful
Do not assume Codex will behave the same as Claude Code in:
- long-form planning depth
- architecture narrative quality
- documentation style
- memory continuity across sessions
- plugin or command compatibility with Claude-oriented setups

## Recommended Usage Pattern
### Best use cases
Use Codex for:
- bounded implementation tasks
- code changes tied to task packets
- tests and focused refactors
- reviewing diffs against acceptance criteria
- executing implementation after architecture has already been clarified

### Best workflow mapping
Map the playbook to Codex like this:
- `PROJECT_CONSTITUTION.md` -> generic operating rules
- `CLAUDE.md` -> can still be used as a general agent instruction file if no Codex-specific equivalent exists
- `status.md` -> restart context and current state
- `task packets` -> main execution input
- `handoffs` -> preserve continuity across Codex sessions
- `architecture.md` and ADRs -> stable design references

## What to keep portable
Because Claude-oriented commands or plugins may not carry over, keep these in repo docs instead:
- workflow rules
- design decisions
- task boundaries
- implementation acceptance criteria
- post-task summaries

## Suggested Codex strengths in a mixed workflow
A practical split is:
- Claude Code for planning and architecture-heavy reasoning
- Codex for bounded coding, tests, and implementation execution

That said, both tools should still be able to operate from the same repo memory and task model.

## Anti-Pattern
Do not put critical process knowledge only in Claude-specific commands or plugin behavior and then expect Codex to follow it.

## Safe Optimizations
Codex-specific helpers are fine if:
- they remain optional
- the generic prompt and document system still works
- important instructions remain in repo docs, not hidden tool config

## Recommended Prompts To Use First
- `prompts/implementation-task.md`
- `prompts/status-update.md`
- `prompts/review-task.md`
- `prompts/repo-audit.md`
