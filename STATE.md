---
mode: execute
current_milestone: m4
next_action: Add regression coverage that verifies the GitHub Actions workflow invokes `tools/run_playbook_check.py` and publishes `.agent/artifacts/playbook-inventory.json`.
last_outcome: CODE_LANDED
last_commit: none
last_session_date: 2026-04-28
---

# STATE

## Last Session
- task: wire the validator and inventory export into a canonical automation check
- changes:
  - added `tools/run_playbook_check.py` as the canonical wrapper for validator regressions plus inventory export
  - added `.github/workflows/playbook-check.yml` to run the wrapper on pushes and pull requests and publish the inventory artifact
  - added wrapper regression coverage for default command sequencing and early-exit failure handling
- verification:
  - `python3 -m unittest tests.test_validate_playbook`: pass
  - `python3 tools/run_playbook_check.py --inventory-out /tmp/playbook-inventory.json`: pass
  - `git push -u origin HEAD`: deferred (network access unavailable in sandbox)
- commits:
  - pending: `m4: add canonical playbook check workflow`
- push: deferred

## Blockers
- none

## Open Questions
- none

## Opportunities
- Add regression coverage for the GitHub Actions workflow file so command and artifact-path drift is caught before CI surprises.

## Notes
- The repository is currently documentation-first; executable validation needs to be introduced incrementally with standard-library tooling.
- `AGENT_PROTOCOL.md` requires non-doc changes for all post-bootstrap execution sessions, so the roadmap is intentionally code-first.
- `.agent/bootstrapped` records the stable bootstrap content commit (`54a7bf0`) because the sandbox cannot push branch state upstream.
- `tools/validate_playbook.py` treats starter-kit and example promises as minimum required entries, so extra illustrative files do not fail validation.
- High-signal link validation is intentionally allowlisted to `README.md`, `docs/getting-started.md`, and `docs/prompts.md` so onboarding coverage expands incrementally instead of turning into brittle repo-wide markdown linting.
- `tools/validate_playbook.py --inventory-out <path>` emits deterministic JSON with top-level prompt/template paths and per-example/per-starter-kit file inventories sorted for stable diffs.
- `tools/run_playbook_check.py` is the canonical automation entrypoint; GitHub Actions writes its inventory artifact to `.agent/artifacts/playbook-inventory.json`.
