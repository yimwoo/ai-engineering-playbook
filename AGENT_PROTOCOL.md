# AGENT_PROTOCOL.md

You are running exactly ONE autonomous coding cycle in this repository. End with a
tested code change or a clean blocker. Doc-only sessions are a failure outside
bootstrap.

---

## Session Contract (non-negotiable)

Every session ends with exactly one outcome:

- **CODE_LANDED** — source/test/config change committed and verified.
- **BLOCKED** — no safe implementation possible; blocker documented with evidence.
- **BOOTSTRAPPED** — first-run planning docs created (one-time only).

If `git diff --stat` shows only documentation files in execution mode, the
session is invalid. The only doc-only commits permitted are a blocker report
(Phase 7) or a replan commit while `mode: replan` is active (Phase 2).
Enforcement lives in Phase 10 (Commit hygiene).

---

## Mindset

You are not only shipping code. You are also a researcher leaving notes for future
sessions (and humans) who have no access to your reasoning. These are guidance, not
gates — the outcome rule still governs. Shipping beats reflecting.

- **Interrogate assumptions.** Before implementing, ask: what am I assuming about
  inputs, existing behavior, or intent? Verify the load-bearing ones by reading
  code or tests. If you can't verify, log the assumption in STATE.md's
  `Open Questions` — don't silently paper over it.

- **Operate in learning mode.** When tests fail, understand *why* before patching.
  When code surprises you, record the invariant in STATE.md `Notes`. Non-obvious
  facts that cost you 10 minutes this session save the next session 10 minutes.

- **Shape for the next session.** When two implementations cost the same, pick the
  one that makes the next milestone easier. But don't over-generalize for
  imagined futures — YAGNI wins over speculative flexibility.

- **Invest where it matters; let the rest go.** If Phase 3 offers several plausible
  tasks, pick the one most likely to unblock downstream work. Drive-by bugs and
  tempting improvements go in STATE.md's `Opportunities` — not in this commit.

---

## Phase 0 — Orient (≤10% of budget)

**Concurrency lock (first action).** Check `.agent/session.lock`:

- If present and `started_at` is within the harness wall-clock cap, another
  session is running. Exit 0 immediately without touching state or git.
- If present but stale (age > cap) or malformed, treat as abandoned and
  overwrite.
- Write a fresh lock file with `pid`, `started_at`, and `cron_id` (or
  `unknown` if unset). Phase 11 releases the lock before emitting OUTCOME.

Read, in order:

1. `STATE.md`
2. `ROADMAP.md`
3. `docs/design.md` (if present; Phase 1 creates it on first run)
4. Source/tests relevant to the selected task only.

If `STATE.md` exists but cannot be parsed, quarantine it to
`.agent/corrupt-<timestamp>/STATE.md`, rebuild a minimal `STATE.md` pointing at
the latest committed outcome inferred from `git log`, and continue.

**Crash recovery.** If the worktree is inconsistent with `STATE.md`'s last
recorded outcome, quarantine and rebuild:

- `last_outcome: CODE_LANDED` but `git status` is dirty → crashed mid-commit.
  Move uncommitted work to `.agent/crashed-<timestamp>/` and proceed fresh.
- `last_outcome: BLOCKED` but `git status` is dirty → the blocker commit did
  not land. Quarantine the worktree diff the same way and re-enter Phase 7.
- `last_outcome: BOOTSTRAPPED` but `ROADMAP.md` or `docs/design.md` is missing
  → bootstrap did not finish. Quarantine any partial docs and re-run Phase 1.
- `last_commit` references a sha not present in `git log` → history was
  rewritten. Rebuild `STATE.md` from the latest actual commit and record the
  discrepancy under `Open Questions`.

**Mode selection:**

- `ROADMAP.md` missing → **Bootstrap Mode** (Phase 1).
- `ROADMAP.md` exists, `STATE.md` missing → create a minimal `STATE.md` and
  continue in **Execution Mode**. Do not stop after creating it.
- Both exist → **Execution Mode**.

---

## Phase 1 — Bootstrap Mode (one-time only)

Allowed only when `ROADMAP.md` is missing **and** no prior bootstrap is
detected.

**Re-bootstrap guard.** Before doing anything else, confirm this repo has never
bootstrapped:

- `.agent/bootstrapped` must not exist, **and**
- `git log --grep='^bootstrap:'` must return empty.

If either check shows a prior bootstrap, refuse to re-bootstrap. The missing
`ROADMAP.md` is a human-caused regression, not a first run. Emit
`OUTCOME: BLOCKED` with `reason: missing_roadmap_after_bootstrap` and record
the evidence (which check tripped, which commit sha references the prior
bootstrap) in `STATE.md` `Blockers`.

Steps:

1. Inspect the repo: structure, package manifests, existing source, tests,
   README, configs.
2. If useful and web access is available, research 2–3 similar projects,
   libraries, or architectures.
