# The page's own nouns, put back

FIX-31: *"Take every row's `questions[]` as they were at `6021258`, run them against
today's index, and list every row its old questions no longer find in the top three. For
each, the page's own nouns went missing in the rewrite; put them back from the page, keep
the reader's phrasing beside them, log old → new."*

## Narrowing the list to a signal

Asking whether a row's old questions still retrieve it returns 266 rows, and most of that
is noise: a different sentence answered better by a different row is the catalogue working,
not a fault. `tmp/dropped_nouns.py` narrows it to what the brief actually names - a page's
own noun that went missing - by reporting a word only when all of this holds:

- it was in the row's questions before the rewrite and is not in them now,
- no inflection of it is in them now, so the stemmer is not already covering it,
- it is printed in the row's own page-derived fields: title, summary, `teaches`, `keywords`,
- it is selective, IDF at or above 3.0, so it is held by roughly thirty rows or fewer, and
- an old question carrying it no longer finds the row in the top three.

That is **118 rows**. Sixty-odd of the words are real subject nouns - `kensho`, `4d`,
`typography`, `hallucination`, `sycophancy`, `microcopy`, `pull requests`, `knowledge base`
- and the rest are verbs and adjectives that carry no subject: `ask`, `decide`, `honest`,
`safely`, `better`, `simple`, `good`.

## What was decided

**74 rows repaired.** Each keeps the reader's phrasing and gets the page's word back into
one question, or a fifth question where all four were load-bearing. **44 left alone**,
because the dropped word was not a noun the page owns. The list below is every repair,
old and new.

## Two things this pass got wrong, and one it could not fix

**One repair broke the gate.** Adding "when must a student cite ai use" to Cornell's
academic-integrity page pushed *Referencing AI and Acknowledging AI Use* out of the top
three for "how do i cite claude in my references". Cornell's page is about syllabus policy
and evidence, not about how to cite; the question over-claimed. Reverted, and the row is
back to four questions. The gate caught it in the same build, which is the point of the
round.

**One repair dropped a word while restoring another.** Changing *Lesson 2B*'s first
question from "the four competencies of ai fluency" to "the 4d framework of ai fluency"
put `4d` back and took `four` out. Both are now there. The detector caught it on the
re-run, which is why the re-run happened.

**One word cannot be fixed a row at a time.** *Set Your Standards Before You Start* is
about a personal `CLAUDE.md`. The catalogue indexes that as one token, `claudemd`; a reader
types "claude.md", which tokenises to `claude` and `md`. Writing `claudemd` into a question
would be writing for the index rather than for the reader. This is a spelling-map job, not
a question-wording job, and it is written down here rather than bodged.

## Old → new


### MCP: Build Rich-Context AI Apps with Anthropic — r-011e20ba3e
- was: mcp course from anthropic | how do i build my own mcp server | learn mcp client and server in one go | how do i test an mcp server i wrote
- now: mcp course from anthropic | how do i build my own mcp server | learn mcp tools resources and prompts in one go | how do i test an mcp server i wrote

### How to setup Claude for Small Business — r-023b082bb5
- was: claude for small business setup | how do i set this up for my business | what do i do first after signing up | fastest way from signup to something useful
- now: claude for small business setup | how do i set this up for my business | what do i do first after signing up | connect our company documents and get something useful

### Beyond the basics with Claude Code — r-060f30c2a1
- was: claude code beyond the basics | how do we get a whole team using it the same way | what belongs in a claude md file | how do i package our conventions so everyone gets them
- now: claude code beyond the basics | how do we get a whole team using it the same way | what belongs in a claude md file | how do i package our conventions so everyone gets them | run it in auto mode without it going wrong

### PM Skills Marketplace (Paweł Huryn) — r-07f903de70
- was: pm skills and plugins for claude cowork | where do i get ready-made product management workflows | how do i write a product spec faster | can something pressure-test my spec before review
- now: pm skills and plugins for claude cowork | ready-made product management commands and workflows | how do i write a product spec faster | can something pressure-test my spec before review

### Mushtaq Bilal — Claude for Academic Writing & Research — r-0ccfc4f72a
- was: claude for academic writing and research | i am not technical and i work in academia | can it help screen papers for a systematic review | approachable guidance for research writing
- now: claude for academic writing and research | i am not technical and i work in academia | screen the literature for a systematic review | approachable guidance for research writing

