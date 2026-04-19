# Repo Structure Review for Large-Repo Readiness

## Objective
Assess whether this repository's current structure and documentation model prepare engineers to onboard code agents safely in large existing repos, enterprise codebases, and multi-module or sub-project systems.

## Scope
- top-level repository structure
- documentation model across `README.md`, `docs/`, `templates/`, `starter-kits/`, and `examples/`
- support for information architecture, module boundaries, migration strategy, and source-of-truth design
- special focus on large repos, monorepos, and sub-project governance

## Current Strengths
- The core operating model is coherent and consistent: bounded work, explicit architecture, visible debt, and repo memory over chat memory.
- Existing-repo adoption guidance is strong and intentionally incremental. `docs/adopting-in-existing-repos.md` and `docs/messy-existing-repo-rescue.md` explicitly avoid forced rewrites.
- The repo already distinguishes reusable guidance by type: `docs/` for concepts, `templates/` for artifacts, `starter-kits/` for adoption bundles, and `examples/` for worked samples.
- The enterprise starter and enterprise example establish the right baseline artifacts for long-lived, architecture-sensitive delivery.
- The design-change-package pattern is a good source-of-truth mechanism for risky architectural changes and migration sequencing.
- `notes/repo-weight-review.md` correctly warns against over-expansion, which is important for keeping the playbook usable.

## Structural Gaps
- The repo does not define a clear precedence model when documentation conflicts. It implies source-of-truth artifacts, but does not state which artifact wins across constitution, architecture, ADRs, roadmap, status, module docs, and task packets.
- Support for module boundaries is present, but mostly as a flat `modules/` concept. The repo does not yet model nested domains, multiple deployables, shared libraries, or cross-subproject contracts explicitly.
- There is no canonical repo-topology artifact for large codebases. Engineers adopting this playbook into a monorepo still need a place to record package boundaries, ownership, critical paths, build/test entrypoints, and risky integration seams.
- There is no explicit interface registry pattern for APIs, events, schemas, or data ownership across modules and sub-projects.
- Current examples are useful, but they are single-project oriented. There is no concrete monorepo or multi-subproject example showing root docs plus local subproject docs.
- The repo relies on several parallel explanatory layers (`README.md`, `docs/`, starter kits, examples, notes). That is workable today, but canonical versus illustrative content is not labeled strongly enough.
- The architect workflow expects strategy and research artifacts, but this repo does not currently provide `docs/strategies/` or `docs/research/` as first-class homes for them.

## Options Considered
### Option 1: Minimal Overlay
Keep the current structure and add only a source-of-truth guide plus a large-repo topology guide.

Pros:
- lowest churn
- aligns with the repo's anti-bloat posture
- easy to adopt without restructuring existing content

Cons:
- still leaves monorepo and sub-project modeling mostly implicit
- weaker guidance for cross-module contracts and local ownership

### Option 2: Layered Source-of-Truth Model
Keep the current core layout, but add an explicit layered model:
- root governance docs for project-wide rules and current state
- durable architecture docs for global topology and ADRs
- per-module or per-subproject docs as local contracts
- interface docs for cross-boundary dependencies
- task packets and handoffs as execution-layer artifacts

Pros:
- scales to large repos without forcing a full restructure
- fits the repo's incremental adoption philosophy
- makes boundaries and ownership clearer for parallel human/agent work

Cons:
- requires a few new templates and at least one large-repo example
- introduces more taxonomy that must be kept intentionally small

### Option 3: Full Taxonomy Restructure
Reorganize the repo into explicit domains such as core docs, reference docs, strategy, research, examples, and templates.

Pros:
- cleanest long-term information architecture
- strongest discoverability for advanced users

Cons:
- highest migration cost
- likely YAGNI for the current repo size and maturity
- risks making the playbook feel heavier before repeated real-world demand exists

## Decision
Recommend Option 2.

It preserves the repo's current strengths while adding the minimum missing structure needed for large existing repos and monorepos: explicit source-of-truth precedence, explicit repo topology, and explicit local contracts for sub-projects.

