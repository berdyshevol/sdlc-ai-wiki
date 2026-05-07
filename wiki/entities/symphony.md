---
title: "Symphony"
type: entity
pillar: software-factories
created: 2026-05-07
updated: 2026-05-07
sources: [lopopolo-openai-extreme-harness-engineering]
tags: [orchestration, openai, elixir, beam, ghost-library, ralph-loop, six-layers, rework-state, symphony]
---

# Symphony

## Overview

**Symphony** is an Elixir-based orchestration system built by [[lopopolo-openai-extreme-harness-engineering|Ryan Lopopolo's team at OpenAI Frontier]] to remove humans from the in-the-moment loop of an autonomous-agent SDLC. It distributes itself as a **"ghost library"** — a sufficiently detailed spec that any coding agent can reassemble the system locally rather than depending on a binary library or shared service.

- **Creator:** OpenAI Frontier team (Ryan Lopopolo et al.)
- **Language:** Elixir (chosen by the model, not the humans, for BEAM process supervision and gen-servers)
- **Distribution:** spec ("ghost library"), reassembled per-org by Codex
- **Status:** Internal at OpenAI as of May 2026; spec published

## Relevance

Symphony is the **most explicit articulation of an "agent-orchestration substrate beneath the harness"** in the wiki. Where an [[agent-harness]] orchestrates a single agent's loop, Symphony orchestrates *many* per-task daemons — each driven by Codex on a Ralph loop — and pushes humans to a latency-insensitive review boundary (*"I open Linear twice a day, say yes/no"*). It is the operational substrate behind the 5–10 PRs/engineer/day result reported in [[lopopolo-openai-extreme-harness-engineering|Lopopolo's article]].

## The Six Layers

Symphony specifies six orthogonal layers — plus an implicit "zero layer" of self-modification:

| Layer | Concern | Example primitives |
|-------|---------|--------------------|
| **Policy** | Institutional knowledge — what must be true for work to be done | "CI must pass," release-branch gates, scoping rules |
| **Configuration** | Per-deployment options; ID formats, ticket-source binding | Linear vs. Jira swap, Slack vs. Teams |
| **Coordination** | The trickiest layer; spec → Elixir process supervision mapping | gen-servers per task, supervision trees, resumability |
| **Execution** | The Ralph loop driving each per-task daemon | Spawn Codex, write code, push PR, wait, fix flakes, merge |
| **Integration** | Tool surface — heavily anti-MCP, pro-CLI | `gh` CLI, GitHub Actions, vibed shim CLIs (e.g. local Playwright daemon) |
| **Observability** | What the agent (and the human) can see | Local VictoriaMetrics + Vector + Mise; Grafana JSON authored by Codex |
| *Zero layer* | Self-modification | Agents cut their own tickets, modify their own skills, distill from session logs |

## Key Concepts

### Ghost Libraries (distribution model)

A **ghost library** is a spec detailed enough for a coding agent to *reassemble* the system locally, rather than vendoring a binary or depending on a hosted service. *"Becomes much cheaper to share software with the world."* Symphony is the wiki's first named instance.

