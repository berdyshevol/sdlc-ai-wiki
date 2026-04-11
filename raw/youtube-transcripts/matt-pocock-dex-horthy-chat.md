# LIVE: Chat with AI Coding Wizard Dex Horthy

**Video:** https://www.youtube.com/live/NKu3T9FUjmU  
**Host:** Matt Pocock  
**Guest:** Dex Horthy (HumanLayer)  
**Date:** 2026-01-17  
**Duration:** ~46 minutes  
**Source:** Auto-generated YouTube captions, cleaned. Speaker turns split on `>>` caption markers. Speaker labels are not reliably attributable from auto-captions; treat sequential turns as alternating between Matt (host) and Dex (guest), with occasional misalignment.

---

## Transcript


**[00:00:00]**

> Amazing.

> I think we're Yeah, we're definitely on.

> What's up, folks? I'm here with Dex. You prefer Dex or Dexter?

> I go with either. I'm very, you know, they say good engineers are lazy. Dex is half the syllables, so I go with Dex off often.

> Very good. Yeah. Jit the T, I suppose. Um,

> yeah.

> Uh, I'm Matt PCO. Um, we're going to talk about I mean loads of stuff. Basically, I had I watched Dex do a really great talk at AI Engineer. I don't know when you gave the talk, but it came out like a month ago on YouTube, let's say.

> Yeah, it was like late November or something, I think.

> Yeah. All about [snorts] Ralphing, I suppose, finding ways to make AI coding actually work inside organizations. And it just sparked a huge fire in my brain, and I needed to um I guess douse the fire with gasoline. So, Dex, you're here. Uh, and I just want to like talk about all this stuff really. [snorts] Uh, I don't know if I've literally just signed up to a like chat service so that I can talk to Deck. So, I just want to get the chat open locally.

> Let's do it.

> Um, let me have a look. But why don't you introduce yourself for the folks just while I'm doing this little bit of admin?

> Absolutely. Um, what's up y'all? I'm Dex. Uh, I do a lot of ranting and raving about coding agents and how to use them. And, uh, I spend a lot of time going to battle with the slop AI hype machine and try to really focus on what actually works and solving hard problems. And uh I think the most exciting parts are around like you know a lot of what we do is still software engineering and there's a lot of engineering to be done and just because the API just because the AI writes the code for you like doesn't mean that you don't that you don't have to think and that you don't have to be thoughtful about systems and how do we how do we how do we uh optimize the the the engineer AI collaboration so that we're all spending time on the highest leverage ideally most exciting and fun part right uh of of building which is like shipping and designing systems and solving hard problems.


**[00:02:11]**

> Yeah, I am like so I my YouTube channel was primarily a TypeScript YouTube channel. I'm still fascinated by TypeScript. I still freaking love TypeScript. I built my career on

> Can't imagine why.

> Yeah, I I mean just like it, man. And I I've been posting more about AI recently, you know, for the last year or so. I've came out with a course on AI and stuff and um so much of what I see on YouTube and weirdly not on X at all is like AI is slop, right? AI it just produces crap. It's just there's there's like the the content is slop or the the video itself is just AI generated and it's I someone made a video about human layer and they're like human layer is insane and then you watch the video and it's just a guy scrolling. It's like an AI browsing agent scrolling around completely irrelevant GitHub issues that have nothing to do with what he's talking about and nothing to do with anything that we've ever done. I'm just like

> this is P. I mean like if you if I turned this on and I wasn't paying attention I'd be like wow someone made a video about our stuff and then you look a little bit more closely and you're like

> nothing here is well thought out. Like nothing here makes sense. It's just like feed like feeding the AI content machine. But so people take that though, they take that opinion because there is real slop out there and then they put it on all code, right? So any code that is created by a must be slop, right? And I kind of want you to say upfront like that's not true, is it? Like from what you're seeing out there, AI can actually produce decent quality outputs.

> Yes, AI can make very good code. Um you have to wield it, right? As uh Bang from Source would say, it's like you have to know how to hold it. Uh, and you have to do some if you if you've never written code before, it's going to be hard to get AI to write good code. Um, and it's going to be hard to know whether the code is good or not. Uh, so it's like and I don't want to like I I think Vibe coding is super interesting and it's incredible. open doors for lots of people to be able to do things. But like what we're really really focused on is like how can we give tools to the like staff and principal engineers at companies with millions of lines of code and thousands of engineers and enable them to one actually do their job faster with AI two to 3x faster on most things is kind of like what I think is bestin-class right now for brownfield code bases and also like how can you build practices and platforms and systems that enable like some kind of standardization across a team and across an org because even if you have a hundred engineers and they're all really good at shipping really high quality code with AI, if they're all doing things in different ways, then you're going to end up with chaos anyways, even if all the code is like peak like the exact same code you would have written by hand, you know, three times slower.


**[00:04:59]**

