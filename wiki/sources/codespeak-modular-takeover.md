---
title: "Modular Takeover: from vibe-coded app to spec-driven development"
type: source
pillar: spec-driven
created: 2026-04-16
updated: 2026-04-16
sources: [codespeak-modular-takeover]
tags: [codespeak, takeover, brownfield, modular, spec-driven, vibe-coding, shrink-factor, web-wizard, folio]
author: Dmitry Savvinov (CodeSpeak)
url: https://codespeak.dev/blog/modular-takeover-20260408
---

# Modular Takeover: from vibe-coded app to spec-driven development

## Metadata

- **Author:** Dmitry Savvinov (CodeSpeak team)
- **URL:** https://codespeak.dev/blog/modular-takeover-20260408
- **Date:** 2026-04-08
- **Format:** Blog post (CodeSpeak product blog)
- **Demo repo:** `codespeak-dev/folio` (branch `modular-takeover`)
- **CLI:** `uv tool install codespeak-cli`
- **Raw file:** `raw/codespeak-modular-takeover.md` *(note: retrieved via Claude Code `WebFetch`, which is AI-processed — direct quotes preserved, non-quoted prose is close paraphrase)*
- **Pillar:** [[spec-driven-development]]

## Summary

**CodeSpeak's April 2026 modular-takeover release is the first documented off-ramp from vibe coding to SDD that preserves existing code.** This is a significant update to the [[codespeak]] entity page, which as of April 8 still described CodeSpeak as alpha v0.0.1 with primarily greenfield framing. The new feature — announced in this blog post by Dmitry Savvinov — directly addresses the most persistent open question in the wiki's SDD coverage: **can SDD work for codebases that weren't spec-driven from the start?** CodeSpeak's answer: yes, via a reverse-engineering step that decomposes an existing app into multiple focused specs through an interactive browser wizard.

The core claim is that vibe coding and SDD are not rival methodologies but **sequential phases**: vibe coding is good for exploration ("excels at … understanding what you want"), but fails on careful evolution because agent context resets and architectural decisions become implicit in implementation rather than documented. Modular takeover formalizes the transition: you vibe-code until the app works, then run `codespeak takeover`, iterate on the proposed module decomposition in a web wizard, confirm, and continue development spec-first. This is a sharper articulation of the [[ai-in-sdlc-research|dual-track thesis]] than any prior source — rather than treating vibe and SDD as parallel choices for different work, the post frames them as **stages in one pipeline** with CodeSpeak as the transition tool.

The post's empirical contribution is the **Folio case study**: a ~3,000-line Go dual-pane terminal file manager, vibe-coded over iterative sessions, decomposed by `codespeak takeover` into **four focused specs totaling 430 lines of Markdown — a ~7× shrink factor**. The four spec files cover: (1) core model, panels, context menu, settings, (2) filesystem operations and archive support, (3) theming and file formatting, (4) integrated terminal panel. Folio is a new demo project for this specific release; the GitHub org `codespeak-dev/folio` exists as of 2026-04-08.

The most interesting concrete example in the post is a **design decision that isn't visible in the code** — the terminal panel's keyboard passthrough rule: "only the following keys are handled by the application itself rather than forwarded to the terminal process: Ctrl+T, Ctrl+\\, Ctrl+Up, Ctrl+Down." The *why* is invisible from any individual file — you avoid intercepting F10 so that `htop` running inside the terminal works. In implementation code, this is a series of switch/case exclusions; in spec form, it's one sentence that documents intent. This is the **strongest Mental-Alignment example in the wiki outside of [[dex-rpi-to-crispy|Dex's]] theoretical framing** — a concrete demonstration that specs preserve information that code alone cannot.

The F7/mkdir example closes the loop: adding folder creation required **one function description in `file-ops.cs.md` and one row in the keybinding table in `app.cs.md`**. After `codespeak build`, the tool auto-generated the function implementation, keyboard handlers, input routing, and panel refresh logic. This is the Shapiro-Level-4 workflow operating in a brownfield context: spec edit → build → working code, no manual code writing. The post doesn't claim this is novel — CodeSpeak has had spec-to-code generation since v0.0.1 — but the significance is that it now works **on a previously vibe-coded codebase**, after takeover.

