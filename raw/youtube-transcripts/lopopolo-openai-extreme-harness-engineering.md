# Extreme Harness Engineering: 1M LOC, 1B toks/day, 0% human code or review — Ryan Lopopolo, OpenAI

- **Source:** https://www.youtube.com/watch?v=CeOXx-XTYek
- **Channel:** Latent Space

---

## Transcript

I do think that there is an interesting space to explore here with codex the harness as part of building AI products. There's a ton of momentum around getting the models to be good at coding. We've seen big leaps in the task complexity with each incremental model release where if you can figure out how to collapse a product that you're trying to build, a user journey that you're trying to solve, into code, it's pretty natural to use the codex harness to solve that problem for you. It's done all the wiring and lets you just communicate in prompts to let the model cook. You kind of have to step back, right? Like you need to take a systems thinking mindset to things and constantly be asking where is the agent making mistakes? Where am I spending my time? How can I not spend that time going forward? And then build confidence in the automation that I'm putting in place so I have solved this part of the SDLC.

Before we get into today's episode, I just have a small message for listeners. Thank you. We would not be able to bring you the AI engineering, science, and entertainment content that you so clearly want if you didn't choose to also click in and tune into our content. We've been approached by sponsors on an almost daily basis. But fortunately, enough of you actually subscribe to us to keep all this sustainable without ads, and we want to keep it that way. But I just have one favor to ask all of you. The single most powerful, completely free thing you can do is to click that subscribe button. It's the only thing I'll ever ask of you, and it means absolutely everything to me and my team that works so hard to bring the In Space to you each and every week. If you do it, I promise you we'll never stop working to make the show even better. Now, let's get into it.

All right, we're in the studio with Ryan Lopopolo from OpenAI. Welcome.

>> Hi.

>> Uh, thanks for visiting San Francisco and thanks for spending some time with us.

>> Yeah, thank you. I'm super excited to be here.

>> You wrote a blockbuster article on harness engineering. It's probably going to be the defining piece of this emerging discipline.

>> Thank you. It's been kind of fun to feel like we've defined the discourse in some sense.

>> Let's contextualize a little bit — this is the first podcast you've ever done. And thank you for spending it with us. What is — where is this coming from? What team are you in? All that jazz.

>> Sure. Sure. Sure. So I work on frontier product exploration, new product development, in the space of OpenAI Frontier, which is our enterprise platform for deploying agents safely at scale with good governance in any business. And the role of me and my team has been to figure out novel ways to deploy our models into packaged products that we can sell as solutions to enterprises.

>> And you have a background — I'll just squeeze it in there — Snowflake, Stripe, Citadel. Yes. Right.

>> Yes. The exact same kind of customer entire life. Yes. The exact kind of customer that you want to —

>> So, I'll say I didn't expect that background. When I looked at your Twitter, I'm seeing the opposite, right? Stuff like this. So you've got the mindset of full-send AI coding, stuff about slop, like buckling in your laptop on your Whimos, and then I look at your profile, I'm like, "Oh, you're correct in the other room, too." So, perfect mix.

>> Perfect. It's quite fun to be AI maximalist. If you're going to live that persona, OpenAI is the place to do it.

>> A token is what they say.

>> Yeah. It certainly helps that we have no rate limits internally and I can go, like you said, full send at this thing.

>> Yeah. So OpenAI Frontier and you're a special team within OAI Frontier.

>> We had been given some space to cook, which has been super super exciting, and this is kind of why I started with kind of an out-there constraint to not write any of the code myself. I was figuring if we're trying to make agents that can be deployed into enterprises, they should be able to do all the things that I do. And having worked with these coding models, these coding harnesses, over 6, 7, 8 months, I do feel like the models are there enough, the harnesses are there enough, where they're isomorphic to me in capability, in the ability to do the job. So starting with this constraint of "I can't write the code" meant that the only way I could do my job was to get the agent to do my job.

>> And just a bit of background before that — this is basically the article. So what you guys did is 5 months of working on an internal tool, zero lines of code, over a million lines of code in the total codebase. You say it was 10x faster than you would have if you had done it by hand. So yeah, that was kind of the mindset going into this, right?

>> That's right. I think we started with some of the very first versions of Codex CLI with the Codex Mini model, which was obviously much less capable than the ones we have today. Which was also a very good constraint, right? It's quite a visceral feeling to ask the model to build you a product feature and it just not being able to assemble the pieces together. Which kind of defined one of the mindsets we had for going into this, which is whenever the model just cannot — you always pop open that task, double click into it, and build smaller building blocks that then you can reassemble into the broader objective. And it was quite painful to do this. Honestly, the first month and a half was 10 times slower than I would be. But because we paid that cost, we ended up getting to something much more productive than any one engineer could be, because we built the tools, the assembly station, for the agent to do the whole thing.

But yeah, so onward to GPT-5, 5.1, 5.2, 5.3, 5.4. To go through all these model generations and see their kind of quirks and different working styles also meant we had to adapt the codebase to change things up when the model was revved. One interesting thing here is 5.2 — the Codex harness at the time did not have background shells in it, which means we were able to rely on blocking scripts to perform long-horizon work. But with 5.3 and background shells, it became less patient, less willing to block. So we had to retool the entire build system to complete in under a minute. And this is not a thing I would expect to be able to do in a codebase where people have opinions. But because the only goal was to make the agent productive, over the course of a week we went from a bespoke makefile build to Bazel to Turbo to NX, and just kind of left it there because builds were fast at that point.

>> Interesting. Talk more about Turbo to NX. That's interesting because that's the other direction that other people have been doing. Ultimately, I have not a lot of experience with actual front-end repo architecture.

>> You're talking to Josh, who built us this. So like, I know the NX team and I know Turbo from Jared Palmer, and I'm like, yeah, that's an interesting comparison.

>> The hill we were climbing was: make it fast.

>> Is there micro frontends involved? It's like, how complex — React, Electron, single app sort of thing —

>> And must be under a minute. That's an interesting limitation. I'm actually not super familiar with the background shell stuff. Probably was talked about in the 5.3 release.

>> Basically means that Codex is able to spawn commands in the background and then go continue to work while it waits for them to finish. So it can spawn an expensive build and then continue reviewing the code, for example. And this helps it be more time-efficient for the user invoking the harness.

>> I guess, just to really nail this — what does 1 minute matter? Like why not five, you know?

>> Okay, we want the inner loop to be as fast as possible. 1 minute was just a nice round number and we were able to hit it.

>> And if it doesn't complete, it kills it or something?

>> No. We just take that as a signal that we need to stop what we're doing. Double click, decompose the build graph a bit to get the time back under, so that we're able to enable the agent to continue to operate.

>> It's almost like a ratchet. It's like you're forcing build-time discipline, because if you don't, it'll just grow and grow and grow.

>> That's right. And you mentioned that — like the software I work on currently is at 12 minutes. It sucks.

>> This has been my experience with platform teams in the past, right? Where you have sort of an envelope of acceptable build times, and you let it go up to breach, and then you spend 2-3 weeks to bring it back down to the lower end. But because tokens are so cheap and we're so insanely parallel with the model, we can just constantly be gardening this thing to make sure that we maintain these invariants. Which means there's way less dispersion in the code and the SDLC, which means we can kind of simplify in a way and rely on a lot more invariants as we write the software.

>> You kind of mentioned in your article — humans became the bottleneck, right? You kicked off as a team of like three people. You're putting out a million lines of code, like 1500 PRs. Basically, what's the mindset there? As much as code is disposable, you're doing a lot of review. A lot of the article talks about how you want to rephrase everything as prompting — everything is what the agent can see; what it can't see is kind of garbage, you shouldn't have it in there. So what's the high level of how you went about building it, and then how you address — okay, humans are just kind of PR review, like how is human-in-the-loop for this?