> Yeah. Um we should give you a chance to plug as well. So like what are you working on right now? What are you building? Let's give you a chance to plug at the beginning of the end.

> We'll do a little plug. Uh yeah, so we're working on um it's it's very early. So we shipped we launched in like September an open-source IDE for managing lots of parallel cloud code sessions. Um it's called code layer. Um I' I've said this publicly once or twice now, so I guess we could pop it off again is like there is a wait list for it, but it's also it's open source, so you can go build it and and play with it yourself. The wait list was we like to joke the wait list was a little bit of a scop of like if you can't go to the GitHub repo and figure it out like we're probably like not ready like it's an early product and so it's like I'm I'm I I'm very excited for all the you know thousands of people who have gone and figured it out and showed up in our Discord and sent us PRs and things like that. We've basically in the last six weeks taken everything we've learned trying to roll that out to customers and um rebuilt the entire product from scratch, redesigned the it's funny I six months ago I was giving this talk about research plan implement. I was like look the the the magic is not in the prompts. There is no perfect prompt. Like the thing you should understand is like context engineering and intentional compaction and really being like again intentional about how you manage your context windows and stuff. And I said these exact words. I was like the words won't be research plan implement the prompts will be different there might not even be three steps there might be six there might be two I don't know what's going to happen in six months this is like me like giving paying my respects to the bitter lesson or whatever it is


**[00:06:29]**

> and then we woke up in the middle of December like you know what RPI is not enough we actually need six steps and like just based on like okay how how do we help people like what are people pick up these prompts and they try to use them and if you use them for a thou you put in your thousand hours you can get incredible results results. Uh we saw lots of people would like try them, get really good results, give them to their team and their team would have a vast spectrum of quality of results. So we're rebuilding the workflows and then we're it's more steps now. And so it's like okay, I don't want to ask someone to learn how to wield six prompts. Three was already a lot. So, how do we rebuild the product around um more guided workflows and basically splitting up these very long um if you read the create plan prompt that's in the open source repo. Have you have you tried it?

> No.

> Okay. I've not tried it.

> So, there's a there's a prompt you can use. It's slashcreate plan and it has about 50 instructions in it. Um, and it's basically like a thing that I went up in June and talked about 12 factor agents and it was like don't use prompts for control flow. If you know, excuse me, if you know what the workflow is, use control flow for control flow because it's going to be much more reliable. It's guaranteed that things are going to happen in the order. So, we split up the planning process into multiple steps. Um, and so the deterministic code that wraps that and guides the user through those steps, um, is like I think we're really obsessed with getting really really tight and really really well. So that it's your chance of getting really good results and the parts of the conversation that you're involved in like the things you have to do are the interesting most high lever things you can do versus like well if you don't sprinkle in these magic words at this part of the process it might not work as well you know.


**[00:08:08]**

> Yeah. So it sounds like you are close almost as close as humanly possible atomically to like people actually doing this in the wild and trying to solve their problems basically is like getting AI coding agents to behave properly and teaching people how to hold it right and building a product that helps people hold it right and that is I think where I want to go today which is like how do you hold this thing right you know what I mean

> like that's the question right now and

> okay

> why don't We do a little bit of like scene setting which is one thing I really love from your talk is that you talked a lot about the constraints that LLM have and that you have to work within those constraints. Specifically, you say that there's like a dumb zone and a smart zone, right, in terms of context.

> And what I might do is I might just sort of do a bit of live diagramming. And

> let's do it.

> You do as we go.

> I'm a draw of

> I've been meaning to switch over. I

> I think Excala just looks like um like I've said this publicly before. I think it looks like the scrawlings of a serial killer and I think [laughter] that TL Draw Hang on let me Yeah, you can edit that. I think

> Oh, yeah. You dropped me a link. Amazing. Let's do it.

> And T because I know

> you changed all the hot keys in TL Draw and so I'm going to have to relearn. I'm going to be a little slow but uh

> so I think

> Hello. Is this going to work? Oh, no. I'm not actually sharing my screen. That's what I'm not doing. Hang on. Here we go. Entire screen. There we go. Hello. We're here.

> We're in. Amazing.

> Oh, hi. Oh, you're literally here. Awesome.

> All right. So, LM have a context window, right? They've got, let's say, this is the context window and somewhere here is like a smart zone and a dumb zone.


**[00:10:01]**

> Yep.

> Right. Let's say the top bit is the smart zone and bit here is the dumb zone. What is what does this mean like concretely to people who are doing this stuff? Um yeah I mean so it's like be before coding agents we would we would just like the answer was like you will always get better results the less context you use right and the way we think about like a tool calling agent is you're always just in a loop you are taking this con whatever so like whatever's in your context window in the first place um so let's put this here so you have your let's see how much did they change the hotkeys do uh you have your like system message and then you have your like built-in claude tools like uh agents and tasks and read write uh edit all that stuff. You have like whatever's custom MCPS you have in or the tool search thing but like um what you know custom MCPS is no longer as much of a problem. I haven't messed with the tool search but the promise of it seems like it'll probably work pretty well.

