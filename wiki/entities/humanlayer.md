---
title: HumanLayer
type: entity
pillar: coding-agents
created: 2026-04-08
updated: 2026-04-11
sources: [12-factor-agents, humanlayer-codelayer, agent-control-plane, dex-rpi-to-crispy, matt-pocock-dex-horthy-chat]
tags: [company, tools, orchestration, open-source, crispy, rpi]
---

# HumanLayer

## Overview

HumanLayer is a company/organization founded by **Dex (dexhorthy)** focused on building tools for AI-assisted software development. They are one of the most prolific contributors to the AI coding agent ecosystem, with a coherent product stack spanning principles, IDE tooling, and infrastructure.

**Website:** [humanlayer.dev](https://humanlayer.dev)
**GitHub:** [github.com/humanlayer](https://github.com/humanlayer)

## Product Stack

HumanLayer's products form a **layered architecture** for AI-assisted development:

| Layer | Product | Purpose | Stars |
|-------|---------|---------|-------|
| Principles | [[12-factor-agents]] | Design methodology for production agents | ~19.2k |
| Methodology | [[dex-rpi-to-crispy\|CRISPY]] | 7-stage coding workflow (evolved from RPI) | — |
| IDE | [[humanlayer-codelayer\|CodeLayer]] | Developer interface for orchestrating agents | ~10.3k |
| Infrastructure | [[agent-control-plane\|ACP]] | Kubernetes-native agent runtime | ~384 |

This is notable because most players in this space offer only one layer. HumanLayer provides the full stack: **how to think about agents** (12-factor) → **how to work with agents** (CRISPY) → **how to interact with agents** (CodeLayer) → **how to run agents** (ACP).

### RPI → CRISPY Evolution

HumanLayer's original methodology was **Research/Plan/Implement (RPI)**, which gained wide adoption (10,000+ users, 9.5k GitHub stars, talks with 350k+ views). After rolling it out to thousands of engineers from startups to Fortune 500s, Dex publicly admitted to three key failures and evolved RPI into **CRISPY** — see [[dex-rpi-to-crispy]] for full details.

Key evolution: single monolithic 85-instruction prompt → seven focused stages with <40 instructions each. Also includes a major reversal on code legibility: HumanLayer now advocates reading the code, not just the plan.

### CodeLayer rebuild (Dec 2025 → Jan 2026)

Per [[matt-pocock-dex-horthy-chat]], HumanLayer **rebuilt CodeLayer from scratch in roughly six weeks** (mid-December 2025 → late January 2026) to wrap deterministic control flow around the [[dex-rpi-to-crispy|CRISPY]] planning workflow. Motivation: the open-source RPI prompts produced a "vast spectrum of quality" when teams adopted them — expert users got incredible results, others got inconsistent ones. The fix is to stop asking users to wield monolithic 50-instruction prompts and instead build the workflow into the product itself, splitting the long `/create-plan` prompt into multiple steps that deterministic code guides the user through. Stated principle: *"the parts of the conversation you're involved in should be the highest-leverage parts"* — not "don't forget to sprinkle these magic words at this stage." This is Factor #8 of [[12-factor-agents]] ("don't use prompts for control flow") applied to the product itself.

## Relevance

HumanLayer is a key entity in this research because:

1. **The 12-factor agents framework** is the most systematic treatment of agent architecture principles in the wiki
2. **CodeLayer** represents the emerging category of "AI-native IDEs" — purpose-built for managing agents, not just editing code
3. **ACP** tackles the unsolved infrastructure problem — how do you actually run autonomous agents reliably in production?
4. The **human-in-the-loop** emphasis (it's in the name) positions them in the [[code-legibility-debate]] — they believe humans should stay involved

## Key Claims

- AI coding agents can solve "hard problems in complex codebases" — not just greenfield
- Context engineering is the key to scaling AI-first development across teams
- Human-in-the-loop is a first-class pattern, not an afterthought
- Agents should be small, focused, and explicitly controlled (not autonomous black boxes)
- **"Please read the code"** — reversed from "don't read the code" (Aug 2025) after 6 months of production experience. "We have a profession to uphold."
- **Shoot for 2-3x, not 10x** — quality is the bottleneck, not speed
- **Mind your [[instruction-budget]]** — keep prompts under 40 instructions; use control flow instead of prompts for workflow logic
- **"No more slop"** is the 2026 mandate
- **"Do not send your co-workers a 20,000-line PR that refactors the entire codebase"** — concrete corollary of the legibility reversal, demonstrated via the "Ralph is back" cautionary tale (6-hour Ralph run, 20k LOC, never merged due to ~100 merge conflicts two days later). Production pattern instead: **cron-Ralph** — 3 iterations per night against a stable end-state spec, "wake up to a slightly better codebase"
- **Models cannot plan work the way humans plan work** — they default to horizontal phased plans when an experienced engineer would slice one thing end-to-end first to learn the unknowns. Planning is one of the load-bearing places where humans must remain in the loop
- **HumanLayer targets brownfield at scale** — staff/principal engineers at companies with millions of lines of code and thousands of engineers, explicitly *not* aimed at vibe coding or greenfield work

## Links

- [[12-factor-agents]] — design principles
- [[dex-rpi-to-crispy]] — CRISPY methodology (evolved from RPI)
- [[matt-pocock-dex-horthy-chat]] — conversational supplement: cron-Ralph, "Ralph is back" PR, CodeLayer rebuild news, learning tests, tracer bullets
- [[humanlayer-codelayer]] — IDE/orchestration tool
- [[agent-control-plane]] — infrastructure platform
- [[spec-driven-development]] — related methodology
- [[automation-levels]] — enabling Level 3-4 workflows
- [[code-legibility-debate]] — Dex's reversal is a major data point
- [[instruction-budget]] — key concept from CRISPY development
- [[context-engineering]] — core to HumanLayer's approach