>> We've moved beyond even the humans reviewing the code as well. Most of the human review is post-merge at this point.

>> But merge merge?

>> That's not even review, that's just like, oh, let's just make ourselves happy by using —

>> Fundamentally the model is trivially parallelizable, right? As many GPUs and tokens as I'm willing to spend, I can have capacity to work on my codebase. The only fundamentally scarce thing is the synchronous human attention of my team. There's only so many hours in the day. We have to eat lunch. I would like to sleep — although it's quite difficult to stop poking the machine because it makes me want to feed it. You kind of have to step back, right? Like you need to take a systems thinking mindset to things and constantly be asking: where is the agent making mistakes? Where am I spending my time? How can I not spend that time going forward? And then build confidence in the automation that I'm putting in place. So I have solved this part of the SDLC.

And usually what that has looked like is — we started needing to pay very close attention to the code because the agent did not have the right building blocks to produce modular software that decomposed appropriately, that was reliable and observable, and actually accreted a working frontend in these things, right? So in order to not spend all of our time sitting in front of a terminal at most doing one or two things at a time, invested in giving the model that observability — which is that graph in the post here.

>> Yeah. Let's walk through this — traces, which existed first.

>> We started with just the app, and the whole rest of it from Vector through to all these logs and metrics APIs was, I don't know, half an afternoon of my time. We have intentionally chosen very high-level fast developer tools. There's a ton of great stuff out there now. We use Mise a bunch, which makes it trivial to pull down all these Go-written VictoriaMetrics stack binaries in our local development. Tiny little bit of Python glue to spin all these up and off you go.

One neat thing here is we have tried to invert things as much as possible. Which is, instead of setting up an environment to spawn the coding agent into, instead we spawn the coding agent — like that's the entry point, just `codex`, and then we give Codex via skills and scripts the ability to boot this stack if it chooses to. And then tell it how to set some env variables so the app in local dev points at this stack that it has chosen to spin up. And this I think is the fundamental difference between reasoning models and the 4.1s and 4o's of the past, where these models could not think. So you kind of had to put them in boxes with a predefined set of state transitions. Whereas here we have the model the harness be the whole box and give it a bunch of options for how to proceed, with enough context for it to make intelligent choices.

>> So sales — feel like a lot of that is around scaffolding, right? Previous agents, you would define a scaffold. It would operate in that loop, try again. That's kind of pivoted off from when we've had reasoning models. They're seeming to perform better when you don't have a scaffold, right? And you go into niches here too — like your spec.md and having a very short AGENTS.md.

>> Yes.

>> You even lay out what it is here, but I like the table of contents. Stuff like this, it really helps guide people because everyone's trying to do this.

>> This structure also makes it super cheap to put new content into the repository to steer both the humans and the agents.

>> I mean, you kind of reinvented Skills, right?

>> One big agent skills from first principles. Skills did not exist when we started doing this, right? You have a short 100-line overall table of contents and then you have little skills, right? Core beliefs MD, tech tracker. Yeah. Yeah. The skills over the tech tracker and the quality score are pretty interesting, because this is basically a tiny little scaffold — like a markdown table — which is a hook for Codex to review all the business logic that we have defined in the app, assess how it matches all these documented guardrails, and propose follow-up work for itself. So before bots and all these ticketing systems, we were just tracking follow-up work as notes in a markdown file, which we could spawn an agent on a cron to kind of burn down.

There's this really neat thing — the models fundamentally crave text. So a lot of what we have done here is figure out ways to inject text into the system, right? When we get a page because we're missing a timeout, for example, I can just at-codex in Slack on that page and say, "I'm going to fix this by adding a timeout. Please update our reliability documentation to require that all network calls have timeouts." So I have not only made a point-in-time fix, but also durably encoded this process knowledge around what good looks like. And we give that to the root coding agent as it goes and does the thing. But you can also use that to distill tests out of, or a code review agent which is pointed at the same things, to narrow the acceptable universe of the code that's produced.

>> One of the concerns I have with that kind of stuff is — you think you're making the right call by making it persisted for all time across everything. But then you didn't think about the exceptions that you need to make, right? And then you have to roll it back. Part of it is also — sometimes it can follow instructions too well.

>> It's somewhat a skill, right? So it determines when it uses the tools. It's not like it'll run at every call. It'll determine when it wants to check quality score, right?

>> Yeah. And in the prompts we give these agents, we allow them to push back. When we first started adding code review agents to the PR, it would be: Codex locally writes the change, pushes up a PR. On those PR synchronizations, a review agent fires, it posts a comment. We instruct Codex that it has to at least acknowledge and respond to that feedback. And initially the Codex driving the code author was willing to be bullied by the PR reviewer, which meant you could kind of end up in a situation where things were not converging. So we kind of had to add more optionality to the prompts on both of these things.

The reviewer agents were instructed to bias toward merging the thing — to not surface anything greater than a P2 in priority. We didn't really define P2, but we gave it a framework within which to score its output. And then —

>> Greater than P0 is worse, right? P0 is "you will nuke the codebase if you merge this thing," right?

>> Yeah. But also on the code authoring agent side, we also gave it the flexibility to either defer or push back against review feedback, right? It happens all the time — like I happen to notice something and leave a code review which could blow up the scope by a factor of two, right? I usually don't mean for that to be addressed exactly in the moment. It's more of an FYI, right? File it to the backlog, pick it up in the next fix-it week sort of thing. And without the context that this is permissible, the coding agents are going to bias toward what they do, which is following instructions.

>> I wanted to check in on a couple things. The code review agent — it can merge autonomously?

>> Yeah.

>> I think that's something that a lot of people aren't comfortable with. And you have a list here of how much agents do — they do product code and test, CI configuration, release tooling, internal dev tools, documentation, eval harness, review comments, scripts that manage the repository itself, production dashboard definition files. Like everything. And so they're just all turning at the same time. Is there a cord that any human on the team pulls to stop everything?

>> So because we are building a native application here, we're not doing continuous deployment, right? So there is still a human in the loop for cutting the release branch. We require a blessed, human-approved smoke test of the app before we promote it to distribution, these sorts of things.

>> So you're working on the app. You're not building infrastructure where you have nines of reliability, that kind of stuff.

>> That's correct. That's correct. And also like, full recognition here that all of this activity took in a completely greenfield repository. There should be no — that this applies generally to "this is a production thing you're going to ship to customers" — of course. So this is real.

>> One of the things there is — you mentioned you started this as a repo from scratch. The onboarding first month or so was pretty — it was like working backwards, right? And you had to work with the system and now you're at that point where you're very autonomous. I'm curious — okay, so how human-in-the-loop is it? What are the bottlenecks that you wish you could still automate? And part of that is also, where do you see the model trajectory improving and offloading more human-in-the-loop? We just got 5.4 — it's a really good fantastic model by the way.

>> Yeah. It's the first one that's merged top-tier coding. So it's Codex-level coding and reasoning. So general reasoning, both in one model, right?

>> And computer use.

>> Computer use. Now I can just have Codex write the blog post — whereas for this one I had to balance between chat and —

>> Oh, I might be out of a job.

>> Oh my god. I know. You just gave me an idea for a completely AI newsletter that 5.4 could do.

