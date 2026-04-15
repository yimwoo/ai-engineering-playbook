# Daily Path

## Purpose
This is the lightweight path for using AI Engineering Playbook in everyday software work without feeling overwhelmed by the full repository.

You do **not** need to use every doc, template, or prompt every day.

---

## The default daily workflow

### Step 1: Start from current repo memory
Read only the minimum useful context:
- `README.md` if you need orientation
- `status.md`
- `architecture.md` if the task touches design or integration
- the relevant task packet if one exists

If you are switching between code agents, also check the latest handoff note.

---

### Step 2: Pick the smallest useful prompt or instruction shape
You do not need a perfect prompt.
Usually this is enough:
- objective
- relevant context/docs
- constraints
- acceptance criteria
- out of scope

If needed, use one of the repo prompts as a starting point.

---

### Step 3: Keep the work bounded
Prefer:
- one module
- one feature
- one migration
- one refactor
- one test improvement

Avoid asking the code agent to solve the whole system at once.

---

### Step 4: Update project memory before you stop
At the end of meaningful work, update at least one of:
- `status.md`
- a handoff note
- `technical-debt.md` if a shortcut was taken
- the relevant module doc if design assumptions changed

This matters more than having a fancy prompt.

---

### Step 5: Capture one small learning if something interesting happened
If you notice a repeated pattern, add a quick note to:
- `notes/workflow-observations.md`
- `notes/tool-comparison-notes.md`
- `notes/weekly-learning-log.md`

You do not need a full retrospective every day.

---

## Minimal daily file set
If you want the lightest useful setup, focus on:
- `status.md`
- `architecture.md`
- `prompts/implementation-task.md`
- `prompts/status-update.md`
- `notes/tool-comparison-notes.md`

That is enough for many normal workdays.

---

## When to use more structure
Use more of the repo only when needed:

### Use task packets when:
- the task is risky
- the task spans multiple files or modules
- you may switch agents or sessions
- acceptance criteria need to be explicit

### Use ADRs when:
- architecture changes
- public contracts change
- data ownership changes
- security or deployment decisions change

### Use design-change packages when:
- the change is large
- the roadmap is affected
- multiple modules are touched
- rollback and migration risk are real

---

## Practical rule
When in doubt, choose the lightest process that still preserves clarity for the next session.

---

## A good daily rhythm
### Before work
- read `status.md`
- read only the relevant design context

### During work
- keep tasks bounded
- avoid relying on tool-specific memory

### After work
- update `status.md` or handoff
- capture one lesson if useful

That is enough to get value from the playbook without turning it into overhead.
