# Mechanical fix log - the duplicated `Skip if` labels

Attack 2, 2026-09-05. The card prints the heading **Skip if:** and a quarter of the
catalogue then started the sentence with "Skip if" again, so the reader saw
**Skip if: Skip if you do not write shell scripts.** Two agents measured it
independently; one counted thirteen consecutive offenders on a single screen.

104 cards already used the correct form, so this conforms to the file's own house
standard rather than inventing one. Only the leading label was removed and the next
letter capitalised. A mid-sentence "Skip also if" is correct English and was left
alone. No other word was changed.

157 lines changed. Every one, before and after.

### r-fb8dc53be9 - Best practices for Claude Code

- **before:** Skip it if you have never run a Claude Code session - the advice is corrective, so without your own bad habits to match against it reads as a list of abstractions.
- **after:**  You have never run a Claude Code session - the advice is corrective, so without your own bad habits to match against it reads as a list of abstractions.

### r-4f437b4495 - Hooks reference (Claude Code)

- **before:** Skip if you are still learning the basics. Read the hooks guide first. This is a lookup reference, not a tutorial, and it is enormous.
- **after:**  You are still learning the basics. Read the hooks guide first. This is a lookup reference, not a tutorial, and it is enormous.

### r-c4c418a887 - Choose a sandbox environment for Claude Code

- **before:** Skip if you only run short supervised sessions on your own code and approve each action yourself. The setup effort will not pay for itself.
- **after:**  You only run short supervised sessions on your own code and approve each action yourself. The setup effort will not pay for itself.

### r-671a36db48 - Agent SDK overview

- **before:** Skip if you only use Claude Code interactively. Skip also if you want raw model access and intend to write the tool loop yourself, in which case the Client SDK is the right choice.
- **after:**  You only use Claude Code interactively. Skip also if you want raw model access and intend to write the tool loop yourself, in which case the Client SDK is the right choice.

### r-3f564157f0 - Claude Code on Amazon Bedrock

- **before:** Skip if you are an individual on a Pro or Max plan. You gain nothing and take on a lot of AWS configuration.
- **after:**  You are an individual on a Pro or Max plan. You gain nothing and take on a lot of AWS configuration.

### r-4601878d32 - Skill authoring best practices

- **before:** Skip if you have not written a skill yet; read the Skills overview first. Skip also if your need is a one-off prompt rather than a reusable workflow.
- **after:**  You have not written a skill yet; read the Skills overview first. Skip also if your need is a one-off prompt rather than a reusable workflow.

### r-1564c417fe - Claude Managed Agents overview

- **before:** Skip if you need Zero Data Retention or a HIPAA BAA. Managed Agents is stateful by design and is not eligible for either. Skip also if you want full control of the agent loop; use the Messages API instead.
- **after:**  You need Zero Data Retention or a HIPAA BAA. Managed Agents is stateful by design and is not eligible for either. Skip also if you want full control of the agent loop; use the Messages API instead.

### r-42516bb950 - Effective context engineering for AI agents

- **before:** Skip if you only make single-turn API calls. Read the July 2026 follow-up first if you are on Claude 5 generation models, because it reverses several recommendations here.
- **after:**  You only make single-turn API calls. Read the July 2026 follow-up first if you are on Claude 5 generation models, because it reverses several recommendations here.

### r-4f67b063af - Writing effective tools for agents - with agents

- **before:** Skip if you only consume other people's tools and never write your own.
- **after:**  You only consume other people's tools and never write your own.

### r-4dd2373a00 - Code execution with MCP: building more efficient agents

- **before:** Skip if you connect two or three MCP servers. The pattern requires a code execution sandbox, which is a real security surface you then have to own.
- **after:**  You connect two or three MCP servers. The pattern requires a code execution sandbox, which is a real security surface you then have to own.

### r-414ce4b52e - Demystifying evals for AI agents

- **before:** Skip if you have not shipped an agent yet; it will read as abstract. Skip if you want a ready-made eval framework, because this is concepts and worked reasoning, not code.
- **after:**  You have not shipped an agent yet; it will read as abstract. Skip if you want a ready-made eval framework, because this is concepts and worked reasoning, not code.

### r-97cd97d27d - How we contain Claude across products

- **before:** Skip if you want configuration steps. This is architecture and postmortem thinking, not something you can copy into settings.json.
- **after:**  You want configuration steps. This is architecture and postmortem thinking, not something you can copy into settings.json.

### r-81e43f0350 - The new rules of context engineering for Claude 5 generation models

- **before:** Skip if you are pinned to older Claude models. The advice is explicitly tied to the Claude 5 generation and removing guardrails can hurt on earlier ones.
- **after:**  You are pinned to older Claude models. The advice is explicitly tied to the Claude 5 generation and removing guardrails can hurt on earlier ones.

### r-9f1cc05b1c - Maximizing the value of your Claude Code sessions

- **before:** Skip if cost is not a constraint for you. The workflow advice on its own is already covered in the best-practices page.
- **after:**  Cost is not a constraint for you. The workflow advice on its own is already covered in the best-practices page.

### r-7340ad4c33 - Claude Code 101

- **before:** Skip if you already use Claude Code daily; go straight to the best-practices page. Reported to require a Pro, Max or Enterprise plan or an API key for the hands-on exercises.
- **after:**  You already use Claude Code daily; go straight to the best-practices page. Reported to require a Pro, Max or Enterprise plan or an API key for the hands-on exercises.

### r-cc36d642e5 - Building with the Claude API

- **before:** Skip if you only use Claude Code and never touch the API. Nine hours is a real commitment, and if you learn by reading code the cookbooks get you there faster.
- **after:**  You only use Claude Code and never touch the API. Nine hours is a real commitment, and if you learn by reading code the cookbooks get you there faster.

### r-ff743e0d5a - Agent Skills with Anthropic

- **before:** Skip if you want depth on one surface; this course deliberately spreads across four. It is labelled Beginner, so it will feel slow if you already write skills.
- **after:**  You want depth on one surface; this course deliberately spreads across four. It is labelled Beginner, so it will feel slow if you already write skills.

### r-2bbb198498 - Claude Code: A Highly Agentic Coding Assistant

- **before:** Skip if you do not know Python and git. Skip if you need current feature coverage: the syllabus predates auto mode, agent teams and dynamic workflows, so check anything about commands or flags against the docs.
- **after:**  You do not know Python and git. Skip if you need current feature coverage: the syllabus predates auto mode, agent teams and dynamic workflows, so check anything about commands or flags against the docs.

### r-190f8f5259 - Claude Code (Frontend Masters)

- **before:** Skip if you want deep API or SDK work; this is about Claude Code the tool. Needs a free account, and 1.9 hours is tight for that many topics, so expect breadth over depth in places.
- **after:**  You want deep API or SDK work; this is about Claude Code the tool. Needs a free account, and 1.9 hours is tight for that many topics, so expect breadth over depth in places.

