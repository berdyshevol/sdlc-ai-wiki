---
title: Wiki Log
type: log
created: 2026-04-08
updated: 2026-04-13
---

# Wiki Log

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
