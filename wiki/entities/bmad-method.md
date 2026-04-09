---
title: BMAD Method
type: entity
pillar: spec-driven
created: 2026-04-08
updated: 2026-04-08
sources: [SDD comparison table, research-04-AI-in-SDLC.docx]
tags: [framework, methodology, multi-agent, agile, spec-driven, open-source]
---

# BMAD Method

## Overview

**BMAD** (Breakthrough Method for Agile AI-Driven Development) is an open-source multi-agent framework that simulates a full Agile development team using AI. Created by **bmadcode**, it provides 12+ specialized agent personas (Business Analyst, Architect, PM, Scrum Master, Developer, QA, etc.) and 34+ structured workflows covering the entire SDLC — from brainstorming to deployment.

**GitHub:** [github.com/bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) (~19.1k stars)
**Runtime:** Runs on top of Claude Code, Cursor, Windsurf (not a standalone IDE)

## Philosophy

BMAD's core principle distinguishes it from typical AI tools: rather than having AI "do the thinking for you" (which produces average results), BMAD positions AI as **expert collaborators who guide you through a structured process** to bring out your best thinking in partnership with the AI.

This is a **partnership model**, not delegation. The human remains the decision-maker; the AI provides structure, domain expertise, and systematic coverage.

## Architecture

### Agent Roles

BMAD provides 12+ specialized agent personas representing different Agile team roles:

| Agent | Role |
|-------|------|
| Business Analyst | Requirements gathering, PRD creation |
| Architect | System design, technical decisions |
| Product Manager | Vision, prioritization |
| Scrum Master | Sprint planning, story breakdown |
| Developer | Implementation |
| QA Agent | Testing, review against acceptance criteria |
| UX Designer | User experience |
| + others | Additional specialized roles |

### Key Features

- **Adaptive Complexity Management** — automatically adjusts planning depth based on project complexity (from bug fix to enterprise system)
- **Party Mode** — multiple agent personas collaborate within a single session, simulating cross-functional team discussions
- **Structured Workflows** — 34+ workflows grounded in Agile best practices across analysis, planning, architecture, and implementation
- **`bmad-help` skill** — interactive guidance system available throughout development
- **Expansion Packs** — customizable agent configurations and templates

### Artifact Pipeline

BMAD generates a cascade of structured artifacts:

```
Vision/Brainstorm → PRD → Architecture Doc → User Stories → Implementation → QA Review
```

Output volume is significant: PRD + Architecture + Stories can reach thousands of lines of structured documentation.

## Comparison with Other SDD Tools

From the [[spec-driven-development]] comparison:

| Dimension | BMAD | Spec-Kit | Kiro | Claude Code |
|-----------|------|----------|------|-------------|
| Philosophy | Full AI agile team | Spec → Code | IDE with SDD | Unopinionated platform |
| Scale | Enterprise | Mid-size | Feature-level | Any |
| Workflow | Rigid (Analyst→PM→Arch→SM→Dev→QA) | Rigid (specify→plan→tasks→implement) | Rigid | Fully flexible |
| Setup time | Hours/days | Minutes | Install IDE | Minutes |
| Brownfield | Possible but heavy | Not optimized | Average | Excellent |
| Small fixes | Overkill | Overkill | Overkill | Ideal |

**Key distinction:** BMAD is an **opinionated framework** — it prescribes how you should work. Claude Code is an **unopinionated platform** — you assemble your own workflow. Since BMAD runs *on top of* Claude Code, they are **complementary, not competing**.

## Hybrid Model (BMAD + Spec-kit)

A notable approach from industry analysis combines BMAD's strategic planning with Spec-kit's tactical execution:

1. **Phase 1 — Strategic Planning (BMAD):** Business Analyst and Architect agents define vision, create PRD, establish system design. Scrum Master breaks PRD into user stories.
2. **Phase 2 — Feature Implementation (Spec-kit):** Developer takes a user story, runs Spec-kit's `/specify → /plan → /tasks → /implement` pipeline to generate code.
3. **Phase 3 — QA & Integration (BMAD):** QA Agent reviews implementation against original user stories and acceptance criteria.

## Relevance

BMAD is significant to this research because:

1. **Most comprehensive SDD framework** — covers the full lifecycle, not just spec-to-code
2. **Multi-agent pioneer** — one of the earliest and most popular frameworks to simulate an entire Agile team with AI agents
3. **Validates the spec-driven thesis** — demonstrates that structured specifications lead to better AI output than ad-hoc prompting
4. **Anti-vibe-coding** — explicitly positions itself against unstructured "vibe coding", advocating for process and rigor
5. **Runtime-agnostic** — runs on multiple AI coding platforms, proving that methodology can be separated from tooling

## Key Claims

- AI produces average results when it "does the thinking for you" — structured collaboration yields better outcomes
- Full Agile team simulation with AI is viable and productive for complex projects
- Adaptive complexity management prevents over-engineering small tasks and under-engineering large ones
- Multi-perspective collaboration ("Party Mode") catches issues that single-agent approaches miss
- The framework is complementary to, not competing with, AI coding platforms like Claude Code

## Strengths and Limitations

**Strengths:**
- Fills the gap between "just ask ChatGPT" and a full human SDLC team
- Correct emphasis on AI augmenting, not replacing, human thinking
- Full lifecycle coverage from ideation to QA
- Large community (19.1k GitHub stars)

**Limitations:**
- High setup time (hours/days vs. minutes for simpler tools)
- Overkill for small projects, bug fixes, brownfield changes
- Rigid workflow pipeline (Analyst→PM→Arch→SM→Dev→QA) may not suit all team structures
- Heavy output volume (thousands of lines) can overwhelm context windows
- Prompt-dependent — model updates may require workflow adaptation

## Open Questions

- How does BMAD perform in brownfield/legacy codebases compared to greenfield?
- What is the actual productivity multiplier vs. unstructured AI coding?
- How does it handle the [[instruction-budget]] problem — do 12+ agents with complex prompts exceed effective context limits?
- Can the rigid pipeline be relaxed for teams that don't follow Scrum?
- How does it compare to emerging approaches like [[dex-rpi-to-crispy|CRISPY]] which favor smaller, focused stages?

## Links

- [[spec-driven-development]] — the methodology BMAD embodies
- [[automation-levels]] — enables Level 3-4 in Shapiro's framework
- [[code-legibility-debate]] — BMAD's spec-as-source-of-truth stance is relevant
- [[human-in-the-loop]] — partnership model, not full autonomy
- [[software-factory]] — BMAD as a step toward automated software production
