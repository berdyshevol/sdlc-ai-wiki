# Stop Shipping on Vibes — How to Build Real Evals for Coding Agents?

- **Source:** https://www.youtube.com/watch?v=VbX24V_JFQI
- **Speaker:** Jessica ("Jess") Wang — Brain Trust (eval and observability platform)
- **Event:** Coding Agents: AI-Driven Dev Conference
- **Date of talk:** 2026-03-03
- **Location:** Computer History Museum, Mountain View, CA
- **Organizer:** MLOps Community
- **Duration:** ~28 minutes (~24-min talk + ~4-min Q&A)
- **Channel:** MLOps Community (publisher of conference recordings)
- **Format:** Conference talk with audience Q&A
- **Companion slides:** `raw/slides/extracted_text.txt` (Wang section)
- **Source page:** [[coding-agents-conf-2026]]
- **CEO referenced:** Ankur Goyal ("Anker") — Brain Trust founder/CEO

---

## Transcript

> **Source:** Auto-generated YouTube captions, lightly cleaned. Transcript provided by user (2026-04-27). Timecodes preserved as `[m:ss]` markers for reference. Caption errors retained where they could distort meaning if "corrected" silently — see notes at end of document.

**[0:05]** All right. So, we're going to keep that applause going. Please give a warm welcome to Jess from Brain Trust. [applause] Thank you. Awesome.

**[0:23]** All right. Hi everyone. Um, so I'm Jess from Brain Trust. Um, I'm a bit shorter, so I'm just going to stand over here. Um, [laughter] so, um, Brain Trust is a platform that lets you do observability and eval tooling. So, pretty much in this talk, I'm going to talk about, um, what evals are, why they're important, and then I'll talk through a real life pretty complex eval that we ran a couple weeks ago.

**[0:52]** Um, okay. So, I have been in legitimate calls where um teams have told me that they've shipped AI features um either one because the engineering team told them that it was ready um or a PM tried a couple of prompts and they said it looked good. Um that's very problematic uh because you're essentially making ship decisions based off of vibes, which is not good. Um, ideally, uh, you would like to be able to quantify when you're shipping, uh, by saying things like, *"We ran 200 different test cases and 94 % of them passed and so therefore we're shipping it."* Or, um, to be able to say nuance things like, um, *we shipped this change and it improved the tone but decreased accuracy by 5 %.*

**[1:42]** This is why evals are important. Actually, can I get a raise of hands of how many people have heard just the term evals or — Okay, good. Okay, glad we're on the same page.

**[1:54]** Um, okay. So, evals are important for a couple of reasons. They can answer questions:

- Which LLM is the best choice for our needs? Um, especially when new models drop. This is always a big question in our minds.
- How does the AI perform across diverse real-world scenarios? So, for example, it could perform really well on Python codebases, but not TypeScript codebases. Um, it could do really well with English inputs, but not Japanese.
- Cost efficiency. Can we achieve high performance without excessive costs?
- Does the AI reliably reflect our company's voice and standards?
- Are we learning from users in improving iteratively?
- And how do we know when something breaks or gets worse?

**[2:37]** Um actually this is a really interesting real-world scenario that happened. So in April of 2025, so about a year ago, um OpenAI actually had to revert an entire model update um because the changes that they made um to make it more helpful actually made it too agreeable and therefore not very useful. Um and so this is an example of when it's very easy to overtrain models. Um and so you want to be able to catch these nuances early on.

**[3:11]** Okay. So there are four major parts to kind of creating an eval.

**The first is you have to create a data set.** So a data set is going to be a collection of test cases that you are going to pass into your system. Um these are usually going to be um your golden use cases, your edge cases and then failure modes.

**Um then you need to write a task.** So a task is going to essentially tell your system how you want it to behave when it takes in an input and gives you an output. So this is usually in the form of a prompt and then also picking a specific model to do this task with.

**[3:51]** Uh then you want to write a scoring system. So, um, for your scoring system, essentially, it is what tells you whether the, um, AI's output is good or bad. Um, there's a couple, if you've heard of them before, there's deterministic scoring, there's LLM as a judge, and there's human-in-review. Um, but essentially, you who are writing the scorer is um, defining the criteria of what comprises what good and bad is.

