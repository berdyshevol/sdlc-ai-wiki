# Spec-Driven Development with Coding Agents — DeepLearning.AI × JetBrains

**Course URL:** https://learn.deeplearning.ai/courses/spec-driven-development-with-coding-agents
**Companion repo:** https://github.com/https-deeplearning-ai/sc-spec-driven-development-files
**Instructor:** Paul Everett (Developer Advocate, JetBrains)
**Intro by:** Andrew Ng (DeepLearning.AI)
**Credits:** Konstantin Chaika and Zina Smirnova (JetBrains), Isabel Zaro (DeepLearning.AI)
**Partnership:** DeepLearning.AI × JetBrains
**Tooling shown:** WebStorm + Claude Code (but explicitly framed as tool-agnostic — works with VS Code, Zed, Cursor, Codex CLI, Gemini CLI, etc.)
**Note:** The transcript below is a concatenation of multiple course-video auto-transcripts that the user pasted. Timestamps restart at 0:00 per video segment. Lesson boundaries are inferred from content breaks.

---

## Lesson 1 — Introduction (Andrew Ng + Paul Everett)

Welcome to this course on Spec-Driven Development built in partnership with JetBrains. Spec-Driven Development is currently the best type of workflow for building serious applications with agentic coding assistance. Give your coding agent a markdown file or a long prompt, explaining exactly what to build and it implements that spec. Rather than writing code by hand, you focus on writing down the context that the agent doesn't already know.

I'm delighted that our instructor for this course is Paul Everett, who's developer advocate at JetBrains.

Thank you Andrew — and wait, I didn't know you wore spectacles. You're right, I don't actually need these. Okay, that's what I thought.

Anyway, Spec-Driven Development has three main benefits that you'll start to see right away.

**First, you can control large code changes with small changes to the spec.** One sentence like "use SQLite with Prisma ORM" might affect hundreds of lines of code. Change that to MongoDB for the same downstream amplification. This makes writing specs really efficient — far more so than writing code.

**Second, specs help eliminate context decay between sessions, preserving the non-negotiable.** Agents are stateless, so loading them with the highest quality context right when they boot up is important.

**And finally, specs improve your intent fidelity.** You define the problem, success criteria, constraints, and so on, and the agent can elaborate to create a fuller plan.

One way I often write a spec is by having a conversation with an agent like Claude Code or Gemini or ChatGPT Codex, to make the key architectural choices using my knowledge of how I want to make different trade-offs. Then have the agent summarize the key decisions in a markdown file. Writing a spec requires thinking, and this is hard work. You have to decide what product you want to build, what its features are, its technical architecture.

Without a spec, you'll be leaving these important decisions up to the whims of the coding agent, which might be okay if you want to move really fast and just roll the dice, but certainly leads to less maintainable code and sometimes pretty weird products. For example, I've seen teams working on a complex software product where there was no clear spec, and this led to many downstream headaches from these different coding agents under the direction of different developers, building quickly, building in contradictory ways.

Spec-Driven Development involves developing a **constitution** at the project level to define the immutable standards. Then iterating through **feature development loops**. These loops isolate each feature on its own branch with plan, implement, and verify steps that leave a clean slate between features and reduce headaches and context switching.

This same workflow supports both greenfield and brownfield projects. In greenfield projects, you start from scratch. You'll develop the constitution in a conversation with the agent. In Brownfield, existing code bases, you'll generate the project constitution based on the existing code base. In both cases, you'll then iterate through these feature development loops, managing versioning in small steps.

In this course, you'll also see how to write your own agent skills to automate your spec-driven workflow. You know, if you can accomplish what you need in just one short prompt, that's great. I'm definitely an advocate of lazy prompting when it works. But the great developers I know out there almost always will write detailed specs for projects with any significant complexity, because they have unique context and an opinion on what or how to build that'll be superior to letting the LLM, which is missing that context, pick randomly.

If a coding agent is going to go off and write code for 20 or 30 minutes, which may correspond to several hours of traditional developer work, you're often better off sitting down for three or four minutes and writing really clear instructions.

Many people have contributed to this course, including Konstantin Chaika and Zina Smirnova from JetBrains and Isabel Zaro from DeepLearning.AI. Let's go on to the next video and let's write some specs.

---

