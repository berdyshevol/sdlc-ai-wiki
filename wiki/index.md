---
title: Wiki Index
type: index
created: 2026-04-08
updated: 2026-04-16
last_change: agentic-coding-stack-aslan ingest
---

# Wiki Index

## Overview

- [[overview]] — High-level synthesis of all research. Start here.

## Sources

| Page | Author | Pillar | Summary |
|------|--------|--------|---------|
| [[five-levels-shapiro]] | Dan Shapiro | Industry/Factories | Five-level maturity model from "spicy autocomplete" to autonomous "dark factory." Most devs stuck at Level 2. |
| [[superpowers-intro]] | Jesse Vincent | Agents/Spec-Driven | Oct 2025 launch post for the Superpowers plugin. Skills as the reusable unit of agent capability, mandatory skill invocation, Cialdini persuasion principles improve LLM compliance, brainstorm→plan→implement with worktrees + TDD. |
| [[superpowers-5]] | Jesse Vincent | Agents/Spec-Driven | Subagent-driven development, adversarial spec review, cascade pattern (spec → implement → review). |
| [[12-factor-agents]] | Dex (HumanLayer) | Coding Agents | 12 principles for production AI agents: own your prompts, own your control flow, small focused agents. |
| [[humanlayer-codelayer]] | Dex (HumanLayer) | Coding Agents | Open-source IDE for orchestrating AI coding agents. "Superhuman for Claude Code." MultiClaude parallel sessions. |
| [[agent-control-plane]] | Dex (HumanLayer) | Coding Agents | Kubernetes-native orchestration for long-lived autonomous agents. Async-first, MCP support, agent-to-agent delegation. |
| [[dex-rpi-to-crispy]] | Dex (HumanLayer) | Coding Agents / Code Legibility | RPI methodology failures and evolution to CRISPY/QRSPI. Major reversal on code legibility. Instruction budget, Smart Zone, Mental Alignment. |
| [[alexlavaee-rpi-to-qrspi]] | Alex Lavaee | Coding Agents / Code Legibility | Independent commentary on Dex's RPI → QRSPI. Names three failure modes (Instruction Budget Overflow, Magic Words Dependency, Plan-Reading Illusion). Cross-practitioner validation of 40% context threshold. Sub-agents as context firewalls vs. personas. |
| [[skill-issue-harness-engineering]] | Kyle (HumanLayer) | Coding Agents | Tactical configuration-layer companion to Dex's CRISPY talk. Six harness levers (CLAUDE.md, MCP, skills, sub-agents, hooks, back-pressure). Linear MCP→CLI case study. Reactive configuration philosophy. "Success is silent." Terminal Bench 2.0 shows Opus 4.6 overfit to Claude Code harness (#33 → #5 in others). |
| [[humans-in-the-loop-dex-interview]] | Andrew × Dex Horthy | Coding Agents / Industry | Heavybit Substack interview (Mar 26 2026). Mainstream-adoption reframing of CRISPY story. Product vision: "Google Docs/Notion/Figma-like SDLC." SaaS-displacement thesis with Klarna caveat. Ralph Loop "extract the lessons, don't ship it" position. QRDSPWIP naming origin. |
| [[coding-agents-conf-2026]] | Multiple speakers | Industry (all pillars) | Full-day conference: trust ladder (Kilo Code 25T tokens), agentic search vs RAG, agent memory, SWE Atlas, enterprise governance, security. |
| [[ai-in-sdlc-research]] | Academic paper | Industry/Spec-Driven/Agents | Full survey: AI across all SDLC stages, Copilot case study, spec-driven vs. vibe coding bifurcation, practitioner SDD observation (5-person team). |
| [[anatomy-agent-harness]] | Akshay Pachaar | Coding Agents | Comprehensive anatomy of the agent harness: 12 components, 7 architectural decisions, 5-framework comparison. "The harness is the product, not the model." |
| [[long-running-claude]] | Siddharth Mishra-Sharma (Anthropic) | Coding Agents / Factories | Multi-day autonomous Claude Code for scientific computing. Five patterns: CLAUDE.md as living plan, CHANGELOG.md as lab notes, test oracles, git as coordination, Ralph Loop. Months-to-days time compression. |
| [[everything-is-a-ralph-loop]] | Geoffrey Huntley | Software Factories | Ralph Loop as mindset and orchestrator pattern. Extends automation to "level 9" — evolutionary software that self-heals and optimizes for revenue. Introduces The Weaving Loom. Provocative claim: "software development is dead." |
| [[everything-is-a-ralph-loop]] | Geoffrey Huntley | Software Factories | Ralph Loop as mindset and orchestrator pattern. Extends automation to "level 9" — evolutionary software that self-heals and optimizes for revenue. Introduces The Weaving Loom. Provocative claim: "software development is dead." |
| [[bmad-method-docs]] | bmadcode | Spec-Driven | Official BMAD docs: four-phase cycle, three planning tracks (Quick Flow/BMad/Enterprise), 6 named agent personas, adversarial review, fresh-chat requirement, project-context.md as shared context. |
| [[matt-pocock-dex-horthy-chat]] | Matt Pocock × Dex (HumanLayer) | Coding Agents | Live conversation (Jan 2026): cup metaphor for task sizing, quadratic-attention explained, "Ralph is back" 20k-LOC cautionary PR, cron-Ralph (3 iterations/night), pipeline-Ralph, untrusted-input safety, learning tests, tracer bullets, CodeLayer rebuilt in 6 weeks around CRISPY. |
| [[cole-medin-ai-dark-factory]] | Cole Medin | Software Factories | YouTube Live (~2h 24m): "Building an AI Dark Factory: A Codebase That Writes Its Own Code." ⚠️ Transcript pending — metadata-only stub; auto-captions blocked from this environment. |
| [[sdd-course-deeplearning-ai]] | Paul Everett (JetBrains) | Spec-Driven | DeepLearning.AI × JetBrains course (Andrew Ng intro). Three-file Constitution (mission/tech-stack/roadmap) + per-feature loop on dated branches (plan/requirements/validation) + explicit replanning phase. Skills as workflow automation. Brownfield by reverse-engineering from existing code. First mainstream course articulation of the full SDD loop; reproducible companion repo with 10 lesson snapshots. |
| [[codespeak-modular-takeover]] | Dmitry Savvinov (CodeSpeak) | Spec-Driven | Apr 8 blog post announcing CodeSpeak's **modular takeover**: vibe-coded app → `codespeak takeover` → interactive web wizard proposes modular decomposition → confirm → multiple focused specs. Folio demo: ~3000 Go LOC → 430 MD lines × 4 specs = **~7× shrink**. Reframes vibe coding and SDD as **sequential phases** (not parallel alternatives). First quantitative shrink-factor dataset in the wiki. |
| [[codespeak-vibe-takeover]] | Andrey Breslav (CodeSpeak) | Spec-Driven / Code Legibility | Mar 17 post (CodeSpeak 0.3.6): takeover reads Claude Code sessions (24 sessions / 150 prompts per subsystem), language-agnostic LCOV coverage, Anthropic-compatible providers. Philosophical core: *"human intent is what matters"* + maximalist goal *"build a world where you don't need to look at the code at all, even to review it."* **Strongest School-1 statement in the wiki.** Chronological predecessor to modular takeover. |
| [[codespeak-modularity]] | CodeSpeak team | Spec-Driven | Mar 9 post (CodeSpeak 0.3.4): introduces **spec imports** (`import X.cs.md` in frontmatter, transitive, dependency-ordered builds) + **managed files** (per-spec source-file scope with four-way trust model for non-managed writes). The **architectural foundation** for multi-spec CodeSpeak projects — modular takeover (Apr 8) runs on this primitive. Memo-app demo shows one-line spec change rewriting only one module. |
| [[agentic-coding-stack-aslan]] | Murat Aslan | All five pillars | Apr 2026 Dev Genius post. Stack-map of 7 tools across 5 layers (Delivery Methodology / Agent Discipline / Technical Context / Token Optimization / Product Surface). First explicit failure-mode taxonomy for agentic coding (5 modes). Adds 4 new entities to the wiki ([[ctxo|Ctxo]], [[rtk|RTK]], [[context-mode]], [[gsd-2]]). Sharpens [[superpowers]] positioning at L2. Names **spec-to-code traceability** as the unbuilt missing link — third position in [[code-legibility-debate]]. |
| [[software-factory-practitioners-guide-woolley]] | Chad Woolley (GitLab) | Software Factories | Feb 2026 practitioner guide: most comprehensive reference yet. Repository structure (spec/holdings/factory/src), NLSpec definition, [[shift-work]] (interactive/non-interactive), [[holdout-scenarios]] (prevent reward-hacking), [[attractor]] orchestration, [[digital-twin-universe]], three agent sets, satisfaction metric. Honest about what doesn't work. **No large enterprise has implemented at scale yet.** |

