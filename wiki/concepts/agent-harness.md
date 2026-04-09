---
title: "Agent Harness"
type: concept
pillar: coding-agents
created: 2026-04-09
updated: 2026-04-09
sources: [anatomy-agent-harness, 12-factor-agents, coding-agents-conf-2026, everything-is-a-ralph-loop]
tags: [agent-harness, orchestration, infrastructure, architecture]
---

# Agent Harness

## Definition

The **agent harness** is the complete software infrastructure wrapping an LLM that transforms it from a stateless text generator into a capable, goal-directed agent. It encompasses the orchestration loop, tools, memory, context management, state persistence, error handling, guardrails, verification loops, and subagent orchestration.

The term was formalized in early 2026, though the concept predates the name. Anthropic's Claude Code documentation describes the SDK as "the agent harness that powers Claude Code." OpenAI's Codex team uses the same framing.

**Canonical formula** (Vivek Trivedy, LangChain): *"If you're not the model, you're the harness."*

**Key distinction**: The "agent" is the emergent behavior (goal-directed, tool-using, self-correcting). The harness is the machinery producing that behavior. When someone says "I built an agent," they mean they built a harness and pointed it at a model.

## The Von Neumann Analogy

Beren Millidge (2023, "Scaffolded LLMs as Natural Language Computers") formalized the analogy:

| Computer | LLM Agent |
|----------|-----------|
| CPU | LLM (model weights) |
| RAM | Context Window |
| Hard Disk | Vector DB / Long-term Storage |
| Device Drivers | Tool Integrations |
| **Operating System** | **Agent Harness** |
| Application | Agent (emergent behavior) |

*"A raw LLM is a CPU with no operating system. The harness is the OS that makes it useful."*

## Three Levels of Engineering

Three concentric levels of engineering surround the model:

1. **Prompt engineering** — crafting the instructions the model receives
2. **[[context-engineering]]** — managing what the model sees and when
3. **Harness engineering** — encompasses both, plus the entire application infrastructure (tool orchestration, state persistence, error recovery, verification loops, safety enforcement, lifecycle management)

The harness is not a wrapper around a prompt. It is the complete system that makes autonomous agent behavior possible.

## Key Sources

- **[[anatomy-agent-harness]]** — Primary source. Comprehensive synthesis across 5 frameworks, identifies 12 components and 7 architectural decisions.
- **[[12-factor-agents]]** — Principles for production agents; shares the "own your infrastructure" ethos but focuses on design principles rather than components.
- **[[coding-agents-conf-2026]]** — Multiple speakers discuss harness-adjacent topics (verification, memory, tool scoping).

## Current Understanding

### The 12 Components

A production agent harness has twelve distinct components (synthesized across Anthropic, OpenAI, LangChain, and the practitioner community):

1. **Orchestration Loop** — The ReAct/TAO cycle. Mechanically a while loop; complexity lives in what it manages.
2. **Tools** — Schema-defined capabilities injected into context. Registration, validation, sandboxed execution, result formatting.
3. **[[agent-memory|Memory]]** — Multi-timescale: short-term (conversation) and long-term (CLAUDE.md, JSON Stores, SQLite/Redis).
4. **[[context-engineering|Context Management]]** — Strategies to combat context rot: compaction, observation masking, JIT retrieval, sub-agent delegation.
5. **Prompt Construction** — Hierarchical assembly: system prompt + tools + memory + history + user message.
6. **Output Parsing** — Native tool calling (structured objects) vs. legacy free-text parsing.
7. **State Management** — Checkpointing, persistence, resume. Approaches: git commits, typed dicts, sessions.
8. **Error Handling** — Error compounding (99% per-step × 10 = ~90.4% e2e). Four error types (LangGraph).
9. **Guardrails & Safety** — Input/output/tool guardrails, tripwires, permission enforcement separated from reasoning.
10. **Verification Loops** — Rules-based, visual, LLM-as-judge. "Verification improves quality 2-3x" (Boris Cherny).
11. **Subagent Orchestration** — Fork/Teammate/Worktree (Anthropic), agents-as-tools + handoffs (OpenAI), nested graphs (LangGraph).
12. **Lifecycle/Termination** — Exit conditions: no tool calls, max turns, token budget, guardrail tripwire, user interrupt.

### The Agent Loop

The core runtime cycle:

