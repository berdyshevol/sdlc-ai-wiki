---
title: "The Anatomy of an Agent Harness"
type: source
pillar: coding-agents
created: 2026-04-09
updated: 2026-04-09
author: Akshay Pachaar (@akshay_pachaar)
url: https://x.com/akshay_pachaar/status/2041146899319971922
sources: [anatomy-agent-harness]
tags: [agent-harness, orchestration, tools, memory, context-management, framework-comparison]
---

# The Anatomy of an Agent Harness

## Metadata

- **Author:** Akshay Pachaar (@akshay_pachaar)
- **Date:** April 2026
- **URL:** https://x.com/akshay_pachaar/status/2041146899319971922
- **Format:** Long-form X thread with illustrated diagrams
- **Pillar:** [[coding-agents]]
- **Raw file:** `raw/anatomy-agent-harness.md`

## Summary

A comprehensive synthesis of agent harness architecture across Anthropic, OpenAI, LangChain, CrewAI, and AutoGen. The article formalizes the concept of the **agent harness** — the complete non-model infrastructure (orchestration loop, tools, memory, context management, state, error handling, guardrails) that transforms a stateless LLM into a capable agent.

The central argument: **the harness is the product, not the model.** LangChain demonstrated this empirically by jumping from outside the top 30 to rank 5 on TerminalBench 2.0 by changing only their harness infrastructure (same model, same weights). A separate research project achieved 76.4% pass rate by having an LLM optimize the infrastructure itself.

The article introduces the **Von Neumann analogy** (from Beren Millidge, 2023): a raw LLM is a CPU with no OS. Context window = RAM, vector DB = disk, tool integrations = device drivers, harness = operating system. It identifies **12 components** of a production harness, **7 architectural decisions** every harness builder faces, and provides a detailed comparison of how 5 major frameworks implement the same core pattern with different philosophies.

A key meta-insight is the **scaffolding metaphor**: the harness is temporary infrastructure that enables the LLM to do work it couldn't do alone. As models improve, harness complexity should decrease — but models are now post-trained with specific harnesses, creating tight coupling (changing tools can degrade performance).

## Key Claims

### The Harness Matters More Than the Model
- LangChain: same model, harness-only changes → outside top 30 to rank 5 on TerminalBench 2.0
- Separate research: 76.4% pass rate via LLM-optimized infrastructure, surpassing hand-designed systems
- Two products with identical models can have wildly different performance based solely on harness design

### The Von Neumann Analogy
- Raw LLM = CPU (no RAM, no disk, no I/O)
- Context window = RAM (fast but limited)
- Vector DB / external storage = Hard disk (large but slow)
- Tool integrations = Device drivers
- Agent harness = Operating system
- Agent = Application (emergent behavior)
- From Beren Millidge (2023): "We have reinvented the Von Neumann architecture"

### Three Levels of Engineering
- **Prompt engineering** — crafting instructions
- **[[context-engineering]]** — managing what the model sees and when
- **Harness engineering** — encompasses both, plus all application infrastructure

### 12 Components of a Production Harness
1. **Orchestration Loop** — the ReAct/TAO cycle; mechanically simple ("dumb loop"), complexity lives in what it manages
2. **Tools** — schemas injected into context; registration, validation, sandboxed execution, result formatting
3. **Memory** — multi-timescale (short-term: conversation; long-term: CLAUDE.md, JSON Stores, SQLite/Redis); Claude Code uses 3-tier hierarchy
4. **[[context-engineering|Context Management]]** — context rot degrades performance 30%+ at mid-window positions ("Lost in the Middle"); strategies: compaction, observation masking, JIT retrieval, sub-agent delegation
5. **Prompt Construction** — hierarchical assembly (system prompt + tools + memory + history + user message)
6. **Output Parsing** — native tool calling (structured tool_calls objects) vs. legacy free-text parsing
7. **State Management** — LangGraph: typed dicts + checkpoints; OpenAI: 4 strategies; Claude Code: git commits as checkpoints
8. **Error Handling** — errors compound fast (99% per-step × 10 steps = ~90.4% e2e); LangGraph: 4 error types; Stripe: cap retries at 2
9. **Guardrails & Safety** — OpenAI: input/output/tool guardrails + tripwires; Anthropic: separates permission from reasoning, ~40 discrete capabilities
10. **Verification Loops** — rules-based (tests, linters), visual (Playwright screenshots), LLM-as-judge; "verification improves quality 2-3x" (Boris Cherny)
11. **Subagent Orchestration** — Claude Code: Fork/Teammate/Worktree; OpenAI: agents-as-tools + handoffs; LangGraph: nested state graphs
12. *(Implied: Lifecycle/Termination management)*

