# The Agentic Coding Stack: 7 Tools, 5 Layers, and the Missing Link Nobody Has Built Yet

**Author:** Murat Aslan
**Publication:** Dev Genius (Medium)
**Date:** April 2026 (~2026-04-11, "5 days ago" as of 2026-04-16)
**URL:** https://blog.devgenius.io/the-agentic-coding-stack-7-tools-5-layers-and-the-missing-link-nobody-has-built-yet-de264b260db3
**Read time:** 13 min

---

Series 1 of Agentic Coding Systems.

A practitioner's map of the agentic coding ecosystem: what each tool is for, where it fits in the stack, and what still does not exist.

AI coding assistants are no longer just function generators. The serious question in 2026 is different: how do you make an AI plan well, understand a real codebase, work with engineering discipline, avoid wasting tokens, and stay reliable across long sessions?

Most conversations about AI devtools still collapse into the wrong debate: "Which tool wins?" That framing misses the point. The best tools are often not direct competitors. They live at different layers of the workflow.

After analyzing seven tools across this space, my conclusion is simple: serious agentic coding needs a stack, not a favorite tool.

Disclosure: I am a contributor to some repos. That is exactly why I want to make the evaluation criteria explicit. This post is not a benchmark or a ranking. It is a stack map based on four questions: what problem does the tool solve, which layer does it belong to, when should you use it, and what cost does it introduce?

## The Real Problem

When teams say "AI worked great for the first hour and then everything got weird," the failure is usually not model quality alone. It is stack design.

In practice, five failure modes show up over and over:

- **Consistency failures**: the same kind of prompt produces different implementation quality across sessions.
- **Context loss**: the agent sees too much raw output, drops important state, and starts contradicting itself.
- **Specification gaps**: product intent does not survive the trip from idea to code.
- **Review bottlenecks**: code generation accelerates, but confidence and quality control do not.
- **Multi-session conflicts**: parallel agent work creates merge pain, overlapping edits, and fragile ownership.

Every tool in this post reduces one or more of these failures. None eliminates all five.

That is the core thesis for this series: agentic coding is a systems problem.

## The 5-Layer Map

**Layer 1 — Delivery Methodology**
- Primary question: When should the AI analyze, plan, and implement?
- Tools: BMAD-METHOD, spec-kit
- Main failure modes reduced: Consistency failures, specification gaps

**Layer 2 — Agent Discipline**
- Primary question: How should the AI behave while building?
- Tools: superpowers
- Main failure modes reduced: Review bottlenecks, consistency failures

**Layer 3 — Technical Context**
- Primary question: What does the code actually mean?
- Tools: Ctxo
- Main failure modes reduced: Review bottlenecks, multi-session conflicts

**Layer 4 — Token Optimization**
- Primary question: How much tool output should enter context?
- Tools: RTK, context-mode
- Main failure modes reduced: Context loss

**Layer 5 — Product Surface**
- Primary question: Where does the developer operate the whole system?
- Tools: gsd-2
- Main failure modes reduced: Multi-session conflicts, review bottlenecks

This model matters because bad tool decisions usually come from mixing up layers. Teams compare a methodology tool with a token tool, or a semantic analysis tool with a product shell, and then wonder why the conclusion feels fuzzy.

The right way to compare is this:

1. First ask which layer is missing in your workflow.
2. Then choose the lightest tool that solves that missing layer.
3. Only add the next layer when the previous one becomes a bottleneck.

## Layer 1: Delivery Methodology

This layer answers a deceptively simple question: when should the AI do what?

Without a methodology layer, agents jump straight to code, skip problem framing, and produce work that looks productive but ages badly.

### BMAD-METHOD

**What it is:** An AI-assisted delivery methodology with 34+ workflows, 12+ expert personas, and a structured multi-phase approach to moving from analysis to implementation.

**Why it matters:** BMAD's real value is not "more prompts." It is sequencing. The four-phase structure forces the agent to analyze first, plan second, solution third, and implement last. That one constraint prevents a surprising amount of architectural churn.

```
npx bmad-method install
# installs personas, workflows, and modular configs into the repo
```

**Use it when:** You are working on large repositories, teams with governance or compliance expectations, or product areas where "just start coding" creates long-tail cleanup.

**Helps most with:** consistency failures and specification gaps.

**Trade-off:** Ceremony. BMAD is intentionally opinionated. For a narrow fix or a one-file patch, the workflow overhead can outweigh the gain. It also costs more tokens because each stage loads its own planning context.