>> Yeah. I get it now. This sort of thing is just one example of closing the loop, right? Like the dashboard thing you mentioned — we have Codex authoring the JSON for the Grafana dashboards and publishing them, and also responding to the pages. Which means when it gets the page, it knows exactly which dashboards are defined and what alerts — what alert was triggered by which exact log in the codebase — because all of this stuff is collated together.

>> It has to own everything.

>> Yes. And it means that if we have an outage that did not result in a page, it has the existing set of dashboards available to it, it has the existing set of metrics and logs, and can figure out where the gaps in the dashboard are or in the underlying metrics, and fix them in one go. In the same way you would have a full-stack engineer be able to drive a feature from the backend all the way to the frontend.

>> So it seems like a lot of the work you guys had to do was — you, as a small team, are fully working for a way that the model wants the software to be written, right? It's less human-legible for better code legibility, agent legibility. How do you think that affects broader teams? Like at OpenAI, do you liaise — "this is how software should be written"? I can imagine, say, you join a new team with this methodology, this mindset. There's ways teams do code review, teams write code, teams are structured. And a lot of it is for human legibility. So should we all swap? How does this play back, one, broader into OpenAI, and then broader into software engineering, right? Like, teams that pick this up — you have to make a pretty big switch. Should they just full send?

>> The mindset is very much that I'm removed from the process, right? I can't really have deep code-level opinions about things. It's as if I'm group tech-leading a 500-person organization. Like, it's not appropriate for me to be in the weeds on every PR. This is why that post-merge code review thing is a good analog here, right? Like, I have some representative sample of the code as it is written, and I have to use that to infer what the teams are struggling with, where they could use help, where they're already moving quickly and I can pivot my focus elsewhere. So I don't really have too many opinions around the code as it is written. I do however have, like, a command-based class which is used to have repeatable chunks of business logic that comes with tracing and metrics and observability for free, right? And the thing to focus on is not how that business logic is structured, but that it uses this primitive — because I know that's going to give leverage by default.

Back to that sort of systems thinking — and you have part of that in your blog post: enforcing architecture and taste, how you set boundaries for what's used. There's also a section on redefining engineering and stuff. But yeah, it's interesting to hear. As the models have gotten better, they have gotten better at proposing these abstractions to unblock themselves, which again lets me move higher and higher up the stack to look deeper into the future on what ultimately blocks the team from shipping.

>> So you — this is primarily an, it's like a 1-million-line-of-code codebase, Electron app — but it manages its own services as well. So it's like a backend-for-frontend type thing.

>> We do have a backend in there, but that's hosted in the cloud. But this sort of structure is actually within the separate main and renderer processes within the Electron.

>> That's just how Electron works.

>> Yeah. So we have also treated MVC-style decomposition with the same level of rigor, which has been very fun.

>> I have a fun pun — this is a tangent — but you know, MVC is Model-View-Controller and any sort of full-stack web dev knows that. But my AI-native version of this is Model-View-Claw. The Claw, the harness.

>> That's right. That's right. I do think that there is an interesting space to explore here with Codex the harness as part of building AI products. There's a ton of momentum around getting the models to be good at coding. We've seen big leaps in the task complexity with each incremental model release, where if you can figure out how to collapse a product that you're trying to build, a user journey that you're trying to solve, into code, it's pretty natural to use the Codex harness to solve that problem for you. It's done all the wiring and lets you just communicate in prompts to let the model cook.

>> It's been very fun. And it's also like a very engineering-legible way of increasing.

>> Just give the model scripts — the same scripts you would already build for yourself.

>> So for listeners, this is Ryan saying that software engineering or coding agents will eat knowledge work — like the non-coding parts that you would normally think, oh, you have to build a separate agent for it. No, you start with coding agent and go up from there. Which OpenClaw has, right? It's PI under the hood.

>> Yes. Basically define your task in code. Everything is a coding agent.

>> By the way, since I brought it up, it's probably the only place you bring it up — is any OpenClaw usage from you?

>> No, no, not for me. I don't have any spare Mac minis rattling around my house.

>> You can afford it. No, I'm just kind of curious if it's changed anything in OpenAI yet, but it's probably early days. And then the other thing I want to pull on here is — you mentioned ticketing systems and you mentioned PRs, and I'm wondering if both those things have to go away or be reinvented for this kind of coding, right? So git itself is very hostile to multi-agents.

>> Yeah, we make very heavy use of worktrees.

>> Right? But like, even then — I just dropped a podcast yesterday with Cursor saying they're getting rid of worktrees because it still has too many merge conflicts. It's still too unintuitive. But go ahead.

>> The models are really great at resolving merge conflicts. And to get to a state where I'm not synchronously in the loop in my terminal, I almost don't care that there are merge — disposable, right? We invoke a `dollar-land` skill, and that coaches Codex to push the PR, wait for human and agent reviewers, wait for CI to be green, fix the flakes if there are any, merge upstream if the PR comes into conflict, wait for everything to pass, put it in the merge queue, deal with flakes until it's in main. And this is kind of what it means to delegate fully, right? Like, this is in a, you know, very large model probably a significant tax on humans to get PRs merged, but the agent is more than capable of doing this and I really don't have to think about it other than keep my laptop open.

I used to be much more of a control freak, but now I'm like, yeah, actually you could do a better job than me with the right context.

>> Yes.

>> Anything else in harness engineering in general? Just this piece — I just wanted to make sure we —

>> I think one thing that I maybe didn't make super clear in the article that I kind of heard on Twitter as an interest to them — what's the chatter and then what's your response?

>> Ultimately, all the things that we have encoded in docs and tests and review agents and all these things are ways to put all the non-functional requirements of building high-scale, high-quality, reliable software into a space that prompt-injects the agent. We either write it down as docs, we add lints where the error messages tell how to do the right thing. So the whole meta of the thing is to basically tease out of the heads of all the engineers on my team what they think good looks like, what they would do by default, or what they would coach a new hire on the team to do to get things to merge. And that's why we pay attention to all the mistakes that the agent makes, right? This is code being written that is misaligned with some as-yet-not-written-down non-functional requirement.

>> Sorry, what did the online people misunderstand?

>> No, what somebody just literally said that. I was like, "Oh, yeah. Okay. This is the thing. This is what I was doing." Agree with. Yeah. I see. I see. I see. Interesting.

>> One other neat thing which I did totally not expect is folks were just taking the link to the article and giving it to like PI or Codex, and saying "make my repo this." You achieve a full recursion. And it was wildly effective. Really, it was wildly effective.

>> This actually is something I tried with 5.4 yesterday. I didn't have that much time — I was out speaking at something — and this is one of my things. I was like, okay, I have this article, can we just scaffold out what it would be like to run this. And I did it first as that, and then I was like, okay, let me take another little side repo and say, like, okay, if I was to fully automate this. Cuz I haven't written a line of code, it's like a full set — it's a side thing I'm doing with voice TTS. I'm just slobbing out whatever, it's not production. I'm like, how would I make this like this. And it's actually a really good way — it's a good way to learn what could be changed, what could be — it's just a good analyzing, right? You give it all the code, you give it all the context, you give it the article, and it walks you through it very well.

>> That's right. That's right.

>> I guess one more thing before we go to Symphony — I wanted to cover Bret Taylor's response. We had him on the show. He is your chairman, which is wild.

>> Yeah.

>> That he's reading your articles as well and getting engaged in it. He says software dependencies are going away, basically. They can just be vendored. Response?

>> 100%. You still pay Datadog. You still pay Temporal. Thank you. The level of complexity of the dependencies that we can internalize is, I would say, low-medium right now. Right, just based on model capability.

>> What is medium?

