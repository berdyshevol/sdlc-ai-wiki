---
title: Superpowers (obra/superpowers)
type: entity
pillar: [coding-agents, spec-driven]
created: 2026-04-13
updated: 2026-04-13
sources: [superpowers-5]
tags: [framework, skills, agent-harness, tdd, spec-driven, open-source, claude-code, jesse-vincent]
---

# Superpowers

## Overview

**Superpowers** is an open-source agentic skills framework providing "a complete software development workflow for your coding agents, built on top of a set of composable 'skills.'" It is the concrete, installable companion to Jesse Vincent's [[superpowers-5|Superpowers blog series]] — the repo where the patterns described in the posts ship as executable skills.

**Created by:** Jesse Vincent (obra) with the Prime Radiant team
**Repository:** [github.com/obra/superpowers](https://github.com/obra/superpowers)
**License:** MIT
**Launched:** October 2025

## Seven-Stage Workflow

Superpowers enforces a mandatory development cycle:

1. **Brainstorming** — Socratic dialogue to refine ideas; ends with a saved design document
2. **Git worktrees** — isolated branch workspaces with a verified clean test baseline
3. **Planning** — decompose design into 2–5 minute tasks with exact paths, code, and verification steps
4. **Execution** — subagents handle individual tasks under two-stage review (spec + quality), or batch with human checkpoints
5. **Test-driven development** — enforced RED-GREEN-REFACTOR; code written before tests is removed
6. **Code review** — scored against the plan, severity-categorized, blocks on critical findings
7. **Branch completion** — test-suite verify, then merge / PR / retain / discard; clean up worktrees

## Skills Architecture

Capabilities are organized as composable skills across four categories:

- **Testing & Quality** — TDD with RED-GREEN-REFACTOR, anti-patterns reference
- **Debugging & Verification** — 4-phase root-cause analysis, defense-in-depth, condition-based waiting, verification-before-completion
- **Collaboration & Project Management** — Socratic brainstorming, implementation planning, batch execution with checkpoints, parallel subagent coordination, pre-review checklists, worktree management, merge/PR decisions, fast subagent-driven iteration
- **Meta & Infrastructure** — skill authoring guidelines, system introduction

## Platform Support

Superpowers is designed to run across coding-agent surfaces via plugin/marketplace installs:

- **Claude Code** — official marketplace plugin
- **Cursor** — plugin marketplace
- **Codex** — remote install
- **OpenCode** — remote install
- **GitHub Copilot CLI** — marketplace
- **Gemini CLI** — extension

## Relevance

Superpowers matters to this research because:

1. **Skills as a concrete unit of agent capability.** It operationalizes the "[[agent-harness|harness is the product]]" thesis — the framework itself is mostly skills + workflow, portable across models.
2. **Subagent cascade in production.** The planning → execution → review cascade from [[superpowers-5]] ships as code, not prose. A real-world implementation of [[12-factor-agents]]' "small, focused agents."
3. **TDD-first autonomy.** Mandatory RED-GREEN-REFACTOR is a testable oracle — a concrete answer to the agentic-laziness problem documented in [[long-running-claude]].
4. **Spec before code, by convention.** Brainstorming and planning stages precede execution, aligning with [[spec-driven-development]] without requiring an external spec framework.
5. **Cross-platform framework.** Unlike IDE-bound tools (Kiro, CodeLayer), Superpowers targets the skill-layer across most major agents — a bet that skills travel better than harnesses.

## Key Claims (from sources)

- Planning-first, subagent-driven development outperforms single-session approaches ([[superpowers-5]])
- Adversarial subagent review catches "TBD" placeholder failures before implementation ([[superpowers-5]])
- Cheaper models (e.g. Claude Haiku) can handle implementation when specs are detailed enough ([[superpowers-5]])
- Visual browser mockups beat ASCII/text diagrams for agent-generated design artifacts ([[superpowers-5]])
- Large files signal insufficient decomposition — a design problem, not a style problem ([[superpowers-5]])

## Relationship to Other Entities

- **Complement to [[claude-agent-sdk]]** — the SDK provides the dumb-loop harness; Superpowers provides the skills and workflow on top
- **Sibling to [[bmad-method]]** — both enforce a multi-phase cycle with adversarial review and named workflows. BMAD uses persona agents (Mary, John, Winston...); Superpowers uses skills + subagents. BMAD is heavier on Agile artifacts; Superpowers is heavier on TDD and worktrees
- **Sibling to [[spec-kit]]** — both structure the spec→plan→tasks→implement pipeline. Spec Kit is slash-command based; Superpowers is skills-based with mandatory TDD
- **Contrast with Ralph Loop ([[everything-is-a-ralph-loop]])** — Superpowers is structured, gated, human-in-the-loop; Ralph is monolithic and autonomous. Superpowers is closer to the "Ralph is not the final answer" position in [[matt-pocock-dex-horthy-chat]]

## Links

- Repository: [github.com/obra/superpowers](https://github.com/obra/superpowers)
- Source page: [[superpowers-5]] — blog post on the methodology
- Author: Jesse Vincent — [blog.fsck.com](https://blog.fsck.com/)

## Open Questions

- How does skill portability actually hold up across models — are the workflows truly model-agnostic, or tuned for Claude?
- Does mandatory TDD slow down exploratory work enough to push users toward unstructured alternatives?
- What's the failure mode when a subagent's two-stage review disagrees with the planning agent?
