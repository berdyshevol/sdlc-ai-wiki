---
title: StrongDM
type: entity
created: 2026-04-25
updated: 2026-04-25
sources: [software-factory-practitioners-guide-woolley]
tags: [company, software-factory, access-management, zero-trust]
---

# StrongDM

## Overview

StrongDM is a security infrastructure company that in February 2026 published the first detailed public account of a production software factory in operation. A three-person team built access management software (controlling permissions across Okta, Jira, Slack, Google Workspace) under two foundational rules: no human writes code, no human reviews code.

Founded c. 2015 (TBD — verify). Based in the US. Series-stage (TBD — verify funding).

## Relevance to This Research

StrongDM is the **primary reference implementation** for the software factory pattern in practice. [[five-levels-shapiro|Shapiro's taxonomy]] is theoretical; StrongDM's published experience is operational. They've demonstrated:
- The Attractor pattern works for non-interactive agent orchestration
- Holdout scenarios prevent reward-hacking in agent-driven development
- Shift work (interactive spec refinement vs. non-interactive autonomous execution) separates human and machine responsibilities effectively
- A small, experienced team can produce working, tested software without human code review

## Key Claims and Contributions

From [[software-factory-practitioners-guide-woolley]] and references:

1. **The Attractor pattern** — DOT-graph-based orchestration of coding agents through phases (implement, test, refine, validate) until convergence. Agents traverse the graph autonomously, deciding at each transition whether criteria are met to advance.

2. **Holdout scenario validation** — Scenarios used to evaluate software are stored separately from the codebase, inaccessible to implementation agents during building. This prevents agents from optimizing for tests rather than genuine correctness. Borrowed from machine learning practice (holdout validation sets).

3. **Shift work pattern** — Separation of interactive shift (humans + agents collaborating on specs/scenarios) from non-interactive shift (factory running autonomously). The boundary between them (when specs are "complete enough") is the central design decision.

4. **Digital Twin Universe (DTU)** — Behavioral clones of all external dependencies (Okta, Jira, Slack, Google Workspace APIs) enabling deterministic, high-volume validation without hitting rate limits or accumulating API costs. Can itself be built by agents from API documentation.

5. **Satisfaction metric** — Probabilistic validation: "across all observed trajectories through all scenarios, what fraction likely satisfies the user?" A shift from boolean (pass/fail) to probabilistic (97%, 95%) validation, necessary for agentic software with inherent non-determinism.

6. **CXDB** — Context database storing agent conversations, tool outputs, and convergence history. Internal to the factory's operation.

7. **StrongDM ID** — Identity management for humans, workloads, and AI agents with federated authentication and path-scoped credential sharing.

8. **Gene transfusion** — Moving working patterns between codebases by pointing agents at concrete exemplars. For specifications, means copying successful specification patterns from one service to another (pattern, not code).

## Limitations and Open Questions

1. **Scale demonstrated**: Only at a small startup team (3 people), greenfield codebase, no customers yet. How it scales to enterprise teams, brownfield codebases, established customer bases remains unproven.

2. **Production observability**: The largest unsolved problem. How production signals (behavioral drift, specification gaps, satisfaction regression) feed back into specification evolution is acknowledged as unsolved.

3. **SOA boundary coordination**: When one service's contract changes, how does that propagate to consuming services? Unsolved at scale.

4. **Code provenance and compliance**: Factory-produced software lacks the commit-by-commit audit trail existing compliance frameworks assume. StrongDM's answer: treat specifications as the auditable source, generated code as build artifact. Whether auditors accept this is unproven.

## Links

- **Website**: https://strongdm.com
- **Software Factory documentation**: https://factory.strongdm.ai
- **Techniques**: https://factory.strongdm.ai/techniques/shift-work
- **Attractor (GitHub)**: https://github.com/strongdm/attractor

## Related Concepts

- [[attractor]] — The orchestration pattern
- [[shift-work]] — Interactive/non-interactive boundary
- [[holdout-scenarios]] — Validation approach
- [[digital-twin-universe]] — Validation environment
- [[software-factory]] — The pattern they're implementing
