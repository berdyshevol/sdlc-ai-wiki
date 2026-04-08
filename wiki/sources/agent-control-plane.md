---
title: "Agent Control Plane: Kubernetes for AI Agents"
type: source
pillar: coding-agents
created: 2026-04-08
updated: 2026-04-08
sources: []
tags: [infrastructure, kubernetes, orchestration, async, mcp, distributed, alpha]
author: Dex (dexhorthy) / HumanLayer
url: https://github.com/humanlayer/agentcontrolplane
date: 2025-2026
---

# Agent Control Plane (ACP)

**Author:** Dex (dexhorthy) / HumanLayer
**URL:** [github.com/humanlayer/agentcontrolplane](https://github.com/humanlayer/agentcontrolplane)
**Stars:** ~384
**Status:** Alpha

## Summary

Agent Control Plane (ACP) is a **Kubernetes-based orchestration platform for AI agents**. It's designed specifically for "long-lived outer-loop agents" that need to process asynchronous execution of both LLM inference and long-running tool calls. Think of it as the infrastructure layer that makes [[software-factory]] pipelines actually run in production.

Where [[12-factor-agents]] provides the design principles and [[humanlayer-codelayer|CodeLayer]] provides the developer interface, ACP provides the **runtime infrastructure** — the plumbing that keeps autonomous agents running reliably, handling async workflows, maintaining conversation context, and integrating external tools.

The Kubernetes-native approach is significant: it treats agents as first-class infrastructure objects (like pods and services) rather than scripts running on someone's laptop.

## Key Architecture (Four Core Objects)

1. **LLM** — Manages provider configuration, API credentials, model parameters. Abstracts the model layer.
2. **Agent** — Combines an LLM with a system prompt and available tools. The unit of autonomous behavior.
3. **Tools** — Supplied via MCP servers, human operators, or other agents. Extensible tool ecosystem.
4. **Task** — Represents a conversation instance with full context history. The unit of work.

## Execution Flow

```
1. Configure LLM resource (API credentials, model)
2. Define Agent (system prompt + tools)
3. Submit Task (user message)
4. LLM processes → may request tool execution
5. Tool results integrate into conversation context
6. Cycle repeats until final response
```

## Key Claims

- **Kubernetes-native agent orchestration** — agents as infrastructure, not scripts
- **Async-first design** — built for long-running, non-blocking agent operations
- **Full MCP support** — Model Context Protocol for tool extensibility
- **Human-in-the-loop as a tool** — approval workflows are just another tool call (validates [[12-factor-agents]] Factor #7)
- **Agent-to-agent delegation** — agents can invoke other agents, enabling multi-agent pipelines
- **Durability and reliability guarantees** — agents survive failures and restarts
- **Distributed task scheduling** — optimized for simplicity over complexity

## Connections

- **Infrastructure layer for the HumanLayer ecosystem:** [[12-factor-agents]] (principles) → [[humanlayer-codelayer|CodeLayer]] (IDE) → ACP (runtime)
- The four-object model (LLM, Agent, Tools, Task) is a clean implementation of [[12-factor-agents]] principles — especially #4 (tools as structured outputs), #6 (launch/pause/resume), #10 (small focused agents)
- Agent-to-agent delegation directly enables the [[superpowers-5]] subagent pattern at infrastructure level
- MCP support connects to the broader tool ecosystem — agents aren't locked into one provider
- The async-first design is essential for [[software-factory]] pipelines where steps take minutes or hours
- Relates to [[automation-levels]] — ACP is the infrastructure that makes Level 4-5 operationally feasible

## Questions Raised

- How does ACP compare to other agent orchestration platforms (LangGraph, CrewAI, AutoGen)?
- What's the operational overhead of running Kubernetes for agent orchestration?
- How does the system handle context window limits across long-running conversations?
- What happens when agent-to-agent delegation creates circular dependencies?
- How mature is the alpha? What's missing for production use?
- Can ACP run non-coding agents (e.g., research, customer support)?
