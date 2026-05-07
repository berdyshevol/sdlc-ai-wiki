---
title: Software Factory
type: concept
pillar: software-factories
created: 2026-04-08
updated: 2026-05-07
sources: [five-levels-shapiro, superpowers-5, everything-is-a-ralph-loop, zakariasson-cursor-software-factory, software-factory-practitioners-guide-woolley, cole-medin-ai-dark-factory, parsons-ralph-loops-workshop, lopopolo-openai-extreme-harness-engineering]
tags: [automation, autonomous, dark-factory, production-pipeline]
---

# Software Factory

## Definition

A software factory is a **fully or near-fully automated system for producing software** — analogous to a manufacturing factory where raw materials (requirements/specs) go in and finished products (working software) come out, with minimal or no human intervention during the production process.

The term "Dark Factory" (from [[five-levels-shapiro]]) references Fanuc's lights-out robot factories that operate without human workers present. Applied to software, it means AI systems that can take a specification and produce working, tested, deployed software without a human in the loop.

## Key Sources

- [[five-levels-shapiro]] — Level 5 ("Dark Factory") is the software factory vision
- [[superpowers-5]] — The cascade pattern (spec → implement → review) is a proto-factory pipeline
- [[everything-is-a-ralph-loop]] — Geoffrey Huntley's "level 9" vision: autonomous loops that evolve products and optimize for revenue. The most extreme articulation of the software factory concept. Introduces The Weaving Loom as infrastructure for evolutionary software.
- [[software-factory-practitioners-guide-woolley]] — most comprehensive practitioner-level reference; introduces [[shift-work]], [[holdout-scenarios]], [[attractor]], [[digital-twin-universe]], satisfaction metric.
- [[zakariasson-cursor-software-factory]] — Cursor's production data point (May 2026). Three-part build decomposition (**primitives & patterns / guardrails / enablers**) and a checklist (**runnable, accessible, verifiable**); thousands of cloud agents/day with computer-use verification; **agentic code owner** and **continual-learning** as concrete factory automations.
- [[lopopolo-openai-extreme-harness-engineering]] — OpenAI Frontier's production data point (May 2026). Three-engineer team, 1M LOC, ~1,500 PRs, 5 months, **0% human-authored code** with **post-merge review only**. Introduces [[symphony]] (six-layer Elixir orchestration substrate as a "ghost library"), the on-policy-harness principle, and harness-engineering-as-text-injection-discipline. The most extreme School-1 production datapoint in the wiki.
- [[cole-medin-ai-dark-factory]] — independent factory framing for individual developers.
- [[parsons-ralph-loops-workshop]] — Ralph-Loop pattern as the dumb-but-effective factory substrate.
- The Software Factory (lukepm.com) — dedicated article on this concept (to be fully ingested)

## Current Understanding

The software factory vision sits at the **far end of the automation spectrum**. Based on current sources:

**What it requires:**
- Robust [[spec-driven-development]] — specs must be precise enough for autonomous execution
- Multi-agent orchestration — different agents handling different pipeline stages
- Comprehensive automated testing — the primary quality gate when no human reviews code
- Self-healing capabilities — agents that can diagnose and fix their own failures

