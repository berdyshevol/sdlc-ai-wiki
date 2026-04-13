---
title: "From RPI to QRSPI: Rebuilding the First Structured Workflow for Coding Agents"
type: source
pillar: [coding-agents, code-legibility]
created: 2026-04-13
updated: 2026-04-13
sources: []
tags: [rpi, qrspi, crispy, instruction-budget, context-engineering, sub-agents, dex, humanlayer, commentary, practitioner-validation]
author: Alex Lavaee
url: https://alexlavaee.me/blog/from-rpi-to-qrspi/
date: 2026
---

# From RPI to QRSPI: Rebuilding the First Structured Workflow for Coding Agents

**Author:** Alex Lavaee (builder of Atomic, open-source agent tooling)
**URL:** [alexlavaee.me](https://alexlavaee.me/blog/from-rpi-to-qrspi/)

## Summary

Alex Lavaee's article is **informed commentary and independent practitioner validation** of Dex Horthy's RPI → QRSPI evolution. It overlaps substantially with [[dex-rpi-to-crispy]] but earns its own source page because it (1) systematizes Dex's failure-mode analysis into three named categories with technical framing, (2) reports cross-practitioner validation of the 40% context-utilization threshold, (3) draws an original distinction between sub-agents-as-context-firewalls vs. sub-agents-as-personas, and (4) frames the whole evolution as discipline maturation — "the craft is maturing" rather than "here's the final answer."

The article's thesis: structured agent workflows are an **engineering discipline subject to iteration**, not a finished product. Dex's willingness to publicly retract RPI and ship QRSPI is the case study.

## Key Claims

### Lavaee's three-name taxonomy of RPI failures

Lavaee names the failure modes Dex described, making them more quotable and teachable:

1. **Instruction Budget Overflow** — frontier models lose consistency after 150-200 instructions; RPI's 85+ instructions caused silent skips of critical constraints without surfacing errors
2. **Magic Words Dependency** — the workflow required specific trigger phrases (e.g. "work back and forth with me") to function correctly; indicates systemic brittleness
3. **Plan-Reading Illusion** — well-written plans feel authoritative but lack technical validation; architectural assumptions stay unexamined until implementation reveals the misalignment

### QRSPI's eight stages (Lavaee's framing)

Lavaee splits QRSPI into **five alignment phases + three execution phases**:

- **Alignment:** Questions → Research → Design Discussion → Structure Outline → Plan
- **Execution:** Work Tree → Implement → Pull Request

### Validated practitioner insights

- **40% context utilization threshold** — keep context under 40%; restart sessions at 60% regardless of window size. More context paradoxically *increases* hallucinations. Lavaee reports this threshold holding across multiple practitioners, not just HumanLayer
- **Vertical slices over horizontal layers** — mock API → frontend → database as end-to-end checkpoints beats DB-then-API-then-UI. Maps cleanly to context resets
- **Sub-agents as context firewalls** — the architectural point: sub-agents are *context boundaries* (filesystem artifacts beat shared conversation history), not personas. Cheap models for scoped tasks (codebase search, testing, formatting); expensive models for orchestration

### Embedded practical advice

- Start fresh sessions rather than extending long-running contexts
- Persist alignment artifacts (specs, task lists) to disk between sessions
- Hide the feature ticket during research to prevent premature architectural opinions
- Require engineers to read and own all generated code without exception
- Design workflows with explicit verification checkpoints after each vertical slice

## Original Contributions vs. Dex's Material

**Derived from Dex:** the QRSPI framework structure, the "brain surgery" concept for architectural redirection during design discussion, vertical-slices recommendation, the code-legibility reversal.

**Original to Lavaee:**
- The three *named* failure modes — systematic articulation with technical framing
- 40% threshold *validation* across practitioners (not just HumanLayer)
- Sub-agents as **context firewalls vs. personas** — a sharper architectural distinction than Dex explicitly makes
- Framing as discipline maturation process — positioning the article as meta-commentary on craft evolution

## Connections

- **Commentary on [[dex-rpi-to-crispy]]** — this is Lavaee's synthesis/validation; read after the primary source
- **Cites [[humans-in-the-loop-dex-interview]]** — Lavaee's "The Humans in the Loop interview (March 2026)" reference resolves to this Dex interview
- **[[instruction-budget]]** — Lavaee's "Instruction Budget Overflow" naming may be the stickiest articulation of this concept yet
- **[[context-engineering]]** — cross-practitioner validation of the 40% threshold strengthens the claim beyond HumanLayer's single data point
- **[[agent-harness]]** — Lavaee references "harness engineering as the differentiator layer," explicitly citing [[skill-issue-harness-engineering]] (HumanLayer's canonical post on the topic) and connecting QRSPI to the harness-is-the-product thesis in [[anatomy-agent-harness]]
- **[[code-legibility-debate]]** — echoes Dex's "please read the code" reversal: "require engineers to read and own all generated code without exception"
- **[[agent-memory]]** — "persist alignment artifacts to disk between sessions" aligns with the CHANGELOG.md pattern in [[long-running-claude]]
- **Contrasts with Ralph Loop** ([[everything-is-a-ralph-loop]]) — Lavaee's framing of "discipline maturation" is directly opposed to Ralph's "software development is dead" maximalism

## Questions Raised

- Is the 40% threshold actually model-invariant, or will it move as context windows improve?
- Does the context-firewall framing hold up when sub-agents need to share learned state (e.g. memory extraction patterns from [[superpowers-intro]])?
- What's the failure rate of the alignment phase itself — how often does Design Discussion catch architectural issues vs. miss them?
- Who else (beyond Dex and Lavaee) is shipping variants of this pattern? Is QRSPI converging with [[bmad-method]]'s four-phase cycle or [[superpowers]]'s seven stages?
