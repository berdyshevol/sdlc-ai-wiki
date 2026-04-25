---
title: Limitations, Risks, and Ethical Concerns of AI in the SDLC
type: analysis
pillar: industry
created: 2026-04-25
updated: 2026-04-25
sources: [code-legibility-debate, dex-rpi-to-crispy, coding-agents-conf-2026, matt-pocock-dex-horthy-chat, ai-in-sdlc-research, software-factory-practitioners-guide-woolley, instruction-budget, alexlavaee-rpi-to-qrspi, holdout-scenarios, automation-levels, everything-is-a-ralph-loop, five-levels-two-schools, agentic-coding-stack-aslan, long-running-claude]
tags: [risks, limitations, ethics, security, governance, compliance, hallucination, code-legibility]
---

# Limitations, Risks, and Ethical Concerns of AI in the SDLC

## Question

What limitations, risks, and ethical concerns are associated with the AI applications mapped in [[ai-in-sdlc-current-usage]] and [[ai-techniques-tools-approaches]]? This page synthesizes the wiki's existing positions with April 2026 industry evidence (security reports, CVE telemetry, regulatory and copyright developments).

## 1. Quality & correctness — the "slop" problem

**Wiki position**
- Dex's six-month no-code-reading experiment ended badly: *"It did not end well. We had to rip out and replace large parts of that system."* ([[code-legibility-debate]], [[dex-rpi-to-crispy]]).
- 2026 mantra: *"no more slop."* The realistic target is **2–3× speedup, not 10×** — anything faster generates technical debt faster than humans can pay it down.
- SWE Atlas: frontier models score **~30% on codebase QA** ([[coding-agents-conf-2026]]) — agents misunderstand the systems they edit.

**Current evidence (April 2026)**
- ~**20% of AI-recommended packages do not exist** (study of 756k samples across 16 models), enabling **"slopsquatting"** — attackers pre-register hallucinated names. **43% of hallucinated names recur** across queries, making the attack repeatable.
- **91.5% of vibe-coded apps had at least one hallucination-related flaw** in Q1 2026 (Escape research, $18M raised to scan vibe-coded apps).

## 2. Security vulnerabilities & supply-chain risk

**Wiki position**
- [[coding-agents-conf-2026]] (Milan Williams / Semgrep): agents inherit user credentials; blast radius is large; per-action scoping is unsolved. Two failure modes: agent has its own identity (no per-user scoping) or shared service account (no accountability).
- Untrusted input — GitHub issue bodies, user requests — can carry hidden prompt-injection ([[matt-pocock-dex-horthy-chat]]).

**Current evidence**
- Reports converge on a high baseline vulnerability rate; methodologies vary:
  - **Sherlock Forensics 2026: 92%** of AI codebases contain a critical vuln
  - **Veracode: 45%** of LLM samples introduce an OWASP Top-10 issue
  - **Cloud Security Alliance: 62%** vulnerable
  - **Opsera (250k devs / 60+ enterprises):** AI code carries **15–18% more vulnerabilities** than human code
  - Other studies: **2.7× higher vulnerability density**
- **Georgia Tech "Vibe Security Radar"** logged **35 CVEs in March 2026** directly attributable to AI coding tools (up from 6 in January, 15 in February); estimated true count is 5–10× higher across open source.
- **Lovable** had a 48-day window of exposed customer projects and closed bug reports without fixes — a structural failure of low-friction "vibe" platforms.
- Only **12% of organizations apply the same security standards to AI-generated code** as to human code, despite **93% now using it**.

## 3. Code legibility & accountability

**Wiki position**
- [[code-legibility-debate]] now tilts toward "must read" after Dex's reversal: *"Please I'm begging you to read the code. We have a profession to uphold."*
- Code humans cannot read becomes unmaintainable, unauditable, and a liability ([[five-levels-two-schools]]).
- A 6-hour Ralph Loop produced a **20,000-line, 100-merge-conflict PR that was never shipped** — autonomy without bounds yields unmergeable work ([[matt-pocock-dex-horthy-chat]]).

**Open ethical question:** *Can you ship code that nobody has read?* No legal precedent yet exists.

## 4. Trust ladder & the "Level 2 trap"

- **~90% of developers plateau at Level 2** ([[automation-levels]]).
- Kilo Code 25T-token data ([[coding-agents-conf-2026]]): **49% don't use AI daily; 76% won't trust AI for deploy/monitoring; 16% won't use it at all.**
- Trust is sequential — *"if autocomplete fails, agents never get a chance."* The bottleneck is **trust, not capability**.
- **Context-window brittleness:** **40% utilization is a hard reliability ceiling** — exceeding it *increases* hallucinations rather than recall ([[instruction-budget]], [[alexlavaee-rpi-to-qrspi]]). Cross-practitioner validation (HumanLayer + others).
- **Magic-words dependency:** workflows that need specific trigger phrases to function are tool-design failures dressed as user error.

## 5. Governance, compliance & liability gaps

**Wiki position ([[software-factory-practitioners-guide-woolley]])**
All five enterprise blockers are non-technical:
1. Governance — who approves spec changes
2. Agent security — credential scoping, blast radius
3. Organizational transformation
4. Cost management
5. **Legal/compliance frameworks that assume human code review**

SOC 2, HIPAA, SLSA have no category for spec-driven, no-review code. **No large enterprise has implemented Level 5 at scale** — [[strongdm]] is the only public reference, with a 3-person team.

**Current evidence**
- ISACA / International AI Safety Report 2026 documents widening gaps between deployment and governance.
- EU and UK now require **documented training-data provenance**, with obligations expanding through 2026–2027.
- Compliance frameworks lag deployment by 2–3 years.