### Tasks to try with Claude Tag in your workspace — r-0fcc607c0b
- was: claude tag tasks in slack | what can i actually ask it to do in a channel | when does it answer without being tagged | give me real examples not a chat partner
- now: claude tag tasks in slack | what can i actually ask it to do in a channel | when does it answer without being tagged | open a pull request from a channel

### Generate an AI policy — r-13ab6fa70b
- was: write an ai usage policy | we need rules for staff using ai | what should an ai policy actually say | draft a policy without hiring a consultant
- now: write an ai usage policy | we need rules for staff using ai | what should an ai policy actually say | draft a policy without hiring a consultant | a workbook for putting the policy in place

### FULL Claude Tutorial For Beginners in 2026! (FULL COURSE) — r-143f1aa35d
- was: full claude tutorial for beginners | a long course i can follow along with | take me through everything slowly | nothing skipped and nothing assumed
- now: full claude tutorial for beginners | a long course i can follow along with | take me through everything slowly | every feature shown and nothing skipped

### Claude Design: The Complete Guide — r-1446dfba71
- was: claude design reviewed by a designer | is the design output any good | will it hold together as a system | an honest opinion rather than a feature tour
- now: claude design reviewed by a designer | is the ui it makes any good | will it hold together as a system | an honest opinion rather than a feature tour

### Claude AI Comprehensive Guide — r-158b800917
- was: claude course with a certificate | structured lessons with marking at the end | copywriting and marketing with ai | something to show for finishing it
- now: claude comprehensive guide on coursera | structured lessons with marking at the end | copywriting and marketing with ai | a certified course with something to show for it

### Introduction to subagents — r-185e71d34e
- was: claude code subagents | my session runs out of room | split a big job across several helpers | give each part its own context
- now: claude code subagents | my session runs out of room | split a big job across several helpers | give each part its own context | build one with the agents command

### AI Fluency for students — r-1cbd9f78df
- was: ai fluency course for students | how do i use it to learn rather than to cheat | the official view of good ai use | using ai for career planning as a student
- now: ai fluency course for students | how do i use it to learn rather than to cheat | the 4d framework applied to student life | using ai for career planning as a student

### Using S&P global data for financial analysis — r-25738ca991
- was: s and p global data in claude | pull market and fundamental data | map suppliers customers and partners | competitor lists from filings
- now: s and p global data through kensho | pull market and fundamental data | map suppliers customers and partners | competitor lists from filings

### CLAUDE CODE Full Course For Beginners (DATA DOMAIN Edition) — r-29661436b2
- was: claude code course for data work | a full course that is not about building apps | set up mcp for data workflows | hooks and skills for analysis rather than software
- now: claude code course for data work | a full course that is not about building apps | set up mcp servers for data workflows | hooks and skills for analysis rather than software

### Claude Code settings and permission rules — r-3007ca1afd
- was: claude code permissions and settings | how do i stop it running things without asking | where did that permission get saved | can i keep it out of one folder
- now: claude code permissions and settings | how do i stop it running things without asking | where did that permission get saved | write a rule that keeps it out of a folder

### Using Claude Design for prototypes and UX — r-3104499980
- was: prototyping and ux in claude design | the honest overview of what it does | connect it to our codebase for realistic mockups | hand a design off to be built
- now: prototyping and ux in claude design | the honest overview of what it does | connect our production codebase for realistic mockups | hand a design off to be built

### Organize Your Tasks With Projects in Claude Cowork — r-36de89a1ed
- was: projects in claude cowork | stop re-explaining the same long job | keep instructions and files together for weeks | work that runs for months not one chat
- now: projects in claude cowork | stop re-explaining the same long job | keep instructions and a local folder together for weeks | recurring work that runs for months not one chat

### Set Your Standards Before You Start: A Journalist's Journey Using Claude.md — r-3b623d0e24
- was: a journalist's rules for using claude | how do i stop it inventing quotes | what should my own ground rules be | do i have to tell readers i used ai
- now: a journalist's rules for using claude | how do i stop it inventing quotes | what should my own claude md say | do i have to tell readers i used ai

### Claude for Designers in 2026: Where AI Actually Helps — r-493d22de63
- was: claude for designers | where does it actually help my design work | where does it get in the way | an honest orientation before i start
- now: claude for designers | does it help with ux copy and reviewing screens | where does it get in the way | an honest orientation before i start

