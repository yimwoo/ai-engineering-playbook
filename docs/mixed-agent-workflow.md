# Mixed-Agent Workflow

## Purpose
This guide shows how to use multiple code agents together without splitting your project memory.

## Core Rule
Different agents may perform different tasks, but they should all work from the same repo-based source of truth.

That means all agents should rely on:
- `PROJECT_CONSTITUTION.md`
- `status.md`
- `architecture.md`
- `roadmap.md`
- ADRs
- task packets
- handoffs
- technical debt tracking

## A Practical Division of Labor
### Claude Code
Often strong for:
- architecture analysis
- roadmap/milestone planning
- decomposition
- design-change packages
- review summaries

### Codex
Often strong for:
- bounded implementation
- code edits
- tests
- focused refactors
- tighter execution loops

## Example Mixed Workflow
1. Use Claude Code to plan the milestone
2. Use Claude Code or another planning-oriented agent to draft task packets
3. Use Codex for implementation of a bounded task packet
4. Use either tool for review, but compare against the same acceptance criteria
5. Update `status.md` and create a handoff before switching sessions or tools

## Switching Rule
Before switching from one code agent to another, update:
- `status.md`
- the relevant task packet if scope changed
- technical debt if a shortcut was taken
- handoff notes for the next session

## Anti-Pattern
Do not let each tool invent its own parallel memory system.

## Goal
The tools may vary, but the workflow should remain coherent.
