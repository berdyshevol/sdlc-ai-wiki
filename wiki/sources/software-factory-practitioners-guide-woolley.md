---
title: The Software Factory: A Practitioner's Guide to Specification-Driven Development for Enterprise Services
type: source
pillar: software-factories
created: 2026-04-25
updated: 2026-04-25
sources: []
tags: [software-factory, spec-driven, attractor, shift-work, holdout-scenarios, nlspec, enterprise, soa]
---

# The Software Factory: A Practitioner's Guide to Specification-Driven Development for Enterprise Services

**Author**: Chad Woolley, GitLab  
**Date**: February 2026  
**Version**: 1.0  
**URL**: https://gitlab.com/cwoolley-gitlab/software-factory-practitioners-guide/-/blob/main/software-factory-practitioners-guide-v01.md  
**License**: UNLICENSE (public domain)

## Summary

This is the most comprehensive practitioner guide yet published on factory-pattern software development — authored by someone who has hands-on experience with the pattern while also being transparent about what doesn't work. Woolley positions the software factory as the Level 4-to-5 transition in [[five-levels-shapiro|Shapiro's taxonomy]], building on StrongDM's published work, GitHub's Spec Kit, and his own experiments with a forked version of Kilroy.

The guide's core insight: **factory-pattern development introduces a fundamental repository structure divide** — humans manage specifications (intent, contracts, constraints) and scenarios; machines produce implementation code; a separate validation process verifies correctness. The repository structure encodes this divide:
- `spec/` — human-managed (intent, contracts, constraints)
- `holdout-scenarios/` — human-authored validation kept hidden from coding agents
- `factory/` — human-written orchestration (Attractor graph)
- `src/` — machine-generated, opaque, version-controlled for auditability

The **key innovation** is holdout scenario validation — borrowed from ML practice, scenarios are kept hidden from the agents that build the code, preventing reward-hacking (agents optimizing for tests rather than genuine correctness).