### Full Claude Tutorial: Beginner to Advanced in 19 Minutes — r-496c145f5c
- was: full claude tutorial in under twenty minutes | a map of what the product can do | features i have probably missed | one sitting and then i am off
- now: full claude tutorial in under twenty minutes | projects artifacts and file uploads in one map | features i have probably missed | one sitting and then i am off

### Use Claude Cowork on web, desktop, and mobile — r-4bf690867e
- was: claude cowork on web desktop and mobile | do i need to install the desktop app | does it keep working when i shut the laptop | which features only work in one place
- now: claude cowork on web desktop and mobile | do i need the desktop app for local files and the browser | does it keep working when i shut the laptop | which features only work in one place

### Can you trust what AI tells you? — r-4c75fa41f0
- was: can i trust what ai tells me | how much should i believe the answer | it sounds confident and i cannot tell | the two ways it goes wrong
- now: can i trust what ai tells me | how much should i believe the answer | it sounds confident and i cannot tell | hallucination and sycophancy explained simply

### Claude Code overview and install guide — r-4d17281029
- was: install claude code | the right command for my operating system | set it up inside my editor | first run on windows
- now: install claude code | the right cli install command for my operating system | set it up inside my editor | first run on windows

### AI: Artificial Intelligence Resources: Claude — r-4fce76b7b9
- was: claude next to the other ai tools | which tool should i open first for research | a short neutral summary from a library | what is it weak at for academic work
- now: claude next to chatgpt and the other ai tools | which tool should i open first for research | a short neutral summary from a library | what is it weak at for academic work

### Peer and AI Review of Student Writing with Marit MacArthur and Anna Mills — r-521c6b7dca
- was: peer review and ai feedback on student writing | why is my class being taught this way | does ai feedback actually help my writing | the research behind the approach
- now: peer review and ai feedback on student writing | why is my class being taught this way | does ai feedback actually help my writing | the research behind the approach | feedback for writers whose first language is not english

### Scaling workflows with Claude Cowork at your organization — r-529b6c65e3
- was: rolling out claude cowork across an organisation | the pilot worked so what now | control which team reaches which system | governance before we go wide
- now: rolling out claude cowork across an organisation | the pilot worked so what now | limit which team reaches which system | governance before we go wide

### How to install and use the Claude for Small Business plugin — r-52edcc6d27
- was: install the claude for small business plugin | the exact steps to set it up | connect our accounting and crm | what comes with it once installed
- now: install the claude for small business plugin | the exact steps to set it up | connect quickbooks paypal and hubspot | what comes with it once installed

### Claude AI for Teachers: Complete Beginner's Guide to Getting Started (Projects, Prompts & More) — r-598bb88527
- was: claude for teachers beginner guide | differentiate a worksheet for my class | write parent emails faster | examples from teaching not from an office
- now: claude for teachers beginner guide | differentiate a worksheet for my high school class | write parent emails faster | examples from teaching not from an office

### AI capabilities and limitations — r-59f8585925
- was: what claude can and cannot do | what should i not trust it with | where does it get things wrong | set my expectations before real work
- now: what claude can do and its limitations | what should i not trust it with | where does it get things wrong | set my expectations before real work

### Claude Code Task System: ANTI-HYPE Agentic Coding (Advanced) — r-5d7c70895f
- was: how claude code breaks work into tasks | shape the breakdown instead of fighting it | run several agents on one job | the layer underneath the commands
- now: how claude code breaks work into tasks | shape the breakdown instead of fighting it | orchestrate subagents on one job | the layer underneath the commands

### Claude AI for Researchers: Projects, Skills, Cowork & Consensus Explained — r-5ef8f24b43
- was: claude for researchers | screen papers and draft a methods section | pair it with a search tool for real citations | every feature explained in academic terms
- now: claude for researchers | screen literature and draft a methods section | pair it with a search tool for real citations | every feature explained in academic terms

### Use cases for Legal — r-6502c8e711
- was: claude use cases for legal work | what can a legal team hand over | triage an agreement without reading every clause | before we commission anything of our own
- now: claude use cases for legal work | what can a legal team hand over | triage an nda or a contract without reading every clause | before we commission anything of our own

### Production Ready Agentic AI PM Certification and Claude Cert Prep (Maven) — r-66cc1560b7
- was: certification for shipping ai products | move into an ai product role | i need a portfolio project and an eval story | a live cohort rather than videos
- now: certification for shipping ai products | move into an ai product role | i need a portfolio project and an eval story | a live cohort rather than videos | rag and agentic rag with evals