### r-26b52d229f - anthropics/claude-quickstarts

- **before:** Skip if you want explanation. These are projects with minimal narration. Skip if your work is Claude Code workflows rather than API integration.
- **after:**  You want explanation. These are projects with minimal narration. Skip if your work is Claude Code workflows rather than API integration.

### r-e683190d69 - anthropics/claude-agent-sdk-python

- **before:** Skip if you work in TypeScript; use anthropics/claude-agent-sdk-typescript instead. Skip if you want tutorials, because the docs site is the better starting point.
- **after:**  You work in TypeScript; use anthropics/claude-agent-sdk-typescript instead. Skip if you want tutorials, because the docs site is the better starting point.

### r-7773ad4116 - anthropics/claude-code-action

- **before:** Skip if you are not on GitHub; see the GitLab CI/CD docs instead. Skip until you have a token budget and a review policy, because this runs unattended against your repository.
- **after:**  You are not on GitHub; see the GitLab CI/CD docs instead. Skip until you have a token budget and a review policy, because this runs unattended against your repository.

### r-57a8f3a8c5 - ClaudeLog

- **before:** Skip if you need authoritative answers. This is one person's experiments, it is not affiliated with Anthropic, and individual pages carry no visible date, so verify anything about flags or commands against the official docs first.
- **after:**  You need authoritative answers. This is one person's experiments, it is not affiliated with Anthropic, and individual pages carry no visible date, so verify anything about flags or commands against the official docs first.

### r-881029ebe6 - Agentic Engineering Patterns

- **before:** Skip if you want Claude-specific configuration; it covers OpenAI Codex too and stays tool-agnostic on purpose. Skip if you need a finished book, because chapters are still being added.
- **after:**  You want Claude-specific configuration; it covers OpenAI Codex too and stays tool-agnostic on purpose. Skip if you need a finished book, because chapters are still being added.

### r-967880ec2e - Code w/ Claude Developer Conference (session recordings)

- **before:** Skip if you want a tutorial. These are conference talks, not walkthroughs, and any live demo of a specific flag or command may already be out of date.
- **after:**  You want a tutorial. These are conference talks, not walkthroughs, and any live demo of a specific flag or command may already be out of date.

### r-97df5a7a7d - Build an MCP server

- **before:** Skip if you only want to connect existing MCP servers; the Claude Code MCP quickstart is faster. Skip if you have no local Python or Node toolchain to work in.
- **after:**  You only want to connect existing MCP servers; the Claude Code MCP quickstart is faster. Skip if you have no local Python or Node toolchain to work in.

### r-9f57e8bf80 - Head of Claude Code: What happens after coding is solved (Boris Cherny)

- **before:** Skip if you want technique. There is almost nothing here you can copy into your terminal, and the framing is aimed at product and career questions as much as engineering ones.
- **after:**  You want technique. There is almost nothing here you can copy into your terminal, and the framing is aimed at product and career questions as much as engineering ones.

### r-aac1f93a7e - Prompt engineering best practices for 2026

- **before:** Skip it if you already use examples, explicit constraints and chain-of-thought by habit - this stops at general craft and never gets into evals or model-specific tuning.
- **after:**  You already use examples, explicit constraints and chain-of-thought by habit - this stops at general craft and never gets into evals or model-specific tuning.

### r-5780f44af0 - Steering Claude Code: when to use CLAUDE.md, skills, hooks, and subagents

- **before:** Skip it if you have not yet used Claude Code on a real project - it assumes you know what a session, a compaction and a slash command are, and teaches none of them.
- **after:**  You have not yet used Claude Code on a real project - it assumes you know what a session, a compaction and a slash command are, and teaches none of them.

### r-4d17281029 - Claude Code overview and install guide

- **before:** Skip it if Claude Code is already installed and working - it is an index page, so everything past the install block is links rather than instruction.
- **after:**  Claude Code is already installed and working - it is an index page, so everything past the install block is links rather than instruction.

### r-7d24e5faa2 - Building effective agents

- **before:** Skip it if you need current implementation detail: it is from December 2024, Anthropic has added a banner saying the tooling has changed, and it points you at Managed Agents instead.
- **after:**  You need current implementation detail: it is from December 2024, Anthropic has added a banner saying the tooling has changed, and it points you at Managed Agents instead.

### r-77ae700ce1 - Equipping agents for the real world with Agent Skills

- **before:** Skip it if you want step-by-step authoring instructions - this is the reasoning behind skills, and it hands the how-to off to the docs and the cookbook.
- **after:**  You want step-by-step authoring instructions - this is the reasoning behind skills, and it hands the how-to off to the docs and the cookbook.

### r-3ce8106ea6 - Building agents with the Claude Agent SDK

- **before:** Skip it if you want runnable code - it is a five-minute design argument with an illustrative example, not a tutorial with a repository to clone.
- **after:**  You want runnable code - it is a five-minute design argument with an illustrative example, not a tutorial with a repository to clone.

### r-d20ed293a5 - Claude Platform documentation home

- **before:** Skip it if you work only in Claude Code or the Claude app - nothing here applies until you are writing API calls yourself.
- **after:**  You work only in Claude Code or the Claude app - nothing here applies until you are writing API calls yourself.

### r-d98aa6f2dd - Claude Cookbooks

- **before:** Skip it if you do not have an API key with credits - the notebooks call the paid API, and reading them without running them gives you far less than the time costs.
- **after:**  You do not have an API key with credits - the notebooks call the paid API, and reading them without running them gives you far less than the time costs.

### r-f606f9314f - Anthropic courses: API fundamentals, prompting, evals and tool use

- **before:** Skip it if you want current model behaviour - the material deliberately uses Claude 3 Haiku to keep student API bills low, so the model choices and some SDK patterns are behind.
- **after:**  You want current model behaviour - the material deliberately uses Claude 3 Haiku to keep student API bills low, so the model choices and some SDK patterns are behind.

### r-10ba719313 - anthropics/skills: example Agent Skills and the skill spec

- **before:** Skip it if you want an explanation of why skills work the way they do - this is a folder of examples with a thin README, so read the Agent Skills engineering post first.
- **after:**  You want an explanation of why skills work the way they do - this is a folder of examples with a thin README, so read the Agent Skills engineering post first.

### r-75454d3190 - AI Fluency for pK-12 Educators (learning path)

- **before:** Skip it if you teach at university level or want Claude product training - the framing, examples and workshop kit are all built for pK-12 classrooms.
- **after:**  You teach at university level or want Claude product training - the framing, examples and workshop kit are all built for pK-12 classrooms.

### r-e42f68c371 - Claude Code: Software Engineering with Generative AI Agents

