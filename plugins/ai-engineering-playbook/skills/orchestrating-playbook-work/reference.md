# Orchestration Reference

## Latest Handoff Discovery
Use this order:
1. explicit file path named by the user
2. newest file in `handoffs/`
3. `status.md` or `STATE.md` last-session section
4. recent task packet completion notes
5. recent git commits only when repo files do not answer the question

## Role Separation
The same model may perform several roles, but it should keep the responsibilities distinct:
- Orchestrator: decomposition, dependency awareness, milestone tracking, status updates
- Architecture: design impact, module boundaries, ADRs, migration strategy
- Implementation: bounded code/docs changes, tests, assumptions, handoff
- Review: quality, architecture compliance, risk, test adequacy

## Session Shape
For a meaningful task, produce:
- context summary
- impact analysis
- blocker-level questions only
- bounded plan
- changes made
- verification
- risks and follow-ups
- handoff

## Portability Rule
Plugin behavior can improve Claude Code ergonomics, but project memory must stay in ordinary repository files so another agent can continue from the same state.
