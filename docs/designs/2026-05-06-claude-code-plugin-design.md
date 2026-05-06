# Claude Code Plugin Design

## Objective
Package AI Engineering Playbook workflows as an optional Claude Code plugin while keeping ordinary repository files as the durable source of truth.

## Context
The latest repository state points at wrapper CLI hardening as the queued automation task, but the current user request asks for a Claude Code plugin path. The repo is documentation-first, so this feature needs an executable validation surface to avoid becoming untested content drift.

## Scope
In scope:
- root Claude Code marketplace metadata
- one self-contained plugin under `plugins/ai-engineering-playbook/`
- focused skills for adoption, orchestration, planning, implementation, and review
- validator and test coverage for the marketplace, plugin manifest, and skill frontmatter
- README and adapter links to the plugin

Out of scope:
- publishing to a remote marketplace
- replacing the portable playbook docs with plugin-only behavior
- adding hooks, MCP servers, slash commands, or bundled automation beyond skills

## Design
The plugin is intentionally thin. It gives Claude Code better activation points for common playbook workflows, but it does not own project memory. Durable state still lives in `PROJECT_CONSTITUTION.md`, `CLAUDE.md`, `AGENTS.md`, `architecture.md`, `roadmap.md`, `status.md`, task packets, handoffs, technical debt notes, and ADRs.

The marketplace lives at `.claude-plugin/marketplace.json`. The installable plugin lives at `plugins/ai-engineering-playbook/` with its own `.claude-plugin/plugin.json`.

Each skill keeps `SKILL.md` concise and delegates details to an adjacent `reference.md`. This keeps activation cheap while still giving Claude Code enough local procedure when a workflow is selected.

## Skills
- `adopting-playbook`: choose a starter level and align repo artifacts.
- `orchestrating-playbook-work`: resume from status, task packets, handoffs, and source-of-truth docs.
- `planning-playbook-tasks`: convert roadmap/design intent into bounded implementation tasks.
- `implementing-playbook-tasks`: execute a task with checks, scoped docs updates, and handoff.
- `reviewing-playbook-work`: review against objective, architecture, verification, and handoff quality.

## Validation
The existing validator expands from starter-kit/example/link checks to include Claude Code plugin checks:
- marketplace JSON exists and points at the plugin source
- plugin manifest exists and uses the expected plugin name
- required skills exist under `skills/<name>/SKILL.md`
- skill frontmatter contains matching `name` and useful `description`
- skill names are kebab-case and avoid vendor-reserved terms
- every skill has an adjacent `reference.md`

## Intent Contract
intent: Make AI Engineering Playbook usable as an optional Claude Code plugin without weakening the tool-agnostic workflow.

constraints:
- portable repo docs remain authoritative
- plugin paths stay self-contained under the plugin root
- validation uses Python standard-library tooling only
- existing starter-kit, example, workflow, and inventory checks keep passing

success_criteria:
- Claude Code marketplace and plugin files exist in the expected structure
- skills cover adoption, orchestration, planning, implementation, and review workflows
- local tests fail if plugin metadata or skill frontmatter drifts
- README and adapter docs point users to the plugin

risk_level: low

## Verification Contract
verify_steps:
- run `python3 -m unittest tests.test_validate_playbook`
- run `python3 tools/validate_playbook.py --inventory-out .agent/artifacts/playbook-inventory.json`
- if available, inspect with Claude Code plugin validation tooling before publishing

## Governance Contract
approval_gates:
- human review before publishing or advertising a remote marketplace URL
- human review before adding hooks, commands, MCP servers, or workflows that perform side effects

rollback:
- remove `.claude-plugin/marketplace.json`
- remove `plugins/ai-engineering-playbook/`
- revert validator and documentation additions

ownership:
- Orchestrator owns scope and handoff.
- Architecture owns plugin boundary and portability.
- Implementation owns files, tests, and verification.
- Review owns regression and source-of-truth checks.
