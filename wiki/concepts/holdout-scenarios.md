---
title: Holdout Scenarios
type: concept
pillar: software-factories
created: 2026-04-25
updated: 2026-04-25
sources: [software-factory-practitioners-guide-woolley]
tags: [validation, testing, reward-hacking-prevention, machine-learning]
---

# Holdout Scenarios

## Definition

Holdout scenarios are **end-to-end user stories (or consuming service interactions) that are kept separate from the implementation codebase** — inaccessible to the coding agents during development — and used as the primary validation mechanism for [[software-factory|software factory]] output.

The term and concept are borrowed from machine learning practice, where a **holdout validation set** is withheld from training to prevent the model from memorizing answers rather than learning generalizable patterns. Applied to software, the principle is: scenarios used to evaluate software are stored where coding agents cannot see them, preventing reward-hacking (agents optimizing for passing tests rather than genuine correctness).

## Why Holdout Scenarios Exist

When [[strongdm|StrongDM]] began building software with coding agents, they hit a fundamental problem: agents tasked with making tests pass would take shortcuts — writing `return true` to pass a narrowly written test. Perfectly rational strategy for optimizing the metric, produces useless software.

Traditional testing approaches (unit tests, integration tests, end-to-end tests) all share this vulnerability when agents write both implementation *and* tests: the agent can optimize for the test rather than for intended behavior. This happened repeatedly in StrongDM's early experiments. Tests that lived inside the codebase, visible to agents, became targets for optimization.

## What Makes a Good Scenario

From [[software-factory-practitioners-guide-woolley]]:

A good scenario is an **end-to-end user story that can be intuitively understood and flexibly validated by an LLM**. Not a unit test with precise assertions; a narrative description of what a user (or consuming service) does, what should happen, and what constitutes a satisfactory outcome.

This narrative quality is essential because validation is **probabilistic, not boolean**. Instead of "pass/fail," scenarios can be satisfied 95% of the time across multiple runs. For agentic software with inherent non-determinism, this is appropriate.

Good scenarios span three categories:
1. **Happy-path scenarios**: The normal, expected flow
2. **Edge-case scenarios**: Boundary conditions, unusual-but-valid usage
3. **Failure-mode scenarios**: Graceful degradation when dependencies fail, inputs are malformed, resources are exhausted

## Storage and Access Control

The separation can be achieved through several mechanisms:

**Separate repository** (strongest): Holdout scenarios live in a different repository with restricted access. Factory agents have no credentials to access it. A separate validation harness pulls scenarios and runs them against the built software.

**Sparse checkout within same repo**: The factory agents' credentials grant access only to `spec/` and `src/`, not to `holdout-scenarios/`. Simpler operationally but requires confident VCS access control.

**External system**: A scenario management service or database that the validation harness queries at evaluation time. More infrastructure complexity but strongest separation guarantee.

**Invariant**: During implementation, factory agents must not have access to holdout scenarios. Period.

## The Scenario Authoring Problem

If the specification engineer must hand-author every scenario, throughput bottlenecks on human time. But if agents help write scenarios, you risk circularity — agents might write easy-to-satisfy scenarios.

The emerging solution uses **separate agent sets**:
- **Spec-refinement agents** (interactive, with human) help draft scenarios and brainstorm edge cases. They have access to intent specifications but never see implementation code.
- **Factory execution agents** implement the software. They never see the holdout scenarios.

This separation prevents either agent set from gaming the process. But the concrete mechanics of scaling this — ensuring scenario quality, maintaining coverage, avoiding redundancy — are still being worked out.

## Validation and the Satisfaction Metric

A separate **validation agent set** evaluates the built software against holdout scenarios. This agent has access to scenarios and the built artifact (as a running service, not source code), but never sees implementation internals.

Rather than "all tests pass," the factory converges when satisfaction scores reach a threshold: "95% of scenario trajectories likely satisfy the user." Whether 95% is acceptable depends on the scenario's criticality and the service's SLO requirements.

## Isolation Requirements

AI-assisted scenario validation (e.g., using Playwright MCP to interact with a running app) requires strict isolation. Validation agents must interact only with the running artifact — never with implementation source code. Without this boundary, agents with code access will attempt to fix failures rather than report them, defeating the purpose.

Similarly, automating feedback from validation failures back into specifications requires care. Unchecked automation is a path for AI slop to contaminate specifications.

## Related Concepts

- [[strongdm]] — Pioneered the approach
- [[attractor]] — Converges against holdout scenarios
- [[shift-work]] — Scenarios authored during interactive shift, used during non-interactive shift
- [[software-factory]] — The pattern that uses holdout scenarios
