---
title: "Extreme Harness Engineering: 1M LOC, 1B toks/day, 0% human code or review — Ryan Lopopolo (OpenAI)"
type: source
pillar: software-factories
created: 2026-05-07
updated: 2026-05-07
sources: [lopopolo-openai-extreme-harness-engineering.md]
tags: [openai, codex, harness-engineering, software-factory, symphony, ghost-libraries, post-merge-review, electron-app, ralph-loop, in-housing-dependencies, frontier, computer-use, code-legibility, school-1, billion-tokens, 1m-loc, practitioner]
---

# Extreme Harness Engineering: 1M LOC, 1B toks/day, 0% human code or review — Ryan Lopopolo (OpenAI)

**Author:** Ryan Lopopolo — engineer on OpenAI Frontier (frontier product exploration / new product development). Background: Snowflake, Stripe, Citadel.
**Venue:** Latent Space podcast (Ryan's first podcast appearance), recorded at OpenAI's Bellevue office grand opening.
**URL:** https://www.youtube.com/watch?v=CeOXx-XTYek
**Pillar:** [[software-factory]] / [[agent-harness]] / [[code-legibility-debate]]
**Date:** May 2026

## Summary

A practitioner interview with the engineer behind OpenAI's "harness engineering" article — a five-month internal-tool build at OpenAI Frontier where a three-person team produced **~1 million lines of code across ~1,500 PRs, with zero human-authored code and post-merge review only**. Lopopolo's self-imposed founding constraint was *"I can't write a single line of code"* — chosen so that the product (an Electron-based AI agent control plane) would be built the way Frontier's enterprise customers will eventually build software: by directing Codex agents end-to-end. The first month-and-a-half was 10× slower than writing it by hand; the team paid that cost to build the "assembly station" — once the scaffolding for the agent existed, throughput climbed to 5–10 PRs per engineer per day, and humans became the bottleneck rather than the agent.

The talk's core thesis is that **the agent harness, not the model, is where the product gets built**. Lopopolo formalizes harness engineering as a discipline above [[context-engineering|context engineering]] and prompt engineering: *"the whole meta of the thing is to basically tease out of the heads of all the engineers on my team what they think good looks like… and put all the non-functional requirements of building high-scale, high-quality reliable software into a space that prompt-injects the agent."* Concretely, this means: writing instructions in `AGENTS.md` and short skill files (their codebase has six skills total), encoding "what good looks like" as lints with prompt-targeted error messages, building a `core-beliefs.md` that captures team/product/customer context, slurping Codex session logs into blob storage and running daily agent loops over them to extract team-wide improvements, and treating PR comments and failed builds as signals that the agent was missing context which now needs to be encoded back into the repo. **All non-functional requirements become text the harness injects.**

The build system is treated as a hard ratchet: under-one-minute builds are an invariant, enforced by the agent's impatience itself. When 5.3 introduced background shells the agent stopped tolerating long blocking commands, so the team retooled from a bespoke makefile to Bazel to Turbo to NX in a single week — *"this is not a thing I would expect to be able to do in a codebase where people have opinions, but because the only goal was to make the agent productive… we just kind of left it there because builds were fast."* The repo is decomposed into ~500 npm packages — architecture-to-the-max for what would normally be a 7-person team — because each engineer is effectively 10–50× and the decomposition prevents agents from trampling on each other. **Code review has been pushed past the merge boundary**: the PR-author Codex and the PR-reviewer Codex negotiate within prompts (P0/P1/P2 framework, reviewer biases toward merging anything below P2, author can push back or defer scope-creep feedback to the backlog), the merge is autonomous, and most human review is post-merge sampling to detect what process knowledge is still missing.

The second half of the conversation introduces **Symphony**, a six-layer Elixir-based orchestration spec that Lopopolo's team distributes as a "ghost library" — a complete blueprint that a coding agent can reassemble locally. The team built it by pointing Codex at their proprietary repo and Ralph-looping: spawn-disconnected-Codex-to-implement-spec → spawn-another-Codex-to-review-implementation-vs-upstream → update-spec-so-it-diverges-less → loop until fidelity converges. The model picked Elixir because BEAM process supervision and gen-servers map naturally to spawning per-task daemons; Lopopolo doesn't write Elixir himself, and explicitly cites this as freedom to use the right tool when no humans are in the loop. Symphony's six layers (policy / configuration / coordination / execution / integration / observability) plus a meta "zero layer" of self-modification (agents that cut their own tickets, modify their own skills, run agent loops over session logs) cover the orchestration substrate beneath the harness. The team also introduces a **rework state**: if a human escalates a PR as "not mergeable," Symphony trashes the entire worktree and PR and starts again from scratch — the agent-driven version of "throw it away and redo" rather than incremental fixup.

The conversation closes on three forward-looking themes: (1) **In-housing dependencies as the new norm** — Bret Taylor's "software dependencies are going away" thesis, validated; the team treats low-to-medium-complexity deps as in-housable in an afternoon (most of the code isn't needed; Codex Security can review the internalized version). (2) **Operational stance on tooling** — anti-MCP (forced token injection, breaks autocompaction), pro-CLI (token-efficient, easy to filter — "patch `--silent` to Prettier so the agent doesn't read formatting confirmations"), `gh` CLI as exemplar; tools should be CLI-shaped because models love text. (3) **The on-policy harness bet** — Lopopolo argues the harness should be *native to* what Codex already produces (code, tests, lints) rather than an off-policy ROS-style scaffold around it; this avoids degrading agent performance and stays aligned with how the model continues to advance. He calls out OpenAI Frontier as the eventual platform that will package this approach for enterprises, with safety specs (GPT-OSS SafeGuard) plugged in per-customer.

