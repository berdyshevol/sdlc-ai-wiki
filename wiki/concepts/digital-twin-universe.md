---
title: Digital Twin Universe (DTU)
type: concept
pillar: software-factories
created: 2026-04-25
updated: 2026-04-25
sources: [software-factory-practitioners-guide-woolley]
tags: [validation, testing, mocking, dependencies, deterministic]
---

# Digital Twin Universe (DTU)

## Definition

The **Digital Twin Universe** is [[strongdm|StrongDM]]'s term for **behavioral clones of every external dependency** that a service consumes. For StrongDM's own access management software, this means full replicas of:
- Okta's API
- Jira's API
- Slack's API
- Google Workspace APIs

These aren't simple mocks. They're behavioral clones that include:
- Full API endpoint coverage
- Edge cases and failure modes
- Realistic latency and response patterns
- Rate limiting behavior
- Partial/invalid request handling

## Why DTU?

The factory's [[attractor|Attractor]] converges by running [[holdout-scenarios|scenarios]] repeatedly against the built software. Validation at production scale is impractical:
- **Rate limits**: Hitting real APIs triggers rate-limit throttling
- **Cost**: High-volume testing accumulates API costs
- **Non-determinism**: Real services behave differently based on state; tests are unrepeatable
- **Isolation**: Testing against production data violates security and data residency policies

The DTU solves this by providing a **validation environment where agents can exercise the software realistically and repeatedly at scales far exceeding production limits**, with fully deterministic and replayable conditions.

## How DTU Works

The DTU is deployed alongside the factory during the [[shift-work|non-interactive shift]]. When the Attractor runs scenarios:

1. The built service connects to the DTU instead of real external services
2. The DTU responds with realistic behavior
3. Scenarios execute at any volume (1,000s of requests/sec) without hitting rate limits
4. Every run is deterministic and replayable — same inputs, same outputs
5. Failure modes (timeouts, invalid responses) can be injected and tested

## DTU as a Service Built by Agents

StrongDM's insight: **The DTU itself can be built by coding agents.** The process:
1. Take a service's public API documentation (OpenAPI, protobuf, etc.)
2. Feed it to a coding agent
3. Have the agent build a behavioral clone as a self-contained binary (or containerized service)
4. The agent can implement the happy path from docs, but also infer and implement common edge cases

This bootstrapping is itself a factory application — converting API specs into working mock services.

## Scaling DTU

Building a DTU at StrongDM's fidelity is a significant investment. But it scales down for smaller teams:

**At minimum**: Contract stubs for upstream services (mocking their APIs according to `spec/contracts/` definitions) plus a test harness that exercises downstream APIs.

**As the factory matures**: Invest in higher-fidelity twins that capture more realistic behavior.

**For services within your own SOA**: You may already have contract test suites or API simulators that serve as a foundation. The DTU formalizes this practice as first-class infrastructure.

## Determinism and Repeatability

A critical property: DTU behavior must be **deterministic and replayable**. Every scenario run should produce identical results given the same inputs, so the factory can reliably measure convergence.

For services with inherent randomness (e.g., generating UUIDs, timestamps), the DTU can either:
- Accept the variation (scenarios are scored probabilistically, not boolean)
- Seed randomness so runs are repeatable
- Stub out non-determinism (return fixed values during testing)

## Storage and State

The DTU needs to manage state (database records, service state) that scenarios expect to find. Options:
- **Ephemeral per scenario**: Reset state before each scenario, test against clean state
- **Persistent per run**: Maintain state across scenarios within a single factory run
- **Stateless**: DTU doesn't persist state; scenarios are designed to be independent

The choice depends on whether scenarios need to test state transitions across multiple interactions.

## Validation Environment Setup

From [[software-factory-practitioners-guide-woolley]]:

The DTU is part of the broader validation environment:
1. **Contract stubs** (upstream services the built software calls)
2. **DTU** (behavioral clones of external dependencies)
3. **Built artifact** (the software under test, running as a service)
4. **Scenario harness** (drives scenarios, observes outcomes, computes satisfaction scores)

This entire environment is typically ephemeral — spun up for a factory run, torn down afterward — or containerized for repeatability.

## Cost and Complexity Tradeoff

Building a comprehensive DTU requires:
- API documentation review
- Behavioral cloning (agent-assisted or manual)
- Testing the DTU's correctness against the real service
- Maintenance as the real service's API evolves

The tradeoff: high upfront cost, but then unlimited high-volume deterministic testing.

For teams not ready to invest in a DTU: Start with simpler contract stubs and accept lower validation coverage. The DTU concept is aspirational infrastructure, not a requirement for a functional factory.

## Related Concepts

- [[holdout-scenarios]] — Scenarios run against the DTU
- [[attractor]] — The factory uses DTU during convergence checking
- [[shift-work]] — DTU is non-interactive shift infrastructure
- [[software-factory]] — The pattern that uses DTU
- [[strongdm]] — Created the concept

## Open Questions

1. **DTU maintenance**: How do you keep the DTU in sync with real API changes? Is there a contract-based mechanism to auto-update DTU when external APIs change?

2. **Partial DTU**: For services with many dependencies, do you need complete DTUs for all, or can you mock some and use real services for others?

3. **Chaos engineering**: Can the DTU inject failures (timeout, error responses, slow responses) for scenario testing? Should this be part of the standard DTU?

4. **Comparison to staging**: How does DTU differ from staging environments? Both provide isolated testing space. Is DTU essentially "better staging" or fundamentally different?

5. **DTU for brownfield services**: Building a DTU requires API knowledge. For legacy services with undocumented APIs, how would you construct a DTU?
