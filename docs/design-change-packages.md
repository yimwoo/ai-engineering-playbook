# Design Change Packages

## Purpose
A design-change package is a structured proposal and impact plan for meaningful changes to roadmap, architecture, or delivery sequencing.

Use one when a change affects:
- multiple modules
- milestone structure
- architecture
- major scalability/reliability assumptions
- observability or failover posture
- security model
- migration strategy

## Why It Exists
Large changes often fail when teams jump directly into implementation.
A design-change package creates a safer path:
1. explain the change
2. analyze impact
3. compare options
4. decide intentionally
5. update source-of-truth docs
6. then execute in bounded tasks

## Typical Outputs
- a change package document
- updated architecture.md if needed
- updated roadmap.md if needed
- updated status.md
- one or more ADRs if durable design decisions changed
- new task packets for the approved transition

## Recommended Structure
Use `templates/design-change-package-template.md`.