>> I would say like a couple-thousand-line dependency is a thing that we could in-house no problem in an afternoon of time. One neat thing about it is, like, probably most of that code you don't even need, right? Like by in-housing an abstraction, you can kind of strip away all the generic parts of it and only focus on what you need to enable the specific things you're building.

>> I've been calling this "the end of plugins."

>> Yeah, because there's so much — like, you know, when I publish an open source thing, I want to accept everything and be liberal, I want to accept — right, this is Postel's law. But that means there's so much overhead.

>> One other neat thing about this too is when we deploy Codex Security on the repo, it is able to deeply review and change the internalized dependencies, in a much lower-friction way than it would be to push patches upstream, wait for them to be released, pull them down, make sure that's compatible with all the transitives I have in my repo, and things like that. So it's also much lower friction to internalize some of these things, if code is free because the tokens are cheap, sort of thing.

>> The only argument I have against this is basically scale testing, which obviously the larger pieces of software like Linux, MySQL — he calls up even the Datadogs and Temporals — and then maybe security testing, where, classically I think it is Linus Torvalds who said open source is the best disinfectant.

>> Right, many eyes.

>> Many eyes. And if you inline your dependencies and code them up, you're going to have to relearn mistakes from other people.

>> Yep. Yep. And to internalize that dependency, you're back to zero, and you have to kind of start reassembling all those bits and pieces to have high confidence in the code as it is written.

>> Even part of the first intro of this, you basically mentioned everything was written by Codex including internal tooling, right? So internal tooling — like, when you're visualizing what's going on, it's writing it forward to —

>> Yeah, I built internal tools for AIE now and I just showed them off and they're like, how long did you spend? And I didn't spend any time, I just prompted it.

>> Very funny story here. We had deployed our app to the first dozen users internally, had some performance issues. So we asked them to export a trace for us — get a tarball, gave it to our on-call engineer, and he did a fantastic job of working with Codex to build this beautiful local-dev-tool Next.js app that you drag and drop the tarball in and it visualizes the entire trace. It's fantastic — took an afternoon — but none of this was necessary, because you could just spin up Codex and give it the tarball and ask the same thing, and get the response immediately. So in a way, optimizing for human legibility of that debugging process was wrong. It kept him in the loop unnecessarily, when instead he could have just like — Codex cooked for 5 minutes and gotten the same.

>> Yeah. You have to fight your instincts here of "this is how we used to do it," or "this is how I would have used to solve it."

>> Yeah. In this local observability stack — like sure, you can deploy Jaeger to visualize the traces, but I wouldn't expect to be looking at the traces in the first place because I'm not going to write the code to fix them.

>> Yeah. I mean, so basically there needs to be like this kind of in-house stack and owning the whole loop. I think that is very well established. And it sounds like you might be sharing more about that in the future, right?

>> Yeah. I think we're excited to do so. We're going to talk about Symphony in a little bit, but the way we distribute it as a spec — which I think folks are calling "ghost libraries" on Twitter, like this is such a cool name — it does mean it becomes much cheaper to share software with the world, right? You define a spec how you could build your own, specifying as much as is required for a coding agent to reassemble it locally. The flow here is very, very cool. Like, we have taken all the scaffolding that has existed in our proprietary repo, spun up a new one, asked Codex with our repo as a reference, write the spec. We tell it: spin up a tmux, spawn a disconnected Codex to implement the spec, wait for it to be done, spawn another Codex and another tmux to review the implementation compared to upstream and update the spec so it diverges less. And then you just loop over and over and over — Ralph style — until you get a spec that is with high fidelity able to reproduce the system as it is. It's fantastic.

>> And you're basically not really adding any of your human bias in there, right? Like a lot of times people will write a spec and be like, okay, I think it should be done this way, and you'll riff on something, and it's like, no, that agent could have just handled it. Like you're still scaffolding in a sense, right? "I want it done this way." It can determine that spec better.

>> That's right. That's right. Part of me — I've been working a lot on eval recently — and part of me is wondering if an agent can produce a spec that it cannot solve. Like, is it always capable of things that it can imagine? Or can you imagine things that it is impossible to do? I think with Symphony there's this axis, right, where you have things that are easy or hard, established or new, right? And I think things that are hard and new is still something that the models need humans to drive. But I think those other quadrants are largely solved given the right scaffold and the right thing that's going to drive the agent to completion.

>> It's crazy that it's solved.

>> But it means that the humans, the ones with limited time and attention, get to work on the hardest stuff, right? Like the problems where it's pure whitespace out in front, or the deepest refactorings where you don't know what the proper shape of the interfaces are. And this is where I want to spend my time, because it lets me set up for the next level of scale.

>> Yeah. Amazing. Let's introduce Symphony. I think we've been mentioning it every now and then. Elixir — interesting option.

>> Yeah. And again, the Elixir manifestation here is just a derivative.

>> Is it a model-chosen?

>> Uh, yeah. And it chose that because the process supervision and the gen servers are super amenable to the type of process orchestration that we're doing here, right? You are essentially spinning up little daemons for every task that is in execution and driving it to completion. Which means the model gets a ton of stuff for free by using Elixir and the BEAM.

>> I had to go do a crash course in BEAM and Elixir, and I think most people are not operating at that scale of concurrency where you need that. But it is a good mental model of resumability and all those things, and these are things I care about. But tell me the origin story of Symphony — what do you use it for? How did it form, and maybe any abandoned paths that you didn't take?

>> At the end of December, we were at about three and a half PRs per engineer per day. This was before 5.2 came out in the beginning of January. Everyone gets back from holiday with 5.2 and no other work on the repository — we were up in the five-to-ten PRs per day per engineer. And like, I don't know about y'all, but it's very taxing to constantly be switching like that. Like, I was pretty tapped out at the end of the day. So again, where are the humans spending their time? They're spending their time context-switching between all these active tmux panes to drive the agent forward. So let's again build something to remove ourselves from the loop.

And this is what — uh, frantic sprint — adapter here, to find a way to remove the need for the human to sit in front of their terminal. So lot of experimentation with dev boxes and automatically spinning up agents. It seems like a fantastic end state here where my life is beach. I open L twice a day and say yes/no to these things. And this is again a super, super interesting framing for how the work is done because I become more latency-insensitive. I have way less attachment to the code as it is written. Like I've had close to zero investment in the actual authorship experience. So if it's garbage, I can just throw it away and not care too much about it.

In Symphony, there's this rework state where once the PR is proposed and it's escalated to the human for review, it should be a cheap review, right? It is either mergeable or it is not. And if it's not, you move it to rework — the Elixir service will completely trash the entire worktree and PR and start it again from scratch. And this is that opportunity again to say: why was it trash, right? What did the agent do that was — fix that before moving the ticket to progress again.

>> Why is this not in Codex app? I guess it's — you guys are ahead of Codex app, I guess.

>> Yeah. So the way the team has been working is basically to be as AI-pilled as possible and spread ahead, and a lot of the things we have worked on have fallen out into a lot of the products that we have. Like, we were in deep consultation with the Codex team to have the Codex app be a thing that exists, right? To have skills be a thing that Codex is able to use, so we didn't have to roll our own. To put automations into the product, so all of our automatic refactoring agents didn't have to be these hand-rolled control loops. It has been really fantastic to be in a way unanchored to the product development of Frontier and Codex, and just very quickly try to figure out what works, and then later find the scalable thing that can be deployed widely. It's been a very fun way to operate.

