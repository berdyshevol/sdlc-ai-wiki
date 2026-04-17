---
title: context-mode
type: entity
pillar: coding-agents
created: 2026-04-16
updated: 2026-04-16
sources: [agentic-coding-stack-aslan]
tags: [tool, mcp-server, sandbox, token-optimization, sqlite, fts5, l4]
---

# context-mode

## Overview

**context-mode** is an MCP server that **sandboxes tool execution and only returns what the agent explicitly prints.** Raw output stays in the sandbox; only the result of the agent's analysis (typically `console.log()` calls) reaches the conversation context.

Per [[agentic-coding-stack-aslan]], context-mode occupies **Layer 4 (Token Optimization)** of the agentic coding stack. The pipeline:

```
Agent runs code via ctx_execute
→ raw output stays in sandbox
→ only console.log() output enters context
```

**Source:** [[agentic-coding-stack-aslan]] (Murat Aslan, Apr 2026) — first appearance in the wiki.

**Status in the wiki:** Single source. Repository, license, and authorship not yet verified independently.

## Layer in the Aslan Stack

- **Layer:** L4 — Token Optimization
- **Question it answers:** *How much tool output should enter context?*
- **Failure mode reduced:** Context loss
- **Aslan's "my take":** *"RTK optimizes noisy commands. context-mode optimizes the workflow itself."*

## Operating Model: "Think in Code"

The defining shift, per [[agentic-coding-stack-aslan]]:

> *"Instead of reading huge outputs and mentally compressing them, the agent writes code to do the analysis and prints only the answer. That 'think in code' posture can cut token waste far more aggressively than post-processing alone."*

This is structurally similar to **sub-agent delegation** (a [[context-engineering]] strategy where subagents do verbose work and return condensed summaries) — but the "agent" doing the verbose work is a sandboxed code interpreter, not another LLM call. Cheaper per-token; deterministic per-input.

The named MCP tool primitive (`ctx_execute`) mirrors the OpenAI Code Interpreter / Claude Code Bash patterns but with explicit context-isolation semantics.

## Session Continuity: SQLite + FTS5

A distinguishing feature: context-mode persists work across sessions using **SQLite + FTS5 (full-text search)**. This means:

- Long research/exploration sessions can survive context resets and conversation compaction
- The agent can re-query earlier sandbox results without re-running the analysis
- The retrieval is full-text, not vector — keyword/structured queries against deterministic results

This places context-mode adjacent to the [[agent-memory]] concept the wiki has been tracking — but mechanistically simpler (deterministic query against logged outputs, not learned summarization).

## When to Use (per Aslan)

> *"Sessions are long, exploration is multi-step, and you want recoverability across compaction or context resets. It is especially strong when the right move is not 'filter output' but 'do the analysis inside the sandbox.'"*

Best fit: long research sessions, multi-step exploration, codebase forensics, situations where the question is *"what does this data say"* rather than *"what is the data."*

Not a fit: workflows where the agent doesn't reliably route to sandbox tools (it'll keep reaching for native shell tools and the value evaporates).

## Trade-offs

- **Depends on agent routing discipline.** Per [[agentic-coding-stack-aslan]]: *"If the agent keeps reaching for native shell tools instead of sandbox execution, the value drops."* This is a known failure mode for any tool-routing optimization — the agent must learn to prefer the better tool.
- **Heavier startup than a tiny Rust binary.** Trade-off vs. [[rtk|RTK]].
- **MCP-only surface.** Requires an MCP-capable host.

## Comparison with [[rtk|RTK]]

The two L4 tools attack token waste at different points in the pipeline. From [[agentic-coding-stack-aslan]]:

|  | [[rtk|RTK]] | context-mode |
|---|---|---|
| Operating layer | OS/shell hook | MCP sandbox |
| Core idea | Filter command output **after** execution | **Prevent** raw output from entering context at all |
| Intelligence | Static command-specific rules | Dynamic analysis written by the agent |
| Session continuity | None | SQLite + FTS5 retrieval |
| Best first use case | Shell firehose | Long research/exploration sessions |
| Main weakness | No memory; bounded by command output | Depends on correct tool routing |

Aslan's rule of thumb:

> *"If your pain is 'the shell talks too much,' start with RTK. If your pain is 'the agent should compute the answer instead of reading noise,' start with context-mode. If you are operating at scale, use both."*

> *"Used together, they form a clean sequence: RTK reduces noisy shell output, then context-mode keeps the remainder from flooding the conversation."*

## Relevance to the Wiki

1. **First "agent computes inside sandbox" entity in the wiki.** Existing tools either let the agent see all output ([[claude-agent-sdk|Claude Code Bash]]), filter it after the fact ([[rtk|RTK]]), or delegate verbose work to a sub-LLM. context-mode introduces a fourth option: deterministic sandbox compute with structured-output return.

2. **Concrete instantiation of [[anatomy-agent-harness|Anthropic's]] "smallest possible set of high-signal tokens" guidance** — the agent does the compression work itself, in code, with deterministic results.

3. **First MCP tool with built-in cross-session continuity in the wiki.** [[bmad-method|BMAD's project-context.md]] and [[long-running-claude|Anthropic's CLAUDE.md/CHANGELOG.md patterns]] also provide cross-session memory, but they're file-based conventions, not tool-managed structured stores.

4. **Bridges to the [[agent-memory]] frontier.** The Coding Agents Conference 2026 ([[coding-agents-conf-2026]]) flagged agent memory as the next major capability frontier. context-mode's SQLite+FTS5 model is one architectural answer — not learned memory, but deterministic recall of prior tool outputs.

## Recommended Combinations

Per [[agentic-coding-stack-aslan]], context-mode appears in:

- **Token-constrained:** [[rtk|RTK]] + context-mode + [[ctxo|Ctxo]]
- **Solo developer (upgrade path):** Add context-mode when sessions become research-heavy or when continuity becomes lossy

It is **not** in the default solo, team, or spec-first stacks — explicitly positioned as an upgrade for long sessions or research-heavy work.

## Open Questions

1. **What's the repository / who's the author?** Not stated in [[agentic-coding-stack-aslan]].
2. **What execution environment runs in the sandbox?** Node.js? Python? Multi-language?
3. **How is the SQLite store scoped** — per session, per project, per user, persistent across machines?
4. **What's the routing-discipline failure rate?** Aslan flags this as the main weakness but doesn't quantify how often agents fail to route correctly.
5. **Does context-mode interact with model-provider memory features** (Claude's memory tool, OpenAI's memory)? Or is it independent?
6. **Could context-mode and [[ctxo|Ctxo]] compose** — i.e., context-mode running Ctxo queries inside the sandbox so semantic-graph results don't enter context until the agent prints a summary?

## Links

- [[agentic-coding-stack-aslan]] — primary (and currently only) source
- [[rtk|RTK]] — L4 sibling tool; explicit pairing per Aslan
- [[context-engineering]] — context-mode as sandbox-compute as context strategy
- [[agent-memory]] — context-mode's SQLite+FTS5 store as deterministic-recall memory
- [[agent-harness]] — context-mode as L4 token-optimization harness component
