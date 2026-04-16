---
title: "Your intent is everything: Reconstructing specs from vibe coding sessions"
type: source
pillar: spec-driven
created: 2026-04-16
updated: 2026-04-16
sources: [codespeak-vibe-takeover]
tags: [codespeak, takeover, brownfield, vibe-coding, intent, claude-code-sessions, shrink-factor, byok, prompt-caching, version-0.3.6]
author: Andrey Breslav (CodeSpeak)
url: https://codespeak.dev/blog/vibe-takeover-20260317
---

# Your intent is everything: Reconstructing specs from vibe coding sessions

## Metadata

- **Author:** Andrey Breslav (CodeSpeak team)
- **URL:** https://codespeak.dev/blog/vibe-takeover-20260317
- **Date:** 2026-03-17
- **Version announced:** CodeSpeak 0.3.6
- **Format:** Product release announcement on CodeSpeak blog
- **Raw file:** `raw/codespeak-vibe-takeover.md`
- **Pillar:** [[spec-driven-development]]

## Summary

This is the **chronological predecessor** to [[codespeak-modular-takeover]] — the March 17, 2026 post from CodeSpeak that first introduces the "takeover reads Claude Code sessions" capability. Without this step, the April modular-takeover release wouldn't have been possible: the session-reading primitive is what makes multi-spec decomposition accurate, because it gives CodeSpeak access to the **intent history** (corrections, dead ends, user answers to `AskUserQuestion`) that shaped the code. The post by Andrey Breslav is also the most direct **philosophical manifesto** in the CodeSpeak corpus to date — the tagline "human intent is what matters" is declared and defended here, and the maximalist long-term goal is stated unambiguously: *"Our goal is to eventually build a world where you don't need to look at the code at all, even to review it."*

The core argument has two parts. First, vibe coding is repositioned as a legitimate first phase — *"great for exploration, ideation, for prototyping, for going from a vague feeling of 'what if we try something like this' to having a clear understanding"* — not a competitor to SDD. The post explicitly names its function: *"dialog-based coding agents are good tools for **intent elicitation** and **exploration**."* Second, the *"annoying gap"* after vibe sessions is characterized concretely: you're left with a working prototype plus a *long* chat history — *"scattered across many messages, some of which are corrections to the previous ones, some are dead ends, some make no sense out of context, and some are just answers to `AskUserQuestion` tool."* Takeover's job is to mine this history and produce specs that preserve the intent.

The post provides the **first quantified shrink claim** in the CodeSpeak canon: *"Specs are often 5-10 times shorter."* This number later gets empirical backing in [[codespeak-modular-takeover|Folio (~7×) and Faker (9.9×)]], but the claim is established here first, stated as a rough rule-of-thumb from usage rather than as a case-study result. It's also the first public documentation of scale: a single subsystem (`src/app/my-subsystem`) takeover processed **24 Claude Code sessions with 150 prompts**. This is realistic vibe-coding volume — not a toy demo.

The release is **0.3.6**, confirming that the wiki's prior "Alpha v0.0.1" framing for CodeSpeak was dated. Three concrete product artifacts ship: (1) session-reading takeover with opt-in permission flow stored in `~/.codespeak/preferences.json`, (2) language-agnostic `codespeak coverage` using universal LCOV format (previously Python-only) with auto-detection of test framework and `--target 100 --max-iterations 5` style autonomous test generation, and (3) Anthropic-compatible provider support via `ANTHROPIC_BASE_URL` (z.ai example given; security-constrained via whitelist). Supporting changelog items: **prompt caching enabled**, default model bumped to **Claude Sonnet 4.6**, spec files protected from accidental overwrites, `.codespeak` snapshot folder, **opt-in cost cap per build**.

The explicitly listed limitations at this version (March 17) are the most honest technical admission in the CodeSpeak corpus. Session-reading takeover **at this version** cannot: generate more than one spec file (solved by modular takeover three weeks later), support non-Claude-Code agents (still open), guarantee spec completeness, guarantee delete-code-regenerate equivalence, or verify that spec-diffs produce adequate code-diffs. Reading this alongside the April modular-takeover post shows a **visible three-week engineering cycle**: the single-spec limitation listed here as "to be fixed" is solved by the web wizard approach announced April 8.

