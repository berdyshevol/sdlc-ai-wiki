---
title: "12 Factor Agents: Principles for Production LLM Applications"
type: source
pillar: coding-agents
created: 2026-04-08
updated: 2026-04-08
sources: []
tags: [agent-architecture, design-patterns, production, modularity, humanlayer]
author: Dex (dexhorthy)
url: https://github.com/humanlayer/12-factor-agents
date: 2025
---

# 12 Factor Agents: Principles for Production LLM Applications

**Author:** Dex (dexhorthy / HumanLayer)
**URL:** [github.com/humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents)
**Stars:** ~19.2k

## Summary

Inspired by the original 12-Factor App methodology for SaaS, this repository proposes 12 foundational principles for building production-grade LLM-powered applications. The core philosophy is pragmatic: rather than adopting heavyweight agent frameworks wholesale, builders should incorporate small, modular concepts into their existing products.

The principles cover the full lifecycle of agent development — from prompt management and context window control to lifecycle APIs, error handling, and human-in-the-loop patterns. The emphasis throughout is on **developer ownership and explicit control** rather than framework magic.

A key insight is the distinction between "tools as structured outputs" (treating tool calls as JSON data you control) versus the framework-default approach where tool execution is opaque. This reflects a broader theme: production agents need deterministic, debuggable behavior, not autonomous black boxes.

## Key Claims (The 12 Factors)

1. **Natural Language to Tool Calls** — Convert user intent into structured function invocations
2. **Own Your Prompts** — Maintain direct control over prompt engineering; don't rely on framework defaults
3. **Own Your Context Window** — Actively manage what information reaches the LLM; context is precious
4. **Tools Are Structured Outputs** — Treat tool calls as JSON/structured data, not magic framework features
5. **Unify Execution and Business State** — Keep agent state and application state synchronized
6. **Launch/Pause/Resume APIs** — Build agents with simple, composable lifecycle controls
7. **Contact Humans with Tools** — Integrate human approval/intervention as tool calls, not afterthoughts
8. **Own Your Control Flow** — Implement explicit decision logic rather than relying on LLM autonomy
9. **Compact Errors into Context** — Fit error information efficiently within token limits
10. **Small, Focused Agents** — Build narrow, specialized agents rather than monolithic ones
11. **Trigger from Anywhere** — Design agents callable from multiple entry points
12. **Stateless Reducer Pattern** — Structure agents to process events deterministically

**Meta-principle:** "The fastest way for builders to get good AI software in the hands of customers is to take small, modular concepts from agent building, and incorporate them into their existing product."

## Connections

- Factor #10 ("Small, Focused Agents") directly validates the subagent approach in [[superpowers-5]]
- Factor #7 ("Contact Humans with Tools") relates to [[human-in-the-loop]] as a first-class pattern
- Factor #8 ("Own Your Control Flow") is in tension with [[five-levels-shapiro|Shapiro Level 5]] (full autonomy) — 12-factor advocates explicit human control
- The emphasis on ownership and explicit control connects to [[code-legibility-debate]] — you should understand and own your agent's behavior
- Factors #2-3 (own prompts + context) are relevant to [[spec-driven-development]] — specs as context management
- [[humanlayer]] and [[dex-humanlayer]] are the org/person behind this work

## Questions Raised

- How do the 12 factors apply to agents that manage other agents (orchestration)?
- Is Factor #8 (own your control flow) compatible with Level 4-5 autonomy, or does it cap you at Level 3?
- How does the "stateless reducer pattern" work in practice for long-running coding tasks?
- Are some factors more important than others? Is there a priority ordering?