**My take:** BMAD is strongest when your real enemy is premature implementation.

### spec-kit

**What it is:** GitHub's spec-driven development toolkit. It is lighter than BMAD and focused on installing a spec-first artifact chain into a repo.

```
constitution -> specify -> plan -> tasks -> implement
```

**Why it matters:** spec-kit treats specifications as executable workflow artifacts rather than documentation that gets ignored after kickoff. The fact that it can emit agent-specific command files for many AI platforms makes it especially practical for mixed-tool teams.

**Use it when:** You want spec-first behavior without adopting a full methodology system. It is a strong fit for greenfield work, product teams that already think in requirements, and teams standardizing across multiple AI tools.

**Helps most with:** specification gaps and consistency failures.

**Trade-off:** It is younger and narrower than BMAD. The overlap between the two can confuse adoption. Most teams do not need both. If you choose BMAD, choose it because you want process depth. If you choose spec-kit, choose it because you want lighter structure.

**My take:** BMAD is the heavier operating model. spec-kit is the cleaner starting point for teams that want structure without a full methodology culture shift.

## Layer 2: Agent Discipline

Methodology decides the sequence. Discipline decides the behavior inside that sequence.

This is the layer many teams underestimate. Even with a great plan, an undisciplined agent still guesses, skips tests, and declares victory too early.

### superpowers

**What it is:** A skill and workflow library that injects engineering discipline into AI agents. It does not decide the delivery phases. It decides how the agent behaves while executing.

**Why it matters:** The best part of superpowers is that it operationalizes engineering habits that humans often claim to value but skip under time pressure: test-driven development, systematic debugging, scoped delegation, and verification before completion.

Core behaviors it reinforces:

- TDD before implementation
- Systematic debugging instead of random trial-and-error
- Deliberate subagent delegation for bounded tasks
- Explicit verification gates before claiming completion

**Use it when:** You already know what you are trying to build and need the agent to behave like a disciplined engineer instead of an eager autocomplete engine.

**Helps most with:** review bottlenecks and consistency failures.

**Trade-off:** Prompt weight and rigidity. Strong process skills cost tokens, and the TDD-first posture can feel heavy for tiny edits. That is not a bug in the system; it is the price of discipline.

**My take:** If BMAD or spec-kit answers "what order should work happen in?", superpowers answers "how do we stop the agent from being sloppy once work begins?"

## Layer 3: Technical Context

This layer answers the question most AI coding setups still handle badly: what does this code actually mean?

Without a technical context layer, even a disciplined agent is still operating with a shallow mental model.

### Ctxo

**What it is:** An MCP server for semantic codebase analysis. It exposes deeper questions than plain text search can answer: blast radius, logic slices, why-context from git history, symbol importance, dead code, and PR impact.

**Why it matters:** Ctxo moves the workflow from "find me a string" to "help me understand the system." That difference becomes critical as soon as the change crosses module boundaries, touches shared abstractions, or depends on historical intent.

Representative questions it can answer:

- What breaks if I change this? → `get_blast_radius`
- What does this symbol depend on? → `get_logic_slice`
- Why was this implemented this way? → `get_why_context`
- What code matters most in this repo? → `get_symbol_importance`
- What appears to be dead? → `find_dead_code`
- What is the likely risk of this PR? → `get_pr_impact`

**Use it when:** The cost of misunderstanding the code is higher than the cost of indexing the repo. In other words: non-trivial edits, shared modules, legacy surfaces, or changes where "just inspect a few files" is not good enough.

**Helps most with:** review bottlenecks and multi-session conflicts.

**Trade-off:** There is an indexing step, and the strongest support today is still TypeScript/JavaScript. That means it is not the first tool I would add to a toy project or a throwaway script.

**My take:** This is the scarcest capability in the current ecosystem. Plenty of tools tell agents how to behave. Far fewer help them understand the code they are about to change.

## Layer 4: Token Optimization

This layer exists because the context window is still a hard systems constraint.

If your stack allows raw logs, giant diffs, and unfiltered command output to enter context, you are not just wasting tokens. You are degrading reasoning quality.

Two tools matter here, and they solve the problem from different directions.

### RTK

**What it is:** A Rust CLI proxy that intercepts shell command output and compresses it before the agent sees it.

```
Agent runs: git log -50
RTK intercepts -> applies command-specific filter -> smaller output reaches the model
```

**Why it matters:** RTK is not generic truncation. It understands command ecosystems. A test runner, a git command, and a docker command each have different "signal" patterns, and RTK uses command-specific filters to keep the right parts.

