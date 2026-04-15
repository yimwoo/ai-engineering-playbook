# AI Engineering Playbook

A practical workflow for using code agents on large-scale software projects.

This repository provides:
- reusable project governance docs
- templates for architecture, roadmap, status, ADRs, task packets, and handoffs
- prompts for orchestrator, architecture, implementation, and review sessions
- guidance for working with code agents across long-lived, complex software delivery cycles

## Why this exists

Code agents are very effective for:
- bounded implementation tasks
- drafting docs
- impact analysis
- refactoring
- reviews
- structured decomposition

But they often struggle with large-scale software development when projects involve:
- evolving architecture
- many modules and submodules
- roadmap changes
- cross-session memory loss
- parallel work
- context window limits
- hidden shortcuts and untracked technical debt

This playbook addresses those problems with a document-driven operating model.

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

## What’s in this repo

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
- existing repo audits

### `docs/`
Guides for:
- getting started
- operating model
- updating status
- handling architecture and roadmap changes
- adopting this system in existing repos

### `examples/`
Example layouts for:
- lightweight startup projects
- enterprise-style projects
- adopting the playbook into an existing codebase

## Who this is for

This playbook is useful for:
- solo builders using Claude Code / Codex / similar tools
- small teams building ambitious systems
- engineering leads introducing AI-assisted development practices
- teams managing architecture drift and context fragmentation
- enterprise software projects with many modules and long timelines

## Recommended usage

In your project repo, create a minimum doc set:

1. `PROJECT_CONSTITUTION.md`
2. `CLAUDE.md`
3. `architecture.md`
4. `roadmap.md`
5. `status.md`
6. `modules/` for critical modules
7. `decisions/` for ADRs
8. `technical-debt.md`

Then use the prompts in this repo to:
- plan milestones
- run bounded implementation tasks
- review work
- update docs
- manage architecture changes
- handle large design transitions safely

## Minimum workflow

1. Define the initial architecture and roadmap
2. Break work into milestones
3. Convert milestone work into bounded task packets
4. Ask the code agent to read the relevant docs first
5. Require status updates and handoffs after meaningful work
6. Track shortcuts in technical debt
7. Use design-change packages for architecture or roadmap changes

## Design principles

- docs are memory, not chats
- bounded tasks beat broad autonomy
- architecture is a first-class artifact
- shortcuts must be visible
- humans decide high-leverage tradeoffs
- agents execute, draft, analyze, and review within constraints
- status and handoffs keep sessions coherent
- roadmap and architecture are living documents

## Start here

- [Getting Started](docs/getting-started.md)
- [Operating Model](docs/operating-model.md)
- [Prompts](docs/prompts.md)
- [Adopting in Existing Repos](docs/adopting-in-existing-repos.md)

## Suggested project types

This playbook is especially effective for:
- SaaS platforms
- internal enterprise systems
- multi-module backend systems
- AI platforms
- workflow and orchestration systems
- long-lived codebases with multiple parallel efforts

## License

MIT
