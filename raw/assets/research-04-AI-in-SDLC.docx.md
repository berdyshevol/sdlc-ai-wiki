# **AI in SDLC Research Project**

## **Artificial Intelligence in the Software Development Life Cycle**

\---

# **Full Paper Outline**

1\. Introduction / Field Overview  

2\. How AI is Used Across SDLC Today  

3\. AI Techniques and Approaches  

4\. Tools and Platforms (Real Products)  

5\. What Problems AI Solves Better Than Traditional Methods  

6\. Applied Example (Case Study: GitHub Copilot)  

7\. Spec-Driven Development vs. Vibe Coding (NEW)  

8\. Challenges, Risks, and Ethical Concerns  

9\. Future Outlook (Next 3–5 Years)  

10\. Conclusion  

11\. References (APA)

\---

# **1\. Introduction / Field Overview**

The  **Software Development Life Cycle (SDLC)**  is a structured process used to design, build, test, deploy, and maintain software systems. Traditional SDLC models vary (Waterfall, Agile, DevOps, Spiral), but most include similar phases:  **requirements gathering, system design, development, testing, deployment, and maintenance** . The SDLC exists to ensure that software is created in a predictable, efficient, and high-quality manner, reducing errors and improving long-term maintainability.

In recent years,  Artificial Intelligence (AI)  has become a major force reshaping software engineering. AI is now integrated into many SDLC stages, improving productivity and automating tasks that traditionally required significant human effort. The rise of  Large Language Models (LLMs)  such as GPT-based systems has introduced new capabilities: generating code, writing documentation, summarizing requirements, creating test cases, and assisting with debugging.

AI in SDLC matters today because software systems are growing in complexity while businesses demand faster delivery cycles. Companies face constant pressure to release features quickly, improve security, and reduce operational costs. AI tools provide significant benefits by accelerating development and improving decision-making. However, AI also introduces risks such as hallucinated code, security vulnerabilities, intellectual property concerns, and over-reliance on automation. Therefore, understanding how AI fits into SDLC is essential for modern software engineering and organizational strategy.

\---

# **2\. How AI is Used Across SDLC Today**

AI tools are increasingly applied across every stage of SDLC. Instead of being limited to coding, AI now supports planning, design, testing, deployment, and long-term maintenance.

## **2.1 Requirements Gathering**

Requirements gathering is one of the most critical SDLC phases. Poorly written requirements often lead to project failure. AI is now used to assist in extracting, organizing, and refining requirements.

Common AI applications include:

* summarizing meetings and extracting key action items  
* converting stakeholder discussions into user stories  
* detecting ambiguous or conflicting requirements  
* generating acceptance criteria

For example, AI-powered meeting assistants can summarize calls and automatically create structured Jira tickets. This reduces manual documentation work and helps product teams communicate requirements more clearly.

## **2.2 System Design and Architecture**

During the design phase, engineers decide how the system will be structured, including database architecture, service boundaries, APIs, and security strategies. AI can assist by recommending architectures, generating diagrams, and identifying risks.

AI can be used for:

* suggesting system design patterns (microservices, monolith, event-driven)  
* generating database schema drafts  
* performing automated threat modeling  
* recommending performance improvements

Although AI cannot replace human architects, it accelerates brainstorming and supports early decision-making.

## **2.3 Development (Coding Phase)**

The development stage is currently the most visible area of AI impact. AI-powered coding assistants such as GitHub Copilot and ChatGPT can generate functions, refactor code, and explain unfamiliar codebases.

AI helps developers with:

* autocomplete suggestions  
* generating boilerplate code  
* producing refactoring suggestions  
* writing unit tests  
* writing documentation and comments  
* translating code between languages

This significantly improves productivity, especially for repetitive tasks.

## **2.4 Testing**

Testing is often time-consuming, and incomplete testing can lead to bugs in production. AI can assist in generating test cases, identifying edge cases, and analyzing failures.

AI applications include:

* generating unit and integration tests  
* detecting anomalies in test results  
* suggesting missing test coverage  
* automating regression test creation

AI can also help identify patterns in bug reports and predict high-risk modules.

## **2.5 Deployment and DevOps**

DevOps focuses on continuous integration, delivery, monitoring, and infrastructure automation. AI improves DevOps by analyzing logs and detecting anomalies before incidents occur.

AI supports DevOps through:

* monitoring system health using anomaly detection  
* predicting failures from telemetry data  
* automating incident response workflows  
* optimizing CI/CD pipelines

Platforms such as Datadog and Dynatrace use AI to detect abnormal behavior in distributed systems.

## **2.6 Maintenance**

