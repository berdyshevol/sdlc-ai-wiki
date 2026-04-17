---
title: "The Agentic Coding Stack: 7 Tools, 5 Layers, and the Missing Link Nobody Has Built Yet"
type: source
pillar: [coding-agents, spec-driven, software-factories, code-legibility, industry]
created: 2026-04-16
updated: 2026-04-16
sources: [agentic-coding-stack-aslan]
tags: [stack, layers, traceability, methodology, discipline, semantic-context, token-optimization, product-surface, bmad, spec-kit, superpowers, ctxo, rtk, context-mode, gsd-2]
---

# The Agentic Coding Stack: 7 Tools, 5 Layers, and the Missing Link Nobody Has Built Yet

## Metadata

- **Author:** Murat Aslan
- **Publication:** Dev Genius (Medium publication)
- **Date:** April 2026 (~2026-04-11; "5 days ago" as of fetch on 2026-04-16)
- **URL:** https://blog.devgenius.io/the-agentic-coding-stack-7-tools-5-layers-and-the-missing-link-nobody-has-built-yet-de264b260db3
- **Read time:** ~13 min
- **Series:** Series 1 of "Agentic Coding Systems"
- **Author repo:** https://github.com/murataslan1
- **Disclosure:** Author states *"I am a contributor to some repos."* No specific list given.
- **Raw file:** `raw/agentic-coding-stack-aslan-2026.md` (full article body, fetched via Playwright after Cloudflare blocked direct curl/WebFetch access; verbatim DOM `innerText` extraction, 20,617 chars)

## Summary

A practitioner's stack-map of seven AI-coding tools across five orthogonal layers. The author's central move is to reject the "which tool wins?" framing — most of these tools are not direct competitors and live at different layers of an agentic-coding workflow. The argument: *"serious agentic coding needs a stack, not a favorite tool."*

Each tool is evaluated against four questions: **what problem does it solve, which layer does it belong to, when should you use it, what cost does it introduce?** The framing-of-a-stack as five layers is the post's main contribution to the discourse — it gives the wiki's existing tools (BMAD, spec-kit, superpowers) a clean architectural slot and introduces four tools previously absent from the wiki (Ctxo, RTK, context-mode, gsd-2).

The post's analytical move is to first enumerate **five failure modes** in agentic coding (consistency, context loss, specification gaps, review bottlenecks, multi-session conflicts) and then show that each layer reduces a subset of those failures. *"Every tool in this post reduces one or more of these failures. None eliminates all five."*

The recommended-combinations section (solo / team / spec-first / token-constrained) treats the layer model as a deployment guide, not a taxonomy: start from the failure mode that hurts most, pick the lightest tool that fills the missing layer, only add the next layer when the previous becomes a bottleneck.

The post closes with the **"missing link" thesis**: the unclaimed layer is **spec-to-code traceability** — tracking which code symbols implement which requirements, which tests cover which spec items, and how requirement changes propagate into code. None of the seven tools provides this; the author claims whoever builds it well will *"own the most strategic connective tissue in the agentic coding stack."*

## The 5-Layer Map

| Layer | Question | Tools | Failure modes reduced |
|-------|----------|-------|----------------------|
| **1. Delivery Methodology** | When should the AI analyze, plan, implement? | [[bmad-method\|BMAD-METHOD]], [[spec-kit]] | Consistency, specification gaps |
| **2. Agent Discipline** | How should the AI behave while building? | [[superpowers]] | Review bottlenecks, consistency |
| **3. Technical Context** | What does the code actually mean? | [[ctxo|Ctxo]] | Review bottlenecks, multi-session conflicts |
| **4. Token Optimization** | How much tool output should enter context? | [[rtk|RTK]], [[context-mode]] | Context loss |
| **5. Product Surface** | Where does the developer operate the whole system? | [[gsd-2]] | Multi-session conflicts, review bottlenecks |

Decision rule: *first ask which layer is missing in your workflow, then choose the lightest tool that solves that missing layer, only add the next layer when the previous one becomes a bottleneck.*

## The 7 Tools (one-line summary)

