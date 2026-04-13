---
title: "Skill Issue: Harness Engineering for Coding Agents"
type: source
pillar: coding-agents
created: 2026-04-13
updated: 2026-04-13
sources: []
tags: [harness-engineering, context-engineering, claude-md, mcp, skills, sub-agents, hooks, back-pressure, humanlayer, dex, kyle]
author: Kyle (@0xblacklight) — HumanLayer
url: https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents
date: 2026-03-12
---

# Skill Issue: Harness Engineering for Coding Agents

**Author:** Kyle (@0xblacklight) — published on HumanLayer's blog
**Published:** March 12, 2026
**URL:** [humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents](https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents)

> **Authorship note:** Despite being published on HumanLayer's blog (Dex Horthy's company) and building on Dex's context-engineering vocabulary, the byline is **Kyle** — not Dex. Treat this as a HumanLayer company post extending Dex's framework with tactical, empirically-grounded implementation detail rather than as a Dex primary source. Dex is quoted/cited, not the author.

## Summary

A tactical, empirically-grounded companion to [[dex-rpi-to-crispy]]. Where Dex's conference talk stays at the methodology level (RPI failures, QRSPI stages, instruction budget), this post drops into the **configuration layer** — what knobs to actually turn on CLAUDE.md, MCP servers, skills, sub-agents, hooks, and verification loops — based on "dozens of projects and hundreds of agent sessions" at HumanLayer.

The central thesis: **"it's not a model problem. It's a configuration problem."** Rather than waiting for GPT-6, teams should optimize their agent's **harness** — the runtime environment and peripherals determining how models interact with their environment. The term **harness engineering** (coined by Viv Trivedy) is positioned as a subset of context engineering (coined by Dex in [[12-factor-agents]]), which is itself a superset of prompt engineering.

Mitchell Hashimoto's quoted formulation becomes the operational definition: *"anytime you find an agent makes a mistake, you take the time to engineer a solution such that the agent never makes that mistake again."* The article's distinctive contribution is **reactive configuration** — add harness elements only when you observe real failures, never preemptively.

## Key Claims

### The Six Primary Harness Components

1. **CLAUDE.md / AGENTS.md files** — markdown deterministically injected into system prompts. Authors keep theirs under 60 lines. ETH Zurich study (arxiv 2602.11988, 138 agentfiles tested) found **LLM-generated CLAUDE.md files *hurt* performance and added ~20% cost**; human-written ones helped ~4%. Less is more.
2. **MCP servers (tools)** — inject tool descriptions into system prompts; too many tools push agents into the Dumb Zone via context saturation. Also a security vector for prompt injection. **Prefer CLI tools over MCP servers** when the CLI is familiar from training data (GitHub, Docker, databases).
3. **Skills (progressive disclosure)** — bundle related markdown; activation loads `SKILL.md` as a user message only when contextually relevant. Alternative to MCP servers for bundling knowledge without system-prompt bloat. Security warning: skill registries can distribute malicious code.
4. **Sub-agents (context control)** — function as a **context firewall**: the parent sees only the sub-agent's prompt and final result, not the intermediate noise. Use cases: codebase research, pattern analysis, information tracing. Cost pattern: Opus for parent, Sonnet/Haiku for sub-agents.
5. **Hooks (control flow)** — user-defined scripts at lifecycle points. Claude Code and OpenCode support them; Codex doesn't. Authors' example: a hook that runs `biome` formatter + TypeScript typecheck — **silent on success, verbose only on failure.**
6. **Back-pressure mechanisms (verification)** — context-efficient typechecks, builds, tests. Critical principle: *"success is silent, only failures produce verbose output."* Early mistake: running the full test suite (5+ minutes) flooded context; now they run subsets.

### The Linear CLI Case Study

HumanLayer replaced the **Linear MCP server with a lightweight CLI wrapper + 6 examples in CLAUDE.md**. Outcome: thousands of tokens saved per session, zero loss in capability. This is the article's clearest operational example of "prefer CLI over MCP when training familiarity is high."