## Key Claims

### The constraint and the result

- **Self-imposed founding constraint: "I can't write a single line of code."** Chosen so the product would be built the way enterprise customers must build software with Frontier — through Codex agents end-to-end.
- **Team of ~3 engineers, 5 months, ~1M LOC across ~1,500 PRs, 0% human-authored code, post-merge review only.** "10× faster than I would have if I had done it by hand."
- **First 1.5 months were 10× slower than hand-coding.** The cost was paid to build the "assembly station" — scaffolding so the agent could do the whole job. Once paid, throughput jumped to **5–10 PRs/engineer/day** by January 2026 (post-5.2).
- **The product is a native Electron application** with cloud-hosted backend; main + renderer process MVC decomposition treated with the same rigor as a 10,000-engineer architecture.
- **Repository structured as ~500 npm packages.** Architecture-to-the-max for a 7-person team, but rational when each person is effectively 10–50× via agents — decomposition prevents agents from trampling each other.

### Harness engineering as a discipline

- **The agent harness is the product, not the model.** Aligns with [[anatomy-agent-harness]] thesis.
- **Three concentric layers**: prompt engineering ⊂ context engineering ⊂ harness engineering. Harness encompasses all the non-model infrastructure including non-functional requirements expressed as text the model can read.
- **"Every non-functional requirement becomes text the harness injects."** Docs, lint error messages, skill files, PR-review prompts, build-failure signals — all pathways for putting "what good looks like" in front of the agent.
- **Six skills total in the entire codebase.** *"If some part of the SDLC isn't covered, our first attempt is to encode it in one of the existing skills."*
- **`AGENTS.md` is short** (~100 lines, table of contents); detail lives in skill files (`core-beliefs.md`, `tech-tracker.md`, quality-score skill). Lopopolo notes they "reinvented Agent Skills from first principles" before Skills existed.
- **Models fundamentally crave text.** *"My job is to figure out ways to funnel text from one agent to the other."*

### The build-time ratchet

- **Sub-1-minute builds are an invariant**, enforced because the agent itself becomes impatient and won't block on slow commands.
- **5.3's "background shells" capability rewrote build economics.** Previously the agent would block on long scripts; with 5.3 it stops blocking, so any build over ~1 minute is a signal to decompose the build graph.
- **Migrated from makefile → Bazel → Turbo → NX in one week** — "not a thing I'd expect in a codebase where people have opinions; we just kept moving until builds were fast."
- **Tokens are cheap; insanely-parallel agents can constantly garden these invariants.** This compresses the "envelope of acceptable build times" that platform teams classically allow to drift.