**Where we are today:**
- Shapiro claims Level 5 has been achieved only by very small teams (<5 people)
- Most teams operate at Level 2 — collaborative coding, far from factory automation
- The [[superpowers-5]] cascade pattern represents a middle ground — structured but still human-supervised
- Products like [[devin]] aim for autonomous coding but reviews suggest they still need significant oversight
- Geoffrey Huntley ([[everything-is-a-ralph-loop]]) claims to have achieved "evolutionary software auto-heal" — self-repairing systems under autonomous Ralph loops — and extends the automation levels to 8-9, with level 9 being fully autonomous revenue-optimizing software factories
- [[strongdm]] (Feb 2026, [[software-factory-practitioners-guide-woolley|Woolley's guide]]) — three-person team, no humans write or review code, uses [[shift-work]] / [[holdout-scenarios]] / [[attractor]] / [[digital-twin-universe]]
- **[[cursor]] (May 2026, [[zakariasson-cursor-software-factory|Zakariasson]])** — *internal* factory running thousands of cloud agents/day; sub-parts at L5, company self-positions as "between L3 and L4 with sub-parts at L5." First IDE-vendor data point. Concrete factory automations: **agentic code owner** (auto-approves low-risk PRs), **continual-learning plugin** (extracts rules from chat history), Linear-ticket → cloud-agent pipelines, **Cursor Workers** for self-hosted agent infrastructure.
- **OpenAI Frontier (May 2026, [[lopopolo-openai-extreme-harness-engineering|Lopopolo]])** — three-engineer team, 5 months, ~1M LOC, ~1,500 PRs, **zero human-authored code**, **post-merge review only**. Self-positioned as "between L4 and L5." Operating substrate: short `AGENTS.md` + six skills + lint-as-prompt + the `dollar-land` merge skill + Symphony's six-layer orchestration. Caveat: greenfield Electron app (not continuous-deployment infrastructure); release branches still cut by humans.

## The Three-Part Build Decomposition (Zakariasson)

Adding to the cascade and pipeline models, [[zakariasson-cursor-software-factory|Zakariasson]] proposes a practical decomposition for what an *agent* needs to operate inside a factory:

| Part | What it covers | Examples |
|------|----------------|----------|
| **Primitives & patterns** | Codebase structure agents can navigate | Modular folders, co-located code, discoverable layouts; existing usage patterns (auth methods, startup scripts, test patterns) the agent can copy |
| **Guardrails** | What bounds the agent | [[skill-issue-harness-engineering\|hooks]] that block sensitive paths (auth/encryption); rules that emerge from observed failures (not pre-emptive scaffolding); tests as self-verification |
| **Enablers** | What empowers the agent | Skills, MCPs, environment access (start dev server, run tests, computer-use for UI), allowed external tools |

Summary checklist: **runnable, accessible, verifiable.** Verifiable is the under-invested one — backend invariants are easy; UI verification is genuinely hard and motivates computer-use tooling.

This frame aligns with [[skill-issue-harness-engineering|Kyle's six harness levers]] but reorganized around what the agent *needs* / what *bounds* it / what *empowers* it.

**The pipeline model:**
```
Spec → Plan → Implement → Test → Review → Deploy
  ↑                                         |
  └─────── feedback loop ──────────────────┘
```

Each stage could be handled by specialized agents ([[12-factor-agents]] Factor #10: Small, Focused Agents).

## Orchestration Substrate Patterns (the tier *above* the harness)

As factories scale, the orchestration tier (the system spawning, supervising, and rework-ing many agent runs in parallel) becomes a distinct concern from the per-agent harness. Three named substrates are now in the wiki:

| Substrate | Source | Runtime | Key primitive |
|-----------|--------|---------|---------------|
| **[[attractor]]** | [[strongdm]] / [[software-factory-practitioners-guide-woolley|Woolley]] | Directed graph (DOT) | LLM-evaluable phase transitions |
| **[[agent-control-plane]]** | [[humanlayer]] | Kubernetes-native | Long-lived agents, async-first, MCP |
| **[[symphony]]** | OpenAI Frontier ([[lopopolo-openai-extreme-harness-engineering|Lopopolo]]) | Elixir / BEAM | Per-task gen-server daemon, rework state, ghost-library distribution |

All three solve the same problem (running many agents in parallel against a single codebase or product) at different points in the runtime/distribution-model design space. Convergent insight: **rework should be cheap** — Symphony's rework-state explicitly trashes the entire worktree+PR rather than incrementally fixing it; StrongDM's holdout scenarios prevent agents from incrementally hacking their way to a passing test.

## Open Questions

- Is the factory metaphor actually appropriate? Software is not manufacturing — requirements are ambiguous, domains are complex, edge cases are infinite
- Can software factories handle maintenance and evolution, or only greenfield?
- What's the minimum viable factory? What subset of the pipeline must be automated first?
- How do software factories handle security, compliance, and other non-functional requirements?
- Is there a "valley of death" between Level 3 and Level 5 where the investment doesn't pay off?

## Related Concepts

- [[spec-driven-development]] — the input mechanism for software factories
- [[automation-levels]] — the progression toward factory automation
- [[human-in-the-loop]] — the tension between full automation and human oversight
- [[code-legibility-debate]] — factories produce code humans may never read
- [[agentic-development]] — the agent patterns that enable factory pipelines