Maintenance includes bug fixes, security patches, incident response, and technical debt management. AI can improve maintenance by identifying vulnerabilities and helping engineers respond to issues faster.

Common AI use cases:

* automated incident triage  
* root cause analysis suggestions  
* code quality scanning  
* vulnerability detection  
* technical debt identification

Maintenance is often the most expensive SDLC stage, so AI-based automation can provide strong business value.

Early practitioner experience supports this bifurcation. In the author's professional context, the transition from ad-hoc AI-assisted coding to spec-driven workflows did not eliminate the use of informal, rapid prototyping—vibe coding remained useful for exploration and proof-of-concept work. However, any feature intended for production was routed through a specification-first process before AI agents were used for implementation. This practical split mirrors the theoretical distinction between exploratory and governed workflows: organizations are likely to maintain both modes, with governance rigor scaling to the risk and durability of the deliverable. The implication for SDLC design is that future lifecycle models may need to explicitly accommodate dual-track workflows—one optimized for speed and learning, another for traceability and compliance—rather than assuming a single process fits all AI-assisted work.

\---

# **3\. AI Techniques and Approaches**

AI systems supporting SDLC rely on multiple methods and architectures. These approaches help AI understand human language, generate code, and make predictions based on historical data.

## **3.1 Large Language Models (LLMs)**

LLMs are trained on large datasets of text and code. They can generate human-like responses, produce code, and explain technical concepts. LLMs are widely used in coding assistants and documentation tools.

## **3.2 Natural Language Processing (NLP)**

NLP techniques help AI process human language. In SDLC, NLP is used to analyze requirement documents, summarize meetings, and extract user stories.

## **3.3 Machine Learning Classification**

Classification models can label or categorize issues. In software engineering, this can be used for bug prediction, ticket classification, or identifying security vulnerabilities.

## **3.4 Anomaly Detection**

Anomaly detection is used heavily in DevOps and monitoring. AI systems analyze logs and metrics to detect unusual behavior, which may indicate system failures or attacks.

## **3.5 Reinforcement Learning (RL)**

Reinforcement learning is less common in daily SDLC tasks, but it can be relevant for optimizing CI/CD pipelines, scheduling resources, or automatically tuning performance systems.

## **3.6 Embeddings and Semantic Search**

Embeddings represent text and code as numerical vectors. Semantic search allows AI to retrieve relevant information even if exact keywords do not match. This is essential for codebase search and documentation retrieval.

## **3.7 Retrieval-Augmented Generation (RAG)**

RAG improves accuracy by combining an LLM with a retrieval system. Instead of relying only on model memory, AI retrieves relevant documents from a company’s codebase, wiki, or tickets and then generates responses based on that information.

## **3.8 AI Agents and Autonomous Workflows**

AI agents represent a new stage of AI development. Instead of generating single answers, agents can execute multi-step tasks such as implementing a feature, writing tests, and opening a pull request. This approach is expected to grow rapidly in the next few years.

\---

# **4\. Tools and Platforms (Real Products)**

Many real-world AI products already support SDLC activities. These tools differ in focus, but together they represent a growing AI ecosystem.

## **4.1 Development Tools**

*  **GitHub Copilot** : AI coding assistant integrated into IDEs.  
*  **ChatGPT / Claude** : general-purpose AI for code generation and reasoning.  
*  **Amazon CodeWhisperer** : AWS coding assistant with security features.  
*  **Tabnine** : code completion and suggestions.

## **4.2 Requirements and Project Management**

*  **Jira AI** : helps summarize tickets and generate task breakdowns.  
*  **ServiceNow AI** : automates IT service workflows and incident management.

## **4.3 Code Quality and Security**

*  **SonarQube AI** : static analysis for code quality.  
*  **Snyk AI** : detects vulnerabilities in dependencies and code.

## **4.4 Monitoring and DevOps**

*  **Datadog AI** : log analysis and anomaly detection.  
*  **Dynatrace AI** : root cause analysis and predictive monitoring.  
*  **Azure DevOps AI** : AI features integrated into CI/CD pipelines.

These tools collectively demonstrate that AI is now embedded in the full SDLC pipeline.

\---

# **5\. What Problems AI Solves Better Than Traditional Methods**

AI provides value by improving efficiency and quality compared to traditional development methods.

## **5.1 Productivity and Faster Delivery**

AI reduces time spent on boilerplate code, documentation, and repetitive tasks. This increases feature delivery speed.

## **5.2 Automation of Repetitive Tasks**

Traditional methods require developers to manually create documentation, tests, and monitoring scripts. AI automates much of this work.

## **5.3 Improved Code Quality**

