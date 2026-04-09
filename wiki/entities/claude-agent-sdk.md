---
title: "Claude Agent SDK"
type: entity
pillar: coding-agents
created: 2026-04-09
updated: 2026-04-09
sources: [anatomy-agent-harness]
tags: [framework, anthropic, agent-harness, sdk]
---

# Claude Agent SDK

## Overview

**Claude Agent SDK** is Anthropic's agent framework — the harness infrastructure that powers Claude Code. Anthropic's documentation describes it as "the agent harness that powers Claude Code." It exposes the harness through a single `query()` function that creates the agentic loop and returns an async iterator streaming messages.

- **Creator:** Anthropic
- **Philosophy:** Thin harness, trust the model
- **Key person:** Boris Cherny (creator of Claude Code)

## Relevance

The Claude Agent SDK represents the **thin harness** end of the architectural spectrum. Its core design bet: all intelligence lives in the model; the harness is a "dumb loop" that manages turns. This contrasts with graph-based frameworks (like [[langgraph]]) that encode workflow logic explicitly.

This matters to the wiki because it's the strongest example of the thesis that **harness thickness should decrease as models improve** — Anthropic regularly deletes planning steps from the harness as new model versions internalize those capabilities.

## Architecture

### Runtime
- **"Dumb loop"** — a simple while loop that assembles prompts, calls the LLM, parses output, executes tool calls, and feeds results back
- Single `query()` entry point → async iterator streaming messages
- All intelligence lives in the model, not the harness

### Gather-Act-Verify Cycle
Claude Code uses a specific pattern:
1. **Gather** — search files, read code (context assembly)
2. **Act** — edit files, run commands (tool execution)
3. **Verify** — run tests, check output (verification loop)
4. Repeat

### Tools
Six categories: file operations, search, execution, web access, code intelligence, and subagent spawning.

### Memory
- **CLAUDE.md** project files for persistent project knowledge
- **MEMORY.md** auto-generated files for cross-session memory
- Three-tier hierarchy: lightweight index (~150 chars/entry, always loaded) → detailed topic files (on demand) → raw transcripts (search only)
- Critical principle: memory treated as a "hint," verified against actual state before acting

### State Management
- Git commits as checkpoints
- Progress files as structured scratchpads
- No external state store required

### Multi-Agent (Subagent Orchestration)
Three execution models:
1. **Fork** — byte-identical copy of parent context
2. **Teammate** — separate terminal pane with file-based mailbox communication
3. **Worktree** — own git worktree, isolated branch per agent

### Safety
- Permission enforcement separated from model reasoning architecturally
- Model decides what to attempt; tool system decides what's allowed
- ~40 discrete tool capabilities gated independently
- Three stages: trust establishment (project load) → permission check (each tool call) → explicit user confirmation (high-risk operations)

### The "Ralph Loop" (Long-Running Tasks)
For tasks spanning multiple context windows:
1. **Initializer Agent** — sets up environment (init script, progress file, feature list, initial git commit)
2. **Coding Agent** — reads git logs + progress files to orient, picks highest-priority incomplete feature, works, commits, writes summaries
- Filesystem provides continuity across context windows

## Key Claims

- "Giving the model a way to verify its work improves quality by 2-3x" (Boris Cherny)
- Claude Code achieves 95% context reduction via lazy loading
- The runtime is a "dumb loop" — all intelligence lives in the model
- Anthropic regularly deletes planning steps from the harness as new model versions internalize that capability

## Links

- [[agent-harness]] — concept page; Claude Agent SDK is a canonical thin-harness implementation
- [[context-engineering]] — Claude Code's compaction, JIT retrieval, and sub-agent delegation are production context strategies
- [[agent-memory]] — Claude Code's 3-tier memory hierarchy
- [[anatomy-agent-harness]] — source article with detailed comparison