**Use it when:** Your workflow is shell-heavy and the biggest source of token waste is command output from builds, tests, git, package managers, or logs.

**Helps most with:** context loss.

**Trade-off:** It is still a hook-and-filter model. That means installation overhead per agent environment, a Rust dependency, and no session memory. RTK makes outputs smaller, but it does not change the fact that the underlying command still generated the output.

**My take:** RTK is the fastest way to improve a noisy shell-based workflow without redesigning how the agent works.

### context-mode

**What it is:** An MCP server that sandboxes tool execution and only returns what the agent explicitly prints. The raw output stays in the sandbox.

```
Agent runs code via ctx_execute
-> raw output stays in sandbox
-> only console.log() output enters context
```

**Why it matters:** context-mode changes the operating model. Instead of reading huge outputs and mentally compressing them, the agent writes code to do the analysis and prints only the answer. That "think in code" posture can cut token waste far more aggressively than post-processing alone.

**Use it when:** Sessions are long, exploration is multi-step, and you want recoverability across compaction or context resets. It is especially strong when the right move is not "filter output" but "do the analysis inside the sandbox."

**Helps most with:** context loss.

**Trade-off:** It depends on agent routing discipline. If the agent keeps reaching for native shell tools instead of sandbox execution, the value drops. Startup is also heavier than a tiny Rust binary.

**My take:** RTK optimizes noisy commands. context-mode optimizes the workflow itself.

### RTK vs context-mode

These are not substitute products in the narrow sense. They attack token waste at different points in the pipeline.

**RTK**
- Operating layer: OS/shell hook
- Core idea: Filter command output after execution
- Intelligence model: Static command-specific rules
- Session continuity: None
- Best first use case: Shell firehose
- Main weakness: No memory, bounded by command output

**context-mode**
- Operating layer: MCP sandbox
- Core idea: Prevent raw output from entering context
- Intelligence model: Dynamic analysis written by the agent
- Session continuity: SQLite + FTS5 retrieval
- Best first use case: Long research/exploration sessions
- Main weakness: Depends on correct tool routing

My rule of thumb is simple:

- If your pain is "the shell talks too much," start with RTK.
- If your pain is "the agent should compute the answer instead of reading noise," start with context-mode.
- If you are operating at scale, use both.

Used together, they form a clean sequence: RTK reduces noisy shell output, then context-mode keeps the remainder from flooding the conversation.

## Layer 5: Product Surface

At some point the stack stops being a set of components and becomes a user experience problem.

That is where the product surface layer shows up: the place where planning, execution, state, cost, and recovery are exposed as an operating system for AI work.

### gsd-2

**What it is:** A full autonomous coding agent platform. Where the other tools act like stack components, gsd-2 looks like an integrated product surface around long-running agentic work.

```
gsd auto -> plan -> execute -> verify -> commit -> repeat
```

**Why it matters:** gsd-2 is valuable when the problem is no longer "I need a better prompt flow" and becomes "I need a controlled operating environment for autonomous work." Worktree isolation, state recovery, multi-provider support, cost tracking, and milestone execution all become more important at that scale.

**Use it when:** You want an actual operational shell for agentic development across larger scopes, longer task horizons, and more autonomous execution.

**Helps most with:** multi-session conflicts and review bottlenecks.

**Trade-off:** Complexity. It is a bigger mental and operational commitment than adding one narrow capability. For a solo developer doing tactical edits, it can be too much machinery.

**My take:** gsd-2 is not just "another tool" in the same category as the others. It is the closest thing in this set to a full product shell for the stack.

## Recommended Combinations

The fastest way to misuse this ecosystem is to install everything at once.

Instead, start from the failure mode that hurts you most.

**1. Solo developer, minimum overhead**
`superpowers + Ctxo + RTK`

Why this works: superpowers adds discipline, Ctxo reduces accidental misunderstanding, and RTK cleans up shell noise with relatively low operational overhead.

Use this if: you work mostly alone, you care about code quality, and you want better outcomes without adopting a full orchestration platform.

Upgrade path: add context-mode when your sessions become research-heavy or you start losing continuity across long conversations.

**2. Team workflow, larger repos**
`BMAD-METHOD + superpowers + Ctxo + gsd-2`

Why this works: BMAD provides sequencing, superpowers enforces implementation discipline, Ctxo gives semantic understanding, and gsd-2 gives the team a structured operating surface.

Use this if: the cost of inconsistent agent behavior is already visible in architecture, review, or merge quality.

