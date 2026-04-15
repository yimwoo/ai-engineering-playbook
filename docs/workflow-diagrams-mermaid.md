# Mermaid Workflow Diagrams

These diagrams are a richer visual version of `docs/workflow-diagrams.md`.

They are kept in Mermaid so they remain versionable and Markdown-friendly.

---

## 1. Core operating model

```mermaid
flowchart TD
    A[Human goals and constraints] --> B[Source-of-truth repo docs]
    B --> C[Architecture / Roadmap / Status / ADRs / Debt / Task Packets]
    C --> D[Code agent reads repo context]
    D --> E[Bounded task execution]
    E --> F[Docs / Status / Handoff updates]
    F --> G[Next session or next agent starts from repo memory]
```

---

## 2. Mixed-agent workflow

```mermaid
flowchart TD
    A[Claude Code / Codex / Other agent] --> B[Read same repo memory]
    B --> C[Work on bounded task packet]
    C --> D[Update status / handoff / debt if needed]
    D --> E[Another agent can continue safely]
```

---

## 3. Large change workflow

```mermaid
flowchart TD
    A[Problem or new requirement] --> B[Impact analysis]
    B --> C[Design-change package]
    C --> D[Decision / ADR updates]
    D --> E[Roadmap and architecture updates]
    E --> F[Bounded implementation tasks]
    F --> G[Status and handoff updates]
```

---

## 4. Daily improvement loop

```mermaid
flowchart TD
    A[Real project usage] --> B[Notes / observations / comparisons]
    B --> C[Patterns / retros / experiments]
    C --> D[Promote proven ideas into docs / prompts / templates]
    D --> E[Better future workflow]
```

---

## 5. Portable workflow rule

```mermaid
flowchart LR
    A[Tool-specific optimization] --> B[Optional]
    C[Repo memory and workflow artifacts] --> D[Required]
```
