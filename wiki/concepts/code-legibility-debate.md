---
title: "Code Legibility Debate: Black Box vs. Must-Read"
type: concept
pillar: code-legibility
created: 2026-04-08
updated: 2026-04-08
sources: [five-levels-shapiro, superpowers-5, 12-factor-agents, dex-rpi-to-crispy, coding-agents-conf-2026]
tags: [code-review, readability, specs-vs-code, two-schools, philosophy, slop, trust]
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
- **[[dex-rpi-to-crispy]]** — ⚠️ **Major data point.** Dex reverses his August 2025 position. After 6 months of not reading code: "It did not end well. We had to rip out and replace large parts of that system." Now says: "Please I'm begging you to read the code. We have a profession to uphold." Draws a sharp line between OSS (acceptable to skip) and production SaaS (must read).
- **[[coding-agents-conf-2026]]** — Scott Breitenother (Kilo Code): "AI shifts the work, it doesn't remove it." Trust is the bottleneck, not capability. Scale AI: leading models score ~30% on codebase understanding. Both suggest code review remains essential because agents aren't reliable enough to go unsupervised.

## Current Understanding

The debate is **tilting toward School 2** based on new production evidence. The strongest signal is Dex's reversal — a prominent School 1 advocate who tried "don't read the code" for 6 months in production and had to reverse course. This is no longer purely theoretical.

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
- OSS examples: Beads (300k+ lines Go, "never read"), OpenClaw — maintainers skip line-by-line review and it works

**Arguments for School 2 (Must-Read):**
- Tests only cover known scenarios; code review catches unknown unknowns
- Security vulnerabilities, performance issues, and architectural debt require code-level inspection
- "Own your control flow" ([[12-factor-agents]]) implies you must understand the code
- Production debugging still requires reading code
- AI-generated code can be subtly wrong in ways tests don't catch
- ⚠️ **Dex's production experience (2026):** 6 months of not reading code led to having to "rip out and replace large parts" of a production system. "No more slop" is his 2026 mandate.
- **Kilo Code data (25T tokens):** AI shifts cognitive load from doing to orchestrating — review is part of orchestration, not eliminated by it
- **Scale AI benchmarks:** Leading models score ~30% on codebase understanding tasks — they can't be trusted unsupervised

**Emerging synthesis:** The answer depends on **stakes, not just risk profile**:
- **OSS / side projects / demos:** School 1 is viable. Stakes are lower, nobody gets paged at 3am.
- **Production SaaS / regulated / user-facing:** School 2 is winning. Dex's reversal and Kilo Code's data both point here.
- **The leverage question:** Dex's CRISPY/QRSPI methodology offers a middle path — don't read the 1000-line *plan*, but DO read the code. Use 200-line *design discussions* as the high-leverage review point.
- **Mental Alignment:** The QRSPI slide framing emphasizes that artifacts (Questions, Research, Outlines) create "Mental Alignment" between human and agent — shared understanding that makes code review more effective because the reviewer already knows the intent.
- **Target 2-3x, not 10x:** Multiple speakers at the Coding Agents Conference 2026 converge on this — quality-constrained speedup is more sustainable than raw throughput.

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