1. **Prompt Assembly** — construct full input (system prompt + tool schemas + memory + history + user message)
2. **LLM Inference** — model generates output tokens
3. **Output Classification** — tool calls? → execute. No tool calls? → final answer. Handoff? → switch agent.
4. **Tool Execution** — validate arguments, check permissions, sandbox, execute, capture results
5. **Result Packaging** — format as LLM-readable messages; errors returned as error results for self-correction
6. **Context Update** — append to history; trigger compaction if near limit
7. **Loop** — return to step 1

### Seven Architectural Decisions

Every harness architect faces these choices:

| Decision | Options | Key Insight |
|----------|---------|-------------|
| 1. Agent Count | Single vs. Multi-agent | Maximize single first; split at ~10 overlapping tools |
| 2. Reasoning Strategy | ReAct vs. Plan-and-Execute | Plan-and-execute 3.6x faster (LLMCompiler) but less adaptive |
| 3. Context Strategy | Aggressive compaction vs. Rich context | ACON: 26-54% token reduction preserving 95%+ accuracy |
| 4. Verification | Computational vs. Inferential | Guides (feedforward) vs. sensors (feedback) — Thoughtworks |
| 5. Permissions | Permissive vs. Restrictive | Fast/risky vs. safe/slow; depends on deployment context |
| 6. Tool Scoping | Full toolkit vs. Minimal per step | Less is more; Vercel cut 80% of tools, got better results |
| 7. Harness Thickness | Thin vs. Thick | Trust model vs. encode in code; trend is toward thinner |

### Harness Thickness Spectrum

A core architectural bet about how much to trust the model vs. encode in code:

- **Thin** (Claude Agent SDK, OpenAI Agents SDK) — Give model tools + context + permissions; model makes all decisions. Bets on model improvement.
- **Thick** (CrewAI Flows, LangGraph) — Harness encodes routing, planning steps, multi-step strategies. Bets on explicit control.

As models improve, the bar shifts toward thinner harnesses. Anthropic regularly deletes planning steps from Claude Code's harness as new model versions internalize that capability.

### The Scaffolding Metaphor

The harness is like construction scaffolding: temporary infrastructure enabling workers to reach upper floors. It doesn't do the construction, but without it, workers can't reach the work.

Key insight: **scaffolding is removed when the building is complete.** As models improve, harness complexity decreases. Manus was rebuilt 5 times in 6 months, each rewrite removing complexity.

But: **co-evolution creates coupling.** Models are post-trained with specific harnesses. Changing tool implementations degrades performance because of this tight coupling.

**Future-proofing test**: Does performance scale with better models without adding harness complexity?

### Evidence: Harness > Model

- **TerminalBench 2.0**: LangChain changed only harness infrastructure (same model) → jumped from outside top 30 to rank 5
- **Automated optimization**: 76.4% pass rate via LLM-optimized infrastructure, surpassing hand-designed systems
- Two products with identical models can have wildly different performance based solely on harness design

## Framework Implementations

| Dimension | [[claude-agent-sdk]] | [[openai-agents-sdk]] | [[langgraph]] | [[crewai]] | [[autogen]] |
|-----------|---------------------|----------------------|---------------|------------|-------------|
| Loop | Dumb loop, smart model | Runner class | State graph | Sequential/Hierarchical | Conversation-driven |
| State | Git commits | 4 strategies | Typed dicts + checkpoints | Task results | Message history |
| Multi-Agent | Fork/Teammate/Worktree | Agents-as-tools + Handoffs | Nested graphs | Agent-Task-Crew | 5 orchestration patterns |
| Philosophy | Thin harness, trust model | Code-first | Graph-based control | Role-based collaboration | Conversation as protocol |

## Open Questions

1. **Is harness thickness converging?** Will the trend toward thinner harnesses continue, or will new capabilities require new harness complexity?
2. **Co-evolution trap**: If models are post-trained with specific harnesses, how do you upgrade the harness without retraining?
3. **Standardization**: Will harness architecture converge on a standard (like POSIX for operating systems), or remain fragmented?
4. **Measurement**: How do you benchmark harness quality independently of model quality?
5. **What's the right level of tool scoping?** Vercel's 80% cut is dramatic — is there a principled way to determine the optimal tool set per step?

## Related Concepts

- [[context-engineering]] — a subset of harness engineering; managing what the model sees
- [[agent-memory]] — the persistence layer of the harness
- [[instruction-budget]] — the constraint that drives tool scoping and context management decisions
- [[12-factor-agents]] — design principles that inform harness architecture
- [[everything-is-a-ralph-loop]] — Geoffrey Huntley's Ralph pattern: a monolithic orchestrator loop as harness philosophy. Emphasizes simplicity ("300 lines"), loop-based control, and the engineer as loop programmer