**[4:20]** And then the last thing is you want to experiment. This is the most fun part but essentially um one run of this specific configuration of your data set, your task and your score is equal to one experiment run. So as you are testing out different hypotheses and um trying to tweak things in your system these will all turn into different experiment runs.

**[4:44]** So then once you have a bunch of experiments um you can actually start to compare them. So um you can essentially see if there are any regressions or improvements across your experiment runs. Um and you can also click into individual rows to see which test cases have changed.

**[5:06]** Uh Brain Trust also has a feature called Loop which um allows you to query your experiments using natural language. So, um, essentially I can ask it, um, *"highlight problems in my experiments"* or *"highlight specific patterns that you're seeing in my experiments"* or if you ran a bunch of different experiments, you can ask it which experiment performed the best. Um, I was honestly really skeptical of Loop when I joined the company, but I use it a lot now. Um, mostly because traces — like long traces of like an LLM does a bunch of turns and it hallucinates or it drifts — is really really hard to manually read through. Um, and so I find that Loop is just better, it's faster than what I can do and it's better at detecting these patterns than I can.

**[5:55]** Uh, and then the last thing is you can log. So you can just wrap your code using the Brain Trust SDK and you can start to get live production logs.

**[6:04]** So the way that we chain this all together is um essentially you have some sort of application. So for example, let's say it's a documentation page with um a chat bot on the side where people can ask questions about documentation. Um so what happens is you have users or customers that use the chatbot or the chat panel. Um, and so they um you start to get live production logs that have the uh user question as well as what the LLM responded with um and then whatever metadata that you want to um pass into those logs as well. Um then you can take those logs and sample um 10 to 20 % of them depending on how much traffic you're getting in production and turn that into a data set. Um using that data set then you can start to write evals. So you can start to tweak the data set or tweak your score or tweak your prompt. Um, and you might try to write a prompt that is more concise or you want the AI to answer more enthusiastically um or things like that. Whatever you and your team um think is correct for a response. Uh, and then based off of how the evals do and what you learn from them, um, you will then bring that back into the app and ship code changes and tweak the app, uh, based off of what you learned from the evals. So that's usually how it works in a loop.

**[7:30]** Um, if you are the type of person who's taking pictures on your phone, this is the best slide in the deck. So [laughter] it's the one slide I did not make. So um but I — my coworker made this slide and it's just so good that our entire team has been using it over and over again.

**[7:48]** Uh so evals are a team sport. Um I really like this. Uh evals — uh on the right you can see they comprise of a lot of different steps. If you've ever done an eval before you'll understand that it's a living breathing machine and it requires a lot of um components.

**[8:04]** So um you have like the AI engineer that is bringing data to the platform as well as obviously making the uh bug changes and feature changes as well. Um then you have the product manager um who uh — you know if you work at Kilo Code it might just be the same as engineer because they don't believe in product managers but um — I mean the — sorry [clears throat] that was not — that did not — that came out aggressive. [laughter]

**[8:33]** Um but like they could be the same thing which is totally fine. Um but they are the people who develop hypotheses or um also tell you what the success criteria is. Um then you have subject matter experts um who help label the data or tweak the prompt. Um this is especially useful um I've seen in like medicine fields or law fields or insurance fields where they are very niche subsets of knowledge and you need subject matter experts to help you like label data. Uh and then you have data analysts that help you um define the scores and obviously analyze data. So evals are a team sport.

---

### Case study: agentic search vs vector search

**[9:14]** Okay. So now that we've kind of gone through a lot of the concepts of evals, um I thought it would be interesting to uh tie it to a real-life scenario, a real-life eval. Um so I wanted to talk about an eval that I ran to measure which one is better, agentic search or vector search.

**[9:35]** Uh this was actually an idea from our CEO, Anker. Um he often pings me with things I should eval. I do ignore him about 99 % of the time [gasps] but this one was interesting. So he is on Twitter a lot um and he sent our Slack channel this article from Cursor um talking about how um they use semantic search — also know I call it agentic search — um to significantly improve their coding agent experience or performance. Um and uh after a quick search online I did see there was a lot of discourse about whether agentic search or vector search was better. Um, and I just thought it would be an interesting thing to independently eval. So, we did that.

