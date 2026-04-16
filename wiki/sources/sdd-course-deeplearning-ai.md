---
title: "Spec-Driven Development with Coding Agents — DeepLearning.AI × JetBrains"
type: source
pillar: spec-driven
created: 2026-04-16
updated: 2026-04-16
sources: [sdd-course-deeplearning-ai]
tags: [spec-driven, deeplearning-ai, jetbrains, paul-everett, constitution, feature-loop, replanning, skills, brownfield, greenfield, course, claude-code, webstorm]
author: Paul Everett (JetBrains)
url: https://learn.deeplearning.ai/courses/spec-driven-development-with-coding-agents
---

# Spec-Driven Development with Coding Agents — DeepLearning.AI × JetBrains

## Metadata

- **Instructor:** Paul Everett (Developer Advocate, JetBrains)
- **Intro by:** Andrew Ng (DeepLearning.AI)
- **Credits:** Konstantin Chaika and Zina Smirnova (JetBrains), Isabel Zaro (DeepLearning.AI)
- **Partnership:** DeepLearning.AI × JetBrains
- **Format:** 13-lesson hands-on video course (DeepLearning.AI "Short Course" format)
- **Course URL:** https://learn.deeplearning.ai/courses/spec-driven-development-with-coding-agents
- **Companion repo:** https://github.com/https-deeplearning-ai/sc-spec-driven-development-files
- **Tooling shown:** WebStorm IDE + Claude Code (explicitly framed as tool-agnostic — VS Code + Codex CLI, Zed + local model, Cursor agent, Gemini CLI all said to work)
- **Raw file:** `raw/sdd-course-deeplearning-ai.md`
- **Pillar:** [[spec-driven-development]]

## Summary

This is the **first wiki source to be a structured, hands-on course** on Spec-Driven Development, rather than a blog post, talk, or academic paper. It matters because (a) it brings Andrew Ng's DeepLearning.AI distribution channel to SDD, (b) it's taught by a JetBrains developer advocate and therefore targets professional IDE users, and (c) it's the first source in the wiki to **prescribe an opinionated, end-to-end SDD workflow** — not a methodology talk (like [[dex-rpi-to-crispy|Dex's CRISPY]]) or a framework (like [[bmad-method|BMAD]] or [[spec-kit|Spec Kit]]), but a working template that a solo developer can copy from `Lesson_04/` and run.

The course codifies a **three-layer SDD workflow**: (1) **Constitution** (mission + tech stack + roadmap as three markdown files committed at project root under `specs/`), (2) a **per-feature loop** run on a dated branch — plan → implement → validate — with three companion files (`plan.md`, `requirements.md`, `validation.md`) in a dated `specs/YYYY-MM-DD-<feature-name>/` directory, and (3) an explicit **replanning phase** between features where the constitution itself is updated, workflow improvements are captured as skills (e.g., a `changelog` skill, a `feature-spec` skill), and product-manager updates (like "40% of users are mobile — add responsive design") get absorbed into specs *before* code.

