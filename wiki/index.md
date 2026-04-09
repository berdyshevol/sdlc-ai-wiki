---
title: Wiki Index
type: index
created: 2026-04-08
updated: 2026-04-08
---

# Wiki Index

## Overview

- [[overview]] — High-level synthesis of all research. Start here.

## Sources

| Page | Author | Pillar | Summary |
|------|--------|--------|---------|
| [[five-levels-shapiro]] | Dan Shapiro | Industry/Factories | Five-level maturity model from "spicy autocomplete" to autonomous "dark factory." Most devs stuck at Level 2. |
| [[superpowers-5]] | Jesse Vincent | Agents/Spec-Driven | Subagent-driven development, adversarial spec review, cascade pattern (spec → implement → review). |
| [[12-factor-agents]] | Dex (HumanLayer) | Coding Agents | 12 principles for production AI agents: own your prompts, own your control flow, small focused agents. |
| [[humanlayer-codelayer]] | Dex (HumanLayer) | Coding Agents | Open-source IDE for orchestrating AI coding agents. "Superhuman for Claude Code." MultiClaude parallel sessions. |
| [[agent-control-plane]] | Dex (HumanLayer) | Coding Agents | Kubernetes-native orchestration for long-lived autonomous agents. Async-first, MCP support, agent-to-agent delegation. |
| [[dex-rpi-to-crispy]] | Dex (HumanLayer) | Coding Agents / Code Legibility | RPI methodology failures and evolution to CRISPY. Major reversal on code legibility. Instruction budget concept. |
| [[coding-agents-conf-2026]] | Multiple speakers | Industry (all pillars) | Full-day conference: trust ladder (Kilo Code 25T tokens), agentic search vs RAG, agent memory, SWE Atlas, enterprise governance, security. |

### Sources To Ingest

- lukepm.com — "The Software Factory"
- blog.fsck.com — Superpowers series (earlier installments)
- Spec-kit documentation/articles
- ~~BMAD method documentation~~ ✅ entity page created
- Kiro (AWS) documentation
- Devin case studies/reviews
- Industry landscape reports

## Concepts

| Page | Pillar | Summary |
|------|--------|---------|
| [[spec-driven-development]] | Spec-Driven | Specifications as the primary artifact; code generated from specs by AI. The gateway to Level 4+. |
| [[software-factory]] | Software Factories | Fully automated software production — specs in, working software out. Shapiro's "Dark Factory" vision. |
| [[automation-levels]] | Industry | Five-level maturity model for AI in SDLC. Role transformation at each level, not just productivity. |
| [[code-legibility-debate]] | Code Legibility | Should devs read AI-generated code? Two schools: "black box" vs. "must read." Tilting toward "must read" after Dex's reversal. |
| [[instruction-budget]] | Coding Agents | LLMs follow ~150-200 instructions reliably. Monolithic prompts fail; split into <40-instruction focused stages. |
| [[context-engineering]] | Coding Agents | Managing context window contents for quality. "Dumb zone" at 40%. Two reads: more info vs. better instructions. |
| [[agent-memory]] | Coding Agents | Mechanisms for cross-session knowledge retention. Next frontier after commoditized capabilities (Cleric, Pinterest). |

### Concepts To Create

- **Human-in-the-loop** — patterns for human oversight in AI pipelines
- **Agentic development** — building software via autonomous AI agents
- **Technical deflation** — falling cost of software production and its implications
- **Adversarial review** — using AI to validate AI-generated specs/code
- **Agentic search** — LLM-driven code exploration using grep/find/cat vs. vector search (Braintrust data)
- **Enterprise agent governance** — centralized management of multiple coding tools (Databricks gateway)

## Entities

| Page | Type | Summary |
|------|------|---------|
| [[humanlayer]] | Company | Full-stack AI coding agent company: 12-factor principles → CodeLayer IDE → Agent Control Plane infrastructure. |
| [[bmad-method]] | Framework | Multi-agent Agile team simulation (12+ roles, 34+ workflows). Spec-driven, anti-vibe-coding. Runs on Claude Code/Cursor/Windsurf. 19.1k stars. |

### Entities To Create

- **Devin** — Cognition's autonomous coding agent
- **Spec-kit** — Spec-driven development framework
- **Kiro** — AWS spec-driven development tool
- **Dan Shapiro** — Five levels framework author
- **Jesse Vincent** — Superpowers series author
- **Dex (dexhorthy)** — 12-factor agents / HumanLayer creator

## Analyses

_No analysis pages yet. Analyses are created from substantial query answers._
