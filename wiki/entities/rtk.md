---
title: RTK
type: entity
pillar: coding-agents
created: 2026-04-16
updated: 2026-04-16
sources: [agentic-coding-stack-aslan]
tags: [tool, rust, cli-proxy, shell-output, token-optimization, l4]
---

# RTK

## Overview

**RTK** is a Rust CLI proxy that **intercepts shell command output and compresses it before the agent sees it.** It sits between the agent's tool layer and the shell, applying command-specific filters that understand which parts of a given command's output carry signal.

Per [[agentic-coding-stack-aslan]], RTK occupies **Layer 4 (Token Optimization)** of the agentic coding stack. The pipeline:

```
Agent runs: git log -50
RTK intercepts → applies command-specific filter → smaller output reaches the model
```

**Source:** [[agentic-coding-stack-aslan]] (Murat Aslan, Apr 2026) — first appearance in the wiki.

**Status in the wiki:** Single source. Repository, license, and authorship not yet verified independently. Name "RTK" is not disambiguated in the source post.

## Layer in the Aslan Stack

- **Layer:** L4 — Token Optimization
- **Question it answers:** *How much tool output should enter context?*
- **Failure mode reduced:** Context loss
- **Aslan's "my take":** *"RTK is the fastest way to improve a noisy shell-based workflow without redesigning how the agent works."*

## Key Mechanism: Command-Specific Filters

RTK's distinguishing claim is that it is **not generic truncation.** Per [[agentic-coding-stack-aslan]]:

> *"It understands command ecosystems. A test runner, a git command, and a docker command each have different 'signal' patterns, and RTK uses command-specific filters to keep the right parts."*

This places RTK in the same category as **observation masking** strategies documented in [[anatomy-agent-harness]] (JetBrains Junie hides old tool outputs while keeping tool calls visible) — but pushed earlier in the pipeline (filter at output generation, not after-the-fact context compaction).

## When to Use (per Aslan)

> *"Your workflow is shell-heavy and the biggest source of token waste is command output from builds, tests, git, package managers, or logs."*

Best fit: shell-centric workflows with verbose tools (test runners, build systems, package managers, git commands at scale).

Not a fit: workflows that already do most work via direct file reads or sandboxed code execution.

## Trade-offs

- **Hook-and-filter model.** Per-environment installation overhead.
- **Rust dependency.** Requires Rust toolchain or pre-built binary.
- **No session memory.** RTK only acts on individual command invocations; it doesn't remember earlier outputs or compose across commands.
- **Bounded by what the underlying command emits.** RTK shrinks output but doesn't change the fact that the command still generated all of it on disk / in the OS pipe — it's a *display* optimization, not an *execution* optimization.

## Relevance to the Wiki

1. **First "shell-output proxy" entity in the wiki.** Existing [[context-engineering]] strategies operate inside the agent's loop (compaction, JIT retrieval, sub-agent delegation, structured note-taking). RTK operates *outside* the loop, at the OS/shell hook layer. This is a category the wiki had named only descriptively before.

2. **Concretization of Anthropic's "find the smallest possible set of high-signal tokens" guidance.** Quoted in [[context-engineering]] from the Anthropic context-engineering guide. RTK is one specific implementation of that principle for shell tools.

3. **Counterweight to "let the agent see everything" defaults.** Many MCP servers and CLI tools dump full output into context by default. RTK is part of an emerging tooling category that treats context as a budgeted resource.

## Comparison with [[context-mode]]

The two L4 tools attack token waste at different points in the pipeline. From [[agentic-coding-stack-aslan]]:

|  | RTK | [[context-mode]] |
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

## Recommended Combinations

Per [[agentic-coding-stack-aslan]], RTK appears in two of four recommended stacks:

- **Solo developer:** [[superpowers]] + [[ctxo|Ctxo]] + RTK
- **Token-constrained:** RTK + [[context-mode]] + [[ctxo|Ctxo]]

It does **not** appear in the team-workflow stack (BMAD + superpowers + Ctxo + gsd-2) — possibly because gsd-2 internalizes some of RTK's role at L5, possibly because team workflows don't have the same shell-firehose problem.

## Open Questions

1. **What does "RTK" stand for?** Not expanded in the source. Disambiguation needed.
2. **What's the repository / who's the author?** Not stated in [[agentic-coding-stack-aslan]].
3. **How are command-specific filters defined and updated?** Static rules, plug-in registry, or community-contributed?
4. **How does RTK handle exit codes and error states?** Filter-on-success is straightforward; filter-on-failure is where filtering most damages debugging.
5. **Does RTK compose with shell pipes** (`cmd1 | cmd2`)? The OS/shell hook model has known issues with pipes.
6. **Is there any data on token-savings ratio per command?** A specific number (e.g., "70% reduction on `cargo test --verbose`") would make the case more concrete.

## Links

- [[agentic-coding-stack-aslan]] — primary (and currently only) source
- [[context-mode]] — L4 sibling tool; explicit pairing per Aslan
- [[context-engineering]] — RTK as observation-masking-as-tool
- [[agent-harness]] — RTK as a harness component bolted on outside the agent loop