The course explicitly addresses several topics the rest of the wiki has treated as separate debates: **vibe coding vs. engineering** (Lesson 2 casts SDD as "the professional response to the chaos of unsupervised AI generation" — converging with [[ai-in-sdlc-research]]'s dual-track thesis), **brownfield adoption** (Lesson 11: the agent is instructed to "reverse-engineer the SDD artifacts from the existing code base" — a sharp counter to the common "SDD only works for greenfield" claim), **cognitive debt / AI fatigue** (Lessons 7 and 9: the rationale for reviewing at the spec level, not the CSS-class level), **sub-agents as context firewalls** (Lesson 9: spawning sub-agents for deep review "preserves the main agent's context window, rather than polluting it" — the same framing as [[alexlavaee-rpi-to-qrspi|Lavaee]] and [[skill-issue-harness-engineering|Kyle]]), and **drift between code and specs** (Lesson 7: do refactors through the agent, not the IDE, so all artifacts stay in sync).

Paul Everett's most useful synthesis line is the architect analogy: **"You'll want to avoid telling the builders how to do their jobs and focus on providing the context they don't know."** This is essentially the same idea as Dex's "instruction budget" and Kyle's "it's not a model problem, it's a configuration problem" — but framed for a non-HumanLayer audience. The course is the most **mainstream, stakeholder-friendly articulation of SDD in the wiki so far.**

Because the course ships a **real repo with 10 lesson snapshots**, it also functions as a reproducible artifact. Every `Lesson_NN/` folder is a git-verifiable state of the example project (AgentClinic), so claims made in the course can be checked against the actual files (the `specs/` directory structure, the `skills/feature-spec/SKILL.md` skill definition with its `AskUserQuestion` three-question interview pattern, the example mission and tech-stack docs, and the final roadmap with its ten small phases).

## Key Claims

- **SDD has three benefits worth memorizing.** (1) Control large code changes with small spec changes ("Change SQLite to MongoDB → hundreds of lines rewritten"). (2) Eliminate context decay between sessions — specs persist where context does not. (3) Improve intent fidelity — specs force you to define problem/success-criteria/constraints *before* the agent starts generating. These three framings recur almost verbatim in both Andrew Ng's intro and Lesson 2.

- **The Constitution has three artifacts: `mission.md`, `tech-stack.md`, `roadmap.md`.** Not one file (`agents.md`) — three, because they serve different audiences. Mission = *why* (stakeholder-facing). Tech stack = *how* (engineering team). Roadmap = *what next* (living sequence of phases). The course explicitly contrasts this with the monolithic `agents.md` pattern: "A project Constitution is **agent-agnostic and more structured**." This is the most structured greenfield SDD template documented in the wiki.

- **The feature loop has three artifacts: `plan.md`, `requirements.md`, `validation.md`.** Kept in a **dated** directory: `specs/YYYY-MM-DD-<feature-name>/`. The date prefix is what makes per-feature specs sortable and diff-able over time — a design choice that shows up in the `skills/feature-spec/SKILL.md` instruction.

- **Work each feature on its own branch with fresh agent context.** `/clear` between features is explicit. "Did I clear the agent's context to ensure the specs capture the intent instead of memory snapshots?" This converges with [[bmad-method-docs|BMAD's "fresh chat requirement"]] and Dex's [[instruction-budget]] thesis.

- **Use `AskUserQuestion` with exactly 3 questions in one call: Scope / Decisions / Context.** The `feature-spec` skill in the companion repo pins this down as a concrete interview pattern. Claude Code's `AskUserQuestion` tool is "totally optional, but we just like the way it looks in the interface" — the pattern itself (three structured headers) is the contribution, not the tool.

- **"Don't edit directly — ask the agent to make changes."** Lesson 4's strongest procedural rule: when you notice the mission document is missing a target-audience section, you don't edit the markdown yourself — you continue the conversation with the agent so that related documents (roadmap, tech stack) stay in sync. This is an **anti-drift discipline** that generalizes beyond this course.

- **Replanning is a first-class phase, not a retrospective.** Between features, you update the constitution, absorb product-manager updates (responsive design, testing preferences), possibly re-group roadmap phases, and capture workflow improvements as **skills**. "Make time between features to replan" — positioned as the equivalent of test-after-feature in classical agile.

- **Skills encode repeatable workflows; use the agent to write them.** "Many agents actually have skills that help you write a skill." Two concrete examples ship in the repo: a **changelog skill** (stakeholder-facing) and a **feature-spec skill** (the three-question interview itself, reified). Skills can be global (reusable across projects) or local — "you'll gain better understanding as you use it." This parallels [[superpowers|Jesse Vincent's skills framework]] and its mandatory-invocation pattern, but targets a less opinionated audience.

- **Sub-agents for deep review preserve the main context.** Lesson 9: "tell the agent to spawn several sub-agents to do a deep review of the entire project with this feature change. This deep review gives the agent more space to think about the changes. And using sub-agents **preserves the main agent's context window, rather than polluting it.**" This matches the [[alexlavaee-rpi-to-qrspi|context-firewall framing]] word-for-word, and is the first time the wiki has documented this pattern appearing in **mainstream course material**.

- **MVP as an "extreme test" of the constitution.** Lesson 10 reframes the rush-to-demo impulse: don't implement the remaining roadmap in one shot as a shortcut — do it only if you **trust your constitution and specs**. "If we now get something different from what we wanted, it means we need to very responsibly carry out another replanning phase." The MVP is a **spec-quality test**, not a feature-count test.

- **Brownfield works by reverse-engineering the constitution from existing code.** Lesson 11's key move: "the agent will discover and in a sense reverse-engineer the SDD artifacts from the existing code base." Inputs are README.md, TODO.md, issue trackers, spreadsheets, Word documents — whatever exists. This is the most **accessible** brownfield SDD framing in the wiki so far (compare to [[codespeak|CodeSpeak's]] brownfield OSS conversions, which are more automated but less documented as a workflow).

- **Cognitive debt is managed by size discipline, not tooling.** "Because agents are so fast at writing code, software developers have lately been talking about cognitive debt — the mental load of tracking what your code is doing and how it has evolved." The answer is not a better tool — it's **smaller task groups**, reviewing at the spec level, and clean breaks between features.

- **Drift between artifacts is the main enemy.** Several specific rules target this: don't refactor in the IDE (ask the agent so related specs and READMEs stay in sync); when reviewing, if the mistake flowed from a mistake in the plan, fix the plan; "we want the specs to capture decisions, not just the code." The premise: **the spec, the code, and the changelog must agree.**

## Connections

- **[[spec-driven-development]]** — This source is the most **prescriptive greenfield template** in the wiki. Its three-file constitution (mission/tech-stack/roadmap) and three-file feature spec (plan/requirements/validation) should be added to the concept's "Tools and Frameworks" section as an archetype, not a tool. It also gives the concept its first named **dual-track stance** in course format: vibe coding is acknowledged as legitimate for buttons; SDD is reserved for systems.

- **[[bmad-method]] / [[bmad-method-docs]]** — BMAD's **fresh chat requirement** and **project-context.md** shared-context file have direct analogues here: the per-feature `/clear` discipline and the tech-stack.md artifact. The course differs in that it has **no named agent personas** (Mary, Winston, etc.) — instead, all interaction is with one agent (Claude Code) playing every role, controlled by the human's steering. This is the **single-agent counterpart** to BMAD's multi-persona structure.

- **[[spec-kit]]** — The course's `specify → plan → tasks → implement` pipeline is a near-direct mirror of Spec Kit's workflow, but run **entirely in plain markdown files + git** rather than through a CLI. It's the "spec-kit without the kit" expression — which matters because it shows the workflow is the irreducible part; the tooling is optional.

- **[[kiro]] / [[codespeak]]** — Compared to Kiro (AWS-hosted IDE) and CodeSpeak (a platform that generates apps from `.cs.md` files), this course **refuses to tie the workflow to tooling**. "The specs travel with you when you switch tools" — this is the same portability claim that [[alexlavaee-rpi-to-qrspi|Lavaee's]] QRSPI makes, but here it's framed as an onboarding benefit rather than an architectural one.

- **[[dex-rpi-to-crispy]]** — Every major CRISPY concept appears here under a different name: Dex's "Mental Alignment via artifacts" = Everett's "constitution + feature spec as shared context"; Dex's "Smart Zone / Dumb Zone" 40% threshold = Everett's "clear the context between features"; Dex's "instruction budget" = Everett's "stick to higher-level requirements, avoid nitpicking variable names." **The two sources converge on the same practices without cross-referencing each other.** Cross-practitioner validation.

- **[[alexlavaee-rpi-to-qrspi]] / [[skill-issue-harness-engineering]]** — The Lesson 9 phrasing on sub-agents as context preservers is almost identical to Lavaee's **"sub-agents as context firewalls"** framing and to Kyle's configuration-layer writeup. First appearance of this concept in **non-HumanLayer course content**.

- **[[superpowers]] / [[superpowers-intro]] / [[superpowers-5]]** — Two points of convergence. (1) **Skills as the unit of agent capability**: the course's changelog skill and feature-spec skill are *exactly* the kind of "SKILL.md under ~/.claude/skills/" artifact Jesse Vincent prescribes. (2) **Workflow-over-prompts**: Vincent's "brainstorm → plan → implement" cascade and Everett's "plan → implement → validate" feature loop are the same shape. The main difference: Superpowers enforces RED-GREEN-REFACTOR TDD as mandatory; this course is softer on test-writing discipline (tests are a Lesson 8 add-on).

- **[[12-factor-agents]]** — Lesson 2's line that "your main task as the human now shifts: learn how to convert your intentions into clear specifications" aligns with Factor #2 ("own your prompts"). The whole constitution artifact is a form of owned context — Factor #3.

- **[[anatomy-agent-harness]] / [[agent-harness]]** — Claude Code + WebStorm is used as a concrete harness, and the course treats the harness as **swappable** ("VS Code with the Codex CLI, Zed editor with a local model, all great for spec-driven development"). This is consistent with Pachaar's observation that "the harness is the product, not the model" — the course inverts it slightly: **the specs are the product; the harness is swappable.**

- **[[context-engineering]]** — The constitution + per-feature spec structure is a concrete implementation of context engineering: static artifacts (mission, tech stack, roadmap, plan, requirements, validation) are shared ground between human and agent. The `/clear` between features is context-window hygiene. Sub-agents as context firewalls is context isolation.

- **[[everything-is-a-ralph-loop]]** — Implicit counter-position. Everett's "the agent is the muscle, but the SPEC is the brain" and "shoot for 2-3×, not 10×" (via architect analogy) contradict Huntley's "software development is dead" maximalism. The course does not invoke Ralph Loop once; the entire pedagogy assumes human-in-the-loop validation is non-negotiable.

- **[[ai-in-sdlc-research]]** — The Lesson 2 vibe-coding-vs-engineering framing is essentially the paper's dual-track thesis restated for practitioners.

- **[[automation-levels]] / [[five-levels-shapiro]]** — The course is a **Level 3–4 template**. It does not entertain Level 5 / Dark Factory framings. Useful datapoint for where mainstream educational content currently lives on Shapiro's ladder.

## Questions Raised

1. **How does the course handle the Dex-style "instruction budget overflow"** at Lesson 10's MVP step? Implementing the remaining roadmap in one shot risks blowing past the ~150-200 instruction effective range. Is the constitution-as-shared-context supposed to compensate? If yes, is there empirical evidence it does?

2. **Is the three-file constitution (mission/tech-stack/roadmap) load-bearing**, or can it be reduced? BMAD uses a single `project-context.md`. Spec Kit uses a different breakdown. What are the tradeoffs?

3. **The course prescribes `specs/YYYY-MM-DD-<feature-name>/` as the per-feature directory name.** How does this scale when two features ship on the same day? What's the convention for features that span multiple days?

4. **Skills are created via the agent and can be global or local.** The course explicitly flags this as a style choice. Is there emerging community guidance on which skills belong global vs. local? (cf. [[superpowers]] ships skills as a distributable unit across IDEs.)

5. **Lessons 12 and 13** (not in the transcript the user provided, but present in the companion repo) are titled "Build Your Own Workflow" and "Agent Replaceability." The latter is particularly interesting — what does the course say about swapping agents (Claude Code → Codex → Gemini) mid-project while preserving specs? Transcripts for those lessons should be ingested next.

6. **Where does the course land on "should you read the code?"** Lesson 7's "focus your review on high-level concerns… rather than details like which CSS classes were implemented" leans toward School 1 (don't read the code line-by-line). But Lesson 9's "make sure it creates code that you can commit under your name" leans toward School 2 (you're responsible for what you merge). This is potentially the **mainstream middle-ground articulation** the [[code-legibility-debate]] concept has been missing.

7. **JetBrains partnership signal.** JetBrains is producing this course rather than Cursor, GitHub, or Anthropic. What does this say about IDE vendors' positioning on SDD? Is JetBrains betting on SDD as the reason developers stay in professional IDEs (vs. moving to chat-first AI UIs)?

8. **The `feature-spec` skill's three-question interview pattern** (Scope / Decisions / Context) is surprisingly specific. Is it empirically derived (from the creators' agent sessions) or theoretically motivated? Would four questions be worse? Two?