> Yeah.

> Uh and then you have your like custom instructions, right? your claude MD or your agents MD or whatever it is. This is I'm gonna talk I'm gonna use a lot of cloud words, but this is true for no matter what LLM you use. Like they all have quadratic attention. They all work in this way. Uh and then you're going to put in, you know,

> just to pause you. I'm going to pause you a lot, I think, which is Could you just explain quadratic attention to me? What does that mean? Uh yeah. So that's basically um the idea that the more the longer your context window um the amount of basically like the amount of compute and like the quality of like the responses that you get from the LLM um the amount of like I don't want to say compute intelligence required increases quadratically with the number of tokens. And so if you have five tokens uh and you go to 10 tokens, the 10 tokens is going to be you double the number of tokens, you four times the amount of um computation that's needed to ingest all that context and actually like act on it.


**[00:12:06]**

> That sound right?

> Yeah, that's right. And that's per layer and per attention head too, right? So that is just going crazy, you know, and you can have like 50 80, you know, this these numbers aren't public, but it just goes nuts. every single token you add quadratically scales into oblivion and it's uh makes it really dumb.

> Yes. And it's like a lot of the benchmarks for long context are about this like they've run on this thing called needle in a hay stack which I think is not actually useful. I mean Jeff Hley was talking about this the Ralph guy was talking about this in like March or April of like needle in a haystack is not useful because most of the time you don't need to read you know a 100,000 words and pick the one sentence that matters. you need to read a 100,000 words and act on all of the information that's in there or you know tease out the 50,000 words that actually matter. Uh and that's a much harder problem that we're not as good at benchmarking. I mean people are working on benchmarks for long context agents and stuff like this. But um yeah, back to the back to the context window thing though. Um are are you ready to jump back in? Does that sufficiently answer the quadratic attention question?

> You did it wonderfully. Well done.

> Amazing. Um, so we'll have like your user message comes in here, right? Is this okay? That's great. Now, um,

> you over here with the T draw choice, haven't I?

> It's okay. Um, I'm I'm ready to rock with it. It's about time I learned it. Um, the agent's going to call some tools. You're going to get some uh let's see, you're going to get some tool responses. This happens, you know, many, many time. If you're like, what's in the readme of this project? That one's pretty easy. Um, and then you eventually are going to get back some kind of like assistant response, right? And your your dumb zone, smart zone has uh is is smaller, but uh this is not to scale. Let's put it that way. Yeah, this context window is much longer.


**[00:14:00]**

> Yeah.

> At some point, you're going to like run out of room in the smart zone, right? Like you will continue going down, continue sort of long longass contacts, and you'll hit some sort of barrier.

> Yes. Exactly. Um, and so the idea, yeah, the idea here is, uh, there's lots of different ways to use a coding agent. Um, the most naive way is just to pop it open, ask it for some stuff, when it finishes that stuff, ask it for some more stuff. Uh, and basically like the there there's the I also like the smart zone dunzone I think is is a rule of thumb like 40 I always say like 40% context usage and like that's based on how I count tokens. Like actually the way I count tokens and the way we count tokens in rip tide is slightly different from the way the one you get default in cloud code because they include the like end buffer in their percentage calculations as far as like they don't actually count that as available

> not quite relevant. The point is the number doesn't really matter is like the way to really understand this is like for different types of work and different types of tasks uh the number of changes it's flexible um but the more context you use the worse results you'll get basically

> and I think the important thing is the paranoia right like is the feeling of I should be worried about this or I should be thinking about this and trying to optimize for it right

> yes and basically and the idea there is like every time you're about to send a new message you should ask yourself the question like could this be a new context like is the information and sometimes I'll keep it right sometimes like well there's a lot of good information in here and I don't really have the patience to wait for the model to go read all those files over again in another context window or to have it like hey I or I don't have the confidence that it will be able to like accurately summarize everything we have so far so that I can onboard the new context window but you should be asking yourself every time like should this be a new user message or should this be a new context And the hope, I suppose, is that you're not needing to ask yourself that, but you're designing systems and harnesses in a way that you optimize for the smart zone and avoid the dumb zone, right? And that kind of leads us into Ralph, [laughter]


**[00:16:08]**

> right?

> I love it. Yeah. I mean, right? So, yeah, Ralph is a system that optimizes for always working in the early part of the context window and doing so I like to think of Ralph this is I' I've talked about this a little bit before. I like to think of Ralph as like a control loop. Um, have you ever like spent time in like the Kubernetes world?

> Me? No, I've not touched it once.

