---
title: Kiro
type: entity
pillar: spec-driven
created: 2026-04-08
updated: 2026-04-08
sources: [ai-in-sdlc-research]
tags: [tool, ide, spec-driven, aws, agentic]
---

# Kiro

## Overview

**Kiro** is an agentic development environment focused on turning prompts into structured specifications and production-ready implementation workflows. It bridges the gap between informal AI prompting and structured spec-driven development.

**Company:** AWS (Amazon)
**Website:** [kiro.dev](https://kiro.dev/)

## Relevance

Kiro is significant to this research because:

1. **Major cloud vendor backing SDD** — AWS investing in spec-driven development validates the approach
2. **Agentic environment** — goes beyond autocomplete to structured spec → implementation pipelines
3. **Bridges vibe coding and SDD** — designed to convert informal prompts into formal specs
4. **Compared with [[bmad-method]] and [[spec-kit]]** in [[ai-in-sdlc-research]] as one of three emerging SDD frameworks

## Key Claims

From [[ai-in-sdlc-research]]:
- Kiro is an "agentic environment focused on turning prompts into structured specs and production-ready implementation workflows"
- Represents the trend toward tooling that enforces specification discipline

From [[bmad-method]] comparison:
- Feature-level scope (vs. BMAD's enterprise scope or Spec-kit's mid-size scope)
- Rigid workflow pipeline
- Average brownfield support

## Open Questions

- How does Kiro's spec format compare to CodeSpeak's `.cs.md` and BMAD's PRD/Architecture docs?
- What is the adoption trajectory — is AWS promoting this within its ecosystem?
- How does Kiro handle brownfield/legacy codebases?
- What is the actual developer experience compared to [[spec-kit]] and [[bmad-method]]?

## Links

- [[spec-driven-development]] — the methodology Kiro embodies
- [[bmad-method]] — compared in SDD framework landscape
- [[spec-kit]] — compared in SDD framework landscape
- [[ai-in-sdlc-research]] — cited as SDD framework
- [[automation-levels]] — enables Level 3-4 workflows