It's certainly chaotic. I have lost track very often of what the actual state of the code looks like because I'm not in the loop, right? There was one point where we had wired Playwright directly up to the Electron app with MCP. MCPs I'm pretty bearish on because the harness forcibly injects all those tokens in the context and I don't really get a say over it. They mess with autocompaction. The agent can forget how to use the tool. There's probably only like three calls in Playwright that I actually ever want to use. So I pay the cost for a ton of things. Somebody vibed a local daemon that boots Playwright and exposes a tiny little shim CLI to drive it. And I had zero idea that this had occurred, because to me I run Codex and it's able to, you know, get better.

>> Yeah. Like no knowledge of this at all. So we have had, in human space, to spend a lot of time doing synchronous knowledge sharing. We have a daily standup that's 45 minutes long because we almost have to fan out the understanding of the current state.

>> I was going to say — this is good for a single human, multi-agent. But multi-human, multi-agent is a whole — like POL, like explosion of stuff.

>> Yeah. And this is fundamentally why we have such a rigid, like 10,000-engineer-level architecture in the app, because we have to find ways to carve up the space so people are not trampling on each other.

>> Sorry, I don't get the 10,000 thing. Did I miss that?

>> The structure of the repository is like 500 npm packages. It's architecture-to-the-max for what you would consider — I think normal for a seven-person team. But if every person is actually like 10 to 50, then the numbers on being super super deep into decomposition and sharding and proper interface boundaries make a lot more sense.

>> Right, to me that's why I talked about micro-frontends, and NX is from that world. But cool — just coming back to this, I don't know if you have other thoughts on orchestrating so much work going through. Is this enough? Is there any aha moments?

>> It'll be interesting to see — okay, so right now you pick Linear as your issue tracker, right?

>> Or, is it actually Linear?

>> This is actually Linear.

>> Oh, that's Linear.

>> It's Linear.

>> Oh, I never look at the video. The demo video I had to download to run, but yeah. So I — cuz I'm a Slack maxi, but Linear is also really good.

>> Yes, we do make good use of Slack. We fire off Codexes to do all these low-complexity fixups, the things that sync that knowledge into the repository. It's super cheap.

>> Yeah, do it in Codex.

>> My biggest plug is — OpenAI needs to build Slack, right? You need to own Slack to build us to turn this into —

>> I did read it. Yeah.

>> I would say that if we think that we want these agents to do economically valuable work — which is the mission, right? We want AI to be deployed widely to do economically valuable work — then we need to find ways for them to naturally collaborate with humans. Which means collaboration tooling I think is an interesting space to explore.

>> Yeah, totally. GitHub, Slack, Linear. Yeah, that was kind of my thing — like, okay, where do we see right now? Codex has started — Codex model, then CLI, now there's an app. App can let me shoot off multiple Codexes in parallel, but there's no great team collaboration for Codex, right? And it seems like your team had some say into what comes out, right? Like you talked to them, Codex kind of was a thing from there. If you guys are on the bleeding edge stuff that you might not focus on — but like, what do you expect other people to be building, right? So people that are 5x'ing, 50x'ing — should you build stuff that's very niche for your workflow, for your team? Should it be more general so other people can adopt it? Is there a niche there? Because part of it is like, okay, is everything just internal tooling? Do we have everything our own way? The way our team operates has its own ways that we like to communicate. Or is there a broader way to do it? Is it something like an issue tracker? Just thoughts if you want to riff on that.

>> I think TBD — like, we have not figured this out in a general way. I do think that there is leverage to be had in making the code and the processes as much the same as possible. If you think that code is context, code is prompts, it's better from the agent behavior perspective to be able to look in a package in directory XYZ and it not have to page so deeply into directory ABC, because they have the same structure, use the same language, they have the same patterns internally. And that same leverage comes from aligning on a single set of skills that you're pouring every engineer's taste into to make sure that the agent is effective. So like in our codebase, we have I think six skills. That's it. And if some part of the software development loop is not being covered, our first attempt is to encode it in one of the existing setup skills. Which means that we can change the agent behavior more cheaply than changing the human-driver behavior.

>> Have you experimented with agents changing their own behavior?

>> We do. Yes. Or parent agent changing a sub-agent's behavior, or something like that. We have some bits for skill distillation. So for example, there's one neat thing you can do with Codex which is just point it at its own session logs and ask it to tell you how you can use the tool better.

>> Introspection — ask it to do things.

>> "How can I use this session better? What skills should I have?" Yeah, I like the modification of "you can just do things" — like you can just ask agent to do things.

>> Yeah, you can just Codex things. This is like a silly emoji that we have — "you can just Codex things." You can just prompt things. It's really glorious future we live in. But like, okay, you can do that one-on-one. But we're actually slurping these up for the entire team into blob storage and running agent loops over them every day to figure out where as a team can we do better, and how do we reflect that back into the repository. So everybody benefits from everybody else's behavior for free. Same for like PR comments, right? These are all feedback that means the code as written deviated from what was good. A PR comment, a failed build — these are all signals that mean at some point the agent was missing context. We've got to figure out how to slurp it up and put it back in the repo.

>> By the way, I do this exactly right. I used — when I use Claude Code for knowledge work — Claude code work is a nice product, right? I think you would agree. I always have it tell me, "what do I do better next time?" And that's the meta-programming reflection thing.

>> So almost think — like you have six reflection extraction levels in Symphony, almost like the zero layer. So the six levels are policy, configuration, coordination, execution, integration, observability. We've talked about a couple of these, but the zero layer is like the okay, well, are we working well? Can we improve how we work? Like, can I modify my own workflow MD or something? I don't know.

>> Yeah, of course. Yeah, of course you can. Like, this thing is also able to cut its own tickets because we give it full access.

>> Yeah. Make it a ticket to have it cut tickets. You can put in the ticket that you expected to file it on follow-up work.

>> Self-modifying.

>> Yeah. Don't put the agent in a box. Give the agent full accessibility over its domain.

>> I had a mental reaction when you said don't put the agent in a box. So I think you should put it in a box — like, it's just that you're giving the box everything it needs.

>> Yeah. Context and tools, right? But we're, like, as developers we're used to calling out to different systems. But here, you use the open-source things, like Prometheus or whatever, and you run it locally so that you can have the full loop. Right? I assume.

>> Yep. Right. I think you want to minimize cloud dependencies. You also want to make sure that you think about what the agent has access to, right? Like, what does it see? Does it go back into the loop, like, from the most basic sense of you let it see its own calls, traces? It can determine where it went wrong, right? But are you feeding that back in? So just the most basic level of: you want to see exactly what's input, output. Like, does the agent have access to what is being outputted, right? It can self-improve a lot of these things.

>> It's all text, right? My job is to figure out ways to funnel text from one agent to the other.

>> It's so strange. Like, you know, way back at the start of this whole AI wave, like Andrej was like, you know, "English is the hottest new programming language." It's here. The features.

>> Yeah, a lot of, okay, like a lot of software, a lot of stuff, there's a GUI, it's made for the human. We're seeing the evolution of CLI for everything, right? All tools have CLI, you can use them well. But, you know, do we get good vision? Do we get good little sandboxes? Like right now it's a really effective way, right? Models love to use tools, they love to bash, they love to read through text. So slap a CLI, let it go loose — that works for everything.

>> That does. Yeah. We've also been adapting non-textual things to that shape in order to improve model behavior in some ways, right? Like we want the agent to be able to see the UI. Agents do not perceive visually in the same way that we do, right? Like, they don't see a red box, they see "red box button," right? They see these things in latent space. So if we want — yeah, we have a thing that goes off every time he goes to space. Ding.

Anyway — if we want to actually make it see the layout, it's almost easier to rasterize that image and feed it in to the agent. And there's no reason you can't do both, right? To further refine how the model perceives the object it's manipulating.