### Sources To Ingest

- lukepm.com — "The Software Factory"
- ~~blog.fsck.com — Superpowers series (earlier installments)~~ ✅ Oct 2025 launch post ingested as [[superpowers-intro]]
- ~~Spec-kit documentation/articles~~ ✅ entity page created
- ~~BMAD method documentation~~ ✅ entity page created, ✅ source page ingested from official docs
- ~~Kiro (AWS) documentation~~ ✅ entity page created
- ~~Chad Woolley — "Software Factory: A Practitioner's Guide"~~ ✅ Feb 2026 ingested as [[software-factory-practitioners-guide-woolley]], created [[strongdm]], [[attractor]], [[shift-work]], [[holdout-scenarios]], [[nlspec]], [[digital-twin-universe]]
- Devin case studies/reviews
- Industry landscape reports

## Concepts

| Page | Pillar | Summary |
|------|--------|---------|
| [[spec-driven-development]] | Spec-Driven | Specifications as the primary artifact; code generated from specs by AI. The gateway to Level 4+. |
| [[software-factory]] | Software Factories | Fully automated software production — specs in, working software out. Shapiro's "Dark Factory" vision. |
| [[automation-levels]] | Industry | Five-level maturity model for AI in SDLC. Role transformation at each level, not just productivity. |
| [[code-legibility-debate]] | Code Legibility | Should devs read AI-generated code? Two schools: "black box" vs. "must read." Tilting toward "must read" after Dex's reversal. |
| [[instruction-budget]] | Coding Agents | LLMs follow ~150-200 instructions reliably. Monolithic prompts fail; split into <40-instruction focused stages. |
| [[context-engineering]] | Coding Agents | Managing context window contents for quality. "Smart Zone" / "Dumb Zone" at 40%. Mental Alignment via static artifacts. Two reads: more info vs. better instructions. |
| [[agent-memory]] | Coding Agents | Mechanisms for cross-session knowledge retention. Next frontier after commoditized capabilities (Cleric, Pinterest). |
| [[agent-harness]] | Coding Agents | The complete non-model infrastructure wrapping an LLM. 12 components, Von Neumann analogy, thin vs. thick spectrum, scaffolding metaphor. |
| [[agentic-coding-stack-layers]] | Coding Agents | Five-layer composition model from [[agentic-coding-stack-aslan|Aslan 2026]]: Delivery Methodology / Agent Discipline / Technical Context / Token Optimization / Product Surface. Workflow-oriented complement to [[agent-harness]]. Names spec-to-code traceability as the unbuilt missing link. |
| [[shift-work]] | Software Factories | Separation of [[software-factory|software factory]] into interactive (spec refinement) and non-interactive (autonomous execution) phases. Central unsolved question: when is a specification "complete enough"? Three agent sets prevent gaming. |
| [[holdout-scenarios]] | Software Factories | End-to-end user stories kept separate from implementation codebase to prevent agents from reward-hacking tests. Borrowed from ML holdout validation sets. Stories span happy path, edge cases, failure modes. Validation probabilistic, not boolean. |
| [[nlspec]] | Spec-Driven | Natural-language specification — markdown precise enough for agents to implement against, yet human-readable. Answers three questions: what, under what conditions, why it matters. Rigor bottleneck: hard to write with machine-executable precision. |
| [[digital-twin-universe]] | Software Factories | Behavioral clones of all external dependencies (APIs, services). Enables deterministic, high-volume validation at factory scale without hitting rate limits or incurring costs. Can itself be built by agents from API docs. StrongDM's most ambitious infrastructure. |