| Tool | Layer | What it is | Author's "my take" |
|------|-------|------------|--------------------|
| [[bmad-method\|BMAD-METHOD]] | L1 | 34+ workflows, 12+ expert personas, four-phase structure | "Strongest when your real enemy is premature implementation" |
| [[spec-kit]] | L1 | GitHub's spec-first artifact chain `constitution → specify → plan → tasks → implement` | "BMAD is the heavier operating model; spec-kit is the cleaner starting point" |
| [[superpowers]] | L2 | Skill/workflow library injecting TDD, debugging, verification, scoped delegation | "If BMAD/spec-kit answers 'what order should work happen in?', superpowers answers 'how do we stop the agent from being sloppy once work begins?'" |
| [[ctxo\|Ctxo]] | L3 | MCP server for semantic codebase analysis (blast radius, logic slices, why-context, dead code, PR impact) | "The scarcest capability in the current ecosystem" |
| [[rtk\|RTK]] | L4 | Rust CLI proxy that intercepts shell output and applies command-specific filters | "The fastest way to improve a noisy shell-based workflow without redesigning how the agent works" |
| [[context-mode]] | L4 | MCP sandbox; agent writes code to compute the answer, only `console.log()` reaches context | "RTK optimizes noisy commands. context-mode optimizes the workflow itself" |
| [[gsd-2]] | L5 | Full autonomous coding platform: `gsd auto → plan → execute → verify → commit → repeat` | "The closest thing in this set to a full product shell for the stack" |

## Key Claims

1. **"Serious agentic coding needs a stack, not a favorite tool."** The post's thesis. Reframes the AI-devtool debate from product comparison to architectural-layer composition. *"Most conversations about AI devtools still collapse into the wrong debate: 'Which tool wins?' That framing misses the point. The best tools are often not direct competitors. They live at different layers of the workflow."*

2. **Five failure modes of agentic coding.** Consistency failures, context loss, specification gaps, review bottlenecks, multi-session conflicts. *"Every tool in this post reduces one or more of these failures. None eliminates all five. That is the core thesis for this series: agentic coding is a systems problem."* This is the wiki's first explicit failure-mode taxonomy for agentic coding.

3. **Five layers are orthogonal, not hierarchical.** Methodology decides sequence; discipline decides behavior inside that sequence; semantic context decides what the agent understands; token optimization protects the context window; product surface coordinates the whole system. Mixing layers in tool comparisons is the source of confusion. *"Bad tool decisions usually come from mixing up layers. Teams compare a methodology tool with a token tool, or a semantic analysis tool with a product shell, and then wonder why the conclusion feels fuzzy."*

4. **Lightest-stack-first deployment rule.** *"The fastest way to misuse this ecosystem is to install everything at once. Instead, start from the failure mode that hurts you most."* Four recommended combinations are given as starting points (Solo / Team / Spec-First / Token-Constrained), each layered against the failure mode that hurts most.

5. **RTK and context-mode are not substitutes — they attack token waste at different points in the pipeline.** RTK filters command output *after* execution at the OS/shell hook layer. context-mode prevents raw output from entering context by sandboxing tool execution. *"Used together, they form a clean sequence: RTK reduces noisy shell output, then context-mode keeps the remainder from flooding the conversation."* This is the wiki's first articulation of multi-layer token-optimization composition.

6. **Ctxo's six semantic-analysis primitives.** `get_blast_radius`, `get_logic_slice`, `get_why_context` (uses git history), `get_symbol_importance`, `find_dead_code`, `get_pr_impact`. *"Plenty of tools tell agents how to behave. Far fewer help them understand the code they are about to change."* Strongest TS/JS support today; indexing required.

7. **superpowers reframed as L2 "Agent Discipline" — not a methodology and not a harness.** The post draws a clean distinction: methodology (L1) sequences work; discipline (L2) governs in-flight behavior. This sharpens the [[superpowers]] entity-page positioning, which previously shared real-estate with BMAD and spec-kit as a "methodology-adjacent" tool.

