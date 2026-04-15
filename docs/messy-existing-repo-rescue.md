# Messy Existing Repo Rescue Guide

## Purpose
This guide helps you introduce AI Engineering Playbook into a real-world repository that already has:
- inconsistent docs
- unclear architecture
- multiple partially-overlapping workflows
- stale READMEs or design docs
- implicit team knowledge
- historical shortcuts

This is one of the most common adoption scenarios.

---

## What not to do
Do **not** start by:
- rewriting every document
- forcing a brand-new folder structure everywhere
- generating dozens of docs no one will maintain
- asking the agent to redesign the entire system in one pass
- replacing working practices without understanding why they exist

That usually creates more chaos, not less.

---

## Goal
The goal is not to make the repo look perfect.

The goal is to make the repo:
- understandable enough for the next session
- safe enough for bounded agent work
- explicit enough for architecture-sensitive changes
- maintainable enough for ongoing delivery

---

## Recommended rescue sequence

### Phase 1: Stabilize the minimum memory system
Add only:
- `PROJECT_CONSTITUTION.md`
- `CLAUDE.md`
- `status.md`

Why:
- `PROJECT_CONSTITUTION.md` defines operating rules
- `CLAUDE.md` defines how the agent should behave
- `status.md` gives the next session a reliable starting point

At this stage, do not try to document the whole system yet.

---

### Phase 2: Audit reality before restructuring
Use:
- `prompts/repo-audit.md`
- `prompts/repo-alignment.md`

Ask the agent to identify:
- the actual architecture
- useful existing docs
- stale docs
- contradictions
- missing governance artifacts
- risky areas where assumptions are implicit

Output should include:
- what to preserve
- what to archive
- what to merge
- what to create first

---

### Phase 3: Document only the highest-value architecture
Do not try to document everything.

Start with:
- system overview
- major modules or bounded contexts
- known risky integration points
- major data ownership boundaries
- critical external interfaces
- top unresolved architectural questions

If needed, create:
- `architecture.md`
- a few module specs
- 1-3 ADRs for major current decisions

---

### Phase 4: Create a bounded delivery model
Once minimum memory exists, introduce:
- task packets for important work
- handoffs for meaningful sessions
- technical debt tracking for shortcuts

This prevents the repo from falling back into undocumented drift.

---

### Phase 5: Use design-change packages for bigger repairs
If the repo needs:
- major refactoring
- module boundary cleanup
- observability redesign
- eventing changes
- scaling/failover redesign
- roadmap resets

Do not jump straight into code.

Create a design-change package first.

---

## A practical triage framework
When auditing a messy repo, classify files and docs into 4 buckets:

### 1. Keep
Still useful and mostly accurate.

### 2. Fix
Useful, but stale or incomplete.

### 3. Merge
Multiple overlapping docs should be consolidated.

### 4. Archive
Misleading, obsolete, or duplicative.

This is usually more practical than rewriting from scratch.

---

## A practical adoption rule
Use the smallest useful governance layer.

For example:
- a solo app may only need constitution + CLAUDE + status + architecture
- a medium product may also need roadmap + technical debt + module specs
- a large platform may need AGENTS + ADRs + task packets + handoffs + design-change packages

Do not over-govern too early.

---

## Common pitfalls

### Pitfall 1: creating docs nobody updates
Fix: keep docs small, operational, and tied to real workflow.

### Pitfall 2: treating generated docs as truth without review
Fix: have humans review major architecture and product claims.

### Pitfall 3: trying to standardize the whole repo in one pass
Fix: roll out changes incrementally by priority.

### Pitfall 4: mixing architecture redesign with feature delivery blindly
Fix: separate design analysis from implementation tasks.

### Pitfall 5: letting shortcuts go undocumented again
Fix: add `technical-debt.md` as soon as shortcuts start accumulating.

---

## Suggested first 7 actions
1. add `PROJECT_CONSTITUTION.md`
2. add `CLAUDE.md`
3. add `status.md`
4. run a repo audit
5. identify 3-5 critical modules
6. document only those modules first
7. introduce task packets for risky or cross-cutting work

---

## Suggested prompt flow
1. `prompts/repo-audit.md`
2. `prompts/repo-alignment.md`
3. `prompts/module-spec-generation.md`
4. `prompts/orchestrator-kickoff.md`
5. `prompts/implementation-task.md`

---

## Success criteria
You are succeeding if:
- the next session can understand current state quickly
- important architecture is explicit enough to avoid accidental drift
- work is increasingly bounded and reviewable
- stale docs are shrinking instead of growing
- the human is used for high-value decisions, not every small clarification