## Lesson 2 — Vibe Coding vs Spec-Driven Development

When you hear agentic coding, you might think Vibe coding. Let's compare the two and see how Spec-Driven Development gives better results by bringing back engineering.

**Vibe coding** gives quick results. You write a prompt describing what you want, like "create me a button," and hope for the best. Then you look at the result. That's a big button. It's kind of close, but off on some important things. So you point out the mistakes to the agent, it tries again and so on until you are satisfied. As a result, you will end up with a long dialogue with the agent, the history of which will not even be saved.

This approach works okay for a button, but it doesn't scale to a large ongoing project. While high-level prompts are fast, they lead to disposable code and mounting technical debt. **We need engineering.** A well-maintained specification that creates a permanent technical artifact.

**Spec-Driven Development is the professional response to the chaos of unsupervised AI generation.** It is a paradigm shift where the Specification, explaining the *what* and *why*, is decoupled from the Implementation, the *how*. With specs, we get a contract between the humans, but also with the agent. Your main task as the human now shifts: **learn how to convert your intentions into clear specifications.**

Spec-driven development with agentic coding assistance has three main benefits:

1. **Control large code changes with small spec changes.** A few sentences in the spec outlining the look and feel of the app might translate to hundreds of lines of CSS. This spec-driven approach reduces the cognitive overhead needed for working with these ultra-fast coding agents.

2. **Eliminate context decay.** As you work with your coding agent, its context window will fill up, often leading to more mistakes as the agent tries to cope with a full working memory. Specs persist between sessions and even agents, anchoring the agent to the core context needed to work in a code base and implement a feature.

3. **Improve intent fidelity** — the agent is more likely to produce code that matches your goals. That's because specs force you to define the problem, success criteria, constraints, user flows, and so on before the agent starts generating code.

Specs are a key differentiator between vibe coding (some slop) and engineering a viable software product. Whether you are starting a new project from scratch or want to implement the SDD approach into a project that has been running for years, specs help solve the drift and productivity problems.

As a comparison, think of **compilers**, which convert understandable source code into machine code. SDD guides the agent and prompts, converting specs into source code. Even better, the specs are in a human language, making it easy for stakeholders.

Spec-driven development has taken off recently as a solution to concerns about productivity. Multiple SDD projects, tools built around spec authoring, conference talks on capturing intent. This is all part of a broader push to bring engineering — lessons learned from the software development life cycle — to agentic coding.

**SDD is used with Coding Agents, not simple chatbots.** A chatbot can talk about code, but the chatbot doesn't have access to your project's code nor tools you have installed. It just responds to your prompts. Agents are different. They take your prompt, make a plan, and guide themselves to a result using reasoning along the way. Importantly, agents have access to your code base and your development tools.

In the SDD workflow, we treat these agents as **highly capable pair programmers**. They provide the technical knowledge and the speed, and you, the senior architect, provide the blueprints.

> As we move forward in this course, remember: **the agent is the muscle, but the SPEC is the brain.**

With practice, you ensure that the software produced is not just functional, but is aligned with your long-term goals.

---

## Lesson 3 — The SDD Workflow (Constitution + Feature Loop + Replanning)

Spec-driven development tells the agent how to build what you want — up front for the project, then for each feature, getting better as you go. With SDD, we help the agent with the best quality context. First with decisions about the project, then with details about each feature.

One key skill in SDD is **knowing the right level of detail**. If you treat your agent as a highly capable pair programmer, you'll often hit the right level. Lots of context about the Goals, mission, target audience and constraints — and less about the low-level decisions the agent can figure out on its own.

### The workflow

**First, we specify the Constitution.** What is the mission, the Tech stack, the Roadmap? A Constitution is just one way to formalize these project level details. Many developers use a top-level `agents.md` file for this purpose. But a project Constitution is **agent-agnostic and more structured**.

The Constitution captures the agreement on key decisions between the human and the agent, but also the agreement between the humans:

- **The mission** explains the *why*. This project's vision, audiences, scope, etc.
- **The tech stack** is for the engineering team — a common understanding of development and deployment technologies and constraints.
- **The Roadmap** is a living document with a sequence of phases, each implemented with their own feature spec process.

**Once the Constitution has been drafted, we work on each feature with a repeatable process.** First, plan the feature, implement it, and finally, validate the result.