8. **The missing link: spec-to-code traceability.** The post's headline insight. Four unanswered questions: (a) which code symbols implement requirement RQ-12; (b) which tests cover this spec item; (c) if this requirement changes, what breaks; (d) which open PRs/agents are touching the same requirement. *"If someone builds that bridge well, they will not just have a useful feature. They will own the most strategic connective tissue in the agentic coding stack."* Today's ecosystem is good at the edges (intent generation, execution discipline, code semantics, token protection) but the **bridge between specification and implementation is still weak**.

9. **Five lessons.** (1) Worst tool debates are layer-confusion debates. (2) Good planning does not compensate for poor code understanding. (3) Token optimization is reliability infrastructure, not a nice-to-have. (4) The lightest useful stack usually wins first. (5) Spec-to-code traceability is the next serious frontier.

## Connections

### Direct slot-fill for existing wiki entities

- **[[bmad-method]]** — placed at L1 alongside spec-kit. The post's framing of BMAD as *"strongest when your real enemy is premature implementation"* converges with [[bmad-method-docs|the BMAD docs ingest]]'s emphasis on the four-phase cycle and adversarial review. Aslan's tradeoff note (*"ceremony"*; *"each stage loads its own planning context"* costs tokens) is consistent with the wiki's existing "high setup time" limitation entry on the [[bmad-method]] page.

- **[[spec-kit]]** — placed at L1 as the lighter alternative to BMAD. Aslan's framing (*"the cleaner starting point for teams that want structure without a full methodology culture shift"*) sharpens the wiki's existing comparison and gives a cleaner heuristic than the prior comparison table: *"if you choose BMAD, choose it because you want process depth. If you choose spec-kit, choose it because you want lighter structure."*

- **[[superpowers]]** — placed at L2 with the cleanest single-sentence positioning the wiki has yet recorded for it: *"If BMAD/spec-kit answers 'what order should work happen in?', superpowers answers 'how do we stop the agent from being sloppy once work begins?'"* Aslan independently corroborates the wiki's existing characterization (TDD-first, scoped delegation, verification gates) as engineering discipline, not methodology.

### Slot-fills for new entities (created from this source)

- **[[ctxo|Ctxo]]** — first appearance in the wiki. New L3 entity. Closes the "Technical Context" gap in the [[agent-harness]] / [[context-engineering]] vocabulary: most existing harness tools optimize *how* the agent operates, not *what* the agent understands about the code. Closest existing parallel: [[claude-agent-sdk]]'s grep/glob/head/tail JIT retrieval pattern documented in [[anatomy-agent-harness]] — but text search vs. semantic graph is the same gap Aslan names.

- **[[rtk|RTK]]** — first appearance. New L4 entity. Mechanism: shell-output proxy with command-specific filters. Closest existing parallel: the **observation masking** strategy from [[anatomy-agent-harness]] (JetBrains Junie hides old tool outputs while keeping tool calls visible).

- **[[context-mode]]** — first appearance. New L4 entity. Mechanism: MCP sandbox where the agent's code computes the answer and only `console.log()` enters context. Closest existing parallels: (a) the **sub-agent delegation** strategy from [[anatomy-agent-harness]] where subagents return 1-2k token summaries; (b) [[bmad-method]]'s `project-context.md` and [[dex-rpi-to-crispy|CRISPY]]'s static artifacts as Mental Alignment infrastructure. The shared insight: keep the verbose work outside the conversation.