## Key Claims

- **"Human intent is what matters."** The post's philosophical core. Reframes LLM utility as gap-filling against human-defined intent, not autonomous decision-making: *"many things that have always been obvious to humans are now obvious to machines as well."* Position is structurally opposite to [[everything-is-a-ralph-loop|Huntley's]] "software development is dead" framing — CodeSpeak says intent is irreducibly human, machines are executors.

- **Vibe coding is an intent-elicitation tool, not a coding tool.** Sharpest articulation of vibe coding's legitimate role in any wiki source: *"dialog-based coding agents are good tools for intent elicitation and exploration."* Prototype + chat history is an artifact of thinking, not the end product. Compare to [[ai-in-sdlc-research|ai-in-sdlc-research's]] dual-track thesis — the post operationalizes one interpretation of it.

- **5-10× shrink factor, stated as empirical rule.** *"Specs are often 5-10 times shorter, because they are more high-level."* The first time this number appears in a CodeSpeak publication. Validated later by Folio (~7×) and Faker (9.9×) per [[codespeak-modular-takeover]] and [[codespeak]].

- **Maximalist code-legibility position.** *"Our goal is to eventually build a world where you don't need to look at the code at all, even to review it."* **The strongest School-1 statement in the wiki** ([[code-legibility-debate]]) — stronger than anything Shapiro or Huntley have published. Note: stated as *"goal,"* hedged with *"story for another day,"* but the direction is unambiguous.

- **Scale datapoint: 24 sessions / 150 prompts per subsystem.** The first public datapoint on vibe-session volume in the wiki. Implication: a single coherent subsystem absorbs tens of sessions and low hundreds of prompts of intent. Context-budget implications for takeover: compressing 150-prompt history into one spec is a meaningful context-engineering problem.

- **Session history as first-class source material.** Takeover pre-March read code only; this version reads Claude Code sessions. The insight: *"The history **contains** all the intent that you have formulated, but it's scattered across many messages."* Code + session-history > code alone for intent reconstruction. This is the primitive that [[codespeak-modular-takeover|modular takeover]] later builds on.

- **Opt-in permission flow for session access.** `~/.codespeak/preferences.json` stores per-project consent. Three-state choice (Allow / Not now / **No, never**). Privacy-by-design, not just privacy-by-policy. Rare in AI developer tools.

- **Language-agnostic coverage via LCOV.** `codespeak coverage --auto-configure` detects language + framework; `codespeak coverage --target 100 --max-iterations 5` autonomously adds missing tests. Test-generation tightly integrated with spec pipeline — tests are part of the spec→code→verify loop, not a separate concern.

- **Anthropic-compatible providers via `ANTHROPIC_BASE_URL`.** Whitelisted for security. Example: `z.ai`. Sign that CodeSpeak is hedging against pure Anthropic lock-in — but not fully — compatible API still required.

- **Prompt caching + default model bump to Sonnet 4.6 + cost cap.** Three operational cost-control mechanisms landing simultaneously. Signals that CodeSpeak usage at scale was producing uncomfortable bills; cost engineering is a product priority.

- **Honest limitation list.** *"Make sure that if we delete the code, an equivalent implementation can be generated from the spec"* is listed as a **goal, not a guarantee**. This admits the fundamental risk of strict-SDD: if spec→code isn't deterministic, "the spec is source of truth" is partially aspirational. Honesty about this is noteworthy.

## Connections

- **[[codespeak]]** — Primary entity this source describes. Version 0.3.6 is documented here. Changelog items (prompt caching, Sonnet 4.6 default, cost cap, `.codespeak` folder) should be reflected in the entity's CLI/Operational notes.

- **[[codespeak-modular-takeover]]** — **Direct predecessor**. This post's stated limitation *"support generating more than one spec file"* is exactly the problem solved by modular takeover (April 8, 21 days later). Together these two sources document CodeSpeak's brownfield-SDD arc in 2026.

