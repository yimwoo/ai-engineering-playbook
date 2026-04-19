# Getting Started

## Purpose
This guide helps you adopt the playbook in a new or existing project repo.

## Choose a starting mode

### Mode 1: New project
Use this when you are starting from scratch and want an initial operating model before coding heavily.

Start with:
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

### Mode 2: Existing project
Use this when the codebase already exists and you want to introduce better structure without creating chaos.

Start with:
- an audit of current docs, architecture, and repo topology
- a keep/fix/merge/archive/superseded inventory
- a small alignment plan

Only then add:
- `PROJECT_CONSTITUTION.md`
- `CLAUDE.md`
- `status.md`

## First-Time Workflow
1. copy the relevant templates into your project repo
2. fill in architecture and roadmap at a high level
3. define the current milestone
4. define the first few module boundaries
5. ask the agent to plan the milestone before coding
6. convert planned work into bounded tasks
7. require status updates and handoffs after meaningful work

## Minimal Quickstart
If you want the smallest useful adoption path, do this:
1. copy `PROJECT_CONSTITUTION.md`, `CLAUDE.md`, and `status.md`
2. create a simple `architecture.md`
3. use `prompts/orchestrator-kickoff.md`
4. require `status.md` updates after meaningful tasks

## First Prompts to Use
- New project planning: `prompts/orchestrator-kickoff.md`
- Existing project audit: `prompts/repo-audit.md`
- Large repo or monorepo audit: `prompts/monorepo-audit.md`
- One implementation task: `prompts/implementation-task.md`
- Architecture change: `prompts/design-change-package.md`

## Rule of thumb
Do not start by generating every possible doc.
Start with the minimum structure that improves clarity, then add rigor as the project grows.
