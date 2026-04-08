---
title: Wiki Log
type: log
created: 2026-04-08
updated: 2026-04-08
---

# Wiki Log

## [2026-04-08] init | Wiki Created

Initialized the SDLC AI Automation Research Wiki with five research pillars:
1. Spec-Driven Development
2. Software Factories
3. Gen AI Coding Agents
4. Code Legibility Debate
5. Industry Landscape

Created schema (CLAUDE.md) and directory structure.

## [2026-04-08] ingest | Dan Shapiro — "The Five Levels"

Ingested: "The Five Levels: From Spicy Autocomplete to the Software Factory" by Dan Shapiro (Jan 2026).
Five-level maturity model for AI-assisted software development. Key insight: each level is a role transformation, not just productivity. ~90% of devs stuck at Level 2.

Pages created/updated:
- `wiki/sources/five-levels-shapiro.md` (new)
- `wiki/concepts/automation-levels.md` (new)
- `wiki/concepts/software-factory.md` (new — referenced)
- `wiki/concepts/code-legibility-debate.md` (new — referenced)

## [2026-04-08] ingest | Jesse Vincent — "Superpowers 5"

Ingested: "Superpowers 5: AI Coding Agent Evolution" by Jesse Vincent (Mar 2026).
Subagent-driven development, adversarial spec review, cascade pattern. Practical Level 3-4 workflows.

Pages created/updated:
- `wiki/sources/superpowers-5.md` (new)
- `wiki/concepts/spec-driven-development.md` (new — referenced)

## [2026-04-08] ingest | Dex — "12 Factor Agents"

Ingested: "12 Factor Agents" by Dex / HumanLayer (2025).
12 principles for production AI agents. Emphasis on developer ownership, modularity, human-in-the-loop.

Pages created/updated:
- `wiki/sources/12-factor-agents.md` (new)

## [2026-04-08] synthesis | Initial Overview

Created initial overview synthesizing all three sources. Identified emerging thesis:
- Industry at inflection point (Level 2 → Level 3+)
- Spec-driven development as gateway to higher automation
- Multi-agent architectures over monolithic assistants
- Code legibility debate unresolved
- Tension between control and autonomy

Pages created/updated:
- `wiki/overview.md` (new)
- `wiki/index.md` (new)

## [2026-04-08] ingest | HumanLayer / CodeLayer

Ingested: "HumanLayer / CodeLayer" — open-source IDE for orchestrating AI coding agents, built on Claude Code. "Superhuman for Claude Code" with MultiClaude parallel sessions and context engineering at scale.

Pages created/updated:
- `wiki/sources/humanlayer-codelayer.md` (new)
- `wiki/entities/humanlayer.md` (new)
- `wiki/index.md` (updated — added source + entity)

## [2026-04-08] ingest | Agent Control Plane (ACP)

Ingested: "Agent Control Plane" — Kubernetes-native orchestration for long-lived AI agents. Async-first, MCP support, agent-to-agent delegation. Four core objects: LLM, Agent, Tools, Task. Alpha status.

Pages created/updated:
- `wiki/sources/agent-control-plane.md` (new)
- `wiki/entities/humanlayer.md` (updated — added ACP to product stack)
- `wiki/index.md` (updated — added source)
