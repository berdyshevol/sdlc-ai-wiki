---
title: "Ralph Loops: Build Dumb AI Loops That Ship — Chris Parsons"
type: source
pillar: software-factories
created: 2026-05-05
updated: 2026-05-05
sources: [parsons-ralph-loops-workshop.md]
tags: [ralph-loop, workshop, claude-code, skills, slash-loop, theory-of-constraints, sandboxing, lethal-trifecta, just-in-time-specs, ticket-driven, practitioner]
---

# Ralph Loops: Build Dumb AI Loops That Ship

**Author:** Chris Parsons (CTO, Cherrypick — AI adoption consultancy; ex-startup CTO, ex-agency CEO)
**Venue:** AI Engineer (workshop, ~2 hours, live demo + extended Q&A)
**URL:** https://www.youtube.com/watch?v=2TLXsxkz0zI
**Pillar:** [[software-factory]] / [[agent-harness]]

## Summary

A hands-on, two-hour workshop teaching the [[everything-is-a-ralph-loop|Ralph Loop]] pattern that Geoffrey Huntley introduced in January 2026. Parsons positions it as the natural successor to brittle visual-orchestration tools (he opens with an n8n nightmare story — a complex newsletter workflow that broke at 2pm every Monday) and demonstrates a far simpler alternative: a single skill running in a loop with the right prompt. He credits Matt Pocock as the person who showed him how to take Ralph loops "to the next level," and Ash Maru for the startup-loop ideas.

The pedagogical core is a live demo on a deliberately under-engineered Pomodoro timer with a `doc/tickets/` folder. Parsons walks the audience from the dumbest form ("implement this ticket" → repeat) up to the practical form: **"implement the next most important ticket using TDD principles from doc/tickets — commit when done."** The key conceptual move is rejecting up-front dependency graphs (which he tried and failed at — "I had recreated waterfall and given it to Claude") in favor of letting the model pick the next most important ticket each iteration. He shows three loop substrates in increasing sophistication: hitting Enter manually, a `while true; do claude -p ...` shell loop, and the new Claude Code `/loop` slash command (with `cron_create` under the hood, e.g., `/loop every minute build the next ticket`).

He shares his actual Ralph skill, framed as **"you are one engineer in a relay team — do exactly one change, then drop the context and stop, start again."** The skill encodes ticket format, status values, git-state checks, recovery semantics for crashed runs (dirty tree + tests passing = probably done; tests failing = mid-flight, throw away), and refactoring/test-passing checks. He generalizes well beyond code: the same loop pattern runs his newsletter writing, a 6 a.m. morning briefing, a 15-minute heartbeat check, a Kanban-style worker loop reading project files, and an experimental `startup` skill that produced an unprompted investor memo deck.

The Q&A section is unusually substantive. Parsons argues against spec-driven tools like [[kiro]] ("I worry that will fossilize one approach with AI that works today but may not work when Mythos comes out"); favors **just-in-time specs** built iteratively in chat. He invokes Goldratt's *Theory of Constraints* — AI exposes whichever step is the bottleneck (often release process or review, not coding speed), and teams that don't fix the actual constraint will go *slower* with AI. On security, he runs Claude on a VPS with separate keys, fine-grained permissions, never letting it send email — only draft — and points to Simon Willison's **lethal trifecta** (untrusted tokens + internet access + secret data = data loss). On parallel orchestration (Gas Town, MCP agent mail), he's skeptical: "they're solving a problem most people don't have yet"; the bottleneck is usually you, not tokens-per-second.

The most existential thread runs through the second hour: when AI handles all the rubbish work, the developer becomes a reviewer of work they didn't want to do in the first place. Parsons' response is to redesign feedback so the AI evaluates its own output (sub-agent adversarial review, audience-simulation skills, screenshot loops), and to consciously decide which work he wants to keep — strategy, thinking — versus offload entirely.

## Key Claims

