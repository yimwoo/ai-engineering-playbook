# AI Engineering Playbook

> A practical, reusable workflow for AI-assisted software engineering, code agent orchestration, architecture planning, roadmap management, and long-lived software delivery.

AI Engineering Playbook helps teams and solo builders use code agents like Claude Code, Codex, and similar AI coding tools more effectively on real software projects — especially projects that are too large or long-lived for ad hoc prompting.

It provides:
- project governance templates for AI-assisted development
- practical prompts for planning, architecture, implementation, review, repo audits, and documentation audits
- starter kits for lightweight, standard, and enterprise-scale adoption
- examples for new projects and existing codebase migration
- a document-driven operating model for large-scale software development with code agents
- a tool-agnostic approach that works across Claude Code, Codex, and similar code agents

---

## Why use this playbook?

AI coding agents are strong at:
- generating code quickly
- drafting docs
- refactoring bounded areas
- reviewing code
- analyzing impact in a defined scope

But they often struggle with large-scale software development because of:
- context window limits
- weak long-term memory across sessions
- architecture drift
- unclear milestones and ownership
- parallel work collisions
- hidden technical debt
- ambiguous human-in-the-loop workflows

This repository gives you a practical system to address those problems.

It is intentionally designed to stay useful across different code agents instead of binding your workflow to one vendor-specific tool surface.

---

## What problem does this solve?

This repo is designed for teams and builders asking questions like:
- How do I use code agents for large software projects instead of just small demos?
- How do I keep architecture, roadmap, and implementation aligned across sessions?
- How do I avoid losing project memory when context windows reset?
- How do I reduce endless clarifying questions from code agents?
- How do I let humans stay in the loop without becoming the bottleneck?
- How do I manage big design changes like scalability, failover, observability, or design v2?

---

## Quick navigation

- [Overview](docs/overview.md)
- [Getting Started](docs/getting-started.md)
- [Operating Model](docs/operating-model.md)
- [Source of Truth and Doc Lifecycle](docs/source-of-truth-and-doc-lifecycle.md)
- [Prompts](docs/prompts.md)
- [FAQ](docs/faq.md)
- [Tool-Agnostic Principle](docs/tool-agnostic-principle.md)
- [Daily Use and Continuous Improvement](docs/daily-use-and-improvement.md)
- [Daily Path](docs/daily-path.md)
- [Mixed-Agent Workflow](docs/mixed-agent-workflow.md)
- [Workflow Diagrams](docs/workflow-diagrams.md)
- [Mermaid Workflow Diagrams](docs/workflow-diagrams-mermaid.md)
- [Status Update Protocol](docs/status-update-protocol.md)
- [Design Change Packages](docs/design-change-packages.md)
- [Adopting in Existing Repos](docs/adopting-in-existing-repos.md)
- [Monorepo and Multi-Project Adoption](docs/monorepo-and-multi-project-adoption.md)
- [Messy Existing Repo Rescue Guide](docs/messy-existing-repo-rescue.md)
- [GitHub Metadata Suggestions](docs/github-metadata-suggestions.md)

---

## Choose your adoption level

### 1. Lightweight starter
Best for:
- solo developers
- MVPs
- smaller codebases
- fast iteration

Use the starter kit in:
- [`starter-kits/lightweight/`](starter-kits/lightweight/)

Recommended files:
- `PROJECT_CONSTITUTION.md`
- `CLAUDE.md`
- `architecture.md`
- `status.md`

### 2. Standard starter
Best for:
- growing products
- evolving architecture
- several modules or workstreams

Use the starter kit in:
- [`starter-kits/standard/`](starter-kits/standard/)

Recommended files:
- `PROJECT_CONSTITUTION.md`
- `CLAUDE.md`
- `architecture.md`
- `roadmap.md`
- `status.md`
- `technical-debt.md`
- `modules/`
- `decisions/`

### 3. Enterprise starter
Best for:
- large-scale software projects
- enterprise software delivery
- long-lived codebases
- parallel human and AI agent workflows
- architecture-sensitive systems

Use the starter kit in:
- [`starter-kits/enterprise/`](starter-kits/enterprise/)

Recommended files:
- `PROJECT_CONSTITUTION.md`
- `CLAUDE.md`
- `AGENTS.md`
- `architecture.md`
- `repo-map.md` for monorepos or many-subproject repos
- `roadmap.md`
- `status.md`
- `technical-debt.md`
- `modules/`
- `decisions/`
- `task-packets/`
- `handoffs/`

---

## Quickstart for AI-assisted software development

### New project setup
1. pick a starter kit
2. copy the starter kit files into your project repo
3. define the initial architecture and current milestone
4. create or update `status.md`
5. ask the code agent to plan work before coding
6. convert planned work into bounded task packets
7. require status updates and handoffs after meaningful tasks

