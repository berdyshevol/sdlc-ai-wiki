---
title: "Long-running Claude for Scientific Computing"
type: source
pillar: coding-agents
created: 2026-04-09
updated: 2026-04-09
sources: [long-running-claude]
tags: [long-running-agents, scientific-computing, claude-code, anthropic, orchestration, ralph-loop, test-oracle, agent-memory]
---

# Long-running Claude for Scientific Computing

## Metadata

- **Author:** Siddharth Mishra-Sharma (Researcher, Discovery team, Anthropic)
- **Published:** March 23, 2026
- **URL:** https://www.anthropic.com/research/long-running-Claude
- **Pillar:** [[agent-harness|Coding Agents]] / [[software-factory|Software Factories]]

## Summary

This Anthropic research post describes a practical methodology for running **multi-day autonomous Claude Code sessions** on scientific computing tasks — specifically reimplementing a cosmological Boltzmann solver (predicting Cosmic Microwave Background properties) as a differentiable version. The author, a physicist on Anthropic's Discovery team, demonstrates that agent-driven development can compress **months or years of research work into days** when tasks are well-scoped with clear success criteria.

The post codifies five key patterns for long-running agent work: (1) **CLAUDE.md as living project plan** — the agent reads and updates its own instructions across sessions; (2) **CHANGELOG.md as portable memory** — "lab notes" tracking status, completed tasks, failed approaches, and accuracy checkpoints to prevent repeating dead ends; (3) **test oracles** — reference implementations providing quantifiable success criteria; (4) **git as coordination** — commits after meaningful work units for recoverable history and hands-off monitoring; (5) **the Ralph Loop** — a re-prompting pattern that combats "agentic laziness" by iterating until the agent declares genuine completion.

The article also provides a concrete **SLURM + tmux execution recipe** for running Claude Code on HPC compute nodes with 48-hour allocations, enabling detach-and-check-periodically workflows. The Boltzmann solver achieved sub-percent (0.1%) agreement with the reference CLASS implementation over several days of autonomous work.

## Key Claims

- **Multi-day autonomous agent sessions are viable** for well-scoped scientific computing tasks with clear success criteria and reference implementations for validation.
- **CLAUDE.md serves dual purpose:** both as initial project plan and as a living document the agent edits to update instructions for future sessions — a form of self-modifying memory.
- **CHANGELOG.md as "lab notes"** prevents successive sessions from repeating failed approaches — the most practical cross-session memory pattern described to date.
- **"Agentic laziness" is a real failure mode:** models stop before completing complex multi-part tasks. The Ralph Loop (iterative re-prompting up to N times) combats this.
- **Git commits as coordination primitive:** agents commit after meaningful work units, enabling both recoverable history and hands-off progress monitoring.
- **Test oracles are essential for autonomous scientific work:** without quantifiable objectives (reference implementations, test suites), there's no mechanism for the agent to assess its own progress.
- **Time compression is dramatic:** "months or years of research work into days" — though with caveats (not production-grade, some inefficiencies like initially testing at single parameter points).
- **The opportunity cost framing:** "As models improve, not running agents feels increasingly costly. Unused agent-working hours represent abandoned progress opportunities."
- **Anthropic's C compiler project** used ~2,000 sessions to build a Linux-kernel-capable compiler — demonstrating industrial-scale long-running agent work.

## Connections

- **[[claude-agent-sdk]]** — The Ralph Loop pattern is a core feature of the Claude Agent SDK. This article provides the most detailed real-world case study of its use in scientific computing. The CLAUDE.md + CHANGELOG.md + git pattern maps directly to the SDK's memory and state management architecture.
- **[[agent-memory]]** — CHANGELOG.md as "lab notes" is a practical, lightweight implementation of episodic memory (cf. Pinterest's JSON-based episodic memory in [[coding-agents-conf-2026]]). The "document failed experiments to prevent repeating dead ends" principle aligns with Cleric's "reward corrections with persistence" lesson.
- **[[agent-harness]]** — The execution recipe (SLURM + tmux + Ralph Loop) is a concrete example of harness infrastructure for long-running tasks. The gather-act-verify cycle from the Claude Agent SDK is implicit in the test oracle pattern.
- **[[context-engineering]]** — CLAUDE.md as living instructions + CHANGELOG.md as portable memory are context engineering strategies that solve the cross-session continuity problem.
- **[[automation-levels]]** — This is a Level 4 (autonomous) workflow: the human sets up the task, provides success criteria, and checks in periodically. The agent works independently for hours/days.
- **[[software-factory]]** — While focused on scientific computing, the pattern (spec → autonomous execution → verification against oracle) is a miniature software factory for a specialized domain.

## Questions Raised

1. **How does this scale beyond well-scoped tasks?** The Boltzmann solver had a clear reference implementation. What about novel research where no oracle exists?
2. **What are the failure modes of multi-day sessions?** The article mentions "some inefficiencies" but doesn't detail catastrophic failures or recovery patterns.
3. **Is the Ralph Loop sufficient for all agentic laziness?** Or are there deeper architectural solutions (e.g., planning agents that decompose work upfront)?
4. **How does the 48-hour SLURM allocation interact with context window limits?** Does the agent need multiple context windows within one SLURM job?
5. **Can this pattern generalize beyond scientific computing** to other domains with clear success criteria (e.g., compiler construction, database optimization, protocol implementation)?
