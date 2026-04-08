---
title: "Code Legibility Debate: Black Box vs. Must-Read"
type: concept
pillar: code-legibility
created: 2026-04-08
updated: 2026-04-08
sources: [five-levels-shapiro, superpowers-5, 12-factor-agents]
tags: [code-review, readability, specs-vs-code, two-schools, philosophy]
---

# Code Legibility Debate

## Definition

A fundamental divide in the AI-assisted development community: **should developers read AI-generated code, or treat it as a black box?**

**School 1 — "Code is a black box, read only the spec":**
The spec is the source of truth. If the tests pass and the spec is satisfied, the code's internal structure doesn't matter. Reading AI-generated code is a waste of time — you should focus on specs, tests, and behavior. This school argues that the code is an intermediate artifact, like compiled bytecode.

**School 2 — "You still have to read the code":**
Code is still the real artifact that runs in production. Specs can be incomplete, tests can miss edge cases, and AI-generated code can contain subtle bugs, security vulnerabilities, or architectural debt that only code review reveals. Treating code as a black box creates dangerous blind spots.

## Key Sources

- [[five-levels-shapiro]] — Implicitly supports School 1 at Level 4-5. At Level 4, "you leave for 12 hours and check if tests pass" — no mention of reading code
- [[superpowers-5]] — Mixed position. Emphasizes spec quality (School 1) but also enforces code review as a pipeline stage (School 2)
- [[12-factor-agents]] — Factor #8 ("Own Your Control Flow") implies you need to understand what the agent is doing — leans School 2

## Current Understanding

This is an **unresolved tension** in the field. The sources suggest it may not be a binary choice but a spectrum:

| Level | Code Reading | Primary Artifact |
|-------|-------------|-----------------|
| Level 1-2 | Read everything | Code |
| Level 3 | Review/skim | Code + Tests |
| Level 4 | Spot-check only | Spec + Tests |
| Level 5 | Never read | Spec + Tests |

**Arguments for School 1 (Black Box):**
- Reading AI-generated code doesn't scale — too much volume, too fast
- Specs + tests are a more reliable contract than code review
- Developers already don't read most code they depend on (libraries, frameworks)
- Shapiro's Level 4 workflow apparently works without code reading

**Arguments for School 2 (Must-Read):**
- Tests only cover known scenarios; code review catches unknown unknowns
- Security vulnerabilities, performance issues, and architectural debt require code-level inspection
- "Own your control flow" ([[12-factor-agents]]) implies you must understand the code
- Production debugging still requires reading code
- AI-generated code can be subtly wrong in ways tests don't catch

**Emerging synthesis:** Perhaps the answer depends on the **risk profile** of the code. Low-risk features can be black-boxed; high-risk (security, financial, safety-critical) still needs human code review.

## Open Questions

- Is there empirical data on bug rates in AI-generated code that passes tests but was never human-reviewed?
- Does code reading become more or less important as AI gets better?
- Are there intermediate approaches — e.g., AI-assisted code review where another AI reviews the code?
- How does this debate apply differently to greenfield vs. brownfield codebases?
- What's the liability/compliance angle? Can you ship code nobody has read?

## Related Concepts

- [[spec-driven-development]] — School 1 is essentially the spec-driven position
- [[software-factory]] — factories imply code is a black box
- [[automation-levels]] — higher levels imply less code reading
- [[human-in-the-loop]] — where exactly is the human if not reading code?
