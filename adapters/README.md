# Agent Adapters

This directory explains how to use the playbook with specific code agents without making the repo depend on any single one.

## Principle
The source of truth should remain in portable repo artifacts:
- markdown docs
- prompts
- task packets
- handoffs
- ADRs
- status files

Adapter docs should explain how to map the generic operating model onto a tool, not replace the generic model.

## Included Adapters
- `claude-code.md`
- `codex.md`

## Rule
If an agent-specific feature is useful, treat it as an optional acceleration layer.
Do not let it become the only way the workflow works.