> So, the way it works is it's built on control loops which is a really simple like your thermostat is a control loop, right? You read the current state of the world Oh my god. All right. This is not a TL draw thing. I just can't type this morning. [laughter] Uh, and then you read the desired state of the world and then you take some action and you just do this forever. Like you just take take action to advance the current state of the world to the desired state of the world. Let's see. Yeah.

> Okay, that hotkey is the same. Nice.

> And you just do this in a loop forever, right? And so when I think of like Ralph, I think of Ralph the same [snorts] as a control loop um where you have your system prompt, your built-in tools, your cloud MCPs, and your user message is like telling it to read a couple files and then what gets pulled in is basically the specs which is your desired state of the world. You have it look at source which is the current state of the world and then you say implement one thing, right? Yeah.

> And the goal when I think about the smart zone like the most practical advice I can give you is like figure out a task that is and this one thing like sizing this thing is important because you basically want to be able to do your like edit edit edit tool calls and then you're going to verify as like you know run the tests or run the llinter or whatever it is. Maybe it was broken and you run a couple more edits


**[00:18:01]**

> um and then you run the test [clears throat] and it passes. And basically when I think about like task sizing or like if you're doing a more like like oneoff like planning and you're not doing Ralph forever, you want to be able to do your task should be sized that you can like make the changes, run the tests, fix any issues, run the tests, and then like do the you know commit and push or whatever it is all before all like in as little context as possible, right? There's trade-offs because if you make the test too small, there's like, you know, you change one file and you change the signature of a function and then like the test won't pass until you change the other file. So, some of these like change you can't just do one edit per per loop. I think someone were you the one talking about the cursor one where it was just like the the loop was someone was on X talking about like the loop was too tight in some implementation of Ralph.

> So, this I kind of think of it like you've got

> you've got some amount of water, right? And you need to like

> you can't fit all of this water in a single cup, right? And so you need to put it in multiple cups. And I think what people don't realize is that the cup is smaller than you think it is, right? The agent has less available to it than you think it is. So, and that's a really interesting question. I mean, there's there's so many interesting questions with Ralph.

> Yeah.

> Like,

> and you have a you have a lot of levers you can pull. Like, can we pull up the whiteboard again?

> Yeah. Yeah. There you go.

> Yeah. So, like you have here you have your specs. You can you can make the specs smaller and tighter. You can find a way to like give it better ways to traverse the source so that's not taking up too much. You could rip out some of your custom MCPS. You can disable some of the built-in tools. Like you have lots of and and then it's like, okay, like how big is this task? And this is probably the highest leverage thing you can do. But again, it's like you have lots of leverage you can pull to control what goes in here and like how big your tasks are and like how how how far what is your average context length. That would actually be really interesting. If I were going to build like a Ralph tool, part of what I would build is like give people visibility and metrics into how much of the context is being used by each thing so that you know which place is kind of your bottleneck and you know you get to the end of the loop how much context was used at each loop as it's exiting right and you can chart that per iteration and then understand like oh this is always making it to 60% context I need to make my task smaller.


**[00:20:30]**

> Yep. That's one thing I find I mean we can get into this later but that's one thing I find really tricky with implementing this like myself locally is that the observability is so bad right like I don't get any real stats here

> um but let's let's keep it at a high level for now which is

> you are cons like you're trying to build a system with Ralph Whoops I just completely knocked you off um

> that's okay

> with where you're just trying to fill each cup a little bit right so that it has room in the cup to do tests to do um check the uh uh state of the world with a player MCP or something.

> Yeah.

> And sizing the amount of water that you put in is is like is mostly the whole game.

> How though, if someone's like going, "Okay, I like the sound of that. Um I want to run an agent in a loop to just like do some tasks." How do they integrate it into their organization? Like what's the one small thing they can do to like, you know, because because all we're doing here, it sounds stupid Ralph Wigum, right? But all we're doing here is we're just running the tools that we have already like clawed code in a loop, right? That's all we're doing.

> How do you get that into an organization just for yourself to try things out? How do you set it up?

> Yeah. Um, so there's a bunch of ways you I mean like the literal exact steps that I end up doing is like I don't know I had this I tell the story at some point um but we had like I was sitting with one of our front end engineers uh who was going through a bunch of React code and we were like trying to debug something together and he said like h this code is like it needs to be refactored. We need to refactor. like, "Okay, great. You go fix the thing." And like while we're working, I'm kind of like on the side. I'm like chatting back and I spend like 30 minutes going back and forth with Claude of like, "Build me the world's best React style guide." And it came it read the code and came back with a bunch of questions like, "Do you want to allow barrel exports or you want to do something else like do you want to use use effect or do you want to use like Zustan stores?" Like I see all these different patterns. Which ones are the right patterns? spent like 30 minutes going back answering. There's came back with like 25 or 27 like React rules and I kind of shared the PR and you can put it on the video in the show notes or whatever because PR I'll get to why the PR never got merged but uh you came up with these rules. I spent another 30 minutes with with the front end engineer and we like went back and forth iterated a couple of them and then we dropped that in a repo and we did a Ralph loop that was basically like I set up a GCP VM I turned on a T-Mo session. I grabbed this like style guide and I made like a slight variation on Jeff's prompt, right? Because Jeff's prompt is like read the specs and implement them. In this case, the the desired state of the world was all the code aderes to the style guide.


