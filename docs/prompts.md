# Prompts

This directory contains reusable prompts for different types of agent work.

## Prompt Types
- orchestrator kickoff
- architecture analysis
- implementation task
- review task
- repo audit
- status update
- design-change package
- roadmap refresh
- repo alignment
- module spec generation

## Guidance
Use the lightest prompt that still gives the agent enough context.
Do not load every file for every task.

## Recommended Starting Points
- New project planning: `prompts/orchestrator-kickoff.md`
- Existing repo analysis: `prompts/repo-audit.md`
- One bounded implementation task: `prompts/implementation-task.md`
- Architecture/design work: `prompts/architecture-analysis.md`
- Major roadmap or design shift: `prompts/design-change-package.md`
- Ongoing project state maintenance: `prompts/status-update.md`
