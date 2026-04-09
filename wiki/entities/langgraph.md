---
title: "LangGraph"
type: entity
pillar: coding-agents
created: 2026-04-09
updated: 2026-04-09
sources: [anatomy-agent-harness]
tags: [framework, langchain, agent-harness, graph, state-machine]
---

# LangGraph

## Overview

**LangGraph** is LangChain's graph-based agent framework that models the [[agent-harness]] as an explicit state graph. It evolved from LangChain's `AgentExecutor`, which was deprecated in v0.2 because it was hard to extend and lacked multi-agent support. LangChain's Deep Agents product explicitly uses the term "agent harness."

- **Creator:** LangChain
- **Philosophy:** Graph-based control; explicit state management
- **Key person:** Harrison Chase (LangChain CEO)

## Relevance

LangGraph represents the **thick harness** end of the architectural spectrum. Where Anthropic's Claude Agent SDK trusts the model to make all decisions, LangGraph encodes workflow logic as explicit graph structures. This provides more control and debuggability but adds overhead.

LangChain's TerminalBench 2.0 result — jumping from outside the top 30 to rank 5 by changing only harness infrastructure (same model) — is the strongest empirical evidence that the harness matters more than the model.

## Architecture

### Runtime
- Explicit **state graph**: two core nodes (`llm_call` and `tool_node`) connected by a conditional edge
- If tool calls present → route to `tool_node`
- If absent → route to `END`
- Evolved from the deprecated `AgentExecutor` (v0.2)

### State Management
- State modeled as **typed dictionaries** flowing through graph nodes
- **Reducers** merge updates at each step
- **Checkpointing** at super-step boundaries
- Enables: resume after interruptions, time-travel debugging

### Error Handling
Four distinct error types:
1. **Transient** — retry with backoff
2. **LLM-recoverable** — return error as `ToolMessage` so the model can adjust
3. **User-fixable** — interrupt for human input
4. **Unexpected** — bubble up for debugging

### Multi-Agent
- Subagents implemented as **nested state graphs**
- Full graph composability

### Memory (LangGraph)
- **Namespace-organized JSON Stores** for long-term memory

### Deep Agents (LangChain Product)
Explicitly uses the term "agent harness":
- Built-in tools
- Planning via `write_todos` tool
- File systems for context management
- Subagent spawning
- Persistent memory

### Structured Outputs
Schema-constrained responses via Pydantic models. Legacy `RetryWithErrorOutputParser` available for edge cases (feeds original prompt + failed completion + parsing error back to model).

## Key Claims

- **TerminalBench 2.0**: Same model, harness-only changes → outside top 30 to rank 5 (strongest evidence for "harness > model")
- LangChain coined/popularized the formula: "If you're not the model, you're the harness" (Vivek Trivedy)
- `AgentExecutor` was deprecated because it was hard to extend and lacked multi-agent support — validating the need for graph-based harness architecture

## Links

- [[agent-harness]] — concept page; LangGraph is a canonical thick-harness implementation
- [[context-engineering]] — graph structure enables explicit context management at each node
- [[anatomy-agent-harness]] — source article with detailed comparison
