---
title: "Building an AI Dark Factory: A Codebase That Writes Its Own Code, Live"
type: source
pillar: software-factories
created: 2026-04-16
updated: 2026-04-16
sources: [cole-medin-ai-dark-factory.md]
tags: [dark-factory, software-factory, cole-medin, live-stream, self-writing-code, context-engineering, level-5, pending-transcript]
---

# Building an AI Dark Factory: A Codebase That Writes Its Own Code, Live

## Metadata

- **Speaker:** [Cole Medin](https://www.youtube.com/@ColeMedin) — founder of Dynamous AI, AI educator and content creator, author of Microsoft Learn "Learn with Cole Medin" series
- **Format:** YouTube Live stream (~2h 24m)
- **Video:** https://www.youtube.com/live/Xg0tNz9pICI
- **Raw transcript:** `raw/youtube-transcripts/cole-medin-ai-dark-factory.md` *(metadata only — auto-captions could not be retrieved from this environment; see file for manual-ingest instructions)*
- **Pillar:** Software Factories

## Pending Transcript

> **Status (2026-04-16):** The auto-generated transcript has **not yet been ingested**. YouTube's IP blocks and public transcript mirrors' rate limits prevented automated retrieval from this environment. This page currently captures only what's inferable from the **title**, the **channel**, and the wiki's existing research context. It will be expanded into a full source summary (Summary, Key Claims, Connections, Questions Raised) once the transcript is pasted into `raw/youtube-transcripts/cole-medin-ai-dark-factory.md`.

## Why This Source Matters (pre-transcript)

The title — **"Building an AI Dark Factory: A Codebase That Writes Its Own Code, Live"** — places this source squarely inside the wiki's **[[software-factory]]** pillar. "Dark Factory" is the term Dan Shapiro uses for [[five-levels-shapiro|Level 5]] of his maturity model: a fully autonomous software production system where *no human looks at the code*, by analogy to Fanuc's lights-out robot factories. The live-stream framing ("a codebase that writes its own code, live") suggests Cole is demonstrating an actively running autonomous build system on camera — not just talking about one.

As of April 2026, the wiki's Software Factory evidence comes from three directions:

- **Shapiro's aspirational framing** ([[five-levels-shapiro]]) — Level 5 is the end-state; he claims only very small teams have reached it.
- **Huntley's Ralph-Loop maximalism** ([[everything-is-a-ralph-loop]]) — extends the ladder to Level 8–9 (evolutionary self-healing software). The wiki's strongest "it's here now" position.
- **Dex's counterweight** ([[dex-rpi-to-crispy]], [[matt-pocock-dex-horthy-chat]]) — "not the right final answer for production software … aim for 2-3×, not 10×."

A **live, on-stream** Dark Factory build from a well-known AI educator is a different genre of evidence: closer to a reproducible demo than to a manifesto or a talk, and from a creator explicitly aimed at *mainstream* AI developer audiences rather than at the HumanLayer/Huntley enterprise-frontier corner of the debate. Once the transcript is in, this source is expected to test several open questions:

1. **Does the demo actually reach Level 5**, or does it rely on human interventions that qualify it as Level 3–4?
2. **What harness / loop pattern** does Cole use? Ralph-style? Multi-agent cascade ([[superpowers-5]])? BMAD-style personas?
3. **What verification layer** keeps the self-writing codebase from producing slop? Tests? Adversarial review? Learning tests?
4. **What's the scope** — greenfield TODO app, or a real brownfield codebase? (This is the "complexity valley-of-death" question.)
5. **How does Cole's framing compare** to Simon Willison's Feb 2026 write-up of StrongDM's Dark Factory (referenced in web search results)?

## Connections (expected, based on title + channel)

- **[[software-factory]]** — direct contribution; likely candidate for citation in the concept page once transcript is in.
- **[[five-levels-shapiro]]** — "Dark Factory" is Shapiro's Level-5 term; this video may explicitly reference the ladder or implicitly operate at that level.
- **[[everything-is-a-ralph-loop]]** — the orchestration pattern most likely to underpin a live self-writing codebase demo.
- **[[automation-levels]]** — once the transcript is ingested, the demo should be placeable on the ladder.
- **[[context-engineering]]** — Cole Medin's prior work on Microsoft Learn and his talks (e.g., gitnation "Advanced Claude Code Techniques: Agentic Engineering With Context Driven Development") emphasize context engineering as the core discipline; expect this to appear.
- **[[code-legibility-debate]]** — "a codebase that writes its own code" is the strong-form "don't read the code" position. Interesting counterweight to Dex's reversal.
- **[[spec-driven-development]]** — if the factory accepts specs-in-working-software-out, SDD is likely the input mechanism.

## Questions Raised (pre-transcript)

1. Is "Dark Factory" being used in Shapiro's precise sense, or more loosely as a marketing term?
2. What prevents the self-writing codebase from diverging into slop across iterations? (cf. Dex's "Ralph is back" 20k-LOC cautionary PR in [[matt-pocock-dex-horthy-chat]])
3. How does Cole's demo compare to **StrongDM's** Dark Factory described in Simon Willison's Feb 2026 write-up ("no human even looks at the code")?
4. Given Cole's context-engineering emphasis, does he treat Dark Factory as an evolution of context engineering, or as a *departure* from it (toward loop engineering)?
5. Is the demo reproducible, or is it a curated artifact like Huntley's `cursed-lang` runs?

## Next Steps

1. **Ingest transcript** — paste auto-captions into `raw/youtube-transcripts/cole-medin-ai-dark-factory.md` (instructions in that file).
2. **Expand this page** — add Summary, Key Claims, and confirmed Connections sections once transcript is available.
3. **Consider creating `entities/cole-medin.md`** — if the transcript makes clear he's authoring a specific named framework or repo.
4. **Update [[software-factory]]** — cite this source alongside [[five-levels-shapiro]] and [[everything-is-a-ralph-loop]] once ingested.
5. **Cross-reference [[code-legibility-debate]]** — Dark Factory is, by definition, the "no one reads the code" end of that debate.
