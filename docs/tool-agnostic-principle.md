# Tool-Agnostic Principle

This repository should remain useful across multiple code agents, including Claude Code, Codex, and future tools.

## Why this matters
Different code agents vary in:
- supported commands
- plugin ecosystems
- memory behavior
- context handling
- tool integrations
- formatting preferences
- instruction-following style

If the workflow depends too heavily on one agent-specific feature, it becomes fragile.

## Rule
Prefer patterns that can work across agents:
- repo-based memory instead of chat memory
- markdown docs instead of tool-specific hidden state
- task packets instead of one-off prompts
- handoffs instead of relying on session continuity
- ADRs and status files instead of proprietary memory features

## Allowed Agent-Specific Optimizations
Agent-specific additions are allowed only if:
- they are clearly optional
- the generic workflow still works without them
- they do not become the single source of truth

## Preferred Strategy
Build the generic operating model first.
Then add small tool-specific adapters only where they create clear value.
