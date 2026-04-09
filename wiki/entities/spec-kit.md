---
title: Spec Kit (GitHub)
type: entity
pillar: spec-driven
created: 2026-04-08
updated: 2026-04-08
sources: [ai-in-sdlc-research]
tags: [tool, framework, spec-driven, github, open-source]
---

# Spec Kit

## Overview

**Spec Kit** is an open-source toolkit from GitHub that guides developers through specification creation, planning, and execution using AI coding agents. It implements a structured pipeline: specify → plan → tasks → implement.

**Company:** GitHub
**Website/Blog:** [Spec-driven development with AI (GitHub Blog)](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/)
**Repository:** [github.com/github/spec-kit](https://github.com/github/spec-kit)

## Workflow

Spec Kit follows a four-stage pipeline:

```
/specify → /plan → /tasks → /implement
```

1. **Specify** — create a structured specification with requirements, acceptance criteria, and constraints
2. **Plan** — generate an implementation plan from the spec
3. **Tasks** — break the plan into discrete, actionable tasks
4. **Implement** — AI agents execute tasks against the spec

## Relevance

Spec Kit is significant to this research because:

1. **GitHub's official SDD framework** — signals that the platform behind Copilot is investing in structured development
2. **Open source** — available for community adoption and extension
3. **Used in practitioner observation** — the author of [[ai-in-sdlc-research]] applied Spec Kit (alongside [[bmad-method]]) in a production SaaS team with positive results
4. **Compared with [[bmad-method]] and [[kiro]]** as one of three emerging SDD frameworks
5. **Complements Copilot** — moves GitHub's AI story from autocomplete (Copilot) to structured agent workflows

## Key Claims

From [[ai-in-sdlc-research]]:
- Spec Kit "guides developers through specification creation, planning, and execution using AI coding agents"
- Part of the practitioner observation: when combined with BMAD for strategic planning, Spec Kit provided tactical execution that reduced hallucination-driven rework

From [[bmad-method]] comparison:
- Mid-size project scope
- Rigid workflow (specify → plan → tasks → implement)
- Quick setup time (minutes)
- Not optimized for brownfield

## Hybrid Model (Spec Kit + BMAD)

A notable approach documented in [[bmad-method]]:

1. **Phase 1 — Strategic Planning (BMAD):** BA and Architect agents create PRD, system design, user stories
2. **Phase 2 — Feature Implementation (Spec Kit):** `/specify → /plan → /tasks → /implement` for each story
3. **Phase 3 — QA & Integration (BMAD):** QA Agent reviews against acceptance criteria

## Open Questions

- What is the optimal project size/type for Spec Kit vs. BMAD vs. Kiro?
- How does Spec Kit handle evolving requirements mid-implementation?
- What is the adoption rate among GitHub Copilot users?
- Can the pipeline stages be customized or extended?

## Links

- [[spec-driven-development]] — the methodology Spec Kit implements
- [[bmad-method]] — complementary framework (strategic planning + Spec Kit tactical execution)
- [[kiro]] — compared in SDD framework landscape
- [[github-copilot]] — same company; Copilot = autocomplete, Spec Kit = structured SDD
- [[ai-in-sdlc-research]] — cited and used in practitioner observation
- [[automation-levels]] — enables Level 3-4 workflows
