---
title: "BMAD Method — Official Documentation"
type: source
pillar: spec-driven
created: 2026-04-09
updated: 2026-04-09
sources: [bmad-method-docs]
tags: [bmad, framework, multi-agent, spec-driven, methodology, agile, documentation]
author: bmadcode
url: https://docs.bmad-method.org/llms-full.txt
---

# BMAD Method — Official Documentation

## Metadata

- **Author:** bmadcode
- **URL:** https://docs.bmad-method.org/llms-full.txt
- **Pillar:** [[spec-driven-development]]
- **Raw file:** `raw/bmad-method-docs.md`

## Summary

The official BMAD documentation provides a comprehensive look at the framework's internal architecture, agent system, and workflow mechanics — far more detail than was available from secondary sources previously ingested. BMAD is revealed to be more nuanced than the initial entity page suggested: it offers **three planning tracks** (Quick Flow, BMad Method, Enterprise) that adapt to project complexity, directly addressing the earlier criticism that BMAD is "overkill for small projects."

The framework is structured around a **four-phase development cycle**: Analysis → Planning → Solutioning → Implementation. Each phase is served by specialized AI agent personas with named identities (Analyst "Mary", PM "John", Architect "Winston", Developer "Amelia", UX Designer "Sally", Technical Writer "Paige"), each with dedicated skill IDs and workflow sets. Agents are customizable via `.customize.yaml` files that survive framework updates.

A key architectural insight is the **project-context.md** file — a shared document capturing technology stack versions and implementation rules that ensures consistency across agents implementing different epics. This directly addresses the multi-agent coordination problem: rather than agents communicating with each other, they all read from a shared specification of conventions and constraints. This is a form of [[context-engineering]] — using static artifacts as shared ground between agents, similar to Dex's "Mental Alignment" concept from [[dex-rpi-to-crispy]].

The documentation also reveals several sophisticated patterns: **adversarial review** (mandating that reviewers find problems — "no 'looks good' allowed"), **advanced elicitation** (second-pass analysis using pre-mortem, inversion, and first-principles reasoning), and a **fresh chat requirement** (each workflow runs in a new session to prevent context contamination). The fresh chat requirement is a practical acknowledgment of the [[instruction-budget]] problem — by resetting context between workflows, BMAD keeps each agent's instruction set manageable.

## Key Claims

- **Three planning tracks solve the "overkill" problem.** Quick Flow handles bug fixes and small features with just a tech-spec; the full BMad Method adds PRD + architecture for standard products; Enterprise track adds comprehensive documentation for compliance-heavy systems. This is adaptive complexity management in practice.

- **Architecture-as-shared-context prevents multi-agent conflicts.** Rather than agents communicating directly, documented architecture decisions (API style, database technology, auth approach, state management, naming conventions) create a shared reference that all agents consult. This is a coordination-through-artifacts pattern.

- **Adversarial review mandates finding problems.** The code review workflow explicitly forbids "looks good" responses. Reviewers must assume issues exist and surface specific findings. This addresses confirmation bias in approval workflows — a problem [[superpowers-5]] also tackles with adversarial spec review.

- **Fresh chats for each workflow** prevent context window overflow. This is a practical solution to the [[instruction-budget]] problem: rather than cramming all agent instructions into one session, each workflow gets a clean context window with only its relevant instructions.

- **`project-context.md` as implementation guardrails.** This file captures technology stack versions and implementation rules that agents might otherwise miss or hallucinate. It's a form of [[context-engineering]] — ensuring agents have the right constraints without overloading them with full project documentation.

- **Named agent personas with specific skill IDs** create clear role boundaries. Each agent has defined workflows it can run, preventing role confusion and ensuring the right expertise is applied at each phase.

- **`bmad-help` as intelligent onboarding.** The help system inspects the project, detects completed work, and recommends next steps — reducing the steep learning curve identified as a limitation in earlier analysis.

- **Checkpoint Preview** presents code review by concern rather than file order, building reviewer comprehension progressively. This addresses the code review cognitive load problem.

- **Quick Dev workflow** autonomously handles the full cycle (intent → spec → implement → review → present) for small tasks, minimizing human checkpoints. This parallels CRISPY's approach to small-scope work.

## Connections

- **[[bmad-method]]** — This source provides the detailed internals for the existing entity page, resolving several open questions.

- **[[context-engineering]]** — BMAD's `project-context.md` and architecture-as-shared-context patterns are practical implementations of context engineering. The "Mental Alignment" concept from [[dex-rpi-to-crispy]] describes the same idea: static artifacts as shared ground between human and agent.

- **[[instruction-budget]]** — The fresh chat requirement is a direct response to context window limitations. By resetting between workflows, BMAD keeps each agent's instruction set within the effective range (~150-200 instructions per Dex's data).

- **[[spec-driven-development]]** — BMAD's three-track system (Quick Flow / BMad Method / Enterprise) shows how SDD can scale across project complexity levels, addressing the criticism that SDD frameworks are inherently heavyweight.

- **[[agent-harness]]** — BMAD is effectively a thick harness that runs on top of thinner harnesses (Claude Code, Cursor, Windsurf). It sits at the methodology layer above the agent SDK layer, prescribing workflows rather than just providing infrastructure.

- **[[superpowers-5]]** — Both BMAD and Jesse Vincent's work emphasize adversarial review as a quality gate. BMAD's "no 'looks good' allowed" policy is the most explicit articulation of this principle in the wiki.

- **[[dex-rpi-to-crispy]]** — BMAD's Quick Dev workflow parallels CRISPY's approach to small tasks. Both recognize that full planning pipelines are overkill for bug fixes and small features. The three-track system (Quick Flow / BMad Method / Enterprise) mirrors CRISPY's emphasis on right-sizing process to task complexity.

## Questions Raised

- How does the three-track system work in practice? Is there a clear heuristic for choosing Quick Flow vs. BMad Method vs. Enterprise, or does it require judgment?
- Does the fresh chat requirement create knowledge loss between phases? How much context is reconstructed from artifacts vs. lost entirely?
- How does `project-context.md` handle evolving decisions — are agents ever confused by outdated entries?
- Is the named-persona approach (Mary, John, Winston, etc.) more effective than anonymous role-based agents? Does anthropomorphization improve or hinder human-AI collaboration?
- How does BMAD handle brownfield projects where no existing architecture document exists? Does the Architect agent generate one from code analysis?
- What happens when adversarial review and the developer agent disagree? Is there an escalation path?
