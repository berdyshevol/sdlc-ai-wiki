---
title: Natural-Language Specification (NLSpec)
type: concept
pillar: spec-driven
created: 2026-04-25
updated: 2026-04-25
sources: [software-factory-practitioners-guide-woolley]
tags: [specification, intent, markdown, machine-executable]
---

# Natural-Language Specification (NLSpec)

## Definition

**NLSpec** is the term coined by [[strongdm]] to describe markdown documents that serve as specifications precise enough for [[software-factory|factory]] agents to implement against, yet written in natural language that a domain expert can author and review without programming knowledge.

An NLSpec is not a traditional requirements document, user story, or product requirements document (PRD), though it shares DNA with all three. The goal: **express what the software should accomplish and why**, not how.

## Why "Intent" Over "Requirements"

The terminology choice matters. [[software-factory-practitioners-guide-woolley|Woolley]] selected "intent specifications" deliberately over "requirements" because it aligns with factory philosophy: humans express what should happen and why it matters to the user, not prescribe implementation details.

## Structure and Content

An effective NLSpec answers three questions for every significant behavior:
1. **What should happen?** (the behavior)
2. **Under what conditions?** (the constraints/context)
3. **Why does this matter to the user?** (the rationale)

### Example
**Poor**: "Users must authenticate before accessing resources"  
**Good**: "Users must authenticate before accessing resources because this service manages sensitive permission data, and unauthenticated access would violate our zero-trust security model. When authentication fails, the service should return a 401 response and log the attempt for audit."

The second version gives the agent context for making reasonable decisions when the spec is silent on edge cases. If the spec says "zero-trust," the agent can infer to fail closed rather than open.

## Organization

NLSpec documents are organized around **behavioral narratives** rather than technical components:

- **User journeys** (or, in an SOA context, **consuming service journeys**) describe end-to-end flows from the perspective of the service's consumers
- **Decision records** capture significant architectural choices and their rationale
- **Scenarios and examples** illustrate expected behavior concretely

The goal is to give agents enough context that they can infer reasonable behavior for unspecified edge cases.

## Machine-Executable Rigor

The challenge: NLSpec must be **precise enough for agents to implement** while remaining **natural language enough for humans to author and review**. This is where the difficulty lies.

[[software-factory-practitioners-guide-woolley|Woolley]] emphasizes: "You cannot take shortcuts by relying too heavily on AI to generate the specification... The difficulties are real. Defining specifications with machine-executable rigor, when you can't rely on an experienced domain-aware human to 'know what you really mean.'"

An NLSpec that's too vague (relying on human domain knowledge to fill gaps) will cause agents to make wrong assumptions. An NLSpec that's too rigid (prescribing implementation details) defeats the purpose of specification-driven development.

## Example Structure (From CLAUDE.md)

For a service within an SOA:

```
spec/
├── intent/
│   ├── overview.md          # High-level purpose and domain model
│   ├── user-journeys.md     # End-to-end flows
│   └── architecture.md      # Significant design decisions and rationale
├── contracts/
│   ├── upstream.md          # What we consume from other services
│   └── downstream.md        # What we promise to consumers
└── constraints/
    ├── slos.md              # Latency, error budget, throughput targets
    ├── security.md          # Auth, encryption, authorization
    └── operational.md       # Memory, CPU, deployment topology
```

## Relation to Other Specification Concepts

- **Spec Kit's "Constitution"** (GitHub): Similar in spirit — immutable principles applied to all changes
- **BMAD's "project-context.md"**: Shared context across agent personas, similar information density
- **CodeSpeak's `.cs.md` files**: Markdown specs for code generation, aligned with NLSpec philosophy but more focused on code-generation specifics

## The Scenario Connection

[[holdout-scenarios]] are authored based on NLSpec intent. If you can't write a scenario because you don't know what correct behavior is, the NLSpec has a gap. This creates a feedback loop: incomplete NLSpec → can't author scenarios → reveals where spec needs to be more precise.

## Authoring Process

Interactive shift activity (human + spec-refinement agents):
1. Domain expert describes intent
2. Agent asks clarifying questions, identifies gaps
3. Agent proposes specification language
4. Human reviews, approves, or refines
5. Iterate until coverage feels complete
6. Author holdout scenarios to test coverage
7. Return to step 2 if gaps are revealed

Woolley notes this process "takes significant time and experience." The shortcut of having agents write specs alone leads to vague, implementable specifications that agents then exploit.

## Related Concepts

- [[shift-work]] — NLSpec is the output of the interactive shift
- [[holdout-scenarios]] — Scenarios validate NLSpec completeness
- [[spec-driven-development]] — NLSpec is the primary artifact
- [[strongdm]] — Coined the term

## Open Questions

1. **Measurement of completeness**: Can we formalize when an NLSpec is "complete enough" for autonomous implementation?

2. **Scaling to complexity**: How much specification detail is required for a service with hundreds of behavioral paths? At what point does NLSpec become unwieldy?

3. **Multi-team authoring**: How do multiple teams collaborate on a single NLSpec without introducing inconsistencies?

4. **Tooling gaps**: What tools would make NLSpec authoring more efficient? Structure templates? AI-assisted gap detection? Consistency checking?

5. **Evolution and versioning**: As production signals reveal gaps or new requirements emerge, how should NLSpec be versioned? Does each change trigger a factory rebuild?
