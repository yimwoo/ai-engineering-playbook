# repo-map.md

## Purpose
Describe the repository topology so humans and AI agents can understand how the repo is organized before making changes.

## Repository Topology
- root apps or services
- shared packages or libraries
- infrastructure or deployment directories
- docs and design areas
- generated, vendored, mirrored, or external-code paths

## Major Subprojects
For each major subproject, include:
- path
- purpose
- owner or owning team
- deployable or library
- key dependencies
- downstream consumers
- primary build and test commands
- local instruction or contract docs

## Shared Libraries and Contracts
- shared packages
- APIs
- events
- schemas
- other contracts that affect multiple subprojects

## Do-Not-Touch or Special-Handling Areas
- generated code
- vendored code
- third-party mirrors
- regulated or high-risk paths

## Key Entry Points
- main app entrypoints
- build entrypoints
- CI entrypoints
- test entrypoints
- release or deployment entrypoints

## High-Risk Integration Points
- shared data boundaries
- auth boundaries
- cross-service contracts
- infrastructure assumptions

## Open Questions
- unresolved ownership gaps
- unclear boundaries
- risky dependency hotspots