>> Cool. Could we — you want to talk about a couple more of these layers that might bear more introspection or that you have personal passion for? I will say that the coordination layer here was a really tricky piece to get right.

>> Let's do it. Yeah, I'm all about that. And this is Temporal's core core thing.

>> This is where when we turn the spec into Elixir, where the model takes a shortcut, right? It's like, oh, I have all these primitives that I can make use of in this lovely runtime that has native process supervision. Which is, I think, kind of a neat way to have taken the spec and made it more achievable by making choices that naturally map the domain, right? In the same way that you would prefer to have a TypeScript monorepo if you are doing full-stack web development, right? Because the ability to share types across the front end and back end reduces a lot of complexity.

>> That's what GraphQL used to be.

>> That's right. And —

>> I don't know if it's still alive, but —

>> No humans in the loop here. So like, my own personal ability to write or not write Elixir doesn't really have to bias us away from using the right tool for the job. Which is just wild.

>> Love it. I love it. Yeah. I wonder if any languages struggle more than others because of this. I feel like everyone has their own abstractions that would make sense, but maybe it might be slower. It might be more faulty, where you would have to just kick the server every now and then. I don't know. I think observability layer is really well understood. Integration layer — MCP is dead. I think all these — just like a really interesting hierarchy to travel up and down. It's common language for people working on the system to understand.

>> The policy stuff is really cool, right? Like, yeah, you don't really have to build a bunch of code to make sure the system waits for CI to pass. It's your institutional knowledge.

>> Yeah, you just give it the GH CLI with some text to say "CI has to pass."

>> It makes the maintenance of these systems a lot easier.

>> Do you think that CLI maintainers need to do anything special for agents? Or just as is, it's good? Cuz like, I don't think when people made the GitHub CLI they anticipated this happening.

>> That's correct. The GH CLI is fantastic. It's great. Super industry. If you want to go try `gh repo create`, like `gh pull` and then pull request number — right, `gh` like 153 whatever, right? And then it pulls — basically my only interaction with the GitHub web UI at this point is `gh pr view --web`, glance at the diff, and be like, "sure thing, send it." Yeah. Yeah.

But the CLIs are nice cuz they're super token-efficient, and they can be made more token-efficient really easily, right? Like, I'm sure you all have seen — like, I go to Buildkite or Jenkins and I just get this massive wall of build output. And in order to unblock the humans, your developer productivity team is almost certainly going to write some code that parses the actual exception out of the build logs and sticks it in a sticky note at the top of the page. And you basically want CLIs to be structured in a similar way, right? You're going to want to patch `--silent` to Prettier because the agent doesn't care that every file was already formatted. It just wants to know it's either formatted or not, right? So they can then go run the write command. Similarly, like in our pnpm sort of distributed script runner, when you do `--recursive`, it produces an absolute mountain of text, but all of that is for passing test suites. So we ended up wrapping all of this in another script to suppress the —

>> Which you can vibe to generally output the failing parts of the test.

>> Yeah, you could pipe errors versus standard out.

>> I don't know. Okay, whatever. Too much thinking to have to do the CLI. I used to maintain a CLI for my company, and like, yeah, this is core, very core to my heart. But you're vibing my job.

>> That's right.

>> Cool. Any other things? I mean, this is a long spec. I appreciate that. It's got a lot of strong opinions in here. Any other things that we should highlight? You know, I think obviously you can spend the whole day going through some of these. But I do think that some of these have a lot of care, or some of these you might want to tell people, "hey, take this, but make it your own."

>> Fundamentally, software is made more flexible when it's able to adapt to the environment in which it is deployed, right? Which means that things like Linear or GitHub — even — are specified within the spec, but not required pieces of it, right? There's like a more platonic ideal of the thing, that you could swap in like Jira or Bitbucket for example, right? But being able to tightly specify things like the ID formats, or how the Ralph loop works for the individual agents, basically means you can get up and running with a fully-specified system quickly that you then evolve later on. I think we never intended for this to be a static spec that you can never change, right? It's more like a blueprint to get something working up and running for you, then to vibe later till your heart's content.

>> You have like code and scripts in here where it's like, oh — I mean, I think this is a really good prompt. It's just a very, very long prompt.

>> Fundamentally, the agents are good at following instructions. So give them instructions, right? And it will improve the reliability of the result, right? Like, much like the way we use Symphony, we don't want folks to have to monitor the agent as it is vibing the system into existence. So being very opinionated, very strict around what these success criteria are, means that our deployment success rate goes up. Means we don't have to get tickets on this thing.

>> I think it all goes back to that "it's disposable," right? Like early on, when you had CLI or you'd kick off a Codex run, it would take two hours. You would kind of want to monitor like, okay, I'm in the workflow of just using one. I don't want it to go down the wrong path, I'll cut it off. But, you know, just shoot all four. Like, that was my favorite thing of the Codex app, right? Just 4x it. Like, it's okay. One of them will probably be right, one of them might be better. Stop overthinking it.

Like my first example was probably deep research. When you put out deep research, and I asked it something — it thought it was legal something and spent an hour, came back with a report completely off the rails. And I was like, okay, I got to monitor this thing a bit. No — don't monitor it, just you want to build it so that it goes the right way and you don't want to sit there and babysit, right? You don't want to babysit your agents.

>> With that deep research query that you made looking at the bad result, you probably figured out you needed to tweak your prompt a bit, right? Like, that's the guardrail that you fed back into the codebase, or the ask, your prompt, to further align the agent's execution. Same sort of concepts apply there too.

>> When you talk — I mean, how are the customers feeling for Symphony?

>> I think we have none, right? This is a thing we have put out into the world.

>> I mean, Symphony is internal, right? As long as you're happy, you're the customer.

>> That's right.

>> Just, you know, what's the external view?

>> I'd say folks are very excited about this way of distributing software and ideas in cheap ways. For us as users, it has again pushed the productivity 5x. Which means I think there's something here that's like a durable pattern around removing the human from the loop and figuring out ways to trust the output, right? The video that is shared here is the same sort of video we would expect the coding agent to attach to the PR that is created. You know, that's part of building trust in this system. And that's to me, fundamentally, what has been cool about building this is — it more closely pushes that persona of the agent working with you to be like a teammate, right? I don't shoulder-surf you for the tickets that you work on during the week. I would never think that I would want to do that. I wouldn't want a screen recording of your entire session in Cursor or Claude Code. I would expect you to do what you think you need to do to convince me that the code is good and mergeable, and compress that full trajectory in a way that is legible to me, the reviewer.

>> And you can just do that because — Codex will absolutely sling some FFmpeg around. It's great.

>> Oh, I mean, FFmpeg is the OG god CLI.

>> Yeah. Swiss army chainsaw.

>> I used to say there's a SaaS — micro-SaaS, let's call it — in every flag in FFmpeg.

>> Oh, for sure.

>> You know what I mean? For sure. Like, just host it as a service, put a UI on it. People who don't know FFmpeg will pay for it.

>> When we were first experimenting with this, it was a wild feeling to be at the computer with just like windows just popping up all over the place and getting captured and files appearing on my desktop. Like, very much felt like the future to have a thing controlling my computer for actual productive use, right? Like I'm just there keeping it awake, jiggling the mouse every once in a while.

>> That's what some office workers do. They buy a mouse jiggler.

>> That's right. That's right.

>> One thing I wanted to ask — so okay, as stuff is so good, is disposable async, shoot off a bunch of agents. One question is — okay, are you always like an extra-high thinking guy, and where do you see Spark, so 5.3-Spark? Like, there's a lot of me wanting to make quick changes. I'm not going to open up an IDE, I'm not going to do anything, but I will say "okay, fix this little thing, change a line, change a color." Spark is great for that. But like, am I still the bottleneck? Why don't I just let that go back in like just riff on that, you know? Is there —