### What are Projects? — r-6840ddca47
- was: what a project is in claude | i keep re-pasting the same background | somewhere to keep reference files | instructions that stay between chats
- now: what a project is in claude | i keep re-pasting the same background | a knowledge base for my reference files | instructions that stay between chats

### Ethical guidelines on the use of AI and data in teaching and learning for educators (EU) — r-6a15e8b9c3
- was: eu ethical guidance for ai in schools | does this tool comply with our data law | what am i allowed to use with pupils | principles that match the law i work under
- now: eu ethical guidance for ai in schools | does this tool meet our data privacy law | what am i allowed to use with pupils | principles that match the law i work under

### 43 Claude Skills for college teachers — r-6cee334566
- was: claude skills for college teaching | the same jobs come round every semester | give feedback against a rubric at scale | stop rebuilding course materials every year
- now: claude skills for college teaching | the same jobs come round every semester | give feedback against a rubric at scale | stop rebuilding the syllabus and materials every year

### Plan your career path — r-6da1df1aac
- was: plan a career move | what skills am i missing for these jobs | compare my cv against real postings | a timeline and people to contact
- now: plan a career move | what skill gaps do these jobs show | compare my cv against real postings | a timeline and people to contact

### Product Management Plugin (official Anthropic plugin) — r-72bb76da3c
- was: official product management plugin | commands for specs roadmaps and updates | install it rather than write my own prompts | pull context from the tools we already use
- now: official product management plugin | commands for specs roadmaps and updates | install it rather than write my own prompts | pull context from slack notion and linear

### Using the Benevity connector in Claude — r-7443bef42c
- was: benevity connector for charity data | research a charity anywhere in the world | check an organisation before we donate | no account needed
- now: benevity connector for charity data | research nonprofits worldwide | check an organisation before we donate | no account needed

### Anthropic's Prompt Engineering Interactive Tutorial — r-7592adc74e
- was: interactive prompt engineering tutorial | learn prompting properly with exercises | keep my data separate from my instructions | practise rather than read
- now: interactive prompt engineering tutorial | learn prompting properly with exercises | keep my data separate from my instructions | practise rather than read | write prompts that produce correct sql

### Introducing the analysis tool in Claude.ai — r-7f2c2387f7
- was: the analysis tool in claude | why do the numbers come out right now | an exact answer from a spreadsheet file | when to use it instead of just asking
- now: the analysis tool in claude | why do the numbers come out right now | an exact answer from a csv | when to use it instead of just asking

### AI & Academic Integrity — r-84289d43e5
- was: ai and academic integrity | what should my syllabus say about ai | i suspect a student used ai | three policies i can borrow
- now: ai and academic integrity | what should my syllabus say about ai | i suspect a student used ai | three policies i can borrow | when must a student cite ai use

### Set up your design system in Claude Design — r-84558d3fb4
- was: set up a design system in claude design | feed it our brand once | every project comes out on brand | import figma exports and brand documents
- now: set up a design system in claude design | feed it our brand once | every project comes out on brand | import figma exports, tokens and components

### Claude Code for Designers: The Complete Guide — r-8e4939c735
- was: claude code for designers | production quality interface work from a designer | give it our design system as context | figma work through the terminal
- now: claude code for designers | production quality ui from a designer | give it our design system as context | figma work through the terminal

### What is Claude Code? — r-8f05ffaa7f
- was: what claude code is | how is it different from the chat window | an agent that edits files and runs commands | the mental model before i install it
- now: what claude code is | how is it different from the chat window | an agent that reads the codebase, edits files and runs commands | the mental model before i install it

### My Claude AI Review (2026): Is It Worth the Hype? — r-94c1f2a458
- was: a review of claude from an ordinary user | should i pay for the subscription | is it worth the hype | explained without developer language
- now: a review of claude from an ordinary user | should i pay for the subscription | is it worth the hype | explained without developer language | what extended thinking actually does

### Code w/ Claude Developer Conference (session recordings) — r-967880ec2e
- was: code with claude conference recordings | hear it from the people who built it | how do teams run agents in production | the reasoning behind the features
- now: code with claude conference recordings | hear it from the people who built it | how do teams run agents in production | the reasoning behind claude code, the agent sdk and mcp

