---
mode: execute
current_milestone: m3
next_action: Add a machine-readable inventory export describing prompts, starter kits, templates, and examples.
last_outcome: CODE_LANDED
last_commit: none
last_session_date: 2026-04-26
---

# STATE

## Last Session
- task: validate high-signal onboarding links in README and docs indexes
- changes:
  - extended `tools/validate_playbook.py` to validate relative links from `README.md`, `docs/getting-started.md`, and `docs/prompts.md`
  - added regression coverage for link extraction and missing-target failures alongside the existing structure validation tests
  - advanced the roadmap to `m3` after completing the `m2` reference integrity milestone
- verification:
  - `python3 -m unittest tests.test_validate_playbook`: pass
  - `python3 tools/validate_playbook.py`: pass
  - `git push -u origin HEAD`: pending
- commits:
  - pending: `m2: validate high-signal onboarding links`
- push: pending

## Blockers
- none

## Open Questions
- none

## Opportunities
- Add CI wiring once the validator exists so future sessions can rely on a canonical repo check.

## Notes
- The repository is currently documentation-first; executable validation needs to be introduced incrementally with standard-library tooling.
- `AGENT_PROTOCOL.md` requires non-doc changes for all post-bootstrap execution sessions, so the roadmap is intentionally code-first.
- `.agent/bootstrapped` records the stable bootstrap content commit (`54a7bf0`) because the sandbox cannot push branch state upstream.
- `tools/validate_playbook.py` treats starter-kit and example promises as minimum required entries, so extra illustrative files do not fail validation.
- High-signal link validation is intentionally allowlisted to `README.md`, `docs/getting-started.md`, and `docs/prompts.md` so onboarding coverage expands incrementally instead of turning into brittle repo-wide markdown linting.
