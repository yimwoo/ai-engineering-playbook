# AGENTS.md

## Agent Roles
### Orchestrator
Maintains roadmap, status, task decomposition, and integration decisions.

### Architecture Agent
Produces specs, ADRs, impact analyses, and migration guidance.

### Implementation Agent
Executes bounded tasks, updates tests/docs, and records assumptions.

### Review Agent
Checks correctness, architecture compliance, tests, and hidden risks.

## Standard Flow
1. Orchestrator defines task packet
2. Architecture agent validates design impact if needed
3. Implementation agent executes bounded task
4. Review agent evaluates output
5. Orchestrator integrates and updates status