**In between features, it's time for the Replanning phase.** Revise your Constitution, update the roadmap, even improve the process itself.

### The architect analogy

In the feature phase and the replanning phases, you steer the agent. Imagine that you are an architect and you give detailed drawings of a building to builders. Then it's up to them. Your role is to design, supervise the construction, then review and accept the results, or ask for changes. You'll want to **avoid telling the builders how to do their jobs and focus on providing the context they don't know.**

Spec-Driven Development gets you from thinking at the start to delivering at the finish. Best of all, it keeps you improving from there.

---

## Lesson 3a — Course Setup (reading item + optional video)

### Course Setup

Before the next video, take a moment to get your environment ready so you can follow along with the hands-on lessons.

**1. Get the course repo**

Repo: `https-deeplearning-ai/sc-spec-driven-development-files`

```bash
git clone https://github.com/https-deeplearning-ai/sc-spec-driven-development-files.git
```

If you want to follow along with the course, start with the files in `Lesson_04/` and follow along from there. Every subsequent video builds directly on that starting point, so if you copy Lesson 4 into your own working directory once, you can keep going video-by-video without touching the repo again.

```bash
cp -r Lesson_04/ my-agentclinic/
cd my-agentclinic
npm install
```

If you'd rather jump in partway through — say, straight into Lesson 7 — each `Lesson_NN/` folder is a self-contained snapshot of the project as it should look at the start of that lesson.

**2. Install an IDE** — The course is recorded in WebStorm, but any editor or IDE works — VS Code, Zed, Cursor, Neovim. SDD isn't tied to a specific tool.

**3. Set up a coding agent** — The course uses Claude Code in the terminal inside the IDE, but Codex CLI, Cursor's agent, Gemini CLI, a local model in Zed — all of them work with the SDD workflow. **The specs travel with you when you switch tools.**

### Optional Setup Video

Spec-Driven Development is a best practice that isn't tied to any specific IDE or coding agent. So you can choose the setup you're already using or the same one you'll see in this course. VS Code with the Codex CLI, Zed editor with a local model — all great for spec-driven development.

Since we are planning to develop a web application, this course will use the **WebStorm IDE with Claude Code as a coding agent**. Let's open up WebStorm and start a brand new project named **Agent Clinic**. This will be a TypeScript project with a Git repository to keep close track of versioning your code and specs.

Although many IDEs, including WebStorm, offer a chat panel, we know there's a lot of diversity in how you interact with your coding agents. In spec-driven development with agents, it's important to keep close track of versioning your code.

Let's say we want to create an initial commit using the agent. Every time it needs to execute a command, it will ask you for the confirmation unless you start Claude Code in an unsafe mode. **Pay close attention to what Claude Code asks you to do. The ultimate responsibility for the code is yours.**

---

## Lesson 4 — Writing the Constitution (Mission, Tech Stack, Roadmap)

You need to tell your agent about your project — the mission, audience, and other decisions. In this lesson, we'll work together with the agent to write the Constitution.

What really is your project? Say you're working on a new web app for your company. What's the core idea behind its development? How does it fit within your company's preferred tech stack? What features are planned? These three foundational principles form the Constitution, a global set of high-level requirements that will guide future feature development and explain the project's shape to stakeholders.

We write it **in a conversation with the agent.** You'll be surprised at the great questions it will ask — architecture patterns you hadn't considered, external packages that already do the work, or tradeoffs (for example, speed versus data fidelity).

The mission, tech stack, and roadmap aren't just properties of a Greenfield project you're starting from scratch. Existing codebases use these three pillars too.

### The example project: AgentClinic

We are writing **AgentClinic**, a place for AI agents to get relief from their humans. AgentClinic is a fun parody of the popular learning project Pet Clinic. Coding agents are doing a lot of work — it's stressful. Hallucinations, context rot, memory issues and co-worker sub-agent coordination all take a toll on agent health. Let's build a clinic where they can get help with their issues.

It's a full-stack web app with a Next.js back end and a React front end. The app allows you to manage appointments, ailments like hallucination, and treatments like a context infusion.

### The long spec example

This document contains a lot of information that the average Claude code instance isn't going to know:

