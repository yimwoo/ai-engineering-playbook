# Enterprise/Monorepo Coverage Evaluation

## Objective
Evaluate whether this repository adequately covers the needs of engineers working in large enterprise repos, monorepos, and codebases with many submodules or sub-projects.

## Scope
- Local inspection only
- Core docs, prompts, templates, starter kits, and examples
- Focus on operational guidance, not theoretical adaptability

## Coverage That Already Exists
- The repo already has a solid document-driven operating model for large, long-lived projects with bounded agent work, explicit roles, and persistent project memory in repo artifacts rather than chat history. See [README](../../README.md), [docs/operating-model.md](../operating-model.md), and [starter-kits/enterprise/README.md](../../starter-kits/enterprise/README.md).
- Existing-repo adoption is handled well at a high level: start small, audit reality, preserve useful docs, and add governance incrementally. See [docs/adopting-in-existing-repos.md](../adopting-in-existing-repos.md), [docs/messy-existing-repo-rescue.md](../messy-existing-repo-rescue.md), [prompts/repo-audit.md](../../prompts/repo-audit.md), and [prompts/repo-alignment.md](../../prompts/repo-alignment.md).
- The core templates and prompts cover several enterprise needs inside a single system boundary: architecture, module ownership, dependencies, impact analysis, migration planning, bounded tasks, and handoffs. See [templates/architecture.md](../../templates/architecture.md), [templates/module-template.md](../../templates/module-template.md), [prompts/module-spec-generation.md](../../prompts/module-spec-generation.md), [prompts/implementation-task.md](../../prompts/implementation-task.md), and [templates/design-change-package-template.md](../../templates/design-change-package-template.md).
- Mixed-agent coordination is also well covered when different tools share the same repo-based source of truth. See [docs/mixed-agent-workflow.md](../mixed-agent-workflow.md).
- The enterprise example demonstrates a multi-module platform, but it is still modeled as one product/system with module boundaries, not as a monorepo or repo with many nested projects. See [examples/enterprise-product/README.md](../../examples/enterprise-product/README.md) and [examples/enterprise-product/architecture.md](../../examples/enterprise-product/architecture.md).

## Comparison
| Need | Current Coverage | Assessment |
| --- | --- | --- |
| Large-project governance and role separation | Strong | Well covered |
| Incremental adoption in messy existing repos | Strong | Well covered |
| Module ownership within one system | Strong | Well covered |
| Cross-cutting design change planning | Strong | Well covered |
| Monorepo/workspace topology mapping | Weak | Underdeveloped |
| Many-subproject status and task coordination | Weak | Underdeveloped |
| Git submodules / external source boundaries | Missing | Important gap |
| Build graph / affected-target / CI-scope guidance | Missing | Important gap |
| Nested agent instructions by subproject | Weak | Underdeveloped |

## Missing or Underdeveloped Scenarios
- There is no explicit monorepo or workspace guidance. The repo talks about modules, bounded contexts, and large platforms, but not about package graphs, app/lib separation, workspace roots, or multi-project repo topology.
- There is no dedicated artifact for repository topology. `architecture.md` describes the system, but large repos usually also need a repo map covering subprojects, deployable units, owners, commands, generated code, and do-not-touch areas. See [templates/architecture.md](../../templates/architecture.md).
- The task packet model is still single-task/single-system oriented. It does not ask for affected paths, packages, owners, CI targets, or rollout order across multiple subprojects. See [templates/task-packet-template.md](../../templates/task-packet-template.md).
- The repo-audit and alignment prompts are useful, but they do not explicitly ask agents to map monorepo layout, build tooling, cross-project dependencies, ownership hotspots, or nested instruction files. See [prompts/repo-audit.md](../../prompts/repo-audit.md) and [prompts/repo-alignment.md](../../prompts/repo-alignment.md).
- There is no guidance for git submodules, vendored code, generated code, or external repos mirrored into the tree. In enterprise repos, those boundaries matter because agents should often analyze but not edit them.
- The examples do not show a realistic enterprise monorepo shape such as `apps/`, `services/`, `packages/`, `infra/`, `docs/`, plus per-subproject conventions and cross-project release sequencing. See [examples/enterprise-product/README.md](../../examples/enterprise-product/README.md).
- The playbook also does not explain how root-level governance should interact with subproject-local instructions. In very large repos, engineers often need both a root operating model and narrower local rules.

## Suggested Additions
### Docs
- `docs/monorepo-and-multi-project-adoption.md`
  Covers repo topology mapping, root vs subproject governance, ownership boundaries, shared-library rules, and rollout strategy.
- `docs/submodules-vendored-and-generated-code.md`
  Covers edit policies, update flow, review expectations, and safe agent behavior around external code.

### Templates
- `templates/repo-map.md`
  Sections: repo topology, subprojects, owners, primary commands, build/test entrypoints, deployable units, generated/vendor paths, high-risk integration points.
- `templates/cross-project-task-packet.md`
  Adds affected paths, affected packages/services, owning teams, CI/build targets, contract consumers, rollout order, and validation matrix.
- `templates/subproject-instructions-template.md`
  A lightweight local instructions file for teams that need repo-root rules plus stricter subproject rules.

### Prompts
- `prompts/monorepo-audit.md`
  Explicitly asks for workspace layout, dependency hotspots, ownership map, duplicate tooling, and risky cross-project boundaries.
- `prompts/cross-project-impact-analysis.md`
  Focuses on affected targets, downstream consumers, contract compatibility, rollout sequence, and rollback scope.
- `prompts/submodule-update-review.md`
  Focuses on version delta, local integration risk, touched interfaces, and safe validation scope.

### Examples
- `examples/enterprise-monorepo/`
  A realistic sample with `apps/`, `services/`, `packages/`, `infra/`, root status, shared architecture, and at least one cross-project task packet.
- One example of nested instructions
  Show root governance plus a stricter local instructions file for a high-risk subproject.

## Recommendation
The repo is already strong for large single-product codebases and generic enterprise governance, but it does not yet adequately cover repo-shape-specific needs for monorepos, submodules, or many-subproject codebases. The best next move is not to rewrite the core playbook. Add a focused monorepo extension layer: one adoption guide, one repo-map template, two prompts, and one concrete example.

## Assumptions
- “Adequately covers” means engineers can apply the playbook with explicit operational guidance, not just by extrapolating from generic principles.
- The current repo intentionally favors minimalism, so some gaps may be deliberate rather than accidental.
- I evaluated only the local repository contents and did not browse external sources.

## Blockers
- No hard blockers for this evaluation.
- The main uncertainty is intent: the repo does not say whether monorepo/submodule coverage is intentionally deferred or simply not yet written.

## Next-Step Recommendation
Suggested next step: @Architect can design a solution based on these findings.
