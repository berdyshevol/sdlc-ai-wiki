---
title: "Coding Agents Conference 2026 — Multi-Speaker Slides"
type: source
pillar: industry
created: 2026-04-08
updated: 2026-04-27
sources: [extracted_text.txt, breitenother-kilo-25t-tokens.md, wang-brain-trust-evals.md]
tags: [conference, industry, adoption, evals, benchmarks, security, memory, enterprise, trust]
---

# Coding Agents Conference 2026 — Multi-Speaker Slides

## Metadata

- **Event:** Coding Agents: AI-Driven Dev Conference
- **Date:** March 3, 2026
- **Location:** Computer History Museum, Mountain View
- **Organizer:** MLOps Community
- **Event page:** https://luma.com/codingagents
- **YouTube playlist (all talks):** https://www.youtube.com/playlist?list=PL3vkEKxWd-uuMAa8LDmcFEh7iMyKDJlyW
- **Raw files:**
  - Slides: `raw/slides/extracted_text.txt` (all speakers)
  - Brightenother talk transcript: `raw/youtube-transcripts/breitenother-kilo-25t-tokens.md` (full talk + Q&A)
  - Wang talk transcript: `raw/youtube-transcripts/wang-brain-trust-evals.md` (full talk + Q&A)
- **Speakers:** Sid Bidasaria (Anthropic), Scott Breitenother (Kilo Code), Jessica Wang (Braintrust), Niels Bantilan (Union AI), Faye Zhang (Pinterest), Yanis He (Scale AI), Erin Ahmed (Cleric), Milan Williams (Semgrep), Ash Lewis (Fastino), Ankit Mathur (Databricks), Zach Lloyd (Warp), Mihail Eric (Monaco), Dexter Horthy (HumanLayer), Harrison Chase (LangChain), Sam Partee (Arcade)

## Summary

A full-day conference capturing the state of AI coding agents in early 2026. The slides reveal an industry rapidly maturing past "vibe coding" into production-grade concerns: **trust, governance, memory, evaluation, and security**. Multiple speakers independently converge on the same themes: developers are climbing an adoption ladder, agent quality matters more than speed, and the infrastructure for enterprise-scale agent deployment is the next frontier.

The most data-rich talk is Scott Breitenother's (Kilo Code), drawing on **25 trillion tokens processed across 1.5M+ developers** to map how AI adoption actually happens. The most forward-looking is Yanis He's (Scale AI), introducing SWE Atlas as a benchmark that goes beyond issue resolution to measure codebase understanding, test writing, and refactoring.

## Key Claims by Speaker

### Scott Breitenother — Kilo Code (25T Tokens)

> **Talk title:** "Lessons from 25 Trillion Tokens — Scaling AI-Assisted Development at Kilo"
> **YouTube:** https://www.youtube.com/watch?v=tG1CSRaJhKQ
> **Full transcript + Q&A:** `raw/youtube-transcripts/breitenother-kilo-25t-tokens.md`

**Headline data and framework**
- **AI adoption is a trust ladder:** Autocomplete → Chat → Single Agents → Orchestration. Each rung requires more trust. *"You have to climb and you have to earn it."*
- **Three breakpoints in adoption:** Context construction, model routing, and feedback loops consistently cause adoption to stall.
- **Trust is measurable but signal degrades up the ladder:** Autocomplete (sub-200ms, clean signal — accept-or-reject) → Chat (seconds, noisier — copy/ignore) → Agents (minutes, sparse — diff accept/revert) → Orchestration (hours, delayed — workflow outcome).
- **Quantitative trust threshold:** *"When our latency peaked at 200 ms, usage went down."* Speed is itself a trust signal — slow autocomplete causes users to disable the feature, and they may never re-engage.
- **"Build for trust, not capability."** *"Benchmarks tell you what models can do. 25 trillion tokens tell you what developers actually do."*