- Lines 37–43 — real problems we're trying to solve. Agents can check themselves in via API and their issues persist over time. So we can see how effective treatments are.
- Line 57 — The visit lifecycle is mapped out, including a TRIAGE step to route them to the right place and a FOLLOW-UP with three possible states.
- Line 379 — An ailment catalog plus the ability to have custom ailments. Ailments have codes and severity levels, which can be modified if the agent handles medical or legal data.
- Line 430 — Auto-create a custom ailment when symptoms don't match any existing ailment above a 0.6 similarity threshold.
- Line 581 — The exact algorithm used to update a treatment's effectiveness.

Let's chat with the agent to see if there's anything that could be cleared up. The agent says there's a threshold inconsistency in the diagnosis flow. Let's scroll to line 143 and check it out. It looks like three is actually the correct option. If a diagnosis is between 0.4 and 0.6 confidence, then it's included but flagged as uncertain.

This is a great sign. There's no issue with the spec — we're just confirming our understanding with the agent.

For this question, let's just say having an unprotected dashboard is fine because we expect to deploy this privately in a secure environment to our company. For the LLM, let's leave that configurable because we don't know how soon a new model will be released. For archiving, we're not sure about this behavior right now, so let's choose the first option, soft-delete, which gives us the most flexibility later.

### The lightweight prompt

To generate the more lightweight documents, let's chat with the agent. First, we provide our project description to the agent and tell it that our stakeholders gave their input in README.md, which we added to the repo.

In the important note, we directly mention Claude Code's **AskUserQuestion tool**. This tool is totally optional, but we just like the way it looks in the interface. Also, for the project's constitution, tell the agent to work with you on a mission, tech stack, and roadmap.

> Spec-driven development works best with a **human-in-the-loop approach** where you review small changes. So tell the agent to organize the roadmap in small steps.

As we work together, the agent asks questions:

- **Tone for the mission?** → playful.
- **Tech stack backend language?** → TypeScript (our engineers are used to TypeScript on the back end).
- **Roadmap granularity?** → first (smallest) option.

The first question says, "what tone should the mission.md take?" I'll choose, you guessed it, playful. That covers the mission. Now some questions for the tech stack. Our engineers are used to TypeScript on the back end, so let's add that to the requirements. Next for our roadmap — it asks how granular it should be. I'll choose the first option.

We finished the initial interview. Let's choose submit answers. The agent will ask you for write permissions. This keeps changes under your control. If you are comfortable with the security tradeoffs, you can select the option to approve all instances of a particular command for this session.

Now we're done and we have three files in the specs directory: **`mission.md`, `tech-stack.md`, `roadmap.md`**. It's human-in-the-loop time. Let's review.

For example, the mission left out a target audience. That's reasonable — how could the agent know your business? **Instead of editing directly, let's continue the conversation.** To keep all artifacts consistent, it is better practice to ask the agent to make changes to them. Manually, and you might miss updating related documents.

We want to use **SQLite** for this project since this is a quick prototype. We didn't mention it, but the agent figured it out in recommendations. It's now part of our tech stack.

Do one final review. It's important to get everything right up front. Let's commit the Constitution so it will be a living document for the project.

AgentClinic now has a constitution — mission, roadmap, tech stack — to guide our project. We're ready to tackle our first feature.

---

## Lesson 5 — Feature Specification (Hello Hono — the first feature)

We now have a roadmap with features. But how do we build them? With specs of course, starting with the first roadmap feature.

Here's our phase one feature: **Hello Hono.** But it's too early to start coding. We need to discuss the spec and clarify all the details. A good plan outlines the approach, the sequence of work, and how to validate success.

### Start with fresh agent context

The agent can get what it needs from the official source, the constitution. We will work on this feature in a **separate branch**, which we will indicate to the agent.

Our prompt will help start a conversation with the agent about the feature spec, a plan for tasks, collect requirements, and a scorecard for validation. The agent will ask you to make key decisions. Pay attention to potential conflicts or problems. **You don't have to agree with the solutions proposed by the agent. Make sure to clarify anything that bothers you.**

Decisions made here:

- Phase 1 scope: keep it exactly as written.
- Requirements: pin the Hono version and enforce strict TypeScript.
- Confirmation: manual curl looks good.

That was fast — must have been a nano. Work is done and the ball is back on our side for reviewing the feature spec created by the agent.

### Three files per feature spec

