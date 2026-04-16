---
title: CodeSpeak
type: entity
pillar: spec-driven
created: 2026-04-08
updated: 2026-04-16
sources: [codespeak-modular-takeover]
tags: [tool, spec-driven, code-generation, claude, anthropic, github-integration, takeover, modular, brownfield, cli, vibe-sharing]
---

# CodeSpeak

## Overview

**CodeSpeak** is a spec-driven development platform (active alpha, weekly releases) built by the codespeak-dev team. It enables developers to **write application specifications in markdown** (`.cs.md` files) and have AI — specifically Anthropic's Claude — **automatically generate production code** from those specs. As of April 2026, the platform has matured beyond its v0.0.1 framing: it ships a CLI (`uv tool install codespeak-cli`) with commands `init`, `build`, `takeover`, `impl`, and `test`, and supports **modular takeover** of existing vibe-coded applications into focused spec sets via an interactive web wizard.

- **Website:** [codespeak.dev](https://codespeak.dev)
- **Blog:** [codespeak.dev/blog](https://codespeak.dev/blog) (weekly posts since Feb 2026)
- **GitHub org:** [github.com/codespeak-dev](https://github.com/codespeak-dev)
- **Status:** Active alpha, weekly feature releases
- **CLI install:** `uv tool install codespeak-cli`
- **AI Backend:** Anthropic Claude + Anthropic-compatible providers (since March 17, 2026)

## Modular Takeover (April 2026) — brownfield workflow

Introduced in [[codespeak-modular-takeover|the April 8 blog post]] by Dmitry Savvinov. Reframes CodeSpeak as a **vibe-to-SDD graduation tool**, not just a greenfield SDD platform:

1. Build your app via vibe coding (any tool)
2. Run `codespeak takeover` on the completed codebase
3. Interactive **browser wizard** proposes modular decomposition
4. Refine: split, merge, rearrange modules
5. Confirm → CodeSpeak generates **multiple focused specs** (one per module)
6. From here, develop spec-first: edit spec → `codespeak build` → code regenerates

This is a significant evolution from the February 2026 "monolithic takeover" (single spec file). The April version produces **multiple coupled specs** via "Managed files" + spec-dependencies machinery introduced in March.

### Shrink-factor data (spec size vs. code size)

| Project | Source LOC | Spec lines (MD) | Shrink factor | Type |
|---------|-----------|-----------------|---------------|------|
| Folio | ~3,000 Go | 430 | **~7×** | Demo (dual-pane terminal file manager, April 2026) |
| Faker | — | — | **9.9×** | Brownfield conversion (Python) |
| yt-dlp | — | — | **5.9–9×** range | Brownfield conversion (Python) |
| markitdown | — | — | 5.9–9× range | Brownfield conversion (Python) |
| beautifulsoup4 | — | — | 5.9–9× range | Brownfield conversion (Python) |

First dataset in the wiki documenting empirical spec-vs-code size ratios. Suggests the "spec is shorter than code" claim holds at **~6–10× reduction** for well-bounded projects, but sample is limited to libraries and small apps — production-SaaS data absent.

### Concrete example of intent preservation (from Folio)

Specs can capture design decisions invisible in code. Example from the terminal panel spec:

> "Only the following keys are handled by the application itself rather than forwarded to the terminal process: Ctrl+T, Ctrl+\\, Ctrl+Up, Ctrl+Down."

The *why* (F10 must be forwarded so that `htop` running inside the terminal works correctly) is preserved in the spec as one sentence. In implementation code, this is a series of switch/case exclusions with no context. This is one of the sharpest concrete examples in the wiki of the [[dex-rpi-to-crispy|Mental Alignment via artifacts]] principle.

## How It Works

CodeSpeak follows a tight spec → build → commit loop:

1. **Define specs** — Write or edit `spec/main.cs.md` in natural language / markdown describing application requirements
2. **Build** — CodeSpeak's build process sends specs to Claude, which generates full application code
3. **Git integration** — Generated code is delivered as automatic git commits, preserving full history
4. **Iterate** — Submit change requests via `change-request.cs.md` files for bug fixes or refinements
5. **Run** — Execute locally using the `uv` package manager or GitHub Codespaces

### Setup Requirements

- Anthropic API key configured as a GitHub secret
- CodeSpeak GitHub App installed on the repository
- `uv` runtime for executing generated applications

## Relevance

CodeSpeak is a concrete, working implementation of the [[spec-driven-development]] paradigm. It represents one of the most direct approaches to the spec → code vision:

- **Specs are the source of truth** — `.cs.md` files are what developers maintain; code is a generated artifact
- **Git-native** — Unlike some spec-driven tools, CodeSpeak integrates directly into the git workflow via automatic commits
- **Change requests as first-class** — Bug fixes and refinements go through the same spec-driven pipeline
- **Conversion of existing projects** — The team has demonstrated converting portions of major open-source projects (faker, markitdown, yt-dlp, beautifulsoup4) to CodeSpeak specs

This positions CodeSpeak as evidence that spec-driven development is moving from theory to practice, directly supporting the thesis that **specs as source of truth** is viable for real-world codebases.

## Key Claims

- **Full-app generation from markdown specs** — Not just code completion or snippets; entire Django applications with migrations and dev server functionality generated from specs
- **Existing codebase conversion** — The team has forked and partially converted major Python projects (faker, markitdown, yt-dlp, beautifulsoup4), demonstrating that spec-driven approaches can work with brownfield codebases — a key [[spec-driven-development#Open Questions|open question]] in the wiki
- **Multi-language support** — Repositories show projects in Python, TypeScript, and Go
- **POSIX utilities built with AI** — Their `posix-utilities` repo demonstrates generating system-level code from specs

## Demonstrated Conversions

The codespeak-dev GitHub organization includes forks of well-known projects with parts converted to CodeSpeak specs:

| Project | Original | Language | Notes |
|---------|----------|----------|-------|
| faker | joke2k/faker | Python | Test data generation library (9.9× shrink) |
| markitdown | microsoft/markitdown | Python | Document-to-markdown converter |
| yt-dlp | yt-dlp/yt-dlp | Python | Video downloader |
| beautifulsoup4 | — | Python | HTML/XML parser |
| django-oscar | — | Python | Domain-driven e-commerce |
| **folio** | (first-party demo) | Go | **Dual-pane terminal file manager, April 2026 — demo for modular takeover (~7× shrink)** |

This is notable because it directly addresses the open question of whether spec-driven development works for legacy/brownfield codebases. With modular takeover (April 2026), the workflow is no longer limited to cherry-picked module conversions — full applications can be converted via the CLI + web wizard.

## CLI Commands (as of April 2026)

| Command | Purpose | Introduced |
|---------|---------|------------|
| `codespeak init` | Initialize a project for CodeSpeak | v0.0.1 |
| `codespeak build specs/app.cs.md` | Generate code from specs | v0.0.1 |
| `codespeak takeover` | Convert existing code to specs (monolithic) | Feb 2026 |
| `codespeak takeover` (modular) | Convert via web wizard → multiple focused specs | Apr 2026 |
| `codespeak impl` | Standalone implementation step | Mar 2026 |
| `codespeak test` | Auto-configured test runner | Mar 2026 |

Install: `uv tool install codespeak-cli`

## Community and Data Strategy

Launched **April 15, 2026**: `codespeak-dev/vibe-sharing` — a data-donation tool asking users to contribute vibe-coded projects (code, git history, agent sessions) to improve takeover quality. Signal: takeover is the **product priority**, and the team is betting on user-contributed training data to close the quality loop. Opt-in with explicit consent; no commercial product built on donated code.

## Blog Timeline (Feb–Apr 2026)

| Date | Post | New capability |
|------|------|----------------|
| 2026-02-23 | First glimpse of `codespeak takeover` | Monolithic takeover (single spec output) |
| 2026-03-02 | Test coverage improvement | CodeSpeak generates tests |
| 2026-03-09 | Spec dependencies + Managed files | Multi-spec projects, coupling primitives |
| 2026-03-17 | Reconstructing specs from vibe coding sessions | Anthropic-compatible providers |
| 2026-03-24 | Tests + `impl` command | `codespeak test`, `codespeak impl`, faster builds |
| **2026-04-08** | **[[codespeak-modular-takeover\|Modular takeover]]** | **Web wizard, multi-spec decomposition** |
| 2026-04-15 | (repo-only) `vibe-sharing` launched | Data-donation program

## Comparison with Other Spec-Driven Tools

| Aspect | CodeSpeak | [[bmad-method\|BMAD]] | [[spec-kit\|Spec Kit]] | [[sdd-course-deeplearning-ai\|Everett course]] |
|--------|-----------|------|----------|------------|
| Spec format | `.cs.md` markdown (multiple, coupled) | Multi-template Agile artifacts | Markdown pipeline (spec → plan → tasks) | 3 constitution + 3 per-feature files |
| AI backend | Claude + Anthropic-compatible | Claude Code / Cursor / Windsurf | Agent-agnostic | Agent-agnostic (shown: Claude Code) |
| Integration | CLI + GitHub App + web wizard | IDE plugin (manual) | CLI | Plain markdown + git |
| Scope | Full app **auto-generation** | Full SDLC (planning → QA) | Feature pipeline | Project constitution + features + replanning |
| Brownfield | **Modular takeover via web wizard (Apr 2026)** | Primarily greenfield | Feature-level | Reverse-engineering via agent (Lesson 11) |
| Who writes code | **CodeSpeak (you never do)** | You (via agents) | You (via agents) | You (via agents) |
| Status | Active alpha, weekly releases | Active (19.1k ⭐) | Active | Course launched April 2026 |

**Positioning:** CodeSpeak is the **strictest SDD tool in the wiki** — you never write or edit code, only specs. The other three are SDD *workflows* that still involve reading and steering agent-written code. CodeSpeak is **spec-as-source, code-as-compiled-output** in the literal sense; the others are **spec-leading, code-following**.

## Open Questions

- ~~How complete are the brownfield conversions? Are entire codebases converted or just selected modules?~~ *Partially answered by [[codespeak-modular-takeover]]: full applications can now be converted via `codespeak takeover`, producing multiple focused specs (e.g., Folio's 3000-line Go codebase → 4 specs × 430 lines total). Remaining: how does this scale to 100k+ LOC?*
- How does CodeSpeak handle specs that conflict with existing code structure? (Web wizard allows manual rearrangement, but no evidence on opinionation — does takeover silently preserve architectural flaws or suggest cleanups?)
- What's the quality of generated code vs. the original in the forked projects? (No published side-by-side comparison.)
- How does the `change-request.cs.md` workflow compare to traditional issue tracking?
- What happens when specs are ambiguous — does CodeSpeak have validation/review steps like [[superpowers-5]]'s adversarial review?
- **What is the algorithm behind the wizard's initial decomposition proposal?** LLM-driven clustering? Static import analysis? File structure heuristics?
- **Cost per takeover run** — undisclosed, unclear if enterprise-viable at scale.
- **How does "Managed files" + spec-dependencies work in practice?** Introduced March 9, not explained in depth publicly.
- **Is the 7× shrink factor reliable on large codebases?** Folio (3k LOC) and Faker (library) are small; production SaaS shrink factors absent.

## Links

- [[spec-driven-development]] — The concept CodeSpeak implements
- [[software-factory]] — CodeSpeak represents a partial realization of the software factory vision
- [[automation-levels]] — CodeSpeak targets Level 4+ (autonomous generation from specs)
- [[bmad-method]] — Alternative spec-driven framework (more process-oriented vs. CodeSpeak's tool-oriented approach)
- [[code-legibility-debate]] — If specs are the source of truth and code is generated, does code legibility matter?
