# ROADMAP

## Delivery Strategy
Use small tooling-first milestones to protect a documentation-heavy repository from drift. Each milestone should land executable checks before broadening the playbook surface area.

## Active Milestone
`m4` - automation hardening

## Milestones

### `m1` Repository validation baseline
Goal: establish a canonical executable check for the repo's documented structure.

- [x] Add `tools/validate_playbook.py` to verify that starter kits and examples contain the files promised by `README.md`.
- [x] Add `tests/test_validate_playbook.py` covering the expected file sets for lightweight, standard, and enterprise starter kits plus the shipped examples.
- [x] Add a simple invocation path (`python3 -m unittest tests.test_validate_playbook`) to the validator workflow and document it inline where needed.

Exit criteria:
- A single local test command validates the repo's documented package structure.
- Failures identify which starter kit or example drifted.

### `m2` Reference integrity checks
Goal: catch broken high-value references before documentation changes land.

- [x] Extend `tools/validate_playbook.py` to validate high-signal relative links from `README.md` and selected `docs/` indexes.
- [x] Add regression tests for missing or renamed linked files.

Exit criteria:
- The validator fails on broken top-level references that would derail onboarding.

### `m3` Content inventory output
Goal: make repo evolution easier to review and maintain.

- [x] Add a machine-readable inventory export describing prompts, starter kits, templates, and examples.
- [x] Add tests covering inventory generation for newly added assets.
- [x] Wire the validator and inventory export into a canonical automation check.

Exit criteria:
- A deterministic inventory can be generated and verified in CI or local sessions.

### `m4` Automation hardening
Goal: keep the canonical playbook check from drifting as repo automation evolves.

- [x] Add regression coverage that verifies the canonical GitHub Actions workflow invokes `tools/run_playbook_check.py`.
- [x] Add regression coverage for the published inventory artifact path so workflow changes stay intentional.

Exit criteria:
- Local regression tests fail when the canonical workflow stops running the wrapper command or publishing the expected inventory artifact.

## Dependencies
- `m2` depends on the validation framework from `m1`.
- `m3` depends on the shared repository traversal helpers introduced in `m1` or `m2`.
- `m4` depends on the canonical check wiring from `m3`.

## Risks
- Repo guidance may continue to drift faster than validation coverage if new content lands without tests.
- The repo currently has no existing test harness, so the first milestone must keep dependencies minimal and use the Python standard library.

## Deferred Items
- Broader linting or markdown style enforcement.
- Automatic generation of README navigation sections.
