# Tool Comparison Notes

Use this file to compare behavior across Claude Code, Codex, and other code agents.

## Compare By
- planning quality
- code generation quality
- refactoring reliability
- test-writing quality
- architecture reasoning
- context retention
- instruction-following
- review quality
- speed / ergonomics

## Claude Code
- strengths:
  - often stronger at planning and architecture reasoning
  - usually better at long-form explanation and design tradeoff discussion
  - helpful for drafting design-change packages, repo audits, and milestone planning
- weaknesses:
  - can become verbose
  - may ask too many sequential clarifying questions if not constrained
  - may propose reasonable shortcuts that later need stronger debt tracking
- best use cases:
  - architecture analysis
  - milestone planning
  - roadmap or design change discussion
  - documentation drafting
  - review summaries

## Codex
- strengths:
  - often efficient for bounded code edits and implementation loops
  - useful for direct execution against clear task packets
  - good fit for focused refactors, coding tasks, and test updates
- weaknesses:
  - may be less strong in long-form architecture narrative or strategic decomposition
  - Claude-specific habits, commands, or plugin assumptions may not transfer well
  - may need clearer repo-based context to avoid shallow execution
- best use cases:
  - bounded implementation tasks
  - refactors
  - tests
  - diff-oriented work
  - focused code changes after planning is already clear

## Cross-Agent Rules That Still Work
- repo docs should remain the source of truth
- task packets should define bounded work
- status and handoffs should be updated before switching agents
- architecture and ADRs should remain in repo docs, not chat memory
- technical debt should be logged when shortcuts are taken

## Agent-Specific Tricks To Keep Optional
- Claude Code-specific prompt shaping
- tool-specific command shortcuts
- plugins and hooks that do not transfer cleanly to other agents

## Initial Comparison Summary
A practical default workflow is:
- use Claude Code more for planning, architecture, and design-heavy reasoning
- use Codex more for bounded implementation and execution
- keep the repo memory and operating model shared across both
