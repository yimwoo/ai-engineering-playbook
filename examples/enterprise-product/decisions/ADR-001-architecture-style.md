# ADR-001: Modular Monolith First

## Status
Accepted

## Context
The project needs strong coherence across modules while architecture and domain boundaries are still evolving.

## Decision
Adopt a modular monolith first, with explicit boundaries and the option to extract services later if justified.

## Alternatives Considered
- service-oriented architecture from the start
- ad hoc modularity without formal boundaries

## Consequences
### Positive
- lower coordination cost early
- easier refactoring while the domain is still being learned

### Negative
- future extraction may require careful separation work

## Follow-up Actions
- document module boundaries clearly
- track extraction candidates over time