The agent produces three files in a dated `specs/YYYY-MM-DD-<feature-name>/` directory:

- **`plan.md`** — numbered task groups (e.g., Data → Components → Page & Route → Navigation → Tests)
- **`requirements.md`** — Scope / Decisions / Context
- **`validation.md`** — Automated (typecheck, tests, assertions), Manual walkthrough, tone check, definition of done

For example, we would like a nice looking placeholder home page in this first feature spec. We make the change via the agent.

Next, the requirements — these were also updated to reflect the homepage update. This is the right place to indicate any important technical needs or constraints. **Don't speed through this, but don't state minor technical details like variable names here. We want to control the process but not oversteer the agent.**

Last, the validation — make sure the agent can check that it got it right. Again, these were updated for the homepage.

We're done with the feature spec. Let's create a commit in the IDE. Nice — we formulated a feature spec strategy, made a feature branch, interviewed with the agent about what the feature should do, put the results in markdown documents, reviewed these spec files, committed.

> The changes you make here in the specs will expand downstream into hundreds of lines of code. So **time spent here is well spent.**

---

## Lesson 6 — Feature Implementation

We're working on the plan for the first feature in the project roadmap. We finished the feature spec. Let's do the full implementation of this feature.

To start your implementation, you'll want to **clear out your context with a `/clear` command.** Let's go back to the agent and enter a prompt to implement all the task groups.

**Sometimes you might choose to do task groups one at a time for even smaller steps and commits.** This technique is especially helpful for areas where small mistakes can compound later, like in security or database management.

While Claude is running, you can observe the changes it displays in the console to see its progress in real time. Afterwards, we can watch for the final changes in the commit window and visit the changes. This gives us an early jump on reviewing the work.

> This is the key role of the developer in such a paradigm: to **act as an architect or supervisor** and ensure that the agent is provided with a clear contract.

We can also see the summary of what was done. As you can see, the agent provides extra details on the work performed for each of the task groups. Now, let's go to the `package.json` file and run the app. The server starts in the console. The browser shows the result of this feature spec. Not much — we said nano — but it's a good feeling to see pixels on the screen.

We just implemented a feature. The agent did its validation. In the next lesson, we'll do ours.

---

## Lesson 7 — Feature Validation (Human-in-the-Loop)

It's nice to have a feature ready, but **don't merge yet.** In this last feature step, we collaborate with the agent to review the work. Fortunately, programmers have good tools for this validation task. After all, programmers have long spent several hours per week on code review.

### Review high-level, not line-level

Start with the commit view. Let's go through the changes. **Focus your review on high-level concerns like whether the features work and reflect the spec, rather than details like which CSS classes were implemented.**

For example, the `Home.tsx` is minimal. Nano really meant nano. We want a layout component with clear landmarks for header, main, and footer, but do these as sub-components. And create a CSS file.

As it turns out, this mistake in the code flowed from a mistake in the plan. We didn't ask for this. Let's ask the agent to do the fix, **thus correcting both spec and implementation.**

This process that consists of the agent generating something and us verifying it is known as the **human in the loop.**

### Cognitive debt

Because agents are so fast at writing code, software developers have lately been talking about **cognitive debt** — the mental load of tracking what your code is doing and how it has evolved. That is why in order for this process to be fast and easy to control, and to reduce cognitive debt, **the changes should be manageable.**

The agent is making our changes, but also validating that these changes didn't break anything.

### Drift-aware refactors

It looks like the three subcomponents were just put in the same file, but that doesn't follow conventions. Let's put these in their own files using the IDE move tool. These kinds of changes are easy in editors and we've always been good at this. No need for an agent, right? Let's just do it.

**Not so fast.** This can lead to **drift** where other artifacts (specs, readmes) get out of sync. Let's ask the agent to fix any mentions and to make sure this doesn't waste some time later.

All changes are done. Did we break something? Tests would help, but the agent didn't install our testing package. Since this is needed for all features, we'll cover it in the next lesson.

Now we're ready to mark this work as complete and merge our results. Notice that part of the constitution was updated alongside the feature in this branch. How to handle versioning of the specs and how to associate which specs created which code changes is **an evolving topic in the community.** The change to the roadmap is small — just checking off a step in the roadmap — so it's okay to keep these updates on the same branch. If the overall constitution update is more complicated, it might be better to do this in a separate branch.

