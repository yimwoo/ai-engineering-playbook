# technical-debt.md

## Purpose
Track intentional shortcuts and deferred structural improvements.

### TD-001
- Date: 2026-04-15
- Severity: D1
- Area: reporting
- Current Shortcut: use direct reads from transactional tables for initial reporting views
- Why Acceptable Now: speeds up milestone 2 delivery
- Risk Introduced: later reporting isolation may require refactor
- Upgrade Path: introduce reporting projection layer when reporting load increases
- Trigger for Revisiting: performance or ownership issues emerge
- Target Milestone: Milestone 3
- Owner/Status: architecture / open
