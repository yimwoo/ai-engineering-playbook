# Operating Model

## Core Idea
Use code agents as bounded contributors operating inside a governed project system.

## Why This Works
Large projects fail with agents when:
- project memory lives only in chat
- architecture is implicit
- milestones are vague
- tasks are too broad
- shortcuts are not tracked
- parallel work lacks boundaries

This playbook addresses those issues with explicit documentation and role separation.

## Roles
### Human
Owns business priorities, major tradeoffs, approvals, and irreversible decisions.

### Orchestrator Agent
Owns milestone planning, decomposition, and status alignment.

### Architecture Agent
Owns design analysis, ADR drafting, and migration thinking.

### Implementation Agent
Owns bounded execution within clear scope.

### Review Agent
Owns quality, compliance, and hidden-risk detection.

## Core Artifacts
- constitution
- agent instructions
- architecture
- roadmap
- status
- module specs
- ADRs
- technical debt
- task packets
- handoffs
- design-change packages

## Living Docs
Architecture and roadmap should exist early, but they are living documents.
Major changes should go through a design-change package before implementation.
