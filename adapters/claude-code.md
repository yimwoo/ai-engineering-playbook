# Claude Code Adapter

## Purpose
This guide explains how to use AI Engineering Playbook with Claude Code while keeping the workflow portable.

## Where Claude Code is strong
Claude Code often works well for:
- structured planning
- architecture discussion
- longer-form analysis
- documentation drafting
- multi-step decomposition
- implementation with good narrative explanation

## Where to be careful
Do not rely too heavily on Claude Code-specific behavior such as:
- proprietary memory assumptions
- tool-specific command habits
- plugin-only workflows as the source of truth
- long chat continuity as the main project memory

## Recommended Usage Pattern
### Best use cases
Use Claude Code for:
- milestone planning
- architecture analysis
- design-change package drafting
- repo audit work
- implementation tasks with strong context reading requirements
- review and documentation refinement

### Best workflow mapping
Map the playbook to Claude Code like this:
- `PROJECT_CONSTITUTION.md` -> core operating rules
- `CLAUDE.md` -> Claude-specific working instructions
- `status.md` -> session restart context
- `task packets` -> bounded implementation units
- `handoffs` -> continuity across sessions
- `ADRs` and `architecture.md` -> long-term design memory

## What to keep portable
Even if Claude Code supports richer workflows, keep these portable:
- system design decisions
- roadmap and milestone state
- technical debt tracking
- task boundaries
- session summaries

## Suggested Claude Code strengths in a mixed workflow
A practical split is:
- Claude Code for planning, architecture, doc drafting, and complex decomposition
- Codex or other agents for more direct implementation or alternate execution style where helpful

## Anti-Pattern
Do not design the repo so that understanding the project depends on reading prior Claude Code chat sessions.

## Safe Optimizations
Claude Code-specific prompt tuning is fine if:
- it stays inside `CLAUDE.md` or adapter notes
- the base repo workflow still works with another tool
- the repo artifacts remain the primary memory system

## Recommended Prompts To Use First
- `prompts/orchestrator-kickoff.md`
- `prompts/architecture-analysis.md`
- `prompts/design-change-package.md`
- `prompts/review-task.md`
