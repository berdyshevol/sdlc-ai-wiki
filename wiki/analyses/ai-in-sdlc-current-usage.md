---
title: How AI Is Currently Being Used in SDLC
type: analysis
pillar: industry
created: 2026-04-25
updated: 2026-04-25
sources: [five-levels-shapiro, coding-agents-conf-2026, ai-in-sdlc-research, dex-rpi-to-crispy, long-running-claude, everything-is-a-ralph-loop, software-factory-practitioners-guide-woolley, sdd-course-deeplearning-ai, agentic-coding-stack-aslan, bmad-method-docs, anatomy-agent-harness]
tags: [industry-landscape, adoption, sdlc-stages, automation-levels, current-state]
---

# How AI Is Currently Being Used in SDLC

## Question

How is AI currently being used across the software development lifecycle today (April 2026) — what's actually deployed, what's emerging, and what's still hype? Sister question to [[five-levels-two-schools]], which focuses on the philosophical divergence at Levels 4+.

## Framing: A Maturity Spectrum, Not a Single Mode

AI usage in the SDLC spans a range mapped by [[automation-levels|Shapiro's five levels]] and validated empirically by Kilo Code's 25T-token trust ladder ([[coding-agents-conf-2026]]). The model is **sequential** — *"if autocomplete fails, agents never get a chance"* — meaning teams climb a trust ladder before they can adopt higher-leverage AI patterns.

| Shapiro Level | Kilo Code Rung | Where Most Teams Are |
|---|---|---|
| L1 Assisted | Autocomplete | Mainstream — Copilot/Cursor everywhere |
| L2 Collaborative | Chat | **~90% stop here** ("Level 2 trap") |
| L3 Managed | Single Agents | Growing — production adopters |
| L4 Autonomous | Orchestration | Emerging case studies |
| L5 Dark Factory | — | Only [[strongdm]] publicly demonstrated |

## Where Teams Are Today

### Level 1–2 (dominant mode, ~90% of developers)

- **Inline autocomplete** ([[github-copilot]], Cursor tab, Claude Code) — the most-trusted rung; 200ms latency, clean signal.
- **Chat-driven generation** — copy/paste/iterate; the "pair programmer" feeling that masks higher levels exist.
- **Most widely adopted AI dev tooling** ([[ai-in-sdlc-research]]).

### Level 3 (production-grade adoption)

- Human becomes **code reviewer/manager**; AI is the primary coder.
- Dex's "2-3x quality-constrained speedup beats 10x slop" thesis ([[dex-rpi-to-crispy]]) argues this is the production sweet spot.
- Structured methodologies (CRISPY, RePPIT, [[superpowers]]) make this reliable.

### Level 4 (emerging case studies)

- **Anthropic's long-running Claude Code** ([[long-running-claude]]) — multi-day autonomous sessions compress months of scientific research into days. Five codified patterns: CLAUDE.md as living plan, CHANGELOG.md as lab notes, test oracles, git as coordination, Ralph Loop.
- **Practitioner SDD on small SaaS teams** — 5-person team using [[spec-kit]] + [[bmad-method]] reported reduced hallucination-driven rework ([[ai-in-sdlc-research]]).
- **Cron-Ralph / pipeline-Ralph** ([[matt-pocock-dex-horthy-chat]]) — overnight 3-iteration loops.

### Level 5 (rare, scoped)

- **[[strongdm]]** — first public Dark Factory in production: 3-person team, no human writes or reviews code ([[software-factory-practitioners-guide-woolley]]).
- **No large enterprise has implemented at scale yet.**

## How AI Is Used Across SDLC Stages

| Stage | Current AI Usage | Maturity |
|---|---|---|
| **Requirements / spec authoring** | NLSpec, BMAD planning tracks, spec-kit `specify`, Kiro prompts→specs | Emerging (L3-4) |
| **Design / architecture** | BMAD Architect persona, multi-agent planning, adversarial spec review | Emerging |
| **Code generation** | Autocomplete, chat, full-feature implementation by agents | **Mature (L1-3)** |
| **Code review** | AI-assisted PR review, adversarial review of AI-generated code | Growing |
| **Testing** | TDD enforcement in agents (Superpowers RED-GREEN-REFACTOR), test oracles, [[holdout-scenarios]] | Mature for unit tests |
| **Codebase understanding** | Agentic search (grep/find/cat) outperforms vector RAG (Braintrust); semantic tools like [[ctxo]] | Growing |
| **Refactoring / modernization** | Brownfield SDD conversions ([[codespeak]] takeover: faker 9.9×, folio ~7×) | Emerging |
| **Deployment / ops** | Less covered in the wiki — [[strongdm]] satisfaction metric is the closest signal | Nascent |
| **Governance / orchestration** | Enterprise gateways (Databricks), [[agent-control-plane]], [[humanlayer-codelayer]] | Emerging |

## The Vibe-Coding ↔ SDD Bifurcation

[[ai-in-sdlc-research]] frames two distinct modes coexisting:

- **Vibe coding** — informal, iterative, fast; minimal artifacts.
- **Spec-driven development** — structured, traceable, governed; specs as the primary artifact ([[codespeak]], [[bmad-method]], [[spec-kit]], [[kiro]]).

Organizations are converging on **dual-track workflows** rather than a single process. CodeSpeak's modular takeover ([[codespeak-modular-takeover]]) reframes them as **sequential phases** — vibe-code first, then `codespeak takeover` extracts modular specs (Folio: ~3000 Go LOC → 430 MD lines × 4 specs = ~7× shrink).

## Methodological Convergence

Multiple independent practitioners have converged on the same pattern:

- **CRISPY/QRSPI** (Dex) — research → plan → implement
- **RePPIT** (Mihail Eric) — same shape, independent derivation
- **BMAD** four-phase cycle with three planning tracks
- **Spec-kit** `specify → plan → tasks → implement`
- **DeepLearning.AI × JetBrains course** ([[sdd-course-deeplearning-ai]]) — three-file Constitution + per-feature loop on dated branches; first mainstream educational articulation

The convergence: **research before planning, plan before implementing, review at high-leverage points, test throughout.** Open question: are these independently discovered truths or echo-chamber effects?

## What's Working vs. Hype

**Working:**
- L1-2 productivity tooling (broad adoption, measurable)
- Structured SDD on small teams (practitioner evidence in [[ai-in-sdlc-research]])
- Harness/methodology improvements ([[anatomy-agent-harness]] — LangChain jumped from outside top 30 to rank 5 on TerminalBench 2.0 by changing only harness)
- Long-running scoped autonomous tasks ([[long-running-claude]])

**Unproven at scale:**
- Full Dark Factory / Level 5 for large enterprise
- "Software development is dead" maximalism (Huntley, [[everything-is-a-ralph-loop]]) — Anthropic's own work cautions scoped use; Dex's "2-3x not 10x" pushes back

**Acknowledged bottlenecks:**
- **Trust, not capability** — Kilo Code data shows trust ladder is sequential
- **Spec-to-code traceability** — [[agentic-coding-stack-aslan]] names this as the unbuilt missing link: *"the most strategic connective tissue in the agentic coding stack"*
- **Code legibility** — unresolved ([[code-legibility-debate]]); tilting toward "must read" after Dex's reversal

## Sources Used

- [[five-levels-shapiro]], [[automation-levels]], [[coding-agents-conf-2026]] — the maturity framework + empirical trust ladder
- [[ai-in-sdlc-research]] — academic survey across SDLC stages, vibe ↔ SDD bifurcation, practitioner observation
- [[dex-rpi-to-crispy]] — the "2-3x not 10x" production thesis
- [[long-running-claude]] — Level 4 autonomous case study
- [[software-factory-practitioners-guide-woolley]] — only public Level 5 implementation
- [[everything-is-a-ralph-loop]] — Level-9 maximalist counterposition
- [[sdd-course-deeplearning-ai]], [[bmad-method-docs]], [[codespeak-modular-takeover]] — SDD in practice
- [[agentic-coding-stack-aslan]] — five-layer stack and missing-link thesis
- [[anatomy-agent-harness]] — harness as the differentiator

## Conclusions

1. **AI in SDLC is real and uneven.** L1-2 is mainstream; L3 is production-grade for early adopters; L4 has emerging case studies; L5 has one public reference implementation.
2. **Trust climbs sequentially** — teams can't skip rungs. Reliable autocomplete unlocks agent adoption, not the other way around.
3. **The dominant frontier is methodology and harness, not raw capability.** Same model + better harness = top-5 benchmark jumps.
4. **Two operating modes will coexist** — vibe coding for speed/learning, SDD for traceability/compliance. CodeSpeak's takeover suggests they may chain rather than compete.
5. **The unbuilt thing is spec-to-code traceability.** Whoever builds it owns the connective tissue between L1 (methodology) and L3 (semantic context).

## Related Analyses

- [[five-levels-two-schools]] — companion analysis on the *philosophical* divergence at L4+ (not the current-usage map this page provides)
