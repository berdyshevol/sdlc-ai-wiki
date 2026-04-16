---
title: "Context Engineering"
type: concept
pillar: coding-agents
created: 2026-04-08
updated: 2026-04-16
sources: [dex-rpi-to-crispy, coding-agents-conf-2026, 12-factor-agents, anatomy-agent-harness, matt-pocock-dex-horthy-chat, sdd-course-deeplearning-ai]
tags: [context-window, prompting, architecture, dumb-zone, context-rot, quadratic-attention, cup-metaphor, cognitive-debt, ai-fatigue]
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
- **[[matt-pocock-dex-horthy-chat]]** — Conversational supplement: explicit quadratic-attention explanation, the "cup" metaphor for task sizing, and the cron-Ralph pattern as a context engineering deployment shape.
- **[[sdd-course-deeplearning-ai]]** — DeepLearning.AI × JetBrains course. Mainstream-pedagogy version of the same principles: **clear between features** (`/clear` is explicit Lesson 9 discipline); **sub-agents for deep review preserve the main agent's context window, rather than polluting it**; **cognitive debt** (the mental load of tracking fast AI-generated changes) as the human-side complement to context rot — managed by size discipline (smaller task groups) and review level (spec, not CSS class).

## Current Understanding

### Why context length hurts: quadratic attention

The reason long context degrades quality is mechanical. Per [[matt-pocock-dex-horthy-chat]], Dex frames it for non-ML engineers as: the compute needed to ingest and act on context scales **quadratically** with token count, **per layer and per attention head**. Doubling tokens means roughly 4× the work. With 50–80 layers and many heads, "every single token you add quadratically scales into oblivion and makes it really dumb." This is also why long-context **needle-in-a-haystack** benchmarks are misleading: real coding tasks don't ask the model to find one sentence in 100k tokens, they ask it to act on most of those tokens, which is a much harder problem and is poorly benchmarked.

### The "cup" metaphor for task sizing

From [[matt-pocock-dex-horthy-chat]]: think of the context budget for a Ralph iteration as a cup. You have some volume of work (specs, source reads, edits, test runs, fixes, commit) that needs to fit. **The cup is smaller than you think it is.** The lever is task size: your iteration must be small enough that edits + verification (run tests, fix issues, re-run tests, commit) all fit inside the smart zone. If iterations consistently push past the smart zone, shrink the task. Dex's heuristic for sizing: *"how much code would you write before you pulled up the web app to look at it? How much before you paused to run the tests? That's a good task size for Ralph."*

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

### Context Rot and Production Strategies (from [[anatomy-agent-harness]])

**Context rot** is the phenomenon where model performance degrades 30%+ when key content falls in mid-window positions (Chroma research, corroborated by Stanford's "Lost in the Middle" finding). Even million-token windows suffer from instruction-following degradation as context grows.

Five production strategies to combat context rot:

1. **Compaction** — summarizing conversation history when approaching limits (Claude Code preserves architectural decisions and unresolved bugs while discarding redundant tool outputs)
2. **Observation masking** — JetBrains' Junie hides old tool outputs while keeping tool calls visible
3. **Just-in-time retrieval** — maintaining lightweight identifiers and loading data dynamically (Claude Code uses grep, glob, head, tail rather than loading full files)
4. **Sub-agent delegation** — each subagent explores extensively but returns only 1,000-2,000 token condensed summaries
5. **Structured note-taking** — progress files, MEMORY.md, static artifacts (overlaps with CRISPY's approach)

Anthropic's context engineering guide states the goal: *find the smallest possible set of high-signal tokens that maximize likelihood of the desired outcome.*

### Context Engineering as a Level of Engineering

[[anatomy-agent-harness]] positions context engineering as the middle of three concentric levels:

1. **Prompt engineering** — crafting instructions
2. **Context engineering** — managing what the model sees and when
3. **Harness engineering** — encompasses both, plus all application infrastructure

This reinforces context engineering's status as a distinct discipline, not just "better prompting."

## Open Questions

1. Is the "dumb zone" at 40% consistent across models, or model-specific?
2. How does autocompaction quality compare to CRISPY's static artifact approach?
3. Can you automatically detect when you've exceeded the effective context budget?
4. How do you balance the "less is more" principle with agents that need broad codebase context?
5. **NEW:** How do the five production strategies (compaction, observation masking, JIT retrieval, sub-agent delegation, structured notes) compare in practice? Which combinations work best?

## Related Concepts

- [[instruction-budget]] — the constraint that context engineering works within
- [[agent-memory]] — a context engineering strategy for persistence across sessions
- [[agent-harness]] — context engineering is one of three levels of harness engineering
- [[12-factor-agents]] — context engineering principles applied to agent architecture
