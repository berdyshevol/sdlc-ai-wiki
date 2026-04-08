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

### The Dumb Zone

Around **40% of context window usage**, output quality begins degrading. The less of the context window you use, the better the results. Experienced users can push to 60% depending on task complexity, but beginners should aim to stay under 40%.

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

### Static Artifacts Over Autocompaction

CRISPY produces static markdown artifacts (design docs, structure outlines, plans) at each stage. This means you can resume from any point without depending on autocompaction quality. "Everything that matters is going into static assets."

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