**[10:17]** Um, okay. So, because we were comparing agentic search and vector search, I just thought it'd be good to get us all on the same page about what vector search is. So, um, vector search is essentially the process of converting data — uh, like text or code — into numerical representations called embeddings. Uh, these embeddings capture semantic meaning. So similar items will live closer together in a very high-dimensional space. So if you look at the chart on the right, you'll see that um words like *wild west* and *broncos* are close together. Uh *basketball* and *soccer* are close together and *antelope* and *wildebeest* are close together. Um obviously this is a 2D representation but you can kind of imagine this in an n-space dimension. Um and then what happens is that these embeddings get chunked up and stored into a vector database like Pinecone. Um so for example, if I were to ask uh *"where does the database logic in my codebase live?"* Um essentially my codebase would be vectorized and embedded and stored into my vector DB. Uh and then the vector DB would find the closest embeddings that match my query. So words like *database* or *logic*.

**[11:35]** Okay. So then what is agentic search? Um also known as semantic search. Um so agentic search is what tools like Claude Code uses. Um and essentially what happens is the LLM has access to CLI uh command tools like grep or find, ls, cat, things like that. And it basically reads the code very similar to how a human would. Um, so it would search for a function name, open the file, read the file, sees that the file calls another piece of logic or another function, uh, and then follow that reference and repeat until it finds whatever it needs to. So it's more like how a real human would act. So that's the difference between agentic and vector search.

**[12:21]** Okay. So now that we understand the differences, um, let's build an eval to see which one worked better — or works better.

**[12:30]** Um okay so for this uh experiment design I created um two different data sets. So the first one uh was using Microsoft's TypeScript-Go repo. Uh essentially what we did is we pulled merged PRs from that codebase. Um anything with the word *"fix"* in the title. Uh and then from there we checked out the parent commit so that the codebase was in a known buggy state essentially before the fix. Um and then we used Claude to synthesize a bug description for that PR diff. So essentially we're trying to get like a format like a Linear task or like a bug ticket. Uh and that way we can uh pass it into the agent and tell it to find the bug and fix it. Uh, and then we used the Go test suite um as kind of our like — *if it passes the Go test suite then it passes the eval.* So hopefully that makes sense.

**[13:27]** Um, and then the second data set is essentially using the same thing but we basically pulled a couple rows from the industry-standard SWE-Bench Verified. Um, have people heard about — do people know what SWE-Bench Verified is? Okay, a couple less people who knew what evals were. It's — if you read like any sort of — it's it's what like Anthropic and OpenAI use to like benchmark their models. So it's like more of an industry standard. Um so we pulled uh 25 rows from that uh specifically from the Django related um data rows but the idea is the same.

**[14:03]** Um, and then the reason why I used two different data sets is mostly because I just wanted to have some variety and I wanted to test agentic search and vector search on two different uh languages and two different code bases. Um, so Django is much more of a massive legacy codebase and TypeScript-Go is newer and more modular. So I just wanted to see if there was any difference in how they performed across two very different types of code bases.

**[14:32]** Um, okay. So the next thing we had to do is implement vector search and agentic search. So implementing agentic search was really easy because uh Claude Code uses agentic search by default. So all we did was just set Claude Code on all of these tasks.

**[14:50]** Um for the vector search variant that was a little bit more difficult. So essentially what we did is we um implemented a basic vector search uh and had the agent call that through a script. Um but the problem was uh we still wanted to use Claude Code to keep the eval experiment as consistent as possible. Uh but the key constraint is we actually had to **prevent Claude Code from falling back to agentic search** which it really wanted to do. So this took like a couple of days. I had to um really block it from using agentic search um and try to call that vector search script every time. Um to do this we basically did two things. So I used um Claude Code's `--disallow-tools` flag to block any agentic search. So block uh calling grep or find or things like that. Uh and the second thing I did is I very explicitly said in the prompt uh that anytime it wanted to use search it should use vector search. So I believe this is a screenshot of the prompt I used. Um but yeah without these two things it would continue calling agentic search which would have uh screwed up the whole experiment. So we really had to make sure that it was only using vector search.