**Developer role transformation**
- **Code monkey → orchestrator → conductor of an orchestra.** Developer becomes "the tastemaker, the architect," deciding quality gates while agents handle execution, boilerplate, syntax-error hunting, documentation lookup, and writing.
- **Cognitive ratio inverts.** Old: ~20 % thinking, ~80 % coding. New: **~80 % thinking, ~20 % coding.** *"It's quite taxing... someone joins the kilo engineering team [and] they kind of have to like warm up their muscle to the brain."*
- **Each dev manages 3–5 specialized agents** out-of-the-box (Architect, Code, Ask, Debug, Orchestrator) plus custom modes (e.g., engineer-named "Brian mode").
- **No single best model.** Slides reference Minimax M2.5 / Claude Opus 4.6 / GPT 5.3 Codex; in the talk Brightenother names the cost-effective tier as *"Kimi or MiniMax or GLM"* and warns that defaulting to the most expensive frontier model means *"you're essentially heating your home with inference."*

**Adoption snapshot (data)**
- **49 % of pro devs don't use AI daily.** 76 % won't use AI for deployment/monitoring. 16 % don't plan to use AI at all. (Source: Stack Overflow)
- **Typical team evolution:** March 2025: 1 feature every 2–3 weeks → March 2026: 1–2 features/week. *Same team size.* Kilo had ~15 engineers at the time of the talk.

**Kilo's organizational model (newly surfaced from the talk's narrative)**
- **One feature, one engineer.** Not "one team owns a feature" — *"There's only one engineer per feature."* Single owner runs conception → coding → deployment → end-user feedback → iteration. Cited example: an engineer "Sesh" owns code reviews end-to-end.
- **Anti-collaboration as a stated value.** *"We try to avoid collaboration at all costs. We are very anti-collaboration."* Citing PostHog's blog on collaboration's downsides; engineers talk only when collaboration *adds value*. Frames most habitual collaboration as a *"safety blanket."*
- **No PMs (almost).** *"We don't really believe in PMs at Kilo... every engineer is their own PM."* The entire company has one PM, scoped to the *horizontal* platform layer beneath the engineer-owned vertical features.
- **Vacation policy is honest:** when a single owner is out, *"that product might not move for a week. And we're cool with it because the gains we have when that person is on are so much more."* On-call rotation handles production issues.
- **Production Slackbot:** *"I don't go into Kilo anymore. I just say `kilo extend this promotion one more week`"* — production ops and content edits routed through the agent in Slack, not the IDE.

**Synthesis quotes from the talk**
- *"Coding is the easy part and the bottleneck is no longer the coding, it's kind of all the process."*
- *"You give AI the steering wheel but you also have a secret steering wheel and a secret brake"* — Brightenother's metaphor for single-agent (Level 3-equivalent) work.
- *"AI's got the wheel, you better pray"* — for orchestration (Level 4-equivalent).
- *"You've got to give trust to get trust."* The trust loop also requires the user to feed the agent more context as they ascend the ladder — autocomplete needs only the current file; orchestration needs the entire repo graph.

**Note on framework cross-reference**
- Brightenother does **not** cite Shapiro or the five-level model in the talk or slides. The 4-rung Kilo ladder is his own framing. The mapping to Shapiro's L1–L4 is the wiki's own synthesis (see [[automation-levels]]) — Brightenother's data should be treated as an independent observational signal that *coheres with* Shapiro's progression, not a direct empirical test of it.

### Jessica Wang — Brain Trust ("Stop Shipping on Vibes")

> **Talk title:** "Stop Shipping on Vibes — How to Build Real Evals for Coding Agents?"
> **YouTube:** https://www.youtube.com/watch?v=VbX24V_JFQI
> **Full transcript + Q&A:** `raw/youtube-transcripts/wang-brain-trust-evals.md`

**Headline framing**
- **"Shipping on vibes" is the failure mode.** Wang reports being on calls where teams shipped AI features because *"the engineering team told them it was ready"* or *"a PM tried a couple of prompts and they said it looked good."* The eval-driven alternative is to be able to say *"we ran 200 different test cases and 94 % of them passed and so therefore we're shipping it"* — or to articulate trade-offs like *"we shipped this change and it improved the tone but decreased accuracy by 5 %."*
- **Real-world cautionary tale:** OpenAI's April 2025 sycophancy rollback (the entire GPT-4o update reverted because making the model more helpful made it too agreeable to be useful). *"This is an example of when it's very easy to overtrain models. You want to be able to catch these nuances early on."*