## Key Claims

- **Vibe coding and SDD are sequential phases, not rival methodologies.** Vibe coding is explicitly repositioned as a legitimate first phase for exploration, with takeover as the graduation step. This reframes the wiki's [[spec-driven-development#Vibe Coding: The Unstructured Alternative|prior dual-track thesis]] — instead of picking one or the other per task, use vibe for exploration, then takeover into SDD for evolution.

- **~7× shrink factor for Folio (2938 Go LOC → 430 MD lines across 4 specs).** Concrete empirical number. Combined with prior CodeSpeak shrink factors (Faker 9.9×, markitdown/yt-dlp/beautifulsoup4 in the 5.9–9× range), this gives the wiki its **first dataset of spec-vs-code size ratios**. The claim "specs are shorter than code" moves from theoretical to quantified.

- **Decomposition happens through an interactive web wizard, not automated assignment.** This is the key design choice distinguishing modular takeover from the February 2026 "monolithic takeover": the tool proposes a coarse initial structure, then hands control to the developer, who can request splits, merges, and rearrangements before confirming. The takeover is **human-gated at the module-boundary level** — the choice of "what belongs together" is not automated.

- **Specs preserve design intent that code cannot express.** The keyboard-passthrough example (Ctrl+T / Ctrl+\\ / Ctrl+Up / Ctrl+Down handled by app, F10 forwarded for `htop` compatibility) is the strongest concrete example of this claim in any wiki source. It's not a new principle — [[bmad-method-docs|BMAD's]] project-context.md and Dex's [[dex-rpi-to-crispy|Mental Alignment]] both argue this — but this is the first **worked code-level example** rather than abstract argument.

- **Post-takeover development is spec-only.** Adding a feature (F7 mkdir) required *zero* manual code writing — just one function description added to `file-ops.cs.md`, one row added to a keybinding table in `app.cs.md`, then `codespeak build`. This is the strict-SDD workflow operating **after** brownfield conversion — evidence that the takeover step doesn't just produce specs, it produces specs that actually function as source-of-truth for subsequent change.

- **Modular decomposition beats monolithic specs.** The February 2026 version of `codespeak takeover` produced a single monolithic spec file. The April 8 version produces **multiple focused specs** coupled via "Managed files" and spec dependencies (introduced in the March 9 blog post). This parallels conventional software engineering's move from monorepo-single-package to modular — and implicitly addresses the [[instruction-budget]] concern: multiple 100-line specs fit in context better than one 430-line monolith during build.

- **The `modular-takeover` branch on `codespeak-dev/folio` is a reproducible artifact.** Unlike many SDD claims in the wiki, this one is directly verifiable by `git clone`. The demo includes both the generated specs and the mkdir feature implementation.

## Connections

- **[[codespeak]]** — This post is a major capability update to the entity. The entity page's "Alpha (v0.0.1)" status and "primarily greenfield" framing are now out of date. The entity page needs a Modular Takeover section, an updated shrink-factor table (Folio 7×, Faker 9.9×, others), new CLI commands (`takeover`, `impl`, `test`, `build`), and the `vibe-sharing` data-donation detail.

- **[[spec-driven-development]]** — Sharpens the dual-track thesis. Vibe and SDD are sequential phases, not parallel alternatives. Also adds **brownfield as solved** (via takeover), closing one of the concept's long-standing open questions.

- **[[software-factory]]** — Modular takeover moves CodeSpeak closer to Shapiro's Level 4-5 for brownfield. The F7/mkdir example shows Level 4 operating in a post-takeover codebase — spec edit → build → working change, no manual code.

