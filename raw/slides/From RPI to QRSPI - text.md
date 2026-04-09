[cite_start]The provided slides by Dexter Horthy, CEO of HumanLayer, detail the evolution of AI-integrated software engineering workflows, moving from a simple **RPI** (Research, Plan, Implement) model to a more granular and reliable **QRSPI** framework[cite: 1056, 1193].

Here is a detailed breakdown of the core concepts and images presented:

---

## 1. The Core Evolution: From RPI to QRSPI

[cite_start]The presentation begins by identifying the limitations of the original **RPI** (Research, Plan, Implement) workflow[cite: 1079]. [cite_start]While it worked for experts, it often failed teams because the "Plan" phase became a monolithic "mega-prompt" that models often failed to follow consistently[cite: 1102, 1107].

**The Images of Workflow (Pages 95, 151-152):**

- [cite_start]**Before (RPI):** A linear diagram showing only three stages: Research $\rightarrow$ Plan $\rightarrow$ Implement [cite: 2129-2132].
- [cite_start]**After (QRSPI):** A significantly more granular sequence designed to reduce "slop" and improve leverage[cite: 1131, 2245]:
  - [cite_start]**Questions:** Detangling intent from codebase zones[cite: 1095].
  - [cite_start]**Research:** Objective compression of truth without implemention planning[cite: 1094].
  - [cite_start]**Design:** Deciding "where we are going" before writing any code[cite: 2197].
  - [cite_start]**Structure Outline:** Mapping "how we get there" (analogous to C header files)[cite: 2215, 2220].
  - [cite_start]**Plan:** A tactical document for the agent to follow[cite: 2230].
  - [cite_start]**Implement/PR:** The final execution and code review[cite: 2142, 2244].

---

## 2. Managing the "Instruction Budget"

[cite_start]A critical technical concept illustrated in the slides is that every LLM has an **instruction budget**[cite: 1110].

**The Performance Charts (Pages 51, 88):**

- **Accuracy vs. Instructions:** These slides show a series of graphs for various models (Gemini 2.5 Pro, GPT-4, Claude 3.7 Sonnet). [cite_start]The Y-axis represents **Accuracy (%)** and the X-axis is the **Number of Instructions**[cite: 1113, 1148].
- [cite_start]**The Trend:** As the number of instructions increases beyond **150-200**, accuracy across all models drops significantly [cite: 1111, 1983-2034]. [cite_start]This is why the "mega-prompt" /create_plan (with 85+ instructions) often failed[cite: 1102, 2167].
- [cite_start]**The Solution:** Splitting tasks into multiple prompts (e.g., changing from 85 instructions to 38) ensures the model remains in the "high accuracy" zone[cite: 2168, 2192].

---

## 3. Context Engineering and "The Smart Zone"

[cite_start]The slides explain how to organize an agent's memory to maintain intelligence[cite: 1141].

**The Context Diagram (Pages 28, 87):**

- [cite_start]**The Stack:** The image shows a vertical context window starting with **System Instructions**, **CLAUDE.md**, **Built-in Tools**, and **MCP Tools** [cite: 1480-1483, 1973-1976].
- [cite_start]**"The Smart Zone":** This is the upper 40% of the context window[cite: 1977]. [cite_start]The goal is to keep the core instructions and tools within this space to maintain reliability[cite: 1493, 1978].
- [cite_start]**"The Dumb Zone":** As user messages and massive files (like 1000-line plans) fill the bottom of the window, the model enters a "dumb zone" where it begins to lose track of instructions[cite: 1981].

---

## 4. Architectural Strategy: Horizontal vs. Vertical

[cite_start]The presentation provides a visual guide on how to structure implementation plans for better model performance[cite: 2221].

**The Layer Diagram (Pages 131, 133):**

- [cite_start]**Horizontal Plans:** The diagram shows the tech stack layers—**DB, services, api, frontend**—moving horizontally[cite: 2223, 2225].
- **Phasing:** Instead of building a whole feature at once, the diagram illustrates building in phases (Phase 1: DB, Phase 2: Services, etc.). [cite_start]This provides the model with "leverage" because a 200-line design is easier to manage than a 1000-line plan[cite: 2213, 2225].

---

## 5. The War on "Slop"

[cite_start]A recurring theme is the "War on Slop"—low-quality, AI-generated content that lacks authentic engineering craft [cite: 1869-1873].

**Key Takeaways from the Images:**

- [cite_start]**Leverage is not just speed:** 10x speed doesn't matter if the output is slop; engineers should shoot for **2-3x** speed with high quality[cite: 1887, 1888].
- [cite_start]**Read the Code:** Horthy explicitly corrects his previous advice, begging engineers to **read and own the code** rather than just reading the AI's plans [cite: 1126-1128, 1866].
- [cite_start]**Human-in-the-Loop:** The workflow is designed for "Mental Alignment" between the human and the agent, where artifacts (Questions, Research, Outlines) serve as the shared ground for the team[cite: 2210, 2236].