The **shift work pattern** (StrongDM's terminology) separates interactive and non-interactive phases:
- **Interactive shift**: humans and agents collaborate on specifications, scenarios, and identifying gaps
- **Non-interactive shift**: the Attractor runs autonomously for hours or overnight, agents implement/test/converge without human involvement

**Honest about the difficulty**: Woolley explicitly states he has not yet produced usable software with the factory approach despite weeks of experimentation. The main lessons are about what *doesn't* work — particularly that you cannot take shortcuts on specification rigor. "The difficulties are real."

## Key Claims

1. **The factory pattern works, but only at small scale**: StrongDM (three-person team, greenfield codebase) has demonstrated it operationally. No large enterprise has publicly implemented it at scale. [[five-levels-shapiro|Shapiro]] claims Level 5 achieved only by very small teams; Woolley confirms no large enterprise has publicly shared a factory implementation.

2. **Specification engineering is the hard part, not the coding**: Getting specifications with machine-executable rigor — where you can't rely on a domain-aware human to "know what you really mean" — takes significant time and experience. This bottlenecks on human throughput, not agent capability.

3. **The Attractor pattern enables phase-based agent orchestration**: A directed graph in DOT format where each node is a development phase and edges are natural-language conditions. Different models can run different phases (reasoning-heavy for architecture, fast models for boilerplate). Each edge is evaluated by the LLM based on current codebase state.

4. **Provider-aligned agents perform best**: Anthropic models optimize for Claude Code's tool interfaces. OpenAI models optimize for their schemas. Forcing a universal toolset degrades performance. The factory should abstract over provider-specific agents so each phase can use the best model.

5. **The Digital Twin Universe (DTU) enables deterministic validation at scale**: Behavioral clones of every dependency (Okta API, Jira API, etc.) let you validate at volumes far exceeding production without hitting rate limits or costs. Building a DTU requires investment, but agents can build it from API documentation.

6. **Satisfaction is probabilistic, not binary**: Traditional testing asks "do all tests pass?" Factory validation asks "across all observed trajectories through all scenarios, what fraction likely satisfies the user?" A scenario might be satisfied 97% of the time; whether 97% is acceptable depends on the scenario's criticality and SLO requirements.

7. **Three separate agent sets prevent gaming**: (a) Spec-refinement agents help humans write specs and scenarios, never see the implementation code; (b) Factory execution agents implement code, never see the holdout scenarios; (c) Validation agents evaluate the built artifact, see neither source code nor specifications. This architectural separation prevents any agent set from optimizing for tests rather than correctness.

8. **Production observability feeding back to specification evolution is unsolved**: Three categories of production signals (behavioral drift, specification gaps, satisfaction regression) require different responses, but no existing system fully closes this loop. This is the largest open problem in factory-pattern systems.

9. **When is a specification "complete enough" for autonomous execution?** No formal criterion exists. Heuristics: (a) the "new-hire test" (would a capable newcomer implement correctly without interrupting you?), (b) scenario coverage (can you write holdout scenarios for every behavioral narrative?), (c) contract precision, (d) constraint measurability. Completeness remains a judgment call.

10. **Enterprise adoption faces critical barriers**: Governance (who approves spec changes?), agent security (permissions, credential scoping, blast radius), organizational transformation (redefining what it means to be a software engineer), cost management (StrongDM's $1,000/day benchmark is aggressive), and legal/compliance frameworks that assume human code review. These are separate from the core factory mechanics but critical for real-world adoption.

11. **SOA boundary coordination is a separate, unsolved problem**: When one service's downstream contract changes, consuming services must adapt. Contract change propagation across service boundaries — potentially automated — is the "factory of factories" vision, but no implementation guidance exists yet.

12. **Factory patterns apply beyond SOA**: Libraries, frameworks, standalone applications, infrastructure-as-code, and monoliths can all use the pattern where "what" can be expressed independently of "how."

## Key Concepts Introduced

- **NLSpec** (Natural-Language Specification): Markdown documents precise enough for agents to implement against, yet written in natural language a domain expert can author and review
- **Holdout scenarios**: End-to-end user stories kept separate from the codebase, preventing agents from optimizing for tests rather than behavior
- **Attractor pattern**: DOT-graph-structured orchestration of coding agents through phases until convergence
- **Shift work**: Separate interactive (spec refinement) and non-interactive (autonomous execution) phases
- **Satisfaction metric**: Probabilistic validation measuring what fraction of trajectories likely satisfy the user
- **Digital Twin Universe**: Behavioral clones of dependencies for deterministic, high-volume validation
- **Context/Intent Engineer**: The human role — writes specs, curates scenarios, configures factory, monitors production signals. Does not write code, does not review code

## Connections to Other Sources

- **[[five-levels-shapiro]]**: Woolley positions factory as Level 4-to-5 transition, extensively references Shapiro's taxonomy
- **[[superpowers-5]]**: The cascade pattern is a proto-factory pipeline; Woolley discusses Superpowers alongside BMAD and Spec Kit
- **[[spec-kit]]**: GitHub's framework used as reference for specification structure and "constitution" concept
- **[[bmad-method]]**: Discussed as one existing interactive-shift framework
- **[[everything-is-a-ralph-loop]]**: Geoffrey Huntley's Ralph Loop aligns with Woolley's feedback loops concept, though extends further into revenue optimization
- **[[cole-medin-ai-dark-factory]]**: Cole Medin's work on dark factories is referenced in context of factory patterns

**New references introduced**:
- **StrongDM Software Factory** (factory.strongdm.ai): The primary reference implementation. Shift work technique, gene transfusion, DTU, Attractor, CXDB
- **Kilroy**: Go-based Attractor implementation. Woolley forked it with deterministic pipeline generation
- **8090 Software Factory**: Modules for Refinery (requirements), Foundry (blueprints), Planner (work orders), Validator (feedback)
- **Sandgarden (sgai)**: Alternative approach treating code as ephemeral, never checked in
- **Microsoft AI-led SDLC prototype**: Combines Spec Kit with SRE Agent for production monitoring
- **Jujutsu (jj) VCS**: Git-compatible with operation log capturing mutation history for provenance
- **Stanford CodeX analysis** ("Built by Agents, Tested by Agents, Trusted by Whom?"): Legal and accountability analysis of factory-produced software

## Questions Raised

1. **Specification completeness**: Can we formalize the "completeness enough" criterion? Current heuristics (new-hire test, scenario coverage) are judgmental.

2. **Satisfaction thresholds**: What's the right satisfaction threshold? 95%? 99%? Should it vary by category (higher for security, lower for cosmetics)?

3. **Scenario authoring at scale**: How does hand-authoring scenarios scale to hundreds of behavioral paths? Agent-assisted authoring using separate agent sets is emerging, but quality/coverage mechanics are unproven.

4. **Production signals to specification amendments**: How do we systematically convert SRE anomalies into specification changes? The gap between "anomaly detected" and "intent amended" is currently bridged by human judgment.

5. **Factory pattern applicability to complex services**: Does the pattern work for services with thousands of behavioral paths and deep dependency chains? Specification engineering alone may be a bottleneck.

6. **SOA-scale coordination**: How do contract changes propagate across dozens or hundreds of factory-built services without creating chaotic coordination?

7. **Monoliths and monorepos**: These present different constraints than loosely-coupled services. Agents have no pre-existing codebase knowledge; context window limits (~1M tokens) are infinitesimal compared to domain expertise. How does the pattern adapt?

8. **Code provenance and supply chain**: Do auditors accept specification-level provenance, or will they continue to demand code-level review? Existing compliance frameworks assume human involvement.

9. **Source control evolution**: Should generated code be checked in (auditability, rollback) or treated as ephemeral (Sandgarden approach)? Which model serves enterprise needs better?

10. **Organizational transformation**: How do companies retrain/rehire as the skill profile shifts from code production to specification authoring, scenario design, and system thinking?

## Quotes Worth Keeping

> "The repository encodes a fundamental divide between what humans manage and what machines produce. A 'context/intent engineer' manages the human side: specifications (intent describing what the software should do and why, contracts defining exact API boundaries with neighboring services, constraints establishing non-negotiable invariants)... The machine side is code generated by agents — checked into version control for auditability, but treated as opaque output whose correctness is verified exclusively through externally observable behavior."

> "I have not yet produced usable software with this approach — early experiments have mainly revealed how hard it is to define specifications with machine-executable rigor."

> "The trajectory of software development is moving toward specification-driven, agent-executed production. The economics are compelling: if a specification can drive agents to produce correct, validated software faster and cheaper than human implementation, the industry will adopt it."

> "The skill that matters is not mastering today's toolchain. It is learning to think in specifications, to express intent precisely enough that machines can act on it, and to design validation systems rigorous enough to trust the output."

## Assessment

This is the most practical and honest guide to factory-pattern development yet published. Woolley's transparency about difficulties and unsolved problems (especially specification completeness and production feedback) actually increases credibility. He doesn't oversell the approach; he frames it as "aspirational" and acknowledges the gap between what's theoretically possible and what's been demonstrated at scale.

The guide's real contribution is systematizing what StrongDM has demonstrated into concrete practices — repository structure, specification layer definition, scenario separation, the Attractor pattern, shift work boundaries. It provides enough detail that a team could attempt to implement the pattern with full understanding of what's unsolved.

Key limitations: The guide focuses on greenfield services within SOA. It does not address governance, security, organizational transformation, or the legal/compliance questions that will determine mainstream adoption. These are acknowledged as critical but out-of-scope — which is honest, though it leaves enterprise teams without concrete guidance on adoption barriers.

For a wiki focused on SDLC AI automation, this is a primary reference for the "software factories" pillar, comparable in importance to [[five-levels-shapiro]] for the "automation levels" concept.
