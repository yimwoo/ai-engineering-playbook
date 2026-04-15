# Agent Evaluation Scorecard

## Purpose
Use this scorecard to compare Claude Code, Codex, and other code agents against your actual workflow needs.

This is not a benchmark for hype.
It is a practical evaluation tool for deciding whether an agent fits your operating model.

---

## How to use
1. run the agent on real bounded tasks
2. score behavior based on actual workflow performance
3. add notes for strengths, failure modes, and required adaptations
4. decide whether to keep, adapt, or reject the agent for your workflow

---

## Scoring scale
- 1 = poor fit
- 2 = weak
- 3 = acceptable
- 4 = strong
- 5 = excellent

---

## Evaluation table

| Dimension | Score (1-5) | Notes |
|---|---:|---|
| Reads repo docs before acting |  |  |
| Follows project instructions reliably |  |  |
| Keeps work bounded to scope |  |  |
| Handles architecture constraints well |  |  |
| Writes useful implementation plans |  |  |
| Asks high-value clarifying questions only |  |  |
| Avoids silent architecture or contract drift |  |  |
| Produces usable code changes |  |  |
| Writes or updates tests appropriately |  |  |
| Updates docs/status/handoffs reliably |  |  |
| Works well with task packets |  |  |
| Handles review tasks well |  |  |
| Preserves quality under long sessions |  |  |
| Works well in mixed-agent workflows |  |  |
| Requires minimal tool-specific magic |  |  |

---

## Summary fields
### Agent name

### Best use cases
- item

### Weak spots
- item

### Required adaptations
- item

### Keep / Adapt / Reject

### Recommended role in workflow
Examples:
- planning
- architecture
- implementation
- review
- refactor
- status maintenance

---

## Practical rule
Do not choose a code agent only because it is impressive in demos.
Choose it because it works reliably inside your repo-based operating model.
