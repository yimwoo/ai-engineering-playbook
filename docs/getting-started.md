# Getting Started

## Purpose
This guide helps you adopt the playbook in a new or existing project repo.

## Choose a starting mode

### Mode 1: New project
Use this when you are starting from scratch and want an initial operating model before coding heavily.

Pick one starter kit first, then copy that exact file set into your repo:
- lightweight: `starter-kits/lightweight/` (`PROJECT_CONSTITUTION.md`, `CLAUDE.md`, `architecture.md`, `status.md`)
- standard: `starter-kits/standard/` (lightweight plus `roadmap.md`, `technical-debt.md`, `modules/`, `decisions/`)
- enterprise: `starter-kits/enterprise/` (standard plus `AGENTS.md`, `repo-map.md`, `task-packets/`, `handoffs/`)

If unsure, start with lightweight and add structure only when coordination or architecture complexity demands it.

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
1. pick a starter kit (`lightweight`, `standard`, or `enterprise`)
2. copy that starter kit into your project repo
3. fill in architecture and roadmap at a high level (if your selected starter includes `roadmap.md`)
4. define the current milestone
5. define the first few module boundaries (if your selected starter includes `modules/`)
6. ask the agent to plan the milestone before coding
7. convert planned work into bounded tasks
8. require status updates and handoffs after meaningful work

## Minimal Quickstart
If you want the smallest useful adoption path, do this:
1. copy `starter-kits/lightweight/` into your project repo
2. fill in a simple `architecture.md`
3. use `prompts/orchestrator-kickoff.md`
4. require `status.md` updates after meaningful tasks

## First Prompts to Use
- New project planning: `prompts/orchestrator-kickoff.md`
- Existing project audit: `prompts/repo-audit.md`
- Existing project doc and workflow audit: `prompts/repo-docs-audit.md`
- Large repo or monorepo audit: `prompts/monorepo-audit.md`
- One implementation task: `prompts/implementation-task.md`
- Architecture change: `prompts/design-change-package.md`

## Rule of thumb
Do not start by generating every possible doc.
Start with the minimum structure that improves clarity, then add rigor as the project grows.