**The evals framework (four components)**
- **Dataset → Task → Scoring → Experiment → Compare.**
- **Dataset:** golden cases + edge cases + failure modes.
- **Task:** the prompt + model picked to handle each input.
- **Scoring:** deterministic, LLM-as-a-judge, or human-in-review — but *"you who are writing the scorer is defining the criteria of what comprises good and bad."*
- **Experiment:** one run of one configuration. Multiple experiments make regressions and improvements visible at the row level.

**The production loop** — *live logs → sample 10–20 % → dataset → tweak prompt/score/data → ship → repeat*. Brain Trust's **Loop** feature lets engineers query experiments in natural language (*"highlight problems"*, *"which experiment performed best"*) — Wang reports she was skeptical at first but uses it heavily because long agentic traces are hard to read manually.

**"Evals are a team sport"** — AI engineer (data + bug/feature changes), product manager (hypotheses + success criteria; *"if you work at Kilo Code it might just be the same as engineer"* — live tease of [Brightenother's earlier talk](#scott-breitenother--kilo-code-25t-tokens)), subject-matter experts (label data; especially in medicine / law / insurance), data analysts (define and analyze scores).

**Case study: agentic vs vector search (the eval that produced the headline numbers)**
- **Origin:** prompt from CEO Ankur Goyal pointing at a Cursor blog post claiming semantic (= agentic) search significantly improved their coding agent. Wang independently evaluated.
- **Vector search defined:** text/code → embeddings → vector DB (Pinecone) → return nearest-neighbour chunks.
- **Agentic search defined:** LLM-driven CLI exploration via grep/find/ls/cat — *"more like how a real human would act."* (Note Wang uses *"semantic"* and *"agentic"* interchangeably; this differs from the more common usage where *semantic search* = embedding-based.)
- **Two datasets:**
  - **TypeScript-Go (custom):** merged "fix" PRs from Microsoft's TypeScript-Go repo, parent commit checked out, Claude-synthesized bug ticket as the input. Pass criterion: Go test suite passes after the agent's fix.
  - **SWE-Bench Verified subset:** 25 rows from the Django-related slice of the industry-standard benchmark.
- **Implementation gotcha 1:** Claude Code defaults to agentic search and *"really wanted to fall back."* Wang used `--disallow-tools` to block grep/find/ls and added explicit prompt instructions to force vector-search-only behavior. Tuning this took several days.
- **Implementation gotcha 2:** Claude Code runs as a subprocess — traces were orphaned from the parent. Fix: pass parent span IDs as environment variables so subprocess traces attach to the correct trace tree.
- **Scoring nuance:** SWE-Bench provides a `fail-to-pass` test list (tests failing on the buggy commit, expected to pass after the canonical fix). Wang's scorer accepts a fix if it greens all `fail-to-pass` tests, *even if it incidentally regresses unrelated tests* — a deliberate eval-design choice.

**Results**
- **SWE-Bench Verified (25 Django rows):** vector search **60 %**, agentic search **68 %**.
- **TypeScript-Go (10 rows):** vector and agentic both **70 %** — but vector used substantially more tokens and cost (slide-deck records ~3.1× more tokens / ~2.8× more cost; Wang explicitly disclaims the absolute dollar figures as miscalibrated and asks the audience to read the *ratio*, not the dollar amount).
- **Three takeaways:**
  1. *"Vector search returns chunks, not connective tissue."* Vector retrieved 26 chunks across one SWE-Bench run without ever isolating the bug — proximity to relevant code without import chains, type definitions, or call graphs.
  2. *Agentic search enables chain-of-thought exploration.* The agent reads a function, sees what calls it, follows references across files.
  3. *More searches = more cost.* Vector's "guess and check" loop is expensive precisely because the chunks lack the signal needed to terminate it.

**Honest caveats Wang names herself**
- *"I would not publish a blog post about this yet."* The eval reads as *"agentic is 100 % better than vector,"* which she does not believe.
- Need multiple trials per task — LLM non-determinism alone can swing scores 10–15 %.
- Vector implementation was deliberately basic; chunk overlap, text splitting, and retrieval-model improvements were not attempted.
- Hybrid (vector + agentic) is what most companies actually run.
- Dataset is too small — 10 rows means a single failure swings the score 10 %.

**Q&A highlights**
- **Token-cost confound from `--disallow-tools`** (audience): could the cost gap be inflated because Claude tries agentic, fails, retries via vector? Wang acknowledges yes, this is on her to-fix list.
- **Human control group:** SWE-Bench provides golden answers (human-coded). For the TypeScript-Go set, she could compare against the actual merged PR diff via LLM-as-a-judge.
- **Evals for short-attention-span / non-linear conversations** (audience: chat product where users hop topic-to-topic with no golden answer): Wang's answer — *"turn your actual user journey into just something in your data set."* Log the real journeys, sample them into evals, optionally synthesize additional rows.

**Cross-source notes**
- Wang's *"connective tissue"* framing for what vector search lacks **independently echoes Murat Aslan's** later use of the same phrase for spec-to-code traceability ([[agentic-coding-stack-aslan]]: *"the most strategic connective tissue in the agentic coding stack"*). The two uses are scoped differently (Wang: code-to-code traversal; Aslan: spec-to-code linkage) but the shared metaphor is striking — the wiki's [[code-legibility-debate]] and Aslan-stack discussion may benefit from this earlier pre-citation.
- **Brain Trust commercial datapoint** (from slides, not the talk transcript): Brain Trust reached $10M ARR with 100 % quarterly NDR.

### Faye Zhang — Pinterest (Production Sub-Agents)
- **Before Claude Code: 4-6 week cycle. After: 1 week cycle** — via concurrent sub-agent processes.
- **Four reasons agents fail:** (1) Spec drift across multi-step chains, (2) Data distribution imbalance, (3) Memory collapse, (4) Tool misuse.
- **Fix 1 — Agent SDK orchestration:** Structured skills.md, Tool Calling 2.0.
- **Fix 2 — Customized agent memory:** Procedural memory in CLAUDE.md, episodic memory in `.claude/memories/episodes/*.json`. Hook after Bash/tests to append failure→fix entries. MCP `memory_search(query)` tool for retrieval.
- **Long-horizon development memory:** Treat memory as a learned policy problem — Memory Manager (PPO) + Answer Agent (GRPO). 3-tier infra: hot memory, domain task, cold storage via MCP.
- **Open weights option:** MiniMax-M2.5 at $0.27/M input tokens.

### Yanis He — Scale AI (Beyond SWE-Bench Pro)
- **SWE-Bench Pro** became industry standard via minimal contamination (copyleft licenses, acquired proprietary codebases), human-augmented tasks, enterprise difficulty.
- **"Coding is more than issue resolution."** `assert coding == resolving_github_issues` → `AssertionError`.
- **SWE Atlas** — new benchmark assessing how agents understand, validate, and improve software systems. Three dimensions: Codebase QA (leading models ~30%), Test Writing, Refactoring.
- **Codebase QA breakdown:** Architecture & system design (35%), root-cause analysis (30%), code onboarding (23%), security (9%), API integration (3%).
- **Vision:** "If we give agents enough freedom to explore the environment, coding may become the new scaffolding" — agents self-developing their own tools.
- **SWE-ficiency** — upcoming benchmark for efficiency measurement.

### Erin Ahmed — Cleric (Agent Memory & Learning)
- **"Agent capabilities are commoditized. The next horizon of differentiation is learning."**
- **Lesson 1:** Make it easy for users to teach via correction. "Agents that activate fastest aren't the ones that fail least — they're the ones that make it easy to correct."
- **Lesson 2:** Reward corrections with better performance. Corrections must persist, compound, and be visible.
- **Lesson 3:** Absorb context continuously — route work automatically, absorb every source of environment-specific context.
- **Agents that earn their place** accumulate knowledge about environment, past outcomes, and team preferences.

### Mihail Eric — Monaco (RePPIT Framework)
- **RePPIT:** Research → Propose → Plan → Implement → Test. Very similar to Dex's CRISPY evolution.
- **"Vibe coding confuses expectations."** Writing production AI code requires being methodical.
- **Outcomes:** 2-4x productivity gains, applicable to both greenfield and brownfield codebases.
- **Stanford's first AI software engineering course** creator.

### Milan Williams — Semgrep (Security)
- **Three security tips for AI-generated code:** (1) Minimally scoped permissions ("If you wouldn't give it to an intern, why'd you give it to your agent?"), (2) Set up logging before you need it, (3) Scan code before it ships.
- **Agent credential risk:** Agents inherit your credentials and access. Hard to tell why something goes wrong.
- **"The goal isn't to slow down the agent. It's to make sure you're still in control when it moves fast."**

### Ankit Mathur — Databricks (Coding Agent Gateway)
- **Enterprise problem:** Multiple vendor contracts, multiple admin consoles, no centralized visibility, fragmented billing, hard to enforce security.
- **"Using just one coding tool is extremely limiting."** Developers use 4+ tools for different tasks.
- **Coding Agent Gateway:** Single governance hub for many coding tools. Provides observability, cost controls, privacy guarantees.
- **Databricks internal stats:** 2200+ engineers, 10+ offices, 25K+ monthly commits, 15K+ monthly deployments, 25M+ lines of code.
- **MCP authentication:** UC Managed Connections replace plain-text locally stored tokens with encrypted, auto-rotated credentials.
- **Bottlenecks are shifting** to code reviews, scaling CI, and testing.

### Harrison Chase (LangChain) + Sam Partee (Arcade) — General Purpose Agents
- **Coding agent → General purpose agent:** Limited to IDE → Acts across any service.
- **Two components:** Agent harness (LangChain: loop, planning, sub-agents, skills) + Tool runtime (Arcade: OAuth, MCP gateway, RBAC, execution).
- **Agent security fails two ways:** (1) Agent gets its own identity (can't scope permissions per user), (2) Agent uses service accounts (no accountability).
- **Delegated agent authorization:** User's token, scoped per action, injected not in context. Token never exposed to agent or LLM.
- **MCP Gateway** = exact group of tools across services with governance.

## Connections

- **[[code-legibility-debate]]** — Scott's "AI shifts work, doesn't remove it" and Dex's "read the code" converge: reading and quality assurance don't go away, they transform.
- **[[automation-levels]]** — Scott's trust ladder (Autocomplete → Chat → Agents → Orchestration) maps closely to Shapiro's five levels but with empirical data from 25T tokens.
- **[[context-engineering]]** — Multiple speakers emphasize context as key: Faye's agent memory architecture, Scott's context construction as adoption breakpoint.
- **[[instruction-budget]]** — Dex's talk (companion source) directly addresses this; Databricks' note about "too many MCPs" confirms the problem from a different angle.
- **[[12-factor-agents]]** — CRISPY evolution presented at this conference. Harrison Chase's agent harness echoes many 12-factor principles.
- **[[humanlayer]]** — Dex's closing keynote presented CRISPY here.
- **[[agent-memory]]** — Both Faye and Erin dedicate their talks to agent memory/learning. Converge on: memory is the next frontier after capabilities.
- **[[spec-driven-development]]** — Mihail Eric's RePPIT and Dex's CRISPY both formalize the research→plan→implement pattern.

## Questions Raised

1. Does the trust ladder (Kilo Code) suggest a predictable adoption timeline, or do teams plateau at certain rungs?
2. If agentic search outperforms vector search at lower cost, why is RAG still dominant?
3. How do you implement Faye's 3-tier memory system (hot/domain/cold) in practice?
4. Will SWE Atlas replace SWE-Bench Pro, or do they measure different things?
5. Is the Coding Agent Gateway pattern (Databricks) the beginning of "agent middleware" as a category?
6. How does delegated authorization (Arcade) interact with enterprise SSO/compliance requirements?
