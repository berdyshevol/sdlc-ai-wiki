---
title: "Superpowers: How I'm using coding agents in October 2025"
type: source
pillar: [coding-agents, spec-driven]
created: 2026-04-13
updated: 2026-04-13
sources: []
tags: [skills, claude-code, plugin, brainstorm-plan-implement, tdd, subagents, cialdini, memory-extraction]
author: Jesse Vincent
url: https://blog.fsck.com/2025/10/09/superpowers/
date: 2025-10-09
---

# Superpowers: How I'm using coding agents in October 2025

**Author:** Jesse Vincent
**Published:** 9 October 2025
**Blog:** Massively Parallel Procrastination ([blog.fsck.com](https://blog.fsck.com/2025/10/09/superpowers/))

## Summary

This is the introductory post for the **Superpowers** plugin system for Claude Code — the installable framework now hosted at [[superpowers|github.com/obra/superpowers]]. Written six months before [[superpowers-5]], this post documents the moment Vincent formalized his ad hoc agent workflows into a distributable artifact.

The central idea is that **skills** (documented instructions, typically `SKILL.md` files) are "the interesting part" of agentic development. Skills give agents discrete, documented capabilities, and the Superpowers system enforces *mandatory* skill usage: when a skill applies, the agent must use it. This turns accumulated tacit knowledge into explicit, reusable infrastructure that travels with the plugin.

The workflow Vincent documents — **brainstorm → plan → implement** — already includes automatic git worktree creation, two execution modes (human PM oversight vs. subagent dispatch with code review), and RED/GREEN TDD. By [[superpowers-5]] six months later, this matures into the full seven-stage cascade, but the skeleton is already present here.

Two notable meta-practices: (1) **pressure-testing skills** — Vincent has Claude quiz subagents with realistic "production is bleeding money" scenarios to verify compliance, and discovered that Robert Cialdini's persuasion principles (authority, scarcity, commitment, social proof) measurably improve skill adherence in LLMs — a finding consistent with Dan Shapiro's Wharton study. (2) **Memory extraction** — Vincent fed Claude 2,249 markdown files of prior conversation lessons and had it cluster them by topic; most issues turned out to already be covered by existing skills.

## Key Claims

- **Skills are the interesting part of agentic development** — the reusable unit of agent capability, more transferable than prompts or scaffolding
- **Mandatory skill invocation** — "if Claude has a skill to accomplish something, it must use that skill" — deterministic control flow wrapped around probabilistic generation
- **Cialdini persuasion principles work on LLMs** — authority, scarcity, commitment, and social proof measurably improve skill compliance (corroborated by Dan Shapiro's Wharton study)
- **Pressure-testing via subagent quizzes** — realistic scenarios (e.g. "production is bleeding money, do you debug or check ~/.claude/skills/?") surface compliance failures before production use
- **Memory extraction from conversation history** — bulk-process prior markdown transcripts into clustered lessons; most turn out to already be covered by existing skills, validating the skill abstraction
- **Book-to-skills conversion** — ask Claude to read technical books and extract reusable patterns (author notes uncertainty about IP implications)
- **Brainstorm → plan → implement cycle with worktrees** — already includes parallel isolation and a choice between human PM oversight or subagent dispatch + code review
- **RED/GREEN TDD as enforced practice** — failing test first, minimal implementation, iterate — the seed of the mandatory RED-GREEN-REFACTOR in later Superpowers

## Installation (historical reference)

Requires Claude Code 2.0.13+:

```
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

## Connections

- **Launches the framework** now documented at [[superpowers|github.com/obra/superpowers]] — this post is effectively the "v1 announcement"
- **Precursor to [[superpowers-5]]** — the March 2026 post that documents the matured cascade; the brainstorm/plan/implement skeleton here expands into seven stages there
- **Validates the [[agent-harness|harness-is-the-product]] thesis** — Vincent's bet is that skills (carried by the harness) are what compound over time, not the model
- **Mandatory skill invocation parallels [[12-factor-agents]]** principle of owning the control flow — skills are deterministic gates around LLM generation
- **Pressure-testing = adversarial review** for skills themselves, a meta-layer above the adversarial spec review in [[superpowers-5]] and [[bmad-method]]
- **Memory extraction** relates to [[agent-memory]] — turning ephemeral conversation artifacts into durable, searchable infrastructure
- **Cialdini finding** cross-references to Dan Shapiro's Wharton study — a concrete bridge between [[five-levels-shapiro]]'s author and the Superpowers methodology
- **Microsoft Amplifier inspiration** — cited as a precedent for self-improving agent patterns, worth tracking as a separate entity later

## Questions Raised

- Does mandatory skill invocation scale as skill counts grow into the hundreds? What's the retrieval/selection overhead?
- Are Cialdini-style persuasion techniques robust, or do they weaken as models are RLHF-tuned against them?
- What's the IP/licensing story for book-to-skills extraction at scale?
- How does memory extraction handle contradictions between older and newer lessons?
- At what point does the "skills enforce discipline" framing become over-constraint that blocks legitimate novel approaches?
