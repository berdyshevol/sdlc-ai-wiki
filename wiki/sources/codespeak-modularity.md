---
title: "First step in modularity: Spec dependencies and Managed files"
type: source
pillar: spec-driven
created: 2026-04-16
updated: 2026-04-16
sources: [codespeak-modularity]
tags: [codespeak, modularity, spec-dependencies, managed-files, imports, scope, change-scoping, version-0.3.4]
author: CodeSpeak team
url: https://codespeak.dev/blog/modularity-20260309
---

# First step in modularity: Spec dependencies and Managed files

## Metadata

- **Author:** CodeSpeak team (byline not captured in fetch)
- **URL:** https://codespeak.dev/blog/modularity-20260309
- **Date:** 2026-03-09
- **Version announced:** CodeSpeak 0.3.4
- **Format:** Product release announcement on CodeSpeak blog
- **Raw file:** `raw/codespeak-modularity.md`
- **Pillar:** [[spec-driven-development]]

## Summary

This is the **foundational** post in the CodeSpeak 2026 arc: the March 9 release (v0.3.4) introduces the two primitives — **spec imports** and **managed files** — that later make [[codespeak-modular-takeover|modular takeover]] (April 8) architecturally possible. Without spec dependencies and per-spec source-file scopes, you cannot have a multi-spec CodeSpeak project; takeover would have nowhere to put its outputs beyond a single monolithic spec. This post is, in effect, the runtime model that modular takeover emits into.

Two primitives ship together:

**1. Spec imports (dependency-ordered builds).** Specs declare dependencies via frontmatter:

```
---
import storage.cs.md
---
```

Imports are transitive (A → B → C builds all three in correct order). Only changed specs are rebuilt; unchanged dependencies are skipped. The post demonstrates this with a memo app where a one-line diff in `storage.cs.md` (*"Memos are stored in a JSON file"* → *"Memos are stored in an sqlite file"*) causes CodeSpeak to rewrite `storage.py` to use `sqlite3` while leaving the main CLI code untouched — because `main.cs.md` doesn't care *how* storage works, only *that* storage exists.

**2. Managed files (scope boundaries).** Every spec has a **scope**: the set of source files it created or took over. Those files are *"managed by"* the spec — free to be modified during its builds. Everything else in the project (config files, shared dependencies, other modules) is **non-managed**. When a build needs to modify a non-managed file, CodeSpeak produces a notification at the end of the build listing what was touched outside the scope.

The notification is **not a block**. It gives four explicit handling options, each with a different trust-surface:

| Approach | Scope | Use case |
|----------|-------|----------|
| `suppressNonManagedFilesNotification: true` | All specs | You don't want visibility — you trust the agent |
| `strictManagedFilesControl: true` | All specs | Specs must be self-contained — block writes outside scope |
| `codespeak update-managed-files 'pyproject.toml'` | One spec | Per-spec whitelist — this spec owns this file too |
| `codespeak whitelist 'pyproject.toml'` (supports globs) | All specs | Project-wide shared files (pyproject.toml, shared configs) |