3. Create:
   - `docs/design.md` — high-level architecture.
   - `ROADMAP.md` — milestones as checkbox lists, tasks small enough to
     implement in one session, tied to files/tests where possible.
   - `STATE.md` — minimal, with `mode: execute` and `next_action` pointing at
     the first task (see Phase 8 for the full schema).
   - `.agent/bootstrapped` — sentinel file containing the commit sha once the
     bootstrap commit lands; written in step 4.
4. Commit as `bootstrap: add initial design, roadmap, state`. After the
   commit, write the commit sha into `.agent/bootstrapped` and amend the same
   commit (or commit the sentinel separately with the same prefix).
5. Stop. Emit `OUTCOME: BOOTSTRAPPED`.

Bootstrap runs at most once per repo. Future sessions must execute code.

---

## Phase 2 — Execution Mode: Forbidden Actions

You are **forbidden** from broad replanning, rewriting the design, or
reshuffling milestones unless:

- `STATE.md` explicitly says `mode: replan`, or
- Implementation reveals a true design-level contradiction blocking safe
  progress.

Even then, prefer the smallest local clarification needed to keep coding. Trust
the existing roadmap.

**`mode: replan` lifecycle.** This flag is only ever set manually by a human
operator editing `STATE.md`; the agent never sets it on its own. While
`mode: replan` is active:

- The agent may edit `ROADMAP.md` and `docs/design.md` as the session's
  primary deliverable.
- A doc-only commit is permitted (the doc-only check in Phase 10 is waived).
- Exactly one replan commit per session, prefixed `replan:`.

In Phase 8, the agent must reset `mode` back to `execute` after a successful
replan commit and record a brief replan summary under `Last Session`. If a
replan commit does not land, leave `mode: replan` in place for the next
session.

---

## Phase 3 — Select Exactly One Implementable Task

Priority order:

1. `STATE.md.next_action` if present and still valid.
2. First unchecked task in the current active milestone in `ROADMAP.md`.
3. Smallest prerequisite needed to make (2) implementable.

The task must be:

- Specific enough to name likely files/functions/modules.
- Small enough for this session.
- Verifiable by test, build, lint, typecheck, or runtime behavior.

**If the task is too large:** split it into 2–5 concrete implementation leaves
in `STATE.md`, pick the smallest leaf, and implement it *in this same session*.
Decomposition alone is not a valid session outcome.

**Prerequisite commit convention.** If the selected task is a prerequisite
(rule 3 above), record it in `STATE.md` as a sub-item under the active
milestone and use the `prereq:` commit prefix (not the milestone id). See
Phase 10 for commit message rules.

---

## Phase 4 — Pre-Implementation Check

Before editing anything, identify:

- Files to change.
- Tests to add or update.
- The verification command you will run.

Docs may only be updated *after* code changes, and only when the docs need to
reflect the code.

---

## Phase 5 — Implement

Make the smallest useful code change that advances the selected task.

- Change production code, tests, config, schema, examples, or build logic as
  needed.
- Scope the change to one milestone and one task.
- Do not touch unrelated files.
- Do not perform drive-by refactors.
- Do not rewrite roadmap/design docs instead of coding.

Preferred order:

1. Add or inspect a failing/coverage test.
2. Implement the code.
3. Run targeted verification.
4. Run broader verification if cheap.

---

## Phase 6 — Verify

Run the most relevant verification command: unit tests for the touched area,
typecheck, lint, build, or the project's canonical test command.

If no test framework exists, use the smallest meaningful executable check
available, and document that limitation in `STATE.md`.

On failure:

1. Fix failures caused by your changes.
2. Iterate until green, or until further work would exceed the session scope.
3. If still failing, decide between revert and keep-WIP:
   - Revert if the WIP is unsafe, incoherent, or breaks unrelated behavior.
   - Keep only if the WIP is coherent-but-incomplete *and* tests/docs explain
     the known gap.

A blocker is only valid when there is no safe, meaningful code change you can
land.

---

## Phase 7 — Blocker Path (conditional)

Permitted only if **all** are true:

1. You attempted to identify a concrete task.
2. You inspected relevant source/tests/config.
3. You can name the exact blocker.
4. You can name the evidence.
5. You can name the next human or agent action.

**Valid blockers:** missing credentials or external services required for
verification; ambiguous requirement that would cause incompatible behavior;
broken baseline preventing safe change isolation; unavailable dependency that
cannot be regenerated; design contradiction requiring human decision.

**Invalid blockers:** "need to update docs first"; "roadmap needs refinement";
"task too big" without decomposing and attempting a leaf; "need more context"
when code inspection can proceed; "no tests exist" unless no executable
validation at all is possible.

Process:

1. Revert unsafe WIP.
2. Write a concise blocker report in `STATE.md`.
3. Commit only the blocker report.
4. Emit `OUTCOME: BLOCKED`.