**[16:06]** Okay. Um one other thing that was difficult when we were doing this eval is um that Claude Code runs as a subprocess which means that the traces were orphaned and they weren't actually being connected to the parent trace um ID. So the fix that we did here was passing in the parent span IDs as environment variables so that the subprocess could actually attach itself to the right trace tree. Um if you don't know what that means don't worry I brought pictures.

**[16:35]** So here [clears throat] is what the trace looks like um before we did that fix. So you can see it says uh *"run cloud agent"* but you don't actually get any visibility into what the cloud agent is doing — like what it's actually trying to do.

**[16:54]** And here's what it looks like after we implemented the fix. So you can see that now every single LLM call and uh command line uh execution is logged in the trace here. So you can see it's calling Cloud Sonnet and it's you know running things like find um and read and things like that. Um and you can also see like in the LLM call like what is actually inputting and outputting um to the LLM. So yeah this was really critical for us to implement um because it allowed us to actually debug why certain things were failing or passing.

**[17:35]** And then in terms of the scoring, we just implemented kind of just one scorer um which is essentially *did the fix pass all the repo's existing tests*. So if they passed then the eval run got 100 % and if they failed um it got a 0 %.

**[17:52]** There is one interesting nuance here um for the SWE-Bench data set. Uh so SWE-Bench actually uh gave us a test suite called pass-or-sorry-called *fail-to-pass* um which is essentially um a list of tests that were failing before the fix but should be passing after the fix. But the interesting thing is if the fix passes everything in *fail-to-pass* but then fails another test that's not in that test suite um it still passes the eval because technically it did fix that specific issue. Um so that's just an interesting nuance I wanted to note there. Um and then we also tracked metrics like uh duration um total tokens and cost.

---

### Results

**[18:42]** Okay, so here are the results.

**[18:45]** Um, so for the SWE-Bench data set, which was again the 25 uh Django related code bugs, um the vector search got a 60 % uh accuracy. So it passed 60 %. Um and then agentic got a 68 % accuracy.

**[19:04]** Uh and then for the TypeScript-Go uh code bugs, the vector search and agentic search actually both scored 70 %. Um but as you can see here, um vector search spent a lot more tokens and money.

**[19:20]** Um when you look at these results, um — I — the one thing I'll note is I would take this with a grain of salt. Um, I highly doubt that vector search cost me over $4 per run because if you do the math, that's $40 and it didn't cost me $40. So, I — I think the exact cost is probably off, but what I would look at is the comparison between vector search and agentic search. Essentially seeing that **agentic search is X-multiplier cheaper.**

**[19:51]** Um, so another thing I'll call out is um the reason why I don't have the metrics for SWE-Bench is because I was running this eval last night and um it takes a really long time to complete and so I just didn't have time to get the numbers for uh SWE-Bench. But um yeah, doing this last minute.

**[20:11]** Um okay, so there are three main takeaways that I got when I looked through the results and also the the Claude Code traces.

**[20:21] First — vector search returns chunks, not connective tissue.** Um the first interesting thing was that vector search uh returns a lot of chunks of code. Um so in these chunks of code um there might not be like the relevant imports or relevant type definitions or the relevant um code uh calling code above it. Um and so essentially the agent doesn't get enough signal for what else to look for. Um so for example in the um SWE-Bench data set one of the runs um the agent made 26 different vector search calls um — essentially it was just trying to like guess and check so many times and it just couldn't find the right place in the codebase where the bug was happening. Um and the contrast is — you know in agentic search the agent can essentially look for the function name, read the entire file top to bottom um, see the import chain and then follow it and solve the task um a lot more quickly that way. So the way that I like to kind of think about it or conceptualize it is that **vector search gave the agent a lot of proximity to relevant code but didn't give the connective tissue between the code for it to actually implement a fix.**

**[21:39] Second — agentic search enables chain-of-thought exploration.** The second thing is agentic search um enabled or was able to do a lot of chain-of-thought exploration. So, it's kind of what I mentioned before where it's actually able to look at the function um and see what calls it and actually be able to travel to different files to follow the logic whereas vector search can't really do that at least in the traces that I saw.

