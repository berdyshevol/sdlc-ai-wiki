---
title: "Agentic Coding Stack: Five Layers"
type: concept
pillar: coding-agents
created: 2026-04-16
updated: 2026-04-16
sources: [agentic-coding-stack-aslan, anatomy-agent-harness, skill-issue-harness-engineering]
tags: [stack, layers, taxonomy, methodology, discipline, semantic-context, token-optimization, product-surface, failure-modes]
---

# Agentic Coding Stack: Five Layers

## Definition

The **agentic coding stack** is a five-layer architectural model for assembling AI-coding tools, formalized by Murat Aslan in [[agentic-coding-stack-aslan|"The Agentic Coding Stack"]] (April 2026). The model rejects "which tool wins?" framing and instead organizes tools by the workflow concern they address. *"Serious agentic coding needs a stack, not a favorite tool."*

Each layer answers a single question and reduces a specific subset of agentic-coding failure modes. The five layers are **orthogonal** — a tool at L4 (Token Optimization) is not in competition with a tool at L1 (Delivery Methodology); they live in different slots of the same workflow.

This concept is workflow-oriented (looking at the developer's whole assembly), and is the wiki's complement to the component-oriented [[agent-harness]] model (looking inside a single agent).

## The Five Layers

| Layer | Question | Tools (per Aslan) | Failure modes reduced |
|-------|----------|-------------------|----------------------|
| **L1 — Delivery Methodology** | *When* should the AI analyze, plan, implement? | [[bmad-method\|BMAD-METHOD]], [[spec-kit]] | Consistency failures, specification gaps |
| **L2 — Agent Discipline** | *How* should the AI behave while building? | [[superpowers]] | Review bottlenecks, consistency failures |
| **L3 — Technical Context** | *What* does the code actually mean? | [[ctxo|Ctxo]] | Review bottlenecks, multi-session conflicts |
| **L4 — Token Optimization** | *How much* tool output should enter context? | [[rtk|RTK]], [[context-mode]] | Context loss |
| **L5 — Product Surface** | *Where* does the developer operate the whole system? | [[gsd-2]] | Multi-session conflicts, review bottlenecks |

## Key Source

- **[[agentic-coding-stack-aslan]]** — Primary source. Murat Aslan, Dev Genius, April 2026. Series 1 of "Agentic Coding Systems."

## Five Failure Modes (per Aslan)

The layers are designed to attack a specific taxonomy of failure modes. The wiki's first explicit failure-mode taxonomy for agentic coding:

1. **Consistency failures** — same kind of prompt produces different implementation quality across sessions
2. **Context loss** — agent sees too much raw output, drops important state, contradicts itself
3. **Specification gaps** — product intent does not survive the trip from idea to code
4. **Review bottlenecks** — code generation accelerates, but confidence and quality control do not
5. **Multi-session conflicts** — parallel agent work creates merge pain, overlapping edits, fragile ownership

> *"Every tool in this post reduces one or more of these failures. None eliminates all five."*

## Decision Rule

Aslan's prescription for selecting tools:

1. **First** ask which layer is missing in your workflow.
2. **Then** choose the lightest tool that solves that missing layer.
3. **Only add** the next layer when the previous one becomes a bottleneck.

> *"Bad tool decisions usually come from mixing up layers. Teams compare a methodology tool with a token tool, or a semantic analysis tool with a product shell, and then wonder why the conclusion feels fuzzy."*

## Recommended Combinations (per Aslan)

| Stack | Combination | When |
|-------|-------------|------|
| **Solo, minimum overhead** | [[superpowers]] + [[ctxo|Ctxo]] + [[rtk|RTK]] | Solo work, code-quality focus, no orchestration platform |
| **Team, larger repos** | [[bmad-method|BMAD]] + [[superpowers]] + [[ctxo|Ctxo]] + [[gsd-2]] | Inconsistent agent behavior already visible in architecture/review/merge quality |
| **Spec-first product dev** | [[spec-kit]] + [[superpowers]] + [[ctxo|Ctxo]] | Team writes specs, wants AI to respect them |
| **Token-constrained** | [[rtk|RTK]] + [[context-mode]] + [[ctxo|Ctxo]] | Agent spends too much time reading logs/diffs/output |

[[ctxo|Ctxo]] is the most ubiquitous tool, appearing in all four stacks — consistent with Aslan's "scarcest capability in the current ecosystem" framing.

## How the Wiki's Existing Entities Slot Into the Layers

Most wiki entities can be placed in this taxonomy. Quick triage (wiki interpretation, not direct from Aslan):

- **L1 (Methodology):** [[bmad-method|BMAD]], [[spec-kit]], [[codespeak]] (spec-driven), [[kiro]]
- **L2 (Discipline):** [[superpowers]], [[bmad-method|BMAD's Quick Dev workflow]] (overlap)
- **L3 (Technical Context):** [[ctxo|Ctxo]] only — confirms Aslan's "scarcest capability" claim
- **L4 (Token Optimization):** [[rtk|RTK]], [[context-mode]], [[claude-agent-sdk|Claude Code's]] grep/glob/head/tail JIT pattern (built-in, not a separate tool)
- **L5 (Product Surface):** [[gsd-2]], [[humanlayer-codelayer|CodeLayer]], [[agent-control-plane]], [[everything-is-a-ralph-loop|the Weaving Loom]] (factory-shaped extreme)

The existing wiki has good L1, L2, L4, L5 coverage. **L3 (semantic codebase analysis as a tool category) was a wiki gap** that Aslan's source closes.

## Relationship to Other Models

### vs. [[agent-harness]] (Pachaar's 12 Components)

[[anatomy-agent-harness|Akshay Pachaar's "Anatomy of an Agent Harness"]] (April 2026) is a sister piece. Both 2026 syntheses emerge independently and converge on a layered/component view of agentic coding. The two models complement each other:

| Dimension | Aslan's Stack (this concept) | Pachaar's Harness ([[agent-harness]]) |
|-----------|------------------------------|----------------------------------------|
| Slicing axis | Workflow concern | Component |
| Granularity | 5 layers | 12 components, 7 architectural decisions |
| Looking at | Developer's tool assembly | Inside a single agent |
| Unit of analysis | Tools (BMAD, Ctxo, RTK...) | Mechanisms (orchestration loop, memory, guardrails...) |

The two models should coexist. The agent-harness concept describes *what's inside an agent*; this stack concept describes *what surrounds an agent in a developer's workflow*.

### vs. [[skill-issue-harness-engineering|Kyle's Six Harness Components]]

Kyle's "Skill Issue: Harness Engineering for Coding Agents" (HumanLayer, March 2026) describes six harness components: CLAUDE.md/AGENTS.md, MCP servers, skills, sub-agents, hooks, back-pressure mechanisms. These map to the **single-agent-configuration** view, sitting one level below Aslan's L2 (Agent Discipline) — Kyle is asking *"how do I configure this one agent?"* while Aslan is asking *"which tools do I assemble around the agent?"*

Both diagnose the "AI worked great for the first hour and then everything got weird" pain as something other than model quality:

- Kyle: *"It's not a model problem. It's a configuration problem."*
- Aslan: *"It is stack design."*

### vs. [[automation-levels|Shapiro's Five Levels]]

Shapiro's framework is a **maturity model** (where on the autonomy spectrum is your team?). Aslan's stack is a **composition model** (which tools fit which workflow concern?). They're orthogonal — a Level-2 team and a Level-4 team can both reach for the same five-layer stack, just deploying different combinations. The team-workflow stack (BMAD + superpowers + Ctxo + gsd-2) targets Level 3-4 deployments.

## The Missing Link: Spec-to-Code Traceability

Aslan's headline claim is that the **bridge between specification and implementation is still weak.** Today's ecosystem is good at the edges — methodology generates intent (L1), discipline improves execution (L2), semantic tools explain code (L3), token tools protect context (L4), product shells coordinate work (L5) — but no broadly adopted system tracks a requirement through design, implementation, tests, and ongoing change.

The four unanswered traceability questions:

1. **Which code symbols implement requirement RQ-12?** Prevents intent from disappearing during execution.
2. **Which tests cover this spec item?** Makes review and regression analysis tractable.
3. **If this requirement changes, what breaks?** Connects product change to technical impact.
4. **Which open PRs or agents are touching the same requirement?** Reduces multi-session and multi-agent conflicts.

> *"If someone builds that bridge well, they will not just have a useful feature. They will own the most strategic connective tissue in the agentic coding stack."*

This becomes a new entry on the [[code-legibility-debate]] (third position: navigate-don't-read) and [[spec-driven-development]] open-question lists. See the source page [[agentic-coding-stack-aslan]] for the full argument.

## Five Lessons (per Aslan)

1. **The worst tool debates are really layer-confusion debates.** Once you separate methodology, discipline, semantic context, token optimization, and product surface, most of the confusion disappears.
2. **Good planning does not compensate for poor code understanding.** L1 doesn't fix L3.
3. **Token optimization is reliability infrastructure, not a luxury feature.** L4 protects everything above it.
4. **The lightest useful stack usually wins first.** Most teams should not begin with the most complete setup.
5. **Spec-to-code traceability is the next serious frontier.** The unclaimed competitive layer.

## Open Questions

1. **Is the 5-layer model load-bearing or descriptive?** Aslan presents it as both diagnostic and prescriptive, but four of four recommended combinations skip at least one layer (typically L5). Is L5 separable from the lower layers, or is it a packaging concern?
2. **Is L5 (Product Surface) a real layer or a packaging artifact?** Only one tool ([[gsd-2]]) is placed there. Several wiki entities (CodeLayer, ACP, the Loom) could plausibly occupy the same slot, suggesting the category is real but emerging.
3. **How do the layers interact under stress?** What's the failure mode when L1 (BMAD) sequences work that L2 (superpowers) won't TDD because the test infrastructure isn't there yet? Layer interactions are not yet analyzed.
4. **Are the five failure modes orthogonal?** Some seem coupled — context loss often causes consistency failures. Worth empirical testing.
5. **Is there a benchmark for stack-as-a-whole?** [[anatomy-agent-harness|TerminalBench 2.0]] benchmarks harnesses, [[skill-issue-harness-engineering|Terminal Bench data]] benchmarks configurations, but Aslan explicitly disclaims his post is not a benchmark. What would a stack benchmark look like?

## Related Concepts

- [[agent-harness]] — component-oriented complement to this workflow-oriented model
- [[context-engineering]] — formalized as L4 in this model
- [[spec-driven-development]] — L1 plus the spec-side half of the missing-link traceability layer
- [[code-legibility-debate]] — Aslan's missing-link framing introduces a third position (navigate-don't-read)
- [[software-factory]] — L5 is the workflow-level expression of the factory thesis
- [[automation-levels]] — orthogonal maturity model (where you are) vs. composition model (what you assemble)
- [[instruction-budget]] — the constraint L4 protects
