# AI Engineering Playbook

A practical, reusable operating model for using code agents on large-scale software projects.

This repository provides:
- reusable governance docs for AI-assisted development
- templates for architecture, roadmap, status, ADRs, task packets, handoffs, and design changes
- prompts for orchestrator, architecture, implementation, review, and repo-audit workflows
- guidance for adopting a document-driven workflow in new or existing repos
- examples for lightweight and enterprise-style project setups

---

## Why this exists

Code agents are very effective for:
- bounded implementation tasks
- drafting documentation
- impact analysis
- refactoring
- reviews
- decomposition of complex work

But they often struggle with large-scale software development when projects involve:
- evolving architecture
- many modules and submodules
- roadmap changes
- cross-session memory loss
- parallel work
- context window limits
- hidden shortcuts and untracked technical debt

This playbook addresses those problems with a document-driven operating model.

---

## Core idea

Do not treat a code agent as a single all-knowing engineer.

Instead, treat it as a bounded contributor operating inside a governed project system with:
- source-of-truth docs
- explicit architecture decisions
- milestone planning
- status tracking
- task packets
- handoff discipline
- design-change packages

---

## Who this is for

This playbook is useful for:
- solo builders using Claude Code, Codex, or similar tools
- small teams building ambitious systems
- engineering leads introducing AI-assisted development practices
- teams managing architecture drift and context fragmentation
- enterprise software projects with many modules and long timelines

---

## Choose your adoption level

### Level 1: Lightweight
Best for:
- early-stage projects
- solo builders
- small codebases

Start with:
- `PROJECT_CONSTITUTION.md`
- `CLAUDE.md`
- `architecture.md`
- `status.md`

### Level 2: Standard
Best for:
- growing products
- multiple workstreams
- evolving architecture

Add:
- `roadmap.md`
- `technical-debt.md`
- `modules/`
- `decisions/`

### Level 3: Enterprise-style
Best for:
- large or long-lived systems
- parallel agent/human workflows
- architecture-sensitive projects

Also add:
- `AGENTS.md`
- `task-packets/`
- `handoffs/`
- design-change packages
- fuller module specs and ADR coverage

---

## Quickstart

### For a new project
1. Copy the templates you need from `templates/`
2. Create an initial architecture baseline
3. Create an initial roadmap and current milestone
4. Create `status.md`
5. Ask the agent to plan the milestone before coding
6. Convert the plan into bounded task packets
7. Require status updates and handoffs after meaningful work

### For an existing project
1. Start with `PROJECT_CONSTITUTION.md`, `CLAUDE.md`, and `status.md`
2. Run a repo audit using `prompts/repo-audit.md`
3. Identify current architecture, gaps, stale docs, and drift
4. Introduce module specs, ADRs, and task packets incrementally
5. Avoid blindly rewriting all existing docs at once

---

## Repository layout

### `templates/`
Starter files you can copy into a project repo:
- `CLAUDE.md`
- `AGENTS.md`
- `PROJECT_CONSTITUTION.md`
- `architecture.md`
- `roadmap.md`
- `status.md`
- `technical-debt.md`
- module spec template
- ADR template
- task packet template
- handoff template
- design-change package template

### `prompts/`
Reusable prompts for:
- milestone planning
- architecture analysis
- implementation tasks
- review
- status updates
- design-change packages
- roadmap refresh
- existing repo audits
- repo alignment
- module spec generation

### `docs/`
Guides for:
- getting started
- operating model
- status update protocol
- handling architecture and roadmap changes
- adopting this system in existing repos
- FAQs and overview

### `examples/`
Example layouts for:
- lightweight startup projects
- enterprise-style projects
- adopting the playbook into an existing codebase

---

## Recommended minimum doc set

In your project repo, create at least:

1. `PROJECT_CONSTITUTION.md`
2. `CLAUDE.md`
3. `architecture.md`
4. `roadmap.md` or a simpler milestone plan
5. `status.md`
6. `technical-debt.md`

For larger projects, also add:
7. `modules/` for critical module specs
8. `decisions/` for ADRs
9. `AGENTS.md`
10. `task-packets/`
11. `handoffs/`

---

## Minimum workflow

1. Define the initial architecture and roadmap
2. Break work into milestones
3. Convert milestone work into bounded task packets
4. Ask the code agent to read the relevant docs first
5. Require status updates and handoffs after meaningful work
6. Track shortcuts in technical debt
7. Use design-change packages for architecture or roadmap changes

---

## Design principles

- docs are memory, not chats
- bounded tasks beat broad autonomy
- architecture is a first-class artifact
- shortcuts must be visible
- humans decide high-leverage tradeoffs
- agents execute, draft, analyze, and review within constraints
- status and handoffs keep sessions coherent
- roadmap and architecture are living documents

---

## Start here

- [Overview](docs/overview.md)
- [Getting Started](docs/getting-started.md)
- [Operating Model](docs/operating-model.md)
- [Prompts](docs/prompts.md)
- [Status Update Protocol](docs/status-update-protocol.md)
- [Design Change Packages](docs/design-change-packages.md)
- [Adopting in Existing Repos](docs/adopting-in-existing-repos.md)

---

## Suggested project types

This playbook is especially effective for:
- SaaS platforms
- internal enterprise systems
- multi-module backend systems
- AI platforms
- workflow and orchestration systems
- long-lived codebases with multiple parallel efforts

---

## License

MIT
