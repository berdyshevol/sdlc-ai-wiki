---
title: "CrewAI"
type: entity
pillar: coding-agents
created: 2026-04-09
updated: 2026-04-09
sources: [anatomy-agent-harness]
tags: [framework, agent-harness, multi-agent, role-based]
---

# CrewAI

## Overview

**CrewAI** is a role-based multi-agent framework that implements the [[agent-harness]] through a collaboration metaphor: agents are team members with defined roles, goals, and backstories. Its Flows layer adds deterministic control on top of autonomous agent collaboration.

- **Creator:** CrewAI (company)
- **Philosophy:** Role-based collaboration; "deterministic backbone with intelligence where it matters"

## Relevance

CrewAI represents a **medium-thick harness** approach — thicker than Anthropic/OpenAI (explicit role definitions and task routing) but more flexible than LangGraph's full graph control. Its Agent-Task-Crew abstraction is the most accessible multi-agent model, making it popular for teams new to agent architecture.

The Flows layer is notable because it demonstrates the **hybrid approach**: deterministic routing and validation at the orchestration level, with autonomous AI collaboration within Crews.

## Architecture

### Core Abstractions
Three primary objects:
1. **Agent** — the harness around the LLM, defined by role, goal, backstory, and tools
2. **Task** — the unit of work assigned to an agent
3. **Crew** — the collection of agents working together

### Orchestration
- **Sequential** — tasks executed in order
- **Hierarchical** — manager agent delegates to specialists

### State Management
- **Task results** — state flows through task completion

### Multi-Agent
- **Agent-Task-Crew** model — agents are specialists defined by role
- Agents can share information and delegate work within a Crew

### Flows Layer
Adds a "deterministic backbone with intelligence where it matters":
- Manages routing and validation deterministically
- Crews handle autonomous collaboration within flow steps
- Bridges the gap between full autonomy and full control

## Key Claims

- Role-based definitions (role, goal, backstory) make agent design intuitive
- Flows provide deterministic control over multi-agent workflows without sacrificing agent autonomy within tasks
- Positioned between thin harnesses (trust model) and thick harnesses (encode all logic)

## Links

- [[agent-harness]] — concept page; CrewAI is a role-based harness implementation
- [[anatomy-agent-harness]] — source article with detailed comparison