- **Loops, not workflows** — visual orchestration (n8n) is brittle; "the future of automation looks more like a single skill running in a loop in Claude Code." Most agents already are loops.
- **The Ralph prompt** — "implement the next most important ticket using TDD principles from doc/tickets, commit when done" is enough; let the model figure out dependencies on the fly.
- **No more dependency graphs** — orchestrating large numbers of agents with hand-built dependency graphs *is the waterfall pattern*. AI can't manage what humans couldn't manage either. Start with one loop; don't reach for parallelism.
- **Three loop substrates** — manual re-prompt → `while true; do claude -p ...; done` shell loop → Claude Code `/loop every minute …` (cron-backed) slash command.
- **The relay-engineer prompt** — Parsons' Ralph skill literally tells the agent "you are one engineer in a relay team — do exactly one change, then drop the context and stop." Encodes git-state checks, recovery semantics, ticket format.
- **Latest models obsolete the original Ralph** — Opus 4.6 / Sonnet 4.6 / GPT-5.12+ rarely need the "are you really done?" re-prompt; the simple loop variant is the one that pays off now.
- **Everything is a loop** — newsletters, morning briefings, calendar checks, project Kanban, even running a startup. Parsons has ~50 skills powering loops across his personal/professional life.
- **Anti-spec-driven (cautiously)** — wary that tools like [[kiro]] *codify* one workflow into the tool itself, fossilizing a 2025-era process; prefers iterative just-in-time specs built in chat.
- **Theory of Constraints applied to AI teams** — AI tools expose the actual bottleneck. Teams that don't fix it (often: release cadence, review process) go *slower* with AI. Read *The Goal* (Goldratt, 1984).
- **Lethal trifecta (citing Simon Willison)** — untrusted tokens + internet access + access to secrets ⇒ guaranteed data loss. Sandbox accordingly: VPS isolation, separate keys, draft-only email, Docker sandbox, his "lockbox" project for untrusted-input file-system blocks.
- **Sub-agents as a debiasing mechanism** — agents have confirmation bias about their own output; sub-agents start with empty context and find what the main agent missed. The bundled `simplify` skill is Parsons' go-to.
- **"We're in the era of free tokens"** — don't optimize loops, burn them; he's on Max-20 and pushing 80% weekly.
- **Skills are the unit; sharing is the unsolved problem** — versioning skills with git works; *distributing* them across teams (one repo per skill is too heavy; submodules don't scale; plugin marketplaces version the plugin, not the skill) is the friction Parsons' AirSkills product is trying to solve.
- **Reversible-without-embarrassment rule** — his autonomous worker loop is allowed to do anything reversible (drafts, decks, research) but not anything that would embarrass him to undo (sending email, posting to LinkedIn).
- **Cognitive debt** — even with full automation, Parsons makes his agents stop short of "closing" a project so a human stays current with the codebase.
- **Adversarial review increases ship confidence, doesn't remove the human** — audience confirmed sub-agent validation finds real issues; reviewer becomes the new bottleneck.
- **Slides built by AI** — Parsons' presentation deck was generated by his own slide skill + image skill using Nano Banana Pro; he added only the QR code by hand.

## Connections

- **[[everything-is-a-ralph-loop]]** — direct extension of Huntley's pattern. Parsons cites the Ralph Wiggum origin story, confirms the same "loop the prompt" core, but pushes harder on **iteration sequencing** ("next most important ticket") instead of dependency graphs. Where Huntley is provocative ("software development is dead"), Parsons is practical and hands-on.
- **[[matt-pocock-dex-horthy-chat]]** — Parsons publicly thanks Matt Pocock for showing him the next-level Ralph technique back in September 2025. The two workshops are direct companions; Pocock's "Ralph is back" 20k-LOC cautionary tale is the boundary of what Parsons recommends.
- **[[long-running-claude]]** — Anthropic's own Ralph-Loop reference for multi-day scientific runs uses the same prompt structure ("read CLAUDE.md, do one task, update CHANGELOG.md, repeat").
- **[[superpowers]]** — Parsons leans heavily on **skills** as the unit of reusable context. He explicitly mentions ripping ideas from the `superpowers` plugin and `simplify` (the bundled Anthropic skill) as a key sub-agent.
- **[[claude-agent-sdk]]** — the `/loop` slash command and `cron_create` are Claude Code harness features Parsons uses live; aligns with Anthropic's "dumb loop, smart model" thesis.
- **[[agent-harness]]** — Parsons' Ralph skill IS a harness configuration: ticket format, recovery semantics, git checks, sub-agent validation. A practical instance of [[skill-issue-harness-engineering|Kyle's harness-engineering]] approach.
- **[[code-legibility-debate]]** — Parsons reads diffs for security-critical code ("I won't compromise on customer data") but explicitly hates it; for newsletter-style outputs he reads only the final artifact. Sits closer to **School 1 (black box)** for low-stakes work, **School 2 (must read)** for security, with feedback-design as the long-term escape ("when AI can tell whether something is good or not, I take myself out").
- **[[context-engineering]]** — Ralph skills as the context payload; Parsons argues fresh context per iteration is now less critical with longer-context models, but the **discipline of capturing knowledge into the repo** (so any future session or human can pick up) is the durable value.
- **[[kiro]]** — explicit anti-reference. Parsons is wary of tools that hard-code one SDD workflow.
- **[[ai-techniques-tools-approaches]]** — practical evidence for "agentic loops" and "external memory (skills)" as the dominant techniques for autonomous SDLC work.
- **[[shift-work]]** — the auto-loop ↔ interactive-VCP-session distinction in Parsons' own setup is a personal-scale instance of [[strongdm]]'s shift-work pattern.

## Questions Raised

- **How do you evaluate whether a Ralph skill is actually getting better?** Parsons concedes he has no objective method — Claude is non-deterministic, A/B is noisy, he tinkers subjectively. Open question for the field.
- **Skill distribution across teams** — fundamentally unsolved. Parsons is building AirSkills as one answer; plugin marketplaces are another; nothing has won yet.
- **Where is the line between full autonomy and human review?** Parsons defaults to "don't let workers close projects" to avoid cognitive debt; everyone has to draw their own line.
- **Just-in-time specs vs. structured SDD** — Parsons' anti-Kiro stance is contrarian relative to [[bmad-method]], [[spec-kit]], [[codespeak]]. Is structured spec-first development a temporary scaffolding (Parsons' view) or the durable pattern as code becomes opaque (the [[codespeak-vibe-takeover|CodeSpeak School-1]] view)? Two strong, opposing positions in the wiki.
- **What's the right unit of work for a Ralph loop?** Parsons uses flat-file tickets; Steve Yegge's *beads* is mentioned; Linear/Jira also work. The substrate seems less important than the **"pick the next most important one"** prompt structure.
- **Is "everything is a loop" overreach?** Parsons admits an existential crisis around it ("which work do I actually want to do?"). The answer is feedback design and sub-agent evaluation — but those are still emergent practices.
- **Cost trajectory** — Parsons is at 80% of a Max-20 plan weekly and "getting the jitters." If frontier-token costs spike, the "free tokens, just burn them" stance breaks. GLM 4.6 mentioned as a hedge.