- **before:** Skip it if you want deep coverage of hooks, subagents and MCP internals - this is a beginner orchestration course, and Anthropic's own best-practices docs go further for free.
- **after:**  You want deep coverage of hooks, subagents and MCP internals - this is a beginner orchestration course, and Anthropic's own best-practices docs go further for free.

### r-9189bd0cb6 - Next-Generation AI Assistant: Claude by Anthropic

- **before:** Skip it if the title made you think Anthropic built it - it is a Coursera and Starweaver production, one module long, rated only 4.1 from 33 reviews, and it never leaves basic marketing prompts.
- **after:**  The title made you think Anthropic built it - it is a Coursera and Starweaver production, one module long, rated only 4.1 from 33 reviews, and it never leaves basic marketing prompts.

### r-011e20ba3e - MCP: Build Rich-Context AI Apps with Anthropic

- **before:** Skip it if you are new to Python or to LLM app development, and note it was recorded in May 2025, so the Python SDK has since moved to v2 and some code needs adjusting.
- **after:**  You are new to Python or to LLM app development, and note it was recorded in May 2025, so the Python SDK has since moved to v2 and some code needs adjusting.

### r-b5a28e4e25 - Claude Cowork Tutorial: How to Use Anthropic's AI Desktop Agent

- **before:** Skip it if you already use Cowork daily - the examples are entry level and the advanced sections stop at naming skills, connectors and scheduling rather than teaching them.
- **after:**  You already use Cowork daily - the examples are entry level and the advanced sections stop at naming skills, connectors and scheduling rather than teaching them.

### r-3b409df1d4 - How to Build an MCP Server with Python, Docker, and Claude Code

- **before:** Skip it if you do not have Docker and a Claude Code subscription ready, or if you only want the concept - this is a build-along and reading it without typing gains you little.
- **after:**  You do not have Docker and a Claude Code subscription ready, or if you only want the concept - this is a build-along and reading it without typing gains you little.

### r-b03b4a5725 - Claude Code Essentials (ExamPro full course)

- **before:** Skip it if you learn badly from long video - the same ground is covered faster in Anthropic's written docs, and a video course dates quickly as CLI commands change.
- **after:**  You learn badly from long video - the same ground is covered faster in Anthropic's written docs, and a video course dates quickly as CLI commands change.

### r-13f7418861 - The Claude Code Handbook

- **before:** Skip it if you are already fluent with Claude Code - the first eight chapters are background on Anthropic and the model family, and the depth per topic is lower than the official docs.
- **after:**  You are already fluent with Claude Code - the first eight chapters are background on Anthropic and the model family, and the depth per topic is lower than the official docs.

### r-461f940892 - Claude Code for Product Managers

- **before:** Skip it if you will not subscribe to Every - the free portion stops at the roadmap section, and the three most specific claims sit behind the paywall.
- **after:**  You will not subscribe to Every - the free portion stops at the roadmap section, and the three most specific claims sit behind the paywall.

### r-e36c212931 - Everyone should be using Claude Code more

- **before:** Skip it if you want method rather than inspiration - it is a list of what other people do, most of it sits behind a paid subscription, and it dates from October 2025 so it predates Cowork.
- **after:**  You want method rather than inspiration - it is a list of what other people do, most of it sits behind a paid subscription, and it dates from October 2025 so it predates Cowork.

### r-0e4ddc7e7a - How I AI: Claude Code for product managers, with Teresa Torres

- **before:** Skip it if you want copyable configuration - it is a demonstration and conversation, so you get the shape of the system and have to rebuild the files yourself.
- **after:**  You want copyable configuration - it is a demonstration and conversation, so you get the shape of the system and have to rebuild the files yourself.

### r-56fd40ae95 - How to Use Claude Code: Complete Tutorial for Product Managers

- **before:** Skip it if you want precise, current instructions - it is a conversation with no publication date shown on the page, so treat the version-specific detail as unverified.
- **after:**  You want precise, current instructions - it is a conversation with no publication date shown on the page, so treat the version-specific detail as unverified.

### r-f21dc84635 - Getting started with Claude Cowork (Airtree course)

- **before:** Skip it if you already automate work with Cowork or Claude Code - it is beginner material by design and stops at the one-hour mark.
- **after:**  You already automate work with Cowork or Claude Code - it is beginner material by design and stops at the one-hour mark.

### r-d8e6ba37a0 - Complete Guide to Claude Cowork (Claude Code for Everyone)

- **before:** Skip it if you want an independent assessment of limits - it is a teaching site written by an enthusiast, so pair it with a review that documents what Cowork does badly.
- **after:**  You want an independent assessment of limits - it is a teaching site written by an enthusiast, so pair it with a review that documents what Cowork does badly.

### r-1de0b17424 - Build Your PM Operating System on Claude Code

- **before:** Skip it if you cannot commit to live sessions or will not pay - it needs a Claude Code Pro or Max subscription on top of the course fee, and 13 reviews is a weak quality signal.
- **after:**  You cannot commit to live sessions or will not pay - it needs a Claude Code Pro or Max subscription on top of the course fee, and 13 reviews is a weak quality signal.

### r-289f30bcca - Craft a Professional AI Developer Setup (Cursor & Claude Code)

- **before:** Skip it if you only want Claude Code - roughly half the course is Cursor - and note it was published in August 2025, so parts of both tools have changed since recording.
- **after:**  You only want Claude Code - roughly half the course is Cursor - and note it was published in August 2025, so parts of both tools have changed since recording.

### r-efa0486eba - MCP Python SDK

- **before:** Skip it if you want to learn what MCP is - the README assumes that and sends you to the documentation site, so start with a course or the freeCodeCamp build-along instead.
- **after:**  You want to learn what MCP is - the README assumes that and sends you to the documentation site, so start with a course or the freeCodeCamp build-along instead.

### r-fca8ba2163 - MCP reference servers

- **before:** Skip it if you want servers to deploy - the maintainers warn these are demonstrations without production security hardening, and the registry is the right place for real ones.
- **after:**  You want servers to deploy - the maintainers warn these are demonstrations without production security hardening, and the registry is the right place for real ones.

### r-aa3fb9b26c - A Guide to Claude Code 2.0 and getting better at using coding agents

- **before:** Skip it if you need current detail - it documents Claude Code 2.0 as of December 2025, and both the CLI and the model line-up have moved on since.
- **after:**  You need current detail - it documents Claude Code 2.0 as of December 2025, and both the CLI and the model line-up have moved on since.

### r-bb9cebd574 - Claude for K-12 Teachers: context steering, Projects and Skills

- **before:** Skip it if you teach at university or need assessment-policy guidance - this is classroom practice for K-12 and says nothing about institutional rules.
- **after:**  You teach at university or need assessment-policy guidance - this is classroom practice for K-12 and says nothing about institutional rules.