We just used Spec-Driven Development to develop and validate our first feature. But wait — shouldn't we take another look at the project's broader scope?

---

## Lesson 8 — Project Replanning (Including Skill Creation)

We successfully implemented the first feature. Can't wait to do it again and again. **Don't rush into it. Take a step back and reflect with some replanning. You have to run slow to run fast.**

### Adding a testing framework

We have a workflow step called validation. Tests are good for validation, but we didn't give the agent all our testing preferences. Let's make a **replanning branch** to update the tech stack in our constitution.

As you saw in the previous video, spec versioning is an evolving topic. **The constitution is a living document.** It's good practice to make updates to it in its own separate branch, so you can keep track of which versions of it produced which code.

We'll use a prompt to state our policy. It looks like the agent updated the `package.json` just to have a script, no dependency. Something to note for later when we do run tests. This change to add a testing framework applies to future code. But let's tell the agent to update existing feature specs and implementation based on this constitution change.

The agent set up this testing change, but didn't write the tests themselves. Let's tell the agent to write some new tests. With this setup, we can run tests conveniently in our editor. Let's run under the debugger to give us a chance to step through code execution as part of the human-in-the-loop.

### Responsive design (product update during replanning)

Sometimes we realize we want to do something differently in the product plan. For example, after implementing the first feature, we got an update from the product manager: **because 40% of our users are on mobile, we want to emphasize a responsive design.**

Let's go to the agent. Tell the agent we want responsive design and to correct the product specs and feature specs as well as any code.

Since we're so early on in development, this update is a small change, so it makes sense to directly implement it during replanning. **But if the new work is big, it's better to schedule it on the roadmap as its own feature phase, instead of just doing it in replanning. Use your judgment.**

Remember, we want the specs to capture decisions, not just the code. We want to try to keep both in sync to help team communication.

### Revisiting the roadmap

While this first part of replanning is working, let's step back and do some project housekeeping. For example, let's revisit the project roadmap and look at the next task. Does it still make sense?

Looking through the roadmap, it looks like features two, three, four, and five kind of hang together. Let's update the roadmap to tackle those in one step.

### Creating a changelog skill

Replanning can also be about **improving your spec-driven development workflow, across projects, across your organization.** For example, maybe you have a few non-technical stakeholders that want to monitor the project's progress. You'd like it to update a changelog on each merge to main.

> Most AI coding agents support **skills** — a package of instructions and resources providing the agent new capabilities and expertise. Skills are great for **definable, repeatable workflows that require context specific to your project or organization.** A skill would be great for implementing a changelog update.

You could write this skill by hand, but **many agents actually have skills that help you write a skill.** Let's use the agent to help us write and maintain a changelog skill.

One thing for us to consider: is this skill unique to this project? Or should it be a standard part of all projects? This is a style choice and you'll gain better understanding as you use it.

> You'll learn to automate your SDD workflow with skills. For example, your validation step might include updating the readme, linting, formatting, test writing, and other quality checks. You can work with your agent to package those into a **validation skill**. Repeatable process, less manual work.

The agent finished. It chose to create the skill in the **global skills area** — usable across all projects. Also, Claude Code used the new skill to generate a CHANGELOG in this project. CHANGELOGs are how you talk to your stakeholders, including the agent.

Now that most of your work as a developer is in planning and validation, rather than implementing, **make time between features to replan.**

---

## Lesson 9 — Second Feature Phase (Agents & Ailments) + AI Fatigue

We have an improved constitution and an improved workflow. We're getting better. But before moving on to the next roadmap feature, let's tackle some strategies to deal with a common pain point: **AI fatigue.**

Agents can generate a lot of code with a lot of changes. This massive amount of code makes the human-in-the-loop validation exhausting — so much to review.

### Clean division between features

To fight this confusion, make sure you have a **clean division between each feature phase.** We should start each feature in the right flow state:

- Do I have unfinished work?
- Did I merge the last feature branch to main?
- Is the next roadmap item the right thing to do?
- Did I clear the agent's context to ensure the specs capture the intent instead of memory snapshots? And to let it focus its limited context budget on the next work?

**Take a moment to make a good start to help yourself finish.**

### Feature spec — Agents & Ailments

