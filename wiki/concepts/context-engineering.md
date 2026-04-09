---
title: "Context Engineering"
type: concept
pillar: coding-agents
created: 2026-04-08
updated: 2026-04-08
sources: [dex-rpi-to-crispy, coding-agents-conf-2026, 12-factor-agents]
tags: [context-window, prompting, architecture, dumb-zone]
---

# Context Engineering

## Definition

**Context engineering** is the discipline of carefully managing what goes into an LLM's context window — both the information and the instructions — to maximize output quality. It has two complementary reads:

1. **More information** — RAG pipelines, codebase search, documentation retrieval. "Put the right stuff in."
2. **Better instructions and simpler tasks** — smaller context windows, fewer instructions per prompt, decomposed workflows. "Put less stuff in, but make it count."

Dex argues the second read is more important and less discussed.

## Key Sources

- **[[dex-rpi-to-crispy]]** — Primary source. Introduces the "dumb zone" concept and advocates for smaller context windows. Wrote paper "12 Factor Agents" which was "allegedly the first time anyone was talking a lot about context engineering."
- **[[coding-agents-conf-2026]]** — Kilo Code: context must expand with trust level (autocomplete needs current file; orchestration needs multiple repos). Pinterest: 3-tier memory architecture (hot/domain/cold) as context management. Databricks: too many MCPs degrade output.
- **[[12-factor-agents]]** — Principles of owning your context, small focused agents.

## Current Understanding

### The Smart Zone and The Dumb Zone

Dex's slide version of the talk introduces complementary terminology for context window regions:

- **"The Smart Zone"** — the upper ~40% of the context window, where system instructions, CLAUDE.md, built-in tools, and MCP tools reside. The goal is to keep core instructions within this space to maintain reliability.
- **"The Dumb Zone"** — as user messages, massive files (like 1000-line plans), and conversation history fill the lower portion of the window, the model begins to lose track of instructions and output quality degrades.

The less of the context window you use, the better the results. Experienced users can push to 60% depending on task complexity, but beginners should aim to stay under 40%.

Note: this is a teaching heuristic, not a hard rule. It depends on the ratio of instructions to information and the complexity of the task.

### Two Failure Modes

1. **Too much information:** Context stuffed with RAG results, documentation, tool outputs. The model drowns in data and loses focus on instructions.
2. **Too many instructions:** Context filled with complex workflow prompts, MCP tool descriptions, system prompts. The model exceeds its [[instruction-budget]] and starts skipping steps.

### CRISPY as Context Engineering in Practice

CRISPY decomposes a monolithic workflow into 7 stages, each with its own context window:
- **Research context** — ticket hidden, just codebase facts. Prevents opinion contamination.
- **Design context** — ticket + research + interactive discussion. Focused on alignment.
- **Plan context** — design + structure + implementation details. Focused on tactics.
- Each context stays under 40 instructions and uses a fraction of the available window.

### Mental Alignment via Static Artifacts

CRISPY/QRSPI produces static markdown artifacts (design docs, structure outlines, plans) at each stage. These serve a dual purpose: (1) you can resume from any point without depending on autocompaction quality ("everything that matters is going into static assets"), and (2) they enable **"Mental Alignment"** — the artifacts (Questions, Research, Outlines) act as shared ground between the human and the agent, ensuring both are working from the same understanding before code is written.

### Context Expansion with Trust (Kilo Code)

| Trust Level | Context Needed |
|-------------|---------------|
| Autocomplete | Current file + imports |
| Chat | Current file + related files + docs |
| Agents | Full repo + config + dependencies + build system |
| Orchestration | Multiple repos + production code + meeting transcripts + data lineage |

This suggests context engineering isn't just about minimizing — it's about **right-sizing context to the trust level** of the interaction.

## Open Questions

1. Is the "dumb zone" at 40% consistent across models, or model-specific?
2. How does autocompaction quality compare to CRISPY's static artifact approach?
3. Can you automatically detect when you've exceeded the effective context budget?
4. How do you balance the "less is more" principle with agents that need broad codebase context?

## Related Concepts

- [[instruction-budget]] — the constraint that context engineering works within
- [[agent-memory]] — a context engineering strategy for persistence across sessions
- [[12-factor-agents]] — context engineering principles applied to agent architecture