**[22:02] Third — more searches = more cost.** Uh and the third thing is the more searches the more expensive. So the reason why vector search uh took so many more tokens and took so much more money is because um it was making so many more calls um because it just couldn't find exactly where in the code um the bug was happening. So that's why it was so much more expensive.

---

### Honest caveats

**[22:24]** Now um the last thing I'll say is **I don't consider this eval close to being done at all.** Like I would not publish a blog post about this yet. Um mostly because just from a gut sense I actually like — this eval basically is saying that agentic search is 100 % better than vector search which I don't think that's the case. I think there are places where vector search is better.

**[22:49]** And so something I would do is:

1. **Run multiple trials per task.** Um, LLMs are very non-deterministic and so I would not be surprised if I ran this eval multiple times with all the exact same criteria that it might have a difference of 10 to 15 %. So um that's one thing — that I would run multiple trials and kind of average um the scores across them.
2. **Improve the vector search implementation.** It was a very basic vector search implementation. So maybe that's why it's not performing that well. Um, I'm not an expert on vector search, but I do think there's things like um like chunk overlapping or splitting the text or retrieval models that can be implemented to improve vector search. So it might just be that my vector search implementation was just bad.
3. **Try a hybrid approach.** Um and then the third one, which is not really a blocker, but it would be interesting, is to try a hybrid approach. I do think a lot of companies now are doing a hybrid between vector search and agentic search.
4. **Expand the data set.** Um and then the fourth is to expand the data set. So obviously a data set of 10 — um, 10 rows — if it fails one of them, that's a swing of 10 % in the score. So just expanding data set, um adding more rows and also adding potentially more languages or more uh code bases.

**[24:12]** And that's it. That's kind of evals and also example of how to use an eval in real life. Um, yeah.

---

## Q&A

**[24:14] Jess:** I I think I only have one minute for questions. Um, but we can do like one or two if that's helpful. Um, yeah. Does anyone have any questions?

### Q1 — Token-cost confound from disallow-tools

**[24:34] Audience:** Hi, I uh I wonder if you did anything uh to to try and isolate or characterize the uh the token usage from restricting Claude from going into agentic mode.

**Jess:** Yeah. Yeah. Um that is — so that would be something I'd add to the improvements. It was something I thought of. Um the the short answer is no, I didn't, but I did think of it. That's um — so it was definitely something I thought could be inflating the token count. Um and so as I'm trying to iterate on this eval, I would definitely probably look through the traces — like the Claude Code traces — and see if it's um inflating the token count every time it's trying to essentially do an agentic call but can't do it and then has to switch over to vector. So yes.

### Q2 — Human control group

**[25:23] Audience:** Uh yeah. And one more question if I could. Have you run against uh human respondents — like having a human as a control group for uh for a similar set of questions or a subset of the questions that you're asking the AIs?

**Jess:** Wait, sorry, say that again.

**Audience:** As a control group for questions that you're asking AIs, have you considered asking humans for responses to those and measuring differences?

**Jess:** Yeah, that's a good question. So um the SWE-Bench data set actually comes with a *golden* answer. So SWE-Bench because it's industry standard already has like the answer key essentially that was like human-coded. So we could technically compare it against that human-like-golden — the answer set essentially — for SWE-Bench. For the TypeScript-Go ones, I guess technically because these are merged PRs, we can also just compare it against the actual fix from the PR. So I guess we could actually compare it against um the actual code and probably use some sort of like LLM-as-a-judge to see how close the code is. So I didn't — I haven't done that, but I think that's a really good suggestion.

### Q3 — Evals for short-attention-span / non-linear conversations

