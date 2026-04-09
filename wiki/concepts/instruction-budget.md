---
title: "Instruction Budget"
type: concept
pillar: coding-agents
created: 2026-04-08
updated: 2026-04-08
sources: [dex-rpi-to-crispy, coding-agents-conf-2026]
tags: [prompting, context-window, control-flow, reliability]
---

# Instruction Budget

## Definition

The **instruction budget** is the maximum number of discrete instructions an LLM can reliably follow in a single context window. Beyond this threshold, the model begins half-attending to all instructions rather than fully following each one, leading to unpredictable skipping and degraded workflow adherence.

## Key Sources

- **[[dex-rpi-to-crispy]]** — Primary source. Cites arxiv paper 2507.11538 showing frontier LLMs follow **~150-200 instructions** with good consistency. RPI's single `/create_plan` prompt had 85+ instructions, plus CLAUDE.md, system prompt, tools, and MCPs — well over budget. The slide version of the talk includes per-model accuracy-vs-instructions charts for Gemini 2.5 Pro, GPT-4, and Claude 3.7 Sonnet — all show significant accuracy drops beyond 150-200 instructions.
- **[[coding-agents-conf-2026]]** — Databricks talk mentions "too many MCPs" filling the context window with tool instructions, degrading code-writing quality. Same root cause.

## Current Understanding

The instruction budget is a **practical constraint on prompt design** with major implications:

1. **Monolithic prompts fail.** RPI's 85-instruction planning prompt worked for experts who discovered compensating behaviors ("magic words") but failed for ~50% of users. The fix was splitting into multiple prompts of <40 instructions each.

2. **The budget is shared.** Instructions from your prompt, CLAUDE.md, system prompt, tool descriptions, and MCP server specs all count against the same budget. Adding MCPs reduces the budget available for your actual workflow instructions.

3. **Use control flow, not prompts, for workflow.** Dex: "Don't use prompts for control flow if you can use control flow for control flow." If statements and classifiers are more reliable than instructing a model to conditionally branch.

4. **The number may be model-dependent.** The ~150-200 figure comes from one paper on frontier models. Different models likely have different budgets, and the number may improve over time.

## Practical Guidelines

- Keep individual prompts under **40 instructions** (CRISPY target)
- Audit your total instruction load: prompt + CLAUDE.md + system prompt + tools + MCPs
- Split complex workflows into **multiple context windows**, each with focused instructions
- Use deterministic code (classifiers, if statements) for branching, not prompt instructions

## Open Questions

- Is 150-200 the right number across all frontier models, or does it vary significantly?
- Will this budget increase meaningfully with model improvements, or is it a fundamental attention limitation?
- How do you count "instructions" consistently? (Single sentences? Bullet points? Nested conditions?)
- Does the budget degrade linearly or is there a cliff?

## Related Concepts

- [[context-engineering]] — instruction budget is the core constraint context engineering works within
- [[12-factor-agents]] — Factor #8 "Don't use prompts for control flow" is directly related