### The 7-Step Agent Loop
1. Prompt Assembly → 2. LLM Inference → 3. Output Classification → 4. Tool Execution (validate, sandbox, execute) → 5. Result Packaging → 6. Context Update (compaction if near limit) → 7. Loop back
- Exit conditions: no tool calls, max turns, token budget exhausted, guardrail tripwire, user interrupt, safety refusal

### The "Ralph Loop" for Long-Running Tasks
- **Initializer Agent**: sets up environment (init script, progress file, feature list, initial git commit)
- **Coding Agent**: reads git logs + progress files to orient, picks highest-priority incomplete feature, works, commits, writes summaries
- Filesystem provides continuity across context windows

### Framework Comparison

| Dimension | [[claude-agent-sdk]] | [[openai-agents-sdk]] | [[langgraph]] | [[crewai]] | [[autogen]] |
|-----------|---------------------|----------------------|---------------|------------|-------------|
| **Loop** | Dumb loop, smart model | Runner class (async/sync/streamed) | State graph | Sequential/Hierarchical | Conversation-driven |
| **State** | Git commits + progress files | 4 strategies | Typed dicts + checkpoints | Task results | Message history |
| **Multi-Agent** | Fork / Teammate / Worktree | Agents-as-tools + Handoffs | Nested graphs | Agent-Task-Crew | 5 orchestration patterns |
| **Philosophy** | Thin harness, trust the model | Code-first | Graph-based control | Role-based collaboration | Conversation as protocol |

### Seven Architectural Decisions
1. **Agent Count** — single vs. multi-agent (maximize single first; split at ~10 overlapping tools)
2. **Reasoning Strategy** — ReAct vs. plan-and-execute (LLMCompiler: 3.6x speedup)
3. **Context Strategy** — 5 approaches; ACON: 26-54% token reduction preserving 95%+ accuracy
4. **Verification** — computational (deterministic) vs. inferential (semantic); guides vs. sensors (Thoughtworks)
5. **Permissions** — permissive (fast/risky) vs. restrictive (safe/slow)
6. **Tool Scoping** — less is more; Vercel removed 80% of tools and got better results
7. **Harness Thickness** — thin (trust model, bet on improvement) vs. thick (encode logic in code)

### The Scaffolding Principle
- Harness = construction scaffolding (temporary, enabling, removed when building is complete)
- As models improve, harness complexity should decrease
- **Co-evolution**: models post-trained with specific harnesses; changing tools degrades performance
- **Manus**: rebuilt 5 times in 6 months, each rewrite removing complexity
- **Future-proofing test**: does performance scale with better models without adding harness complexity?

## Connections

- **[[context-engineering]]** — This article positions context engineering as one of three levels of engineering (prompt < context < harness). Adds "context rot" concept and specific production strategies (compaction, observation masking, JIT retrieval, sub-agent delegation). Corroborates "Lost in the Middle" finding.
- **[[agent-memory]]** — Detailed treatment of multi-timescale memory (short-term vs. long-term) with specific implementations across frameworks. Claude Code's 3-tier hierarchy (index → topic files → raw transcripts) is new detail.
- **[[12-factor-agents]]** — Shares the ethos of "own your infrastructure" but goes broader: the 12-factor framework covers agent design principles; this article covers the 12 *components* of the harness itself.
- **[[instruction-budget]]** — Tool scoping decision directly relates: more tools → more instructions → worse performance. Vercel's 80% tool reduction is a concrete data point.
- **[[coding-agents-conf-2026]]** — Several speakers referenced (Boris Cherny on verification, general agent architecture themes). This article synthesizes those ideas into a unified framework.
- **[[dex-rpi-to-crispy]]** — Dex's CRISPY methodology is effectively a harness design for human-AI workflows. The "thin vs. thick" spectrum maps to Dex's "trust the model" principle.

## Questions Raised

1. **Is harness thickness converging?** The article claims the trend is toward thinner harnesses as models improve. But will this continue, or will new capabilities require new harness complexity?
2. **Co-evolution trap**: If models are post-trained with specific harnesses, how do you upgrade the harness without retraining? Is this a moat or a trap?
3. **The 12th component**: The article lists 11 explicitly but claims 12. The implicit 12th seems to be lifecycle/termination management. Is this an oversight or is the 12th distributed across others?
4. **TerminalBench validity**: How reliable is TerminalBench 2.0 as evidence? Is the LangChain jump replicable?
5. **How does the Ralph Loop compare to CRISPY?** Both solve the multi-session continuity problem but with different mechanisms (filesystem vs. static artifacts).
