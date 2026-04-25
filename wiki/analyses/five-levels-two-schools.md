---
title: Five Levels, Two Schools — The Divergence in AI-Driven SDLCs
type: analysis
pillar: industry
created: 2026-04-25
updated: 2026-04-25
sources: [five-levels-shapiro, dex-rpi-to-crispy, humanlayer-codelayer, software-factory-practitioners-guide-woolley, long-running-claude]
tags: [automation-levels, human-in-the-loop, dark-factory, sdlc, divergence, industry-landscape]
---

# Five Levels, Two Schools — The Divergence in AI-Driven SDLCs

## Question

How is AI currently being adopted across the software development lifecycle (SDLC), and what are the competing visions for how teams should structure human and machine work as automation increases?

## Framework: Shapiro's Five Levels

[[five-levels-shapiro|Dan Shapiro's five-level taxonomy]] provides the organizing structure:

- **Level 1**: Spicy Autocomplete — AI as inline code suggestion (GitHub Copilot)
- **Level 2**: Pair Programming — Human + AI in real-time conversation; human drives, AI assists
- **Level 3**: AI as Code Reviewer — Humans write code, AI reviews; human still decides
- **Level 4**: AI as Engineering Manager — Human writes specs, AI implements and makes decisions; human manages
- **Level 5**: Dark Factory — Fully autonomous software production; specs in, working software out, no human review

## Current State: The Two Schools

The industry has bifurcated into **two distinct schools** at Levels 4+ — different philosophies about how to structure human-AI collaboration as automation increases.

### School 1: The Human-in-the-Loop School (HumanLayer / CRISPY)

**Founders/Primary Voices**: Dex Horthy (HumanLayer), Siddharth Mishra-Sharma (Anthropic), Jesse Vincent (Superpowers)

**Core Philosophy**: **Automation should amplify human judgment, not replace it.** Human engineers remain central to decision-making. AI augments their capabilities across all SDLC stages.

**Key Slogan**: "The AI is a collaborator, not a replacement. Success means your best engineers become 10x, not that you replace engineers with AI."

#### Level 1-2: Interactive Augmentation
- Copilot-style inline suggestions (Level 1)
- Agentic pair programming with Claude Code/Cursor (Level 2)
- Human reviews AI-generated code before committing

#### Level 3: Structured Code Review
- **RPI methodology failure** → **CRISPY reversal**: Dex's original RPI (Reasoning, Planning, Implementation) assumed code could be opaque. Experience revealed this was wrong.
- **Code legibility imperative**: Engineers must read and understand AI-generated code. School 1 has reversed position.
- **Adversarial review**: Use AI to review AI, but humans make final calls

#### Level 4: Specification-Driven with Human Oversight
**The CRISPY Model** (7-stage workflow):
1. **Critique** — AI and human brainstorm spec, identify gaps
2. **Revise** — Human refines spec based on critique
3. **Specification Finalized** — Human approves, specs frozen
4. **Plan** — AI generates implementation plan (human reviews)
5. **Implementation** — AI implements; human watches/adjusts
6. **Testing** — AI + human validate together
7. **Complete** — Human sign-off before merge

**Key Properties**:
- Humans remain in the loop at critical gates (spec approval, plan review, final validation)
- Code is produced by AI but **owned by humans** — humans can read, understand, and modify it
- Instruction budget discipline: Each stage is <40 instructions, focused and clear
- Mental alignment via static artifacts: CLAUDE.md as living spec, project context as shared reference

**Tools/Platforms**:
- [[humanlayer-codelayer|CodeLayer]] (HumanLayer's IDE)
- [[bmad-method|BMAD Method]] (6 agent personas, adversarial review, project-context.md)
- [[spec-kit]] (GitHub's SDD toolkit with mandatory gates)
- [[superpowers]] (skills framework with brainstorm→plan→execute→review workflow)
- [[claude-agent-sdk]] (thin harness, trust the model philosophy)

**Current Industry Distribution**: **Levels 2-3 predominate**. Most teams using Copilot (L1) or agentic pair programming (L2). Spec-Kit and BMAD users are at L3-early-L4. **No mainstream adoption of full L4 CRISPY workflows yet** — early adopters (HumanLayer internal, some Anthropic research teams) only.

**Cost Model**: Human engineers stay expensive (still coding, now also overseeing AI). Token costs moderate ($100-300/day per engineer). Suitable for teams valuing engineer agency and code ownership.

**Problem It Solves**: Prevents "AI slop" contamination of codebases. Maintains human understanding of architecture. Creates defensible audit trails (humans approved each stage).

#### Level 5: Not Endorsed by This School

School 1 explicitly rejects the Level 5 dark factory vision.

**Dex's position** (from [[matt-pocock-dex-horthy-chat]]): *"Ralph [autonomous loop] is probably not the right final answer for production software. If anything, it's an incredible lesson in how context windows work."*

**Concern**: Autonomous software without human review creates code that no human can understand or modify. At scale, this becomes a liability (debugging, security audits, compliance, evolution).

---

### School 2: The Dark Factory School (StrongDM / Autonomous)

**Founders/Primary Voices**: StrongDM's AI team (Simon Willison's account, [[software-factory-practitioners-guide-woolley|Chad Woolley's guide]]), Geoffrey Huntley ([[everything-is-a-ralph-loop|Ralph Loop]])

**Core Philosophy**: **Humans specify intent and validate outcomes; machines produce implementation.** Humans should not read or review code — it's an opaque artifact verified exclusively through observable behavior.

**Key Slogan**: "Code is the last-mile implementation detail. Specifications and validation are where human intelligence matters. Generated code is like compiled binaries — no one reads assembly."

#### Level 1-2: Delegated Generation
- AI generates code from descriptions
- Humans don't review generated code; specs and tests are sufficient
- Focus: specs precise enough that agent can implement correctly

#### Level 3: Specification-Driven Code Production
- API contracts, not code, are the interface specification
- Code is generated; humans never read it
- Validation through test suites, not code review

#### Level 4: Autonomous Non-Interactive Factory
**The StrongDM / Shift Work Model** ([[shift-work|Interactive/Non-Interactive Shift]]):

**Interactive Shift** (humans + spec-refinement agents):
- Specification engineering (intent, contracts, constraints)
- Holdout scenario authoring
- Factory configuration
- Human understands the spec deeply

**Non-Interactive Shift** ([[attractor]] orchestration):
- [[strongdm|StrongDM]]'s Attractor runs autonomously
- Implementation, testing, refinement, convergence without human intervention
- Runs for hours/overnight
- [[holdout-scenarios|Holdout scenarios]] validated separately (prevent reward-hacking)
- Humans check satisfaction scores when done

**Key Innovation**: Three separate agent sets prevent gaming:
1. **Spec-refinement agents** (interactive, see specs/scenarios, never see code)
2. **Factory agents** (Attractor, see specs, never see scenarios)
3. **Validation agents** (see scenarios + running artifact, never see code)

**Core Mechanisms**:
- [[nlspec|NLSpec]] — machine-executable specifications
- [[holdout-scenarios]] — validation hidden from implementation agents
- [[attractor]] — DOT-graph phase orchestration
- [[digital-twin-universe]] — deterministic high-volume validation infrastructure
- **Satisfaction metric** (probabilistic, not boolean)

**Tools/Platforms**:
- [[strongdm]] Software Factory (reference implementation)
- Kilroy (Go-based Attractor)
- The open [[attractor]] NLSpec

**Current Industry Distribution**: **Theoretical, with one reference implementation.** StrongDM demonstrated it at a small startup (3-person team, greenfield codebase, no customers yet). **No large enterprise has publicly adopted this pattern.** [[software-factory-practitioners-guide-woolley|Woolley's honest assessment]]: "I have not yet produced usable software with this approach, even of alpha quality."

**Cost Model**: Very high token spend ($1,000/day per human engineer is "aggressive but directionally correct" per StrongDM). Specification engineering bottleneck — humans must write specs with machine-executable rigor. Not suitable for brownfield, complex legacy systems, or organizations without deep domain expertise.

**Problem It Solves**: Eliminates code review bottleneck. Enables truly autonomous software production once specifications are complete. Inverts the cost model — specification engineering is expensive, but implementation becomes cheap and parallelizable.

#### Level 5: Full Autonomous Evolution
**The Geoffrey Huntley Vision** ([[everything-is-a-ralph-loop|Ralph Loop]]):

Extends autonomy beyond code production to specification evolution. Autonomous loops that:
- Monitor production behavior
- Detect failures or gaps
- Amend specifications
- Rebuild and redeploy
- Optimize for business metrics (revenue, user satisfaction)

**Claim**: Level 9 — evolutionary software that self-heals and continuously optimizes.

**Status**: Conceptual; no public production examples. Huntley's own experiments remain internal.

---

## Comparison Across the Five Levels

| Level | Human-in-Loop School (HumanLayer/CRISPY) | Dark Factory School (StrongDM/Ralph) |
|-------|------------------------------------------|--------------------------------------|
| **L1: Autocomplete** | Copilot inline suggestions, human reads/edits | Copilot + code generation, AI can optimize further |
| **L2: Pair Programming** | Real-time Claude Code agentic pair programming; human drives | AI-human pairing, but AI can step to L3 if spec is ready |
| **L3: Code Review** | **Human reviews AI code** (RPI reversal); adversarial AI review assists | **No human code review**; specs and test validation only |
| **L4: Spec-Driven** | CRISPY: humans stay in loop at gates (spec/plan/validation) | **Shift work**: interactive spec → autonomous non-interactive execution |
| **L5: Dark Factory** | **Explicitly rejected** — too risky, unmaintainable | **Target state** — fully autonomous, no human review |

## Key Tensions

### 1. Code Legibility
- **School 1**: Code must be readable by humans. Engineers own the code.
- **School 2**: Code is opaque artifact. Humans own the specification, validation, and observed behavior only.
- **Status**: No consensus. [[code-legibility-debate|School 1 is gaining ground]] — even Dex's RPI reversal shows practitioners learning that code reading matters.

### 2. Specification Rigor
- **School 1**: Specs guide AI but don't fully constrain it. Humans fill gaps during implementation.
- **School 2**: Specs must be machine-executable. Gaps cause factory failure.
- **Status**: School 2's rigor is bottleneck. Woolley: "You cannot take shortcuts on specification precision."

### 3. Human Role
- **School 1**: Human engineers become **10x engineers** (AI-augmented).
- **School 2**: Human engineers become **specification engineers** (new role, different skill set).
- **Status**: Most organizations can't hire for School 2's role. School 1 requires less organizational transformation.

### 4. Ownership and Auditability
- **School 1**: Code is checkpointed, reviewed, human-owned. Clear audit trail.
- **School 2**: Specification is source-of-truth. Code is generated artifact (like compiled binaries). New audit paradigm needed.
- **Status**: Enterprises prefer School 1 model (fits existing governance). School 2 requires new compliance frameworks.

### 5. Error Recovery
- **School 1**: Humans can read and manually fix failing code.
- **School 2**: Humans must fix the specification and re-run the factory.
- **Status**: School 1's recovery path is faster for small issues. School 2's is structural and repeatable.

---

## Current Industry Distribution

### By Level
- **L1 (Autocomplete)**: ~80% of developers (Copilot, GitHub, JetBrains, VS Code)
- **L2 (Pair Programming)**: ~15% (Claude Code, Cursor, Copilot Workspace users)
- **L3 (Code Review)**: ~4% (early CRISPY adopters, some Superpowers users)
- **L4 (Spec-Driven)**: <1% (experimental; HumanLayer, some Anthropic research teams)
- **L5 (Dark Factory)**: 0% (StrongDM only, pre-release; conceptual beyond that)

### By School
- **School 1 (Human-in-Loop)**: ~95% of current L2+ adoption
- **School 2 (Dark Factory)**: <5%, experimental phase, no large-scale deployments

### Trend
- **School 1 gaining momentum**: CRISPY formalization, BMAD codification, Spec Kit adoption, HumanLayer/CodeLayer product maturation
- **School 2 still theoretical**: No large enterprise adoption; Woolley's honesty about difficulties; Shapiro's Level 5 rarely attempted

---

## Unresolved Questions

### For School 1 (Human-in-Loop)
1. **Does 10x actually manifest?** Early claims suggest 2-3x productivity, not 10x. Where's the realistic ceiling?
2. **Scaling human bottleneck**: If human review is mandatory at every gate, does this become a bottleneck at 50-person engineering teams?
3. **When to escalate to L4?** At what scale/complexity should teams move from L2-3 (pair programming + review) to L4 (full spec-driven)?
4. **Code legibility at scale**: Can humans realistically maintain understanding of codebases where AI wrote 80%+ of LOC?

### For School 2 (Dark Factory)
1. **Specification completeness**: How do you know a spec is "complete enough" for autonomous execution? No formal criterion exists.
2. **Production feedback loops**: How do production signals feed back into specification evolution? Unsolved.
3. **Enterprise adoption**: Why hasn't a large enterprise publicly adopted this despite clear benefits? Is the organizational transformation too hard?
4. **Brownfield applicability**: Does dark factory work only on greenfield? How do you apply it to legacy codebases?
5. **Cost realism**: Is $1,000/day token spend a feature or a bug? What's the actual economic case vs. hiring engineers?

### For Both Schools
1. **Role transformation**: Are we ready for the skill shifts this requires? From "code production" to "specification engineering" (School 2) or "AI collaboration" (School 1)?
2. **Legal and compliance**: How do factories fit into SOC 2, HIPAA, SLSA, and other frameworks that assume human review?
3. **Maintenance and evolution**: Which school handles long-term codebase evolution better?
4. **Agent security**: What permissions should autonomous agents have? How do you prevent credential exfiltration or malicious behavior?

---

## Conclusions

1. **The industry is currently in School 1 territory** — human engineers augmented by AI, not replaced. Levels 1-3 are where practice is, Level 4 is experimental.

2. **School 2 (dark factory) remains a theoretical aspiration** — economically attractive (cheap implementation once specs are written) but practically difficult (specification engineering bottleneck, no large-scale adoption, organizational transformation risk).

3. **The divergence is real and widening**: School 1 practitioners (Dex, HumanLayer) are shipping products and building tool ecosystems. School 2 remains mostly published ideas (Shapiro, Woolley, StrongDM's single case study).

4. **Neither school has won**. Most organizations are unlikely to adopt full Level 4-5 workflows in the next 2-3 years. Hybrid approaches (Level 2-3 with pockets of Level 4 spec-driven work) are more probable.

5. **The real frontier is not the factories themselves, but the organizational transformation required**. Skill retraining, role redefinition, career ladders, and cultural shifts matter more than the technical patterns.

---

## Related Concepts and Sources

- [[five-levels-shapiro]] — The five-level taxonomy
- [[dex-rpi-to-crispy]] — School 1's clearest methodology
- [[software-factory-practitioners-guide-woolley]] — School 2's most honest guide
- [[code-legibility-debate]] — The central tension between schools
- [[shift-work]] — School 2's interactive/non-interactive boundary
- [[holdout-scenarios]] — School 2's validation mechanism
- [[nlspec]] — School 2's specification rigor
- [[spec-driven-development]] — The gateway concept for both schools
- [[automation-levels]] — Related framework
