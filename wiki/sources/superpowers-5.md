---
title: "Superpowers 5: AI Coding Agent Evolution"
type: source
pillar: [coding-agents, spec-driven]
created: 2026-04-08
updated: 2026-04-13
sources: []
tags: [agentic-development, subagents, planning, spec-quality, visual-communication]
author: Jesse Vincent
url: https://blog.fsck.com/2026/03/09/superpowers-5/
date: 2026-03
---

# Superpowers 5: AI Coding Agent Evolution

**Author:** Jesse Vincent
**Published:** March 2026
**URL:** [blog.fsck.com](https://blog.fsck.com/2026/03/09/superpowers-5/)

## Summary

The fifth installment in the "Superpowers" series documents the author's evolving approach to agentic software development. The central theme is **maturation** — moving from ad hoc AI pair programming toward disciplined, structured workflows that emphasize planning rigor, visual collaboration, and proper task decomposition.

The article presents several practical breakthroughs. Visual communication replaces ASCII art: instead of agents generating unhelpful text diagrams, they create browser-based HTML mockups. Planning quality improves through adversarial subagent review — a dedicated review layer validates that specification documents are complete before implementation begins, eliminating costly "TBD" placeholder failures downstream.

The most significant architectural insight is the **subagent-driven development model**: a planning agent creates detailed specifications, then cheaper/faster models (like Claude Haiku) handle implementation. This cascading approach — spec → implementation → code review — enforces consistent architectural thinking while reducing cost.

## Key Claims

- **Visual communication over ASCII art:** Agents should generate browser-based mockups, not text diagrams. The principle: "Why am I doing this?" — recognize when to delegate rather than iterate on agent output
- **Planning quality requires adversarial review:** Agents frequently leave "TBD" placeholders in specs, causing downstream failures. A subagent review layer catches these before implementation begins
- **Subagent delegation substantially outperforms single-session approaches** — detailed plans enable cheaper models to handle implementation effectively
- **Software engineering fundamentals still apply:** Interface-driven design, single responsibility, and file structure planning must precede task breakdown
- **Large files are design problems, not style problems** — a sign that decomposition was insufficient
- **The cascade pattern:** specification → implementation → code review, enforcing architectural consistency throughout

## Connections

- The patterns in this post ship as an installable framework — see [[superpowers|Superpowers (obra/superpowers)]]
- Operates at approximately [[five-levels-shapiro|Shapiro Level 3-4]] — the developer manages agents rather than writing code
- The planning-first approach aligns with [[spec-driven-development]] — specs precede and drive all implementation
- The subagent model relates to [[12-factor-agents]] principle of "Small, Focused Agents"
- The adversarial review pattern could be a key practice for the Level 2 → Level 3 transition identified in [[five-levels-shapiro]]
- Connects to [[code-legibility-debate]] — with good specs and review, direct code reading becomes less necessary

## Questions Raised

- How does the adversarial review pattern scale to very large specifications?
- What's the error rate of the subagent implementation approach vs. single-agent?
- Does the cascade pattern work for all types of software, or mainly for greenfield features?
- How do you handle cases where implementation reveals spec-level design flaws?