### r-cd019b4ce7 - Building a Claude Project for Teaching & Learning (recording)

- **before:** Skip it if you need current interface detail - the recording is labelled 2025, so the Projects screens and features shown are behind what you will see today.
- **after:**  You need current interface detail - the recording is labelled 2025, so the Projects screens and features shown are behind what you will see today.

### r-0ccfc4f72a - Mushtaq Bilal — Claude for Academic Writing & Research

- **before:** Skip if you will not hand over an email address: every post is behind a subscribe form, so there is nothing to read until you sign up. Skip too if you want teaching rather than marketing - the recent posts are almost all registration pages for his own webinars and paid tools.
- **after:**  You will not hand over an email address: every post is behind a subscribe form, so there is nothing to read until you sign up. Skip too if you want teaching rather than marketing - the recent posts are almost all registration pages for his own webinars and paid tools.

### r-cb786e071f - Use Claude for Education at your university

- **before:** Skip if your university has no Claude for Education licence - none of it applies. Skip if you want teaching advice; the 'what can I use Claude for' list is written for students, not for people who set assignments.
- **after:**  Your university has no Claude for Education licence - none of it applies. Skip if you want teaching advice; the 'what can I use Claude for' list is written for students, not for people who set assignments.

### r-8e050ee72e - How to Set Up a Claude Project that Answers Questions about Your Class

- **before:** Skip if your syllabus changes often - the guide itself admits the assistant goes stale the moment the course does. Skip if you teach school; it assumes a syllabus, TAs and a Canvas-style platform.
- **after:**  Your syllabus changes often - the guide itself admits the assistant goes stale the moment the course does. Skip if you teach school; it assumes a syllabus, TAs and a Canvas-style platform.

### r-5ef57a95ef - AI Fluency for Educators (Anthropic Academy)

- **before:** Skip if you have never opened an AI chat tool - it assumes the 4D framework from the Framework and Foundations course. Skip if you want Claude-specific, click-by-click steps; this is deliberately model-agnostic.
- **after:**  You have never opened an AI chat tool - it assumes the 4D framework from the Framework and Foundations course. Skip if you want Claude-specific, click-by-click steps; this is deliberately model-agnostic.

### r-f3637f97bc - Teaching AI Fluency (Anthropic Academy)

- **before:** Skip if you only want to cut your own marking and planning time - this is curriculum and assessment work, five to six hours of it including about seventy minutes of video. Skip if you have not done Framework and Foundations first; it assumes the 4Ds.
- **after:**  You only want to cut your own marking and planning time - this is curriculum and assessment work, five to six hours of it including about seventy minutes of video. Skip if you have not done Framework and Foundations first; it assumes the 4Ds.

### r-32b6bdef8a - AI Fluency for pK-12 Educators

- **before:** Skip if you already use AI daily; the first half is beginner material. Skip if you want ready-made classroom prompts - this teaches judgement, not a prompt pack.
- **after:**  You already use AI daily; the first half is beginner material. Skip if you want ready-made classroom prompts - this teaches judgement, not a prompt pack.

### r-f916cddec9 - AI Fluency for pK-12 Train the Trainer

- **before:** Skip if you will never train other adults. Skip if you have not done the pK-12 Educators course first - the kit assumes you can already answer teachers' questions without notes.
- **after:**  You will never train other adults. Skip if you have not done the pK-12 Educators course first - the kit assumes you can already answer teachers' questions without notes.

### r-d26fb9ba53 - The AI Fluency Framework - open educational resources hub

- **before:** Skip if you already know which course you want - this page is a map, not training. It contains no Claude-specific instructions at all.
- **after:**  You already know which course you want - this page is a map, not training. It contains no Claude-specific instructions at all.

### r-d37ce11fa5 - Introducing Claude for Teachers

- **before:** Skip if you teach outside the US or in higher education - you are not eligible. Skip if you want a how-to; this is an announcement, and it only shows the workflow that works.
- **after:**  You teach outside the US or in higher education - you are not eligible. Skip if you want a how-to; this is an announcement, and it only shows the workflow that works.

### r-8f0d9dff87 - Claude for K-12 teachers - product page with worked prompts

- **before:** Skip if sales pages irritate you - most of this is claims, logos and testimonials. Skip if you are outside the US, because the free plan is US-only.
- **after:**  Sales pages irritate you - most of this is claims, logos and testimonials. Skip if you are outside the US, because the free plan is US-only.

### r-5aa9ca06c5 - Claude for Teachers: your data and our terms

- **before:** Skip if your district already has its own written agreement with Anthropic - that agreement overrides these terms. Skip if you are outside the US; none of this applies to you.
- **after:**  Your district already has its own written agreement with Anthropic - that agreement overrides these terms. Skip if you are outside the US; none of this applies to you.

### r-c7fbf92520 - Agent Skills for K-12 Teachers (open source)

- **before:** Skip if you do not use a terminal - installing needs git and Claude Code. Skip if you already have Claude for Teachers, where the skills are installed for you.
- **after:**  You do not use a terminal - installing needs git and Claude Code. Skip if you already have Claude for Teachers, where the skills are installed for you.

### r-ea39152439 - Anthropic Education Report: how educators use Claude

- **before:** Skip if you teach at school level - the sample is higher education only. Skip if you want instructions; this is a usage study with no how-to in it.
- **after:**  You teach at school level - the sample is higher education only. Skip if you want instructions; this is a usage study with no how-to in it.

### r-fccfc16f07 - Practical ways to get started using Claude for educators

- **before:** Skip if you already use Projects - the first half is beginner material. Skip if you need subject-specific worked examples; the prompts are generic across subjects.
- **after:**  You already use Projects - the first half is beginner material. Skip if you need subject-specific worked examples; the prompts are generic across subjects.

### r-a6467110a1 - The Ultimate Claude Guide for Teachers

- **before:** Skip if you have never used any AI tool - it assumes you can already write a prompt. Skip if you need US policy detail; the author writes from an Australian independent school.
- **after:**  You have never used any AI tool - it assumes you can already write a prompt. Skip if you need US policy detail; the author writes from an Australian independent school.

### r-7bf1e57560 - Claude AI for Teachers - the practical guide

- **before:** Skip if you want evidence - the time-saved figures (about five hours a week on planning) are the author's own claim with nothing behind them. Skip if you need US terminology; it uses Year 7, EAL and scheme of work.
- **after:**  You want evidence - the time-saved figures (about five hours a week on planning) are the author's own claim with nothing behind them. Skip if you need US terminology; it uses Year 7, EAL and scheme of work.

### r-6cee334566 - 43 Claude Skills for college teachers

- **before:** Skip if you do not yet know what a Skill is - it does not teach the basics. Skip if you teach at school level; the framing is semesters, syllabi and departments.
- **after:**  You do not yet know what a Skill is - it does not teach the basics. Skip if you teach at school level; the framing is semesters, syllabi and departments.