### Code review past the merge boundary

- **Code review is autonomous and post-merge.** *"We've moved beyond even the humans reviewing the code… most of the human review is post-merge."*
- **PR-author Codex ↔ PR-reviewer Codex negotiation pattern.** Both agents have prompts that allow push-back: reviewer biased toward merging anything below P2, author allowed to defer scope-creep feedback to backlog. Without this optionality, *"the code-author Codex was willing to be bullied by the reviewer"* and convergence failed.
- **P0/P1/P2 priority framework** given to reviewer agent without exact definitions, just framework — model fills in the threshold.
- **The `dollar-land` skill** coaches Codex through the entire merge dance: push PR → wait for human + agent reviewers → wait for CI green → fix flakes → merge upstream on conflicts → wait for green → merge queue → flake-fix until in main. *"Significant tax on humans to do this; agent does it without me."*
- **Worktrees, not branch-on-branch.** Models are great at resolving merge conflicts, so worktree-induced conflicts don't matter at this throughput. (Cf. [[zakariasson-cursor-software-factory]] where Cursor moved away from worktrees toward isolated VMs — different scaling tradeoff.)

### Observability as agent feedback

- **Local observability stack (VictoriaMetrics + Vector + Mise) was half-an-afternoon of work.** Not for humans to watch — for the agent to read.
- *"In this local observability stack — sure, you can deploy Jaeger to visualize the traces, but I wouldn't expect to be looking at the traces in the first place because I'm not going to write the code to fix them."* The agent is the primary observer.
- **Codex authors Grafana dashboard JSON and responds to its own pages.** When paged for a missing timeout, the agent fixes the bug *and* updates reliability documentation to require timeouts on all network calls — "durably encoded process knowledge."
- **Daily-cron agent loops over Codex session logs from the entire team** (slurped to blob storage) → extracts team-wide improvements → reflects them back into the repo. *"Everybody benefits from everybody else's behavior for free."*
- **PR comments + failed builds = signals that the agent was missing context.** Each one becomes a trigger for codifying that context back into the repo.

### Symphony — the orchestration substrate

- **Symphony is an Elixir-based orchestration system** distributed as a "ghost library" spec that a coding agent can reassemble locally.
- **Six layers**: **policy** (institutional knowledge — e.g., "CI must pass," handed to `gh` CLI), **configuration**, **coordination** (the trickiest layer; spec-to-Elixir mapping for process supervision), **execution**, **integration** (anti-MCP; CLI-shaped tools), **observability**. Plus a meta **"zero layer"** of self-modification — agents that cut their own tickets, modify their own skills, propose follow-up work as markdown notes a cron-Codex burns down.
- **Why Elixir**: the model chose it; BEAM process supervision and gen-servers map naturally to spawning per-task daemons. *"My own personal ability to write or not write Elixir doesn't have to bias us away from using the right tool for the job."*
- **The Symphony spec was built Ralph-style**: spawn-Codex-to-implement-spec → spawn-Codex-to-review-implementation-vs-upstream → update-spec-so-it-diverges-less → loop until fidelity converges. Direct application of [[everything-is-a-ralph-loop|Ralph Loop]] to spec generation itself.
- **"Ghost libraries" as a distribution model** — a sufficiently detailed spec that any coding agent can reassemble the system. *"Becomes much cheaper to share software with the world."*
- **Rework state**: when a human marks a PR not-mergeable, Symphony **trashes the entire worktree and PR** and starts from scratch. Throw-away-and-redo is cheaper than incremental fixup at agent throughput. The why-was-it-trash signal becomes new context for the next attempt.
- **Removed humans from the in-the-moment loop**: *"I open Linear twice a day and say yes/no."* Latency-insensitive review unlocks far more parallelism.

### In-housing dependencies and the end of plugins

