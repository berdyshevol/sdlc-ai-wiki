---
title: BMAD Method
type: entity
pillar: spec-driven
created: 2026-04-08
updated: 2026-04-09
sources: [SDD comparison table, research-04-AI-in-SDLC.docx, bmad-method-docs]
tags: [framework, methodology, multi-agent, agile, spec-driven, open-source]
---

# BMAD Method

## Overview

**BMAD** (Breakthrough Method for Agile AI-Driven Development) is an open-source multi-agent framework that simulates a full Agile development team using AI. Created by **bmadcode**, it provides 6 specialized agent personas and structured workflows covering the entire SDLC — from brainstorming to deployment.

**GitHub:** [github.com/bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) (~19.1k stars)
**Docs:** [docs.bmad-method.org](https://docs.bmad-method.org)
**Runtime:** Runs on top of Claude Code, Cursor, Windsurf (not a standalone IDE)

## Philosophy

BMAD's core principle distinguishes it from typical AI tools: rather than having AI "do the thinking for you" (which produces average results), BMAD positions AI as **expert collaborators who guide you through a structured process** to bring out your best thinking in partnership with the AI.

This is a **partnership model**, not delegation. The human remains the decision-maker; the AI provides structure, domain expertise, and systematic coverage.

BMAD emphasizes **reducing human bottlenecks** by allowing longer autonomous agent execution between intentional human checkpoints, rather than constant supervision.

## Architecture

### Four-Phase Development Cycle

BMAD structures work into sequential phases:

1. **Analysis** (Phase 1) — Optional brainstorming, market/domain/technical research, product brief creation
2. **Planning** (Phase 2) — Requirements documentation via PRD or specification
3. **Solutioning** (Phase 3) — Architecture design and work breakdown into epics/stories
4. **Implementation** (Phase 4) — Story-by-story development with code review and retrospectives

### Three Planning Tracks

Projects select complexity-appropriate paths, addressing the "overkill for small projects" criticism:

| Track | Scope | Artifacts |
|-------|-------|-----------|
| **Quick Flow** | Bug fixes, small features | Tech-spec only |
| **BMad Method** | Standard products, platforms | PRD + architecture |
| **Enterprise** | Compliance, multi-tenant systems | Comprehensive documentation |

### Project Directory Layout

```
project/
├── _bmad/                    # Installation folder
│   ├── core/                 # Universal framework
│   ├── bmm/                  # BMad Method module
│   └── _config/agents/       # Agent customizations
└── _bmad-output/             # Generated artifacts
    ├── planning-artifacts/
    ├── implementation-artifacts/
    └── project-context.md    # Implementation guidelines
```

### Agent Personas

BMAD provides 6 specialized agent personas with named identities, dedicated skill IDs, and defined workflow sets:

| Agent | Name | Skill ID | Specialization | Key Workflows |
|-------|------|----------|----------------|---------------|
| Analyst | Mary | `bmad-analyst` | Research, brainstorming, discovery | Brainstorm, research, product brief, PRFAQ |
| PM | John | `bmad-pm` | Requirements and scope | Create/validate PRD, epics/stories |
| Architect | Winston | `bmad-architect` | Technical design decisions | Create architecture, implementation readiness |
| Developer | Amelia | `bmad-agent-dev` | Implementation and testing | Dev story, quick dev, code review, sprint planning |
| UX Designer | Sally | `bmad-ux-designer` | User experience design | UX design workflows |
| Technical Writer | Paige | `bmad-tech-writer` | Documentation | Project documentation, standards, diagrams |

Agents are customizable via `.customize.yaml` files that preserve changes across framework updates.

## Key Mechanisms

### Project Context File

The `project-context.md` document captures technology stack versions and implementation rules. It ensures consistency across agents implementing different epics by documenting conventions agents might otherwise miss or hallucinate. This is a practical implementation of [[context-engineering]] — using static artifacts as shared ground, similar to Dex's "Mental Alignment" concept ([[dex-rpi-to-crispy]]).

### Architecture as Shared Context

When multiple agents implement different epics, documented architecture decisions prevent conflicts by establishing unified standards for API patterns, database design, state management, and naming conventions before implementation begins. Rather than agents communicating directly, they all read from a shared specification of constraints — a **coordination-through-artifacts** pattern.

### Adversarial Review

Code review mandates finding problems — "no 'looks good' allowed." The reviewer assumes issues exist and must surface specific findings, preventing confirmation bias. This is the most explicit articulation of adversarial review in the wiki, paralleling [[superpowers-5]]'s adversarial spec review.

### Advanced Elicitation

After workflows generate content, structured second-pass analysis methods (pre-mortem analysis, inversion, first principles thinking) reconsider output through specific reasoning lenses.

### Fresh Chat Requirement

Each workflow must run in a new chat session to prevent context contamination. This is a practical solution to the [[instruction-budget]] problem: rather than cramming all agent instructions into one session, each workflow gets a clean context window.

### BMad-Help

"The fastest way to get started" — an intelligent guide that inspects projects, detects completed work, and recommends next steps through natural language interaction. Reduces the steep learning curve.

### Party Mode

Orchestrates multiple agents in a single conversation, enabling brainstorming sessions and complex decisions requiring diverse perspectives.

### Quick Dev Workflow

Autonomously handles intent clarification → specification → implementation → review → presentation for small fixes and features — minimizing human checkpoints. Parallels CRISPY's approach to small-scope work.

### Checkpoint Preview

Interactive code review guide presenting changes by concern rather than file order, building reviewer comprehension progressively from design intent through implementation details.

## Development Flow

### Planning Phase (BMad Method Track)

1. Invoke PM agent → run `bmad-create-prd` workflow
2. PRD captures functional and non-functional requirements
3. Optional: UX Designer runs `bmad-create-ux-design`
4. Architect creates architecture document via `bmad-create-architecture`
5. PM creates epics/stories using both PRD and architecture as input
6. Architect validates implementation readiness

### Implementation Phase

1. Developer runs `bmad-sprint-planning` to initialize tracking
2. For each story:
   - Create story file via `bmad-create-story`
   - Implement via `bmad-dev-story`
   - Review via `bmad-code-review` (optional but recommended)
3. After epic completion, run `bmad-retrospective`

### Artifact Pipeline

```
Vision/Brainstorm → PRD → Architecture Doc → Epics/Stories → Implementation → Code Review → Retrospective
```

## Comparison with Other SDD Tools

From the [[spec-driven-development]] comparison:

| Dimension | BMAD | Spec-Kit | Kiro | Claude Code |
|-----------|------|----------|------|-------------|
| Philosophy | Full AI agile team | Spec → Code | IDE with SDD | Unopinionated platform |
| Scale | Quick Flow → Enterprise | Mid-size | Feature-level | Any |
| Workflow | Three tracks (adaptive) | Rigid (specify→plan→tasks→implement) | Rigid | Fully flexible |
| Setup time | Hours/days | Minutes | Install IDE | Minutes |
| Brownfield | Possible but heavy | Not optimized | Average | Excellent |
| Small fixes | Quick Flow (lightweight) | Overkill | Overkill | Ideal |

**Key distinction:** BMAD is an **opinionated framework** — it prescribes how you should work. Claude Code is an **unopinionated platform** — you assemble your own workflow. Since BMAD runs *on top of* Claude Code, they are **complementary, not competing**. In the [[agent-harness]] taxonomy, BMAD is a thick methodology harness layered over thinner agent SDK harnesses.

## Hybrid Model (BMAD + Spec-kit)

A notable approach from industry analysis combines BMAD's strategic planning with Spec-kit's tactical execution:

1. **Phase 1 — Strategic Planning (BMAD):** Analyst and Architect agents define vision, create PRD, establish system design. PM breaks PRD into epics/stories.
2. **Phase 2 — Feature Implementation (Spec-kit):** Developer takes a user story, runs Spec-kit's `/specify → /plan → /tasks → /implement` pipeline to generate code.
3. **Phase 3 — QA & Integration (BMAD):** Adversarial code review against original stories and acceptance criteria.

## Relevance

BMAD is significant to this research because:

1. **Most comprehensive SDD framework** — covers the full lifecycle, not just spec-to-code
2. **Multi-agent pioneer** — one of the earliest and most popular frameworks to simulate an entire Agile team with AI agents
3. **Validates the spec-driven thesis** — demonstrates that structured specifications lead to better AI output than ad-hoc prompting
4. **Anti-vibe-coding** — explicitly positions itself against unstructured "vibe coding", advocating for process and rigor
5. **Runtime-agnostic** — runs on multiple AI coding platforms, proving that methodology can be separated from tooling
6. **Adaptive complexity** — three-track system demonstrates SDD can scale down to bug fixes, not just up to enterprise

## Key Claims

- AI produces average results when it "does the thinking for you" — structured collaboration yields better outcomes
- Full Agile team simulation with AI is viable and productive for complex projects
- Three planning tracks prevent over-engineering small tasks and under-engineering large ones
- Multi-perspective collaboration ("Party Mode") catches issues that single-agent approaches miss
- Architecture-as-shared-context prevents multi-agent conflicts without requiring agent-to-agent communication
- Adversarial review ("no 'looks good' allowed") reduces confirmation bias
- Fresh chat per workflow keeps agents within effective [[instruction-budget]] limits
- The framework is complementary to, not competing with, AI coding platforms like Claude Code

## Strengths and Limitations

**Strengths:**
- Fills the gap between "just ask ChatGPT" and a full human SDLC team
- Correct emphasis on AI augmenting, not replacing, human thinking
- Full lifecycle coverage from ideation to QA
- Three-track system scales from bug fixes (Quick Flow) to enterprise systems
- Adversarial review and advanced elicitation improve output quality
- Customizable agents survive framework updates
- Large community (19.1k GitHub stars)

**Limitations:**
- High setup time (hours/days vs. minutes for simpler tools)
- Fresh chat requirement may cause knowledge loss between phases
- Heavy output volume (thousands of lines) can overwhelm context windows
- Prompt-dependent — model updates may require workflow adaptation
- Brownfield support unclear — no documented path for legacy codebases without existing architecture
- Named-persona approach (anthropomorphization) is untested — may help or hinder collaboration

## Open Questions

- How does the three-track system work in practice? Is there a clear heuristic for choosing tracks?
- Does the fresh chat requirement create knowledge loss between phases? How much context is reconstructed from artifacts?
- How does `project-context.md` handle evolving decisions — are agents confused by outdated entries?
- Is the named-persona approach more effective than anonymous role-based agents?
- How does BMAD handle brownfield projects with no existing architecture document?
- What happens when adversarial review and the developer agent disagree?
- How does it handle the [[instruction-budget]] problem across the full pipeline?
- Can the approach work for teams that don't follow Scrum/Agile?
- How does it compare to emerging approaches like [[dex-rpi-to-crispy|CRISPY]] which favor smaller, focused stages?

## Links

- [[bmad-method-docs]] — official documentation source page
- [[spec-driven-development]] — the methodology BMAD embodies
- [[context-engineering]] — project-context.md as shared context
- [[instruction-budget]] — fresh chat requirement as workaround
- [[agent-harness]] — BMAD as thick harness over thin SDK harnesses
- [[automation-levels]] — enables Level 3-4 in Shapiro's framework
- [[code-legibility-debate]] — BMAD's spec-as-source-of-truth stance is relevant
- [[software-factory]] — BMAD as a step toward automated software production
