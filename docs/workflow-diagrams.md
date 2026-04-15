# Workflow Diagrams (Text Version)

This document provides lightweight text diagrams that explain the playbook's workflow.

These are intentionally simple and portable so they work well in Markdown and across tools.

---

## 1. Core operating model

```text
Human goals + constraints
          ↓
Source-of-truth repo docs
(architecture, roadmap, status, ADRs, debt, task packets)
          ↓
Code agent reads repo context
          ↓
Bounded task execution
          ↓
Docs/status/handoff updates
          ↓
Next session or next agent starts from repo memory
```

---

## 2. Mixed-agent workflow

```text
Claude Code / Codex / other agent
            ↓
   Read same repo memory
            ↓
  Work on bounded task packet
            ↓
 Update status + handoff + debt if needed
            ↓
 Another agent can continue safely
```

---

## 3. Large change workflow

```text
Problem or new requirement
          ↓
Impact analysis
          ↓
Design-change package
          ↓
Decision / ADR updates
          ↓
Roadmap + architecture updates
          ↓
Bounded implementation tasks
          ↓
Status + handoff updates
```

---

## 4. Daily improvement loop

```text
Real project usage
       ↓
Notes / observations / comparisons
       ↓
Patterns / retros / experiments
       ↓
Promote proven ideas into docs/prompts/templates
       ↓
Better future workflow
```

---

## 5. Portable workflow rule

```text
Tool-specific optimization = optional
Repo memory and workflow artifacts = required
```

---

## Recommendation
If you later want richer visuals, these text diagrams can be converted into Mermaid or image-based diagrams.