- **[[code-legibility-debate]]** — Strengthens School 1 ("code is a black box"). If specs are shorter than code by 7-10× and capture intent code doesn't, the argument for reading specs instead of code gets a concrete demonstration. But note: the blog post doesn't explicitly argue "don't read the code" — it argues specs are *better documentation*, which is a weaker claim.

- **[[context-engineering]]** — Implicit instruction-budget optimization. Multiple focused specs (vs. one monolith) keep each `codespeak build` inside the Smart Zone / Dumb Zone threshold. The Managed files + spec dependencies infrastructure (from March 9) is harness-level context management.

- **[[bmad-method]] / [[bmad-method-docs]]** — The modular takeover decomposition parallels BMAD's project-context.md + per-epic spec structure, but automated via tooling. BMAD's multi-persona Agile team is replaced by a single `codespeak takeover` CLI + web wizard.

- **[[sdd-course-deeplearning-ai]]** — [[sdd-course-deeplearning-ai|Paul Everett's course]] Lesson 11 teaches brownfield by having the agent "reverse-engineer the SDD artifacts from the existing code base." Modular takeover is the **tooling version** of the same workflow: what Everett teaches as a manual conversation pattern, CodeSpeak packages as a CLI + wizard. Convergence without cross-reference — same solution, different delivery.

- **[[alexlavaee-rpi-to-qrspi]]** — The "Plan-Reading Illusion" Lavaee names applies here inverted: the claim that specs are readable *is* defensible when they're 430 lines vs. 3000 LOC. Size matters.

- **[[everything-is-a-ralph-loop]]** — Counterpoint. Huntley would argue you should stay in loop-driven evolution even after takeover. CodeSpeak's position is that takeover is a **graduation event** — you leave the loop for structured spec-driven development. Different philosophies of what comes after vibe coding.

## Questions Raised

1. **How does the wizard propose the initial decomposition?** The post says "intentionally coarse initial proposal reflecting the application's gross structure," but doesn't describe the algorithm. Is it LLM-driven clustering? Static import analysis? Heuristics on file structure? This matters for understanding failure modes.

2. **What happens when the code has architectural flaws?** If the vibe-coded app has duplicated logic, misplaced responsibilities, or an unclear module boundary, does takeover preserve the flaws as specs, or does it opinionate toward better decomposition? The post implies the former (preserve), but the wizard's "rearrange" functionality suggests user can opinionate during confirmation.

3. **How does the drift story work after takeover?** If specs and code are both in the repo, and the developer is supposed to edit only specs going forward, what prevents accidental code edits that diverge from spec? The post doesn't address this. [[sdd-course-deeplearning-ai|Everett's course]] addresses it by procedural discipline ("don't edit directly, ask the agent"); CodeSpeak may rely on the `codespeak build` step regenerating code, but this isn't stated.

4. **Can modular takeover handle non-greenfield existing SDD projects?** I.e., a project that already has *some* specs and is being migrated further. The post focuses on vibe→SDD, not SDD-lite→SDD-strict. Unclear if this path exists.

5. **What's the cost per takeover?** Running `codespeak takeover` on a 3000-line codebase must invoke several Claude calls (module proposal, spec generation per module, validation). The post doesn't disclose cost. For enterprise adoption, this is the first question that matters.

6. **How does "Managed files" work?** Introduced March 9 but not explained here. The interaction between modular specs, Managed files, and code generation is key to understanding the full pipeline but is deferred to another post.

7. **Is 7× a reliable shrink factor?** Folio is a small Go app with a clean architecture. Shrink factor on a 100k-line Python monolith with mixed responsibilities is the interesting number. Faker's 9.9× is closer to that, but still a library, not a product. The wiki needs shrink-factor data from **production SaaS codebases** to validate the claim at scale.

8. **What's the CodeSpeak business model?** The post is a product release announcement. The `codespeak-dev/vibe-sharing` repo (launched April 15, one week after this post) asks users to donate vibe-coded projects for training. This suggests takeover quality is currently training-data-limited, and CodeSpeak is betting on user-contributed data. Implications: will quality plateau or grow? Are there privacy considerations?