**[00:23:05]**

> Yeah.

> And the instead of an implementation plan, it was like a refactoring plan.

> Yeah.

> That was our like our our like artifact that we're iterating over and has all the tasks. And this this thing went and churned for about six hours. I checked on it about six hours later and I started to see the messages like hey we're done like I guess I'll do this too and I'm like that's when you know like Jeff always talks about Ralph being like underbaked versus overbaked

> or like you think about like when you when you train a machine learning model you usually like overfit it and then you roll back to the checkpoint that is actually like the right amount of like model fit. Uh with the same thing is like if you leave it going too long it will come up with more stuff to do. These models are like trained to like if user asks you to do something like find a way to be useful, right?

> And to come go to like for a second which is like the way this works like in the implementation is at least the way I've sort of seen it I think it was in the original article maybe and the way I've implemented it

> is you run it in a bash loop and then you say you tell the LLM when you're done emit some sort of sigil that I can then read from your output and then stop the loop, right? And you specify some I've never I've never done that part. That's what the anthropic plugin does. I

> I don't know. I

> I haven't explored that. I think the part of the joy of Ralph is kind of just like let it go and like it's on you to check on it and like you can always roll it back and experiment with the out. But like this is one of the exciting things is like I don't know if you look in the cursed lang repo which is the programming language that Jeff made with Ralph but like you see all kinds of weird emergent behavior like it dumps hundreds of markdown files everywhere as part of its work. Like you never told it to do that but here um is it is it gonna let me share my screen? Let me see if I can

> uh it may not it it may actually it may

> uh while you're doing that I'd never thought of that. I I'd literally never thought of not stopping it, you know what I mean? Like this is this is like I suppose nervous me not wanting to spend too many tokens or something, but I never thought of just like letting it run and run and run.


**[00:25:10]**

> Let's see here. Maybe I can Yeah, let me see if I can share this. Yeah, because

> let's see. Share screen. Let's share We'll share the window. That's fine. Um, so here's the cursing repo. And so this is the thing that Ralph ran in for a very long time, for like weeks and weeks and weeks and weeks and weeks.

> Yeah.

> Oh, interesting. It looks like it's been cleaned up a little bit. Um, if you go to like earlier commits here, you will see probably uh let's just go back to like here.

> You bump the size of the uh uh font a little bit.

> Yeah. Yeah. Yeah. Yep. Um all right. Maybe we can go to the Rust branch. I don't think this one ended up getting cleaned up as much. Um, interesting. Okay. Uh, if you looked at earlier versions of this, there were just like a hundred like markdown files, all caps, of just like work in progress of Claude just like spinning out like thoughts and ideas and documentation and things like this.

> Um, but there's this you get these emergent behaviors and Jeff had this thing too. like, oh, I left it running too long and it decided it needed like it just came up with more stuff to build. It was like, okay, I think we should probably also have this programming language should [laughter] have support for postquantum cryptography or something like this.

> And so, like I kind of think like part of the fun of it is like

> underspecify a little bit and see what happens. Obviously, like if you want really good working production software, you should specify as much as possible,

> but

> yeah.

> Yeah,

> that's that's kind of where I am. That's like cuz I I'm seeing this as just a way that I can do my work basically and like with that

> with this idea that that I have and I suppose I don't know I don't know even where I picked that up whether that that is from did I pick that up from the Ralph plugin? I probably did didn't I? Um


**[00:27:01]**

> they have the like completion promise and the max iterations.

> That's exactly what I do. That's exactly what I do. So that felt natural to me because what I wanted to do was

> choose a scope of work up front that was super well defined.

> Um, and then just let Ralph find its way to the end.

> Whereas what you're talking about there is kind of like choose an underspecified amount of work and just let Ralph play in this zone really. And like what's

> to me it feels like my version you get to that's a lot of upfront work for me basically but it's kind of work that I want to do because I want to sharpen my ideas. I want to describe the desired state of the world really clearly.

> But yeah I'm just interested in your thoughts there like what use cases do you see for like an underspecified Ralph versus a oversp specified maybe Ralph? I mean, I will also say like I've run Ralph on a pile of spec. I've had Ralph write the specs. I've been like, "Hey, go read all this documentation for this product and then extract out the like clean room specifications that define actually like how this would work from scratch, no implementation details, and then you run Ralph on the specs." So, you have like one Ralph is like building the specs and another Ralph is reading the specs and then like I think it was like add AI features. And so it was like having another directory full of specs that are just like literally copy and pip. It's very like almost like lispy or like pipeliny where it's like you have a Ralph that's taking the internet and turning it into specs. You have another Ralph that's taking specs and turning them to like what would this product look like if it had more AI and then you have another one downstream that is like reading those specs and turning them into working code.

