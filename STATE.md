---
mode: execute
current_milestone: m4
next_action: Add regression coverage that verifies `.github/workflows/playbook-check.yml` still runs on `ubuntu-latest`.
last_outcome: CODE_LANDED
last_commit: none
last_session_date: 2026-05-03
---

# STATE

## Last Session
- task: add workflow regression coverage for workflow triggers and Python version pinning
- changes:
  - added workflow regression coverage that pins `.github/workflows/playbook-check.yml` to `push` and `pull_request` events
  - added workflow regression coverage that pins the workflow's Python runtime to 3.11
- verification:
  - `python3 -m unittest tests.test_validate_playbook`: pass
- commits:
  - pending: `m4: add workflow trigger contract regression coverage`
- push: deferred

## Blockers
- none

## Open Questions
- none

## Opportunities
- Add regression coverage for workflow runner selection so CI environment drift is caught alongside workflow command drift.

## Notes
- The repository is currently documentation-first; executable validation needs to be introduced incrementally with standard-library tooling.
- `AGENT_PROTOCOL.md` requires non-doc changes for all post-bootstrap execution sessions, so the roadmap is intentionally code-first.
- `.agent/bootstrapped` records the stable bootstrap content commit (`54a7bf0`) because the sandbox cannot push branch state upstream.
- `tools/validate_playbook.py` treats starter-kit and example promises as minimum required entries, so extra illustrative files do not fail validation.
- High-signal link validation is intentionally allowlisted to `README.md`, `docs/getting-started.md`, and `docs/prompts.md` so onboarding coverage expands incrementally instead of turning into brittle repo-wide markdown linting.
- `tools/validate_playbook.py --inventory-out <path>` emits deterministic JSON with top-level prompt/template paths and per-example/per-starter-kit file inventories sorted for stable diffs.
- `tools/run_playbook_check.py` is the canonical automation entrypoint; GitHub Actions writes its inventory artifact to `.agent/artifacts/playbook-inventory.json`.
- `tests/test_validate_playbook.py` now treats `.github/workflows/playbook-check.yml` as a regression surface for the wrapper command and inventory artifact contract.
- `STATE.md` cannot self-report the sha of the commit that contains it; use the final session outcome block or `git log -1 --oneline` for the exact landed commit.
