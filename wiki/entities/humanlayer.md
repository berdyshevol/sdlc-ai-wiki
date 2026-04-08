---
title: HumanLayer
type: entity
pillar: coding-agents
created: 2026-04-08
updated: 2026-04-08
sources: [12-factor-agents, humanlayer-codelayer, agent-control-plane]
tags: [company, tools, orchestration, open-source]
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
| IDE | [[humanlayer-codelayer\|CodeLayer]] | Developer interface for orchestrating agents | ~10.3k |
| Infrastructure | [[agent-control-plane\|ACP]] | Kubernetes-native agent runtime | ~384 |

This is notable because most players in this space offer only one layer. HumanLayer provides the full stack: **how to think about agents** (12-factor) → **how to interact with agents** (CodeLayer) → **how to run agents** (ACP).

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

## Links

- [[12-factor-agents]] — design principles
- [[humanlayer-codelayer]] — IDE/orchestration tool
- [[agent-control-plane]] — infrastructure platform
- [[spec-driven-development]] — related methodology
- [[automation-levels]] — enabling Level 3-4 workflows