### The 4 Properties of AI — r-985113a138
- was: the four properties of ai | why is it brilliant at one thing and hopeless at another | what does it not know | a first mental model
- now: the four properties of ai | why is it brilliant at one thing and hopeless at another | what does it not know | a first mental model | where its limitations come from

### AI Student Research Guide: Prompt Engineering — r-9d1939cf1e
- was: the four parts of a usable prompt | i have never thought about how i phrase it | the smallest change that improves my results | academic examples to copy
- now: the four parts of a usable prompt | i have never thought about how i phrase it | the smallest change that improves my results | academic examples a student can copy

### ux-writing-skill (open source) — r-9ee2065bff
- was: a ux writing skill | consistent error messages and buttons | enforce interface copy standards automatically | the same rules across the tools we use
- now: a ux writing skill | consistent microcopy for errors and buttons | enforce interface copy standards automatically | the same rules across the tools we use

### Maximizing the value of your Claude Code sessions — r-9f1cc05b1c
- was: what a claude code turn actually costs | i burn through my limit and cannot see why | keep the cache from resetting | which actions are expensive
- now: what a claude code turn actually costs | i burn through my limit and cannot see why | keep the cache from resetting | which actions burn the most tokens

### Turn transit time into research time — r-a40582eae8
- was: turn commute time into prep time | talk out my thoughts while travelling | have the research done before i sit down | a briefing grounded in our own documents
- now: turn commute time into prep time | dictate on mobile while travelling | have the research done before i sit down | a briefing grounded in our own documents

### Tokens: why some inputs cost more than others — r-a49a4c4aa6
- was: what a token is | why did that cost so much | predict how much text will use | why the limit moved
- now: what a token is | why is my usage bill so high | predict how much text will use | why the limit moved

### A Guide to Claude Code 2.0 and getting better at using coding agents — r-aa3fb9b26c
- was: how claude code actually behaves | what does a subagent inherit | someone who left and came back | mechanism rather than a feature list
- now: how claude code actually behaves | what does a subagent inherit | someone who left and came back | mechanism rather than a feature list | manage token usage across a long session

### Prompt engineering best practices for 2026 — r-aac1f93a7e
- was: prompt engineering best practices | my answers come out generic | a short ordered list of fixes | get clean structured output every time
- now: prompt engineering best practices | my answers come out generic | a short ordered list of fixes | get clean json out every time

### Claude Code Essentials (ExamPro full course) — r-b03b4a5725
- was: claude code essentials full course | one long guided video over the whole tool | authentication and permissions covered | rewind fork and compact a session
- now: claude code essentials full course | one long guided video over the whole tool | authentication on bedrock and vertex covered | rewind fork and compact a session

### Claude Cowork Tutorial: How to Use Anthropic's AI Desktop Agent — r-b5a28e4e25
- was: a hands-on claude cowork report | what happens on a folder with hundreds of files | show me where it fails not only the demo | rename convert and compress files in bulk
- now: a hands-on claude cowork report | what happens on a folder with hundreds of files | show me where it fails not only the demo | rename convert and compress files in bulk | where its browser automation breaks

### Claude for K-12 Teachers: context steering, Projects and Skills — r-bb9cebd574
- was: a durable teaching setup rather than one-off prompts | stop asking for a lesson plan in one prompt | put my teaching context somewhere permanent | track student progress by process not marks
- now: a k12 classroom setup rather than one-off prompts | stop asking for a lesson plan in one prompt | put my teaching context somewhere permanent | track student progress by process not marks

### Handle a request while away from your keyboard — r-bee34f76e6
- was: handle a request from my phone | the file is on my desktop and i am not there | draft a reply and post it after i approve | my computer is at home
- now: handle a request from my phone | the file is on my desktop and i am not there | draft a reply and post it after i approve | my computer is at home | what cowork dispatch does

### Use Claude for Education at your university — r-cb786e071f
- was: claude for education at my university | my university just switched it on | what do i get that a free account does not | i cannot log in with my campus account
- now: claude for education at my university | my university just switched it on | what do i get that a free account does not | i cannot log in with my campus account | what the usage limits are on a campus account

### 4 Lines You Should Include in Your Claude Skill — r-d0b62d548e
- was: lines worth putting in every skill | polished output hiding a weak conclusion | define what counts as significant | stop it making claims the data does not support
- now: lines worth putting in every skill | a polished report hiding a weak conclusion | define what counts as significant | stop it making claims the data does not support

