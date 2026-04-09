---
title: "Everything We Got Wrong About RPI — From RPI to CRISPY (QRSPI)"
type: source
pillar: coding-agents
created: 2026-04-08
updated: 2026-04-08
sources: [dex-rpi-to-crispy-coding-agents.md, dex-rpi-to-crispy.md, extracted_text.txt, "slides/From RPI to QRSPI - text.md"]
tags: [rpi, crispy, qrspi, methodology, code-legibility, context-engineering, instruction-budget, humanlayer, dex]
---

# Everything We Got Wrong About RPI — From RPI to CRISPY (QRSPI)

## Metadata

- **Author:** Dex (dexhorthy), HumanLayer
- **Event:** Coding Agents Conference 2026, March 3, Computer History Museum
- **Format:** Conference talk (transcript + slides)
- **Raw files:** `raw/youtube-transcripts/dex-rpi-to-crispy-coding-agents.md`, `raw/youtube-transcripts/dex-rpi-to-crispy.md`, `raw/slides/extracted_text.txt`, `raw/slides/From RPI to QRSPI - text.md`
- **Videos:** https://youtu.be/YwZR6tc7qYg, https://www.youtube.com/watch?v=5MWl3eRXVQk (Limbic Systems channel)

## Summary

Dex, creator of [[12-factor-agents]] and co-founder of [[humanlayer]], delivers a remarkably honest retrospective on the **Research/Plan/Implement (RPI)** methodology he popularized in 2025. RPI was widely adopted (10,000+ users, from startups to Fortune 500s), but when rolled out to teams beyond expert users, it consistently failed. Dex admits to three key errors: telling people not to read the code, advocating for reading long plan files, and tolerating "a little slop."

The core problem was that RPI's single monolithic `/create_plan` prompt contained **85+ instructions**, exceeding the ~150-200 instruction budget that frontier LLMs can reliably follow. This meant the workflow required "magic words" — specific phrasing like "work back and forth with me starting with your open questions and outline" — to trigger the interactive planning behavior. Experts discovered these incantations through experience; most engineers didn't.

The fix is **CRISPY** (also referred to as **QRSPI** — Questions, Research, Structure, Plan, Implement — in slide versions of the talk) — a decomposition of RPI into focused stages: **Questions → Research → Design → Structure → Plan → Worktree → Implement → PR**. Each stage uses its own context window with under 40 instructions, respecting the instruction budget. The key innovation is splitting planning into a **design discussion** (~200 lines, "where are we going?") and a **structure outline** (~300 lines, "how do we get there?"), giving engineers a high-leverage review point before the full plan (~1000 lines) and code (~1000 lines) are generated.

The slide version of the talk also names the upper 40% of the context window the **"Smart Zone"** (complementing the "Dumb Zone" concept) and frames the artifact-based workflow as enabling **"Mental Alignment"** — shared ground between the human and the agent through Questions, Research, and Outline artifacts.

Most significantly, Dex **reverses his position on code legibility**: after six months of not reading code, they "had to rip out and replace large parts of that system." His new advice is unequivocal: "Please I'm begging you please read the code. We have a profession to uphold."

## Key Claims

- **RPI failed at scale because of instruction budget overflow.** A single prompt with 85+ instructions, plus CLAUDE.md, system prompt, tools, and MCPs, leads to inconsistent workflow adherence. Frontier LLMs follow ~150-200 instructions reliably (citing arxiv paper 2507.11538).
- **"Magic words" are a tool design failure.** If a tool requires specific incantations to work correctly, the tool is broken. "This isn't the user's fault... go fix the tool."
- **Research must be kept objective.** When the model knows what you're building, research produces opinions instead of facts. Fix: hide the ticket from the research context window; use separate "query planning" and "research execution" context windows.
- **Plans have no leverage.** ~1000-line plans produce ~1000 lines of code (within 10%). Reviewing the plan is the same work as reviewing the code. "Don't read the plans. Please read the code."
- **Design discussions provide 5x leverage.** A ~200-line design document captures current state, desired end state, patterns, resolved decisions, and open questions. Reviewing 200 lines that steer 1000+ lines of code is real leverage.
- **Structure outlines are "C header files."** Just signatures, new types, phase ordering — enough to see what the agent thinks without the full implementation detail.
- **Vertical plans beat horizontal plans.** Models default to horizontal plans (all DB, then all services, then all API) which produce 1200+ lines before anything works. Vertical plans give testable checkpoints.
- **Context engineering means smaller windows, not bigger ones.** The "dumb zone" starts around 40% context window usage. Less context = better results. Don't use prompts for control flow; use actual control flow.
- **2-3x is the right target, not 10x.** "10x speed doesn't matter if you're going to throw it all away in 6 months." Quality bottleneck is the real constraint.
- **Code legibility reversal:** "In August [2025] you said don't read the code... I was wrong." Six months of not reading code "did not end well." OSS projects (Beads, OpenClaw) can skip code review because the stakes are different; production SaaS cannot.
- **"No more slop" is the 2026 mandate.** "We have a profession to uphold."
- **Agent swarms are premature.** The bottleneck is your ability to ensure quality. Going 10x faster doesn't help if half is rework.

## Connections

- **[[code-legibility-debate]]** — This is the strongest data point yet for School 2 ("must read the code"). Dex went from a leading School 1 voice to an emphatic School 2 advocate based on 6 months of production experience.
- **[[12-factor-agents]]** — CRISPY is the practical evolution of 12-factor principles. Factor #8 ("Don't use prompts for control flow") is directly vindicated: the old RPI prompt *was* using prompts for control flow.
- **[[humanlayer]]** — CRISPY is being productized in CodeLayer IDE.
- **[[spec-driven-development]]** — The design discussion artifact shares DNA with spec-driven approaches, but Dex explicitly warns against outsourcing design decisions to the model.
- **[[automation-levels]]** — Dex implicitly argues that rushing to Level 4-5 without solving quality creates dangerous technical debt. His 2-3x target suggests Level 3 is the sweet spot for now.
- **[[context-engineering]]** — Major source for the concept. Two reads: "more information" vs. "better instructions and simpler tasks."
- **[[instruction-budget]]** — Primary source for this concept.

## Questions Raised

1. How do you measure the "2-3x" improvement empirically across a team?
2. Is CRISPY's seven-step process too complex for adoption? (Dex acknowledges: "3 steps was already a lot... now there are 7")
3. Will the instruction budget problem diminish as models improve, making monolithic prompts viable again?
4. Can the design discussion artifact become a standard for team alignment beyond just AI coding?
5. How does CRISPY interact with formal verification approaches (TLA+/TLA++) that could make code reading unnecessary?
