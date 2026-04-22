# Prompts

This directory contains reusable prompts for different types of agent work.

## Prompt Types
- orchestrator kickoff
- architecture analysis
- implementation task
- review task
- repo audit
- repo docs audit
- monorepo audit
- status update
- design-change package
- roadmap refresh
- repo alignment
- module spec generation
- repo self-improvement

## Guidance
Use the lightest prompt that still gives the agent enough context.
Do not load every file for every task.

## Recommended Starting Points
- New project planning: `prompts/orchestrator-kickoff.md`
- Existing repo analysis: `prompts/repo-audit.md`
- Existing repo doc and workflow audit: `prompts/repo-docs-audit.md`
- Large repo or monorepo analysis: `prompts/monorepo-audit.md`
- One bounded implementation task: `prompts/implementation-task.md`
- Architecture/design work: `prompts/architecture-analysis.md`
- Major roadmap or design shift: `prompts/design-change-package.md`
- Ongoing project state maintenance: `prompts/status-update.md`
- Dogfooding this repo or another playbook repo: `prompts/repo-self-improvement.md`

## When to use the docs-focused audit
Use `prompts/repo-docs-audit.md` when the main problem is not source code quality but repo usability for agents, especially:
- stale or overlapping agent-facing docs
- unclear onboarding or start-here paths
- too much repeated context loading across sessions
- worktree confusion or parallel-agent workflow friction
- missing repo maps, handoff templates, or doc ownership rules

Use `prompts/repo-audit.md` when you need the broader architecture-plus-docs view.
Use `prompts/monorepo-audit.md` when repo topology, ownership, and verification scope are the main risks.
