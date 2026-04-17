---
title: gsd-2
type: entity
pillar: [coding-agents, software-factories]
created: 2026-04-16
updated: 2026-04-16
sources: [agentic-coding-stack-aslan]
tags: [tool, platform, autonomous-agent, product-surface, worktree-isolation, state-recovery, multi-provider, l5]
---

# gsd-2

## Overview

**gsd-2** is a full **autonomous coding agent platform** — an integrated product surface around long-running agentic work, distinct from the harness-component tools at lower layers of the stack.

Per [[agentic-coding-stack-aslan]], gsd-2 occupies **Layer 5 (Product Surface)** of the agentic coding stack — the layer where *"planning, execution, state, cost, and recovery are exposed as an operating system for AI work."* The pipeline:

```
gsd auto → plan → execute → verify → commit → repeat
```

**Source:** [[agentic-coding-stack-aslan]] (Murat Aslan, Apr 2026) — first appearance in the wiki.

**Status in the wiki:** Single source. Repository, license, and authorship not yet verified independently. Name suggests "Get Stuff Done v2" or successor to a prior `gsd` tool, but this is unconfirmed.

## Layer in the Aslan Stack

- **Layer:** L5 — Product Surface
- **Question it answers:** *Where does the developer operate the whole system?*
- **Failure modes reduced:** Multi-session conflicts, review bottlenecks
- **Aslan's "my take":** *"gsd-2 is not just 'another tool' in the same category as the others. It is the closest thing in this set to a full product shell for the stack."*

## Key Capabilities

Per [[agentic-coding-stack-aslan]], gsd-2 provides an integrated operational environment with:

- **Worktree isolation** — parallel agent work in isolated git worktrees, avoiding merge conflicts
- **State recovery** — resume long-running tasks across sessions and crashes
- **Multi-provider support** — works across model providers (Anthropic, OpenAI, etc.)
- **Cost tracking** — measure and budget the financial cost of agent work
- **Milestone execution** — orchestrate work toward named milestones rather than single tasks
- **Auto loop** — `gsd auto` runs `plan → execute → verify → commit → repeat` autonomously

This is structurally similar to several other wiki entities, with key differences (see Comparison below).

## When to Use (per Aslan)

> *"You want an actual operational shell for agentic development across larger scopes, longer task horizons, and more autonomous execution."*

Best fit: large-scope work, long task horizons, teams operating multiple autonomous agents in parallel.

Not a fit: solo developers doing tactical edits — Aslan: *"For a solo developer doing tactical edits, it can be too much machinery."*

## Trade-offs

- **Complexity.** Bigger mental and operational commitment than adding one narrow capability.
- **All-or-nothing adoption.** Unlike L1-L4 tools that drop into existing workflows, gsd-2 wants to *be* the workflow.

## Relevance to the Wiki

1. **Concretizes the L5 "Product Surface" category** that [[humanlayer-codelayer|CodeLayer]] and [[agent-control-plane|ACP]] also occupy. Gives the wiki a third reference point for "integrated operational environment for AI coding work."

2. **Operationalizes the [[long-running-claude|Anthropic long-running Claude]] patterns** at the product layer. Where Anthropic's research showed CLAUDE.md, CHANGELOG.md, test oracles, git as coordination, and Ralph Loop as *patterns*, gsd-2 packages those concerns as *product features*.

3. **Counterpoint to [[everything-is-a-ralph-loop|Huntley's]] "300 lines of loop code" minimalism.** Huntley argues a coding agent is essentially a small loop. Aslan and gsd-2 argue that as task horizons lengthen and parallelism increases, the *operational shell around the loop* becomes the product. Both can be true — Ralph for the inner loop, gsd-2 (or similar) for the outer operating environment.

4. **Concrete L5 example for the [[software-factory]] concept.** Where Shapiro's Level 4-5 framing is directional (*"the dark factory"*), gsd-2 gives a concrete glimpse of what the L5 operating surface might look like in practice.

## Comparison with Similar Product Surfaces

| Tool | Position | Key differentiator |
|------|----------|--------------------|
| **gsd-2** | L5 product surface | Worktree isolation, state recovery, cost tracking, multi-provider, milestone execution |
| [[humanlayer-codelayer]] | "Google Docs/Notion/Figma-like SDLC" (per [[humans-in-the-loop-dex-interview]]) | Collaboration surface; rebuilt around CRISPY workflows |
| [[agent-control-plane]] | Kubernetes-native orchestration | Async-first, MCP support, agent-to-agent delegation |
| [[everything-is-a-ralph-loop\|The Weaving Loom]] | "Evolutionary software factory" | Self-healing loops, revenue optimization, manifesto-style |

Note: this comparison is the wiki's interpretation. Aslan does not directly compare gsd-2 to CodeLayer, ACP, or the Loom.

## Recommended Combinations

Per [[agentic-coding-stack-aslan]], gsd-2 appears in only one recommended stack:

- **Team workflow, larger repos:** [[bmad-method|BMAD-METHOD]] + [[superpowers]] + [[ctxo|Ctxo]] + gsd-2

Aslan's accompanying note: *"Skip this if your team is still proving whether agentic coding is valuable at all. This stack is for operationalization, not experimentation."*

## Open Questions

1. **What does "gsd" stand for?** "Get Stuff Done" is the obvious guess but unconfirmed. The "-2" suggests a v2 successor to an earlier tool.
2. **What's the repository / who's the author?** Not stated in [[agentic-coding-stack-aslan]].
3. **How does gsd-2 relate to existing platforms** (CodeLayer, ACP)? Direct competitor, complement, or different niche?
4. **What does multi-provider support look like in practice?** Provider-abstraction layer? Per-task provider selection? Cost-routing?
5. **Is the worktree isolation per-task, per-agent, or per-milestone?** This determines what kind of parallelism is supported.
6. **What does cost tracking measure** — token spend, wall-clock, success-weighted? And does it drive scheduling decisions or just reporting?
7. **Is state recovery deterministic or best-effort?** Long-running autonomous work needs the former for trustworthy resumption.

## Links

- [[agentic-coding-stack-aslan]] — primary (and currently only) source
- [[humanlayer-codelayer]] — sibling L5 product surface
- [[agent-control-plane]] — sibling L5 orchestration platform
- [[everything-is-a-ralph-loop]] — counterpoint maximalism at the loop layer
- [[long-running-claude]] — patterns gsd-2 packages as product features
- [[software-factory]] — concrete instance of L5 factory infrastructure
- [[automation-levels]] — gsd-2 targets Level 4+ workflows
