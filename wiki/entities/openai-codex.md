---
title: "OpenAI Codex"
type: entity
pillar: coding-agents
created: 2026-05-07
updated: 2026-05-07
sources: [lopopolo-openai-extreme-harness-engineering, anatomy-agent-harness, agentic-coding-stack-aslan]
tags: [openai, codex, coding-agent, cli, app, harness, model, gpt-5, computer-use, billion-tokens]
---

# OpenAI Codex

## Overview

**Codex** is OpenAI's coding-agent product line — a model family (Codex Mini → Codex models within GPT-5 / 5.x), a CLI (`codex`), a desktop App, and a shared harness that runs across all surfaces. Distinct from [[openai-agents-sdk|OpenAI Agents SDK]] (the framework for *building* custom agents), Codex is a *finished* coding-agent product. As of May 2026 the Codex App had passed **2 million weekly active users** with **25% week-over-week growth**.

- **Creator:** OpenAI
- **Surfaces:** Codex CLI (terminal), Codex App (desktop, parallel-session UI), VS Code extension, Slack ChatGPT app, web Codex on chatgpt.com
- **Underlying models:** Codex-class models within GPT-5, 5.1, 5.2, 5.3 (added background shells), 5.3-Spark (fast/cheap variant), **5.4** (computer use + 1M-token context, May 2026)
- **Distinguishing feature:** "Codex models feel better on Codex surfaces than a generic chat window" — same harness across all surfaces.

## Relevance

Codex is the **OpenAI-side counterpart to Claude Code** in the duopoly of frontier coding-agent products driving 2026 SDLC change. Three properties make it unusually load-bearing on the wiki:

1. **Reference platform for harness engineering.** The discipline was named and popularized by [[lopopolo-openai-extreme-harness-engineering|Ryan Lopopolo's article]] about building a 1M-LOC product on Codex without a single human-authored line of code. Codex's CLI/App/skill model is the substrate that practice runs on.
2. **First-class background shells (5.3+) and computer use (5.4)**, both of which materially change harness design — sub-1-minute build invariants, agent-self-verifies UI changes by recording video.
3. **Skill files as a core primitive.** Codex's skill system (and the convention of a short root `AGENTS.md` plus dedicated skill files for `core-beliefs.md`, quality-score, tech-tracker, etc.) is what [[lopopolo-openai-extreme-harness-engineering|Lopopolo]] credits with making harness engineering tractable at 1M-LOC scale. The team "reinvented Skills from first principles" before Skills shipped.

## Surfaces

| Surface | Role | Notes |
|---------|------|-------|
| **Codex CLI** | Terminal entry point | The original; long-horizon agentic runs, background shells, file/stdin tools |
| **Codex App** | Desktop product | Parallel sessions ("4x it"), task management; 2M WAU as of May 2026 |
| **VS Code extension** | IDE integration | Same harness, in-editor surface |
| **Web Codex** | Browser-hosted agent on chatgpt.com | Cloud sandbox, integrated with ChatGPT |
| **Slack ChatGPT app** | At-mention `@codex` to delegate work | The agent can post on the user's behalf |
| **Linear/GitHub native** | Ticket → PR loop | Used by Lopopolo's team as the autonomous-merge pipeline |

## Architecture (Codex extension over Agents SDK)

Per [[anatomy-agent-harness|Pachaar]] and the Agents SDK docs:

1. **Codex Core** — agent loop + runtime
2. **App Server** — bidirectional JSON-RPC API
3. **Client surfaces** — CLI, VS Code, web app, Slack

All surfaces share the same harness — explicit harness convergence is part of the product strategy.

### Skills
- Short top-level `AGENTS.md` (~100 lines, table of contents) + per-capability skill files. Lopopolo's 1M-LOC codebase has **six skills total**.
- Skills are model-callable; agent decides when to invoke each.
- Skills can be derived from session-log distillation and PR-comment slurping (continual learning at the harness level — see [[lopopolo-openai-extreme-harness-engineering]]).

### Background Shells (5.3+)
- Codex can spawn long-running commands and continue working while they run.
- Side effect: model becomes less patient with blocking commands → **forces sub-1-minute builds** as a discipline.

### Computer Use (5.4)
- Agent can record video of itself clicking around to verify UI changes.
- Combined with 1M-token context, enables full UI-verification loops without external scaffolding.

### Codex Security
- Reviews internalized dependencies in-place; key enabler of [[lopopolo-openai-extreme-harness-engineering|Lopopolo's]] "in-house your dependencies" pattern.

## Key Claims

- **2M weekly active users, 25% WoW growth** as of May 2026 (Lopopolo). The fastest-growing OpenAI surface.
- **5.3 → 5.4 in roughly one month** — release cadence has accelerated to monthly major versions.
- **Background shells (5.3) and computer use (5.4) are the two harness-defining feature additions** of early 2026.
- **"Codex models feel better on Codex surfaces than a generic chat window."** First-party validation of the harness > model thesis.
- **Skill files were reinvented from first principles** by Lopopolo's team before Codex's official skill system existed — the convention emerged independently.
- **`gh` CLI is the canonical "agent-good" tool shape** within the Codex idiom — token-efficient, filterable, structured.
- **Anti-MCP stance from the most extreme practitioner.** Lopopolo: MCPs forcibly inject all tokens into context, mess with autocompaction, and the agent can forget how to use the tool. Pro-CLI everywhere it's tractable.
- **OpenAI doesn't restrict Codex internally.** Lopopolo: "no rate limits internally, I can go full send."

## Connections

- **[[openai-agents-sdk]]** — Codex extends the Agents SDK; same Runner class, three-layer architecture, AGENTS.md cascading prompt stack.
- **[[lopopolo-openai-extreme-harness-engineering]]** — The most detailed practitioner account of Codex at 1M-LOC scale. Defines the operational stack: AGENTS.md + 6 skills + lint-as-prompt + session-log slurping + the `dollar-land` merge skill.
- **[[anatomy-agent-harness]]** — Codex is one of the five frameworks compared (with [[claude-agent-sdk]], [[langgraph]], [[crewai]], [[autogen]]).
- **[[claude-agent-sdk]]** — The Anthropic counterpart. Both ship "thin harness, smart model"; both ship cloud-agents-with-computer-use as first-class. Convergent architecture, different vendors.
- **[[agent-harness]]** — Codex is the OpenAI-side reference implementation.
- **[[skill-issue-harness-engineering]]** — Kyle's six harness levers map cleanly onto Codex's primitives (AGENTS.md, MCP, skills, sub-agents, hooks, back-pressure).
- **[[symphony]]** — Lopopolo's orchestration substrate built atop Codex CLI.
- **[[automation-levels]]** — Codex powers all the wiki's L4/L5 case studies on the OpenAI side.
- **[[openai-frontier]] *(referenced — not yet a separate page)*** — the enterprise platform that packages Codex + safety specs + governance for non-OpenAI customers.

## Links

- Codex docs (developer.openai.com/codex)
- [[lopopolo-openai-extreme-harness-engineering]] — extreme harness engineering case study
- [[openai-agents-sdk]] — the SDK Codex is built on
