---
title: Software Factory
type: concept
pillar: software-factories
created: 2026-04-08
updated: 2026-04-08
sources: [five-levels-shapiro, superpowers-5, everything-is-a-ralph-loop]
tags: [automation, autonomous, dark-factory, production-pipeline]
---

# Software Factory

## Definition

A software factory is a **fully or near-fully automated system for producing software** — analogous to a manufacturing factory where raw materials (requirements/specs) go in and finished products (working software) come out, with minimal or no human intervention during the production process.

The term "Dark Factory" (from [[five-levels-shapiro]]) references Fanuc's lights-out robot factories that operate without human workers present. Applied to software, it means AI systems that can take a specification and produce working, tested, deployed software without a human in the loop.

## Key Sources

- [[five-levels-shapiro]] — Level 5 ("Dark Factory") is the software factory vision
- [[superpowers-5]] — The cascade pattern (spec → implement → review) is a proto-factory pipeline
- [[everything-is-a-ralph-loop]] — Geoffrey Huntley's "level 9" vision: autonomous loops that evolve products and optimize for revenue. The most extreme articulation of the software factory concept. Introduces The Weaving Loom as infrastructure for evolutionary software.
- The Software Factory (lukepm.com) — dedicated article on this concept (to be fully ingested)

## Current Understanding

The software factory vision sits at the **far end of the automation spectrum**. Based on current sources:

**What it requires:**
- Robust [[spec-driven-development]] — specs must be precise enough for autonomous execution
- Multi-agent orchestration — different agents handling different pipeline stages
- Comprehensive automated testing — the primary quality gate when no human reviews code
- Self-healing capabilities — agents that can diagnose and fix their own failures

**Where we are today:**
- Shapiro claims Level 5 has been achieved only by very small teams (<5 people)
- Most teams operate at Level 2 — collaborative coding, far from factory automation
- The [[superpowers-5]] cascade pattern represents a middle ground — structured but still human-supervised
- Products like [[devin]] aim for autonomous coding but reviews suggest they still need significant oversight
- Geoffrey Huntley ([[everything-is-a-ralph-loop]]) claims to have achieved "evolutionary software auto-heal" — self-repairing systems under autonomous Ralph loops — and extends the automation levels to 8-9, with level 9 being fully autonomous revenue-optimizing software factories

**The pipeline model:**
```
Spec → Plan → Implement → Test → Review → Deploy
  ↑                                         |
  └─────── feedback loop ──────────────────┘
```

Each stage could be handled by specialized agents ([[12-factor-agents]] Factor #10: Small, Focused Agents).

## Open Questions

- Is the factory metaphor actually appropriate? Software is not manufacturing — requirements are ambiguous, domains are complex, edge cases are infinite
- Can software factories handle maintenance and evolution, or only greenfield?
- What's the minimum viable factory? What subset of the pipeline must be automated first?
- How do software factories handle security, compliance, and other non-functional requirements?
- Is there a "valley of death" between Level 3 and Level 5 where the investment doesn't pay off?

## Related Concepts

- [[spec-driven-development]] — the input mechanism for software factories
- [[automation-levels]] — the progression toward factory automation
- [[human-in-the-loop]] — the tension between full automation and human oversight
- [[code-legibility-debate]] — factories produce code humans may never read
- [[agentic-development]] — the agent patterns that enable factory pipelines
