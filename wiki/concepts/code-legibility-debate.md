---
title: "Code Legibility Debate: Black Box vs. Must-Read"
type: concept
pillar: code-legibility
created: 2026-04-08
updated: 2026-05-07
sources: [five-levels-shapiro, superpowers-5, 12-factor-agents, dex-rpi-to-crispy, coding-agents-conf-2026, sdd-course-deeplearning-ai, codespeak-vibe-takeover, agentic-coding-stack-aslan, lopopolo-openai-extreme-harness-engineering]
tags: [code-review, readability, specs-vs-code, two-schools, three-schools, philosophy, slop, trust, review-level, cognitive-debt, intent, traceability]
---

# Code Legibility Debate

## Definition

A fundamental divide in the AI-assisted development community: **should developers read AI-generated code, or treat it as a black box?**

**School 1 — "Code is a black box, read only the spec":**
The spec is the source of truth. If the tests pass and the spec is satisfied, the code's internal structure doesn't matter. Reading AI-generated code is a waste of time — you should focus on specs, tests, and behavior. This school argues that the code is an intermediate artifact, like compiled bytecode.

**School 2 — "You still have to read the code":**
Code is still the real artifact that runs in production. Specs can be incomplete, tests can miss edge cases, and AI-generated code can contain subtle bugs, security vulnerabilities, or architectural debt that only code review reveals. Treating code as a black box creates dangerous blind spots.

**School 3 — "Build the bridge so you can navigate spec ↔ code on demand" (emerging, [[agentic-coding-stack-aslan]]):**
A third position implied by Aslan's "missing link" framing. Don't pre-commit to either reading code or treating it as a black box — invest in **spec-to-code traceability infrastructure** so that for any given question, the reviewer can navigate from a requirement down to the specific symbols that implement it (and back from a code change to the requirements it touches). Reading then becomes a query response, not a default discipline. Closer to the "navigate-don't-read" stance than either pole. Today the *code-side* graph exists in tools like [[ctxo|Ctxo]]; the *spec-side* graph and the *bridge* are unbuilt.

## Key Sources

- [[five-levels-shapiro]] — Implicitly supports School 1 at Level 4-5. At Level 4, "you leave for 12 hours and check if tests pass" — no mention of reading code
- [[superpowers-5]] — Mixed position. Emphasizes spec quality (School 1) but also enforces code review as a pipeline stage (School 2)
- [[12-factor-agents]] — Factor #8 ("Own Your Control Flow") implies you need to understand what the agent is doing — leans School 2
- **[[dex-rpi-to-crispy]]** — ⚠️ **Major data point.** Dex reverses his August 2025 position. After 6 months of not reading code: "It did not end well. We had to rip out and replace large parts of that system." Now says: "Please I'm begging you to read the code. We have a profession to uphold." Draws a sharp line between OSS (acceptable to skip) and production SaaS (must read).
- **[[coding-agents-conf-2026]]** — Scott Breitenother (Kilo Code): "AI shifts the work, it doesn't remove it." Trust is the bottleneck, not capability. Scale AI: leading models score ~30% on codebase understanding. Both suggest code review remains essential because agents aren't reliable enough to go unsupervised.
- **[[sdd-course-deeplearning-ai]]** — **Mainstream middle-ground articulation.** Paul Everett's course explicitly distinguishes *what* to read. School-1-leaning: "focus your review on high-level concerns like whether the features work and reflect the spec, rather than details like which CSS classes were implemented" (Lesson 7). School-2-leaning: "just make sure it creates code that you can commit under your name" (Lesson 9) — i.e., you're still responsible for what you merge. The synthesis: **review at the spec/behavior level for most changes; reserve line-level reading for security, database, and anything that could compound later.**
- **[[codespeak-vibe-takeover]]** — **Strong School-1 statement.** Andrey Breslav (CodeSpeak): *"Our goal is to eventually build a world where you don't need to look at the code at all, even to review it."* Hedged as a future goal, but unambiguous in direction. Combined with the empirical 5-10× shrink factor between specs and code, CodeSpeak's position is that reading a 430-line spec is legitimately sufficient review for a 3000-line implementation. This is the polar opposite of [[dex-rpi-to-crispy|Dex's]] "please read the code."
- **[[lopopolo-openai-extreme-harness-engineering]]** — ⚠️ **The strongest production-grade School-1 datapoint in the wiki, beating CodeSpeak in commitment depth.** Where Breslav frames it as a future goal, Lopopolo's three-engineer team has *already* removed the read-the-code step from the merge path on a 1M-LOC production codebase shipping inside OpenAI Frontier: *"We've moved beyond even the humans reviewing the code… most of the human review is post-merge."* PR-author Codex and PR-reviewer Codex negotiate within prompts (P0/P1/P2 framework); merge is autonomous; humans sample post-merge to find what process knowledge is still missing. Direct counter-evidence to Dex's reversal — Dex's "6 months of not reading code → had to rip out and replace large parts of that system" vs. Lopopolo's "5 months of not reading code, 1M LOC, working." Both are 2026 production data points; they disagree fundamentally on whether post-merge review is sustainable. Caveat: Lopopolo's project is greenfield Electron (not deployed infrastructure); Dex's was production SaaS.
- **[[agentic-coding-stack-aslan]]** — **First clean articulation of School 3 (the traceability stance).** Aslan doesn't take sides in the black-box-vs-must-read debate; he names the missing infrastructure that would make either side's stance more honest. Four operational questions the bridge must answer (which symbols implement RQ-12, which tests cover this spec item, what breaks if requirement X changes, who else is touching this) give the School-3 position a concrete spec rather than a slogan.

