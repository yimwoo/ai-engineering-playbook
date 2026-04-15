# architecture.md

## System Overview
A long-lived business platform with multiple modules, cross-cutting concerns, and strong requirements for maintainability.

## Architectural Style
Modular monolith initially, with explicit module boundaries and asynchronous workflows where needed.

## Core Modules
- identity-access
- core-domain
- workflow-orchestration
- reporting
- notifications
- audit-traceability

## Architectural Rules
- module boundaries must be explicit
- cross-module contracts must be visible
- operational concerns must be considered in design decisions
- architecture changes require explicit documentation

## Pending Decisions
- future extraction candidates if scale or team topology changes
- long-term eventing approach
