---
title: Shift Work
type: concept
pillar: software-factories
created: 2026-04-25
updated: 2026-04-25
sources: [software-factory-practitioners-guide-woolley]
tags: [interactive, non-interactive, boundary, autonomous-execution, specification-completeness]
---

# Shift Work

## Definition

**Shift work** is [[strongdm|StrongDM]]'s terminology for the separation of [[software-factory|software factory]] development into two distinct phases:

1. **Interactive shift**: Humans and agents collaborate on specification, identify gaps, author scenarios, and configure the factory. Iterative, conversational, goal-directed at reaching specification completeness.

2. **Non-interactive shift**: The [[attractor|Attractor]] runs autonomously — potentially for hours or overnight — implementing, testing, refining, and converging without human intervention. Humans check the satisfaction score when finished.

The term evokes a factory floor where different shifts perform different work. The critical unsolved question: **when is a specification "complete enough" to hand off from interactive to non-interactive?**

## The Interactive Shift

**Purpose**: Collaborative refinement of specifications and validation scenarios until the specification is complete enough for autonomous execution.

**Participants**:
- Human: context/intent engineer (writes intent, contracts, constraints, reviews and approves amendments)
- **Spec-refinement agents** (assist with brainstorming, identify gaps, draft specification language, propose scenarios)

**Inputs**: Domain knowledge, user intent, existing contracts (for SOA services), architectural decisions

**Outputs**: 
- Intent specification (NLSpec) with behavioral narratives and architectural rationale
- Upstream and downstream contracts (precise API boundaries)
- Constraints (SLOs, security requirements, operational limits)
- Holdout scenarios (validated to have good coverage and edge-case depth)
- Factory configuration (Attractor graph, phase prompts)

**Tools**: Agentic TUI (Claude Code, Cursor, Copilot Workspace, etc.), text editor, conversation

**Key Properties**:
- Can't rely on agents alone to generate specifications — Woolley emphasizes that shortcutting this phase ("just let AI write the spec") leads to failure
- Requires deep human involvement: "You have to be deeply involved in creating the specification, understand it thoroughly, and fully grasp how it drives factory operation"
- Iterative: specifications are refined through multiple cycles, often triggered by discovering gaps

## The Non-Interactive Shift

**Purpose**: Autonomous software production — converting complete specifications into working, tested, validated code without human intervention.

**Participants**:
- **Factory execution agents** (the Attractor) — implement, test, refine, and converge
- **Validation agents** (separate from execution) — evaluate against holdout scenarios
- No humans (except for monitoring and checking final satisfaction scores)

**Inputs**: Specifications (intent, contracts, constraints), Attractor configuration, [[holdout-scenarios|holdout scenarios]]

**Outputs**: 
- Implemented source code (in `src/` or equivalent)
- Test suites
- Build artifacts
- Convergence log (which phases ran, what failed, how it was fixed)
- Satisfaction score

**Duration**: Hours to overnight for typical services. StrongDM's experiments ran continuously for extended periods.

**Key Properties**:
- Factory agents never see the holdout scenarios (prevents reward-hacking)
- Validation agents never see the implementation source code (prevents biased evaluation)
- Declarative specification drives agent behavior; agents don't require interactive guidance
- Deterministic (given same specs and same models, should produce consistent results, though minor non-determinism is tolerated)

## The Boundary Question: When Is Specification Complete?

This is the **central unsolved problem** in factory-pattern development. Woolley identifies several heuristics but explicitly states no formal criterion exists:

1. **The new-hire test** (GitHub Spec Kit): Would a capable new hire, given only this specification and no other context, implement correctly without interrupting you more than once?

2. **Scenario coverage**: Can you write holdout scenarios for every behavioral narrative in intent and every edge case in contracts? If you can't articulate what correct behavior should be, the spec has gaps.

3. **Contract precision**: Are upstream and downstream API specifications precise enough that you could hand-write an integration test against them?

4. **Constraint measurability**: Does every constraint have a corresponding measurement? If it can't be measured by the validation harness, it's aspirational guidance, not factory input.

5. **No assumptions about implementation**: Would an agent implementing this spec make reasonable decisions when the spec is silent? If you're uncertain, the spec is incomplete.

## Repository Structure Encoding the Shift

The repository layout encodes which shift owns what:

```
spec/              ← Human-managed (interactive shift output)
├── intent/        ← Intent specifications
├── contracts/     ← API boundaries
└── constraints/   ← Non-negotiable invariants

holdout-scenarios/ ← Human-authored, machine-tested (interactive authoring, non-interactive validation)

factory/           ← Factory configuration (human-authored, non-interactive execution)
├── service.dot    ← Attractor graph
└── attractor-config/

src/               ← Machine-generated (non-interactive shift output)
└── [implementation, tests, etc.]

docs/              ← Human-facing documentation
```

The `spec/`, `holdout-scenarios/`, `factory/`, and `docs/` directories are all outputs of the interactive shift. `src/` is the output of the non-interactive shift. `factory/` bridges — human-authored, but defines how non-interactive shift runs.

## Separate Agent Sets Enforce the Boundary

Three separate agent sets prevent gaming the shift work pattern:

1. **Spec-refinement agents**: Interactive, have specs and scenario drafts, never see implemented code. Can't write easy-to-satisfy scenarios because they don't know code structure.

2. **Factory agents** (Attractor): Non-interactive, have specs, never see holdout scenarios. Can't optimize for test-passing because they can't see tests.

3. **Validation agents**: Have scenarios and running artifact, never see source code. Can't inflate scores through code inspection.

## Open Questions

1. **Partial specification handoff**: Can you run the non-interactive shift with an 80%-complete specification and then refine based on what failed? Or does incompleteness guarantee failure?

2. **Rapid iteration**: If specifications change frequently (daily, hourly), is the shift work pattern still practical? Each change triggers the non-interactive shift, which costs token spend.

3. **Human feedback during non-interactive shift**: If the factory converges to an unsatisfactory state, can the human step in (moving back to interactive shift) to refine the spec, or must the cycle complete?

4. **Specification drift**: As the non-interactive shift produces code and validation reveals gaps, what counts as a specification amendment (requires interactive refinement) vs. a factory bug (correct the Attractor configuration)?

## Comparison to Related Patterns

- **CI/CD pipelines**: Shift work is similar in spirit (automated testing after code committed) but inverts the trust model. CI assumes humans wrote the code; the factory assumes agents did.
- **BMAD's phases**: BMAD has Analysis → Planning → Solutioning → Implementation phases with human approval gates. Similar phase structure but less formal separation of agent responsibilities.
- **Superpowers' brainstorm→plan→implement**: Mandatory workflow gates but less emphasis on agent set isolation.

## Related Concepts

- [[attractor]] — The non-interactive shift engine
- [[holdout-scenarios]] — Validated during non-interactive shift
- [[software-factory]] — The pattern that uses shift work
- [[strongdm]] — Pioneered the terminology