>> Spark is such a different model compared to the extra-high-level reasoning that you get in these.

>> To be fair for people, it is a different model, different architecture, different — like, it doesn't support — it just —

>> It's incredibly fast.

>> I have not quite figured out how to use it yet, to be honest. Faster, I was — I was adapting it to the same sorts of tasks I would use extra-high reasoning for, and it would blow through three compactions before writing a line of code.

>> And I mean, that's another big thing with 5.4 — million-token context, which is huge in agentic, right? Like, you can just run for longer before you have to compact. The more tokens you can spend on a task before compacting, the better you'll do.

>> That's right. That's right. I'm not sure how to deploy Spark. I think your intuition is right that it's very great for spiking out prototypes, exploring ideas quickly, doing those documentation updates. It is fantastic for us in taking that feedback and transforming it into a lint where we already have good infrastructure for ESLints in the codebase. These sorts of things it's great at, and it allows us to unblock quickly doing those antifragile, healing tasks in the codebase.

>> Yeah, that makes sense. So you're pushing models to the freaking limit. What can current models not do well yet?

>> They're definitely not there on being able to go from new product idea to prototype, single one shot. This is where I find I spend a lot of time steering — translating end-state of a mock for a net-new thing, right? Think no existing screens, into product that is playable with. Similarly, while this has gotten better with each model release, the gnarliest refactorings are the ones that I spend my most time with, right? The ones where I am interrupting the most, the ones where I am now double-clicking to build tooling to help decompose monoliths and things like that.

This is a thing I only expect to get better, right? Over the course of a month, we went from the low-complexity tasks to low-complexity and big tasks in both these directions. So, this is what it means to not bet against the model, right? You should expect that it is going to push itself out into these higher and higher complexity spaces. So, the things we do are robust to that. It just basically means I'll be able to spend my time elsewhere and figure out what the next bottleneck is.

>> I do think it's also a bit of a different type of task, right? Like, Codex is really good at codebase understanding, working with codebases. But companies like Lovable, Bolt, Replit — they solve a very different problem: scaffold of zero-to-one, right? Idea to product. And it's like, there are people working on that, and models are also pushing step-function changes there. It's just kind of different than the software engineering agents you see today, right?

>> Like I said, the model is isomorphic to myself. The only thing that's different is figuring out how to get what's in here into context for the model. And for these whitespace sort of projects, I myself am just not good at it. Which means that often over the agent trajectory I realize the bits that were missing — which is why I find I need to have the synchronous interaction. And I expect, with the right harness, with the right scaffold, that's able to tease that out of me, or refine the possible space, right? To be super opinionated around the frameworks that are deployed, or to put a template in place, right? These are ways to give the model all those non-functional requirements, that extra context to anchor on, and avoid that wide dispersion of possible outcomes.

>> Thank you for that. I wanted to talk a little bit about Frontier. Overall, you guys announced it maybe like a month ago. There's a few charts in here, and it's kind of like your enterprise offering, is kind of what I view it. Is there one product, or is there many?

>> I can't speak to the full product roadmap here, but what I can say is that Frontier is the platform by which we want to do AI transformation of every enterprise — from big to small. And the way we want to do that is by making it easy to deploy highly observable, safe, controllable, identifiable agents into the workplace, right? We want it to work with your company-native IAM stack, we want it to plug into the security tooling that you have, we want it to be able to plug into the workspace tools that you used.

>> So you're just going to be stripping specs, right?

>> We expect that there will be some harness things there. Agents SDK is a core part of this to enable both startup builders as well as enterprise builders to have a works-by-default harness that is able to use all the best features of our models — from the shell tool down to the Codex harness with file attachments and containers and all these other things that we know go into building highly reliable, complex agents. We want to make that great, and we want to make it easy to compose these things together in ways that are safe.

For example, the GPT OSS SafeGuard model — one thing that's really cool about it is it ships the ability to interface with a safety spec. Safety specs are things that are bespoke to enterprises. We owe it to these folks to figure out ways for them to instrument the agents in their enterprise to avoid exfiltration in the ways they specifically care about, to know about their internal company code names, these sorts of things. So providing the right hooks to make the platform customizable, but also mostly working by default for folks, is kind of the space we are trying to explore here.

>> Yeah. And this is — the Snowflakes of the world just need this. The Brexes of the world, Stripes. Yeah, makes sense. I was going to go back to your — I think the demo videos that you guys had were pretty illustrative. It's kind of like, also to me, an example of very large-scale agent management.

>> Yes.

>> Like, you give people a control dashboard that, if you play any one of these multiple-agent things, you can dig down to the individual instance and see what's going on.

>> Yes, of course.

>> But who's the user? Is it the CEO, the CTO, CIO, something like that?

>> So, you know, at least my personal opinion here, the buyer that we're trying to build product for here is — one — employees who are making productive use of these agents, right? That's going to be whatever surfaces they appear in, the connectors they have access to, things like that. Something like this dashboard is for IT, your GRC and governance folks, your AI innovation office, your security team, right? The stakeholders in your company that are responsible for successfully deploying into the spaces where your employees work, as well as doing so in a safe way that is consistent with all the regulatory requirements that you have, and customer attestations and things like that. So it is kind of an iceberg beneath the actual end.

>> Yeah, you jump like every — I guess every layer in the UI is going down the layer of abstraction in terms of the agent, right?

>> Yep. The ability to dive deep into the individual agent trajectory level is going to be super powerful, not only from a security perspective, but also from someone who is accountable for developing skills.

One thing that was interesting that we also blogged about shipping was an internal data agent, which uses a lot of the Frontier technology in order to make our data ontology accessible to the agent, and things like that to understand what's actually in the data warehouse.

>> Yeah, semantic layer-type things. I was briefly part of that world. Is it solved? I don't know. It's actually really hard for humans to agree on what revenue is.

>> Yes.

>> What is an active user?

>> There's like five data scientists in the company that have defined this golden — they all different.

>> Yeah, and there's also internal politics as to attribution of, like, "I'm marketing, I'm responsible for this much, and sales is responsible for this much," and they all add up to more than 100, and I'm like, well, you guys have different definitions.

>> Yeah. And if you're a startup, everything is ARR, you know.

>> So I think that's cool. Oh, you guys blogged about this. Okay, I didn't see this. Yeah, is this the same thing? Is this what you're referring to?

>> Yes.

>> Okay, well, we'll send people to read this as our data agent.

>> Yeah, I don't know if you have any highlights.

>> No, no, in general from the point — a lot of good things to read.

>> Yeah. Lots of homework for people. Data as the feedback layer — you need to solve this first in order to have the products feedback loop closed.

>> That's right. This is how you build agents that do more than coding, right? To actually understand how you operate the business, you have to understand what revenue is, what your customer segments are, right? What your product lines are, right? Looping back to the codebase that we described here for harnessing — one thing that's in core-beliefs.md is who's on the team, what product we're building, who our end customers are, who our pilot customers are, what the full vision of what we want to achieve over the next 12 months is. These are all bits of context that inform how we would go about building the software. So we have to give it to the agent, too.

>> I'm guessing that stuff is pretty dynamic and it changes over time too, right? Like, part of it was — it's not just a big spec. You have it as one of the things, and it will iterate.

>> One thing that I think is going to break your mind even more is — we have skills for how to properly generate deep-fried memes and have reaction-emoji culture in Slack. Because with the Slack ChatGPT app that you're able to use, and Codex, like, I can get the agent to post on my behalf.