- **[[spec-driven-development]]** — Provides the sharpest articulation yet of vibe coding as *intent-elicitation*, not coding. This belongs in the Vibe Coding subsection of the concept page.

- **[[code-legibility-debate]]** — **Strongest School-1 statement** recorded in the wiki: *"build a world where you don't need to look at the code at all, even to review it."* Counterweight to [[dex-rpi-to-crispy|Dex's reversal]]. The debate now has a clear polar pair: Dex ("please read the code") vs. Breslav ("you shouldn't need to").

- **[[software-factory]]** — Maximalist code-legibility goal = Shapiro Level 5 territory. CodeSpeak frames this as *"a story for another day,"* which is the most restrained articulation of a Level-5 aspiration in the wiki.

- **[[context-engineering]]** — The 150-prompt session-history compression problem is a concrete context-engineering case. Prompt caching as mitigation is noted. Relates to [[instruction-budget]]: the spec that takeover produces must itself respect instruction-budget constraints when used for `codespeak build`.

- **[[sdd-course-deeplearning-ai]]** — [[sdd-course-deeplearning-ai|Paul Everett's course]] Lesson 11 teaches brownfield as a **manual conversation pattern** with the agent. CodeSpeak's session-reading takeover is the **automated primitive** for the same transformation. Two points on the same spectrum: Everett = pedagogical, manual; CodeSpeak = product, automated.

- **[[bmad-method]]** — BMAD's four-phase cycle (Analysis → Planning → Solutioning → Implementation) has no direct equivalent of vibe-session takeover. A BMAD user entering a brownfield project re-analyzes via the Mary persona; a CodeSpeak user runs `takeover`. Different theories of how brownfield migration should happen — human-led analysis vs. machine-led intent extraction.

- **[[everything-is-a-ralph-loop]]** — Philosophical opposite. Huntley: software development is dead, the loop writes code. Breslav: *"human intent is what matters"* — the spec (authored by a human, helped by an agent) is the irreducible artifact.

## Questions Raised

1. **What's the actual algorithm for mining 150-prompt session histories?** The post says takeover *"reads Claude Code sessions, picking up context from prior coding work,"* but doesn't describe the strategy. Is each prompt scored for intent-signal? Are corrections weighted? Are dead ends filtered? This matters for failure mode analysis.

2. **Does session-reading respect token budgets?** A 150-prompt history compressed into one spec faces [[instruction-budget]] constraints on the analysis side. The post mentions prompt caching but not whether session analysis itself fits in a single Sonnet call or requires multi-pass strategies.

3. **What's the spec's fidelity guarantee?** The post explicitly lists *"make sure that the spec doesn't miss anything important and doesn't include anything unnecessary"* as a future goal — i.e., current takeover may over- or under-specify. How would a user know?

4. **What happens to the spec when multiple developers' sessions are involved?** Team development generates intent across multiple humans' sessions. Does takeover distinguish between authors? Synthesize disagreements? Flag inconsistencies?

5. **The opt-out preference (`D: No, never`) is important.** Does takeover fall back to code-only analysis cleanly? Is there a quality delta between code+session and code-only modes?

6. **`~/.codespeak/preferences.json` is global but per-project.** How does this interact with CI/CD automation? With shared machines? With session histories belonging to other developers?

7. **What's the relationship between session-reading and `codespeak-dev/vibe-sharing`** (repo launched April 15, one month after this post)? Is user-donated session data being used to train better takeover models? If yes, what's the privacy model?

8. **`codespeak coverage --target 100 --max-iterations 5` is autonomous test generation.** What safeguards prevent low-quality tests that inflate coverage without catching real bugs (the classic "assertion-free test" failure mode)?

9. **"You don't need to look at the code at all, even to review it"** — is this plausible at current model capability? [[dex-rpi-to-crispy|Dex's reversal]] argues no. At what capability threshold does CodeSpeak's position become defensible? And what happens in regulated domains?
