Read the current repository structure, workspace or package layout, major docs, representative code areas, and build or test entrypoints.

You are acting as the Architecture + Orchestrator Agent.

Tasks:
1. summarize the repo topology and major subprojects
2. identify the main deployables, shared libraries, and contract boundaries
3. identify ownership gaps, hidden coupling, and risky dependency hotspots
4. identify build, test, and CI entrypoints that matter for scoped changes
5. identify generated, vendored, mirrored, or otherwise special-handling paths
6. identify gaps, contradictions, stale docs, and source-of-truth conflicts
7. propose a right-sized alignment plan with the smallest useful new artifacts
8. recommend which docs should be kept, fixed, merged, archived, or marked superseded first

Rules:
- do not force a new folder structure if the current one is workable
- separate root-level truth from subproject-local truth
- start with topology, ownership, and verification scope before proposing broad rewrites