>> It's part of humor. Humor is part of AGI. Is it funny?

>> It's pretty good. Yeah.

>> Okay. Yeah, it's pretty good at making — it's a lot of, like, I think humor is a really hard intelligence test, right? Like, you have to get a lot of context into very few words.

>> This is why 5.4 is such a big uplift for our varieties. It's the memeing.

>> Yeah, for sure. It's really cool.

>> So 5.4 can chip us. That's the takeaway.

>> Yeah. Maybe — maybe when y'all are done here today, ask Codex to go over your coding agent sessions and to roast you.

>> Love it. I'll give it a shot. Give it a shot.

>> Just coming back to the final point I wanted to make is — I think there are multiple other — like you guys are working on this — but this is a pattern that every other company out there should adopt regardless of whether or not they work with you. To me, this — I saw this and I was like, every company needs this.

>> I mean —

>> This is multiple businesses, what it takes to get people to "yes." Yeah, actually realize the benefits and distribute layer. And I think it sounds boring to people, like "oh, you know, it's for safeguards and whatever," but to handle agents at scale like you're envisioning here, I don't know if it's like a real screenshot, like a demo, but this is what you need. This is my original sort of view of what Temporal was supposed to be, like, you built this dashboard and you basically have every long-running process in the company in one dashboard. And that's it.

>> That's right. That's right.

>> Yeah, I think it's pretty customized towards every enterprise, right? Like, you care about different things.

>> There's a lot of customization, right? But like, I mean, there'll be multiple unicorns just doing this as a service. Like, I don't know. I'm very, very Frontier-pilled, if you can't tell.

>> Amazing. But it only clicked, cuz obviously this came out first, then harness, and then Symphony. And it only clicked for me that this is actually kind of the thing you ship to do that.

>> Yeah, yeah. There's a set of building blocks here that we assembled into these agents, and the building blocks themselves are part of the product, right? The ability to steer, revoke authorization if a model becomes misaligned. Like, all of this is accessible through Frontier. And there's going to be a bunch of stakeholders in the company that have the things they need to see in the platform to get to "yes." So we'll build all those in the Frontier so that we can actually do the widespread deployment. That's the fun part.

>> Yeah. I'm also calling back to — there's this "levels of AGI." I don't know if OpenAI is still talking about this, but they used to talk about five levels of AGI. And one of it was like, "oh, it's like an intern" and the coding software engineer. At some point, it was AI organization. And this is it, right? This is level 4 or 5. I can't remember which level — but it's somewhere along that path was this.

>> You know how I mentioned that my team is having fun sprinting ahead here, right? And we do this thing where we're collecting all the agent trajectories from Codex to slurp them up and distill them. Like, this is what it means to build our team-level knowledge base. You know, happen to reflect it back into the codebase, but it doesn't have to be that way, right? And it doesn't have to be bound to just Codex, right? I want ChatGPT to also learn our meaning culture, and also the product we are building, and how, right? So that when I go ask it, it also has the full context of the way I do my work. And I'm super excited for Frontier to enable this.

>> Yeah, amazing. What are the model people say when they see you do this? Like, you have a lot of feedback obviously, you have a lot of usage, you have a lot of trajectories. I don't imagine a lot of it's useful to them, but some of it is. You have this too — you deploy a billion tokens of intelligence a day. And this was at the beginning of '26. You're, you know, cooking.

>> Yeah, there's this fundamental tension which I think you have talked about — between whether or not we invest deeper into the harness or we invest deeper into the training process to get the model to do more of this by default. And I think success for the way we are operating here means the model gets better taste because we can point the way there, and none of the things we have built actively degrade agent performance. Because really all they're doing is running tests. And running tests is a good part of what it means to write reliable software. If we were building an entire separate ROS scaffold around Codex to restrict its output, that I think would be additional harness that would be prone to being scrapped. But yeah, if instead we can build all the guardrails in a way that's just native to the output that Codex is already producing — which is code — I think one, no friction with how the model continues to advance, but also just good engineering. And that's the whole point.

>> Yeah. So I've had similar discussions with research scientists, where the RL equivalent, on-policy versus off-policy. And you're basically saying that you should build an on-policy harness, which is already well within distribution, and you modify it from there. But if you build off-policy, well, it's not that useful.

>> That's right.

>> Super cool. Well, any thoughts? Any things that we haven't covered that we should get out there?

>> Just — I've been super excited to kind of benefit from all the cooking that the Codex team has been doing. They absolutely ship relentlessly. This is one of our core engineering values: ship relentlessly. And the team there embodies it to an extreme degree. To have 5.3 and then Spark and 5.4 come out within what feels like a month is just phenomenally fast.

>> This was exactly a month ago, 5.3, and yesterday was 5.4. I mean, do we have every month now is 5.5 nice? Like —

>> You know, I can't say that. The poly markets would be very upset, right? Well, I think it's interesting that it's also correlated with the growth, you know. They announced that it's like 2 million users. But, like, almost don't care about Codex anymore. Like, this is it. This is the game, man. Like, it's like coding, cool soft, like, knowledge work.

>> That's right. You know, this is the thing to chase after. And, you know, this is one of the things that my team is excited to support. Get the whole self-hosted harness thing working — which you have done — and like, the rest of us are trying to figure out how to catch up. But like, then do things, you know, right with you.

>> Do things.

>> That's right. You can just do things.

>> That's the line for the episode.

>> That's it. Any other call to actions? You're based in Seattle. Your team, I'm guessing.

>> New Bellevue office.

>> New Bellevue office. We just had the grand opening yesterday as of the recording date, which was fantastic. Beautiful building. Super excited to be part of the Bellevue community, building the future in Washington. And I would say that there is lots of work to be done in order to successfully serve enterprise customers here in Frontier. We are certainly hiring. And if you haven't tried the Codex app yet, please give it a download. We just passed 2 million weekly active users, growing at a phenomenally fast rate, 25% week over week. Please come join us.

>> Yes. And I think that's an interesting — I don't know, my final observation — OpenAI is a very San Francisco-centric company. Like, I know people who turned down the job or didn't get the job because they didn't want to move to SF. And now they just don't have a choice, right? You have to open the London, you have to open the Seattle. And I wonder if that's going to be a shift in the culture, right? Obviously you can't say, but —

>> I was one of the first engineering hires out of our Seattle office. So Seattle was very natural. Success has been part of what I have been building toward, and it has grown quite well, right? We have durable products and lines of business that are built out of there. Ton of zero-to-one work happening as well, which is kind of the core essence of the way we do applied AI work at the company — to sprint after it new, to figure out where we can actually successfully deploy the model. So yes, 100%. We also have a New York office, too, that has a ton of engineering presence.

>> Yeah, exactly. These are my road maps for AIE. Wherever people hire engineers, I will go.

>> That's right.

>> It's a cool office too. New York is the old REI building, I believe. The REI office.

>> Yeah, it's just — no, you'll never be as big. Right. New York is like, you can't get the size of office that they need. The New York — Seattle has a very, like, office mad-men sort of vibe. It's beautiful. The Bellevue one is very green, gold fixtures, very Pacific Northwest. It's a very cool place, which a lot of people are, like, there for. People like New York, they want to be in New York, right?

>> Yeah. We have a fantastic workplace team that has been building out these offices. It really is a privilege to work here.

>> Yeah. Excellent. Okay, well, thank you for your time. You've been very generous, and you've been cooking. So I'm going to let you get back to cooking.

>> It's been amazing chatting with you folks. Happy Friday.

>> Happy Friday.