Implication: at sufficient model capability, library distribution can collapse into spec distribution. Each consumer's agent reassembles the library natively into the consumer's stack, language, and constraints — no transitive-dep compatibility checks, no upstream-patch-and-wait. Closely related to [[lopopolo-openai-extreme-harness-engineering|Lopopolo's]] in-housing-of-dependencies thesis and Bret Taylor's "software dependencies are going away" claim.

### Spec-Generation via Ralph Loop

Symphony's spec was *itself* built by Ralph-looping Codex:

1. Spawn disconnected Codex in tmux to implement the current spec.
2. Spawn another Codex in another tmux to review the implementation against the upstream proprietary repo.
3. Update the spec so the implementation diverges less.
4. Loop until fidelity converges.

This is [[everything-is-a-ralph-loop|Ralph]] applied to *spec authoring*, not just implementation — a meta extension of the pattern.

### Rework State

When a human marks a PR as **not mergeable**, Symphony's Elixir service **trashes the entire worktree and PR** and starts again from scratch. Rebuilding cheaply replaces incremental fixup at agent throughput. The why-was-it-trash signal becomes context for the next attempt — a built-in feedback channel that turns rejection into prompt material.

### Latency-Insensitive Human Review

The human review boundary is async. Lopopolo: *"I open Linear twice a day."* Once humans become latency-insensitive about agent output, the system can scale parallelism arbitrarily — the human is no longer the cycle-time bottleneck.

## Why Elixir / BEAM

The model picked Elixir because BEAM's **process supervision** and **gen-servers** map naturally onto the workload: spinning up a per-task daemon, supervising its Ralph loop, restarting on failure, surviving partial crashes.

Lopopolo doesn't write Elixir himself. He explicitly cites this as freedom that comes from removing humans from the in-the-moment loop: *"my own personal ability to write or not write Elixir doesn't have to bias us away from using the right tool for the job."*

## Connections

- **[[lopopolo-openai-extreme-harness-engineering]]** — The defining source. Symphony is described as the substrate that turns the [[agent-harness]] into a many-agent orchestration system.
- **[[openai-codex]]** — Symphony drives Codex sessions; each per-task daemon spawns a disconnected Codex instance.
- **[[everything-is-a-ralph-loop]]** — Each Symphony task is a Ralph loop; the Symphony *spec itself* was built by Ralph-looping Codex against an upstream reference. Symphony is Ralph at meta-level.
- **[[parsons-ralph-loops-workshop]]** — Parsons' "implement the next most important ticket" workshop is the manual version of what Symphony automates. The rework-cheaply mindset is shared.
- **[[matt-pocock-dex-horthy-chat]]** — Dex's cron-Ralph and pipeline-Ralph patterns are convergent with Symphony's per-task daemons; Symphony is the BEAM-flavored, process-supervised expression.
- **[[agent-harness]]** — Symphony sits *above* the harness: each agent has its own harness (Codex), Symphony orchestrates the population of harnesses.
- **[[skill-issue-harness-engineering]]** — Kyle's six harness levers are inside-the-harness; Symphony's six layers are outside-the-harness, at the orchestration tier.
- **[[agentic-coding-stack-aslan]]** — Symphony occupies Aslan's L5 (Product Surface) for orchestration. Sister to [[gsd-2|GSD-2]] (also L5) and [[humanlayer-codelayer|CodeLayer]] / [[agent-control-plane|ACP]].
- **[[agent-control-plane]]** — HumanLayer's Kubernetes-native orchestration. Architecturally similar to Symphony at the "many long-lived agents" level; different runtime substrate (K8s vs. BEAM), different distribution model (open-source vs. ghost library).
- **[[software-factory]]** — Symphony is the orchestration tier of OpenAI's internal factory; pairs with [[strongdm]]'s [[attractor]] and [[holdout-scenarios]] as a peer factory orchestration primitive.
- **[[shift-work]]** — Lopopolo's "twice-daily Linear check" is shift-work in miniature; Symphony makes this tractable by making rework cheap.

## Open Questions

- **Is Symphony open-sourceable?** The "ghost library" framing implies *anyone* can reassemble it; the deep coupling to OpenAI internal practices and Codex versions implies otherwise. TBD.
- **Multi-human + multi-agent.** Lopopolo openly notes Symphony is currently "single-human, multi-agent"; the team's 45-minute daily standup exists because each engineer loses track of state. Symphony's multi-team primitive doesn't yet exist.
- **The agentic-code-owner failure mode.** Symphony arbitrates between author-Codex and reviewer-Codex via prompt-side optionality (P0/P1/P2). What happens when both are mis-prompted simultaneously and converge on a wrong answer?
- **Cross-language portability.** Symphony chose Elixir for BEAM. Can the spec compile to other supervision substrates (Erlang directly, Rust + Tokio, Go) without losing the rework-state semantics?

## Links

- [[lopopolo-openai-extreme-harness-engineering]] — defining source
- The Symphony spec (published by Lopopolo's team — see source page for current pointer)