### Existing codebase adoption
1. start with an audit of current docs, architecture, and repo topology
2. use [`prompts/repo-audit.md`](prompts/repo-audit.md), [`prompts/repo-docs-audit.md`](prompts/repo-docs-audit.md), or [`prompts/monorepo-audit.md`](prompts/monorepo-audit.md) depending on whether the main issue is broad repo understanding, agent-facing docs, or large-repo topology
3. classify existing docs into keep, fix, merge, archive, or superseded
4. add `PROJECT_CONSTITUTION.md`, `CLAUDE.md`, and `status.md` as the new operating layer only after the audit direction is clear
5. align incrementally instead of rewriting everything at once
6. add module specs, ADRs, repo maps, and task packets only where justified

---

## What is inside this repository?

### `templates/`
Copyable templates for:
- architecture docs
- repo maps
- roadmap docs
- status tracking
- technical debt tracking
- module specs
- ADRs
- task packets
- handoffs
- design-change packages

### `prompts/`
Reusable prompts for:
- orchestrator kickoff
- architecture analysis
- implementation tasks
- review tasks
- repo audits
- repo documentation audits
- monorepo audits
- repo alignment
- repo self-improvement
- status updates
- roadmap refresh
- design-change packages
- module spec generation

### `starter-kits/`
Ready-to-copy starter bundles for:
- lightweight adoption
- standard adoption
- enterprise-style adoption

### `adapters/`
Tool-specific mapping notes for:
- Claude Code
- Codex
- new code agents via a generic onboarding checklist
- agent evaluation via a reusable scorecard

These adapter docs explain how to use the same playbook with different agents without making the workflow depend on one tool.

### `examples/`
Worked examples for:
- startup-lightweight projects
- enterprise-product projects
- existing repo migration

### `notes/`, `patterns/`, `retros/`, `experiments/`
A personal operating layer for:
- weekly learning logs
- tool comparison notes
- reusable patterns
- retrospectives
- lightweight experiments before promotion into the core playbook

### `docs/designs/`, `docs/research/`
Use these when evaluating structural changes or capturing deeper analysis before promoting stable guidance into the main docs.

### `docs/`
Reference guides for:
- getting started
- operating model
- prompt usage
- FAQ
- tool-agnostic workflow principles
- daily use and continuous improvement
- status updates
- design-change packages
- migration/adoption guidance
- messy existing repo rescue
- GitHub metadata and discoverability suggestions

---

## Core operating model

Do not treat a code agent as a single all-knowing engineer.

Treat it as a bounded contributor inside a governed project system with:
- source-of-truth docs
- explicit architecture decisions
- status tracking
- milestone planning
- task packets
- handoff discipline
- technical debt visibility
- design-change packages for large changes

---

## Recommended workflow

1. define architecture and current roadmap
2. break work into milestones
3. turn milestone work into bounded tasks
4. ask the agent to read the relevant docs first
5. require status and handoff updates after meaningful work
6. track shortcuts in `technical-debt.md`
7. use design-change packages for architecture or roadmap changes

---

## Common use cases

This playbook is especially helpful for:
- AI-assisted software engineering
- code agent workflows for large projects
- enterprise software architecture planning
- multi-session coding with Claude Code or Codex
- roadmap-driven software delivery
- existing repo cleanup and governance alignment
- scaling from prototype to production system

---

## Suggested starting points

If you are:
- starting a new project → read [Getting Started](docs/getting-started.md)
- working in a messy existing repo → read [Messy Existing Repo Rescue Guide](docs/messy-existing-repo-rescue.md) and use the [repo audit prompt](prompts/repo-audit.md) or [repo docs audit prompt](prompts/repo-docs-audit.md)
- planning the next milestone → use [orchestrator kickoff prompt](prompts/orchestrator-kickoff.md)
- making a big architecture or roadmap change → use [design-change package prompt](prompts/design-change-package.md)
- working across Claude Code and Codex → read [Mixed-Agent Workflow](docs/mixed-agent-workflow.md), [adapters/claude-code.md](adapters/claude-code.md), and [adapters/codex.md](adapters/codex.md)
- evaluating a new code agent → use [adapters/generic-agent-checklist.md](adapters/generic-agent-checklist.md) and [adapters/agent-evaluation-scorecard.md](adapters/agent-evaluation-scorecard.md)
- trying to use this repo day-to-day without overhead → read [Daily Path](docs/daily-path.md)
- reviewing your first real use of the playbook → read [First Real-Use Retrospective Guide](docs/first-real-use-retrospective-guide.md)

---

## FAQ

See [docs/faq.md](docs/faq.md) for answers to common questions about:
- architecture changes
- roadmap changes
- status ownership
- required docs
- human-in-the-loop workflows
- plugins and tools
- existing repo adoption

---

## License

MIT
