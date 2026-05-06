# AI Engineering Playbook Claude Code Plugin

## Purpose
This plugin packages AI Engineering Playbook workflows as focused Claude Code skills.

It is an optional adapter. The repo-based playbook files remain the source of truth:
- `PROJECT_CONSTITUTION.md`
- `CLAUDE.md`
- `AGENTS.md`
- `architecture.md`
- `roadmap.md`
- `status.md`
- `task-packets/`
- `handoffs/`
- `technical-debt.md`
- ADRs under `decisions/`

## Installation
From Claude Code, add this repository as a plugin marketplace, then install the plugin:

```text
/plugin marketplace add <path-or-git-url-to-this-repo>
/plugin install ai-engineering-playbook@ai-engineering-playbook
```

For a large or monorepo checkout, use sparse paths for:
- `.claude-plugin`
- `plugins/ai-engineering-playbook`

## Included Skills
- `adopting-playbook` - add or align AI Engineering Playbook files in a project
- `orchestrating-playbook-work` - start or resume governed work from repo memory
- `planning-playbook-tasks` - convert roadmap or design intent into bounded tasks
- `implementing-playbook-tasks` - execute one bounded task with tests and handoff
- `reviewing-playbook-work` - review output against playbook contracts and source-of-truth docs

## Portability Rule
Do not move durable project memory into plugin-only state. Use plugin skills to guide the agent, but keep decisions, status, task scope, and handoffs in ordinary repository files so the workflow still works with Claude Code, Codex, and other code agents.
