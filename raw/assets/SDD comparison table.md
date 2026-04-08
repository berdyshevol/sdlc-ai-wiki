SDD comparison table

|  | BMAD | GitHub Spec-Kit | Kiro (AWS) | OpenSpec | Claude Code \+ Skills/Workflows |
| ----- | ----- | ----- | ----- | ----- | ----- |
| **Philosophy** | Full AI agile team simulation | Spec → Plan → Tasks → Code | IDE with built-in SDD | Lightweight, for existing code | Project-aware AI agent with custom skills |
| **Agents** | 12+ specialized roles | None (single assistant) | Built into IDE | None | Sub-agents (Plan/Explore/Task) \+ custom |
| **Structure** | PRD \+ Architecture \+ Stories | Spec → Plan → Tasks | Requirements → Design → Tasks | Spec \+ Delta updates | CLAUDE.md \+ SKILL.md \+ commands \+ hooks |
| **Scale** | Enterprise, complex systems | Mid-size projects | Feature-level | Brownfield, small changes | From bug fixes to full-stack systems |
| **Setup time** | Hours/days (Node.js v20+, npx) | Minutes | Install IDE | 5 minutes | Minutes (CLAUDE.md \+ a few skills) |
| **Output volume** | PRD \+ Arch \+ Stories (thousands of lines) | \~800 lines of specs | Requirements \+ Design \+ Tasks | \~250 lines | You control — as much or little as needed |
| **Greenfield** | ✅ Excellent | ✅ Excellent | ✅ Good | ⚠️ Not ideal | ✅ Good |
| **Brownfield** | ⚠️ Possible but heavy | ⚠️ Not optimized | ⚠️ Average | ✅ Purpose-built | ✅ Excellent (reads existing codebase) |
| **Small fixes** | 🔨 Overkill | 🔨 Overkill | 🔨 Overkill | ✅ Fine | ✅ Ideal |
| **Vendor lock-in** | None (any AI IDE) | GitHub ecosystem | AWS (Code OSS) | None | Anthropic (Claude) |
| **Customization** | Expansion Packs, custom agents | Templates | Hooks (auto-triggers) | Minimal | Skills, commands, hooks, rules — fully custom |
| **Context management** | File-based (story.md, dev.md) | Version-controlled specs | IDE-native context | Lightweight specs | CLAUDE.md \+ MEMORY.md \+ session logs |
| **Learning curve** | High | Medium | Low (IDE) | Low | Low → Medium (grows with you) |
| **Team vs Solo** | Built for teams (virtual) | Solo / small team | Solo developer | Solo | Both — from solo to shared CLAUDE.md |
| **Workflow rigidity** | Rigid: Analyst→PM→Arch→SM→Dev→QA | Rigid: specify→plan→tasks→implement | Rigid: spec mode phases | Flexible | **Fully flexible** — you build your own workflow |
| **GitHub ⭐** | 19.1k | New, growing | Closed preview | Small | N/A (Anthropic product) |

---

**Key takeaway:** BMAD, Spec-Kit, and Kiro are **opinionated frameworks** — they prescribe *how* you should work. Claude Code \+ Skills is an **unopinionated platform** — you assemble your own workflow from building blocks. Notably, BMAD itself runs *on top of* Claude Code (and Cursor, Windsurf) as its runtime, which makes them complementary rather than competing tools.

[https://dzone.com/articles/beyond-vibe-ai-coding-frameworks](https://dzone.com/articles/beyond-vibe-ai-coding-frameworks)

# **Beyond the Vibe: Why AI Coding Workflows Need a Framework**

We are seeing this trend emerge in various forms:

* Spec-Driven Workflows like GitHub’s [Spec-kit](https://github.com/github/spec-kit).  
* Agile-Inspired Methodologies like the [BMad Method](https://www.google.com/search?q=https%3A%2F%2Fgithub.com%2Fbmad-code-org%2FBMAD-METHOD%2Fblob%2Fmain%2Fdocs%2Fuser-guide.md).  
* Test-Driven Development (TDD) Partners like [Aider](https://github.com/paul-gauthier/aider).  
* Autonomous Agentic Systems like [MetaGPT](https://github.com/geekan/MetaGPT) and [SWE-agent](https://swe-agent.com/).

**A Tale of Two Philosophies**

* Spec-kit focuses on feature-level “spec-to-code” generation, whereas the BMad Method focuses on Full project lifecycle management from idea to QA.  
* Spec-kit is primarily for individual developers, whereas the BMad Method is preferable for the entire agile team (PMs, architects, Devs).  
* Spec-kit is capable of rapidly and reliably scaffolding code from a clear, version-controlled specification, whereas the BMad Method is great in integrating AI agents into existing Agile/Scrum processes at a strategic, cross-functional level.

This comparison shows there isn’t a single “best” framework, only the one that best fits the task at hand. You wouldn’t use a full project plan to fix a typo, nor would you build a new microservice based on a one-line prompt.

## **Best-of-Both-Worlds Solution**

The choice isn’t always ‘either/or.’ The real power of these structured approaches lies in their modularity, allowing teams to combine them to create a workflow that fits their unique needs. A hybrid approach can leverage BMad’s strategic planning with Spec-kit’s tactical execution prowess.

Here’s how it could work:

Phase 1: Strategic and sprint planning (BMad)

* Use the BMad Business Analyst and Architect agents to define the project’s vision, create a detailed PRD, and establish the high-level system design.  
* The BMad Scrum Master then breaks down the PRD into user stories for the upcoming sprint.

Phase 2: Feature implementation (Spec-kit)

* A developer picks up a user story from the sprint backlog.  
* They use this user story as the initial prompt for Spec-kit’s /specify command to create a detailed, executable specification.  
* They then run through the /plan, /tasks, and /implement phases to generate high-quality, compliant code that perfectly matches the spec.

Phase 3: Quality assurance and integration (BMad)

* The code generated by Spec-kit is submitted for review.  
* The BMad QA Agent is then invoked to perform an initial review, checking the implementation against the original user story and acceptance criteria, completing the loop.

This hybrid model creates a seamless workflow where high-level project management flows directly into low-level, spec-driven code generation, giving you end-to-end control, consistency, and quality.

