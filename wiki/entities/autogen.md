---
title: "AutoGen"
type: entity
pillar: coding-agents
created: 2026-04-09
updated: 2026-04-09
sources: [anatomy-agent-harness]
tags: [framework, microsoft, agent-harness, multi-agent, conversation-driven]
---

# AutoGen

## Overview

**AutoGen** (evolving into **Microsoft Agent Framework**) pioneered conversation-driven agent orchestration. Agents communicate through structured message passing, with conversations as the primary coordination protocol.

- **Creator:** Microsoft Research
- **Philosophy:** Conversation as protocol; multi-agent orchestration via message passing
- **Evolution:** AutoGen → Microsoft Agent Framework

## Relevance

AutoGen's approach is fundamentally different from other frameworks: instead of explicit graphs (LangGraph), role definitions (CrewAI), or minimal loops (Anthropic), coordination happens through **conversation patterns**. This makes it the most flexible for complex multi-agent scenarios but also the hardest to reason about.

Its five orchestration patterns provide the broadest palette of multi-agent coordination strategies.

## Architecture

### Three-Layer Architecture
1. **Core** — fundamental agent abstractions and message passing
2. **AgentChat** — conversational agent interfaces
3. **Extensions** — integrations and additional capabilities

### State Management
- **Message history** — conversation serves as both state and coordination protocol

### Five Orchestration Patterns
1. **Sequential** — agents take turns in fixed order
2. **Concurrent** — fan-out/fan-in parallel execution
3. **Group chat** — multiple agents in free-form discussion
4. **Handoff** — one agent transfers control to another
5. **Magentic** — a manager agent maintains a dynamic task ledger coordinating specialists

### Multi-Agent
- Conversation-driven coordination
- Agents are first-class citizens that communicate through messages
- No central graph or fixed workflow required

## Key Claims

- Pioneered conversation-driven orchestration as an architectural pattern
- Five orchestration patterns cover most multi-agent coordination needs
- Magentic pattern (dynamic task ledger with manager agent) is the most sophisticated built-in multi-agent strategy
- Evolving into Microsoft Agent Framework suggests enterprise backing and long-term investment

## Links

- [[agent-harness]] — concept page; AutoGen is a conversation-driven harness implementation
- [[anatomy-agent-harness]] — source article with detailed comparison