### r-edbff45289 - Why is Claude for Teachers? (critical hands-on review)

- **before:** Skip if you want a how-to - there is none here. Skip if the sarcastic tone will stop you seeing the fair points underneath it.
- **after:**  You want a how-to - there is none here. Skip if the sarcastic tone will stop you seeing the fair points underneath it.

### r-76de44b7a7 - Anthropic launched Claude for Teachers. We blocked it for our district.

- **before:** Skip if you are a classroom teacher with no say in procurement - it will worry you without giving you an action. Skip if you are outside the US; FERPA does not apply to you.
- **after:**  You are a classroom teacher with no say in procurement - it will worry you without giving you an action. Skip if you are outside the US; FERPA does not apply to you.

### r-1b3a17375f - AI in assignment design - Cornell Center for Teaching Innovation

- **before:** Skip if you want Claude-specific instructions - this is tool-neutral pedagogy and never names a product. Skip if you teach school; the examples assume semester-length US higher-education courses.
- **after:**  You want Claude-specific instructions - this is tool-neutral pedagogy and never names a product. Skip if you teach school; the examples assume semester-length US higher-education courses.

### r-3ef5584cd6 - The AI Assessment Scale (AIAS)

- **before:** Skip if you are looking for a way to catch cheating - the scale is about designing tasks, not policing them, and it deliberately refuses to name a 'best' level. Skip if you need K-12 examples; adoption so far is mostly higher education.
- **after:**  You are looking for a way to catch cheating - the scale is about designing tasks, not policing them, and it deliberately refuses to name a 'best' level. Skip if you need K-12 examples; adoption so far is mostly higher education.

### r-1b663b7646 - Guidance on AI detection, and why we're disabling Turnitin's AI detector

- **before:** Skip if you want current accuracy numbers - this is from August 2023 and the figures have moved since. Skip if you want an alternative to detection; it does not give you one. And never treat any detector score as proof against a student - false accusations fall hardest on non-native English writers.
- **after:**  You want current accuracy numbers - this is from August 2023 and the figures have moved since. Skip if you want an alternative to detection; it does not give you one. And never treat any detector score as proof against a student - false accusations fall hardest on non-native English writers.

### r-71c0227d56 - Using AI in education settings: support materials (UK DfE)

- **before:** Skip if you are outside England - the safeguarding, data and KCSIE references are UK-specific. Skip if you want tool training; it is deliberately generic and never mentions Claude.
- **after:**  You are outside England - the safeguarding, data and KCSIE references are UK-specific. Skip if you want tool training; it is deliberately generic and never mentions Claude.

### r-6b4b766e56 - The Australian Framework for Generative AI in Schools

- **before:** Skip if you want classroom activities; it is a policy framework with no lesson material in it. Skip if you need legal certainty - each state and territory applies it differently.
- **after:**  You want classroom activities; it is a policy framework with no lesson material in it. Skip if you need legal certainty - each state and territory applies it differently.

### r-b19d02a867 - UNESCO AI competency framework for teachers

- **before:** Skip if you want anything practical for Monday - it is a competency map, not training, and contains no prompts or activities. Skip if you already follow a national framework such as the UK or Australian one.
- **after:**  You want anything practical for Monday - it is a competency map, not training, and contains no prompts or activities. Skip if you already follow a national framework such as the UK or Australian one.

### r-6a15e8b9c3 - Ethical guidelines on the use of AI and data in teaching and learning for educators (EU)

- **before:** Skip if you want tool instructions - it never names a product. Skip if you are outside the EU; the legal hooks will not match your rules.
- **after:**  You want tool instructions - it never names a product. Skip if you are outside the EU; the legal hooks will not match your rules.

### r-11991cab3c - Day of AI - free K-12 AI literacy curriculum (MIT RAISE)

- **before:** Skip if you want to learn Claude yourself - this is student-facing and tool-neutral. Skip if you need something that fits one lesson; the units are designed as sequences across several sessions.
- **after:**  You want to learn Claude yourself - this is student-facing and tool-neutral. Skip if you need something that fits one lesson; the units are designed as sequences across several sessions.

### r-6da5a506f4 - Empowering Education Leaders: a toolkit for safe, ethical and equitable AI integration

- **before:** Skip if you are a classroom teacher - it is written for people who set district policy and buy software. Skip if you need current guidance; it is from October 2024 and predates most of what teachers now use daily.
- **after:**  You are a classroom teacher - it is written for people who set district policy and buy software. Skip if you need current guidance; it is from October 2024 and predates most of what teachers now use daily.

### r-c8ea212793 - Getting started with Claude.ai

- **before:** Skip if you already use Claude most days, because this never goes past explaining what each button does.
- **after:**  You already use Claude most days, because this never goes past explaining what each button does.

### r-5a3db6848c - Getting started with projects in Claude.ai

- **before:** Skip if you only ask Claude one-off questions, because Projects add setup work you will not get back.
- **after:**  You only ask Claude one-off questions, because Projects add setup work you will not get back.

### r-638606c3f0 - Getting started with research in Claude.ai

- **before:** Skip if you need controlled academic sourcing, because this is a short feature demo and says nothing about citation quality.
- **after:**  You need controlled academic sourcing, because this is a short feature demo and says nothing about citation quality.

### r-ac6eff0ef2 - What are skills?

- **before:** Skip if you want to build a Skill today, because this explains only the concept and shows no file structure or authoring steps.
- **after:**  You want to build a Skill today, because this explains only the concept and shows no file structure or authoring steps.

### r-f4a911fbc0 - Getting started with Claude Cowork

- **before:** Skip if your plan does not include Cowork, because you cannot follow along with any of it.
- **after:**  Your plan does not include Cowork, because you cannot follow along with any of it.

### r-2f546497f1 - Getting started with Claude in Excel

- **before:** Skip if you are on the free plan, because Claude in Excel is a research preview for Pro, Max, Team and Enterprise only.
- **after:**  You are on the free plan, because Claude in Excel is a research preview for Pro, Max, Team and Enterprise only.

### r-7720f251bd - Lesson 1: Introduction to AI Fluency | AI Fluency: Framework & Foundations Course |

- **before:** Skip if you want hands-on Claude technique, because this lesson only sets up the course frame and teaches no prompting.
- **after:**  You want hands-on Claude technique, because this lesson only sets up the course frame and teaches no prompting.

### r-df3de5cb89 - Lesson 2B: The 4D Framework | AI Fluency: Framework & Foundations Course

- **before:** Skip if you dislike frameworks and learn better from worked examples, because this lesson is all structure.
- **after:**  You dislike frameworks and learn better from worked examples, because this lesson is all structure.

### r-e54eb50967 - Lesson 7: Effective prompting techniques (Deep Dive) | AI Fluency: Framework & Foundations Course

