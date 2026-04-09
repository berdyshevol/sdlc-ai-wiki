# BMAD Method — Official Documentation

**Source:** https://docs.bmad-method.org/llms-full.txt
**Fetched:** 2026-04-09

## What Is BMAD

The BMad Method is an AI-driven development framework designed to guide teams through complete software projects. It describes itself as helping developers "build software through the whole process from ideation and planning all the way through agentic implementation." Rather than a tool, it's a structured methodology integrating specialized AI agents, guided workflows, and intelligent planning that adapts to project complexity.

## Core Concepts

### Four-Phase Development Cycle

BMAD structures work into sequential phases:

1. **Analysis** (Phase 1) - Optional brainstorming, market/domain/technical research, product brief creation
2. **Planning** (Phase 2) - Requirements documentation via PRD or specification
3. **Solutioning** (Phase 3) - Architecture design and work breakdown into epics/stories
4. **Implementation** (Phase 4) - Story-by-story development with code review and retrospectives

### Three Planning Tracks

Projects select complexity-appropriate paths:
- **Quick Flow** - Bug fixes and small features; tech-spec only
- **BMad Method** - Standard products and platforms; PRD plus architecture
- **Enterprise** - Compliance and multi-tenant systems; comprehensive documentation

### Agent-Driven Workflows

Specialized AI personas handle different roles, creating shared context across implementation phases and reducing agent conflicts through explicit architectural decisions.

## Architecture and Structure

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

### Dual Discovery System

Workflows can find documents as monolithic files or as sharded (split) directories with index files. Whole documents take precedence if both exist.

## Key Components and Tools

### BMad-Help

Described as "the fastest way to get started," this intelligent guide inspects projects, detects completed work, and recommends next steps through natural language interaction.

### Project Context File

The `project-context.md` document captures technology stack versions and implementation rules. It ensures consistency across agents implementing different epics by documenting conventions agents might otherwise miss.

### Advanced Elicitation

After workflows generate content, structured second-pass analysis methods (pre-mortem analysis, inversion, first principles thinking) can reconsider output through specific reasoning lenses.

### Adversarial Review

Code review that mandates finding problems—"no 'looks good' allowed." The reviewer assumes issues exist and must surface specific findings, preventing confirmation bias in approval workflows.

### Party Mode

Orchestrates multiple agents in single conversation, enabling brainstorming sessions and complex decisions requiring diverse perspectives.

### Quick Dev Workflow

Autonomously handles intent clarification, specification, implementation, review, and presentation for small fixes and features—minimizing human checkpoints between initial approval and final review.

### Checkpoint Preview

Interactive code review guide presenting changes by concern rather than file order, building reviewer comprehension progressively from design intent through implementation details.

## Agents and Personas

| Agent Name | Skill ID | Specialization | Key Workflows |
|---|---|---|---|
| Analyst (Mary) | `bmad-analyst` | Research, brainstorming, discovery | Brainstorm, research, product brief, PRFAQ |
| PM (John) | `bmad-pm` | Requirements and scope | Create/validate PRD, epics/stories |
| Architect (Winston) | `bmad-architect` | Technical design decisions | Create architecture, implementation readiness |
| Developer (Amelia) | `bmad-agent-dev` | Implementation and testing | Dev story, quick dev, code review, sprint planning |
| UX Designer (Sally) | `bmad-ux-designer` | User experience design | UX design workflows |
| Technical Writer (Paige) | `bmad-tech-writer` | Documentation | Project documentation, standards, diagrams |

Agents are customizable via `.customize.yaml` files that preserve changes across updates.

## Development Flow

### Planning Phase (Typical BMad Method Track)

1. Developer invokes PM agent and runs `bmad-create-prd` workflow
2. PRD document captures functional and non-functional requirements
3. Optional: UX Designer creates `bmad-create-ux-design`
4. Architect agent creates architecture document via `bmad-create-architecture`
5. PM agent creates epics/stories using both PRD and architecture as input
6. Architect validates implementation readiness

### Implementation Phase

1. Developer runs `bmad-sprint-planning` to initialize tracking
2. For each story, repeat:
   - Create story file via `bmad-create-story`
   - Implement via `bmad-dev-story`
   - Review via `bmad-code-review` (optional but recommended)
3. After epic completion, run `bmad-retrospective`

### Fresh Chat Requirement

Each workflow must run in a new chat session to prevent context limitations and ensure clean agent state.

## Conflict Prevention Mechanisms

### Architecture as Shared Context

When multiple agents implement different epics, documented architecture decisions prevent conflicts by establishing unified standards for API patterns, database design, state management, and naming conventions before implementation begins.

### Preventing Common Conflicts

Architecture decisions document choices like API style (GraphQL vs REST), database technology, authentication approach, state management library, and code organization patterns—allowing all agents to reference the same technical constraints.

## Quick Flow Alternative

For small changes and bug fixes, `bmad-quick-dev` combines planning and implementation in one workflow, skipping full PRD and architecture processes for projects where they're unnecessary overhead.

## Key Principles

- **Start with BMad-Help** for guidance rather than memorizing workflows
- **Fresh chats for each workflow** to maintain context boundaries
- **Architecture before implementation** on complex projects to ensure agent alignment
- **Project context guides agents** toward consistent technical decisions
- **Human judgment remains essential** for intent clarification, spec approval, and final review

BMAD emphasizes reducing human bottlenecks by allowing longer autonomous agent execution between intentional human checkpoints, rather than constant supervision.