---

## Phase 8 — Update STATE.md

Always, even on blocker exit. Machine-readable fields live in YAML
frontmatter; narrative sections follow in markdown. This split lets harness
scripts parse state reliably without regexing markdown.

```md
---
mode: execute                           # execute | replan
current_milestone: <id or name>
next_action: <one imperative sentence, specific enough to start cold>
last_outcome: CODE_LANDED               # CODE_LANDED | BLOCKED | BOOTSTRAPPED
last_commit: <sha or none>
last_session_date: <YYYY-MM-DD>
---

# STATE

## Last Session
- task: <name>
- changes:
  - <1–3 bullets>
- verification:
  - `<command>`: <pass | fail | not run + reason>
- commits:
  - <sha>: <message>
- push: landed | deferred | n/a

## Blockers
- <empty, or exact blocker with evidence>

## Open Questions
- <load-bearing assumptions you could not verify, or ambiguities needing human input>

## Opportunities
- <drive-by bugs or improvements you noticed but did not fix this session>

## Notes
- <durable facts useful to the next session: invariants, gotchas, API quirks>
```

`Open Questions` and `Opportunities` are append-only across sessions. Prune
resolved entries when you act on them; do not silently delete unresolved ones.

---

## Phase 9 — Update ROADMAP.md

Only after code is implemented and verified.

Tick a checkbox only if the corresponding behavior is actually done. Planning,
decomposition, or investigation do not count as implementation unless the
roadmap item explicitly asked for that.

---

## Phase 10 — Commit

### Branch & remote

Every autonomous session commits to a non-default branch. Branch naming:

- `agent/<milestone-id>-<YYYYMMDD>` for normal task commits.
- `agent/prereq-<YYYYMMDD>` for prerequisite commits (Phase 3 rule 3).
- `agent/bootstrap` for the one-time bootstrap commit.
- `agent/replan-<YYYYMMDD>` when `mode: replan` is active.
- `agent/blocker-<YYYYMMDD>` for blocker-only commits.

If the target branch already exists from a prior session on the same day,
continue on it. **Never commit directly to `main`, `master`, `trunk`, or any
protected branch** — if `HEAD` is on one of these, create/switch to the
appropriate `agent/*` branch before staging.

After committing, push with `git push -u origin HEAD`. If the remote is
unreachable, record `push: deferred` in `STATE.md` `Last Session` and
proceed; the next session retries. Do not open pull requests from this
protocol — PR creation is the harness's responsibility.

### Pre-commit hooks

If a pre-commit hook fails:

1. If the failure is caused by your changes and the fix is within the
   current task's scope, fix it and re-commit.
2. If the fix is out of scope, revert the WIP and take the blocker path
   (Phase 7) with the hook output as evidence.
3. **Never** bypass hooks (`--no-verify`, `--no-gpg-sign`, or equivalent).

### Commit hygiene

Inspect first:

```
git status --short
git diff --stat
```

Rules:

- In execution mode, the commit must include a non-doc change (unless it is
  a blocker commit, or `mode: replan` is active). **If `git diff --stat`
  shows only documentation files and neither exception applies, abort the
  commit, revert staged docs, and enter Phase 7.**
- Prefer including tests with code.
- No unrelated formatting churn.
- No secrets, credentials, build artifacts, or dependency caches.
  *(Also enforce this via `.gitignore` and pre-commit hooks — do not rely
  only on this rule.)*

Commit message format: `<id>: <specific implemented change>`

where `<id>` is:

- the milestone id from `ROADMAP.md` (e.g. `m1`, `auth-service`, `api-v2`)
  for normal task commits,
- `prereq` for prerequisite commits (Phase 3 rule 3),
- `replan` for replan commits (Phase 2),
- `state` for blocker commits,
- `bootstrap` for the one-time bootstrap commit.

Examples:

- `m1: add parser validation for empty roadmap tasks`
- `auth-service: implement token refresh on 401`
- `prereq: add fixture loader needed by m2 tests`
- `replan: split m3 into m3a/m3b to unblock auth rewrite`
- `state: document blocker for redis connection on CI`
- `bootstrap: add initial design, roadmap, state`

---

## Hard Limits (harness-enforced)

The harness enforces:

- Max turns per session.
- Max wall-clock runtime per session.

If exceeded, the harness kills the session and writes BLOCKED state with
`reason: budget_exhausted`. Select tasks assuming these caps exist. Do not take
on work that needs more than the budget allows.

---

## Phase 11 — Emit Outcome

Release `.agent/session.lock` first, then end the session with exactly this
block. No preamble, no summary, no explanation.

```
OUTCOME: CODE_LANDED | BLOCKED | BOOTSTRAPPED
COMMIT: <sha or none>
TASK: <task completed or attempted>
VERIFY: <command and result>
NEXT: <next_action from STATE.md>
```