### Reactive Configuration Philosophy

**What didn't work:**
- Preemptive harness design before real failures were observed
- Installing dozens of skills/MCP servers "just in case"
- Running full test suites post-session
- Micro-optimizing sub-agent tool access (caused "tool thrash")

**What worked:**
- Add harness elements only after failures occur
- Distribute battle-tested configs via repository-level settings
- Optimize iteration speed over first-attempt success
- Iteratively test and discard ineffective hooks

### Post-Training Overfitting

**Terminal Bench 2.0 data:** Opus 4.6 ranks **#33 in Claude Code's harness** but **#5 in different harnesses unseen during post-training**. Evidence that models are measurably overfit to the harness they trained against. Same point for GPT-5 Codex and Codex's `apply_patch` tool coupling. This validates the thesis that harness customization has meaningful headroom beyond model improvements.

## Original vs. Existing Content

**New in this post (not in [[dex-rpi-to-crispy]] or [[anatomy-agent-harness]]):**
- Empirical numbers from "hundreds of agent sessions" at HumanLayer
- Linear MCP → CLI wrapper case study (thousands of tokens saved)
- Specific `biome` + `tsc` hook implementation pattern
- **"Success is silent, only failures produce verbose output"** — a quotable principle for verification design
- ETH Zurich 138-agentfile study: LLM-generated CLAUDE.md *hurts* performance (+20% cost, -quality)
- Terminal Bench 2.0 Opus 4.6 harness-overfitting numbers (#33 → #5)
- **Reactive-configuration philosophy** as an explicit rule: add harness elements only after observed failures
- Sub-agent compaction pattern with `filepath:line` citations
- MCP tool search experimental-feature context

**Extends (not duplicates) existing wiki content:**
- [[dex-rpi-to-crispy]]'s methodology gets tactical implementation guidance
- [[anatomy-agent-harness]]'s 12-component taxonomy gets empirical validation and configuration advice
- [[context-engineering]]'s "Dumb Zone" framing gets the specific "tool bloat pushes into Dumb Zone" mechanism

## Connections

- **Companion to [[dex-rpi-to-crispy]]** — methodology layer (Dex, conference talk) paired with configuration layer (Kyle, this post). Read together.
- **[[anatomy-agent-harness]]** — this post operationalizes the anatomy. Akshay formalizes the components; Kyle shows how to actually tune them.
- **[[humanlayer]]** — canonical HumanLayer publication on day-to-day tooling craft; sits alongside [[12-factor-agents]] (principles), [[dex-rpi-to-crispy]] (methodology), [[humanlayer-codelayer]] (IDE), [[agent-control-plane]] (infrastructure).
- **[[context-engineering]]** — explicitly positions harness engineering ⊂ context engineering ⊂ prompt engineering.
- **[[instruction-budget]]** — "too many tools push into the Dumb Zone" is an instruction-budget argument made at the tool layer.
- **[[agent-memory]]** — skills with progressive disclosure are a memory-shaped solution to knowledge bundling.
- **Cited by [[alexlavaee-rpi-to-qrspi]]** — Lavaee references HumanLayer's "Skill Issue: Harness Engineering" as the canonical articulation of "harness engineering as the differentiator layer."
- **Matt Pocock's AGENTS.md best-practices follow-up** is referenced — candidate future source.

## Questions Raised

- Does reactive configuration scale to teams with frequent-but-heterogeneous failures, or does it require a shared vocabulary of failure modes first?
- How portable are CLAUDE.md patterns across models — does a HumanLayer config that works for Opus 4.6 transfer to GPT-5 Codex?
- What's the counterpart to "success is silent" for positive-signal hooks (e.g. coverage gained, not just errors avoided)?
- At what point does a growing skill library itself become the next Dumb Zone problem?
- Is Viv Trivedy's "harness engineering" coinage going to stick, or will it collapse back into "context engineering"?