AI can suggest cleaner patterns, detect errors, and recommend refactoring. Combined with static analysis, AI can reduce technical debt.

## **5.4 Faster Bug Detection**

AI-based tools analyze logs and test results faster than humans. They can predict bug-prone areas and generate test coverage improvements.

## **5.5 Faster Onboarding**

New developers can use AI tools to understand unfamiliar codebases quickly through explanations and summaries.

## **5.6 Improved Incident Response**

AI monitoring tools reduce downtime by detecting anomalies early and supporting root cause analysis.

## **5.7 Reduced Cost and Time-to-Market**

Because AI increases speed and reduces manual labor, companies can reduce costs and compete more effectively.

\---

# **6\. Applied Example (Case Study: GitHub Copilot)**

## **6.1 What GitHub Copilot Does**

GitHub Copilot is an AI-powered coding assistant developed by GitHub in partnership with OpenAI. It integrates into development environments such as Visual Studio Code and suggests code completions in real time. Copilot can generate functions, boilerplate, documentation, and even full file templates based on natural language prompts.

Copilot works by analyzing the developer’s current file, surrounding context, and comments. It then predicts the next logical code segments, similar to an advanced autocomplete system.

## **6.2 Impact on SDLC**

Copilot primarily impacts the *development* stage, but it also influences other SDLC phases:

* **Requirements**: Developers can translate user stories into initial code scaffolding.  
* **Design**: Copilot can generate architectural templates and API skeletons.  
* **Testing**: Copilot can generate unit tests and mock data.  
* **Maintenance**: Copilot can assist in debugging and refactoring legacy code.

## **6.3 AI Techniques Used**

Copilot relies on:

* large language models trained on public code and documentation  
* embeddings and contextual prediction  
* natural language processing to interpret comments and prompts

Copilot is not a fully autonomous agent, but it represents an important transition toward AI-driven development.

## **6.4 Business Benefits**

Organizations benefit from Copilot because it:

* increases developer productivity  
* reduces repetitive coding tasks  
* improves developer satisfaction  
* accelerates onboarding  
* speeds up delivery timelines

Microsoft and GitHub studies have reported measurable productivity improvements among developers using Copilot.

## **6.5 Limitations and Risks**

Despite its value, Copilot introduces several risks:

* hallucinated or incorrect code  
* insecure code generation (missing input validation, unsafe patterns)  
* licensing and IP risks if generated code resembles training examples  
* over-reliance, leading to weaker skill development

Copilot is most effective when developers treat it as an assistant rather than a replacement.

\---

# **7\. Spec-Driven Development vs. Vibe Coding (NEW)**

In modern AI-assisted software development, two distinct approaches have emerged: *vibe coding* and *spec-driven development* (SDD).. While both rely on large language models (LLMs) to generate code and accelerate delivery, they differ significantly in structure, traceability, and suitability for production environments.

## **7.1 Vibe Coding**

The term *vibe coding* became popular after Andrej Karpathy described a workflow where developers rely heavily on AI-generated code by “following the vibes,” often without fully understanding every detail of the output. In this approach, the developer interacts with AI using informal prompts, iteratively adjusting the code until the system appears to work. This method can be effective for rapid prototyping and learning, but it introduces risks such as weak documentation, lack of repeatability, and hidden security vulnerabilities.

## **7.2 Spec-Driven Development (SDD)**

In contrast, *spec-driven development (SDD)* is a structured approach where developers first produce a clear specification containing requirements, acceptance criteria, and implementation constraints before generating code. The specification becomes the “source of truth,” guiding the AI in producing consistent and traceable solutions.

## **7.3 Frameworks Supporting Spec-Driven Development**

Several frameworks and toolkits support SDD:

* **GitHub Spec Kit** is an open-source toolkit that guides developers through specification creation, planning, and execution using AI coding agents.  
* **BMAD Method** is a multi-agent framework designed to simulate Agile team roles and workflows.  
* **Kiro** is an agentic environment focused on turning prompts into structured specs and production-ready implementation workflows.

## **7.4 Why This Matters for SDLC**

This shift is important because it addresses one of the biggest limitations of AI: *hallucination and inconsistency*. Vibe coding produces code quickly but can increase technical debt. Spec-driven development improves traceability and governance, making it more appropriate for enterprise SDLC environments.

### **7.5 Practitioner observation: spec-driven development in a production SaaS environment**

The author has applied spec-driven development practices—specifically GitHub Spec Kit and the BMAD Method—as a tech lead managing a five-person engineering team at a project portfolio management SaaS company. Prior to adopting SDD, the team's AI-assisted workflow relied primarily on IDE-level autocomplete (GitHub Copilot) and ad-hoc prompting—an approach closer to vibe coding, where developers interacted with AI tools informally and iteratively adjusted output until it appeared functional.