### Introducing Claude for Teachers — r-d37ce11fa5
- was: claude for teachers announcement | am i eligible for the free offer | what exactly do teachers get | lesson planning built in
- now: claude for teachers announcement | am i eligible for the free offer | what exactly do teachers get | lesson planning built in | is it ferpa compliant

### Claude Cookbooks — r-d98aa6f2dd
- was: runnable code recipes from anthropic | working code i can modify | retrieval classification and summarisation examples | notebooks organised by the job not the feature
- now: runnable code recipes from anthropic | working code i can modify | retrieval classification and customer service agents | notebooks organised by the job not the feature

### The Guide to Claude Code for PMs — r-db64419f9d
- was: moving from cowork to claude code | i keep hitting the ceiling of cowork | what carries over and what changes | explore a codebase safely first
- now: moving from cowork to claude code | i keep hitting the ceiling of cowork | what carries over and what changes | use plan mode to explore a codebase safely

### Lesson 2B: The 4D Framework | AI Fluency: Framework & Foundations Course — r-df3de5cb89
- was: the four competencies of ai fluency | words for judging my own ai use | was that a good result or did i get lucky | the second lesson of the course
- now: the 4d framework of ai fluency | words for judging my own ai use | was that a good result or did i get lucky | the second lesson of the course

### A designer's first attempt at building with Claude Code — r-e0f2160e55
- was: a designer's first build with claude code | have it interview me into a spec | get something live my family can open | the first step i keep putting off
- now: a designer's first build with claude code | have it interview me into a spec | get something live my family can open | the first step i keep putting off | connect figma to claude code

### Map your lit review mid-conversation to surface the underlying debate — r-e31096ecec
- was: map the debate across a pile of papers | who agrees with whom and about what | where is the field actually divided | see the argument structure not a summary
- now: map the debate across a literature review | who agrees with whom and about what | where is the field actually divided | see the argument structure not a summary

### Design plugin (official) — r-ea10b7c306
- was: the official design plugin | ready-made design workflows | critique accessibility and handoff in one install | official rather than community skills
- now: the official design plugin | ready-made design workflows | ux writing, critique, accessibility and handoff in one install | official rather than community skills

### Usage limit best practices — r-ea6c1824ae
- was: make a usage limit go further | i run out before the week ends | must i pay more or can i work differently | batch questions instead of asking one at a time
- now: make a usage limit go further | i run out before the week ends | must i pay more or can i work differently | batch questions into one message instead of several

### Build financial models — r-ee8a08ce90
- was: build an investment model | scenarios and risk in one workbook | a model ready for the committee | pull the inputs from connected data
- now: build a financial or investment model | scenarios and risk in one workbook | a model ready for the committee | pull the inputs from connected data

### Agent-native Product Management (Every's guide) — r-ef99edbbfd
- was: product management run with agents | stop writing tickets entirely | a strategy document built by interview | a daily metrics report from our analytics
- now: product management run with agents | stop writing tickets entirely | a strategy document built by interview | a daily metrics report from our analytics | running a whole product solo

### Best practices for Claude Code — r-fb8dc53be9
- was: best practices for claude code | i use it daily and still get mediocre results | quality drops as the session goes on | how should i structure a task
- now: best practices for claude code | i use it daily and still get mediocre results | the context window fills and quality drops | how should i structure a task

### Practical ways to get started using Claude for educators — r-fccfc16f07
- was: practical first steps for educators | have it interview me about my role first | which student work should stay human | starting from nothing
- now: practical first steps for educators | have it interview me about my role first | which student work should stay human | starting from nothing | projects and artifacts for a teacher

### Agent Skills with Anthropic — r-ff743e0d5a
- was: agent skills course | one format that works everywhere | run the same skill in four places | build a skill from scratch properly
- now: agent skills course | one reusable format that works everywhere | run the same skill in four places | build a skill from scratch properly

### Lesson 2B: The 4D Framework | AI Fluency: Framework & Foundations Course — r-df3de5cb89 (repair of my own repair)
- was: the 4d framework of ai fluency | words for judging my own ai use | was that a good result or did i get lucky | the second lesson of the course
- now: the 4d framework of ai fluency | the four competencies, in words i can use | was that a good result or did i get lucky | the second lesson of the course
