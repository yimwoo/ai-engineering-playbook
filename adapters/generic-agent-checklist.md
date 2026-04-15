# Generic Agent Checklist

## Purpose
Use this checklist when introducing any new code agent into your workflow.

The goal is not to make the repo depend on the new tool.
The goal is to verify that the generic operating model still works.

---

## Rule 1: Repo docs remain the source of truth
Before using a new agent, confirm that important project state still lives in repo artifacts such as:
- `PROJECT_CONSTITUTION.md`
- `status.md`
- `architecture.md`
- `roadmap.md`
- ADRs
- task packets
- handoffs
- `technical-debt.md`

If the workflow starts depending on hidden tool memory, chat history, or plugin-only state, portability is being lost.

---

## Rule 2: Test the agent on bounded work first
Before trusting a new agent with major design or implementation work, test it on:
- one bounded implementation task
- one repo audit or analysis task
- one status update or handoff task
- one review task

Do not start with a whole-system redesign.

---

## Rule 3: Evaluate behavior, not hype
Assess the new agent by how it behaves in your workflow.

### Questions to ask
- Does it follow repo instructions reliably?
- Does it read the docs before acting?
- Does it ask too many low-value clarifying questions?
- Does it over-simplify architecture decisions?
- Does it complete docs/status/handoff work or skip them?
- Does it keep scope bounded?
- Does it silently change contracts or architecture?

---

## Rule 4: Keep tool-specific optimizations optional
If you add tool-specific instructions, commands, hooks, or adapters:
- keep them clearly separate from the generic workflow
- do not let them become required for understanding the project
- document them in `adapters/` or `experiments/`

---

## Rule 5: Compare against the current operating model
A new agent should be judged by whether it can work with:
- your task packet system
- your status update discipline
- your handoff system
- your architecture and ADR workflow
- your technical debt tracking

If it only works well when bypassing those, it is not a clean fit yet.

---

## Lightweight onboarding sequence
1. read `docs/tool-agnostic-principle.md`
2. read `PROJECT_CONSTITUTION.md` and `CLAUDE.md`
3. run one bounded task using `prompts/implementation-task.md`
4. run one review using `prompts/review-task.md`
5. verify that `status.md` and handoff updates still happen cleanly
6. record observations in `notes/tool-comparison-notes.md`
7. only then decide whether to add an adapter note

---

## Keep / Adapt / Reject decision
After testing a new agent, decide:

### Keep
Works well with the existing operating model.

### Adapt
Useful, but needs a small adapter note or usage adjustment.

### Reject
Creates more workflow fragility than value.

---

## Success criteria
A new code agent is a good fit if:
- the repo still remains the source of truth
- the workflow still works without hidden tool magic
- handoffs and status remain reliable
- architecture and scope control do not degrade
- humans do not need to compensate for tool-specific confusion constantly
