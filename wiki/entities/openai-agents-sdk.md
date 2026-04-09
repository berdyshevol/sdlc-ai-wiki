---
title: "OpenAI Agents SDK"
type: entity
pillar: coding-agents
created: 2026-04-09
updated: 2026-04-09
sources: [anatomy-agent-harness]
tags: [framework, openai, agent-harness, sdk, codex]
---

# OpenAI Agents SDK

## Overview

**OpenAI Agents SDK** is OpenAI's agent framework, implementing the harness through the `Runner` class with three modes: async, sync, and streamed. The SDK is "code-first" — workflow logic is expressed in native Python rather than graph DSLs. The Codex product extends this with a three-layer architecture.

- **Creator:** OpenAI
- **Philosophy:** Code-first; workflow logic in native Python
- **Related product:** Codex (coding agent)

## Relevance

The Agents SDK represents a **code-first** approach to harness engineering, sitting between Anthropic's ultra-thin harness and LangGraph's graph-based approach. It explicitly equates the terms "agent" and "harness" to refer to non-model infrastructure. The Codex team's framing that "Codex models feel better on Codex surfaces than a generic chat window" is strong evidence for the [[agent-harness]] thesis that the harness is the product.

## Architecture

### Runtime
- **Runner class** — three execution modes: async, sync, and streamed
- Code-first: workflow logic expressed in native Python, not graph DSLs

### Tools
Three categories:
1. **Function tools** — via `@function_tool` decorator
2. **Hosted tools** — WebSearch, CodeInterpreter, FileSearch
3. **MCP server tools** — Model Context Protocol integration

### Prompt Construction
Strict priority stack:
1. Server-controlled system message (highest priority)
2. Tool definitions
3. Developer instructions
4. User instructions (cascading AGENTS.md files, 32 KiB limit)
5. Conversation history

### State Management
Four mutually exclusive strategies:
1. Application memory
2. SDK sessions
3. Server-side Conversations API
4. Lightweight `previous_response_id` chaining

### Multi-Agent
Two patterns:
1. **Agents-as-tools** — specialist handles bounded subtask, returns result
2. **Handoffs** — specialist takes full control of the conversation

### Guardrails & Safety
Three levels:
1. **Input guardrails** — run on first agent
2. **Output guardrails** — run on final output
3. **Tool guardrails** — run on every tool invocation
- **Tripwire mechanism** — halts agent immediately when triggered

### Codex Architecture (Extension)
Three-layer architecture:
1. **Codex Core** — agent code + runtime
2. **App Server** — bidirectional JSON-RPC API
3. **Client surfaces** — CLI, VS Code, web app

All surfaces share the same harness, which is why "Codex models feel better on Codex surfaces than a generic chat window."

### Structured Outputs
Schema-constrained responses via Pydantic models for type-safe outputs.

## Key Claims

- "Codex models feel better on Codex surfaces than a generic chat window" — evidence that harness matters more than model
- Explicitly equates "agent" and "harness" terminology
- Code-first approach avoids the overhead of graph DSLs

## Links

- [[agent-harness]] — concept page; OpenAI Agents SDK is a code-first harness implementation
- [[anatomy-agent-harness]] — source article with detailed comparison