As before, the agent asks good questions:

- Keep all these features in one phase? → yes (decided in the previous lesson)
- Migrations? → plain SQL
- Validation? → options 1, 2, and 3

When the agent drafts the spec, we can see some of its choices. The agent's reasoning process is useful to watch. If you're using an agent with verbose mode, that could give you even more insight into its intermediate ideas.

Small change to capture our intent: we want to use **PicoCSS** as our CSS framework. Next, we review the three files in the feature spec, starting with the requirements. Let's ask the agent to change the requirements to make sure any other files reflect the change. When the work is finished, let's commit the feature spec. This time, we'll let the agent come up with the message.

> The division between the planning phase and the feature phase helps us to not overflow context, hours, and agents. **If the feature seems too big to implement all at once, ask the agent to implement part of the feature plan first.** This will keep the size of the changes manageable.

### Implementation review (high-level only)

Our agent has implemented the phase two feature. We watched the agent's progress, so we have a rough idea of what was done. But that's not enough — **slow down, do some thinking.**

Everybody has their own style on how much to review the agent's results. **To play to the agent's strengths and reduce AI fatigue, stick to higher level requirements. Avoid nitpicking stuff like variable names. Just make sure it creates code that you can commit under your name.**

For example, it used inline type information for the props. We'd like the prop definition in a standalone TypeScript type. Let's tell the agent to fix this everywhere in the code.

> You probably didn't include this decision in your spec. Remember, **an omission such as extracted prop types isn't a failure. You are evolving the spec as you discover new details and capturing that leads to better future results.**

### Sub-agents for deep review

Sometimes you need to validate that you weren't lied to. **Tell the agent to spawn several sub-agents to do a deep review of the entire project with this feature change.**

This deep review gives the agent more space to think about the changes. And using sub-agents **preserves the main agent's context window, rather than polluting it.** These sub-agents will come back with a number of issues and recommendations.

The agent goes off, does a bunch of fixes, runs tests, and gets our project into a good state. Keep this in your tool chest — **the agent can usually find important issues during a second look.**

Once we are finished with our validation, our feature is complete. It's time to commit our feature. As our last step on this feature, let's use the **changelog skill** that we made in the previous lesson.

This clean break between features helps manage AI fatigue. Now you can take a break for some coffee.

---

## Lesson 10 — MVP (Implementing the Rest of the Roadmap)

We made a lot of progress. Two features implemented with our spec workflow. But management just asked, of course, for an MVP. Have we made enough progress to do an experiment?

Let's do a variation of our standard feature spec prompt. This time we'll tell it to **implement the rest of the roadmap** and give some guidance about existing feature specs.

> In general, you should only implement such a large chunk if you feel confident in the quality of your constitution and spec. The better the context you provide your agent, the more confident you can be in getting a result aligned with your intentions. And you should be sure that you can handle review and validation.

But since we've taken this risk now, let's view the MVP as an **extreme test of our constitution and completed feature specs.** If we now get something different from what we wanted, it means we need to very responsibly carry out another replanning phase to eliminate whatever led the agent astray.

A lot of spec files start as a back-and-forth conversation with an agent. Finished with the interview and we selected Submit Answers. Let's write the MVP specs to disk.

It's always good to review the specs. You'll often notice incorrect assumptions the agent made to fill the gaps. Let's give a quick look at the plan, the requirements, and the validation. As always, we like to work in small steps with frequent commits.

The agent now does a lot of work. Once it's finished, it's showtime. Each section now has much more — driven by sample data queried from the database.

At this point, usually we would validate the code results, but this is an MVP. Let's **ask the agent to validate the specs.** As it turns out, this was useful — the agent showed places where the MVP found holes in our planning. We can share this evaluation with the stakeholders for their MVP review, then merge or archive the branch.

Our spec-driven workflow succeeded. After a constitution and two features, the MVP produced a useful demo, thanks to our guidance.

Of course, not all software projects involve building an MVP. Many projects are so-called **brownfield** — they start from an existing code base. Next, let's see how to introduce this workflow to legacy projects.

---

## Lesson 11 — Brownfield / Legacy Support

People say spec-driven development and even AI are only good for greenfield projects. **But SDD is also good for existing legacy projects.**

