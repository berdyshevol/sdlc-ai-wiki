---
title: Wiki Log
type: log
created: 2026-04-08
updated: 2026-04-25
last_change: Polished MSIS research report (formal-academic, single applied example) filed under analyses/research-report/
---

# Wiki Log

## [2026-04-25] report | MSIS Research Report — polished formal-academic version

Filed [[research-report/ai-in-sdlc-research-report]] as a polished formal-academic MSIS research report (~3,900 words / ~7 pages). Synthesizes the five wiki analyses ([[ai-in-sdlc-current-usage]], [[ai-techniques-tools-approaches]], [[where-ai-beats-traditional-sdlc]], [[risks-and-limitations]], [[ai-sdlc-3-5-year-outlook]]) into a single integrated narrative with strict adherence to the assignment template: abstract, introduction (field overview and why AI matters now), the maturity spectrum and four-property predicate, six-block techniques section (frontier LLMs with tool use, agentic loops, multi-agent orchestration, SDD, persistent memory and context engineering, the harness), one applied example (Amazon Kiro — 18-month / 30-developer rearchitecture in 76 days with 6 people, ~10× headcount-equivalent reduction; StrongDM cited only briefly to bracket the L5 ceiling), seven categories of risks/ethics (slop and hallucination, security uplift with 35 CVEs/month and accelerating, code legibility and accountability, the Level-2 trap and trust brittleness, governance/compliance gaps, reward-hacking, and economic/workforce/copyright ethics), six predictions for 2027–2031, and six MSIS-practice takeaways. Restates the four-property predicate (verifiable / repetitive-or-parallelizable / language-native / loosely human-coupled) as a portfolio-screening tool. Defensible 2026 posture: 2–3× quality-constrained productivity at L2–L3 with mandatory review, scoped credentials, holdout-style evaluation, and explicit spec-change governance — not Level 5 autonomy. Updated wiki/index.md analyses table.

## [2026-04-25] report | MSIS Research Report — `analyses/research-report/` variant

Filed [[research-report/ai-in-the-sdlc-msis-report]] in the `wiki/analyses/research-report/` folder per assignment request. Reorganized the existing [[msis-research-report-ai-in-sdlc]] content around the assignment template — abstract, introduction and relevance, the maturity spectrum and four-property predicate, current applications and techniques (frontier LLMs with tool use, agentic loops, multi-agent orchestration, SDD, persistent memory, the harness), one applied example (Amazon Kiro: 18-month / 30-developer rearchitecture completed in 76 days with 6 people, ~10× headcount-equivalent reduction; StrongDM referenced as bracketing L5 ceiling), seven categories of risks/ethics (slop and hallucination, security uplift with 35 CVEs/month and accelerating, code legibility and accountability, the Level-2 trap and trust brittleness, governance/compliance gaps, reward-hacking, and economic/workforce/copyright ethics), six 2027–2031 predictions, and six MSIS-practice takeaways. Tightened to ~3,900 words (~7 pages). Defensible 2026 posture restated: 2–3× quality-constrained productivity at L2–L3 with mandatory review, scoped credentials, holdout-style evaluation, and explicit spec-change governance — not Level 5 autonomy. Updated wiki/index.md analyses table.

## [2026-04-25] report | MSIS Research Report on AI in the SDLC