- **before:** Skip if you build on the API, because Anthropic's own prompt engineering deep dive covers far more for that audience.
- **after:**  You build on the API, because Anthropic's own prompt engineering deep dive covers far more for that audience.

### r-e6aff5f442 - AI prompt engineering: A deep dive

- **before:** Skip if you have never prompted Claude yourself, because the whole discussion assumes you have already hit these problems.
- **after:**  You have never prompted Claude yourself, because the whole discussion assumes you have already hit these problems.

### r-a4e8419f79 - Prompting 101 | Code w/ Claude

- **before:** Skip if you only use the Claude chat app, because the session is framed around API calls and system prompts.
- **after:**  You only use the Claude chat app, because the session is framed around API calls and system prompts.

### r-8f05ffaa7f - What is Claude Code?

- **before:** Skip if you have already run Claude Code on a real task, because nothing here will be new.
- **after:**  You have already run Claude Code on a real task, because nothing here will be new.

### r-7f3c49d115 - The CLAUDE.md file

- **before:** Skip if you already maintain a tuned CLAUDE.md, because this stays at the level of writing your first one.
- **after:**  You already maintain a tuned CLAUDE.md, because this stays at the level of writing your first one.

### r-927657d732 - The Explore → Plan → Code → Commit workflow in Claude Code

- **before:** Skip if you already plan and review before you commit, because this only names a habit you have.
- **after:**  You already plan and review before you commit, because this only names a habit you have.

### r-91bd3a4786 - MCP in Claude Code

- **before:** Skip if you have not used Claude Code yet, because MCP only pays off once your basic loop works.
- **after:**  You have not used Claude Code yet, because MCP only pays off once your basic loop works.

### r-e09981c25f - Mastering Claude Code in 30 minutes

- **before:** Skip if you have never opened Claude Code, because the pace assumes you already know the basic loop.
- **after:**  You have never opened Claude Code, because the pace assumes you already know the basic loop.

### r-ed4346440d - Claude Code best practices | Code w/ Claude

- **before:** Skip if you have not written a CLAUDE.md yet, because the advice assumes the basics are already in place.
- **after:**  You have not written a CLAUDE.md yet, because the advice assumes the basics are already in place.

### r-060f30c2a1 - Beyond the basics with Claude Code

- **before:** Skip if you are still learning the basic prompt loop, because this assumes you already ship with Claude Code daily.
- **after:**  You are still learning the basic prompt loop, because this assumes you already ship with Claude Code daily.

### r-439ea99e4e - The Model Context Protocol (MCP)

- **before:** Skip if you want to write an MCP server today, because this stays conceptual and shows no code.
- **after:**  You want to write an MCP server today, because this stays conceptual and shows no code.

### r-0006a6ee09 - Tips for building AI agents

- **before:** Skip if a single well-shaped prompt already solves your problem, because agents add cost and failure modes you do not need.
- **after:**  A single well-shaped prompt already solves your problem, because agents add cost and failure modes you do not need.

### r-9d3aadf6a3 - Claude Code for Beginners Tutorial [Full Course]

- **before:** Skip if you already run Claude Code daily. The first two hours cover install, permissions, and basic prompting, and you will only get the last part of value for four and a half hours of time.
- **after:**  You already run Claude Code daily. The first two hours cover install, permissions, and basic prompting, and you will only get the last part of value for four and a half hours of time.

### r-fe5b9ebe20 - Claude Code Tutorial - Build Apps 10x Faster with AI

- **before:** Skip if you want MCP, subagents, or hooks. This stays on core coding work and does not touch the extension layer.
- **after:**  You want MCP, subagents, or hooks. This stays on core coding work and does not touch the extension layer.

### r-a5e8a7bac1 - Claude Code Crash Course For Developers

- **before:** Skip if you are new to the terminal or to git. The pace assumes you already know your stack and only need the Claude Code part.
- **after:**  You are new to the terminal or to git. The pace assumes you already know your stack and only need the Claude Code part.

### r-c01814ac25 - Complete Claude Code Course In 2 Hours For Developers

- **before:** Skip if you want polished production and tight editing. The delivery is live and repeats itself, so two hours holds about ninety minutes of content.
- **after:**  You want polished production and tight editing. The delivery is live and repeats itself, so two hours holds about ninety minutes of content.

### r-29661436b2 - CLAUDE CODE Full Course For Beginners (DATA DOMAIN Edition)

- **before:** Skip if you only have one evening. At 6:47 it needs a real schedule, and a shorter course will teach you the same basics faster.
- **after:**  You only have one evening. At 6:47 it needs a real schedule, and a shorter course will teach you the same basics faster.

### r-6419a4a3bf - My Claude Code Workflow for 2026

- **before:** Skip if you want step-by-step instruction. This is one person's opinion of a good setup, not a tutorial you can copy line by line.
- **after:**  You want step-by-step instruction. This is one person's opinion of a good setup, not a tutorial you can copy line by line.

### r-0d9d05fefc - How I use Claude Code for real engineering

- **before:** Skip if you want a hands-on build. It is a walkthrough of a way of thinking, and at ten minutes it explains more than it demonstrates.
- **after:**  You want a hands-on build. It is a walkthrough of a way of thinking, and at ten minutes it explains more than it demonstrates.

### r-b05c78ed77 - Red Green Refactor is OP With Claude Code

- **before:** Skip if you do not already know how to write a test in your language. The video assumes the red-green-refactor cycle and only adds the agent part.
- **after:**  You do not already know how to write a test in your language. The video assumes the red-green-refactor cycle and only adds the agent part.

### r-5d7c70895f - Claude Code Task System: ANTI-HYPE Agentic Coding (Advanced)

- **before:** Skip if you have not used subagents yet. The video starts where most tutorials end and will not slow down for you.
- **after:**  You have not used subagents yet. The video starts where most tutorials end and will not slow down for you.

### r-bb41b4ccac - Parallel Claude Code + Git Worktrees: This Setup Will Change How You Ship

- **before:** Skip if you work on one feature at a time. Running many agents adds review load, and with a single task it costs you more than it saves.
- **after:**  You work on one feature at a time. Running many agents adds review load, and with a single task it costs you more than it saves.

### r-02984ea890 - Git Worktrees Explained — Run Multiple AI Agents in Parallel (Claude Code Tutorial)

- **before:** Skip if you already use worktrees. Most of the twenty minutes explains the git feature, not the Claude Code part.
- **after:**  You already use worktrees. Most of the twenty minutes explains the git feature, not the Claude Code part.

### r-0cef6247ae - Completely understand hooks in less than 20 minutes

- **before:** Skip if you do not write shell scripts. Every example is a bash file, and without that you cannot use any of it.
- **after:**  You do not write shell scripts. Every example is a bash file, and without that you cannot use any of it.

