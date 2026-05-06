# Planning Reference

## Choose the Planning Level
Use a bounded task when:
- one module or small file set changes
- success can be verified locally
- no architecture decision changes

Use a phase plan when:
- several bounded tasks share one milestone goal
- the work can be delivered incrementally
- each task still has local verification

Use a design-change package when:
- architecture, roadmap, scaling, failover, data ownership, security model, or migration strategy changes
- multiple modules or teams are affected
- rollback, sequencing, or risk review matters

## Good Task Boundaries
A good task:
- can be completed in one focused session
- names the acceptance signal
- records what is intentionally out of scope
- leaves room for implementation judgment without hiding the goal

## Before Coding
Confirm:
- source-of-truth docs were read
- implementation scope is narrow
- likely files are named
- tests or checks are known
- handoff fields are required
- blocker-level unknowns are surfaced
