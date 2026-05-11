---
mode: execute
current_milestone: m6
next_action: Add regression coverage that `tools/validate_playbook.py` rejects a Claude plugin marketplace source that does not match `./plugins/ai-engineering-playbook`.
last_outcome: CODE_LANDED
last_commit: none
last_session_date: 2026-05-11
---

# STATE

## Last Session
- task: add wrapper subprocess ordering regression coverage
- changes:
  - added a mocked subprocess regression test covering the unit-test-then-inventory command order when inventory generation fails
  - verified the wrapper returns the inventory generation failure after running the commands in order
  - marked the `m5` wrapper ordering coverage task complete and added the next `m6` plugin validation task
- verification:
  - `python3 -m unittest tests.test_validate_playbook`: pass
  - `python3 tools/run_playbook_check.py --inventory-out .agent/artifacts/playbook-inventory.json`: pass
- commits:
  - landed: `m5: add wrapper subprocess ordering regression coverage`
- push: landed

## Blockers
- none

## Open Questions
- none

## Opportunities
- Consider adding an optional CI job or release checklist step for `claude plugin validate` when Claude Code is available, while keeping the canonical local validator free of non-standard-library dependencies.

## Notes
- The repository is currently documentation-first; executable validation needs to be introduced incrementally with standard-library tooling.
- `AGENT_PROTOCOL.md` requires non-doc changes for all post-bootstrap execution sessions, so the roadmap is intentionally code-first.
- `.agent/bootstrapped` records the stable bootstrap content commit (`54a7bf0`) because the sandbox cannot push branch state upstream.
- `tools/validate_playbook.py` treats starter-kit and example promises as minimum required entries, so extra illustrative files do not fail validation.
- High-signal link validation is intentionally allowlisted to `README.md`, `docs/getting-started.md`, and `docs/prompts.md` so onboarding coverage expands incrementally instead of turning into brittle repo-wide markdown linting.
- `tools/validate_playbook.py --inventory-out <path>` emits deterministic JSON with top-level prompt/template paths and per-example/per-starter-kit file inventories sorted for stable diffs.
- `tools/run_playbook_check.py` is the canonical automation entrypoint; GitHub Actions writes its inventory artifact to `.agent/artifacts/playbook-inventory.json`.
- `tests/test_validate_playbook.py` now treats `.github/workflows/playbook-check.yml` as a regression surface for the wrapper command and inventory artifact contract.
- `tests/test_validate_playbook.py` now treats the workflow runner label (`runs-on: ubuntu-latest`) as part of the canonical CI contract alongside triggers and Python version pinning.
- The Claude Code plugin package is an optional adapter; durable project state should remain in repo files, not plugin-only memory.
- Claude Code 2.1.131 locally validates the marketplace and plugin manifests; `tools/validate_playbook.py` mirrors the important package checks with standard-library Python so CI does not require Claude Code.
- `STATE.md` cannot self-report the sha of the commit that contains it; use the final session outcome block or `git log -1 --oneline` for the exact landed commit.
- `tests/test_validate_playbook.py` now covers both the default and custom `--inventory-out` wrapper paths with mocked subprocess calls.
- `tests/test_validate_playbook.py` now verifies the wrapper preserves unit-test-then-inventory subprocess ordering even when the inventory generation command fails.