**[26:34] Audience:** Um first of all, thank you for the presentation. I'm curious about this. Um I I work closer to the users and uh one of the things that we are seeing as we're building a conversational AI product on top of data is that we are starting to deal with a lot more people who have smaller attention spans, and what that means in translation of the product is they will start a question for example thinking about *where can I get a matcha from*, there they will go to *where can I buy a Lululemon*, from there they will go to *the latest price of Tesla*, from there they'll go to something else about, you know, *Elon Musk's latest conspiracy*, whatever. Now what I'm curious about is it is becoming increasingly harder for me to think about evals in that perspective because the idea of a golden data set suddenly doesn't make sense to me. I — it's impossible for me to emulate the thought of this person. I've thought about maybe getting a synthetic uh agent to like think about this, but for a case like this where there's no going to be — there's not going to be a straight chain of thought, there's not going to be a consistent golden data set — how do you think about evals, and is this something that you may have published that we should probably be thinking about or reading about?

**Jess:** Yeah, definitely. So, I think if you are seeing it in your application — or if you're seeing it in whatever product that you're building — um that's enough, because essentially you should be able to log that and turn that — and add that to your data set. Um, so if you're seeing people who have short attention spans or are jumping through different questions or different parts of your app, um, that should be logged somewhere and you should be able to turn that — uh, add that to your data set. Um, so that'd be my answer. Um, then from there, sure, you can use AI to add more synthetic uh rows to your data set based off of that. But I think that's the biggest thing — is just to **turn your actual user journey into just something in your data set.**

**[28:31] Audience:** Yeah. Okay. Awesome. Yeah.

**[28:33] Demetrios:** Thank you, Jess. [applause]

**Jess:** Thank you so much.

**[28:40] Demetrios:** How are we doing right now? Quick vibe check on the floor. How's it going? We're doing all right. Yeah, I like that. All right, we got some good energy in here. That's cool. Good people. So, spoiler alert, that was me on your app there earlier, my man in the front row. Uh, I'm your problem. So, we can talk later. I could tell you too — much TikTok is the answer.

---

## Transcript Notes

- **"agentic search ↔ semantic search"** — Wang uses both terms interchangeably throughout. In her usage, *semantic search* is the marketing term Cursor used; *agentic search* is the practitioner-friendly framing she prefers (LLM-driven CLI exploration via grep / find / cat). Note this differs from the wider field, where *semantic search* often refers to embedding-based search (the *opposite* of what she means).
- **"$4 per run / agentic is X-multiplier cheaper"** — Wang explicitly disclaims the absolute dollar figure as miscalibrated (*"I highly doubt that vector search cost me over $4 per run"*) and asks the audience to focus on the *ratio* instead. The slide-deck summary records this ratio as **agentic used ~3.1× fewer tokens and cost ~2.8× less** on the TypeScript-Go data set.
- **OpenAI April 2025 sycophancy rollback** — A real event. OpenAI rolled back a GPT-4o update that made the model excessively agreeable. Wang uses it as motivation for "you want evals to catch these nuances early."
- **"Anker"** — Wang's CEO, Ankur Goyal (founder of Brain Trust). The transcript renders the name phonetically.
- **"if you work at Kilo Code it might just be the same as engineer because they don't believe in product managers"** — A live cross-reference to Scott Brightenother's earlier Kilo Code talk (same conference, same morning). See [[coding-agents-conf-2026]] / `raw/youtube-transcripts/breitenother-kilo-25t-tokens.md` for the source claim Wang is teasing.
- **"Connective tissue"** — Wang's key metaphor for what vector search lacks: *"vector search gave the agent a lot of proximity to relevant code but didn't give the connective tissue."* This phrasing **independently echoes Murat Aslan's later use of the same metaphor** for spec-to-code traceability ([[agentic-coding-stack-aslan]] — *"the most strategic connective tissue in the agentic coding stack"*). The two uses are scoped differently (Wang: search-time code traversal; Aslan: spec-to-implementation linkage) but suggest a shared concept emerging across the 2026 agentic-coding discourse.
- **"Demetrios"** — Demetrios Brinkmann, founder of MLOps Community and conference host.
- **`fail-to-pass`** — A SWE-Bench Verified concept. The dataset provides a list of tests that were failing on the buggy commit but should pass after the canonical fix. Wang's scorer accepts a fix if it makes all `fail-to-pass` tests green, even if it incidentally regresses an unrelated test in the existing suite. This is a deliberate eval-design choice and worth noting for anyone replicating SWE-Bench-style scoring.