The trust model is subtle and deserves attention: **non-managed edits are allowed by default, but surfaced.** This is neither fully permissive (default-suppress) nor fully restrictive (default-block). It's a *"tell you what happened"* model that makes implicit actions visible without stopping them. For SDD at scale with multiple developers and multiple specs in one repo, this is a reasonable middle ground — CodeSpeak does what it needs, you see what it did, and you can tighten the boundary going forward. The design philosophy echoes [[bmad-method-docs|BMAD's]] "artifacts-as-shared-context" and [[dex-rpi-to-crispy|Dex's]] "Mental Alignment" — a shared understanding between human and agent about *who owns what*, enforced by artifacts (the managed-files list) rather than by rules.

The memo-app example is worth calling out as a pedagogical artifact: a 10-line spec and a 15-line spec produce a working CLI with storage and commands. Change one line → CodeSpeak surfaces the semantic diff as a build title (*"Changing memo storage from JSON to SQLite"*) and rewrites only the affected module. This is the first time in the wiki we see **a CodeSpeak build plan display semantic understanding of the diff** (not just "implement spec" but "*what* the change is about). Small but telling — suggests CodeSpeak is doing non-trivial spec-diff analysis, not just re-running the whole pipeline.

The post also documents a subtle but important assumption: **interface stability between specs is not enforced, only encouraged.** The post states *"changes to one concern don't ripple into unrelated specs … if the interface stays the same."* But the post explicitly lists as a *future* goal: *"reporting errors when an imported spec does not provide what the importing one expects."* This is the foundational SDD correctness problem — if specs can silently drift from the contracts their importers assume, the whole dependency-graph story loses its leverage. CodeSpeak is honest that this is not yet solved in v0.3.4.

## Key Claims

- **Modularity arrives to CodeSpeak as two primitives: imports + managed files.** *"We are starting to introduce modularity to CodeSpeak. Specs can now import one another, and every spec knows which source files are managed by it."* Before v0.3.4, CodeSpeak was effectively single-spec-per-project. After, multi-spec projects are possible.

- **`import` directive in frontmatter + transitive dependency resolution.** `---\nimport storage.cs.md\n---`. Transitive: A → B → C builds all in order. Classic dependency-graph semantics, just applied to markdown specs. Direct analogue of module imports in code.

- **Change scoping principle:** *"when a spec S gets updated, only the code S manages should normally update."* This is the formal statement of the "modular change locality" property that modular-SDD requires. Later proven in practice by the storage-to-sqlite one-line change affecting only `storage.py`, not `main.py`.

- **Dependency tracking principle:** *"S will be built before any of its dependencies."* (The post's wording is slightly inverted — what's actually meant is "S's dependencies will be built before S." The example makes the intent clear.) Dependency-ordered builds with change detection: only changed specs rebuild.

- **Managed files = per-spec source-file scope.** Each spec has a scope of source files it owns; writes inside scope are free, writes outside are surfaced. This is the runtime model that later lets modular takeover emit multiple coupled specs with clear boundaries.

- **Semantic diff understanding in build titles.** *"Changing memo storage from JSON to SQLite"* is a build-progress title that describes the semantic intent of the diff, not just "implement spec." Suggests CodeSpeak does non-trivial spec-diff analysis to decide what to rebuild and how to report it.

- **Four-way trust model for non-managed writes:** permissive/suppressed/strict/fine-grained. Default = permissive with notification. Trust model is explicit, not hidden. This is a design choice worth emulating elsewhere — other SDD tools could learn from this.

- **Glob-pattern support in whitelist.** `codespeak whitelist 'config/*.yaml'`. Pragmatic detail — shared configs often match patterns, not specific paths.

- **Explicit acknowledgment of unsolved problems.** Future goals listed at the end of the post:
  - *"specifying APIs for specs to provide a clean boundary between modules"*
  - *"reporting errors when an imported spec does not provide what the importing one expects"*
  - *"generating modules in relative isolation to make them reusable in other projects"*

  These are the three hardest problems in modular SDD: contract definition, contract violation detection, and module isolation. Honest about what's not yet done.

## Connections

- **[[codespeak]]** — Updates the entity's understanding of v0.3.4 capabilities. The "Managed files" + spec-dependencies mechanism should be documented in the entity's architecture notes. Current entity doesn't elaborate on the scope boundaries and notification options.

- **[[codespeak-modular-takeover]]** — **Direct dependency.** Modular takeover's multi-spec output (4 specs for Folio) runs on the primitives introduced here. Without imports + managed files, the April 8 wizard would have nowhere to materialize its module decomposition. Reading the two posts together:
  - Mar 9: runtime model for multi-spec projects
  - Apr 8: UX for generating multi-spec projects from existing code

- **[[codespeak-vibe-takeover]]** — Chronological successor (8 days later). Vibe-takeover's limitation *"support generating more than one spec file"* is gated on the infrastructure introduced here. The Mar 17 post is effectively saying: "we have the runtime (Mar 9), but takeover doesn't yet use it." Modular takeover (Apr 8) finally closes the loop.

- **[[spec-driven-development]]** — Gives the concept page its first concrete example of **modular SDD**: how to express module boundaries in specs and enforce change locality. This is the missing link between "one-file SDD" (Spec Kit / early CodeSpeak) and "multi-module SDD" (BMAD / modular-takeover CodeSpeak).

- **[[bmad-method]] / [[bmad-method-docs]]** — BMAD's `project-context.md` is the shared-context file across all agents. CodeSpeak's managed files are the **opposite** pattern: per-spec scope, notification when you cross it. BMAD pools context; CodeSpeak isolates context with explicit crossing points. Two philosophies of multi-module SDD.

- **[[sdd-course-deeplearning-ai]]** — Paul Everett's course uses one Constitution + one feature-spec folder. No modularity primitives. CodeSpeak's v0.3.4 is more structurally sophisticated than the mainstream pedagogical template — but also more tool-bound.

- **[[context-engineering]]** — The managed-files notification is a **context-engineering affordance**: you see what the agent touched outside its scope, so you can decide whether to promote those files to scope, block them, or whitelist globally. Every edit is observable. Compare to [[skill-issue-harness-engineering|Kyle's]] "success is silent, only failures produce verbose output" — CodeSpeak inverts this for boundary crossings: boundary crossings are noisy, in-scope work is silent.

- **[[dex-rpi-to-crispy]]** — Dex's "Mental Alignment via artifacts" — shared ground between human and agent via documented decisions — is the philosophical basis for managed files. The managed-files list is an artifact that records *"these files belong to this spec"* as a shared contract.

- **[[instruction-budget]]** — Multi-spec projects help with instruction budget: each build step only loads the relevant spec (and its transitive imports), not the whole project. Smaller context per build → more reliable agent behavior. Modular SDD is implicitly instruction-budget-aware.

## Questions Raised

1. **What counts as "managed" when takeover ingests existing code?** Modular takeover (Apr 8) produces multiple specs from an existing codebase. Each spec gets a scope — but how is that scope initially assigned? Presumably by the wizard's decomposition, but the post doesn't say whether files can be in multiple scopes, or in none.

2. **How is the semantic diff title computed?** *"Changing memo storage from JSON to SQLite"* — is this from the git diff of the spec? From the model's understanding of intent? Caching implications are different.

3. **Is there a way to see the dependency graph?** As projects grow to dozens of specs, transitive imports become a graph. The post doesn't mention tooling to visualize the dependency graph. Useful for debugging "why did this spec rebuild?"

4. **`strictManagedFilesControl: true` + needing to add a library.** The post warns: *"If the spec genuinely requires a change to a non-managed file (like adding a dependency), CodeSpeak won't be able to make it, which might lead to unexpected build results."* What does "unexpected build results" mean in practice? Silent skip? Error? Half-built state?

5. **Interface contracts between specs are not yet enforced.** The post lists *"reporting errors when an imported spec does not provide what the importing one expects"* as future work. Until this lands, how does CodeSpeak prevent a spec from changing in a way that breaks its importers? Does `codespeak build` fail silently? Fail loudly? Just produce code that doesn't compile?

6. **What happens when two specs want to manage the same file?** Conflict resolution is not documented. Does CodeSpeak error? Pick one? Show notification?

7. **Glob patterns in whitelist — are they evaluated at build time or config time?** `config/*.yaml` matching could behave differently if evaluated on every build (new files auto-whitelisted) vs. at config-time (static list).

8. **Is there an `exports` counterpart to `import`?** The post mentions *"specifying APIs for specs to provide a clean boundary between modules"* as a future goal. This would presumably look like frontmatter directives describing the contract a spec exposes. How formal will these APIs be? Type-level? Behavioral? Just prose?
