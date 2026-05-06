---
name: reviewing-playbook-work
description: Reviews AI Engineering Playbook work for correctness, architecture compliance, risk, tests, and handoff quality. Use when a user asks for review of a task, branch, pull request, implementation output, design-change package, or agent handoff.
---

# Reviewing Playbook Work

## Workflow
1. Read the task packet, status, architecture notes, ADRs, and latest handoff relevant to the work.
2. Inspect the actual diff or files changed.
3. Prioritize bugs, regressions, missing verification, architecture drift, and unclear handoff state.
4. Report findings first, with file and line references when possible.
5. Keep summaries secondary to actionable findings.

## Review Criteria
- Does the change satisfy the stated objective?
- Did it stay inside scope?
- Are tests or checks adequate for the risk?
- Did docs/status/handoff updates preserve continuity?
- Did any tool-specific behavior become a hidden source of truth?

## Reference
Read `reference.md` for review priorities and output format.
