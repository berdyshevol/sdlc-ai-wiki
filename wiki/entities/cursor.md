---
title: Cursor
type: entity
pillar: coding-agents
created: 2026-05-05
updated: 2026-05-05
sources: [zakariasson-cursor-software-factory, agentic-coding-stack-aslan]
tags: [ide, agent-first, cloud-agents, computer-use, bugbot, agentic-code-owner, cursor-workers, anysphere]
---

# Cursor

## Overview

**Cursor** is an AI-first code editor and the flagship product of **Anysphere**. Originally a fork of VS Code, it added tab autocomplete and chat as its initial differentiators (2022–2023). Over 2024–2026 it added agent mode, cloud agents (each with its own VM), computer-use for UI verification, **Bugbot** (PR-review automation), an **agentic code owner**, a **continual-learning** plugin (extracts rules from chat history), and most recently **Cursor Workers** — a self-hosted variant of the same orchestration layer.

In **April–May 2026**, Cursor launched **Cursor 3** — a complete rewrite with no VS Code base. The UI is reorganized around managing many agents instead of editing files (per [[zakariasson-cursor-software-factory|Zakariasson's AI Engineer talk]]). Cursor describes Cursor 3 as a "first stab at multi-agent orchestration."

## Relevance

Cursor is one of two major IDE-vendor data points in the wiki (alongside JetBrains' [[sdd-course-deeplearning-ai|SDD course partnership]]) and the only IDE vendor that has publicly described the architecture of its in-house [[software-factory]] in detail. Notable:

- **Reference implementation of large-scale agent operations** — "multiple thousands a day" of cloud agents internally per Zakariasson; comparable to [[strongdm]] as a production data point.
- **Pioneered cloud-agent-with-computer-use** as a first-class feature for UI verification, a concrete answer to the [[code-legibility-debate]] question of how to validate work without reading code.
- **Bugbot, agentic code owner, continual-learning plugin** are reusable factory automations now part of the wiki's pattern library — Cursor's read-merge-PR-comments and agentic code-owner patterns appear nowhere else in the corpus.
- **Cursor Workers (May 2026)** brings the same agent harness to user-owned infrastructure, partially answering enterprise/security objections about cloud-only agent execution.
- **Anti-cursor.directory rule philosophy** — Zakariasson explicitly argues *against* the "install every rule" approach, calling for rules to emerge dynamically from observed failures. This is a contrarian position from inside the company that ships rules infrastructure.

## Key Claims

- **Originally a VS Code fork; Cursor 3 is a complete rewrite** with an agent-first UI ([[zakariasson-cursor-software-factory]]).
- **Cloud agents run in isolated VMs** per agent — Zakariasson favors this over git-worktree shared workspaces because shared workspaces force you to branch DB/cache/users anyway. ~$1/turn cost reference.
- **Computer-use tool for cloud agents** — agents record video of themselves clicking through the app to verify UI work; described as Zakariasson's "AGI moment" at internal launch.
- **Bugbot** — automated PR reviewer that enforces team-specific rules (e.g., Cursor's "no foreign keys" rule for performance reasons; models always add foreign keys, Bugbot flags them).
- **Agentic code owner** — assesses PR risk; auto-approves low-risk PRs (unblocks engineers blocked by absent code-owners 20% of the time); pulls in the original code-author for high-risk PRs.
- **Continual-learning plugin** — extracts rules from chat-history transcripts so users don't have to remember to write rules manually. Cursor anticipates this evolving into per-team weight-level fine-tuning.
- **Linear integration: every ticket spawns a cloud agent.** Stale feature flags auto-create Linear issues that trigger auto-removal cloud agents — a closed-loop signal → ticket → PR pipeline.
- **Cursor Workers (May 2026)** — `agent worker start` CLI runs the same orchestration on any machine (Mac mini, VM, dev container), surfacing in cursor cloud as a self-hosted worker.
- **Domain-modular teams** — extensibility, cloud, etc. — each team owns a domain, with cross-team work coordinated via the agentic code owner instead of meetings ([[zakariasson-cursor-software-factory]]).
- **Designers push to production** — at Cursor, designers are 50/50 Figma/code per Zakariasson; this is unusual enough to be noteworthy.
- **Listed in [[agentic-coding-stack-aslan|Aslan's stack]]** as a Layer 1 / Layer 5 example (Delivery Methodology / Product Surface), though Aslan's piece predates Cursor 3.

## Links

- Source pages: [[zakariasson-cursor-software-factory]] (primary), [[agentic-coding-stack-aslan]] (mention)
- Concepts: [[software-factory]], [[agent-harness]], [[automation-levels]], [[agent-memory]] (continual learning), [[shift-work]] (sync planning / async execution mirrors the StrongDM pattern)
- Related entities: [[claude-agent-sdk]] (parallel cloud-agent-with-computer-use architecture from Anthropic), [[humanlayer]] (parallel orchestration: [[agent-control-plane]], [[humanlayer-codelayer|CodeLayer]])
- External: https://cursor.com
