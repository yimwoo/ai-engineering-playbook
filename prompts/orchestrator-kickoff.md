Read:
- PROJECT_CONSTITUTION.md
- CLAUDE.md
- AGENTS.md
- architecture.md
- roadmap.md
- status.md
- relevant module specs
- relevant ADRs

You are acting as the Orchestrator Agent.

Goal:
Plan execution for the current milestone.

Tasks:
1. summarize the current project state
2. identify blockers, assumptions, and risks
3. identify the current milestone scope and exit criteria
4. break the milestone into bounded implementation tasks
5. identify which tasks can run in parallel safely
6. identify what needs human input before implementation
7. propose the top 3 next tasks in execution order

Rules:
- do not start coding yet
- do not broaden scope
- call out any outdated docs or architecture mismatches
- separate blockers from assumptions
