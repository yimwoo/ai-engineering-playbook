# Repo Weight Review

## Purpose
This document is a periodic self-check to keep the repo useful instead of over-engineered.

---

## Current assessment
The repository is now strong and well-structured, but it is approaching the point where additional structure could reduce usability if not grounded in real daily use.

That does **not** mean the repo is too heavy yet.
It means future additions should be more selective.

---

## What feels high-value and stable
These parts look worth keeping as core:
- `README.md`
- `docs/getting-started.md`
- `docs/operating-model.md`
- `docs/tool-agnostic-principle.md`
- `docs/mixed-agent-workflow.md`
- `templates/`
- `prompts/`
- `starter-kits/`
- `adapters/generic-agent-checklist.md`
- `adapters/agent-evaluation-scorecard.md`

These define the durable operating model.

---

## What is useful but should stay lightweight
These are valuable, but should not grow too much without repeated real use:
- `examples/`
- `notes/`
- `patterns/`
- `retros/`
- `experiments/`
- some long-form docs in `docs/`

Rule:
If these sections expand, they should expand from actual usage, not speculation.

---

## Signs the repo might be getting too heavy
Watch for these warning signs:
- too many docs say similar things
- multiple prompts overlap without clear differences
- examples become stale
- adapters multiply without real need
- users do not know where to start
- maintaining the repo becomes work by itself

---

## Simplification rules going forward
1. prefer improving existing docs over adding new ones
2. add a new file only when it solves a repeated problem
3. archive or merge overlapping content when drift appears
4. avoid turning every idea into a first-class artifact
5. keep the stable core small and easy to explain

---

## Suggested current core path for daily use
If you want the lightest practical usage path today, focus mostly on:
- `README.md`
- `docs/getting-started.md`
- `docs/tool-agnostic-principle.md`
- `docs/mixed-agent-workflow.md`
- `prompts/implementation-task.md`
- `prompts/orchestrator-kickoff.md`
- `prompts/status-update.md`
- `templates/status.md`
- `notes/tool-comparison-notes.md`

This is likely enough for everyday use.

---

## Recommendation
Pause major structural expansion for a bit.
Use the repo in real projects, log friction, and let the next changes come from real workflow pain.