> Yeah. Wild. Okay. I guess

> it didn't it didn't go great. I didn't read the specs and I got a thing that I like didn't love. And like that's part of it too is like

> I think Ralph is like probably not the right final answer for how we build production software. I think it's probably it's if anything it's like an incredible lesson in how context windows work. And that's kind of I think what Jeff runs around doing is like don't use the Andropic plugin. Learn the theory because the theory is actually what makes you a better AI and like coding engineer. And you should still use it but you should understand why it works so well. Well, so let's define Ralph as that [clears throat] kind of wild free form like play around idea. Sure. There is an idea here though, right? Like running something in a loop that is really specified and tight, right? And that sounds like if that's not Ralph, then that's I don't know something else, right? But how do you when you're talking to people who are doing this and like they want longunning coding agents to just run AFK, what's the structure that you recommend if it's not Ralph?


**[00:29:50]**

> Um so so that part if you're doing like full AFK like this refactor plan like I can finish like talking through how we did this and like

> what I would do. The PR didn't get merged. Um actually here I can pull I can pull it up and show it to you. I think that would that would be um probably an interesting thing to look at. So, we'll go to poll requests. Close. You're going to like the name of this one, too. [snorts] Uh this was very low effort. Um here it is. Ralph is back.

> Ralph is back.

> So, this is 20 commits over six hours. Um here is the like React coding standards doc that I made with the engineer. Here's the like you can view actually the refactoring plan that it used to like track all its progress. You see the rich div.

> Um so it's like cool. We consolidated all the custom hooks. We added error boundaries everywhere. We made sure that we used proper form states and just like did all this stuff that was in our spec.

> Uh this didn't get merged. Um the reason why is because it's you know thousands of how many lines is this? Let's go back to the top. It's uh yeah 20,000 lines and some of that is the plan files and stuff but like


**[00:31:03]**

> I was like this was a cool experiment. I said to the engineer he looked at it two days later and there was a hundred merge conflicts and I was like okay that's fine. Like we'll go do this later. Like you could always just like rebase route, right? The nice thing about Ralph too is you can just like control C it throw away all the code and just like same specs like update the code and just run it again and it was so low. It was like took 10 minutes to set up the GCP instance and then took 10 minutes to turn it off later. Yeah.

> Um I think if I was going to do something like this in a company for real and like a thing we've experimented with internally was a lot more towards um do less like Ralph is a cool like current state of the world desired state of the world make one change. Um I deployed something like this for a internal repo that we have and I set it to only run I run it on cron every night and only run three iterations of the loop. I want every morning to wake up to like the codebase just for free. I just get the codebase is a little bit better.

> And [clears throat] we didn't merge all those PRs, but every morning we wake up and just be like, oh yeah, this is this is great. And I the specification is just here's how I want the codebase to look. Here's how I want it to be architected in the end world. And Ralph just kind of does these little increments. Uh so my advice is do not send your co-workers 20,000 line PR that refactors the entire codebase. That will not work in the real world. But you can use the concepts and it's like a building block that you can use to kind of hands off, don't think about it, just run it in a GitHub action every night and and and see what you get.

> Yeah. One thing that I'm thinking about actually I was going to give this a go actually before we started but we started early so I didn't get a chance but I have a um a couple of open source repos and I just don't get time to like uh triage all of the issues that come in basically. And so there's an extremely simple Ralph loop here, right? Which is you just feed all the issues into a loop and you get it to work out whether it's I you can categorize it, right? You work out whether it's a feature request which there's no real action to be taken or you like get it to make a reproduction of the bug or something and then you maybe feed that to something else that another Ralph that's looking for a GitHub label or something to actually fix the bug to make a PR. There's just like a a workflow pattern here, right? Like


**[00:33:17]**

> Yeah. You managing little cues and then Ralph's different Ralphs different prompts are appropriate for different cues.

> Yeah. And you tune those prompts with a bit of like sitting on the loop and watching what it's doing. And then you let it go AFK overnight as you're kind of describing basically. And I suppose like not too much at once is the way of thinking about it. I will also say you should be careful with taking GitHub issues from the community and feeding them to a claw that is in dangerously skip permissions because it's technically untrusted input. So like we have a Ralph that runs through our linear queue, but it is not allowed to see anything until we like look at it and look for hidden prompts in like HTML markdown comments and all of this stuff and make sure okay this is actually okay for a model in DSP to to process. Go. Yeah. Yeah, that makes total sense. Okay. So, assuming then that you've got this loop set up, what are we talking about in terms of like task size? Let's go there first. Like, is this like when you're prompting Ralph?

> Yeah.

