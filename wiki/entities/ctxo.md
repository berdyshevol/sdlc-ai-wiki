---
title: Ctxo
type: entity
pillar: coding-agents
created: 2026-04-16
updated: 2026-04-16
sources: [agentic-coding-stack-aslan]
tags: [tool, mcp-server, semantic-analysis, codebase-graph, technical-context, l3]
---

# Ctxo

## Overview

**Ctxo** is an MCP server for **semantic codebase analysis** — exposing graph-level questions about a code repository (blast radius, logic slices, why-context from git history, symbol importance, dead code, PR impact) to coding agents.

Per [[agentic-coding-stack-aslan]], Ctxo occupies **Layer 3 (Technical Context)** of the agentic coding stack — the layer that answers *"what does this code actually mean?"* Distinct from text-search or grep tools, Ctxo provides *"deeper questions than plain text search can answer"* by indexing the codebase as a semantic graph.

**Source:** [[agentic-coding-stack-aslan]] (Murat Aslan, Apr 2026) — first appearance in the wiki.

**Status in the wiki:** Single source. Repository, license, and authorship not yet verified independently.

## Layer in the Aslan Stack

- **Layer:** L3 — Technical Context
- **Question it answers:** *What does this code actually mean?*
- **Failure modes reduced:** Review bottlenecks, multi-session conflicts
- **Aslan's "my take":** *"This is the scarcest capability in the current ecosystem. Plenty of tools tell agents how to behave. Far fewer help them understand the code they are about to change."*

## Six Semantic-Analysis Primitives

Ctxo exposes (at least) six MCP tool primitives, each answering a distinct codebase-understanding question:

| Tool | Question it answers |
|------|---------------------|
| `get_blast_radius` | What breaks if I change this? |
| `get_logic_slice` | What does this symbol depend on? |
| `get_why_context` | Why was this implemented this way? (uses git history) |
| `get_symbol_importance` | What code matters most in this repo? |
| `find_dead_code` | What appears to be dead? |
| `get_pr_impact` | What is the likely risk of this PR? |

The shape of these primitives suggests Ctxo maintains a multi-modal index: dependency graph (blast radius, logic slice), call graph or centrality measure (symbol importance), reachability analysis (dead code), and a git-blame-aware why-context retrieval.

## When to Use (per Aslan)

> *"The cost of misunderstanding the code is higher than the cost of indexing the repo. In other words: non-trivial edits, shared modules, legacy surfaces, or changes where 'just inspect a few files' is not good enough."*

Best fit: production codebases, brownfield surfaces, refactors that touch shared abstractions.

Not a fit: toy projects, throwaway scripts.

## Trade-offs

- **Indexing step required.** Not zero-setup; the repo must be indexed before queries return useful results.
- **Strongest support today: TypeScript/JavaScript.** Other languages may have weaker coverage.
- **MCP-only surface.** Requires a host that supports MCP servers (Claude Code, Cursor, others).

## Relevance to the Wiki

Ctxo is significant for several reasons not yet covered elsewhere in the wiki:

1. **Closes the L3 gap in the wiki's tool taxonomy.** Most existing entities improve *how* an agent operates ([[claude-agent-sdk]], [[langgraph]], [[crewai]], [[autogen]]) or *what process* it follows ([[bmad-method]], [[spec-kit]], [[superpowers]]). Ctxo is the first wiki entity dedicated to improving **what the agent understands about the code itself.**

2. **Concrete instantiation of "[[context-engineering|just-in-time retrieval]]" — but semantic, not textual.** [[anatomy-agent-harness]] documents JIT retrieval (grep/glob/head/tail) as a context-engineering strategy in [[claude-agent-sdk|Claude Code]]. Ctxo extends this from text-level to graph-level retrieval.

3. **Counterweight to vector-RAG-first thinking.** The [[coding-agents-conf-2026]] documented the agentic-search-vs-vector-RAG debate (Jessica Wang, Braintrust). Ctxo's graph-query primitives are a third option: not text search, not vector retrieval, but typed semantic queries.

4. **Mechanistic enabler for spec-to-code traceability.** Aslan calls out spec-to-code traceability as the unbuilt missing link. Ctxo's `get_blast_radius` and `get_logic_slice` are *half* of that bridge — the code-side graph. The unbuilt half is the spec-side graph (which spec items map to which symbols). Aslan: *"Ctxo gets closest to the code-side graph."*

## Comparison with Similar Capabilities

| Capability | Ctxo | grep/glob (Claude Code) | Vector RAG | Sourcegraph |
|------------|------|--------------------------|------------|-------------|
| Lookup type | Semantic graph | Text search | Embedding similarity | Mixed (text + LSIF graph) |
| Setup cost | Indexing required | None | Embedding pipeline | Indexing required |
| Best at | "What breaks if I change X" | "Find this string" | "Code similar to this" | Mixed |
| Agent integration | MCP server | Built-in tool | Custom retrieval | API/MCP |

Note: this comparison is the wiki's interpretation, not a direct claim from [[agentic-coding-stack-aslan]].

## Recommended Combinations

Per [[agentic-coding-stack-aslan]], Ctxo appears in **all four** recommended stacks — the most ubiquitous tool in the post. This is consistent with Aslan's "scarcest capability" framing:

- **Solo developer:** [[superpowers]] + Ctxo + [[rtk|RTK]]
- **Team workflow:** [[bmad-method|BMAD-METHOD]] + [[superpowers]] + Ctxo + [[gsd-2]]
- **Spec-first:** [[spec-kit]] + [[superpowers]] + Ctxo
- **Token-constrained:** [[rtk|RTK]] + [[context-mode]] + Ctxo

## Open Questions

1. **What's the repository / who's the author?** Not stated in [[agentic-coding-stack-aslan]]. Worth resolving before the entity page is treated as authoritative.
2. **Is the index incremental or full-rebuild?** Practical question for large monorepos.
3. **How does `get_why_context` handle squash-merged history?** Git-blame-based why-context degrades when history is rewritten.
4. **What's the failure mode when the index is stale?** Production codebases drift — does Ctxo detect drift, refuse queries, or return stale answers silently?
5. **Could the same primitives be exposed for non-code artifacts** (specs, design docs)? This is one path toward the spec-to-code traceability layer Aslan calls missing.

## Links

- [[agentic-coding-stack-aslan]] — primary (and currently only) source
- [[agent-harness]] — Ctxo as the L3 component most existing harnesses lack
- [[context-engineering]] — Ctxo as semantic JIT retrieval
- [[code-legibility-debate]] — Ctxo as enabling infrastructure for "navigate-don't-read"
- [[spec-driven-development]] — Ctxo as the code-side half of the spec-to-code traceability bridge