## Constraints
- Do not break the current lightweight and standard adoption path.
- Avoid adding a fourth starter kit until repeated user demand justifies it.
- Keep the stable core small; new structure should clarify, not multiply overlapping docs.
- Preserve the rule that existing repos should align incrementally rather than conform to identical folder names.

## Risks
- If large-repo guidance is added without clear precedence rules, users may create more docs but still lack a canonical answer.
- If monorepo support is modeled as a heavy new framework, the repo may violate its own anti-bloat guidance.
- If examples are added without update discipline, the repo will accumulate stale "illustrative truth" that conflicts with canonical guidance.

## Recommendations on Repo and Doc Structure
1. Define source-of-truth precedence explicitly.
Suggested model:
- `PROJECT_CONSTITUTION.md`: operating rules and non-negotiables
- `architecture.md` plus repo-topology doc: current structural truth
- `decisions/`: durable decision records when architecture or policy changes
- `roadmap.md`: intended future state
- `status.md`: current execution state and near-term focus
- module or subproject docs: local contracts and boundaries
- task packets and handoffs: bounded delivery context, never architectural truth

2. Label content classes more clearly.
Suggested classes:
- canonical: root docs and approved architecture artifacts
- reusable: templates and starter kits
- illustrative: examples
- exploratory: notes, patterns, retros, experiments

3. Add a canonical repo-topology pattern for large codebases.
That artifact should capture:
- major apps, services, libs, and tools
- ownership boundaries
- build, test, and deploy entrypoints
- critical shared infrastructure
- risky integration seams
- where local docs live

4. Extend the module model to support subprojects.
The playbook should describe how a root-level architecture view relates to per-subproject docs, instead of assuming one flat `modules/` layer.

5. Add an interface-contract pattern.
Large repos need a documented home for cross-module APIs, events, schemas, and shared-data rules so agents do not infer contracts from scattered code alone.

6. Add lightweight document lifecycle guidance.
At minimum, define how to mark docs as active, illustrative, or archived, and when to merge or retire overlapping guidance.

## Recommendations Specific to Large Repos, Monorepos, and Sub-Projects
1. Use a layered documentation model.
- Root docs should answer global policy, topology, roadmap, and current status.
- Subproject docs should answer local architecture, commands, boundaries, and risks.

2. Give each major subproject a local contract file.
This can be a local `README.md`, `AGENTS.md`, or module spec, but it should state:
- purpose
- owned code and data
- dependencies
- public interfaces
- test and verification entrypoints
- local constraints

3. Introduce a repo map before broad module documentation.
For large existing repos, the first high-value artifact is usually a topology map, not dozens of detailed module docs.

4. Prefer one monorepo extension over a full new starter kit.
Recommended first increment:
- one large-repo topology guide
- one subproject contract template
- one monorepo example

This is likely enough to validate the model before expanding.

5. Separate global truth from local truth.
Architecture decisions that affect multiple subprojects belong in root architecture docs or ADRs. Local implementation details belong near the owning subproject.

## Migration Strategy
Phase 1:
- add explicit source-of-truth precedence to the playbook
- add a repo-topology guidance doc for large repos

Phase 2:
- add a subproject contract template
- add an interface-contract template or guidance
- update existing-repo adoption docs to reference the layered model

Phase 3:
- add one worked monorepo or multi-subproject example
- validate that the new structure improves navigation without increasing noise

## Assumptions
- The repo intends to remain tool-agnostic and lightweight by default.
- The primary growth area is helping users adopt the playbook in existing enterprise repositories, not only greenfield projects.
- Any added large-repo structure should remain optional and incremental.

## Blockers
- No `docs/strategies/` or `docs/research/` directories currently exist, so there are no formal strategy or research artifacts to anchor this review.
- There is no real monorepo example in the repo today, so large-repo recommendations are structurally sound but not yet validated by an in-repo reference implementation.
- I did not assess external user feedback or adoption metrics, so prioritization is based on repository structure and internal guidance only.

## Next-Step Recommendation
Prioritize one small architectural extension rather than a broad restructure:
1. document source-of-truth precedence
2. add large-repo topology guidance
3. add one subproject contract pattern
4. validate with a single monorepo-style example before expanding further
