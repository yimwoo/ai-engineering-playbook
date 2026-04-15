# PROJECT_CONSTITUTION.md

## Purpose
This repository defines reusable operating patterns for AI-assisted software engineering.

The same principles should be applied when adapting these templates into a real project repo.

This constitution exists to preserve:
- architectural integrity
- decision continuity
- delivery discipline
- maintainability over time
- reliable collaboration between humans and AI agents

---

## Core Principles

### 1. Repo docs are the memory, not chat history
No important decision should live only in a chat session.

### 2. Bounded work beats broad autonomy
Agents should work in bounded scopes with explicit constraints.

### 3. Architecture is a first-class artifact
Architecture should not be changed silently.

### 4. Shortcuts must be visible
A shortcut is allowed only if its rationale, risk, and revisit trigger are documented.

### 5. “Done” includes docs, tests, and operational thinking
A feature is not complete if docs and operational considerations are omitted.

### 6. Ask humans only for high-leverage decisions
Humans should resolve major tradeoffs, not minor implementation details.

### 7. Parallel work requires contract discipline
Parallel agents may work independently only when boundaries are clear.

### 8. Favor evolutionary architecture over speculative complexity
Do not overbuild too early, but do not neglect expensive-to-reverse foundations.

---

## Repository Goals
This repo should help users:
- bootstrap AI-assisted development workflows
- introduce governance into agent workflows
- manage long-lived software delivery with better context continuity
- adopt a document-driven process incrementally

---

## Required Artifacts for Example Projects
A mature project repo adopting this playbook should usually include:
- `PROJECT_CONSTITUTION.md`
- `CLAUDE.md`
- `AGENTS.md`
- `architecture.md`
- `roadmap.md`
- `status.md`
- `technical-debt.md`
- module specs
- ADRs
- task packets
- handoffs

---

## Prohibited Behaviors
- silent architecture drift
- undocumented breaking contract changes
- undocumented schema changes
- claiming future “v2” fixes without tracking them
- treating partial work as complete
- relying on chat memory instead of repo memory

---

## Operational Goal
The system and its documentation should remain understandable, evolvable, and supportable by future humans and future agents.
