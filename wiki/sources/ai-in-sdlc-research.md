---
title: "AI in SDLC: Artificial Intelligence in the Software Development Life Cycle"
type: source
pillar: [industry, spec-driven, coding-agents]
created: 2026-04-08
updated: 2026-04-08
sources: []
tags: [survey, sdlc, ai-tools, copilot, spec-driven, vibe-coding, rag, agents, ethics, governance, practitioner-report]
author: Research paper (academic)
date: 2026
---

# AI in SDLC: Artificial Intelligence in the Software Development Life Cycle

**Type:** Academic research paper (full survey)
**Date:** 2026

## Summary

A comprehensive survey of how Artificial Intelligence is applied across all stages of the Software Development Life Cycle. The paper covers AI's role in requirements gathering, system design, development, testing, deployment/DevOps, and maintenance. It catalogs AI techniques (LLMs, NLP, ML classification, anomaly detection, RL, embeddings, RAG, AI agents), maps real-world tools to SDLC stages, and provides a detailed case study of GitHub Copilot.

The paper's most original contribution is **Section 7: Spec-Driven Development vs. Vibe Coding**, which frames the emerging bifurcation in AI-assisted development. Vibe coding — a term popularized by Andrej Karpathy — describes an informal, iterative workflow where developers "follow the vibes" of AI output. Spec-driven development (SDD) is the structured alternative where specifications anchor code generation. The paper surveys frameworks supporting SDD ([[spec-kit|Spec Kit]], [[bmad-method|BMAD]], [[kiro|Kiro]]) and argues that SDD is more appropriate for production/enterprise environments due to improved traceability and governance.

The paper also includes a **practitioner observation** (Section 7.5): the author applied SDD practices (Spec Kit + BMAD) as a tech lead on a five-person team at a project portfolio management SaaS company. Three observable changes emerged after moving from ad-hoc AI prompting to structured specifications: (1) improved task scoping for AI agents, (2) reduced hallucination-driven rework, and (3) more consistent AI-generated code across team members. The author notes this is not a controlled study but aligns with the broader SDD literature.

The paper concludes with a risks/ethics section (hallucinations, insecure code, IP concerns, privacy, bias, skill loss, accountability, governance) and a future outlook predicting AI agents implementing full features, AI-driven code review becoming standard, and new job roles emerging.

## Key Claims

- **AI is now applied across all six SDLC stages** — not just coding, but requirements, design, testing, deployment, and maintenance
- **LLMs, RAG, and AI agents are the three most impactful AI techniques** for SDLC today
- **GitHub Copilot** is the most visible AI tool in development, with measurable productivity improvements, but introduces risks (hallucinated code, insecure patterns, IP concerns)
- **Vibe coding is effective for prototyping but risky for production** — weak documentation, lack of repeatability, hidden security vulnerabilities
- **Spec-driven development improves traceability and governance** — making it more appropriate for enterprise SDLC
- **Three SDD frameworks are emerging:** [[spec-kit|GitHub Spec Kit]], [[bmad-method|BMAD Method]], and [[kiro|Kiro]]
- **Practitioner observation:** Transitioning from ad-hoc AI prompting to SDD on a 5-person team reduced hallucination-driven rework, improved task scoping, and increased code consistency
- **Dual-track workflows may be needed:** organizations will likely maintain both vibe coding (for exploration) and SDD (for production), with governance scaling to risk
- **AI will not eliminate software engineers** but will shift work toward higher-level reasoning, design, and oversight
- **Predicted trends (3-5 years):** AI agents implementing full features (requirements → code → tests → PR), predictive DevOps, increased regulation, new roles (AI engineer, AI QA specialist, AI governance lead)

## Connections

- [[spec-driven-development]] — central concept; paper provides practitioner evidence and framework comparison
- [[bmad-method]] — cited as SDD framework; used in the practitioner observation
- [[spec-kit]] — cited as SDD framework; used in the practitioner observation
- [[kiro]] — cited as SDD framework
- [[github-copilot]] — full case study (Section 6)
- [[automation-levels]] — paper's future outlook aligns with progression toward higher automation levels
- [[software-factory]] — the paper's vision of AI agents handling full features maps to factory concepts
- [[code-legibility-debate]] — implicit in the vibe coding vs. SDD distinction: vibe coding often means not reading the code
- [[coding-agents-conf-2026]] — paper's agent predictions align with conference themes

## Questions Raised

- How do you measure ROI of SDD vs. vibe coding in a controlled setting? The practitioner observation is suggestive but not definitive.
- Is the dual-track model (vibe coding for exploration, SDD for production) stable, or will one approach dominate?
- How do governance requirements differ across SDLC stages when AI is involved?
- What is the actual security risk profile of AI-generated code compared to human-written code at scale?
- How will AI agent autonomy affect accountability frameworks in regulated industries?
