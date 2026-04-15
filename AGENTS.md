# AGENTS.md

## Purpose
Defines role separation and coordination rules for multi-agent development.

---

## Agent Types

### 1. Orchestrator Agent
Owns:
- decomposition
- task assignment
- dependency awareness
- milestone tracking
- status updates

### 2. Architecture Agent
Owns:
- system design
- module boundaries
- ADR drafting
- impact analysis
- migration strategy

### 3. Implementation Agent
Owns:
- bounded coding tasks
- tests
- local docs updates
- assumptions/risk recording
- handoff output

### 4. Review Agent
Owns:
- code quality review
- architecture compliance review
- risk review
- test adequacy review

---

## Standard Delivery Flow
1. Orchestrator defines task packet
2. Architecture agent validates design impact if needed
3. Implementation agent executes bounded task
4. Review agent checks output
5. Orchestrator integrates and updates status

---

## Required Handoff
Every meaningful task should produce:
- objective
- scope
- files changed
- assumptions
- decisions
- blockers
- next step recommendation
