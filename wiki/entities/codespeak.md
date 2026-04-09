---
title: CodeSpeak
type: entity
pillar: spec-driven
created: 2026-04-08
updated: 2026-04-08
sources: []
tags: [tool, spec-driven, code-generation, claude, anthropic, github-integration]
---

# CodeSpeak

## Overview

**CodeSpeak** is a spec-driven development platform (alpha, v0.0.1) built by the codespeak-dev team. It enables developers to **write application specifications in markdown** (`.cs.md` files) and have AI — specifically Anthropic's Claude — **automatically generate production code** from those specs.

- **Website:** [codespeak.dev](https://codespeak.dev)
- **GitHub:** [github.com/codespeak-dev](https://github.com/codespeak-dev)
- **Status:** Alpha (v0.0.1)
- **AI Backend:** Anthropic Claude

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
| faker | joke2k/faker | Python | Test data generation library |
| markitdown | microsoft/markitdown | Python | Document-to-markdown converter |
| yt-dlp | yt-dlp/yt-dlp | Python | Video downloader |
| beautifulsoup4 | — | Python | HTML/XML parser |
| django-oscar | — | Python | Domain-driven e-commerce |

This is notable because it directly addresses the open question of whether spec-driven development works for legacy/brownfield codebases.

## Comparison with Other Spec-Driven Tools

| Aspect | CodeSpeak | [[bmad-method|BMAD]] | Spec-kit | Kiro (AWS) |
|--------|-----------|------|----------|------------|
| Spec format | `.cs.md` markdown | Multi-template Agile artifacts | TBD | TBD |
| AI backend | Claude (Anthropic) | Claude Code / Cursor / Windsurf | TBD | TBD |
| Integration | GitHub App + git commits | IDE plugin (manual) | TBD | TBD |
| Scope | Full app generation | Full SDLC (planning → QA) | TBD | TBD |
| Brownfield | Demonstrated (5+ conversions) | Primarily greenfield | TBD | TBD |
| Status | Alpha (v0.0.1) | Active (19.1k ⭐) | TBD | TBD |

## Open Questions

- How complete are the brownfield conversions? Are entire codebases converted or just selected modules?
- How does CodeSpeak handle specs that conflict with existing code structure?
- What's the quality of generated code vs. the original in the forked projects?
- How does the `change-request.cs.md` workflow compare to traditional issue tracking?
- What happens when specs are ambiguous — does CodeSpeak have validation/review steps like [[superpowers-5]]'s adversarial review?

## Links

- [[spec-driven-development]] — The concept CodeSpeak implements
- [[software-factory]] — CodeSpeak represents a partial realization of the software factory vision
- [[automation-levels]] — CodeSpeak targets Level 4+ (autonomous generation from specs)
- [[bmad-method]] — Alternative spec-driven framework (more process-oriented vs. CodeSpeak's tool-oriented approach)
- [[code-legibility-debate]] — If specs are the source of truth and code is generated, does code legibility matter?
