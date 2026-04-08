---
title: "The Five Levels: From Spicy Autocomplete to the Software Factory"
type: source
pillar: [software-factories, industry]
created: 2026-04-08
updated: 2026-04-08
sources: []
tags: [automation-levels, maturity-model, software-factory, role-transformation]
author: Dan Shapiro
url: https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/
date: 2026-01
---

# The Five Levels: From Spicy Autocomplete to the Software Factory

**Author:** Dan Shapiro
**Published:** January 2026
**URL:** [danshapiro.com](https://www.danshapiro.com/blog/2026/01/the-five-levels-from-spicy-autocomplete-to-the-software-factory/)

## Summary

Dan Shapiro proposes a five-level maturity model for AI-assisted software development, arguing that most developers plateau at Level 2 without realizing higher levels exist. The key insight is that progressing through the levels requires **fundamental role transformations**, not just incremental productivity gains. Each level changes *what the human does*, not just how fast they code.

The framework draws a parallel to autonomous driving levels — the progression isn't linear improvement but qualitative shifts in the human-machine relationship. Shapiro claims to personally operate at Level 4, where the developer becomes a product manager writing specs while the AI codes autonomously.

The ultimate vision — Level 5, the "Dark Factory" — references Fanuc's lights-out robot factories: fully autonomous software generation with no human oversight. Shapiro notes only small teams (<5 people) have reached this level.

## Key Claims

- **~90% of developers are stuck at Level 2** (collaborative coding), unaware that higher levels exist
- **Level 0 (Manual):** Fully human-controlled. No AI involvement.
- **Level 1 (Assisted):** AI handles discrete tasks (tests, docstrings) while human retains core work
- **Level 2 (Collaborative):** Feels like pairing with a colleague. The "dangerous illusion of completion" — developers think this is the ceiling
- **Level 3 (Managed):** Developer becomes a code reviewer/manager. "You are the human in the loop."
- **Level 4 (Autonomous):** Developer becomes PM/spec writer. "You leave for 12 hours, and check if tests pass."
- **Level 5 (Dark Factory):** Fully autonomous. Named after Fanuc's robot-only factory. No human oversight.
- **Technical deflation** only benefits teams that progress beyond Level 2
- Each level transition looks *worse* initially but unlocks exponential efficiency

## Connections

- Directly relates to [[software-factory]] concept — Level 5 is the software factory vision
- The Level 3-4 transition maps to [[spec-driven-development]] — at Level 4, the spec *is* the primary artifact
- The [[code-legibility-debate]] is implicit: at Level 4-5, do you need to read code at all?
- [[superpowers-5]] describes practices at approximately Level 3-4
- The maturity model provides a framework for evaluating all tools in this wiki ([[devin]], [[humanlayer]], [[kiro]], etc.)

## Questions Raised

- What specific practices enable the Level 2 → Level 3 transition? This seems to be where most teams get stuck.
- Is Level 5 actually achievable for complex software, or only for narrow/templated applications?
- How does the model account for debugging and maintenance? Production issues may force you back to lower levels.
- What's the relationship between team size and achievable level?