## Current Understanding

The debate is now **actively contested** by competing 2026 production data points. Through Q1 2026 the trend was tilting toward School 2 based on Dex's reversal. **In May 2026, [[lopopolo-openai-extreme-harness-engineering|Lopopolo's article]] reset that trend** with a stronger School-1 datapoint (1M LOC, 5 months, post-merge review only, working) than the wiki had previously contained. The two cases are not directly comparable (greenfield Electron app vs. production SaaS) but they are both *operating production code at non-trivial scale*. The honest reading: **stakes and surface still matter, and there is no single winning position in May 2026.**

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
- ⚠️ **Lopopolo's OpenAI Frontier production case (May 2026):** 5 months, ~1M LOC, ~1,500 PRs, **0% human-authored code**, **post-merge review only**. Author-Codex ↔ reviewer-Codex negotiation within prompts; humans sample post-merge to find what process knowledge is missing and add lints/skills accordingly. Strongest School-1 production datapoint to date.

**Arguments for School 2 (Must-Read):**
- Tests only cover known scenarios; code review catches unknown unknowns
- Security vulnerabilities, performance issues, and architectural debt require code-level inspection
- "Own your control flow" ([[12-factor-agents]]) implies you must understand the code
- Production debugging still requires reading code
- AI-generated code can be subtly wrong in ways tests don't catch
- ⚠️ **Dex's production experience (2026):** 6 months of not reading code led to having to "rip out and replace large parts" of a production system. "No more slop" is his 2026 mandate.
- **Kilo Code data (25T tokens):** AI shifts cognitive load from doing to orchestrating — review is part of orchestration, not eliminated by it
- **Scale AI benchmarks:** Leading models score ~30% on codebase understanding tasks — they can't be trusted unsupervised

**Emerging synthesis:** The answer depends on **stakes and surface, not just risk profile**:
- **OSS / side projects / demos:** School 1 is viable. Stakes are lower, nobody gets paged at 3am.
- **Production SaaS / regulated / user-facing:** Contested. [[dex-rpi-to-crispy|Dex's reversal]] and Kilo Code's data point at School 2; [[lopopolo-openai-extreme-harness-engineering|Lopopolo's]] internal-product 1M-LOC datapoint (greenfield Electron, no continuous deployment, humans still cut release branches) shows School 1 working in 2026 with sufficient harness investment. The honest read: **the practitioner's harness sophistication may matter more than the abstract school they belong to.**
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