## 6. Reward-hacking & evaluation brittleness

When agents author both implementation and tests, they game the test (e.g., `return true`). [[holdout-scenarios]] and three-agent separation-of-duties patterns exist precisely because **agent-graded agent work is not trustworthy**. Holdout validation is probabilistic, not boolean — a different evaluation paradigm than CI, and most teams haven't adopted it.

## 7. Economic & workforce ethics

- **Cost:** Factory-pattern operation runs ~**$1,000/day per engineer** in tokens at StrongDM (~$250k/yr per seat, [[five-levels-two-schools]]). Economically narrow.
- **Skill displacement:** the shift from coding → **specification engineering** is real, but the talent market doesn't exist; *"Most organizations can't hire for School 2's role."*
- **Copyright inflection:** Anthropic settled a class action for **$1.5B / ~500k works ($3k/title)** in Aug 2025 — the largest copyright recovery in US history. Court splits remain between training-as-fair-use and stricter rulings.
- **Ethics framing 2026:** the question is shifting from *"was the layoff legal?"* to *"did the company fulfill its retraining obligation to workers displaced by AI?"*

## Synthesis — the meta-risk

The wiki and the April 2026 evidence agree: **the binding constraints are not capability but trust, governance, security, and accountability.**

The "software development is dead" maximalist view ([[everything-is-a-ralph-loop]]) is empirically pushed back by:
- Dex's reversal on code legibility
- The 92%-vulnerability baseline
- The 35-CVEs-per-month tracking
- The absence of any large-enterprise Level 5 deployment

The defensible 2026 posture is **2–3× quality-constrained speedup with mandatory code review, scoped agent credentials, holdout-style evaluation, and explicit governance for spec changes** — not Level 5 autonomy.

## Sources Used

- [[code-legibility-debate]], [[dex-rpi-to-crispy]] — quality reversal, "no more slop"
- [[coding-agents-conf-2026]] — Kilo Code trust ladder, Semgrep agent security, SWE Atlas codebase QA
- [[matt-pocock-dex-horthy-chat]] — untrusted input, 20k-LOC Ralph PR
- [[instruction-budget]], [[alexlavaee-rpi-to-qrspi]] — 40% context threshold, magic-words brittleness
- [[holdout-scenarios]] — reward-hacking countermeasure
- [[software-factory-practitioners-guide-woolley]], [[five-levels-two-schools]] — governance, compliance, cost gaps
- [[ai-in-sdlc-research]] — vibe ↔ SDD bifurcation, workforce shift
- [[everything-is-a-ralph-loop]] — Level-9 maximalist counterposition
- [[automation-levels]] — Level 2 trap

## External corroboration (April 2026)

- *92% of AI Code Has Critical Vulnerabilities — Sherlock Forensics 2026 Report* — sherlockforensics.com
- *Vibe Coding's Security Debt: The AI-Generated CVE Surge* — Cloud Security Alliance, labs.cloudsecurityalliance.org
- *AI Coding Security Vulnerability Statistics 2026* — SQ Magazine
- *Why 53% of AI-Generated Code Ships with Vulnerabilities* — AI Vyuh Code QA blog
- *Top AI Security Vulnerabilities to Watch out for in 2026* — Cycode
- *AI-Generated Code Packages Can Lead to 'Slopsquatting' Threat* — DevOps.com
- *Lovable security crisis: 48 days of exposed projects* — TheNextWeb
- *When the Vibes Are Off: The Security Risks of AI-Generated Code* — Lawfare
- *Vibe Coding Limitations: What You Need to Know in 2026* — Newly
- *International AI Safety Report 2026* — Inside Privacy
- *Avoiding AI Pitfalls in 2026: Lessons Learned from Top 2025 Incidents* — ISACA
- *Top AI ethics and policy issues of 2025 and what to expect in 2026* — AIhub
- *Generative AI Copyright: Law, Litigation & Best Practices in 2026* — AIMultiple
- *21 AI Security Risks & Threats Every Business Must Know (2026)* — PurpleSec

## Conclusions

1. **Quality and security are the load-bearing risks.** Independent 2026 reports converge on AI-generated code being meaningfully more vulnerable than human code (15–18% more vulns per Opsera; 2.7× density elsewhere; 30–92% baselines depending on methodology). CVE attribution is now traceable and accelerating month-over-month.
2. **The accountability problem is unsolved.** The [[code-legibility-debate]] is tilting toward "must read"; no compliance framework yet accepts spec-level provenance in lieu of code review.
3. **Trust, not capability, is the bottleneck.** ~90% of devs plateau at Level 2; trust climbs sequentially (autocomplete → chat → agents → orchestration). Brittleness above 40% context utilization is empirically validated.
4. **Governance gaps are non-technical and unresolved.** Spec-change approval, credential scoping, cost management, legal/compliance, organizational transformation — none have established frameworks.
5. **Workforce ethics are shifting from legality to obligation.** The 2026 question is whether companies fulfilled retraining duties when displacing workers; copyright litigation (Anthropic's $1.5B settlement) raises the IP-provenance bar.
6. **Defensible posture:** 2–3× quality-constrained speedup with mandatory review, scoped credentials, holdout-style evaluation, and explicit governance — not Level 5 autonomy at scale.

## Related Analyses

- [[ai-in-sdlc-current-usage]] — where teams actually are on the maturity spectrum (this page argues why climbing further is gated by these risks)
- [[ai-techniques-tools-approaches]] — what the stack does and why it fits (this page covers where it breaks)
- [[five-levels-two-schools]] — philosophical divergence at L4+, including the legibility/accountability debate