Filed [[msis-research-report-ai-in-sdlc]], a 6–8 page research report aimed at an MSIS audience. Synthesizes the five wiki analyses ([[ai-in-sdlc-current-usage]], [[ai-techniques-tools-approaches]], [[where-ai-beats-traditional-sdlc]], [[risks-and-limitations]], [[ai-sdlc-3-5-year-outlook]]) into an integrated narrative across eight sections: introduction and relevance, the maturity spectrum, the eight problems where AI beats traditional SDLC, current AI applications and techniques (LLMs + tool use, agentic loops, multi-agent orchestration, SDD, persistent memory, harness, dual-track workflows), an applied example (StrongDM Level-5 dark factory paired with Amazon Kiro's L3–L4 SDD result — 18-month/30-dev rearchitecture done in 76 days with 6), seven risk categories (slop, security, legibility, trust ladder, governance, reward-hacking, workforce/copyright), seven future predictions for 2027–2031, and seven IS-practice takeaways. Frames the four-property predicate (verifiable / repetitive-or-parallelizable / language-native / loosely human-coupled) as a portfolio-screening tool. Defensible 2026 posture: 2–3× quality-constrained productivity gains at L2–L3 with mandatory review, scoped credentials, holdout-style evaluation, and explicit spec-change governance — not Level 5 autonomy at scale. Updated wiki/index.md analyses table.

## [2026-04-25] analysis | Where AI Beats Traditional Methods in the SDLC

Filed [[where-ai-beats-traditional-sdlc]] as a problem-centric analysis identifying eight specific SDLC problems where AI demonstrably outperforms traditional methods: time compression on verifiable tasks, routine code generation, test generation/continuous validation, brownfield reverse-engineering into specs, coordinated multi-file refactors, documentation sync, adversarial spec review, parallel exploration. Includes evidence-strength matrix (wiki + April 2026 industry data — DreamzTech, Akraya, MetaCTO, DORA, Anthropic Trends Report) and a "muddier picture" section on contested wins (legibility, architectural judgment, full autonomy, spec rigor). Names the shared predicate across all wins: verifiable / repetitive-or-parallelizable / language-native / loosely human-coupled. Positioned as problem-centric counterpart to [[ai-techniques-tools-approaches]] (mechanism view) and [[ai-in-sdlc-current-usage]] (maturity view). Updated wiki/index.md analyses table.

## [2026-04-25] analysis | How AI Might Change the SDLC Over the Next 3–5 Years (2027–2031)

Filed [[ai-sdlc-3-5-year-outlook]] as a forward-looking analysis. Synthesizes 15 wiki sources with April 2026 industry signals (Gartner 60% AI-generated code by EOY 2026, 40% enterprise-app agent embed, $7.8B → $52B agentic-AI market by 2030, Factory AI $1.5B Series C, junior-hiring -20–35% offset by IBM tripling junior hires, 48% of Q1 2026 tech layoffs AI-attributed). Headline thesis: the 3–5 year story is *organizational, not technical* — trust climbing the ladder, methodology hardening into infrastructure, workforce restructuring around oversight. Seven predictions: (1) L3 as median by 2028–29; (2) vibe→SDD chains via [[codespeak-modular-takeover|takeover]]-style pipelines; (3) **spec-to-code traceability becomes a product category** (highest-leverage prediction); (4) L5 dark factories scale only in oracle-rich domains; (5) workforce inverts via IBM-amplification model with new roles (spec author, evals engineer, harness engineer, governance lead, loop programmer); (6) [[code-legibility-debate]] resolves on Aslan's third position; (7) agent memory becomes the new moat. Six major uncertainties (maximalism vs. caution, SDD enterprise scaling, [[instruction-budget]] persistence, trust-ladder cadence, regulatory shock, memory commoditization timing). Resolution table for 11 wiki open questions. External corroboration via Anthropic 2026 Agentic Coding Trends Report, CIO, The New Stack, Stack Overflow, IEEE Spectrum, CNN, Tom's Hardware. Updated wiki/index.md analyses table.

## [2026-04-25] analysis | Limitations, Risks, and Ethical Concerns of AI in the SDLC

Filed [[risks-and-limitations]] as an analysis synthesizing 14 wiki sources with April 2026 industry evidence. Seven buckets: quality/slop (Dex reversal, ~30% codebase QA, 20% phantom packages, 91.5% vibe-coded apps with hallucination flaws), security (Sherlock 92% / Veracode 45% / CSA 62% / Opsera 15–18% more vulns / 2.7× density / 35 CVEs in March 2026 via Georgia Tech Vibe Security Radar / slopsquatting / Lovable 48-day exposure), code legibility & accountability, trust ladder & 40% context ceiling, governance/compliance gaps, reward-hacking, and workforce/copyright ethics (Anthropic $1.5B settlement; EU/UK training-data provenance). Defensible 2026 posture: 2–3× quality-constrained speedup with mandatory review, scoped credentials, holdout-style evaluation, explicit governance — not Level 5 autonomy. Updated wiki/index.md analyses table.

## [2026-04-25] analysis | AI Techniques, Tools, and Approaches in the SDLC

Filed [[ai-techniques-tools-approaches]] as a sister analysis to [[ai-in-sdlc-current-usage]]. Organized by **technique → tool → approach** with explicit "why appropriate" rationale, rather than by maturity level. Covers eight core techniques (frontier LLMs, tool use, agentic loops, multi-agent, agentic search, external memory, test-time compute, spec→code synthesis), tool stack mapped to [[agentic-coding-stack-layers|Aslan's five layers]] and SDLC stages, and eight architectural approaches (SDD, software factory, harness engineering, CRISPY/RePPIT, Ralph Loop, trust-ladder, spec-to-code traceability, dual-track). External corroboration via web search (VentureBeat Amazon/Kiro 76-day result, DeepLearning.AI×JetBrains course, Augment Code's living-spec vs. static-spec categorization). Reduces "why appropriate" to four SDLC properties: language-native artifacts, cheap iterative feedback, bounded quality oracles, structured context. Updated wiki/index.md analyses table.

## [2026-04-25] analysis | How AI Is Currently Being Used in SDLC

Filed [[ai-in-sdlc-current-usage]] as an analysis page synthesizing across 11 sources. Maps the maturity spectrum (L1 mainstream / L2 trap / L3 production-grade / L4 emerging / L5 only StrongDM), stage-by-stage usage table, vibe↔SDD bifurcation (CodeSpeak takeover as sequential chaining), methodological convergence (CRISPY/RePPIT/BMAD/spec-kit), and working-vs-hype assessment. Positioned as sister to [[five-levels-two-schools]] (current-usage map vs. philosophical divergence). Updated wiki/index.md analyses table.

## [2026-04-08] init | Wiki Created

Initialized the SDLC AI Automation Research Wiki with five research pillars:
1. Spec-Driven Development
2. Software Factories
3. Gen AI Coding Agents
4. Code Legibility Debate
5. Industry Landscape

Created schema (CLAUDE.md) and directory structure.

## [2026-04-08] ingest | Dan Shapiro — "The Five Levels"

Ingested: "The Five Levels: From Spicy Autocomplete to the Software Factory" by Dan Shapiro (Jan 2026).
Five-level maturity model for AI-assisted software development. Key insight: each level is a role transformation, not just productivity. ~90% of devs stuck at Level 2.

Pages created/updated:
- `wiki/sources/five-levels-shapiro.md` (new)
- `wiki/concepts/automation-levels.md` (new)
- `wiki/concepts/software-factory.md` (new — referenced)
- `wiki/concepts/code-legibility-debate.md` (new — referenced)

## [2026-04-08] ingest | Jesse Vincent — "Superpowers 5"

Ingested: "Superpowers 5: AI Coding Agent Evolution" by Jesse Vincent (Mar 2026).
Subagent-driven development, adversarial spec review, cascade pattern. Practical Level 3-4 workflows.

Pages created/updated:
- `wiki/sources/superpowers-5.md` (new)
- `wiki/concepts/spec-driven-development.md` (new — referenced)

## [2026-04-08] ingest | Dex — "12 Factor Agents"

Ingested: "12 Factor Agents" by Dex / HumanLayer (2025).
12 principles for production AI agents. Emphasis on developer ownership, modularity, human-in-the-loop.

Pages created/updated:
- `wiki/sources/12-factor-agents.md` (new)

## [2026-04-08] synthesis | Initial Overview

Created initial overview synthesizing all three sources. Identified emerging thesis:
- Industry at inflection point (Level 2 → Level 3+)
- Spec-driven development as gateway to higher automation
- Multi-agent architectures over monolithic assistants
- Code legibility debate unresolved
- Tension between control and autonomy

Pages created/updated:
- `wiki/overview.md` (new)
- `wiki/index.md` (new)

## [2026-04-08] ingest | HumanLayer / CodeLayer

Ingested: "HumanLayer / CodeLayer" — open-source IDE for orchestrating AI coding agents, built on Claude Code. "Superhuman for Claude Code" with MultiClaude parallel sessions and context engineering at scale.

Pages created/updated:
- `wiki/sources/humanlayer-codelayer.md` (new)
- `wiki/entities/humanlayer.md` (new)
- `wiki/index.md` (updated — added source + entity)

## [2026-04-08] ingest | Agent Control Plane (ACP)

Ingested: "Agent Control Plane" — Kubernetes-native orchestration for long-lived AI agents. Async-first, MCP support, agent-to-agent delegation. Four core objects: LLM, Agent, Tools, Task. Alpha status.

Pages created/updated:
- `wiki/sources/agent-control-plane.md` (new)
- `wiki/entities/humanlayer.md` (updated — added ACP to product stack)
- `wiki/index.md` (updated — added source)

## [2026-04-08] ingest | Dex — "From RPI to CRISPY"

Ingested: "Everything We Got Wrong About RPI" — Dex's Coding Agents Conference 2026 talk (transcript + slides). Candid retrospective on RPI methodology failures and evolution to CRISPY (7-stage workflow). Major reversal on code legibility: now says "please read the code." Introduces instruction budget concept (~150-200 instructions max). Key claim: shoot for 2-3x, not 10x.

Pages created/updated:
- `wiki/sources/dex-rpi-to-crispy.md` (new)
- `wiki/concepts/code-legibility-debate.md` (major update — Dex's reversal, new evidence for School 2)
- `wiki/concepts/instruction-budget.md` (new)
- `wiki/concepts/context-engineering.md` (new)
- `wiki/entities/humanlayer.md` (updated — added CRISPY to product stack, updated key claims)

## [2026-04-08] ingest | Coding Agents Conference 2026 (Multi-Speaker)

Ingested: Slide deck from Coding Agents Conference 2026 (March 3, Computer History Museum). 15+ speakers covering trust, evals, memory, benchmarks, security, enterprise governance. Key talks: Scott Breitenother (Kilo Code, 25T tokens trust ladder), Jessica Wang (Braintrust, agentic vs vector search), Faye Zhang (Pinterest, agent memory), Yanis He (Scale AI, SWE Atlas), Erin Ahmed (Cleric, agent learning), Mihail Eric (RePPIT methodology), Ankit Mathur (Databricks, coding gateway), Harrison Chase + Sam Partee (general purpose agents).

Pages created/updated:
- `wiki/sources/coding-agents-conf-2026.md` (new)
- `wiki/concepts/agent-memory.md` (new)
- `wiki/concepts/automation-levels.md` (updated — added Kilo Code trust ladder)
- `wiki/overview.md` (updated — new thesis points 6-8, updated sources table, new open questions)
- `wiki/index.md` (updated — added sources, concepts, to-create items)

## [2026-04-08] update | Dex — "From RPI to CRISPY" (additional transcript)

Added second transcript of the same talk from Limbic Systems channel (raw/youtube-transcripts/dex-rpi-to-crispy.md). No new claims — same talk, different recording. Updated source page metadata with additional raw file and video URL.

Pages updated:
- `wiki/sources/dex-rpi-to-crispy.md` (updated — added second raw source + video URL)

## [2026-04-08] update | Dex — "From RPI to QRSPI" (slide text extraction)

Added slide text extraction (`raw/slides/From RPI to QRSPI - text.md`) — same talk, different format. Key additions: **QRSPI** as alternate acronym for CRISPY, **"Smart Zone"** terminology (upper 40% of context window, complement to "Dumb Zone"), **"Mental Alignment"** concept (artifacts as shared ground between human and agent), per-model accuracy-vs-instructions charts (Gemini 2.5 Pro, GPT-4, Claude 3.7 Sonnet).

Pages updated:
- `wiki/sources/dex-rpi-to-crispy.md` (updated — added raw file, QRSPI naming, Smart Zone, Mental Alignment)
- `wiki/concepts/context-engineering.md` (updated — Smart Zone terminology, Mental Alignment via artifacts)
- `wiki/concepts/instruction-budget.md` (updated — per-model chart detail)
- `wiki/concepts/code-legibility-debate.md` (updated — QRSPI naming, Mental Alignment)
- `wiki/index.md` (updated — summaries refreshed)

## [2026-04-08] create | CodeSpeak Entity Page

Created entity page for CodeSpeak — a spec-driven development platform (alpha v0.0.1) that generates full applications from markdown specs (`.cs.md` files) using Anthropic's Claude. GitHub-native with automatic commits. Notable for brownfield conversions of major OSS projects (faker, markitdown, yt-dlp, beautifulsoup4, django-oscar). Compared with BMAD, Spec-kit, Kiro. Source: web research (codespeak.dev, github.com/codespeak-dev).

Pages created/updated:
- `wiki/entities/codespeak.md` (new)
- `wiki/concepts/spec-driven-development.md` (updated — added CodeSpeak to Tools and Frameworks)
- `wiki/index.md` (updated — added entity)

## [2026-04-08] create | BMAD Method Entity Page

Created entity page for BMAD (Breakthrough Method for Agile AI-Driven Development) — multi-agent framework simulating a full Agile team with 12+ AI agent roles and 34+ workflows. Key points: partnership model (AI as collaborator, not replacement), adaptive complexity management, "Party Mode" for multi-perspective collaboration. Runs on top of Claude Code/Cursor/Windsurf. Compared with Spec-Kit, Kiro, and Claude Code. Documented hybrid model (BMAD + Spec-kit) for strategic planning + tactical execution.

Pages created/updated:
- `wiki/entities/bmad-method.md` (new)
- `wiki/concepts/spec-driven-development.md` (updated — expanded BMAD entry, removed "to be researched")
- `wiki/index.md` (updated — added entity, removed from "to create" list)

## [2026-04-08] ingest | AI in SDLC Research Paper

Ingested: "AI in SDLC: Artificial Intelligence in the Software Development Life Cycle" — comprehensive academic survey covering AI across all SDLC stages. Key contributions: (1) GitHub Copilot case study, (2) spec-driven development vs. vibe coding bifurcation framework, (3) practitioner observation of SDD (Spec Kit + BMAD) in a 5-person production SaaS team showing reduced hallucination-driven rework, improved task scoping, and increased code consistency. Also covers AI techniques (LLMs, RAG, agents), tool landscape, risks/ethics, and 3-5 year outlook. Proposes dual-track workflows: vibe coding for exploration, SDD for production.

Pages created/updated:
- `wiki/sources/ai-in-sdlc-research.md` (new)
- `wiki/entities/github-copilot.md` (new)
- `wiki/entities/kiro.md` (new)
- `wiki/entities/spec-kit.md` (new)
- `wiki/concepts/spec-driven-development.md` (major update — vibe coding contrast, practitioner evidence, updated Spec Kit and Kiro entries, new open questions)
- `wiki/index.md` (updated — added source, 3 entities, marked Spec-kit/Kiro/Copilot as created)
- `wiki/overview.md` (updated — new thesis points, updated sources table)

## [2026-04-09] ingest | Akshay Pachaar — "The Anatomy of an Agent Harness"

Ingested: "The Anatomy of an Agent Harness" by Akshay Pachaar (April 2026). Comprehensive synthesis of agent harness architecture across Anthropic, OpenAI, LangChain, CrewAI, and AutoGen. Formalizes the agent harness concept with the Von Neumann analogy (LLM = CPU, harness = OS). Identifies 12 components of a production harness, 7 architectural decisions, and compares 5 frameworks on a thin-to-thick spectrum. Key evidence: LangChain jumped from outside top 30 to rank 5 on TerminalBench 2.0 by changing only harness infrastructure (same model). Scaffolding metaphor: harness complexity should decrease as models improve, but co-evolution creates tight coupling.

Pages created/updated:
- `raw/anatomy-agent-harness.md` (new — raw article)
- `wiki/sources/anatomy-agent-harness.md` (new)
- `wiki/concepts/agent-harness.md` (new — 12 components, 7 decisions, Von Neumann analogy, thin vs. thick spectrum)
- `wiki/concepts/context-engineering.md` (updated — context rot, 5 production strategies, three levels of engineering)
- `wiki/entities/claude-agent-sdk.md` (new — Anthropic's thin harness, dumb loop, Fork/Teammate/Worktree, Ralph Loop)
- `wiki/entities/openai-agents-sdk.md` (new — code-first, Runner class, 3 guardrail levels, Codex architecture)
- `wiki/entities/langgraph.md` (new — graph-based control, typed dicts + checkpoints, TerminalBench evidence)
- `wiki/entities/crewai.md` (new — role-based Agent-Task-Crew model, Flows layer)
- `wiki/entities/autogen.md` (new — conversation-driven, 5 orchestration patterns, Microsoft Agent Framework evolution)
- `wiki/index.md` (updated — added source, concept, 5 entities)
- `wiki/overview.md` (updated — new thesis point on harness engineering)

## [2026-04-09] ingest | Anthropic — "Long-running Claude for Scientific Computing"

Ingested: "Long-running Claude for scientific computing" by Siddharth Mishra-Sharma (Anthropic Discovery team, March 2026). Practical methodology for multi-day autonomous Claude Code sessions on scientific computing tasks. Codifies five patterns: CLAUDE.md as living plan, CHANGELOG.md as "lab notes" (portable episodic memory), test oracles, git as coordination, and the Ralph Loop for combating agentic laziness. Case study: cosmological Boltzmann solver achieving 0.1% agreement with reference CLASS implementation over several days. Key claim: "months or years of research work compressed into days." Also references Anthropic's C compiler project (~2,000 sessions).

Pages created/updated:
- `raw/long-running-claude.md` (new — raw article)
- `wiki/sources/long-running-claude.md` (new)
- `wiki/entities/claude-agent-sdk.md` (updated — added scientific computing case study section)
- `wiki/concepts/agent-memory.md` (updated — added CHANGELOG.md pattern to Key Sources and taxonomy)
- `wiki/index.md` (updated — added source)
- `wiki/overview.md` (updated — new thesis point on long-running agents)

## [2026-04-09] ingest | Geoffrey Huntley — "Everything is a Ralph Loop"

Ingested: "Everything is a Ralph Loop" by Geoffrey Huntley (17 Jan 2026, ghuntley.com/loop/). Manifesto-style article on the Ralph Loop as both orchestrator pattern and development mindset. Key claims: software development is fundamentally changed from "brick by brick" to loop-based orchestration; Ralph is monolithic, one task per loop, one repo; the engineer's role shifts to "programming the loop." Extends automation levels beyond Shapiro's Level 5 to Level 8-9: evolutionary software that self-heals and optimizes for revenue. Introduces The Weaving Loom (github.com/ghuntley/loom) as infrastructure for evolutionary software factories. Provocative: "software development is dead — I killed it." Claims coding agent = ~300 lines of loop code.

Pages created/updated:
- `raw/everything-is-a-ralph-loop.md` (new — raw article)
- `raw/links/links.md` (updated — added link)
- `wiki/sources/everything-is-a-ralph-loop.md` (new)
- `wiki/concepts/software-factory.md` (updated — added Huntley's level 9 vision, evolutionary auto-heal)
- `wiki/entities/claude-agent-sdk.md` (updated — added Huntley as Ralph Loop originator)
- `wiki/concepts/agent-harness.md` (updated — added Ralph as orchestrator pattern philosophy)
- `wiki/index.md` (updated — added source)
- `wiki/overview.md` (updated — new thesis point on Ralph Loop maximalism)

## [2026-04-09] ingest | BMAD Method — Official Documentation

Ingested: Official BMAD Method documentation (docs.bmad-method.org/llms-full.txt). Comprehensive first-party source revealing internal architecture, agent system, and workflow mechanics. Key new information beyond previous secondary sources:

1. **Four-phase development cycle** (Analysis → Planning → Solutioning → Implementation)
2. **Three planning tracks** (Quick Flow / BMad Method / Enterprise) — directly addresses the "overkill for small projects" criticism
3. **6 named agent personas** with dedicated skill IDs: Analyst (Mary), PM (John), Architect (Winston), Developer (Amelia), UX Designer (Sally), Technical Writer (Paige)
4. **project-context.md** as shared context file — coordination-through-artifacts pattern, similar to Dex's Mental Alignment
5. **Adversarial review** — "no 'looks good' allowed," most explicit articulation of adversarial review in the wiki
6. **Fresh chat requirement** — each workflow runs in a new session, a practical solution to the instruction-budget problem
7. **Advanced elicitation** — second-pass analysis using pre-mortem, inversion, first-principles reasoning
8. **Quick Dev workflow** — autonomous small-task pipeline paralleling CRISPY's approach

Pages created/updated:
- `raw/bmad-method-docs.md` (new — raw documentation)
- `wiki/sources/bmad-method-docs.md` (new)
- `wiki/entities/bmad-method.md` (major update — replaced secondary-source content with first-party details)
- `wiki/index.md` (updated — added source, updated entity summary, marked BMAD docs as ingested)
- `wiki/log.md` (updated)

## [2026-04-11] ingest | Matt Pocock × Dex Horthy — Live Chat (Jan 17, 2026)

Ingested: "LIVE: Chat with AI Coding Wizard Dex Horthy" — ~46-minute live YouTube conversation between Matt Pocock and Dex Horthy ([[humanlayer]]), recorded 2026-01-17. Conversational supplement to [[dex-rpi-to-crispy]] with significant new material.

Transcript was downloaded via `yt-dlp` (auto-generated YouTube captions, cleaned and split on `>>` speaker markers; speaker labels not reliably attributable).

Key new material beyond Dex's RPI talk:

1. **Quadratic attention** — explicit, non-ML-engineer-friendly explanation of why long context degrades quality (compute scales quadratically per layer per head; doubling tokens = ~4× work)
2. **The "cup" metaphor for task sizing** — "the cup is smaller than you think it is"; iteration must fit edits + verify cycle in the smart zone
3. **"Ralph is back" cautionary PR** — concrete war story: 6-hour Ralph run, 27-rule React style guide, 20 commits, ~20,000 LOC, never merged due to ~100 merge conflicts. Lesson: "do not send your co-workers a 20k-line PR"
4. **Cron-Ralph production pattern** — 3 iterations per night against a stable end-state spec on an internal HumanLayer repo; "wake up to a slightly better codebase"
5. **Pipeline-Ralph** — chained Ralphs (docs → specs → product proposals → code); honest caveat that Dex's first attempt didn't go great
6. **Issue-triage Ralph** with **untrusted-input safety warning** — never feed public GitHub issues straight to a `--dangerously-skip-permissions` Claude (hidden HTML/markdown comment prompts); HumanLayer's Linear-queue Ralph has a vetting step
7. **Models cannot plan well** — they default to horizontal phased plans when an experienced engineer would slice one thing end-to-end first to learn unknowns. Strongest defense yet for human-in-the-loop planning at high automation levels
8. **Tracer bullets** (Pragmatic Programmer) — canonical name for Dex's "vertical plans over horizontal plans" claim from the RPI talk
9. **Learning tests** (Martin Fowler / Uncle Bob) — unit tests against external libraries (e.g. Claude Agent SDK) to capture and verify your assumptions about contracts; useful for AI dev because docs lie and contracts change
10. **"We are programming in English now"** — old programming books are more valuable than ever as prompt-writing manuals
11. **CodeLayer rebuilt from scratch in 6 weeks** (mid-Dec 2025 → late-Jan 2026) around CRISPY's guided multi-step workflows. Stop asking users to wield monolithic prompts — wrap deterministic control flow around the planning steps so the user's role is the highest-leverage parts
12. **Counterweight to Huntley** — "Ralph is probably not the right final answer for production software. If anything, it's an incredible lesson in how context windows work." Strongest measured response in the wiki to [[everything-is-a-ralph-loop]]'s "software development is dead" maximalism

Pages created/updated:
- `raw/youtube-transcripts/matt-pocock-dex-horthy-chat.md` (new — cleaned transcript)
- `wiki/sources/matt-pocock-dex-horthy-chat.md` (new)
- `wiki/concepts/context-engineering.md` (updated — added quadratic-attention section, cup metaphor, source link)
- `wiki/entities/humanlayer.md` (updated — CodeLayer rebuild timeline, new key claims, source link)
- `wiki/index.md` (updated — added source row)
- `wiki/log.md` (updated)

## [2026-04-13] ingest | Andrew × Dex Horthy — "Making AI Agents Mainstream with Dexter Horthy" (Humans in the Loop interview)

Ingested Andrew (Heavybit) interview with Dex Horthy on The Humans in the Loop Substack (March 26, 2026). Significant overlap with [[dex-rpi-to-crispy]] and [[matt-pocock-dex-horthy-chat]] but earns a separate source page for the **adoption/enterprise reframing** and the **product-vision articulation**.

New material beyond prior Dex sources:

1. **Expert-to-team adoption failure framing** — the tools work for the builders; break when enterprise engineers try the same recipes. "Standing in workshops full of enterprise engineers saying 'folks... don't forget to say the magic words. It was embarrassing.'"
2. **HumanLayer product vision** — explicit "Google Docs / Notion / Figma-like SDLC experience" framing. Positions [[humanlayer-codelayer|CodeLayer]] as a collaboration surface, not just a harness. Clearer articulation than any prior source
3. **Software self-building / SaaS-displacement thesis** — post-ZIRP "build internal tools" direction with Klarna's walked-back Salesforce/Workday narrative as caveat. Maturity counter: "There's a difference between spending 20 years building software and building an internal version in a hurry." Largely absent from his prior talks
4. **QRDSPWIP naming origin** — full acronym didn't stick; QRSPI is the adopted subset. Fills a gap in [[dex-rpi-to-crispy]]
5. **Ralph Loop "extract the lessons, don't ship it"** — HumanLayer's implementer agent operationalizes Ralph's context-engineering lesson: small/fast models write code + run tests; larger model spot-checks, keeps parent context low. Measured counterweight to [[everything-is-a-ralph-loop]] maximalism
6. **Beads vs. production distinction** (sharper) — "Nobody gets paged at 3 a.m. if [OSS projects are] broken. Nobody gets fined millions of dollars if it's done wrong." Cleaner enterprise/regulated boundary for the code-legibility mandate

Resolves the dangling "Humans in the Loop interview (March 2026)" reference in [[alexlavaee-rpi-to-qrspi]].

Pages created/updated:
- `raw/links/links.md` (updated — added URL)
- `wiki/sources/humans-in-the-loop-dex-interview.md` (new)
- `wiki/entities/humanlayer.md` (updated — added as source)
- `wiki/sources/alexlavaee-rpi-to-qrspi.md` (updated — resolved cross-reference)
- `wiki/index.md` (updated — added source row)
- `wiki/log.md` (updated)

## [2026-04-13] ingest | Kyle (HumanLayer) — "Skill Issue: Harness Engineering for Coding Agents"

Ingested HumanLayer's canonical configuration-layer post (March 12, 2026), authored by **Kyle (@0xblacklight)** — not Dex, though published on humanlayer.dev and building on Dex's vocabulary. This is the tactical companion to [[dex-rpi-to-crispy]]: methodology layer (Dex) + configuration layer (Kyle). Explicitly cited by [[alexlavaee-rpi-to-qrspi]] as the canonical articulation of "harness engineering."

Central thesis: *"it's not a model problem. It's a configuration problem."* Harness engineering (term coined by Viv Trivedy) ⊂ context engineering (coined by Dex) ⊂ prompt engineering. Mitchell Hashimoto's operational definition: *"anytime you find an agent makes a mistake, engineer a solution such that the agent never makes that mistake again."*

Six harness components with empirical advice from "hundreds of agent sessions":
1. **CLAUDE.md/AGENTS.md** under 60 lines; ETH Zurich (arxiv 2602.11988, 138 agentfiles) found LLM-generated files *hurt* performance by ~20% cost, human-written helped ~4%
2. **MCP servers** — prefer CLI tools when training familiarity is high
3. **Skills** — progressive disclosure, activation loads SKILL.md only when contextually relevant
4. **Sub-agents as context firewalls** — parent sees only prompt + result, intermediate noise isolated (cross-references Lavaee's same framing)
5. **Hooks** — biome + tsc example, "success is silent, only failures produce verbose output"
6. **Back-pressure mechanisms** — subset tests over full suite

Key original findings:
- **Linear MCP → CLI wrapper case study** — thousands of tokens saved by replacing MCP server with 6 CLAUDE.md examples
- **Reactive configuration philosophy** — add harness elements only after observed failures; preemptive design fails
- **Terminal Bench 2.0 harness overfitting data** — Opus 4.6 ranks #33 in Claude Code's harness but #5 in harnesses unseen during post-training. Evidence that harness customization has measurable headroom beyond model improvements

Pages created/updated:
- `raw/links/links.md` (updated — added URL)
- `wiki/sources/skill-issue-harness-engineering.md` (new)
- `wiki/entities/humanlayer.md` (updated — added as Configuration layer in product stack)
- `wiki/concepts/agent-harness.md` (updated — added as source)
- `wiki/sources/alexlavaee-rpi-to-qrspi.md` (updated — explicit citation link)
- `wiki/index.md` (updated — added source row)
- `wiki/log.md` (updated)

## [2026-04-13] ingest | Alex Lavaee — "From RPI to QRSPI: Rebuilding the First Structured Workflow for Coding Agents"

Ingested Alex Lavaee's informed commentary on Dex Horthy's RPI → QRSPI evolution. Overlaps substantially with [[dex-rpi-to-crispy]] but earns a separate source page for its independent contributions:

1. **Three-name taxonomy of RPI failures** — Instruction Budget Overflow, Magic Words Dependency, Plan-Reading Illusion. Sticky articulations of concepts Dex described in prose
2. **Cross-practitioner validation of the 40% context threshold** — beyond HumanLayer's single data point; strengthens the [[context-engineering]] claim
3. **Sub-agents as context firewalls vs. personas** — sharper architectural distinction than Dex explicitly makes. Sub-agents are context boundaries (filesystem artifacts), not role-playing characters
4. **Framing as discipline maturation** — "the craft is maturing," positioning structured workflows as engineering discipline subject to iteration. Direct counterweight to Ralph Loop maximalism

Author runs Atomic (open-source agent tooling). Article explicitly connects QRSPI to "harness engineering as the differentiator layer," aligning with [[anatomy-agent-harness]] thesis.

Pages created/updated:
- `raw/links/links.md` (updated — added URL)
- `wiki/sources/alexlavaee-rpi-to-qrspi.md` (new)
- `wiki/sources/dex-rpi-to-crispy.md` (updated — added cross-reference to commentary)
- `wiki/index.md` (updated — added source row)
- `wiki/log.md` (updated)

## [2026-04-13] ingest | Jesse Vincent — "Superpowers: How I'm using coding agents in October 2025"

Ingested the October 9, 2025 launch post for the Superpowers plugin — the earliest article in the series and precursor to [[superpowers-5]]. Central claim: **skills are the interesting part of agentic development** — reusable, documented capabilities (SKILL.md) that the framework enforces as mandatory when applicable. The brainstorm → plan → implement workflow already includes automatic git worktrees, two execution modes (human PM vs. subagent dispatch + code review), and RED/GREEN TDD — the seed of the seven-stage cascade documented in [[superpowers-5]] six months later.

Notable findings: (1) **Cialdini persuasion principles** (authority, scarcity, commitment, social proof) measurably improve LLM skill compliance — corroborated by Dan Shapiro's Wharton study, creating a bridge between the [[five-levels-shapiro]] author and the Superpowers methodology. (2) **Pressure-testing via subagent quizzes** — realistic scenarios ("production is bleeding money, do you debug or check ~/.claude/skills/?") surface compliance failures. (3) **Memory extraction** — Vincent fed Claude 2,249 markdown files of prior conversation lessons; most clustered issues were already covered by existing skills, validating the skill abstraction.

Pages created/updated:
- `raw/links/links.md` (updated — added blog URL)
- `wiki/sources/superpowers-intro.md` (new)
- `wiki/entities/superpowers.md` (updated — added as source, new key claims on skills/mandatory invocation/Cialdini)
- `wiki/sources/superpowers-5.md` (updated — added precursor link)
- `wiki/index.md` (updated — added source row, marked "earlier Superpowers installments" as partly ingested)

## [2026-04-13] create | Superpowers Entity Page (obra/superpowers)

Created entity page for **Superpowers** — Jesse Vincent's open-source agentic skills framework (github.com/obra/superpowers, MIT, launched October 2025). The concrete, installable companion to the [[superpowers-5]] blog post: ships the cascade patterns (plan → implement → review, adversarial subagent review, subagent-driven development) as composable skills rather than prose. Implements a mandatory 7-stage workflow (brainstorming → git worktrees → planning → execution → TDD → code review → branch completion) with enforced RED-GREEN-REFACTOR. Installable across Claude Code, Cursor, Codex, OpenCode, GitHub Copilot CLI, and Gemini CLI via plugin marketplaces. Positioned as a cross-platform skill-layer bet — distinct from IDE-bound tools (Kiro, CodeLayer) and from Ralph Loop maximalism.

Pages created/updated:
- `raw/links/links.md` (updated — added GitHub link)
- `wiki/entities/superpowers.md` (new)
- `wiki/sources/superpowers-5.md` (updated — added link to new entity page)
- `wiki/index.md` (updated — added entity row, marked Jesse Vincent as covered)
- `wiki/log.md` (updated)

## [2026-04-16] ingest | CodeSpeak — "First step in modularity: Spec dependencies and Managed files"

Ingested the CodeSpeak **March 9, 2026 blog post (v0.3.4)** — the **foundational** post in CodeSpeak's 2026 arc. Introduces the two primitives — **spec imports** and **managed files** — that every later feature (session-reading takeover, modular takeover) architecturally depends on. Fetched via Claude Code `WebFetch` with aggressive verbatim prompt; close-to-raw text retrieved, including the complete memo-app code example and full four-way trust-model option list.

This now completes the CodeSpeak-2026 dependency triangle in the wiki:

```
Mar 9 (v0.3.4)  — spec imports + managed files  ← infrastructure
Mar 17 (v0.3.6) — session-reading takeover       ← still single-spec output
Apr 8 (Modular) — web wizard + multi-spec output ← uses both above
```

Key new material beyond what was already in the wiki:

1. **Two new primitives: `import` directive + managed files.** Specs declare dependencies in frontmatter (`---\nimport storage.cs.md\n---`); CodeSpeak builds in dependency order, skipping unchanged specs. Every spec has a **scope** — the source files it owns; writes inside scope are silent, writes outside produce a notification.

2. **Change-scoping principle formalized:** *"when a spec S gets updated, only the code S manages should normally update."* Demonstrated concretely by the memo-app example: one-line diff in `storage.cs.md` (JSON → SQLite) rewrites `storage.py` only, `main.py` untouched because the storage interface didn't change.

3. **Four-way trust model for non-managed writes.** Default = permissive with notification. Alternatives: suppress notification, strict mode (block writes outside scope), per-spec whitelist (`codespeak update-managed-files`), project-wide whitelist with glob support (`codespeak whitelist 'config/*.yaml'`). This is a **nuanced and honest** trust model — CodeSpeak surfaces agent behavior at module boundaries rather than hiding or blocking it by default. Worth emulating elsewhere.

4. **Semantic diff titles in build progress.** Progress UI shows *"Changing memo storage from JSON to SQLite"* rather than generic *"Implement spec."* Suggests CodeSpeak does non-trivial spec-diff analysis — not just re-run-the-pipeline. Small but telling.

5. **Explicit admission of unsolved SDD correctness problems.** Future goals listed at the end of the post:
   - *"specifying APIs for specs to provide a clean boundary between modules"*
   - *"reporting errors when an imported spec does not provide what the importing one expects"*
   - *"generating modules in relative isolation to make them reusable in other projects"*
   
   These are the three hardest problems in modular SDD — contract definition, contract-violation detection, module isolation. **Not solved in v0.3.4.** Interface mismatches between imported specs don't produce errors; they produce code that may not work.

6. **`codespeak build` has change detection.** Passing `main.cs.md` when only `storage.cs.md` changed → only the storage spec rebuilds. Dependency graph + content-hash caching without explicit user config.

7. **First concrete example of modular SDD in the wiki.** The memo-app demo (10-line `storage.cs.md` + 15-line `main.cs.md` with import) is the minimum viable example of multi-spec SDD. Useful teaching artifact.

8. **Conceptual connection to BMAD `project-context.md` — by contrast.** BMAD pools context into one shared file across all agents. CodeSpeak managed files **isolate** context per-spec, with explicit crossing points. Two philosophies of multi-module SDD: pooling (BMAD) vs. isolation with observable boundaries (CodeSpeak). The wiki's Connections section surfaces this contrast.

9. **Connection to [[skill-issue-harness-engineering|Kyle's]] "success is silent" principle — inverted for boundaries.** Kyle: success silent, failures verbose. CodeSpeak managed files: in-scope writes silent, boundary crossings verbose. The inversion makes sense — you want to notice the agent touching something it doesn't own.

Pages created/updated:
- `raw/links/links.md` (updated — added item 16)
- `raw/codespeak-modularity.md` (new — close-to-verbatim article with complete memo-app code example and four-way trust-model table)
- `wiki/sources/codespeak-modularity.md` (new — full source page with Summary, 8 Key Claims, Connections to 9 pages, 8 Questions Raised)
- `wiki/entities/codespeak.md` (major update — added **Modularity Primitives (March 2026, v0.3.4)** section with import syntax, memo-app reference, four-way trust model table, and honest-future-work note; updated Blog Timeline row to link the new source page; updated sources frontmatter)
- `wiki/index.md` (updated — added source row)
- `wiki/log.md` (updated)

## [2026-04-16] ingest | Andrey Breslav (CodeSpeak) — "Your intent is everything: Reconstructing specs from vibe coding sessions"

Ingested the CodeSpeak March 17, 2026 blog post (**v0.3.6 release**) — the chronological predecessor to [[codespeak-modular-takeover]]. Fetched via Claude Code `WebFetch` with an aggressive verbatim prompt; this time the tool returned close-to-raw text (code blocks, CLI examples, progress-output verbatim), substantially more faithful than the April 8 fetch.

Key new material beyond what was already in the wiki:

1. **"Human intent is what matters" — CodeSpeak's philosophical manifesto.** Andrey Breslav's sharpest articulation of CodeSpeak's positioning: humans own *"the non-trivial, the differentiating, the interesting"*; LLMs fill gaps. *"Many things that have always been obvious to humans are now obvious to machines as well."* Position is structurally opposite to [[everything-is-a-ralph-loop|Huntley's]] *"software development is dead."*

2. **Strongest School-1 statement recorded in the wiki.** Breslav: *"Our goal is to eventually build a world where you don't need to look at the code at all, even to review it."* Hedged as future goal but direction unambiguous. Now the polar opposite of [[dex-rpi-to-crispy|Dex's]] "please read the code" reversal. [[code-legibility-debate]] has a clearer polar pair.

3. **Vibe coding definitively framed as intent-elicitation, not coding.** *"Dialog-based coding agents are good tools for intent elicitation and exploration."* Vibe coding's role is to help you *"overcome the blank canvas problem, and to understand what we want."* Output is a prototype + chat history — both *artifacts of thinking*, not end products. This is the sharpest vibe-vs-SDD framing in the wiki.

4. **Canonical shrink claim: 5-10× stated as rule-of-thumb.** *"Specs are often 5-10 times shorter, because they are more high-level."* The first time this number appears in CodeSpeak's public communications. Later validated by Folio (~7×) and Faker (9.9×) per [[codespeak-modular-takeover]].

5. **Vibe-session scale datapoint.** A single subsystem takeover processed **24 Claude Code sessions with 150 prompts**. First public datapoint on realistic vibe-coding session volume. Implications for context engineering: compressing 150-prompt history into one spec is a non-trivial problem.

6. **Session-reading primitive introduced — the foundation for modular takeover.** This post's takeover reads Claude Code sessions alongside code; it was the missing primitive that made April's modular decomposition accurate. Seeing both posts together exposes a visible three-week engineering cycle: the *"support generating more than one spec file"* limitation stated here as "to be fixed" is exactly what modular takeover solved 22 days later.

7. **Opt-in three-state permission flow.** *"[Y] Allow / [N] Not now / [D] No, never"* stored in `~/.codespeak/preferences.json` per-project. Privacy-by-design for session access, not just privacy-by-policy. Rare in AI developer tools.

8. **Honest current-version limitations list.** Breslav explicitly lists: single-spec only, Claude Code only, specs may miss or over-include, no delete-code-regenerate guarantee, no spec-diff → code-diff verification. *"Make sure that if we delete the code, an equivalent implementation can be generated from the spec"* is stated as a **future goal, not a current guarantee** — honest admission of the fundamental risk of strict-SDD.

9. **Version confirmation: 0.3.6, not v0.0.1.** This closes the out-of-date entity-page framing. The wiki now has CodeSpeak at 0.3.6 (March 17) and documented weekly releases up to April 15.

10. **Operational cost-engineering:** prompt caching enabled, Claude **Sonnet 4.6** as default model, opt-in **cost cap per build**, `.codespeak` snapshot folder (vs. previous `.last-known` files). Signals CodeSpeak usage at scale is producing real cost pressure.

11. **Anthropic-compatible providers via `ANTHROPIC_BASE_URL`** — `z.ai` cited as example. Whitelisted for security. CodeSpeak hedging against Anthropic lock-in.

12. **Language-agnostic autonomous test generation:** `codespeak coverage --auto-configure` (detects language + framework) + `codespeak coverage --target 100 --max-iterations 5` (iteratively adds missing tests). Test generation is part of the spec→code→verify loop, not a separate tool.

This post is the **philosophical and technical anchor** for the CodeSpeak corpus. Prior ingests documented the *product mechanics* (modular takeover wizard, shrink factors). This post documents the *why* — and provides the strongest code-legibility School-1 quote in the wiki.

Pages created/updated:
- `raw/links/links.md` (updated — added item 15)
- `raw/codespeak-vibe-takeover.md` (new — close-to-verbatim article with retrieval note)
- `wiki/sources/codespeak-vibe-takeover.md` (new — full source page with Summary, Key Claims, Connections, Questions Raised)
- `wiki/entities/codespeak.md` (updated — added **Philosophy** section with manifesto quote + **Session-reading Takeover** section documenting v0.3.6 capability + 24-session/150-prompt scale + `.codespeak` preferences path; updated sources frontmatter; updated Blog Timeline row to link the new source page)
- `wiki/concepts/code-legibility-debate.md` (updated — added [[codespeak-vibe-takeover]] as strongest School-1 statement; added frontmatter source)
- `wiki/index.md` (updated — added source row)
- `wiki/log.md` (updated)

## [2026-04-16] ingest | Dmitry Savvinov (CodeSpeak) — "Modular takeover: from vibe-coded app to spec-driven development"

Ingested the CodeSpeak April 8, 2026 blog post announcing **modular takeover** — the platform's April release that converts vibe-coded applications into multiple focused `.cs.md` specs via an interactive browser wizard. This is a major capability update to [[codespeak]] that renders the existing entity page's "Alpha v0.0.1 / primarily greenfield" framing out of date.

**Retrieval caveat:** fetched via Claude Code `WebFetch`, which pipes HTML → markdown → AI processing. Direct quotes preserved where tool marked them; non-quoted prose is close paraphrase, not 1:1 text. Raw file (`raw/codespeak-modular-takeover.md`) includes an explicit retrieval note.

Key new material beyond the existing entity page:

1. **Vibe coding and SDD repositioned as sequential phases** — "Vibe coding excels at exploration. Evolving a vibe-coded app carefully is a different problem." The post frames modular takeover as an **off-ramp from vibe coding to SDD**, sharpening the [[ai-in-sdlc-research|dual-track thesis]] from "parallel alternatives" to "sequential stages with CodeSpeak as the graduation tool."

2. **Folio case study — concrete shrink-factor data** — A ~3,000-line Go dual-pane terminal file manager was decomposed by `codespeak takeover` into 4 focused specs totaling **430 lines of Markdown (~7× reduction)**. First empirical dataset in the wiki on spec-vs-code size ratios. Combined with prior CodeSpeak numbers (Faker 9.9×, others 5.9–9×), the shrink factor appears to hold at 6–10× for bounded projects; production-SaaS data still absent.

3. **Interactive web wizard for module boundaries** — The decomposition is not fully automated. The wizard proposes a "coarse initial structure reflecting the application's gross structure"; the developer can request splits, merges, rearrangements before confirming. Takeover is **human-gated at the module-boundary level**.

4. **Concrete intent-preservation example** — Terminal-panel keyboard-passthrough rule: "only the following keys are handled by the application itself rather than forwarded to the terminal process: Ctrl+T, Ctrl+\\, Ctrl+Up, Ctrl+Down." The *why* (F10 must be forwarded so `htop` works inside the terminal) is documented in the spec as one sentence. In implementation code, it's invisible switch/case exclusions. Sharpest concrete example of [[dex-rpi-to-crispy|Mental Alignment via artifacts]] in the wiki.

5. **Post-takeover Level-4 SDD demonstrated** — Adding F7/mkdir keybinding required: one function description in `file-ops.cs.md`, one row in keybinding table in `app.cs.md`. After `codespeak build`: all Go code (function, keyboard handlers, input routing, panel refresh) was auto-generated with no manual code writing. Evidence that takeover produces specs that function as source-of-truth for subsequent evolution, not just documentation.

6. **Monolithic → modular evolution** — February's `codespeak takeover` produced a single monolithic spec file. April's version produces **multiple coupled specs** via "Managed files" + spec-dependencies machinery introduced in March. Parallels conventional SE's move from monorepo-single-package to modular.

7. **Demo artifact is reproducible** — `codespeak-dev/folio`, branch `modular-takeover`, verified via `gh api` (repo pushed 2026-04-08). Includes both generated specs and the mkdir feature implementation.

8. **Blog timeline context** — Seven-week evolution: monolithic takeover (Feb 23) → test generation (Mar 2) → spec dependencies + Managed files (Mar 9) → session-reconstructed specs + Anthropic-compatible providers (Mar 17) → `impl`/`test` commands (Mar 24) → **modular takeover with wizard** (Apr 8) → `vibe-sharing` data-donation repo (Apr 15). Weekly release cadence. Fetched the full timeline via `WebFetch` on `codespeak.dev/blog`.

9. **CLI is now public** — `uv tool install codespeak-cli`. Previously GitHub-App-only. Commands: `init`, `build`, `takeover`, `impl`, `test`.

10. **Data-strategy signal** — `codespeak-dev/vibe-sharing` (launched April 15, one week after modular takeover) asks users to donate vibe-coded projects — code + git history + agent sessions — for improving takeover quality. Takeover is the product priority; the team is betting on user-contributed training data. Implications: privacy, quality plateau vs. growth.

This post also strengthens the [[code-legibility-debate]] School 1 position — when specs are 7–10× shorter than code and capture intent code doesn't, "read the spec, not the code" becomes empirically defensible for well-bounded applications.

Pages created/updated:
- `raw/links/links.md` (updated — added item 14: blog URL + demo repo + CLI install command)
- `raw/codespeak-modular-takeover.md` (new — article text with retrieval caveat, repo reference, and blog-timeline context)
- `wiki/sources/codespeak-modular-takeover.md` (new — full source page with Summary, Key Claims, Connections, Questions Raised)
- `wiki/entities/codespeak.md` (major update — new Modular Takeover section with shrink-factor table and keyboard-passthrough example; new CLI Commands section; Community/Data Strategy section; Blog Timeline table; updated Status to "Active alpha, weekly releases"; updated Comparison table; partially closed brownfield open question)
- `wiki/index.md` (updated — new source row; updated CodeSpeak entity summary)
- `wiki/log.md` (updated)

## [2026-04-16] ingest | Paul Everett — "Spec-Driven Development with Coding Agents" (DeepLearning.AI × JetBrains course)

Ingested the DeepLearning.AI × JetBrains short course taught by **Paul Everett** (JetBrains developer advocate), introduced by **Andrew Ng**. First structured hands-on course source in the wiki (vs. talks, blog posts, or papers). Ships a reproducible companion repo (`https-deeplearning-ai/sc-spec-driven-development-files`) with 10 lesson-snapshot folders, example specs, and two reusable skills (`changelog`, `feature-spec`). Verified the repo via `gh api` and pulled excerpts from `Lesson_08/specs/mission.md`, `roadmap.md`, and `skills/feature-spec/SKILL.md` for grounding.

The course codifies the most prescriptive greenfield SDD workflow the wiki has documented to date:

1. **Constitution (3 files)** — `mission.md` (why / stakeholders), `tech-stack.md` (how / engineers), `roadmap.md` (what next / living phase list). Agent-agnostic, structured — explicitly contrasted with the monolithic `agents.md` pattern.
2. **Feature loop (3 files, on a dated branch)** — `specs/YYYY-MM-DD-<feature-name>/` containing `plan.md` (numbered task groups), `requirements.md` (Scope/Decisions/Context), `validation.md` (automated + manual + tone + definition-of-done). `/clear` between features is explicit discipline.
3. **Replanning** as a first-class phase — constitution updates in their own branch, product-manager updates absorbed into specs *before* code, workflow improvements captured as **skills**.

New material beyond prior SDD sources:

- **"The agent is the muscle, but the SPEC is the brain"** — clean pedagogical summary of the architect analogy, targeting professional IDE users.
- **`AskUserQuestion` with exactly 3 questions (Scope / Decisions / Context)** — codified in the `feature-spec` SKILL.md interview pattern; the structure is the contribution, the tool is optional.
- **"Don't edit directly — ask the agent"** — Lesson 4's anti-drift rule: manual edits bypass the agent and make other artifacts fall out of sync. Most explicit drift-discipline articulation in the wiki.
- **Cognitive debt / AI fatigue as human-side complement to context rot** — Lessons 7 and 9. Managed by size discipline (smaller task groups) and review level (spec, not CSS class).
- **Sub-agents for deep review "preserve the main agent's context window, rather than polluting it"** — first appearance of the [[alexlavaee-rpi-to-qrspi|Lavaee context-firewall framing]] in **mainstream course content**. Direct word-for-word convergence without cross-reference.
- **MVP as an "extreme test" of the constitution** — Lesson 10 reframes shipping the rest of the roadmap in one shot: only do this if you trust your spec; if the output drifts, that's a signal to replan, not to rush.
- **Brownfield by reverse-engineering** — Lesson 11: "the agent will discover and in a sense reverse-engineer the SDD artifacts from the existing code base." Inputs = README, TODO, issue trackers, commits. Most accessible brownfield SDD framing in the wiki.
- **Middle-ground position in the code-legibility debate** — Lesson 7 leans School 1 ("focus on whether features reflect the spec, not CSS classes"), Lesson 9 leans School 2 ("make sure it creates code you can commit under your name"). Synthesis: review at spec/behavior level; reserve line-level reading for security, DB, compounding areas.
- **Tool-agnostic stance** — "The specs travel with you when you switch tools." WebStorm + Claude Code is shown but VS Code + Codex CLI, Zed + local model, Cursor, Gemini CLI are all flagged as equivalent. Convergent with [[alexlavaee-rpi-to-qrspi|Lavaee's]] portability claim but framed as an onboarding benefit.
- **JetBrains partnership signal** — IDE vendor betting on SDD as a reason to stay in professional IDEs rather than migrating to chat-first AI UIs.

Pages created/updated:
- `raw/links/links.md` (updated — added item 13: course URL + companion repo)
- `raw/sdd-course-deeplearning-ai.md` (new — transcript consolidated across 12 video segments + verified repo structure + pulled excerpts from `Lesson_08/specs/mission.md`, `roadmap.md`, and `skills/feature-spec/SKILL.md`)
- `wiki/sources/sdd-course-deeplearning-ai.md` (new — full source page with Summary, Key Claims, Connections, Questions Raised)
- `wiki/concepts/spec-driven-development.md` (major update — added Canonical Workflow section with three-layer Constitution/Feature-Loop/Replanning structure; refreshed Key Sources, vibe-coding contrast, Open Questions)
- `wiki/concepts/context-engineering.md` (updated — added course to Key Sources with cognitive-debt and sub-agents-as-context-firewall points)
- `wiki/concepts/code-legibility-debate.md` (updated — added course as mainstream middle-ground articulation)
- `wiki/index.md` (updated — added source row)
- `wiki/log.md` (updated)

**Note:** The user-supplied transcript was truncated partway through Lesson 11. Lessons 12 ("Build Your Own Workflow") and 13 ("Agent Replaceability") are present in the companion repo but not in the ingested transcript. Worth ingesting later — Lesson 13's "Agent Replaceability" is particularly relevant to the wiki's tool-portability thread.

## [2026-04-16] ingest-stub | Cole Medin — "Building an AI Dark Factory: A Codebase That Writes Its Own Code, Live"

Registered a new source: **Cole Medin's** YouTube Live (~2h 24m), ID `Xg0tNz9pICI`, explicitly titled around the **Dark Factory** concept from [[five-levels-shapiro|Shapiro's Level 5]]. This is the wiki's first source from Cole Medin (Dynamous AI founder), and a direct contribution to the [[software-factory]] pillar from a creator aimed at mainstream AI-developer audiences rather than the HumanLayer/Huntley enterprise-frontier corner of the debate.

**⚠️ Transcript retrieval failed from this environment.** YouTube is actively blocking this cloud-provider IP range, and every public transcript mirror attempted (Invidious instances × 15+, Piped instances, ytscribe, tactiq, noembed, downsub, youtube-transcript.io, kome.ai, supadata, pytubefix, yt-dlp, youtube-transcript-api) returned HTTP 401/403/429/503, required auth, or served an empty body. Metadata (title, channel, duration 8615s, thumbnail URL) was retrieved via YouTube's oEmbed endpoint + pytubefix before caption access was blocked.

The source page is currently a **metadata-only stub** that captures expected Connections and Questions Raised based on the title, the channel's prior emphasis on context engineering, and the surrounding wiki context (Dark Factory is the strong-form "don't read the code" end of the [[code-legibility-debate]], sits at/above [[everything-is-a-ralph-loop|Huntley's Level 9]], and inverts [[dex-rpi-to-crispy|Dex's]] "please read the code" reversal). The raw transcript file contains manual-ingest instructions for completing the ingestion from a browser or residential IP.

Pages created/updated:
- `raw/links/links.md` (updated — added item 12: Cole Medin's YouTube Live)
- `raw/youtube-transcripts/cole-medin-ai-dark-factory.md` (new — metadata + manual-ingest instructions; transcript body pending)
- `wiki/sources/cole-medin-ai-dark-factory.md` (new — stub with Pending Transcript notice, Why This Source Matters, expected Connections, Questions Raised)
- `wiki/index.md` (updated — added source row with pending-transcript warning)
- `wiki/log.md` (updated)

## [2026-04-16] ingest | Murat Aslan — "The Agentic Coding Stack: 7 Tools, 5 Layers, and the Missing Link Nobody Has Built Yet"

Ingested Murat Aslan's April 2026 Dev Genius post (Series 1 of "Agentic Coding Systems"). The post is the wiki's cleanest cross-pillar synthesis to date — it touches all five research pillars in a single 13-min read.

**Retrieval note:** Cloudflare blocked direct curl/WebFetch on `blog.devgenius.io` (and `medium.com/p/<id>`). Article body retrieved via Playwright headless browser DOM `innerText` extraction. Wayback Machine had no snapshot. Raw file (`raw/agentic-coding-stack-aslan-2026.md`) contains the full ~20.6k-char verbatim article body.

Aslan's central move is to reject "which tool wins?" framing and propose a **five-layer composition model** for the agentic coding stack:

- **L1 — Delivery Methodology** (when should the AI analyze/plan/implement?): [[bmad-method|BMAD-METHOD]], [[spec-kit]]
- **L2 — Agent Discipline** (how should the AI behave while building?): [[superpowers]]
- **L3 — Technical Context** (what does the code actually mean?): [[ctxo|Ctxo]]
- **L4 — Token Optimization** (how much tool output should enter context?): [[rtk|RTK]], [[context-mode]]
- **L5 — Product Surface** (where does the developer operate the whole system?): [[gsd-2]]

Each layer reduces a specific subset of **five named failure modes** (consistency failures, context loss, specification gaps, review bottlenecks, multi-session conflicts). This is the wiki's first explicit failure-mode taxonomy for agentic coding.

Headline thesis: the **bridge between specification and implementation is still weak**. Aslan calls **spec-to-code traceability** the unbuilt missing link — *"If someone builds that bridge well, they will own the most strategic connective tissue in the agentic coding stack."* Four operational questions the bridge must answer (which symbols implement RQ-12, which tests cover this spec item, what breaks if requirement X changes, who else is touching this).

Key new material:

1. **Cleanest cross-pillar synthesis the wiki has ingested.** Touches all five pillars in one post.
2. **First explicit failure-mode taxonomy** for agentic coding (5 modes mapped to layers).
3. **Four genuinely new entities** added to the wiki: [[ctxo|Ctxo]] (semantic codebase MCP server with 6 primitives — `get_blast_radius`, `get_logic_slice`, `get_why_context`, `get_symbol_importance`, `find_dead_code`, `get_pr_impact`), [[rtk|RTK]] (Rust shell-output proxy with command-specific filters), [[context-mode]] (MCP sandbox where agent writes code and only `console.log()` enters context; SQLite+FTS5 cross-session continuity), [[gsd-2]] (autonomous coding platform with worktree isolation, state recovery, multi-provider, cost tracking, milestone execution).
4. **Sharpens [[superpowers]] positioning** as the sole L2 (Agent Discipline) tool. The cleanest single-sentence framing the wiki has yet recorded: *"If BMAD/spec-kit answers 'what order should work happen in?', superpowers answers 'how do we stop the agent from being sloppy once work begins?'"*
5. **Closes the L3 wiki gap.** Most existing entities improve *how* an agent operates or *what process* it follows; Ctxo is the first wiki entity dedicated to improving **what the agent understands about the code**. Aslan: *"The scarcest capability in the current ecosystem."*
6. **Pairs RTK and context-mode as composable L4 stages** — first wiki articulation of multi-layer token-optimization composition. RTK at OS/shell hook (filter after); context-mode at MCP sandbox (prevent before). Aslan: *"RTK reduces noisy shell output, then context-mode keeps the remainder from flooding the conversation."*
7. **Introduces a third position in the [[code-legibility-debate]]: the Traceability School** — *don't* pre-commit to either "read the code" (School 2) or "treat as black box" (School 1); build infrastructure to navigate spec ↔ code on demand. Reading becomes a query response, not a default discipline.
8. **Sister piece to [[anatomy-agent-harness]].** Pachaar slices the territory by component (12 components, 7 architectural decisions, 5 frameworks); Aslan slices the same territory by workflow layer (5 layers, 7 tools). Both 2026 syntheses; neither cites the other; the convergence on a layered/component view of agentic coding is itself a wiki-worthy data point.
9. **Notable absence: [[codespeak]].** CodeSpeak is the wiki's most aggressive spec-driven platform but doesn't appear in Aslan's seven. Possible reasons: post focuses on **agentic** coding (interactive AI agents); CodeSpeak's `codespeak build` is more pipeline than agent. Worth flagging as an analysis question.

Pages created/updated:

- `raw/links/links.md` (updated — added item 17)
- `raw/agentic-coding-stack-aslan-2026.md` (new — verbatim article body via Playwright; retrieval note included)
- `wiki/sources/agentic-coding-stack-aslan.md` (new — full source page with Summary, 9 Key Claims, Connections to 14 pages, 7 Questions Raised)
- `wiki/entities/ctxo.md` (new — L3 Technical Context, 6 semantic-analysis primitives, "scarcest capability" framing)
- `wiki/entities/rtk.md` (new — L4 Token Optimization, Rust CLI proxy, command-specific filters)
- `wiki/entities/context-mode.md` (new — L4 Token Optimization, MCP sandbox, SQLite+FTS5 continuity)
- `wiki/entities/gsd-2.md` (new — L5 Product Surface, autonomous platform, sibling to CodeLayer/ACP)
- `wiki/entities/bmad-method.md` (updated — new "Position in the Aslan Stack" section, L1 framing, source row)
- `wiki/entities/spec-kit.md` (updated — workflow chain corrected to `constitution → specify → plan → tasks → implement` per Aslan, new "Position in the Aslan Stack" section)
- `wiki/entities/superpowers.md` (updated — new "Position in the Aslan Stack" section, L2 framing as the sole "Agent Discipline" tool)
- `wiki/concepts/agentic-coding-stack-layers.md` (new — formal concept page for the 5-layer model; cross-walks with [[agent-harness]] and Kyle's six harness components; wiki-entity slot triage; lessons; open questions)
- `wiki/concepts/agent-harness.md` (updated — added [[agentic-coding-stack-layers]] as workflow-oriented complement)
- `wiki/concepts/context-engineering.md` (updated — added Aslan as L4 source; promotes context engineering from inside-the-loop discipline to outside-the-loop installable infrastructure)
- `wiki/concepts/spec-driven-development.md` (updated — added Aslan source; new "spec-to-code traceability" open question)
- `wiki/concepts/code-legibility-debate.md` (updated — added **School 3: Traceability School**; added Aslan as primary School-3 source)
- `wiki/index.md` (updated — added source row, new concept row, 4 new entity rows, new "to-create" item: Spec-to-code traceability)
- `wiki/overview.md` (updated — new thesis point #15 on stack-as-composition + missing link; source row #14; two new open questions)
- `wiki/log.md` (updated)

## [2026-04-25] ingest | Chad Woolley — "The Software Factory: A Practitioner's Guide to Specification-Driven Development for Enterprise Services"

Ingested Chad Woolley (GitLab) February 2026 practitioner guide. Most comprehensive reference yet published on factory-pattern software development. Direct URL: https://gitlab.com/cwoolley-gitlab/software-factory-practitioners-guide/-/blob/main/software-factory-practitioners-guide-v01.md (raw markdown fetched via curl).

**Context**: Woolley has hands-on experience with the factory pattern (forked Kilroy, week of experimentation) AND is transparent about what doesn't work ("I have not yet produced usable software with this approach"). Frames guide as "aspirational" — StrongDM demonstrated it at a startup with greenfield codebase; no large enterprise has publicly shared a factory implementation at scale.

**Core insight**: Factory-pattern development introduces a fundamental repository structure divide:
- `spec/` (intent/contracts/constraints) — human-managed
- `holdout-scenarios/` — human-authored validation, kept hidden from coding agents
- `factory/` (Attractor graph, orchestration config) — human-authored
- `src/` (generated code) — machine-produced, opaque, version-controlled for auditability

**Key innovation**: [[holdout-scenarios|Holdout scenario validation]] — scenarios kept separate from implementation to prevent agents from reward-hacking (optimizing for tests rather than genuine correctness). Borrowed from ML holdout-set practice.

**The shift work pattern** (StrongDM terminology): Separation into interactive shift (humans + spec-refinement agents on specifications/scenarios) and non-interactive shift ([[attractor]] runs autonomously, potentially for hours). Central unsolved question: when is a specification "complete enough" for autonomous execution?

**Three separate agent sets** prevent gaming:
1. Spec-refinement agents (interactive, see specs/scenarios, never see implementation code)
2. Factory execution agents / [[attractor]] (non-interactive, see specs, never see holdout scenarios)
3. Validation agents (see scenarios + running artifact, never see source code)

**The Attractor pattern**: DOT-graph-structured orchestration of coding agents through phases (scaffold → implement → test → refine → converge). Each phase is a node, edges are LLM-evaluable conditions. Different models can run different phases (reasoning-heavy for architecture, fast models for boilerplate).

**Satisfaction metric**: Probabilistic validation — "across all observed trajectories, what fraction likely satisfies the user?" Shift from boolean (pass/fail) to probabilistic (95%, 97%) validation, necessary for agentic software with inherent non-determinism.

**Digital Twin Universe (DTU)**: Behavioral clones of all external dependencies (Okta API, Jira API, Slack API, Google Workspace APIs for StrongDM). Enables deterministic, high-volume validation at factory scale without hitting rate limits. Can itself be built by agents from API documentation.

**NLSpec** (Natural-Language Specification): Markdown documents precise enough for agents to implement against, yet human-readable. Answers three questions: what, under what conditions, why it matters. The rigor bottleneck: "you cannot take shortcuts by relying too heavily on AI to generate the specification... Defining specifications with machine-executable rigor, when you can't rely on a domain-aware human to 'know what you really mean,' is genuinely hard."

**Most honest acknowledgement in the guide**: "I have not yet produced usable software with the Software Factory approach, even of alpha quality. After a week or two of hands-on experimentation, the main lessons have been about what doesn't work."

**Out-of-scope but critical**: Governance, agent security, organizational transformation, cost management ($1,000/day per engineer is aggressive), legal/compliance frameworks, SOA boundary coordination, enterprise adoption.

Pages created/updated:

- `wiki/sources/software-factory-practitioners-guide-woolley.md` (new — comprehensive source page)
- `wiki/entities/strongdm.md` (new — Company page; primary reference implementation)
- `wiki/entities/attractor.md` (new — Orchestration pattern; DOT graphs, phase-based, provider-aligned agents)
- `wiki/concepts/shift-work.md` (new — Interactive/non-interactive separation; central unsolved boundary question)
- `wiki/concepts/holdout-scenarios.md` (new — Validation mechanism; separate agent sets; prevent reward-hacking)
- `wiki/concepts/nlspec.md` (new — Natural-language specification; rigor bottleneck; machine-executable prose)
- `wiki/concepts/digital-twin-universe.md` (new — Behavioral clones of dependencies; deterministic validation infrastructure)
- `wiki/index.md` (updated — added source row, 4 new concept rows, 2 new entity rows, marked Woolley source as ingested)
- `wiki/log.md` (this entry)

**Assessment**: This is the most practical and honest guide to factory-pattern development yet published. Woolley's transparency about difficulties and unresolved questions (especially specification completeness and production-signal feedback) increases credibility. He frames the guide as "aspirational" and acknowledges the gap between theoretical possibility and what's been demonstrated at scale. For the wiki's "software factories" pillar, this is comparable in importance to [[five-levels-shapiro]] for automation levels — a primary reference that systematizes emerging practice into concrete, implementable patterns.