Skip this if: your team is still proving whether agentic coding is valuable at all. This stack is for operationalization, not experimentation.

**3. Spec-first product development**
`spec-kit + superpowers + Ctxo`

Why this works: spec-kit establishes the artifact chain, superpowers keeps implementation honest, and Ctxo helps connect changes back to the actual system you are modifying.

Use this if: your team already writes specs and wants AI to respect them instead of bypassing them.

Escalation rule: if governance, handoffs, or program-level coordination become the main problem, move from spec-kit toward BMAD.

**4. Token-constrained environments**
`RTK + context-mode + Ctxo`

Why this works: RTK handles shell verbosity, context-mode handles sandboxed extraction and continuity, and Ctxo provides compact semantic context instead of huge manual file dumps.

Use this if: your agent spends too much time reading logs, diffs, or command output and not enough time reasoning.

Practical rule: RTK is the low-friction first step. context-mode is the deeper systems step.

## The Gap Nobody Has Filled Yet

After looking across all seven tools, one gap stands out more than any other: **spec-to-code traceability**.

Today the ecosystem is getting better at the edges:

- Methodology tools generate intent artifacts
- Discipline tools improve execution behavior
- Semantic tools explain code relationships
- Token tools protect context quality
- Product shells coordinate autonomous work

But the bridge between specification and implementation is still weak.

The missing questions are the important ones:

- **Which code symbols implement requirement RQ-12?** Prevents intent from disappearing during execution.
- **Which tests cover this spec item?** Makes review and regression analysis tractable.
- **If this requirement changes, what breaks?** Connects product change to technical impact.
- **Which open PRs or agents are touching the same requirement?** Reduces multi-session and multi-agent conflicts.

This is the real unclaimed layer in the market.

BMAD and spec-kit create intent. superpowers improves execution quality. Ctxo gets closest to the code-side graph. But there is still no broadly adopted system that tracks a requirement through design, implementation, tests, and ongoing change.

If someone builds that bridge well, they will not just have a useful feature. They will own the most strategic connective tissue in the agentic coding stack.

## 5 Lessons Learned

1. **The worst tool debates are really layer-confusion debates.** Teams waste time comparing tools that are not trying to solve the same problem. Once you separate methodology, discipline, semantic context, token optimization, and product surface, most of the confusion disappears.

2. **Good planning does not compensate for poor code understanding.** A methodology can sequence work beautifully, and an agent can still make unsafe changes if it does not understand the system it is modifying.

3. **Token optimization is reliability infrastructure, not a nice-to-have.** When context is noisy, output quality degrades. That is not cosmetic. It affects reasoning, review quality, and continuity.

4. **The lightest useful stack usually wins first.** Most teams should not begin with the most complete setup. They should begin with the smallest combination that removes the most painful failure mode.

5. **Spec-to-code traceability is the next serious frontier.** The ecosystem is getting better at planning and execution. The next major advantage will come from preserving intent all the way into code and tests.

## Quick Reference

- **BMAD-METHOD** — Methodology. Use when: you need structured multi-phase delivery and strong process guardrails. Avoid when: the task is small and speed matters more than ceremony. Trade-off: workflow overhead.
- **spec-kit** — Methodology. Use when: you want a lighter spec-first workflow across AI tools. Avoid when: you already need a deeper operating model. Trade-off: less depth than BMAD.
- **superpowers** — Discipline. Use when: you want TDD, debugging discipline, and verification behavior. Avoid when: the task is tiny and process cost dominates. Trade-off: prompt weight and rigidity.
- **Ctxo** — Technical Context. Use when: understanding impact is more important than fast generation. Avoid when: the repo is trivial or throwaway. Trade-off: indexing and language coverage trade-offs.
- **RTK** — Token Optimization. Use when: shell output is your main source of token waste. Avoid when: your workflow is not shell-centric. Trade-off: no memory, bounded by filters.
- **context-mode** — Token Optimization. Use when: you want sandboxed extraction and long-session continuity. Avoid when: the agent cannot reliably route to sandbox tools. Trade-off: heavier runtime and routing dependency.
- **gsd-2** — Product Surface. Use when: you want a full operational shell for autonomous coding work. Avoid when: you are still validating basic usage. Trade-off: complexity.

---

This post is the first entry in a broader series on agentic coding systems. The point of the series is not to collect tools. It is to understand the architecture that makes AI coding reliable.

The tools analyzed here: BMAD-METHOD, spec-kit, superpowers, Ctxo, RTK, context-mode, gsd-2.

Author repo: https://github.com/murataslan1