### Concepts To Create

- **Human-in-the-loop** — patterns for human oversight in AI pipelines
- **Agentic development** — building software via autonomous AI agents
- **Technical deflation** — falling cost of software production and its implications
- **Adversarial review** — using AI to validate AI-generated specs/code
- **Agentic search** — LLM-driven code exploration using grep/find/cat vs. vector search (Braintrust data)
- **Enterprise agent governance** — centralized management of multiple coding tools (Databricks gateway)
- **Spec-to-code traceability** — the unbuilt connective tissue named in [[agentic-coding-stack-aslan]]; queryable bridge between requirements and code symbols / tests / PRs

## Entities

| Page | Type | Summary |
|------|------|---------|
| [[humanlayer]] | Company | Full-stack AI coding agent company: 12-factor principles → CodeLayer IDE → Agent Control Plane infrastructure. |
| [[bmad-method]] | Framework | Multi-agent Agile team simulation with 6 named personas, three planning tracks (Quick Flow/BMad/Enterprise), adversarial review, fresh-chat requirement. Runs on Claude Code/Cursor/Windsurf. 19.1k stars. |
| [[codespeak]] | Tool/Platform | Spec-driven dev platform: markdown specs (`.cs.md`) → full app generation via Claude. CLI + GitHub App + modular takeover via web wizard (Apr 2026). Brownfield conversions: faker (9.9×), yt-dlp, beautifulsoup4, markitdown, folio (~7×). Active alpha with weekly releases. Strictest SDD in the wiki — you never write code. |
| [[github-copilot]] | Tool | AI coding assistant (GitHub/OpenAI). Most widely adopted AI dev tool. IDE autocomplete, code generation, test writing. Case study in [[ai-in-sdlc-research]]. Level 1-2 in Shapiro's framework. |
| [[kiro]] | Tool/IDE | AWS agentic development environment. Converts prompts into structured specs and production-ready workflows. SDD framework alongside Spec Kit and BMAD. |
| [[spec-kit]] | Framework | GitHub's open-source SDD toolkit. `specify → plan → tasks → implement` pipeline. Used in practitioner observation alongside BMAD with positive results. |
| [[claude-agent-sdk]] | Framework/SDK | Anthropic's agent harness powering Claude Code. "Dumb loop, smart model" philosophy. Fork/Teammate/Worktree subagent models. Thin harness, trust the model. |
| [[openai-agents-sdk]] | Framework/SDK | OpenAI's code-first agent framework. Runner class, 3 guardrail levels, agents-as-tools + handoffs. Codex extends with 3-layer architecture. |
| [[langgraph]] | Framework | LangChain's graph-based agent framework. Explicit state graphs, typed dicts + checkpoints, nested graph multi-agent. Thick harness, graph-based control. |
| [[crewai]] | Framework | Role-based multi-agent framework. Agent-Task-Crew model, Flows layer for deterministic backbone. Medium-thick harness. |
| [[autogen]] | Framework | Microsoft's conversation-driven orchestration. 3-layer architecture, 5 orchestration patterns including magentic. Evolving into Microsoft Agent Framework. |
| [[superpowers]] | Framework | Jesse Vincent's open-source skills framework (github.com/obra/superpowers). 7-stage workflow (brainstorm → worktree → plan → execute → TDD → review → complete), composable skills, mandatory RED-GREEN-REFACTOR. Installable across Claude Code, Cursor, Codex, Copilot CLI, Gemini CLI. **Layer 2 (Agent Discipline)** in [[agentic-coding-stack-layers]]. |
| [[ctxo]] | Tool/MCP Server | Semantic codebase analysis via MCP. Six primitives: `get_blast_radius`, `get_logic_slice`, `get_why_context`, `get_symbol_importance`, `find_dead_code`, `get_pr_impact`. Strongest TS/JS support. **Layer 3 (Technical Context)** — *"the scarcest capability in the current ecosystem"* (Aslan). |
| [[rtk]] | Tool/CLI Proxy | Rust shell-output proxy with command-specific filters. Intercepts before output reaches the agent. **Layer 4 (Token Optimization)** alongside [[context-mode]]. *"The fastest way to improve a noisy shell-based workflow without redesigning how the agent works"* (Aslan). |
| [[context-mode]] | Tool/MCP Server | MCP sandbox where the agent writes code to compute the answer; only `console.log()` enters context. SQLite + FTS5 for cross-session continuity. **Layer 4 (Token Optimization)** — pairs with [[rtk|RTK]] for at-scale workflows. |
| [[gsd-2]] | Tool/Platform | Autonomous coding-agent platform: `gsd auto → plan → execute → verify → commit → repeat`. Worktree isolation, state recovery, multi-provider, cost tracking, milestone execution. **Layer 5 (Product Surface)** — sole inhabitant. Sibling to [[humanlayer-codelayer|CodeLayer]] and [[agent-control-plane|ACP]]. |
| [[strongdm]] | Company | Security infrastructure company with the first public implementation of [[software-factory|software factory]] pattern in production (Feb 2026). Three-person team built access management software: no human writes code, no human reviews code. Pioneered [[shift-work]], [[holdout-scenarios]], [[attractor]], [[digital-twin-universe]], satisfaction metric, three agent sets. Reference implementation for factory pattern. **No large enterprise has implemented at scale yet.** |
| [[attractor]] | Pattern/Framework | Non-interactive coding agent structured as a directed graph of phases (DOT format). Each node is a dev task, edges are LLM-evaluable conditions. Orchestrates implementation/test/refine/converge cycles. [[strongdm]]'s orchestration engine. Implementations: StrongDM (ref), Kilroy (Go), and the open [[attractor]] NLSpec. |

### Entities To Create

- **Devin** — Cognition's autonomous coding agent
- ~~**Spec-kit** — Spec-driven development framework~~ ✅ entity page created
- ~~**Kiro** — AWS spec-driven development tool~~ ✅ entity page created
- ~~**GitHub Copilot** — AI coding assistant~~ ✅ entity page created
- **Dan Shapiro** — Five levels framework author
- ~~**Jesse Vincent** — Superpowers series author~~ ✅ entity page created ([[superpowers]])
- **Dex (dexhorthy)** — 12-factor agents / HumanLayer creator

## Analyses

_No analysis pages yet. Analyses are created from substantial query answers._