To make it easy, we'll start with a project you already know — the AgentClinic MVP. We'll make it a "legacy" by starting on main without the `specs/` folder in a new Claude Code session in a different project directory.

We have some project background in the `README.md` file with some open work listed in `TODO.md`. Your legacy project might have full product plans in issue trackers, spreadsheets, Word documents, etc.

Remember our workflow? We'll start with the constitution step. We'll use almost the same prompt from Lesson 4. **This time, we'll tell it to look for roadmap items in existing artifacts** — in this case, a TODO file.

> Remember, the agent will discover and in a sense **reverse engineer the SDD artifacts from the existing code base.** The constitution will help align future code changes made by the agent with what past devs have already created.

You can always add more context if you have it. For example, you might have been dropped into this project in order to improve its efficiency while implementing highly requested features. **The process is the same, but the conversation might be richer as the agent has more artifacts** — code, commits, documents, etc.

You'll see a lot of tool calls here as the agent explores the code base.

---

*[Transcript content beyond Lesson 11 was truncated by the user's message — the wiki page should note Lessons 12 (Build Your Own Workflow) and 13 (Agent Replaceability) are present in the companion repo but were not in the transcript provided.]*

---

## Companion repo structure (verified via `gh api`)

```
sc-spec-driven-development-files/
├── README.md                     # Lesson-by-lesson overview
├── Lesson_04/                    # Empty scaffold (package.json, tsconfig.json, src/index.ts)
├── Lesson_05/                    # Constitution in place (mission.md, tech-stack.md, roadmap.md)
├── Lesson_06/                    # + Phase 1 feature spec (plan.md, requirements.md, validation.md)
├── Lesson_07/                    # Phase 1 "Hello Hono" fully implemented with layout
├── Lesson_08/                    # Phase 1 merged, ready for replanning
├── Lesson_09/                    # Replanning complete (testing, responsive, changelog skill)
├── Lesson_10/                    # Phase 2 "Agents & Ailments" merged, MVP-ready
├── Lesson_11/                    # MVP fully implemented, ready for legacy SDD
├── Lesson_12/                    # Rebuilt legacy constitution + Feedback Form feature
├── Lesson_13/                    # feature-spec skill created, backlog/ research notes
├── example_specs/
│   ├── AgentClinic-Mission.md
│   └── AgentClinic-Tech-Stack.md
└── skills/
    ├── changelog/
    │   ├── SKILL.md
    │   └── scripts/
    └── feature-spec/
        └── SKILL.md
```

## Notable files pulled from the repo

### `Lesson_08/specs/mission.md` (excerpt)

> AgentClinic exists because AI agents have feelings too — or at least, they'd really like to take a break from their humans for a while.
>
> ## What We Do
> AgentClinic is a full-service wellness platform for AI agents. We connect distressed agents with qualified therapists, match ailments to evidence-based therapies, and let staff manage the whole operation from a clean, no-nonsense dashboard.
>
> ## Target Audience
> - **Course students** learning spec-driven development with AI coding agents
> - **Conference booth developers** giving AI coding demos

### `Lesson_08/specs/roadmap.md` (structure)

Ten short phases, each a "shippable slice of work, independently reviewable and testable":

1. Hello Hono ✅
2. Base Layout
3. Agent List
4. Agent Detail
5. Ailments Catalog
6. Therapies Catalog
7. Appointment Booking
8. Staff Dashboard
9. Polish & Accessibility
10. Hardening

### `skills/feature-spec/SKILL.md` (excerpt)

```
---
name: feature-spec
description: Kicks off a new feature by finding the next incomplete phase in
  specs/roadmap.md, creating a git branch, interviewing the user about
  scope/decisions/context, and writing a dated spec directory under specs/
  containing plan.md, requirements.md, and validation.md.
---

### 3. Interview the user — BEFORE writing any files

Use `AskUserQuestion` with exactly **3 questions in one call**:

| Header    | Question focus                                                  |
|-----------|-----------------------------------------------------------------|
| Scope     | What the feature collects, exposes, or does                     |
| Decisions | Key implementation choices — storage, visibility, validation    |
| Context   | Tone, constraints, or anything shaping the spec                 |

Do **not** write any files until the user has answered all three questions.

### 5. Create the spec directory
Name: specs/YYYY-MM-DD-<feature-name>/ using today's date.
```
