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

## [2026-04-08] ingest | Dex — "From RPI to CRISPY"

Ingested: "Everything We Got Wrong About RPI" — Dex's Coding Agents Conference 2026 talk (transcript + slides). Candid retrospective on RPI methodology failures and evolution to CRISPY (7-stage workflow). Major reversal on code legibility: now says "please read the code." Introduces instruction budget concept (~150-200 instructions max). Key claim: shoot for 2-3x, not 10x.

Pages created/updated:
- `wiki/sources/dex-rpi-to-crispy.md` (new)
- `wiki/concepts/code-legibility-debate.md` (major update — Dex's reversal, new evidence for School 2)
- `wiki/concepts/instruction-budget.md` (new)
- `wiki/concepts/context-engineering.md` (new)
- `wiki/entities/humanlayer.md` (updated — added CRISPY to product stack, updated key claims)

## [2026-04-08] ingest | Coding Agents Conference 2026 (Multi-Speaker)

Ingested: Slide deck from Coding Agents Conference 2026 (March 3, Computer History Museum). 15+ speakers covering trust, evals, memory, benchmarks, security, enterprise governance. Key talks: Scott Breitenother (Kilo Code, 25T tokens trust ladder), Jessica Wang (Braintrust, agentic vs vector search), Faye Zhang (Pinterest, agent memory), Yanis He (Scale AI, SWE Atlas), Erin Ahmed (Cleric, agent learning), Mihail Eric (RePPIT methodology), Ankit Mathur (Databricks, coding gateway), Harrison Chase + Sam Partee (general purpose agents).

Pages created/updated:
- `wiki/sources/coding-agents-conf-2026.md` (new)
- `wiki/concepts/agent-memory.md` (new)
- `wiki/concepts/automation-levels.md` (updated — added Kilo Code trust ladder)
- `wiki/overview.md` (updated — new thesis points 6-8, updated sources table, new open questions)
- `wiki/index.md` (updated — added sources, concepts, to-create items)

## [2026-04-08] create | BMAD Method Entity Page

Created entity page for BMAD (Breakthrough Method for Agile AI-Driven Development) — multi-agent framework simulating a full Agile team with 12+ AI agent roles and 34+ workflows. Key points: partnership model (AI as collaborator, not replacement), adaptive complexity management, "Party Mode" for multi-perspective collaboration. Runs on top of Claude Code/Cursor/Windsurf. Compared with Spec-Kit, Kiro, and Claude Code. Documented hybrid model (BMAD + Spec-kit) for strategic planning + tactical execution.

Pages created/updated:
- `wiki/entities/bmad-method.md` (new)
- `wiki/concepts/spec-driven-development.md` (updated — expanded BMAD entry, removed "to be researched")
- `wiki/index.md` (updated — added entity, removed from "to create" list)
