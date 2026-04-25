# Design

## Purpose
AI Engineering Playbook is a content-first repository that packages reusable guidance for AI-assisted software delivery. The repo's main outputs are:

- reference documentation under `docs/`
- reusable agent prompts under `prompts/`
- copyable starter kits under `starter-kits/`
- worked examples under `examples/`
- reusable templates under `templates/`
- tool-specific onboarding notes under `adapters/`

## Architectural Shape

### 1. Core reference layer
The top-level `README.md` and `docs/` directory define the canonical narrative for adopting the playbook. These files explain the operating model, document lifecycle, day-to-day workflow, and repo improvement guidance.

### 2. Reusable asset layer
`templates/`, `starter-kits/`, and `examples/` turn the reference guidance into concrete artifacts teams can copy into their own repositories. Starter kits represent progressively heavier adoption modes, while examples show those files in realistic project shapes.

### 3. Agent execution layer
`prompts/`, `AGENTS.md`, and `AGENT_PROTOCOL.md` provide the execution contract for human and autonomous agent sessions. These files constrain how work is selected, handed off, reviewed, and recorded.

### 4. Evidence and learning layer
`notes/`, `patterns/`, `retros/`, `experiments/`, `docs/designs/`, and `docs/research/` hold lower-stability material that may later be promoted into the core reference layer.

## Current Gaps
- The repo has strong narrative structure, but no executable validation ensuring the documented starter-kit and example claims stay true over time.
- There is no canonical verification command for autonomous sessions beyond manual inspection.
- The top-level repo state files required by `AGENT_PROTOCOL.md` were missing before this bootstrap.

## Near-Term Strategy
Add lightweight repository tooling before expanding content. The first useful code path is a validation script plus tests that verify:

- starter kits expose the file sets described in `README.md`
- examples contain the expected baseline files for their advertised adoption mode
- high-signal documentation references point to files that actually exist

That tooling gives future autonomous sessions a concrete verification surface and reduces documentation drift.
