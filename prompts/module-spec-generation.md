Read:
- PROJECT_CONSTITUTION.md
- CLAUDE.md
- architecture.md
- status.md
- relevant ADRs
- existing code or docs for the target area

You are acting as the Architecture Agent.

Task:
Generate or update a module specification for [module name].

Please:
1. summarize the module's purpose in the system
2. define responsibilities and non-responsibilities
3. identify owned data and public interfaces
4. identify upstream dependencies and downstream dependents
5. define invariants, failure modes, and security notes
6. define observability and testing expectations
7. identify open questions and likely future pressure points

Rules:
- avoid vague module boundaries
- make ownership explicit
- do not invent architecture that conflicts with the current system state