After introducing structured specifications as the starting point for AI-assisted implementation, three observable changes emerged in the team's workflow. First, task scoping for AI agents improved: when a specification clearly defined inputs, outputs, acceptance criteria, and constraints before code generation began, AI tools produced more focused and implementable output rather than generating broad, loosely connected scaffolding that required significant manual correction. Second, hallucination-driven rework decreased. Under the previous ad-hoc approach, AI-generated code frequently referenced nonexistent methods or made incorrect assumptions about internal APIs—problems that consumed review and debugging time. With specifications anchoring the generation process, these errors became less frequent because the AI operated within a more constrained and well-defined context. Third, the overall consistency of AI-generated code improved: output across different features and team members became more predictable in structure and style, which reduced the cognitive load during code review and simplified onboarding for newer developers working within the same codebase.

These observations are limited to a single team and product context and do not constitute a controlled study. However, they align with the broader argument in the SDD literature: that structured specifications reduce ambiguity, improve traceability, and give AI systems more reliable targets—benefits that become especially visible in production environments where rework, review burden, and consistency matter more than initial generation speed.

\---

# **8\. Challenges, Risks, and Ethical Concerns**

AI adoption in SDLC creates significant ethical and technical challenges.

## **8.1 Hallucinations in Generated Code**

LLMs may produce incorrect code that looks plausible. This is dangerous because developers may trust output without validation.

## **8.2 Insecure Code Generation**

AI can generate insecure patterns such as SQL injection vulnerabilities or weak authentication logic.

## **8.3 Copyright and Intellectual Property Risks**

Because AI models are trained on public code, there is debate about whether generated code could violate copyrights.

## **8.4 Data Privacy and Code Leakage**

Using AI tools may expose confidential source code to third-party providers, especially if prompts are logged.

## **8.5 Bias in Training Data**

AI models may inherit biases from training data, affecting decision-making in project management or hiring systems.

## **8.6 Over-Reliance and Skill Loss**

If developers depend too heavily on AI, they may lose problem-solving ability and understanding of system fundamentals.

## **8.7 Accountability**

When AI-generated code causes a failure, it is unclear who is responsible: the developer, the company, or the AI provider.

## **8.8 Compliance and Governance**

Organizations increasingly require governance policies to control how AI is used in development.

\---

# **9\. Future Outlook (Next 3–5 Years)**

Over the next 3–5 years, AI is expected to become more autonomous and more deeply integrated into SDLC.

Predicted trends include:

* AI agents implementing full features (requirements → code → tests → PR)  
* AI-driven code review becoming standard  
* predictive DevOps and auto-remediation  
* increased regulation and governance policies  
* new job roles such as AI engineer, AI QA specialist, and AI governance lead  
* reduced demand for simple junior coding tasks, but higher demand for system thinking

AI will not eliminate software engineers, but it will shift their work toward higher-level reasoning, design, and oversight.

\---

# **10\. Conclusion**

Artificial Intelligence is transforming the software development life cycle by automating tasks, improving productivity, and enabling faster delivery of high-quality software. AI is now applied across requirements gathering, design, development, testing, deployment, and maintenance. Tools such as GitHub Copilot, ServiceNow AI, and Datadog AI demonstrate real-world adoption and measurable benefits.

However, AI introduces risks including hallucinations, insecure code generation, IP concerns, privacy issues, and over-reliance. To use AI safely, organizations must establish governance policies and ensure that human oversight remains central. In the next 3–5 years, AI agents and spec-driven development frameworks will likely become common, shifting software engineering into a new era where specifications and automation become more important than manual coding.

\---

# **Presentation Plan (10–12 Slides)**

## **Slide 1: Title**

AI in SDLC: How Artificial Intelligence is Transforming Software Engineering

## **Slide 2: What is SDLC**

* Requirements  
* Design  
* Development  
* Testing  
* Deployment  
* Maintenance

## **Slide 3: Why AI Matters in SDLC**

* faster delivery  
* more complexity  
* higher security needs  
* automation demand

## **Slide 4: AI in Requirements**

* meeting summaries  
* user story extraction  
* acceptance criteria generation

## **Slide 5: AI in Design**

* architecture suggestions  
* diagram generation  
* threat modeling

## **Slide 6: AI in Development**

* Copilot, ChatGPT, Claude  
* code generation and refactoring  
* documentation writing

## **Slide 7: AI in Testing**

* automated test generation  
* bug detection  
* regression automation

## **Slide 8: AI in DevOps \+ Deployment**

* anomaly detection  
* log analysis  
* predictive monitoring