- **Validates Bret Taylor's claim that software dependencies are going away.** Low-to-medium-complexity deps are in-housable in an afternoon.
- **Most dependency code isn't needed** — in-housing strips generic surface area down to only what's used.
- **Codex Security can review internalized deps deeply** in ways that pushing patches upstream cannot — much lower friction than the patches → release → transitive-dep compatibility loop.
- **Acknowledged limits**: large-scale deps (Linux, MySQL, Datadog, Temporal) and security testing's "many eyes" benefit still favor not in-housing.
- **"The end of plugins"** — Postel's-law overhead disappears when you write only the surface you need.

### CLI > MCP, and tool-shape for agents

- **Anti-MCP**: forces token injection into every context (harness can't filter), messes with autocompaction, the agent can forget how to use the tool. Pays cost for capability you may use only 3 of N times.
- **Pro-CLI**: token-efficient, can be filtered/wrapped per agent's needs.
- **`gh` CLI is the exemplar.** *"My only interaction with the GitHub web UI at this point is `gh pr view --web`, glance at the diff, send it."*
- **Patch `--silent` onto Prettier** so the agent doesn't read "every file already formatted" confirmations — it just wants to know if it should run the write command.
- **Wrap noisy CLIs to surface only failures.** Build-output mountain → script that extracts the actual exception, like the sticky note developer-productivity teams write for humans.
- **Vibed shim CLIs as a first-class pattern**: someone on the team wrote a local Playwright-driving daemon + tiny CLI to replace the Playwright MCP — Lopopolo had no idea this had happened, since to him "I just run Codex and it can drive the UI."

### Frontier and the enterprise platform

- **OpenAI Frontier** is the enterprise platform for deploying agents safely at scale — IAM integration, security tooling, workspace tools, observability, the ability to revoke authorization if a model becomes misaligned.
- **Buyer is two-tiered**: employees who use the agents (surfaces, connectors), and IT/GRC/AI-innovation/security stakeholders who govern deployment. The dashboard is the iceberg beneath the surface.
- **Internal data agent** uses Frontier tech to expose the data ontology to the agent — semantic-layer-as-context. Foundation for agents that go beyond coding into business analysis.
- **GPT-OSS SafeGuard model** ships the ability to interface with a per-enterprise safety spec — exfiltration patterns, internal code names, regulatory constraints.

### What models still can't do

- **Net-new product idea → playable prototype, single-shot.** This is where Lopopolo spends most of his manual steering. The whitespace problem.
- **Gnarliest refactorings.** Improving with each release, but still where he interrupts most and builds custom tooling.
- **Spark (5.3-Spark)** is impressive for prototyping/documentation/lint-ESLint work but blew through three compactions before writing a line of code on the high-reasoning tasks Lopopolo was used to with x-high.
- **5.4 with 1M-token context + computer use** is the big jump: longer agentic runs before compaction, agent can "see the UI" rasterized to validate UI changes.

### Philosophical stance — on-policy harness

- **Build harness native to the model's existing output (code, tests, lints), not a separate ROS-style scaffold around it.** *"None of the things we have built actively degrade agent performance, because really all they're doing is running tests."*
- **Don't bet against the model.** Each model release pushes capability outward; harness should be robust to that, not a fence around current limits.
- **On-policy ↔ off-policy analogy with RL.** The harness is *on-policy* with the model's own behavior; off-policy harnesses are prone to being scrapped at the next model version.

## Connections

- **[[agent-harness]]** — Lopopolo's article is the strongest single articulation of harness-engineering-as-a-discipline. The wiki's existing concept page already says *"Anthropic's Claude Code documentation describes the SDK as 'the agent harness'… OpenAI's Codex team uses the same framing"* — this source is the OpenAI-side definitive statement. Adds the on-policy/off-policy distinction and the *"every non-functional requirement is text"* operationalization.
- **[[anatomy-agent-harness]]** — Direct sister piece. Pachaar synthesizes 12 components and 5 frameworks at the architecture-survey level; Lopopolo is the case study showing what those components look like in production at 1M-LOC scale. Same philosophy: harness > model.
- **[[skill-issue-harness-engineering]]** — Kyle's six harness levers (CLAUDE.md, MCP, skills, sub-agents, hooks, back-pressure) overlap heavily with Symphony's six layers and Lopopolo's "encode what good looks like in skills." Both share the **reactive-configuration** philosophy: *encode signals from past mistakes, don't pre-emptively scaffold*. Kyle's "Linear MCP → CLI" case study is empirically validated by Lopopolo's anti-MCP / pro-`gh` stance and the vibed Playwright-shim story.
- **[[zakariasson-cursor-software-factory]]** — The closest peer talk. Both are May 2026 IDE/AI vendor practitioner accounts of running internal software factories. Convergences: post-merge review (Cursor's agentic code owner ≈ Lopopolo's reviewer-Codex), continual-learning (Cursor's plugin ≈ Lopopolo's session-log slurping), thousands of agents/day. Divergences: Cursor uses **isolated VMs** (rejected worktrees), Lopopolo uses **worktrees** at heavy scale (models resolve conflicts). Cursor's "rules should emerge dynamically" is the same stance as Lopopolo's "encode signals from past mistakes."
- **[[software-factory]]** — Adds OpenAI Frontier as the **fourth large-scale software-factory data point** alongside [[strongdm]], [[cursor]], and Anthropic ([[long-running-claude]]). Important distinction: this is a **production product** (the Codex/Frontier control plane shipping to OpenAI's enterprise customers), not a side experiment. Lopopolo also positions himself "between L4 and L5 with sub-parts at L5" via Frontier's internal usage.
- **[[strongdm]] / [[software-factory-practitioners-guide-woolley]]** — StrongDM is the prior wiki gold-standard L5 case (3-person team, no humans write or review code, security infrastructure). Lopopolo's team is the same shape but inside OpenAI itself with much higher LOC throughput. Different patterns: StrongDM uses [[shift-work]] / [[holdout-scenarios]] / [[attractor]] / [[digital-twin-universe]]; Lopopolo uses skills + lint-as-prompt + session-log-extraction + Symphony's six layers. **Both converge on post-merge review only.**
- **[[code-legibility-debate]]** — **Strongest production-grade School-1 statement in the wiki**, beating even [[codespeak-vibe-takeover|CodeSpeak]] in commitment depth. Lopopolo doesn't say "I don't read code" as a future ideal — he says they have *removed* the read-the-code step from the merge path on a 1M-LOC production codebase shipping to enterprise customers. Direct counter-evidence to [[dex-rpi-to-crispy|Dex's reversal]]. Both are 2026 production data points; they disagree fundamentally. Worth tracking which holds up over time.
- **[[everything-is-a-ralph-loop]]** — Symphony's spec-generation Ralph loop (Codex-implements ↔ Codex-reviews ↔ update-spec) is a clean Ralph application *to spec authoring itself*. Extends Huntley's pattern to a meta-level: don't just Ralph-loop implementations, Ralph-loop the spec.
- **[[parsons-ralph-loops-workshop]]** — Parsons' "implement the next most important ticket" Ralph pattern is what Symphony automates at scale. Both share the *throw-away-rework-cheaply* mindset; Lopopolo's rework state is the explicit Symphony primitive for it.
- **[[long-running-claude]]** — Anthropic's "patterns for multi-day Claude" is the scientific-computing version of what Lopopolo runs in production. Same pattern: living plans, change logs, agent-driven verification, opportunity-cost framing of unused agent hours. Lopopolo is the extreme of this applied to enterprise product engineering.
- **[[automation-levels]]** — Strong evidence for **L4–L5 viability in 2026 within a small, AI-pilled team building a greenfield product**. Lopopolo himself doesn't cite Shapiro, but the dynamics map cleanly. The "doesn't apply to all production code" caveat is honest — green-field, native app, no continuous deployment, human still cuts release branches.
- **[[instruction-budget]]** — Lopopolo's *"six skills total"* and short `AGENTS.md` is the operational answer to the instruction-budget constraint. Skills as named, model-callable units rather than sprawling prompts.
- **[[context-engineering]]** — The session-log extraction + lint-as-prompt + observability-for-the-agent pattern is context engineering at the team-knowledge level: every signal becomes injected text. *"Models fundamentally crave text"* is Lopopolo's compressed framing.
- **[[agent-memory]]** — Daily-cron agent loops over the entire team's Codex session logs is a concrete agent-memory implementation. Stored corrections become future context for everyone.
- **[[shift-work]]** — Lopopolo's "I open Linear twice a day" is a small-team manifestation of the StrongDM shift-work pattern. Async review boundary; humans batch their attention.
- **[[holdout-scenarios]]** — Different verification mechanism (CI + agent code review + post-merge sampling) but same goal (preventing reward-hacking). No formal holdout set in this account.
- **[[agentic-coding-stack-aslan]]** — Aslan's five layers (Methodology / Discipline / Technical Context / Token Optimization / Product Surface) map onto Lopopolo's stack roughly: harness eng spans Discipline + Technical Context + Token Optimization; Symphony is the Product Surface for orchestration. Lopopolo's anti-MCP + CLI-shim story is direct evidence for Aslan's L4 (Token Optimization) being a real layer.
- **[[claude-agent-sdk]] / [[openai-agents-sdk]]** — Codex CLI and Codex App are the OpenAI-side practitioner expressions; Frontier + Agents SDK is the OpenAI-side enterprise distribution. The "thin harness, smart model" trajectory continues here.
- **[[cole-medin-ai-dark-factory]]** — Same factory frame at the individual-developer scale. Lopopolo is the enterprise/team scale.
- **[[matt-pocock-dex-horthy-chat]]** — Dex's "cron-Ralph" pattern is the same shape as Lopopolo's daily-cron session-log loops. Convergent emergence.

## Questions Raised

- **Does post-merge review hold up at L5 scale over multi-year time horizons?** Lopopolo's project is 5 months old; Dex's reversal happened at the 6-month mark. Worth tracking through 2027.
- **Is "ghost library" distribution a real category, or a one-off?** Symphony being agent-reproducible from a spec is a clean idea; will others ship like this? What does the licensing model look like? Does it dilute the value of having proprietary code at all?
- **What breaks first when you scale to multi-human + multi-agent?** Lopopolo openly says *"this is good for single-human multi-agent"*; the 45-minute daily standup exists because each human has lost track of state. **What's the multi-human-team primitive that Symphony doesn't yet provide?**
- **How does the on-policy harness bet hold across model-version upgrades?** Lopopolo claims their harness is robust because it's just code+tests+lints native to Codex's output. Is that true across major releases (5.4 → 6.x)? What survives, what breaks?
- **Anti-MCP — is this a Lopopolo-specific stance or a frontier convention?** Cursor is also building toward in-product tools rather than MCP-everywhere. [[skill-issue-harness-engineering|Kyle]] also flags MCP as token-expensive. Is MCP being quietly displaced for serious agentic work?
- **In-housing dependencies — at what complexity ceiling does it stop being viable?** Lopopolo says "low-medium right now"; "thousand-line dep in an afternoon." Where does the ceiling move with 5.4 / 6.x? At what point do Postgres/Redis-tier deps become in-housable too (likely never, but worth bounding).
- **The agentic-code-owner failure mode.** Lopopolo describes the bullyable code-author and notes that prompt-side optionality fixed it. But: **what happens when the code-author and reviewer are mis-prompted simultaneously and converge on a wrong answer?** No public account of this failure yet.
- **Is Symphony open-sourceable, or is it inseparable from Frontier?** The "ghost library" framing implies discoverable; the deep coupling to OpenAI internal tooling implies not. TBD whether external orgs can run Symphony directly or whether it has to be reimplemented per organization.
- **The AGENTS.md ↔ Skills convergence.** Lopopolo says they reinvented Skills before Skills existed. Skills are now first-class in Codex and (separately) Anthropic Claude Code. Does AGENTS.md remain the entry point, or does the skill registry become the harness's primary manifest?
- **Single-team-size limits.** This worked at ~3 people. What's the n where the harness's "encode what good looks like" pipeline starts breaking — where individual engineers' tastes diverge and the lint/skill set becomes contested? Cursor's Q&A flagged the same problem at organizational scale; no resolution yet.

## Raw files

- `raw/youtube-transcripts/lopopolo-openai-extreme-harness-engineering.md` — full transcript with metadata header and YouTube URL.