### r-a2105632bc - Hooks in Claude Code — Full Theory + Practical Use | CampusX

- **before:** Skip if you just want a working hook today. The first half is architecture, and you will wait a long time for the file you can copy.
- **after:**  You just want a working hook today. The first half is architecture, and you will wait a long time for the file you can copy.

### r-ef1045fa72 - Claude Code Headless Automation & Agent Workflows

- **before:** Skip if you have no CI system. Without a pipeline to put it in, headless mode has nowhere to go.
- **after:**  You have no CI system. Without a pipeline to put it in, headless mode has nowhere to go.

### r-c8d8026843 - Claude Code Sub-Agents: Step-by-Step Beginner Tutorial

- **before:** Skip if you already write agent definition files. The pace is slow and there is nothing here about limiting tools or designing output formats.
- **after:**  You already write agent definition files. The pace is slow and there is nothing here about limiting tools or designing output formats.

### r-72f66fc93f - Stop Confusing Skills and Subagents in Claude Code (Watch This)

- **before:** Skip if you want build instructions. It sorts out the concepts in nine minutes and leaves the typing to you.
- **after:**  You want build instructions. It sorts out the concepts in nine minutes and leaves the typing to you.

### r-897ecaef49 - Claude Code Skills + Subagents: Build a Security Scanner

- **before:** Skip if you do not know the OWASP Top 10. The video explains the Claude parts, not the vulnerabilities.
- **after:**  You do not know the OWASP Top 10. The video explains the Claude parts, not the vulnerabilities.

### r-646ba2376f - 8 Claude Code Skills Every Developer Needs in 2026

- **before:** Skip if you have not made a skill yet. It shows finished skills running and does not teach you the file format from zero.
- **after:**  You have not made a skill yet. It shows finished skills running and does not teach you the file format from zero.

### r-019479b8e5 - How Model Context Protocol (MCP) actually works

- **before:** Skip if you want to write an MCP server today. There is no code and no setup, only the model of how it works.
- **after:**  You want to write an MCP server today. There is no code and no setup, only the model of how it works.

### r-59c1cdaa47 - MCP Tutorial for Beginners: Connect Claude to Any Tool (2026)

- **before:** Skip if you write servers already. It spends most of the time on Python basics and setup, and covers nothing about remote hosting or authentication.
- **after:**  You write servers already. It spends most of the time on Python basics and setup, and covers nothing about remote hosting or authentication.

### r-86179f9b6f - Build an MCP Server from Scratch in 2026 | Local, Remote, OAuth & Claude Skills

- **before:** Skip if you only want to install existing MCP servers. This is a production build with auth and deployment, and it is far more than a user needs.
- **after:**  You only want to install existing MCP servers. This is a production build with auth and deployment, and it is far more than a user needs.

### r-f1a6a369d2 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic

- **before:** Skip if you use Claude Code and have no plan to write software around it. This is SDK work and expects you to be comfortable in Python or TypeScript.
- **after:**  You use Claude Code and have no plan to write software around it. This is SDK work and expects you to be comfortable in Python or TypeScript.

### r-b108b1b8f6 - You Can Build The Craziest Things with Claudes Agent SDK

- **before:** Skip if you already decided to use the SDK. Watch the AI Engineer workshop instead, because this one stops before the hard parts.
- **after:**  You already decided to use the SDK. Watch the AI Engineer workshop instead, because this one stops before the hard parts.

### r-6b9e11235c - I Built an Agentic Software Factory with Codex and Claude Code

- **before:** Skip if you are still learning Claude Code basics. This assumes CI, GitHub automation, and a review process you already trust.
- **after:**  You are still learning Claude Code basics. This assumes CI, GitHub automation, and a review process you already trust.

### r-7dac023c0c - How I Use Claude Code as a Data Analyst (10 Real Use Cases)

- **before:** Skip if you have never used a command line. The video assumes you can already run Python from a terminal and navigate folders.
- **after:**  You have never used a command line. The video assumes you can already run Python from a terminal and navigate folders.

### r-70115e8537 - Claude AI Tutorial for Beginners (Step-by-Step)

- **before:** Skip if you already use Claude weekly. This stops at the basics and teaches nothing about Projects, files, or getting better output from harder tasks.
- **after:**  You already use Claude weekly. This stops at the basics and teaches nothing about Projects, files, or getting better output from harder tasks.

### r-496c145f5c - Full Claude Tutorial: Beginner to Advanced in 19 Minutes

- **before:** Skip if you have never opened Claude at all - it moves too fast to be a true first video. Also skip if you want depth on one workflow rather than broad coverage.
- **after:**  You have never opened Claude at all - it moves too fast to be a true first video. Also skip if you want depth on one workflow rather than broad coverage.

### r-c05fa5a028 - FULL Claude Tutorial for Beginners in 2026! (Become a PRO!)

- **before:** Skip if you only have ten minutes, or if you dislike the high-energy YouTube tutorial style with heavy editing and channel promotion between sections.
- **after:**  You only have ten minutes, or if you dislike the high-energy YouTube tutorial style with heavy editing and channel promotion between sections.

### r-143f1aa35d - FULL Claude Tutorial For Beginners in 2026! (FULL COURSE)

- **before:** Skip if you are impatient or already comfortable with chat AI tools - the deliberate pace will frustrate you, and the first half hour will be familiar.
- **after:**  You are impatient or already comfortable with chat AI tools - the deliberate pace will frustrate you, and the first half hour will be familiar.

### r-9b8a0da5f7 - Claude AI Step-by-Step: The Beginner's Blueprint for Real Results

- **before:** Skip if you want feature coverage - Projects, Cowork, and Skills are barely touched. Also skip if you already write good prompts.
- **after:**  You want feature coverage - Projects, Cowork, and Skills are barely touched. Also skip if you already write good prompts.

### r-1eac95e29e - NEW: Claude's 'Super Prompts' Will Save You DAYS of Work (Full Tutorial + Demo)

- **before:** Skip if you have never used Claude - this assumes you already know the interface. The title is louder than the calm, analytical content, so skip if that framing puts you off.
- **after:**  You have never used Claude - this assumes you already know the interface. The title is louder than the calm, analytical content, so skip if that framing puts you off.

### r-d626dfd75e - How to Use Claude Projects (Full Tutorial)

- **before:** Skip if you already use Projects. This covers setup only and does not get into organising a large knowledge base or when Projects is the wrong choice.
- **after:**  You already use Projects. This covers setup only and does not get into organising a large knowledge base or when Projects is the wrong choice.

### r-6191435073 - Learn 80% of Claude Cowork in Under 20 Minutes

