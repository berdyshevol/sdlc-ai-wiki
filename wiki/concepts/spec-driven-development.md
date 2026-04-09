---
title: Spec-Driven Development
type: concept
pillar: spec-driven
created: 2026-04-08
updated: 2026-04-08
sources: [five-levels-shapiro, superpowers-5, 12-factor-agents]
tags: [specifications, automation, code-generation, methodology]
---

# Spec-Driven Development

## Definition

Spec-driven development is an approach where **formal specifications are the primary artifact**, and code is generated from them by AI agents. The human writes and maintains the spec; the AI writes and maintains the code. The spec becomes the source of truth — not the code.

This inverts the traditional relationship between documentation and code. Instead of code being written first and docs being (maybe) written after, the spec comes first and the code follows automatically.

## Key Sources

- [[five-levels-shapiro]] — Level 4 (Autonomous) is essentially spec-driven: "You leave for 12 hours, and check if tests pass"
- [[superpowers-5]] — The cascade pattern (spec → implementation → code review) is spec-driven in practice
- [[12-factor-agents]] — Factors #2-3 (own prompts/context) relate to spec management

## Tools and Frameworks

- **[[codespeak]]** — Spec-driven platform that generates full applications from markdown specs (`.cs.md` files) using Claude. GitHub-native with automatic commits. Notable for brownfield conversions of major OSS projects (faker, yt-dlp, beautifulsoup4). Alpha (v0.0.1).
- **[[bmad-method|BMAD method]]** — Multi-agent framework simulating a full Agile team with 12+ AI agent roles and 34+ workflows. Covers the entire SDLC from brainstorming to QA. Runs on top of Claude Code, Cursor, Windsurf.
- **Spec-kit** — A framework for spec-driven development (to be researched)
- **[[kiro]]** — AWS's spec-driven development tool (to be researched)

## Current Understanding

Spec-driven development appears to be the **enabling methodology for reaching Shapiro Level 4+**. The pattern is consistent across sources:

1. Human writes detailed specifications
2. AI agent(s) implement from specs
3. Tests validate the implementation
4. Human reviews at the spec level, not the code level

The [[superpowers-5]] adversarial review pattern adds a crucial quality gate: specs themselves must be validated for completeness before implementation begins. "TBD" placeholders in specs cause cascading failures.

The [[12-factor-agents]] perspective adds nuance: even in spec-driven workflows, you need to "own your control flow" and "own your context window." Specs are a form of context management for the LLM.

## Open Questions

- What makes a good spec for AI consumption vs. human consumption? Are they different?
- How do you handle emergent requirements that only become clear during implementation?
- What's the right granularity for specs? Too high-level and the AI makes bad decisions; too detailed and you're basically writing pseudocode
- How do spec-driven approaches handle legacy codebases where no spec exists?
- What's the relationship between specs and tests? Can one be generated from the other?

## Related Concepts

- [[software-factory]] — spec-driven development is likely a prerequisite for software factories
- [[automation-levels]] — enables Level 4+ in Shapiro's framework
- [[code-legibility-debate]] — if specs are the source of truth, do you need to read code?
- [[human-in-the-loop]] — the human's role shifts from coder to spec writer/reviewer
