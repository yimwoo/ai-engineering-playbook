---
mode: execute
current_milestone: m5
next_action: Add regression coverage that verifies `tools/run_playbook_check.py` forwards a custom `--inventory-out` path to `tools/validate_playbook.py`.
last_outcome: CODE_LANDED
last_commit: none
last_session_date: 2026-05-04
---

# STATE

## Last Session
- task: add workflow regression coverage for the GitHub Actions runner label
- changes:
  - added regression coverage that treats `.github/workflows/playbook-check.yml` runner selection as part of the canonical workflow contract
  - closed the last unchecked `m4` roadmap task and queued a small wrapper CLI follow-up under new milestone `m5`
- verification:
  - `python3 -m unittest tests.test_validate_playbook`: pass
- commits:
  - pending: `m4: add workflow runner regression coverage`
- push: deferred

## Blockers
- none

## Open Questions
- none

## Opportunities
- Add regression coverage for `tools/run_playbook_check.py` subprocess ordering so future wrapper edits cannot reorder validation and inventory generation unexpectedly.

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
- `STATE.md` cannot self-report the sha of the commit that contains it; use the final session outcome block or `git log -1 --oneline` for the exact landed commit.
