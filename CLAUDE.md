# SDLC AI Automation Research Wiki — Schema

## Purpose

This wiki tracks research on **AI automation in the software development lifecycle (SDLC)** — from code generation tools to fully autonomous software factories. The goal is to build a structured, evolving knowledge base that synthesizes sources across multiple sub-domains.

## Research Pillars

1. **Spec-Driven Development** — approaches where specifications drive code generation (spec-kit, BMAD method, Kiro, etc.)
2. **Software Factories** — the vision of fully automated software production pipelines (Devin, etc.)
3. **Gen AI Coding Agents** — patterns and principles for building AI coding agents (12-factor agents, HumanLayer, etc.)
4. **Code Legibility Debate** — two schools: "code is a black box, only read the spec" vs. "you still need to read the code"
5. **Industry Landscape** — what the industry is doing with AI in SDLC broadly

## Directory Structure

```
sdlc-ai-wiki/
├── CLAUDE.md          # This file — schema and conventions
├── raw/               # Immutable source documents
│   ├── assets/        # Downloaded images
│   └── *.md           # Clipped articles, papers, notes
└── wiki/              # LLM-generated and maintained pages
    ├── index.md       # Content catalog — all pages with summaries
    ├── log.md         # Chronological record of operations
    ├── overview.md    # High-level synthesis of the research
    ├── sources/       # One summary page per ingested source
    ├── concepts/      # Concept and topic pages
    ├── entities/      # Tools, companies, people, projects
    └── analyses/      # Comparisons, syntheses, filed query results
```

## Page Conventions

### Frontmatter

Every wiki page starts with YAML frontmatter:

```yaml
---
title: Page Title
type: source | concept | entity | analysis | overview
pillar: spec-driven | software-factories | coding-agents | code-legibility | industry
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [list of source filenames]
tags: [relevant tags]
---
```

### Cross-References

- Use `[[wikilinks]]` for internal links (Obsidian-compatible)
- Every page should link to related pages
- Every source summary should link to concepts and entities it mentions

### Source Summary Pages

Located in `wiki/sources/`. One per ingested source. Structure:
- **Metadata**: author, date, URL, pillar
- **Summary**: 3-5 paragraph summary of key points
- **Key Claims**: bulleted list of specific claims with brief evidence
- **Connections**: how this source relates to others in the wiki
- **Questions Raised**: open questions prompted by this source

### Concept Pages

Located in `wiki/concepts/`. Structure:
- **Definition**: what the concept is
- **Key Sources**: which sources discuss it
- **Current Understanding**: synthesis across all sources
- **Open Questions**: unresolved debates or gaps
- **Related Concepts**: links to other concept pages

### Entity Pages

Located in `wiki/entities/`. For tools, companies, people, projects. Structure:
- **Overview**: what it is, who made it, when
- **Relevance**: why it matters to this research
- **Key Claims**: what sources say about it
- **Links**: to source pages, concept pages, external URLs

### Analysis Pages

Located in `wiki/analyses/`. For comparisons, syntheses, filed query results. Structure:
- **Question**: what prompted this analysis
- **Findings**: the analysis itself
- **Sources Used**: which wiki pages informed this
- **Conclusions**: takeaways

## Workflows

### Ingest a new source

1. Read the source document from `raw/`
2. Discuss key takeaways with the user
3. Create a source summary page in `wiki/sources/`
4. Create or update relevant concept pages in `wiki/concepts/`
5. Create or update relevant entity pages in `wiki/entities/`
6. Update `wiki/index.md` with new/changed pages
7. Append an entry to `wiki/log.md`
8. Update `wiki/overview.md` if the source changes the big picture

### Answer a query

1. Read `wiki/index.md` to find relevant pages
2. Read relevant wiki pages
3. Synthesize an answer with citations to wiki pages
4. If the answer is substantial, offer to file it as an analysis page in `wiki/analyses/`

### Lint the wiki

1. Check for orphan pages (no inbound links)
2. Check for contradictions between pages
3. Check for stale claims superseded by newer sources
4. Identify concepts mentioned but lacking their own page
5. Suggest new sources to investigate
6. Report findings and fix issues

## Log Format

Each log entry:
```
## [YYYY-MM-DD] operation | Subject
Brief description of what was done. Pages created/updated listed.
```
