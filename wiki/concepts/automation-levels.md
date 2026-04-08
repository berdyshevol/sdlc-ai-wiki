---
title: Automation Levels in Software Development
type: concept
pillar: industry
created: 2026-04-08
updated: 2026-04-08
sources: [five-levels-shapiro, superpowers-5, coding-agents-conf-2026, dex-rpi-to-crispy]
tags: [maturity-model, levels, progression, role-transformation, trust-ladder, adoption]
---

# Automation Levels in Software Development

## Definition

A maturity model describing the **progression from fully manual coding to fully autonomous software generation**. The most developed framework comes from [[five-levels-shapiro]], which defines five levels (0-5) modeled on autonomous driving levels. The key insight: each level represents a **role transformation**, not just a productivity increase.

## The Five Levels (Shapiro Framework)

| Level | Name | Human Role | AI Role |
|-------|------|-----------|---------|
| 0 | Manual | Coder | None |
| 1 | Assisted | Coder + AI for tasks | Task executor |
| 2 | Collaborative | Pair programmer | Pair programmer |
| 3 | Managed | Code reviewer/manager | Primary coder |
| 4 | Autonomous | PM/spec writer | Full implementer |
| 5 | Dark Factory | Not involved | Everything |

## Key Sources

- [[five-levels-shapiro]] — The primary framework (theoretical)
- [[superpowers-5]] — Describes practices at Level 3-4
- [[12-factor-agents]] — Principles that enable Level 3-4 agent architectures
- **[[coding-agents-conf-2026]]** — Kilo Code's **empirical trust ladder** from 25T tokens / 1.5M developers: Autocomplete → Chat → Single Agents → Orchestration. First large-scale data validating a progression model.
- **[[dex-rpi-to-crispy]]** — Argues Level 3 (managed, 2-3x speedup) is the sweet spot for production code. Explicitly skeptical of Level 4-5 for production SaaS: "10x speed doesn't matter if it's slop."

## Kilo Code Trust Ladder (Empirical)

Data from 25T tokens across 1.5M+ developers provides an empirical complement to Shapiro's theoretical framework:

| Rung | Trust Signal | Latency | Signal Quality | ~Shapiro Level |
|------|-------------|---------|---------------|----------------|
| Autocomplete | Tab / dismiss | 200ms | Clean, high-volume | Level 1 |
| Chat | Copy / ignore / follow-up | Seconds | Moderate, noisier | Level 2 |
| Single Agents | Accept diff / revert / edit | Minutes | Sparse, high-stakes | Level 3 |
| Orchestration | Workflow outcome | Hours | Delayed, complex | Level 4 |

Key finding: **"If autocomplete fails, agents never get a chance."** Trust is sequential — you can't skip rungs. Three slow autocomplete suggestions → feature disabled → agents never trusted.

Three consistent adoption breakpoints: (1) Context construction, (2) Model routing, (3) Feedback loops.

## Current Understanding

The model is useful for **diagnosing where teams are and what the next transition looks like**. The Kilo Code data now provides empirical validation. Key observations:

- **The Level 2 trap:** ~90% of developers stop here, thinking they've maximized AI benefits. The collaborative feeling masks the fact that higher levels exist.
- **Level 2→3 is the hardest transition:** It requires giving up control and accepting initially worse-looking output. This is psychologically difficult.
- **Level 3→4 requires [[spec-driven-development]]:** You can't operate at Level 4 without robust specifications
- **Level 5 may not be a single threshold** — it likely requires different capabilities for different types of software

## Open Questions

- Is this model sequential, or can you skip levels?
- Is the model complete? Are there intermediate levels (e.g., 3.5)?
- Does the level depend on the task (greenfield vs. debugging vs. refactoring)?
- How do you measure what level a team is at?

## Related Concepts

- [[spec-driven-development]] — enables Level 4+
- [[software-factory]] — Level 5 is the software factory
- [[code-legibility-debate]] — each level implies different code reading expectations
- [[human-in-the-loop]] — the human's role changes at each level
