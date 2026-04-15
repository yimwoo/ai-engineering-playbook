# Getting Started

## Purpose
This guide helps you adopt the playbook in a new or existing project repo.

## Minimum Setup
For a new project, start with:
- `PROJECT_CONSTITUTION.md`
- `CLAUDE.md`
- `architecture.md`
- `roadmap.md`
- `status.md`
- `technical-debt.md`

For larger projects, also add:
- `AGENTS.md`
- `modules/`
- `decisions/`
- `task-packets/`
- `handoffs/`

## First-Time Workflow
1. copy the relevant templates into your project repo
2. fill in the architecture and roadmap at a high level
3. define the current milestone
4. define the first few module boundaries
5. ask the agent to plan the milestone before coding
6. convert planned work into bounded tasks
7. require status updates and handoffs after meaningful work

## New Project vs Existing Project
### New Project
Start with architecture, roadmap, and module decomposition.

### Existing Project
Run a repo audit first. Do not blindly overwrite existing docs.

## First Prompt to Use
Use the orchestrator kickoff prompt in `prompts/orchestrator-kickoff.md`.