## **Slide 9: AI in Maintenance**

* incident triage  
* technical debt detection  
* vulnerability scanning

## **Slide 10: Spec-Driven vs Vibe Coding**

* vibe coding \= fast but risky  
* spec-driven \= structured and safer  
* frameworks: SpecKit, BMAD, Kiro

## **Slide 11: Risks \+ Ethics**

* hallucinations  
* insecure code  
* IP/copyright  
* privacy  
* governance

## **Slide 12: Future Outlook**

* autonomous AI agents  
* new job roles  
* governance growth

\---

# **Speaker Division (4 Group Members)**

* Speaker 1: Slides 1–3 (Intro, SDLC, why AI matters)  
* Speaker 2: Slides 4–6 (AI in requirements, design, development)  
* Speaker 3: Slides 7–9 (AI in testing, DevOps, maintenance)  
* Speaker 4: Slides 10–12 (Spec-driven vs vibe coding, ethics, future)

\---

# **Suggested Visuals (Diagram Ideas)**

1\. SDLC pipeline diagram (Requirements → Maintenance)  

2\. AI tools mapped to SDLC stages (table/graphic)  

3\. Copilot workflow diagram (developer → prompt → AI suggestion → commit)  

4\. Spec-driven development workflow (spec → plan → tasks → implementation)  

5\. Risk diagram (hallucinations, security, IP, privacy)

\---

# **Professor-Style Q\&A (10 Questions \+ Strong Answers)**

 **Q1: Can AI replace software engineers?**   

A: No. AI improves productivity, but engineers remain responsible for design, architecture, security, and accountability.

 **Q2: Why is AI useful in requirements gathering?**   

A: Because requirements are text-heavy and AI excels at summarization and extracting structured information.

 **Q3: What is the biggest risk of AI-generated code?**   

A: Hallucination and insecure patterns that appear correct but contain hidden bugs.

 **Q4: Why is spec-driven development important?**   

A: It improves traceability and reduces ambiguity, making AI-generated outputs safer and more repeatable.

 **Q5: How does RAG improve AI tools?**   

A: It retrieves real project documents and codebase context, reducing hallucinations.

 **Q6: What is an AI agent in SDLC?**   

A: A system that performs multi-step workflows such as coding, testing, and deployment tasks autonomously.

 **Q7: How does AI help in DevOps?**   

A: It detects anomalies, predicts failures, and improves incident response speed.

 **Q8: What are the ethical issues of AI coding assistants?**   

A: IP/copyright concerns, privacy risks, and unclear accountability for AI mistakes.

 **Q9: How will AI affect junior developers?**   

A: Junior work will shift away from boilerplate coding toward understanding systems, reviewing AI output, and learning architecture earlier.

 **Q10: What is the future of AI in SDLC?**   

A: AI agents will handle larger tasks, but governance and human oversight will become more critical.

\---

# **APA References**

BMAD Code Org. (2025). \*BMAD-METHOD: Breakthrough Method for Agile AI Driven Development.\* GitHub. https://github.com/bmad-code-org/BMAD-METHOD


Cloudflare. (2025). \*What is vibe coding?\* Cloudflare Learning Center. https://www.cloudflare.com/learning/ai/ai-vibe-coding/


Datadog. (2024). \*AI-powered observability and monitoring.\* Datadog Documentation. https://www.datadoghq.com/


Dynatrace. (2024). \*AI-powered observability platform.\* Dynatrace Documentation. https://www.dynatrace.com/


GitHub. (2025, September 2). \*Spec-driven development with AI: Get started with a new open source toolkit.\* GitHub Blog. https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/


GitHub. (2025). \*Spec Kit (spec-kit) repository.\* GitHub. https://github.com/github/spec-kit


Karpathy, A. (2025, February 6). \*There’s a new kind of coding I call “vibe coding”…\* \[Post\]. X (formerly Twitter). https://x.com/karpathy/status/1886192184808149383


Kiro. (2025). \*Kiro: Agentic AI development from prototype to production.\* https://kiro.dev/


McKinsey & Company. (2023). \*The economic potential of generative AI: The next productivity frontier.\* https://www.mckinsey.com/


Microsoft. (2023). \*The impact of GitHub Copilot on developer productivity.\* Microsoft Research / GitHub Research. https://github.com/features/copilot


Snyk. (2024). \*AI-enhanced developer security platform.\* Snyk Documentation. https://snyk.io/


Willison, S. (2025, March 19). \*Not all AI-assisted programming is vibe coding (but vibe coding rocks).\* Simon Willison’s Weblog. https://simonwillison.net/2025/Mar/19/vibe-coding/