> The the the really nice thing I love about Ralph is that it frees you from the burden of choosing the next task. If you've just got like a huge wge of issues or something, you can like, you know, as long as they're correctly described and you sort of have the dependencies all mapped out, then you can kind of just let Ralph do its thing and choose the next issue and then just go from there, which is just so nice. And how like when you're telling Ralph how big a change to make, what are you saying to it? What are you like are you trying to get it as small as possible or what do you think? So yeah, and and like in production and like the the tools we use are a little more human in the loop again because it's like the hardest the hardest software problems in the world are not going to be done completely autonomously. They're going to be done very much in collaboration with humans. But I think this this advice is true in both worlds, which is like when you're designing a plan, whether [clears throat] it's a plan you're going to give to Ralph or you're going to plan, we we have a separate prompt that is basically like runs a parent sub agent, runs each task in a sub a sorry, a parent agent and then runs each implementation in a sub aent. The parent agent checks the work and then moves to the next ph, commits and moves to the next phase. And like this is a plan that's been very vetted. The advice I keep finding myself like the models can't do and it's the thing that like a human needs to like be in the loop right now. Maybe we just need to make the prompts better. But like models are not good at planning work in the way that like I a human would do the work. And I think there's something to be said for trying to steer them to like I don't know we I was doing something the other day with with with uh with a buddy and it was like we have these 40 things on the front end. we're going to move them to the back end, serve them from an API, and then have the front end query the JSON and render it that way. And the model wanted to be like, cool, first we're going to move the 40 things, and then we're going to wire up the API endpoint, and then we're going to refactor the whole front end. Three-phase plan, right? It's like, okay, if you were building this, what would you do? And it's like, well, I would move one thing, get the endpoint working, make sure one thing was working, probably learn some stuff in that in that process, and then like hit some surprises in the land. you like you want to minimize the size of the change in the same way that like if you were an engineer you wouldn't just copy paste 40 files over and then go I mean maybe some people would I wouldn't uh because I want like tighter feedback loops and I I know there's going to be unknowns and there's going to be blast radius to these changes that we didn't think about and I don't particularly want to sit like either you have someone with 15 years of experience in the codebase and they're just like oh yeah you're going to hit that issue or you can sit there for three hours and research every single thing in the codebase and like try to get the plan perfect before you start. But there's like a sweet spot here that is like optimize for learning early on in the implementation plan and then segment the like tasks in the plan the same like how much code would you write? There was no AI. How much code would you write before you like pulled up the web app and looked at it? Or how much code would you write before you like paused to run the tests? And that's a good task size for Ralph or for a very like human in human on the loop AI where you're doing a you know smaller like you know five or sixstep plan or something like this. But like that's that's my rule of thumb is always like your instincts as an engineer are still really really good and you should listen to them and just because you're using AI like a lot of things change but a lot of things don't.


**[00:37:44]**

> The pragmatic programmer has this concept called tracer bullets which is you should write code as it you know this right? Yeah. Yeah, which is you should write code that goes through like that tells you where you're going basically and that goes through all of the integration layers first and you shouldn't do like one huge change. It should be one change that goes through all the layers so you see that all the layers work right

> dude this is crazy. So I read this book like 12 years ago and I loved this idea and I've been explaining exactly what you said this concept to people for the last six months or whatever and I forgot that it had a name. This [laughter] I love it. I literally read the book. I've had it on my shelf for like three years. Still in the wrap, right? But I got it out and I read it in like one sitting the other day. Like it's just the most remarkable well put together thing. Yeah. But

> and this wisdom from 20 years ago is still super important.

> It's I would say more important than ever, right? Because

> Yeah.

> And actually, let's let's take a little sidebar on that, which is that if you're not reading those old books, we are programming in English now. And those books are written in the most clear, perfect way of describing good code that you're ever going to see, right? They are so so good. And so I've been going back to loads of them and just like I'm buying like four more now. Like it's just an amazing way to learn to prompt for coding is reading those 20-year-old books. It really is incredible.


**[00:39:05]**

> I love this. I have a I have another one that I've been obsessed with lately, which is um Do you remember? I think it was Martin Fowler. It might be an Uncle Bob thing, but like this idea of learning tests. Have you heard of this?

> No. No. now.

