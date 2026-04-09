---
title: Spec-Driven Development
type: concept
pillar: spec-driven
created: 2026-04-08
updated: 2026-04-08
sources: [five-levels-shapiro, superpowers-5, 12-factor-agents, ai-in-sdlc-research]
tags: [specifications, automation, code-generation, methodology, vibe-coding]
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
- **[[spec-kit|Spec Kit]]** — GitHub's open-source toolkit implementing a `specify → plan → tasks → implement` pipeline. Mid-size project scope. Quick setup (minutes). Used in practitioner observation alongside BMAD.
- **[[kiro|Kiro]]** — AWS agentic development environment that converts informal prompts into structured specs and production-ready workflows. Feature-level scope. Major cloud vendor backing validates the SDD approach.

## Current Understanding

Spec-driven development appears to be the **enabling methodology for reaching Shapiro Level 4+**. The pattern is consistent across sources:

1. Human writes detailed specifications
2. AI agent(s) implement from specs
3. Tests validate the implementation
4. Human reviews at the spec level, not the code level

The [[superpowers-5]] adversarial review pattern adds a crucial quality gate: specs themselves must be validated for completeness before implementation begins. "TBD" placeholders in specs cause cascading failures.

The [[12-factor-agents]] perspective adds nuance: even in spec-driven workflows, you need to "own your control flow" and "own your context window." Specs are a form of context management for the LLM.

## Vibe Coding: The Unstructured Alternative

The term **vibe coding** was popularized by Andrej Karpathy (Feb 2025) to describe a workflow where developers rely heavily on AI-generated code by "following the vibes" — interacting with AI using informal prompts and iteratively adjusting output until the system appears to work. Vibe coding can be effective for **rapid prototyping and learning**, but it introduces risks:

- Weak documentation and lack of repeatability
- Hidden security vulnerabilities
- Increased technical debt
- No traceability between requirements and implementation

SDD and vibe coding represent a **fundamental bifurcation** in AI-assisted development. Per [[ai-in-sdlc-research]], organizations are likely to maintain **dual-track workflows**: vibe coding for exploration and proof-of-concept, SDD for production features — with governance rigor scaling to the risk and durability of the deliverable.

## Practitioner Evidence

### SDD in a Production SaaS Environment (from [[ai-in-sdlc-research]])

The author applied SDD practices ([[spec-kit|Spec Kit]] + [[bmad-method|BMAD]]) as a tech lead on a five-person team at a project portfolio management SaaS company. Prior workflow relied on IDE-level autocomplete ([[github-copilot|Copilot]]) and ad-hoc prompting (closer to vibe coding).

After introducing structured specifications, three observable changes emerged:

1. **Improved task scoping** — specifications with clear inputs, outputs, acceptance criteria, and constraints produced more focused AI output rather than broad, loosely connected scaffolding
2. **Reduced hallucination-driven rework** — under ad-hoc prompting, AI frequently referenced nonexistent methods or made incorrect API assumptions; specs constrained the generation context and reduced these errors
3. **Increased code consistency** — output across different features and team members became more predictable in structure and style, reducing cognitive load during review and simplifying onboarding

**Caveat:** Single-team observation, not a controlled study. However, aligns with the broader SDD literature: structured specifications reduce ambiguity, improve traceability, and give AI systems more reliable targets.

## Open Questions

- What makes a good spec for AI consumption vs. human consumption? Are they different?
- How do you handle emergent requirements that only become clear during implementation?
- What's the right granularity for specs? Too high-level and the AI makes bad decisions; too detailed and you're basically writing pseudocode
- How do spec-driven approaches handle legacy codebases where no spec exists?
- What's the relationship between specs and tests? Can one be generated from the other?
- Is the dual-track model (vibe coding for exploration, SDD for production) stable long-term, or will one approach dominate?
- How do you measure ROI of SDD vs. vibe coding in a controlled setting?

## Related Concepts

- [[software-factory]] — spec-driven development is likely a prerequisite for software factories
- [[automation-levels]] — enables Level 4+ in Shapiro's framework
- [[code-legibility-debate]] — if specs are the source of truth, do you need to read code?
- [[human-in-the-loop]] — the human's role shifts from coder to spec writer/reviewer
