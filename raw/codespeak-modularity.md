# First step in modularity: Spec dependencies and Managed files

**Source:** https://codespeak.dev/blog/modularity-20260309
**Date:** March 9, 2026
**Author:** (CodeSpeak team — byline not captured in WebFetch output)
**Version announced:** CodeSpeak 0.3.4
**Retrieval note:** Fetched via Claude Code `WebFetch` on 2026-04-16 with an aggressive verbatim prompt. Content is close to raw article text — code blocks, CLI examples, and direct quotes preserved. Author byline was not captured; the vibe-takeover post (March 17) was by Andrey Breslav, so this may be the same author.

---

> ⚠️ CodeSpeak is in Alpha Preview: many things are rough around the edges. Please use at your own risk and report any issues to our Discord. Thank you!

_Today we release CodeSpeak 0.3.4. Please find the full release notes at the end of this post._

We are starting to introduce modularity to CodeSpeak. Specs can now import one another, and every spec knows which source files are managed by it. The principle is: when a spec _S_ gets updated

*   **change scoping**: only the code _S_ manages should normally update (see more below), and
*   **dependency tracking**: _S_ will be built before any of its dependencies.

A single spec works great for small projects, but as the project grows, cramming everything into one file makes it harder for humans to read and change. You want to split things up — just like you'd split code into modules.

While dependencies are more or less familiar, scoping is more specific to our take on spec-driven development. In CodeSpeak, a spec describes one logically self-contained part of your system (a module, or a subsystem), and the corresponding source files form its **scope**. We say that this code is _managed by_ the corresponding spec: it will be generated, updated, and maintained in accordance with the changes to the spec. In many cases, when a spec is changed, only files within its scope change in response, and if anything beyond is being changed, CodeSpeak gives you a heads up.

## How CodeSpeak tracks files

When you build a spec, CodeSpeak keeps track of which files it creates or takes over. These are called **managed files** — files that belong to a specific spec and can be freely modified during builds. For example, if your spec `main.cs.md` produces `main.py`, then `main.py` is a managed file for that spec.

Anything else that already exists in your project — configuration files, shared dependencies, other modules — is _not_ managed. If CodeSpeak needs to modify one of these files to implement your spec, it will let you know.

## Example: A simple memo app

Let's build a small CLI app for managing memos.

### Project setup

(Install CodeSpeak first; `uv tool install codespeak-cli` + `codespeak login`; `uv init --bare`, `git init`, `codespeak init`.)

### Our specs

Two specs:

**`storage.cs.md`**

```
# Memos storage

Each memo has:
- content
- creation date

Memos are stored in a JSON file
```

**`main.cs.md`**

```
---
import storage.cs.md
---
# memo app

This is a simple Python CLI app that supports simple creation and retrieval of memos

## CLI commands

`memo add <memo content>` - creates a new memo with given content
`memo show` - shows all memos, grouped by creation date
`memo find <substring>` - finds a given memo by substring
`memo delete <substring>` - deletes a given memo by substring
```

### The `import` directive

Notice the frontmatter at the top of `main.cs.md`:

```
---
import storage.cs.md
---
```

This tells CodeSpeak that `main.cs.md` depends on `storage.cs.md`. When building `main.cs.md`, CodeSpeak will first build the storage spec, and then build the main spec with full knowledge of what storage provides.

> You can import multiple specs, and imports are transitive — if A imports B and B imports C, CodeSpeak will build all three in the right order.

### Build time!

```
codespeak build main.cs.md --skip-tests
```

```
Processing spec 1/2: storage.cs.md
╭─ CodeSpeak Progress: Building Python CLI memo app with create, retrieve,─╮
│ ✓ Process specification (0.0s)                                           │
│ ✓ Collect project information (0.0s)                                     │
│ ✓ Implement specification (1m 22s)                                       │
│ ╰─ ✓ Collect context & plan work (26.4s)                                 │
│ ╰─ ✓ Add rich dependency to pyproject.toml (6.5s)                        │
│ ╰─ ✓ Implement main CLI app with all required commands (32.5s)           │
│ ╰─ ✓ Test that the rich dependency is available (6.4s)                   │
│ ✓ Finalize mixed mode run (0.0s)                                         │
╰────────────────────────────  Alpha Preview  ─────────────────────────────╯
Processing spec 2/2: main.cs.md
App built successfully.
```

> CodeSpeak processed both specs in dependency order: `storage.cs.md` first (1/2), then `main.cs.md` (2/2). This way each build step is focused on one concern — CodeSpeak can give its full attention to storage in isolation, then build the CLI layer against the result.

### Changing the storage backend — one-line diff

```diff
  # Memos storage

  Each memo has:
  - content
  - creation date

- Memos are stored in a plain text file in JSON format
+ Memos are stored in an sqlite file
```