> Okay. So, a learning test is I've been loving especially if you're integrating with a system that you don't understand like espe like we we do a lot of integrations with the cloud code SDK which like the docs are getting much better but the docs are docs which means like you can't fully trust them all the time. Um, and uh, it's close source and so we like when we're going to build a feature, we'll get halfway through and be like, "Oh, we thought the behavior was this, but it wasn't." And like the surprise would happen halfway through implementation and then we have to throw everything out and roll back. And so a learning test is like you would build it in your unit test framework. You would put it in a place where it doesn't get run on every build because it's not for that but it's like a unit test you know describe expect all this stuff but it's for verifying like how an external library behaves whether it's you know bund color or whether it's some giant battleship piece of software like the cloud agent SDK you basically say like I think the doc say it works like this I think it works like this go write a test that actually like has assertions and console logs that explains the behavior of this thing and often the the assumptions were wrong. But what claude is really coding agents are really good at is like okay let me like go like iterate on this until I have an understanding of what is the contract with this external system and I had a couple that the asserts are really nice because so we don't run these all the time but three months ago we wrote some learning tests about how session IDs work and then they changed the session ID behavior and I was like I think this is wrong like run the learning test again and it's like yep they broke the contract or the contract changed and like here's how it behaves now. It's such a powerful thing to have to like do upfront as part of your research and design for building something new and it's like again it's like a thing that I mean they were for this they have not changed the concept hasn't changed and it's like things that people have been doing for obviously you shouldn't write unit because the wisdom is you shouldn't write unit test on external software it's their job to test it like you you trust the contract and you trust the maintainer and it's like


**[00:41:18]**

> I don't know

> I mean

> super valuable We're on a we're on a total tangent here, but like I had almost ex you know when you like quit a job and you think back things you would have done differently on that job.

> Like we had basically a backend team that was like super unreliable and was like shipping just crap. And what I wanted to do was put like I mean maybe their internal code was good but they just kept breaking the tiny little JSON contracts that we would have between front end and back end. they would put, you know,

> uh, a null where things weren't supposed to be null and blah blah blah blah blah, misspell things. And so I just wanted to put like a little zod thing in between it just on the dev server just to like, you know, that's and that's exactly what you're talking about basically like and that stuff is valuable for the LM2. Okay, heading back.

> Yes.

> The um, so you're basically saying size the tasks super small, almost as small as you can or like is there anything? there is a size that's too small, right? Like I think it's it's around verifiability as well. Like if you could write a unit test to test it, then then do it. Um but again, it's like I size my phases of like I want to know I want to be able to check in on this thing. I mean, for me it's like if we're doing really hard stuff, I'm I'd rather I'd rather check every 10020 lines of code because the last thing you want is like I'm sure you've hit this with Ralph where you're like you get to the end, you're like, I got 2,000 lines of code. It's broken. I don't know why. I don't even know if I was going to reset how I would change my prompts to like make it not be broken other than, you know, make no mistakes ultra thick or whatever the kids are saying to the models these days. And so it's like I'm always looking at dual purpose plans of like if I wanted to just like fire this off and oneshot it and just say, "Hey, go do all the phases while I'm not looking and I'll come check it at the end." Or like this is really like delicate. I have a lot of opinions about exactly how everything looks and how it works and so I'm going to check in after every phase. In either case, it's like size it to a verifiable chunk and it can probably be smaller than you need. And this is another skill that I think people are going to like develop which is like how am I going to know or how is the model going to know that the thing it made is working as I the human intended to.


**[00:43:29]**

> Yeah. Like okay there's two questions. I'll go with the first one. Um

> you're talking about like what what's up?

> Oh my god I just realized I probably I have to I have to run man. I forgot I have a hard stop at 9. Oh my god.

> Do you think

> we should do we should do a part two sometime. Um I'm sure you have more questions. This was a blast though.

> This was great, man. This was so good. I think

> Okay, you go do your thing.

> Always always leave them wanting more, Matt. This is what I've learned. [laughter]

> I'm so annoyed. I had so many things.

> We'll do I'll do another one on Monday if you want. [laughter]

> Sounds good. We'll work it out. See you next.

> Good luck, dude. This was a blast. Thanks, Matt. See you.

> See you guys. Bye. Oh, that's desperately sad. That's desperately sad. So, folks, I'll stay on for a few more minutes and answer your questions because we got um we got a decent number of folks here. And what I kind of wanted to ask in followup is we are entering an era where we're basically working with AI agents and we are going to be like mainly focused on building good plans and good tasks and trying to basically acting as really lead developers. And for those who've never done that in their job, it's going to be quite a big shift. And I I I'm intrigued. My my first question was how do you actually write these plans and what shape do they take? I have some opinions on that on myself. But something I don't really know is how do you take a person who's never been in that position before of, you know, essentially coordinating multiple junior developers underneath them and give them those skills because the only way I learned how to do that was by doing it and doing it badly and then hopefully doing a bit better. So, I don't know. It's intriguing those skills where you basically have to imagine the desired state of the world and figure out what the client wants and then take that and put it into code is something that's hard to teach and I don't quite know how to do it. So, folks, give me some questions. Otherwise, I'm going to head off too. I've got some dinner waiting or not quite waiting, but I've got to make it first. Ah, the thing I love about Dex is he's extremely articulate, extremely I don't know, he he knows what he thinks and he's not afraid to say it and he says it extremely extremely well and I don't know, there's just not that many people talking about this stuff in a way where they're emphasizing code quality. Anyway, right, I'm ahead. Thank you for this, guys. This was fun.

