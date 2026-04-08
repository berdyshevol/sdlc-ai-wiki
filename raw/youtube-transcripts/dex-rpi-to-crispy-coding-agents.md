# Everything We Got Wrong About RPI (Research, Plan, Implement) — Dex (HumanLayer)

**Video:** https://youtu.be/YwZR6tc7qYg
**Speaker:** Dex (HumanLayer)
**Topic:** Evolution from RPI to CRISPY methodology for coding agents

---

## Transcript

**[Intro / Host]**

All right. Before I bring up Dex, I gotta say I met James. And James — Yeah. Can you stand up real fast? James told me this morning that he is going — We can't see the QR code. You got to hit it up. He's going to be having dinner tonight and everybody's invited. So, if you want to go, just scan that QR code real fast and go hang out with James. That's awesome. And that's what we're going for here. That is great.

Yeah, you rock. Yeah, that's — I like it. I like it, too. Okay, so I'm gonna bring up Dex. Uh earlier somebody said we need to have a mustache competition. I don't think that's going to happen, but I will say that he gave us 200 slides that he's about to present.

**Dex:** Whoa, whoa. 158.

**Host:** 158. We're going to keep him honest on the timing. All right, so let it start now everybody.

---

**[Dex's Talk Begins]**

Let's do it. What's up everybody? Uh I am Dex. Uh this is a talk with a very long title that I'm not going to read because we're on the clock now.

I have been talking about coding agents for quite a while. Basically since like August. We did a long talk in November. There's this methodology that we've been talking about a lot called **Research Plan Implement**. A lot of upvotes on Hacker News. There's probably 10,000 people who have gone to our open source and grabbed our prompts and are using them internally from small startups up to the enterprise.

It all started with this guy. Has anyone seen this talk? Yes. Okay. So Eigor went in and he said like okay cool we're using a lot of tokens, we're spending a lot of money to get AI developer productivity. But what he found was that it actually tends to lead to a lot of rework. Like you are shipping 50% more but half of that is just cleaning up the slop from last week. And the other thing they found — and these are last year's numbers, so this does not account for Opus 4.5 — so I would inflate this a little bit, but like it's great for low complexity greenfield tasks, not great for high complexity brownfield tasks.

### What We Got Wrong About RPI

So I could give you a talk about RPI and why it's great. But that would be boring. And there's other talks, so if you haven't seen them, go watch them. It'll give more context. But I'm going to tell you **everything we got wrong about RPI** today.

We thought we had this AI thing figured out. I am humble enough to admit when I was wrong. So we got a couple things wrong:

1. **I don't think it's okay to not read the code.**
2. **You shouldn't read really long plan files** — those two are related.
3. **No, Claude should not be allowed to** — if you're writing production code that is used by users and you're going to get paged at 3 a.m. if it's broken — **no slop.** This is the year 2026. No more slop.

We did get a couple things right:
- **There is no magic prompt.**
- **Do not outsource the thinking.** You the engineer are an important part of this process.
- **Seek leverage.** There's a lot of code being written. Find ways to make sure it's correct without having to read all of it and resteer after the fact.

### The "Magic Words" Problem

So, lots of people have heard of Research Plan Implement. Has anyone actually run this Claude command? Research codebase? Okay, cool. Leave your hand up if you've run it like this — "Tell me how this system works." Has anyone run it like, "Hey, I want to build this thing. Go do the research." Okay. Or maybe go fetch a ticket or something. What about the create plan prompt? A couple hands. How many of you run it like that — "Hey, we got to go build this thing." Yes. Has anyone run it like this — **"Work back and forth with me starting with your open questions and outline before writing the plan."**

Okay. Some of you found out about the magic words. A lot of people didn't though. We'll get into why that's a problem.

### Why People Weren't Getting Good Results

Since October we've basically worked with thousands of engineers from tiny startups all the way up to Fortune 500s. And we would find over and over again we would give these tools to an expert and they would get great results. They would go sit and talk to Claude for 70 hours a week and they would start shipping like crazy. And then they would go give it to their team and the results were not always so good.

**Problem 1: Bad Research.** We talked about this in November — you would pick a zone of your codebase, say "We're going to build something over here," and then you would launch a coding agent session to send these sub-agents through these deep vertical slices through the codebase for just the context — compressed context about what is the thing we're about to go build. And we said keep things objective, discourage opinions, don't actually put any implementation details in there. You just want to compress the truth. What is true about how the code works today?

A skilled engineer was really good at taking "here's my ticket" and writing questions that would cause the model to go touch all the parts of the codebase that matter. But a lot of people would just say, "Hey, research codebase. Here's what I'm building." The problem is that **good research is all facts. But if you tell the model what you're building, then you get opinions.** And we don't want opinions — comes back to this thing that Jake from Netflix came up with: **do not outsource the thinking.**

**Problem 2: Bad Plans.** There were these steps built into this planning prompt — a single giant monolithic thing with 85 or more instructions. It had steps like "present design options to the user, get feedback on the structure before you actually go write the plan."

A good planning session would look like: you load the skill, it looks at your ticket, loads your research doc, launches a bunch of sub-agents to find things that are true about the codebase, and then the agent would come and ask questions. The user would pick options, eventually it would say "here's the order we're going to do the things, what do you think?" And the user could say "we need to add a testing step up front, and I want to swap phases three and four."

But for about 50% of people — maybe more — if you didn't prompt it with "work back and forth with me," or Opus was just feeling dumb for that particular hour, it would just take the stuff and immediately go write the plan out. It would be like "cool, I wrote the plan, didn't ask me any questions, made all the decisions for me." Yikes.

People would literally say "well, you have to say the magic words." And I found myself in workshops full of enterprise engineers saying "Well, guys, guys, guys, yeah, here's the software, but don't forget to say the magic words." It was, quite frankly, embarrassing. But if you said "work back and forth with me starting with your open questions and outline before writing the plan," then the agent would ask you the questions.

**This isn't the user's fault. If you built a tool that requires hours and hours of training and reps to get good results from, go fix the tool.**

### The Instruction Budget

**You have an instruction budget.** My co-founder Kyle wrote this really good blog post that cited this archive paper which said that frontier LLMs could only follow about **150 to 200 instructions** with good consistency. Anything more than that and it's kind of half-attending to all of them and you're rolling the dice. So if you have a prompt with 85 instructions and your CLAUDE.md and your system prompt and your tools and your MCP — yeah, you're not likely to get full adherence to the workflow.

### Don't Read the Plans, Read the Code

We advocated for reading the plans that were output. I was on stage in November telling people you have to read the plan otherwise it won't work. Some people even would PR their plans and code review them together. But a thousand-line plan tends to be about a thousand lines of code within 10% or so. And plans can have surprises. You would review the plan and then write the code and it would be different.

**The new advice: don't read the plans. Please read the code.** It's the same amount of work — look for leverage elsewhere.

You may say, "Hey, Dex, in August you said don't read the code. You said the plans are enough." I was wrong. I am humble enough to admit when I was wrong. Please read the code. We tried not reading the code for like six months. It did not end well. We had to rip out and replace large parts of that system.

You may say "but other people don't read the code!" — Beads, 300,000 lines and counting, no one's read that code allegedly. OpenClaw, Pete's like "I know the structure and the pieces and how they fit together, but I don't read every line of every PR." These are OSS projects. They don't charge money. They are very cool projects. I am humbled by the accomplishments of the maintainers. But the stakes are different than if you're working in a regulated industry shipping production SaaS code.

**If you have people who depend on your code, please I'm begging you please read it.** We have a profession to uphold. 2026 is supposed to be the year of no more slop. This is why I'm a little mid on agent swarms and the whole "gas town" thing — because you still need to be able to ensure quality and going 10 times faster doesn't matter if you're going to throw it all away in 6 months.

**Shoot for 2 to 3x.** That's actually another talk of how you measure this and how you actually get there and maintain a near-human level of quality.

### Goals: Better Research, Better Plans, Better Leverage

- **High leverage planning**
- **Do not outsource the thinking**
- **Read and own the code**
- **Avoid magic words**

### Better Research

The fix: we just hide the ticket from the context window that's doing research, and we do it deterministically. Basically you have one context window to generate questions and then a fresh context window with no knowledge of what we're building to go make your research doc. This is pretty trivial if you're familiar with the concept of query planning.

### Context Engineering

I wrote this paper called 12 Factor Agents which was allegedly the first time anyone was talking a lot about context engineering. There's two ways to read context engineering — most people jumped in with "put more information" (RAG pipelines etc). I actually think the more interesting read is **better instructions and simpler tasks and smaller context windows.**

We talked about the **"dumb zone"** — around 40% of context window usage on average, you hit this point where you have degrading results. The less of the context window you use, the better results you will get. Our friends at Databricks were talking about having too many MCPs — the whole context window is full of instructions about how to use tools you don't care about, and by the time you're writing code the model can't follow your instructions well.

**Don't use prompts for control flow if you can use control flow for control flow.** The if statement is really powerful and LLMs are really good at classifying things.

### From 85 Instructions to Under 40

Before it was Research, Plan, Implement. Now it's: **Questions → Research → Design → Structure → Plan → Work → Implement → PR.** We split the planning into a design discussion and outline and a plan. Before it was 85 instructions, now they're all less than 40.

We told everybody "don't just call tools in a loop, do context engineering and build workflows and graphs and micro agents." Then we turned around in August and wrote this giant monolithic prompt. So we figured it was time to actually go drink our own Kool-Aid. **Mind your instruction budget.**

### Better Leverage: The Design Discussion

**Where are we going?** The design discussion has:
- Current state and desired end state
- Patterns to follow (this is your chance to correct the agent — "Nope, that's not how we do atomic SQL updates. That engineer doesn't work here anymore.")
- Resolved design decisions
- Open questions

It's like taking Claude Code plan mode and the ask-user-question tool and brain-dumping it all to a single document. Matt PCO has this idea he calls the "design concept" — the shared understanding between you and the agent of what's being built and how. We put it in a **200-line markdown artifact.**

**Human-agent alignment:** You're forcing the agent to brain-dump all the things it found, all the things it wants to do, all the things it thinks you want, and ask you questions about things it doesn't know. So you can do brain surgery on the agent before you proceed downstream. Give the agent every single opportunity to show you what it's wrong about before you go write 2,000 lines of code. **200 lines instead of 1,000 — a lot more leverage.**

### Better Leverage: The Structure Outline

If design is "where are we going," the structure outline is **"how do we get there."** Think of it as: architecture review → sprint planning → task breakdown.

We take our design, the ticket, and the research, build a new context window, and create the structure outline — a high-level overview of the phases, not the exact code, but what order we're going to do the changes and how we're going to test along the way.

**Plan = eight pages. Structure outline = two-ish pages.** Much shorter. If the plan is the implementation, **the outline is the C header files** — just the signatures and new types, enough for you to see what the agent is thinking and correct it if it's wrong.

**Vertical vs Horizontal Plans:** Models love to write horizontal plans — "we're going to do all the database, then all the services, then all the API, then all the front end." Before you know it, you're on the other side of 1,200 lines of code and it's not working. **Vertical plans** give you checkpoints where you can see if it's working and pause to fix it before continuing.

### Better Leverage: Team Alignment

The most important part of this leverage is not just about you and the agent — if you're working with a team of engineers, these design discussions and structure outlines are really good for review. I'm not the code owner of most of our code at HumanLayer — my co-founder is. I send him my design discussions on purpose. Any of my bad decisions are headed off on a 200-line doc before I've gone and written the code and gotten attached to it.

**Time savings:** Before AI, a two-day feature is still a two-day feature even with AI coding, because you still have to align with your team, get code review, fix stuff. But if you use AI to help with your planning and alignment, then your code review and rework is also much shorter because you already know what's coming.

### Putting It All Together: CRISPY

Five stages of research and planning: **Questions → Research → Design → Structure → Plan → Worktree → Implement → PR.**

That didn't make a very good acronym, so we just picked the ones we liked and we're calling this **CRISPY**. RPI to CRISPY.

### What's Next

- Three steps was already a lot for some people to learn and now there are seven — need to make it easier.
- How do you measure the impact of doing this in engineering teams?
- If you're a central platform team rolling out changes to everybody in your org, how do you make these prompts better without breaking somebody's workflow?

If you want to help us — if you're in San Francisco and you're working on critical systems and you want to figure out how to get coding agents to do more — let's chat. We're also hiring. Founders@humanlayer.dev. We're building an IDE that orchestrates this stuff for you.

---

## Q&A

**Q: About reading the code — it's not scalable, right? Are you going to be saying the same thing in six months?**

**Dex:** Six months ago, I said not to read it. And I think everyone who is saying "don't read the code" now is going to be in six months being like, "Yeah, we had to throw that out." There's something in the middle. We're binary searching through the space of how much of the code should you read. If you still read the code, you can still get 2 to 3x speed up. And that's actually better business outcomes than going 10x faster and shipping a bunch of slop.

**Q: What about the "software factory" concept — never have a human read either side of it, pushing further into eval?**

**Dex:** There is a whole rabbit hole you can go down with formal verification and TLA+ or TLA++ — "what if we don't read the code? How can we actually formally verify everything that's working?" I think there's a lot more to be built. But a lot of people right now need to ship code to production systems faster. So maybe someday. I used to cite Sean Gro's talk where he was like "it's just the spec, just write the document that explains the desired behavior and you treat the code like it's assembly and you never read it anymore." I do not endorse that. Let's put it that way.

**Q: About the "dumb zone" and context windows — have you gone back to look at that again with autocompaction and other methods?**

**Dex:** If you have been using AI coding agents for six to nine months and you use them for 60 hours a week, the dumb zone is not a useful concept to you. I will regularly go up to 60%. I will regularly aggressively keep it below 30%. It depends on the complexity of your task, the amount of instructions versus information. If you are using coding agents for the first time, this is what we teach people — shoot to keep it under 40% and if you get up to 60%, think about wrapping it up. What's also nice about these artifacts is we don't use the built-in compaction because everything that matters is going into static assets, so you can always resume from where you left off without having to worry about the quality of an autocompact or a manual compact.

**Host:** Brilliant, Dex. Well done, dude. Thank you. Let's give it up for him!