- **[[gsd-2]]** — first appearance. New L5 entity. *"Where the other tools act like stack components, gsd-2 looks like an integrated product surface around long-running agentic work."* Closest existing parallel: [[humanlayer-codelayer|HumanLayer's CodeLayer]] (also positioned as an integrated operating environment for autonomous AI work, per [[humans-in-the-loop-dex-interview]]'s "Google Docs/Notion/Figma-like SDLC" framing). Also resonates with [[everything-is-a-ralph-loop|Huntley's Weaving Loom]] as factory infrastructure.

### Concept connections

- **[[agent-harness]]** — Aslan's 5-layer model is a *product-engineering* slicing of the same territory the [[agent-harness]] concept describes as 12 components / 7 architectural decisions. Useful contrast: the harness model is component-oriented (looking inside a single agent), the stack model is workflow-oriented (looking at the developer's whole assembly). Both should coexist on the wiki.

- **[[context-engineering]]** — L4 (Token Optimization) is a packaging of context-engineering principles into installable tools. RTK = **observation masking** as a tool. context-mode = **sandboxed analysis** + **structured note-taking** as a tool. Aslan provides the wiki's first pairing of these two strategies as composable pipeline stages.

- **[[spec-driven-development]]** — Aslan's "spec-to-code traceability" is the unsolved-problem half of spec-driven development. The existing concept page documents *creating* specs and *generating* code from them; Aslan's missing-link section documents the *traceability* problem that emerges once both exist. Open question added to the SDD concept page accordingly.

- **[[code-legibility-debate]]** — spec-to-code traceability is a third position in the legibility debate. School 1 says *"read the spec, not the code."* School 2 says *"read the code."* Aslan's framing implies a third stance: *"build the bridge so you can navigate from spec to code on demand, then choose what to read based on the question."* This is closer to the [[sdd-course-deeplearning-ai|DeepLearning.AI course]]'s middle-ground synthesis (review at spec/behavior level for most changes; reserve line-level reading for security/database/compounding areas) but adds the **navigability** primitive that the course doesn't articulate.

- **[[software-factory]]** — gsd-2 is the most "factory-shaped" tool in this post's set. Aslan's L5 framing (*"an operating system for AI work"*) parallels [[everything-is-a-ralph-loop|Huntley's]] Weaving Loom but at smaller scale and shorter horizons.

### Cross-reference to other sources

- **[[anatomy-agent-harness]]** (Akshay Pachaar) — Sister piece. Pachaar slices the territory by component (12 components, 7 architectural decisions, 5 frameworks). Aslan slices the same territory by workflow layer (5 layers, 7 tools). Both 2026 syntheses; neither cites the other; the convergence on a layered/component view of agentic coding is itself a wiki-worthy data point. Pachaar's *"if you're not the model, you're the harness"* (Vivek Trivedy) and Aslan's *"agentic coding is a systems problem"* are close cousins.

- **[[skill-issue-harness-engineering]]** (Kyle, HumanLayer) — Same observation in different vocabulary. Kyle: *"it's not a model problem. It's a configuration problem."* Aslan: *"it is stack design."* Both diagnose the "AI worked great for the first hour and then everything got weird" pain as something other than model quality.

- **[[bmad-method-docs]]** — corroborates Aslan's L1 placement. BMAD's four-phase cycle (Analysis → Planning → Solutioning → Implementation) is exactly the *"sequencing"* Aslan calls out as BMAD's core value-add.

- **[[sdd-course-deeplearning-ai]]** — Aslan's L2 (superpowers as discipline) parallels the course's framing of skills as workflow-automation primitives. Both treat reusable engineering discipline as a first-class artifact, not just a prompt.

- **[[matt-pocock-dex-horthy-chat]]** and **[[dex-rpi-to-crispy]]** — Aslan's L4 framing of context as a *systems constraint* echoes Dex's Smart Zone / Dumb Zone and quadratic-attention argument. The five failure modes Aslan enumerates are directly responsive to Dex's "the agent gets dumber as context fills up."

- **[[everything-is-a-ralph-loop]]** — gsd-2 (L5) sits structurally where Huntley's Loom sits, but Aslan stays away from the *"software development is dead"* maximalism. His tone is engineering-pragmatic, not manifesto.

- **[[codespeak]]** — Conspicuous absence. CodeSpeak is the wiki's most aggressive spec-driven platform but doesn't appear in Aslan's seven. Possible reasons: (a) CodeSpeak occupies a different category — it generates code from specs end-to-end rather than augmenting an agentic-coding workflow; (b) the post focuses on **agentic** coding (interactive AI agents), and CodeSpeak's `codespeak build` is more pipeline than agent. Worth flagging as an analysis question.

## Questions Raised

1. **Is the 5-layer model load-bearing or descriptive?** Aslan presents it as both diagnostic (use it to identify which layer is missing) and prescriptive (combinations should respect layer boundaries). But the four "Recommended Combinations" mostly span 3-4 layers, not all 5. Is L5 (gsd-2) genuinely separable from the lower layers, or is it a packaging concern?

2. **Where do the wiki's existing entities fit in the 5-layer map?** Quick triage:
   - L1 (Methodology): BMAD, spec-kit, ✶ also [[codespeak]] (spec-driven), ✶ [[kiro]]
   - L2 (Discipline): superpowers, ✶ also [[bmad-method|BMAD's Quick Dev workflow]] (overlap)
   - L3 (Technical Context): Ctxo only — confirms Aslan's "scarcest capability" claim
   - L4 (Token Optimization): RTK, context-mode, ✶ also [[claude-agent-sdk|Claude Code's]] grep/glob/head/tail JIT pattern (built-in, not a tool)
   - L5 (Product Surface): gsd-2, ✶ also [[humanlayer-codelayer|CodeLayer]], [[agent-control-plane]], ✶ partially [[everything-is-a-ralph-loop|the Weaving Loom]]
   
   The existing wiki has good L1, L2, L4, L5 coverage. **L3 (semantic codebase analysis as a tool category) is genuinely a wiki gap that this source closes.**

3. **Is spec-to-code traceability really unclaimed?** The wiki has at least three sources implicitly working on this: [[bmad-method|BMAD's project-context.md]] tries to maintain shared state across agents; [[codespeak|CodeSpeak's managed files]] (per [[codespeak-modularity]]) maintain per-spec source-file scope with notification on cross-boundary writes; [[sdd-course-deeplearning-ai|Paul Everett's course]] uses dated spec branches. None of these provides the *runtime queryable graph* Aslan describes (*"Which code symbols implement requirement RQ-12?"*). So Aslan's claim is correct in spirit — there's no broadly adopted **queryable, runtime, bidirectional** traceability layer — but partially answered by file-system conventions in some adjacent tools.

4. **Has Aslan ingested the wiki's School-1 / School-2 framing or arrived at his own?** The "missing link" position implies a third stance not directly anticipated by [[code-legibility-debate]]: don't pick black-box vs. must-read; build infrastructure to navigate between spec and code on demand. Worth surfacing on the legibility-debate concept page as a third school: **"Traceability School."**

5. **Which repos is the author a contributor to?** Disclosure is unspecific. Author's repo (https://github.com/murataslan1) may help. Worth a follow-up check before treating tool descriptions as fully neutral. (None of the seven tools names Aslan directly in their README based on initial reading.)

6. **Is L5 (Product Surface) still emerging or already a category?** gsd-2 alone in the column. CodeLayer, ACP, the Weaving Loom, and possibly cron-Ralph deployment surfaces (per [[matt-pocock-dex-horthy-chat]]) are arguably also L5. May be premature to call this a settled layer.

7. **Why no benchmark data?** Aslan explicitly disclaims *"This post is not a benchmark or a ranking."* But the wiki does have benchmark anchors ([[anatomy-agent-harness|TerminalBench 2.0]], [[skill-issue-harness-engineering|Terminal Bench harness-overfitting data]], [[ai-in-sdlc-research|SDD-vs-vibe-coding observations]]). Would be useful to test these stack combinations against measurable failure-mode reduction.

## Why This Source Matters

Five reasons this source earns a top-row entry on the index, despite overlapping substantially with existing material:

1. **Cleanest cross-pillar synthesis the wiki has yet ingested.** Touches all five research pillars in one post — most prior sources hit two or three.
2. **First explicit failure-mode taxonomy for agentic coding.** Five named failure modes mapped to layers; gives the wiki a vocabulary it didn't have.
3. **Adds four genuinely new entities** (Ctxo, RTK, context-mode, gsd-2) — first time any of them appear in the wiki.
4. **Sharpens the [[superpowers]] positioning** — clean L2 framing as "Agent Discipline" distinct from L1 methodology tools.
5. **Names the missing-link category** — spec-to-code traceability — that several other wiki sources circle but don't name. Becomes a new entry on the [[code-legibility-debate]] and [[spec-driven-development]] open-question lists.

## Source File

- `raw/agentic-coding-stack-aslan-2026.md` — full article body (~20.6k chars verbatim DOM `innerText`, fetched via Playwright on 2026-04-16)
