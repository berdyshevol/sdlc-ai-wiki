---
title: "Agent Memory"
type: concept
pillar: coding-agents
created: 2026-04-08
updated: 2026-04-08
sources: [coding-agents-conf-2026, dex-rpi-to-crispy, long-running-claude]
tags: [memory, learning, state, persistence, trust]
---

# Agent Memory

## Definition

**Agent memory** refers to mechanisms that allow AI coding agents to retain and apply knowledge across sessions, tasks, and contexts. Without memory, agents are **stateless** — starting fresh every session with no knowledge of past interactions, corrections, or environment-specific context.

Multiple speakers at the [[coding-agents-conf-2026]] identified memory as the **next frontier of differentiation** now that core agent capabilities are becoming commoditized.

## Key Sources

- **[[coding-agents-conf-2026]]** — Two dedicated talks:
  - **Erin Ahmed (Cleric):** "Agent capabilities are commoditized. The next horizon of differentiation is learning." Three lessons: make correction easy, reward corrections with persistence, absorb context continuously.
  - **Faye Zhang (Pinterest):** Production memory architecture — procedural memory (CLAUDE.md), episodic memory (JSON files), hooks for failure→fix entries, MCP memory_search tool. Long-horizon memory treated as a learned policy problem (PPO/GRPO).
- **[[dex-rpi-to-crispy]]** — CRISPY's static artifacts (design docs, structure outlines) function as a form of **session memory** — enabling resume from any point without autocompaction.
- **[[long-running-claude]]** — Anthropic case study of multi-day autonomous scientific computing. Codifies **CHANGELOG.md as "lab notes"** — a lightweight, file-based episodic memory tracking completed tasks, failed approaches with explanations, accuracy checkpoints, and known limitations. Key principle: "document failed experiments to prevent successive sessions from repeating dead ends." Also demonstrates CLAUDE.md as self-modifying procedural memory (the agent edits its own instructions across sessions).

## Memory Taxonomy (Pinterest)

| Type | Storage | Purpose | Example |
|------|---------|---------|---------|
| Procedural | CLAUDE.md | How to do things | Coding conventions, tool usage patterns |
| Episodic | `.claude/memories/episodes/*.json` | What happened | Failure→fix pairs, past decisions |
| Episodic (lightweight) | CHANGELOG.md | What happened (file-based) | Failed approaches, accuracy checkpoints, "lab notes" ([[long-running-claude]]) |
| Long-horizon | MCP cold storage | Accumulated knowledge | Cross-project patterns, team preferences |

## Three Lessons on Agent Learning (Cleric)

1. **Make it easy to teach via correction.** Harvest skills to encode procedures, capture ratings as quality signals, propose memories to persist lessons. "Agents that activate fastest aren't the ones that fail least — they're the ones that make it easy to correct."

2. **Reward corrections with better performance.** Corrections must:
   - **Persist** — apply in the same context
   - **Compound** — generalize to different contexts
   - **Be visible** — show use of knowledge in actions and reasoning

3. **Absorb context continuously.** Map environment and dependencies proactively. Each investigation produces durable knowledge. Absorb tribal knowledge and team preferences over time.

## Memory as Learned Policy (Pinterest)

Pinterest's advanced approach treats memory as a reinforcement learning problem:
- **Memory Manager** — structured operations via PPO (what to store, how to organize)
- **Answer Agent** — preselects and reasons via GRPO (what to retrieve, how to apply)
- **3-tier infrastructure:** Hot memory (current session), domain task memory, cold storage via MCP

## Why Agents Fail Without Memory

Four failure modes identified by Faye Zhang:
1. **Spec drift across multi-step chains** — without memory of the original spec, agents drift
2. **Data distribution imbalance** — agents can't learn from patterns in past tasks
3. **Memory collapse** — context window limitations cause knowledge loss mid-task
4. **Tool misuse** — agents repeat tool errors without learning from past failures

## Open Questions

1. How do you prevent stale or incorrect memories from degrading performance?
2. What's the right granularity for memory? (Per-project? Per-team? Per-organization?)
3. Can memory systems introduce security risks (leaking context between projects/users)?
4. How do you evaluate whether memory is actually improving agent performance?
5. Is RL-based memory management (Pinterest's approach) practical outside large companies?

## Related Concepts

- [[context-engineering]] — memory is a context engineering strategy for cross-session persistence
- [[instruction-budget]] — memory competes for context window space with instructions
- [[automation-levels]] — higher automation levels likely require more sophisticated memory
- [[code-legibility-debate]] — if agents have good memory of past corrections, does that reduce the need for human code review?
