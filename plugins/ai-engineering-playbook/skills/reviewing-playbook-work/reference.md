# Review Reference

## Finding Priorities
Report in this order:
1. correctness bugs or behavioral regressions
2. security, privacy, or data integrity risk
3. architecture or source-of-truth drift
4. missing or weak verification
5. incomplete status, task packet, technical debt, or handoff updates

## Evidence
Ground each finding in:
- file and line references
- violated acceptance criteria
- failing or missing verification
- mismatch with architecture, ADR, module, roadmap, or task-packet docs

## Output Shape
Use:
1. findings, ordered by severity
2. open questions or assumptions
3. brief change summary
4. verification gaps or residual risk

If there are no findings, say that clearly and still name any remaining test gaps or residual risk.
