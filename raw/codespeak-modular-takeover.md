# Modular takeover: from vibe-coded app to spec-driven development

**Source:** https://codespeak.dev/blog/modular-takeover-20260408
**Date:** April 8, 2026
**Author:** Dmitry Savvinov (CodeSpeak)
**Retrieval note:** Fetched via Claude Code `WebFetch` (2026-04-16). The tool pipes HTML → markdown → AI processing; output is AI-rewritten prose with verbatim quotes preserved where the tool marked them. Direct quotations in the text below are in `"..."`. Non-quoted prose should be treated as a close paraphrase, not 1:1 text. Ingest with this caveat. Re-fetch from a non-AI-processing tool (raw HTML + reader view) if the exact original wording is needed for citation.

---

## Overview

CodeSpeak's new modular takeover feature bridges the gap between exploratory "vibe coding" and careful evolution of applications. The tool analyzes existing codebases and proposes modular decomposition through an interactive wizard, allowing developers to transition from natural-language-driven prototyping to specification-driven development.

## The Problem with Vibe Coding

> "Vibe coding excels at exploration — at understanding what you want. Evolving a vibe-coded app carefully is a different problem."

The approach works well initially but creates challenges when maintaining or extending code, as agent context resets and architectural decisions become implicit in implementation rather than documented.

## How Modular Takeover Works

The workflow involves five steps:

1. Build an application through natural-language prompting
2. Run `codespeak takeover` on the completed codebase
3. Review the proposed module structure in an interactive browser-based wizard
4. Refine the decomposition by requesting splits, merges, or rearrangement
5. Generate specification files and begin spec-driven development

## Folio Case Study

Folio, a dual-pane terminal file manager written in Go, demonstrated the approach. The application grew to approximately 3,000 lines across multiple files through iterative vibe-coded sessions. The takeover wizard produced four modular specifications totaling **430 lines of Markdown — approximately a 7× reduction** compared to the original codebase.

The resulting specs covered:
- Core model, panels, context menu, and settings
- Filesystem operations and archive support
- Theming and file formatting
- Integrated terminal panel

## Intent Preservation

Specifications capture design decisions invisible in code alone. For example, keyboard passthrough rules for the terminal panel documented that:

> "only the following keys are handled by the application itself rather than forwarded to the terminal process: Ctrl+T, Ctrl+\\, Ctrl+Up, Ctrl+Down."

This detail matters because the design deliberately avoids intercepting other keys like F10, ensuring applications like `htop` function correctly within the terminal.

## Practical Development Example — adding F7 (mkdir)

Adding folder creation (F7 keybinding) required only modest specification changes:

- One new function description in `file-ops.cs.md`
- One row added to the keybinding table in `app.cs.md`

Running `codespeak build` generated all necessary Go code — function implementation, keyboard handlers, input routing, and panel refresh logic — without manual code writing.

## Benefits and Future Development

The feature transforms vibe coding economics by providing an "off-ramp" from rapid prototyping to maintainable evolution. Specifications serve dual purposes: feeding back into CodeSpeak for code generation and functioning as concise, human-readable documentation.

The team continues improving the initial modularization proposal intelligence, enhancing module boundary handling, and ensuring focused, predictable code changes from specification edits.

The complete demonstration project is available on GitHub's `modular-takeover` branch, including generated specifications and the mkdir feature implementation.

---

## Repo reference

GitHub org: `codespeak-dev`
Demo repo: `codespeak-dev/folio` (verified via `gh api`, pushed 2026-04-08, corresponds to this blog post)
CLI install: `uv tool install codespeak-cli`

## Companion context (not in the article — from the CodeSpeak blog sequence)

Based on the blog-post timeline retrieved from https://codespeak.dev/blog:

```
2026-02-23 — First glimpse of `codespeak takeover` (initial version — monolithic spec)
2026-03-02 — Test coverage improvement
2026-03-09 — Spec dependencies + Managed files
2026-03-17 — Reconstructing specs from vibe coding sessions (Anthropic-compatible providers)
2026-03-24 — Tests + `codespeak impl` command
2026-04-08 — THIS POST: Modular takeover (web wizard, multi-spec decomposition)
2026-04-15 — codespeak-dev/vibe-sharing repo — asking for vibe-coded-project donations
```

The April 8 post is therefore the **current end-state of a seven-week evolution** from monolithic takeover (Feb 23) → modular takeover with wizard (Apr 8), with intermediate features supporting the modular target (spec dependencies, Managed files, session-reconstructed specs).