> That's it — one line changed. The main spec stays exactly the same, because it doesn't care _how_ memos are stored. It only cares that storage exists and provides certain capabilities. This is the payoff of splitting specs: changes to one concern don't ripple into unrelated specs, making them easier to review and reason about.

### Rebuilding

```
codespeak build main.cs.md --skip-tests
```

```
╭───── CodeSpeak Progress: Changing memo storage from JSON to SQLite ──────╮
│ ✓ Process specification (0.0s)                                           │
│ ✓ Collect project information (0.2s)                                     │
│ ✓ Implement specification (1m 27s)                                       │
│ ╰─ ✓ Collect context & plan work (24.5s)                                 │
│ ╰─ ✓ Update storage.py to use SQLite instead of JSON file (9.3s)         │
│ ╰─ ✓ Update MemosStorage class to use SQLite database operations (33.4s) │
│ ╰─ ✓ Ensure all existing functionality is preserved with SQLite backend  │
│ (9.7s)                                                                   │
│ ✓ Finalize mixed mode run (0.0s)                                         │
╰────────────────────────────  Alpha Preview  ─────────────────────────────╯
Processing spec 1/1: storage.cs.md
App built successfully.
```

> Even though we passed `main.cs.md`, CodeSpeak resolved its dependencies, detected that `storage.cs.md` had changed, and rebuilt it. The main spec hadn't changed, so CodeSpeak skipped it — no unnecessary work.
>
> The progress title — "Changing memo storage from JSON to SQLite" — shows that CodeSpeak understood exactly what the one-line diff meant.

### Imports: summary

*   **`import` in frontmatter** declares a dependency between specs
*   **CodeSpeak builds in dependency order** — dependencies first, then the specs that use them
*   **Only changed specs are rebuilt** — CodeSpeak tracks what changed and skips the rest
*   **Changes stay local** — modifying one spec doesn't require touching its dependents if the interface stays the same

## Managed files: adding a dependency

When adding `App uses rich library for pretty terminal UI` to `main.cs.md`:

```
╭─── CodeSpeak Progress: Adding rich library for pretty terminal UI ────╮
│ ...                                                                   │
╰───────────────────────── 🚧 Alpha Preview 🚧 ─────────────────────────╯

CodeSpeak modified 1 file not directly managed by the current spec:
  - pyproject.toml

To disallow modifications to non-managed files, add this to 
codespeak.json:
  "strictManagedFilesControl": true

To suppress this notification, add this to codespeak.json:
  "suppressNonManagedFilesNotification": true

To allow editing these files when working on the current spec, run:
  codespeak update-managed-files 'pyproject.toml'

To always allow editing these files, run:
  codespeak whitelist 'pyproject.toml'
```

### Why the notification?

The build worked correctly: CodeSpeak figured out that using `rich` requires adding a dependency, and did so on its own. So why flag it?

> Because changes like these deserve your attention. A spec describes one module's behavior. Editing `pyproject.toml` affects the _entire project_ — all its specs, all its modules. In a larger project, you might have multiple specs, and you probably don't want one spec's build silently pulling in new dependencies, modifying shared configs, or rewriting files that belong to another spec.
>
> CodeSpeak doesn't block these changes by default — it just makes sure you know they happened and gives you options for how to handle them going forward.

### Four options

| Approach | Scope | When to use |
|----------|-------|-------------|
| Suppress notification (`suppressNonManagedFilesNotification: true`) | All specs | You don't need visibility into non-managed file changes |
| Strict mode (`strictManagedFilesControl: true`) | All specs | Specs must be fully self-contained (can block valid edits) |
| `codespeak update-managed-files 'pyproject.toml'` | One spec | Fine-grained, per-spec permission |
| `codespeak whitelist 'pyproject.toml'` (supports glob) | All specs | Shared files that any spec may need to modify |

## Conclusion

> Spec dependencies (imports) and managed files are important building blocks on our way to modularity in CodeSpeak projects. The ultimate goal is to represent complex systems with modular specs that help people understand the system better at both design time and run time.

Future directions stated in the post:

*   specifying APIs for specs to provide a clean boundary between modules,
*   reporting errors when an imported spec does not provide what the importing one expects,
*   generating modules in relative isolation to make them reusable in other projects.

---

## Full Changelog since 0.3.2

### New

*   Specs can now import other specs using an `import` directive in the frontmatter, enabling modular project structures with automatic dependency-ordered builds.
*   CodeSpeak now tracks which source files are managed by each spec and warns you at the end of the build when files outside the spec's scope were modified.
*   Added `codespeak update-managed-files` to mark specific files as managed by the current spec, and `codespeak whitelist` for shared files that any spec may need to modify.
*   Spec frontmatter now supports leading whitespace and `//` comments, and rejects unrecognized content with a clear error message.
*   Updated the CodeSpeak logo.

### Bug fixes

*   Fixed a crash that could occur during builds when the AI model sent a malformed internal message.
*   Fixed the `coverage` command failing after internal changes.