- **before:** Skip if you want the remaining 20 percent - advanced setup, custom skills, and edge cases are deliberately left out. Also skip if you do not have a paid Claude plan, since Cowork needs one.
- **after:**  You want the remaining 20 percent - advanced setup, custom skills, and edge cases are deliberately left out. Also skip if you do not have a paid Claude plan, since Cowork needs one.

### r-fb2d847a41 - My Simple Claude Cowork System (for normal people)

- **before:** Skip if you have not tried Cowork yet - start with his 20-minute intro instead. Skip too if you want a general Claude tutorial, since this is narrow by design.
- **after:**  You have not tried Cowork yet - start with his 20-minute intro instead. Skip too if you want a general Claude tutorial, since this is narrow by design.

### r-5ef8f24b43 - Claude AI for Researchers: Projects, Skills, Cowork & Consensus Explained

- **before:** Skip if you are not doing academic or literature-heavy work - the examples will not transfer. Also skip if you want deep coverage of one feature rather than a tour of four.
- **after:**  You are not doing academic or literature-heavy work - the examples will not transfer. Also skip if you want deep coverage of one feature rather than a tour of four.

### r-6102637486 - How To Use Claude For Academic Research (My Actual AI Stack)

- **before:** Skip if you need step-by-step instructions - this is a workflow overview and assumes you can operate the tools yourself. Not useful outside academic writing.
- **after:**  You need step-by-step instructions - this is a workflow overview and assumes you can operate the tools yourself. Not useful outside academic writing.

### r-9dbd5f5607 - 3 Mind Blowing Claude & Consensus Research Workflows | No Coding

- **before:** Skip if you will not use Consensus - two of the three workflows depend on it. Skip if you want general Claude skills rather than research-specific recipes.
- **after:**  You will not use Consensus - two of the three workflows depend on it. Skip if you want general Claude skills rather than research-specific recipes.

### r-0545b73dfe - Claude Cowork for Academics: Full Setup & Use Cases

- **before:** Skip if you do not keep your research as local files, or if you are still deciding whether to pay for Claude - Cowork requires a paid plan.
- **after:**  You do not keep your research as local files, or if you are still deciding whether to pay for Claude - Cowork requires a paid plan.

### r-598bb88527 - Claude AI for Teachers: Complete Beginner's Guide to Getting Started (Projects, Prompts & More)

- **before:** Skip if you already use AI in your teaching - the pace and level are aimed squarely at first-timers. Not useful for university lecturers or corporate trainers.
- **after:**  You already use AI in your teaching - the pace and level are aimed squarely at first-timers. Not useful for university lecturers or corporate trainers.

### r-a80189a012 - How Teachers Can Create Interactive Classroom Activities with AI (Claude Artefacts Tutorial)

- **before:** Skip if you only need text output like lesson plans and worksheets - Artifacts is overkill for that. From January 2026, so the interface has shifted slightly since.
- **after:**  You only need text output like lesson plans and worksheets - Artifacts is overkill for that. From January 2026, so the interface has shifted slightly since.

### r-1446dfba71 - Claude Design: The Complete Guide

- **before:** Skip if you have no design background - the critique assumes you can tell good layout from bad. Skip too if you want Figma integration, which is not the focus.
- **after:**  You have no design background - the critique assumes you can tell good layout from bad. Skip too if you want Figma integration, which is not the focus.

### r-1cab275cb5 - Claude Design Tutorial for Designers | First Look + Full Walkthrough!

- **before:** Skip if you want a clean reference tutorial - this is exploratory and occasionally meanders. Recorded at launch, so some rough edges shown have since been fixed.
- **after:**  You want a clean reference tutorial - this is exploratory and occasionally meanders. Recorded at launch, so some rough edges shown have since been fixed.

### r-0d2b1cdbba - Claude Code for product managers: research, writing, context libraries, custom to-do system, more

- **before:** Skip if the terminal intimidates you - the tool is command-line even though the work is not technical. Skip too if you want a quick tips list rather than 43 minutes of one person's system.
- **after:**  The terminal intimidates you - the tool is command-line even though the work is not technical. Skip too if you want a quick tips list rather than 43 minutes of one person's system.

### r-76a7a8999e - Claude Code for Product Managers with Sachin Rekhi

- **before:** Skip if you are new to product management - the conversation assumes fluency in PM vocabulary. Skip if you want a hands-on tutorial, since much of this is discussion.
- **after:**  You are new to product management - the conversation assumes fluency in PM vocabulary. Skip if you want a hands-on tutorial, since much of this is discussion.

### r-8897af0a88 - Claude Cowork: The Ultimate AI Agent for Writers (Full Tutorial)

- **before:** Skip if you write short pieces - the whole advantage here is scale. Skip if you object to AI in creative writing on principle, since he does not debate that question.
- **after:**  You write short pieces - the whole advantage here is scale. Skip if you object to AI in creative writing on principle, since he does not debate that question.

### r-11acf1db6f - Claude Cowork Just Changed How You Do Marketing

- **before:** Skip if you want a quick overview - this is a long working session. The title is overstated and there is channel promotion in places, so skip if that grates.
- **after:**  You want a quick overview - this is a long working session. The title is overstated and there is channel promotion in places, so skip if that grates.

### r-c2dd3f226c - Anthropic Just Dropped Claude for Small Businesses (31 Skills)

- **before:** Skip if you do not run a business - the framing is entirely commercial. The news-style title means the first minutes are announcement rather than instruction.
- **after:**  You do not run a business - the framing is entirely commercial. The news-style title means the first minutes are announcement rather than instruction.

### r-023b082bb5 - How to setup Claude for Small Business

- **before:** Skip if you need convincing first - there is no case-making here, just instructions. Too shallow if you want to design a serious multi-person workflow.
- **after:**  You need convincing first - there is no case-making here, just instructions. Too shallow if you want to design a serious multi-person workflow.

### r-b857f5251c - Master Claude for Excel in 10 Minutes: Financial Modeling

- **before:** Skip if you do not use Excel or have no paid Claude plan, since the add-in requires one. Skip if your spreadsheets are simple lists rather than models - this is aimed at financial modelling.
- **after:**  You do not use Excel or have no paid Claude plan, since the add-in requires one. Skip if your spreadsheets are simple lists rather than models - this is aimed at financial modelling.

### r-bf694c1746 - How Anthropic's Growth Marketing team cut ad creation from 30 minutes to 30 seconds

- **before:** Skip if you already build your own tooling — the lesson here is that a non-coder can, which you know. Skip too if you want prompt craft rather than workflow automation.
- **after:**  You already build your own tooling — the lesson here is that a non-coder can, which you know. Skip too if you want prompt craft rather than workflow automation.

### r-a3392f8b76 - Create on-brand content (use case)

- **before:** Skip if you write in your own voice for yourself — this is aimed at holding a consistent voice across a team or a brand.
- **after:**  You write in your own voice for yourself — this is aimed at holding a consistent voice across a team or a brand.

