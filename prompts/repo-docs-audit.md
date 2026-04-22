Inspect the repository's agent-facing documentation and workflow files only.

You are reviewing this repository to improve how well AI coding agents can work in it across repeated sessions.

Goal:
- make the repo faster for a fresh agent to understand
- reduce repeated context loading
- improve agent workflow clarity
- improve scalability for larger repos, multi-module repos, and worktree-based workflows

Focus especially on:
- `AGENTS.md` or `AGENT.md`
- `CLAUDE.md`
- `CODEX.md`
- `README.md`
- `CONTRIBUTING.md`
- `docs/**/*.md`
- onboarding, workflow, environment, worktree, and repo-navigation docs

Hard scope boundary:
- do not review or modify application or source code unless needed to confirm a command name, path, or source-of-truth reference
- focus on markdown, text docs, and agent workflow guidance only
- do not spend time on code quality, refactors, tests, or implementation details in source files

Review the docs from the perspective of a code agent that may:
- start in a fresh session with no prior memory
- need to understand the repo quickly
- work across multiple sessions on the same machine
- use git worktrees
- operate in a large repo, monorepo, or future multi-repo setup
- need clear instructions on where to look and what not to touch
- need to avoid loading unnecessary context

Evaluate the current docs for:
1. fast orientation
2. session efficiency
3. agent workflow quality
4. context minimization
5. scalability
6. worktree and multi-checkout support
7. actionability

When evaluating, look for:
- whether there is a clear start-here path
- whether root docs are concise and linked to deeper docs instead of duplicating them
- whether repo layout, module layout, and source-of-truth boundaries are clear
- whether planning, editing, validation, handoff, and review expectations are explicit
- whether stale or overlapping docs create ambiguity
- whether commands are copy-pasteable and paths still look accurate
- whether parallel agent sessions or worktree pitfalls are documented

Deliverables:

A. Findings summary
- summarize the highest-impact documentation problems first

B. Gap analysis
- identify missing sections or missing files that would materially improve agent effectiveness
- examples: start-here doc, repo map, worktree guide, module index, glossary, session handoff template, doc ownership guidance

C. Cleanup recommendations
- list files that should likely be merged, split, renamed, archived, deleted, or linked from a central index
- explain each recommendation in terms of agent usability and context efficiency

D. Proposed documentation structure
- recommend a target structure that scales to larger repos, more modules, more services, or sibling repos

E. Concrete edits
- draft improved content for the highest-value files first
- prioritize:
  1. root-level agent instruction file
  2. root `README.md`
  3. a short `docs/index.md` or `docs/START_HERE.md`
  4. worktree workflow guidance
  5. session handoff template

F. Minimal session bootstrap
- produce a short fresh-session bootstrap section, ideally under 300 words, that tells a new agent what this repo is, where to start, which docs to read first, and how to avoid loading too much context

G. Suggested repo standards
- recommend a small durable set of standards for future docs
- examples: maximum root doc length, when to add a new doc, source-of-truth rules, required sections, how to document subprojects, how to write docs for AI agents versus humans

Editing rules:
- prefer concise, high-signal writing
- prefer explicit bullets and checklists where operational clarity matters
- avoid duplicating the same guidance across multiple files
- centralize durable rules and link to volatile details
- preserve useful project-specific detail
- mark uncertain items as `needs verification`

Output format:
1. audit summary
2. prioritized recommendations
3. proposed file tree for docs
4. draft patches or rewritten markdown for the most important files
5. optional deletions or consolidations
6. open questions or items needing verification

Execution mode:
1. inspect the existing documentation structure and summarize what exists
2. propose a plan
3. make doc edits only after the plan is clear
4. explain the rationale for edits briefly when making them
