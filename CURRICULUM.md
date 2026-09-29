# Curriculum

The plan for becoming, and proving I am, a C#/.NET full-stack engineer who is **AI-ready**, with
**SQL Server depth** as the edge. Evidence rather than claims.

First written 2026-09-17. Rebuilt 2026-09-22 and again on 2026-09-29, this time around what South
African .NET employers actually advertise (`research/2026-09-29-curriculum-sources.md`). This file
is allowed to be wrong. It is not allowed to be vague.

**No dates, no week counts, no estimated finish.** A phase is over when its capstone's exit test
passes, and not before. How long that takes is an output of the work, not an input to it.

## Purpose

I already ship production C#. What that doesn't give me on its own is a map: which skills the
market pays for at each level, in what order to learn them, and a way to prove each one in public.
This file is that map. It's organised in four levels, Junior, Intermediate, Senior and Mastery, and
each level ends in a gate I have to pass cold.

"AI-ready" means two things here, both taken from the postings:

1. **Using AI coding assistants well**, and critically reviewing what they produce. Claude Code
   is the one South African .NET postings name most.
2. **Building LLM features in C#**: calling OpenAI and Anthropic from .NET, RAG, evals, agents and
   MCP. The official `OpenAI` and `Anthropic` C# SDKs, `Microsoft.Extensions.AI`, Microsoft Agent
   Framework and the MCP C# SDK are all stable, so none of this needs Python. Python comes in at
   Senior, for AI services only.

## What the postings ask for

From 39 C#/.NET and 10 AI postings on E-Merge read in full, plus nine listings pasted in by hand,
all read 2026-09-29. Counts and URLs are in `research/2026-09-29-curriculum-sources.md`.

| Level | Postings | What recurs |
|---|---|---|
| Junior | 4 | C#, SQL Server and T-SQL, HTML/CSS/JS. Advantageous: React, .NET Core, EF Core, Azure, CI/CD, containers, "AI tools used responsibly" |
| Intermediate | 14 | ASP.NET Core Web API and SQL Server. Angular as often as React. CI/CD, EF, Azure, Docker. DDD, CQRS and Clean Architecture start to appear, and so do legacy MVC, WebForms and Dapper |
| Senior | 14 | REST design, SQL tuning, Azure (and some AWS), testing, event-driven design, messaging, Bicep or Terraform, Entra ID, GraphQL, mentoring |
| Lead | 7 | Mentoring, architecture, delivery |

- **AI coding assistants:** 8 of 39 C# postings ask for them, and Claude or Claude Code is named 6
  times. Two make it a requirement.
- **LLM integration:** only 1 C# posting requires it. Every AI-engineer posting is Python-first.
  That's why the AI track here builds in C#, and Python waits until Senior.
- **Agile:** named in 13 of 48 postings (27%). Scrum is the only method named. I run lightweight
  Scrum anyway, because it's cheap and because it's what the interview story rests on.

## Sources

Three learning platforms, one practice site, and reference reading.

- **Dometrain** (subscribed): the C# and .NET core, AI in C#, Claude Code, data structures and
  algorithms, TypeScript, and Python.
- **Udemy**, for what Dometrain doesn't teach:
  - Phillip Burton: T-SQL, AZ-900, DP-900, DP-300, DP-800 and SC-900. He has no AZ-104 course.
  - Imran Afzal: Linux.
  - Maximilian Schwarzmüller: React and Angular only. TypeScript comes from Dometrain.
  - Scott Duffy (AZ-104), Alan Rodrigues (AZ-400, SC-300, SC-100), Zeal Vora (Terraform, CKS),
    Mumshad Mannambeth (CKA), Stephane Maarek (Kafka), Aref Karimi (identity), Karthik K.K.
    (Playwright in C#), Eric Roby (FastAPI), Mehmet Ozkaya (Agent Framework and MCP in .NET).
  - SDLC and Scrum: *Complete SDLC (2026)* and 365 Careers' *Complete Agile & Scrum Project
    Management Course*.
- **DeepLearning.AI**: the OpenAI and Anthropic courses, RAG, evals, agents and ML foundations. All
  of it is Python notebooks, so I take the concepts and build them in C#.
- **HackerRank** (free): the Interview Preparation Kit, the SQL track, and its certification tests.
- **Reference reading, not courses:** the official docs, the Scrum Guide 2020, the SDK
  repositories, the specs, and the reference repos below.

Udemy ratings and dates in the research file are unverified: Udemy blocks automated reads.

## The flagship

**A South African municipal service-delivery tracker.** Residents report water, sanitation,
electricity and road faults. Each report gets a public reference number, an age, a path to the
ward councillor, and a link to what the municipality actually spends, from its own finance data.

Why this problem:

- 47% of 848 wastewater systems are critical in the 2025 Green Drop report.
- 47.3% of water earns no revenue nationally, and 60% in KZN and Mpumalanga.
- The metros each run their own reporting channel. Most smaller municipalities have none.
- The **Municipal Money API** covers 292 municipalities from 2008–09 to 2025–26. It's free, needs
  no key, and allows commercial use with attribution and no implied Treasury endorsement.
- Residents' and ratepayers' associations are the first users.

How it grows:

| Level | What gets added |
|---|---|
| Junior | Report intake with photo and location, a React portal, SQL reporting on real Municipal Money data, AI classification and summaries |
| Intermediate | Near-duplicate detection, a queue-driven worker, finance data per ward, an Angular console for councillors and associations, Azure, RAG over by-laws and IDPs |
| Senior | Event-driven notifications, identity with tenant isolation, IaC on Kubernetes, a Python AI service, an MCP triage agent |
| Mastery | Tender discovery for small businesses on the eTenders OCDS API. Later, and only once the security practice is mature, an optional grants and NSFAS appeals assistant for an NGO |

Its public API follows **Open311 GeoReport v2**, the standard FixMyStreet uses, so other civic
tools can talk to it.

**POPIA.** Phone numbers, locations, and faces or number plates in photos are personal
information. Collect as little as possible, get consent, blur photos, host in Azure South Africa
North, and keep public report data apart from private data.

## How every mini and capstone runs

The SDLC, run as Scrum on GitHub.

1. **Requirements.** Every capstone starts with a one-page brief: problem, users, out of scope,
   risks. Then an epic, user stories from an issue form with acceptance criteria, and
   sub-issues. Each mini is one story.
2. **Board.** GitHub Projects: Backlog → Ready → In progress → Review → Done, WIP limit 2.
   Fields: Iteration (the sprint), Story points, Priority. The Sprint Goal goes in the iteration
   description.
3. **Design.** A design note or decision record for anything non-trivial.
4. **Build.** One branch per story. `main` is protected. PRs say `Closes #n` and need green CI.
5. **Definition of Done**, in the PR template: tests pass; README and `NOTES.md` updated; no
   secrets; AI-generated code flagged and reviewed.
6. **Release.** A tag, and a changelog from Conventional Commits and release-please.
7. **Review and retro.** A demo in the README at the end of each iteration, and a closed retro
   issue.
8. **AI is my tutor, not my author.** When I'm stuck I ask for an explanation, a doc or a hint,
   never the solution. Each question and what I learned goes in `NOTES.md`. `AI_USAGE.md` is the
   longer version of this rule.
9. **Solo, from a blank repo**, using only what that phase taught.
10. **Where things live.** Minis in `worked-examples/<level>/<phase>/`. Capstones in the
    flagship's own repo. Once, at Intermediate, one sprint runs in Azure DevOps Boards and
    Pipelines, because that's the tool South African postings name most.
11. **Level gate.** Build the level's capstone unaided, pass its exit test cold, and pass the
    oral check below. A phase I already know can be tested out of by passing its exit test first.

## Explaining the why, and the break-fix loop

The point is to answer "why did you do it this way?" and "tell me about a time something broke"
from my own work, with evidence.

1. **Why this design.** A MADR-format decision record for every capstone and any non-trivial
   mini: the constraints, at least two options stated fairly, what I chose, the trade-off I
   accepted, and what would change my mind. `decisions/000-template.md` is the template.
2. **Why this test.** Every test file opens with the risk it covers. Every capstone README has a
   test strategy table: risk, test type, why that type, and what it doesn't catch. A test whose
   risk I can't name gets deleted.
3. **Why this system design.** Every design doc states the load, the numbers behind it, the
   bottleneck, the failure modes, and what changes at 10×.
4. **The break-fix drill.** Every capstone ends with a planted fault I haven't seen the fix for.
   They get harder:

   | Level | Faults | What I learn to use |
   |---|---|---|
   | Junior | Null reference, off-by-one, wrong status code, broken migration, bad Azure config | Stack traces, the debugger, structured logs, `git bisect` |
   | Intermediate | A query that goes slow after a data change, a deadlock, a race in the worker, RAG quality dropping after a prompt change | Execution plans and Query Store, `dotnet-counters`, `dotnet-trace`, eval regressions, a failing test that reproduces it |
   | Senior | Lost or duplicated messages, a retry storm, a broken token or managed identity, a pod crash loop, an agent calling the wrong tool | OpenTelemetry traces across services, `kubectl` logs and events, dead-letter queues, chaos tests |
   | Mastery | A memory leak, thread-pool starvation, a capacity limit under load, a cascading failure | `dotnet-dump`, `dotnet-gcdump`, load tests, SLO burn alerts, running the incident |

5. **The postmortem**, in `docs/incidents/NNN.md`: what broke and what the user saw; how it was
   detected; why it broke (five whys); how I diagnosed it, dead ends included; how I fixed it and
   why that fix; how it's prevented from happening again; what I'd do differently. The regression
   test, alert or guardrail has to be merged before the story closes.
6. **Interview answer bank.** At each level gate, three STAR answers go into
   `interview/answers.md`: a design decision, a testing choice, and the incident. Each links to
   the real decision record, test or postmortem.
7. **The oral check.** Someone else, or an AI playing interviewer, picks any file in the
   capstone. I explain why it's written that way, what would break it, and how I'd find out why.

Three habits borrowed from `kablewithak/ai-engineering-interview-vault`:

- **`mistake-patterns/`**: one short file per misconception I correct. What I believed, why it
  was wrong, the right mental model.
- **`concepts/`**: a page per concept that grows over time. How to explain it, where I applied
  it, how it fails, how to test it, the trade-offs.
- **`review/queue.md`**: active-recall questions from every `NOTES.md`, revisited at every later
  level gate.

Docs are tagged by Diátaxis type (tutorial, how-to, reference, explanation), with a glossary and
C4 diagrams. A GitHub Action rebuilds the index on every push, the way `simonw/til` does.

## Reference repos

Read for structure and practice, not copied.

| Repo | What to take from it | Level |
|---|---|---|
| `dotnet/eShopSupport` | The closest match to the flagship: AI ticketing with an ingestor, an Evaluator project, staff and customer UIs, Aspire | Intermediate→Senior |
| `mysociety/fixmystreet` and the Open311 spec | The domain model and status lifecycle for civic fault reporting | Intermediate→Senior |
| `dotnet/eShop` | Service and test layout at senior level | Senior |
| `jasontaylordev/CleanArchitecture`, `ardalis/CleanArchitecture` | Starting templates for minis; compare them in a decision record | Junior→Intermediate |
| `kgrzybek/modular-monolith-with-ddd` | A real decision log, C4 diagrams and a glossary next to the code | Intermediate→Senior |
| `modelcontextprotocol/csharp-sdk` samples | The protected ASP.NET Core MCP server | Senior |
| `dotnet/extensions` (`Microsoft.Extensions.AI.Evaluation`) | .NET-native LLM evals that can gate CI | Intermediate→Senior |
| `anthropics/anthropic-sdk-csharp`, `openai/openai-dotnet`, `microsoft/Generative-AI-for-beginners-dotnet` | SDK examples, and repo hygiene worth copying | Junior→Intermediate |
| `adr/madr` | The decision-record format | All |
| `danluu/post-mortems`, `dastergon/postmortem-templates` | Real failures to base drills on, and a postmortem format | All |
| `donnemartin/system-design-primer` | The worked-example structure for design docs | Intermediate→Senior |
| `yangshun/tech-interview-handbook`, `ashishps1/awesome-behavioral-interviews` | STAR and behavioural preparation | All |
| `alexeygrigorev/ai-engineering-field-guide` | The closest peer repo for AI engineering portfolios and interviews | Intermediate→Senior |
| `microsoft/code-with-engineering-playbook` | Scrum ceremonies, Definition of Done, code and design reviews | Intermediate |
| `OpenUpSA/municipal-data` | The source behind the Municipal Money API | Senior |

`floci-io/floci-az`, a local Azure emulator, is a tool here rather than a project: integration
tests run against it at Senior. If it has no .NET Testcontainers module by Mastery, building one
is a good open-source contribution.

## Certifications

At least one data, security or container/IaC certificate at every level. Statuses and
prerequisites were checked on each certifying body's own pages on 2026-09-29.

| Level | Certificates | Optional | Prep |
|---|---|---|---|
| Junior | **DP-900** (data), **SC-900** (security) | AZ-900, GH-900, HackerRank C# and SQL Basic | Phillip Burton |
| Intermediate | **AZ-104**, **DP-800** SQL AI Developer (data), **Terraform Associate 004** (IaC) | CKAD; HackerRank SQL, Problem Solving and REST API Intermediate | Scott Duffy and Dometrain Exam Prep (AZ-104), Burton (DP-800), Zeal Vora (Terraform) |
| Senior | **SC-500** (security), **CKA** (containers) | AZ-400 (needs AZ-104), DP-300, HackerRank SQL Advanced and Software Engineer | Alan Rodrigues (AZ-400), Mumshad Mannambeth (CKA); SC-500 courses are new, so check the instructor |
| Mastery | **SC-100** (needs SC-500), **CKS** (needs CKA) | AZ-305 (needs AZ-104), Terraform Authoring and Operations Advanced | Alan Rodrigues (SC-100), Zeal Vora (CKS), Scott Duffy (AZ-305) |

Retired, so not to be studied for: AZ-204, AZ-500, AI-102, AI-900 (now AI-901). AI-103 and
AI-200 expect Python, so they're optional. Several Microsoft exams get content updates in late
October 2026; check that a prep course was updated after its exam was.

---

## Junior: C# full stack, AI-ready

**The gate:** I can ship a small full-stack app with an LLM feature, containerised, in CI and on
Azure, using an AI coding assistant responsibly.

### J0 — Linux, Git, SDLC and Scrum

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Udemy: Imran Afzal, *Complete Linux Training Course*; *Complete SDLC (2026)*; 365 Careers, *Complete Agile & Scrum Project Management Course*. Dometrain: Hands-On: Learn Git From Scratch; ZTH: GitHub Actions; GS: Claude Code | A users-and-permissions script and a systemd timer; a `grep`/`sed`/`awk` log report; an Actions workflow; the issue form and PR template every later repo reuses | **`logkit`**, the ladder in `challenges/phase-00-shell-linux-git/`, run as the first full sprint | Explain the CI file line by line to another person |

### J1 — C# and the core data structures

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Dometrain: GS: C#; Hands-On: C# for Beginners; ZTH: Working with Null; ZTH: LINQ; Hands-On: LINQ; DD: C#; Hands-On: Data Structures & Algorithms in C#, chapters 1–9. HackerRank: Interview Preparation Kit, first topics | Value objects; a report CSV parser with line-level errors; a linked list, stack and queue from scratch; three sorts, benchmarked | **`fault-cli`**: imports fault reports, validates them, removes exact duplicates, prints report age by ward | Rebuild it from a blank repo. Pass HackerRank C# (Basic) |

### J2 — SQL Server and T-SQL

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Udemy: Phillip Burton, *70-461/761 Querying SQL Server with T-SQL*. Dometrain: GS: SQL Server. HackerRank: SQL track | CTEs and window functions; a `MERGE` upsert; a stored procedure with `TRY`/`CATCH`; a normalised schema from a messy spreadsheet | The tracker's schema (municipalities, wards, reports, statuses) loaded with real Municipal Money data, and five accountability queries | Pass HackerRank SQL (Basic) |

### J3 — ASP.NET Core Web API, EF Core and testing

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Dometrain: GS: ASP.NET Core; ZTH: REST APIs; ZTH: Minimal APIs; ZTH: Entity Framework Core; ZTH: Unit Testing; ZTH: Testing with xUnit | A Municipal Money API client with retries; validation returning Problem Details; EF Core migrations | **Tracker API v1**: create and track reports, the municipality's finance data, an OpenAPI spec, unit tests | Add an endpoint test-first, explaining each step |

### J4 — TypeScript and React

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Dometrain: GS: TypeScript; Hands-On: Learn TypeScript. Udemy: Maximilian Schwarzmüller, *React – The Complete Guide* | A responsive layout; a typed API client; a report form with photo and GPS; a searchable report list | The public React portal: file a report, track it by reference number, view a ward page | Build a new screen from a user story with no tutorial open |

### J5 — LLMs in C#, AI coding assistants, and shipping

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Dometrain: GS: AI for .NET Developers; GS: AI Agents in C#; DD: Claude Code; ZTH: Working with GitHub Copilot; ZTH: Docker; ZTH: Docker Compose; GS: Azure for Developers. DeepLearning.AI: *ChatGPT Prompt Engineering for Developers*; *Building Systems with the ChatGPT API* | The same classifier on OpenAI and on Anthropic behind one `IChatClient`; structured JSON output; cost logging; a `CLAUDE.md` and a custom command | **The Junior gate**: AI classifies each report by category and urgency and writes a plain summary; the provider switches in config; containerised, in CI, on Azure App Service; delivered over two sprints | Demo it, and explain every AI-generated line I kept |

**Certificates:** DP-900 and SC-900.

## Intermediate

**The gate:** I own features end to end in a layered .NET system: tuned SQL, concurrent code,
Angular or React, CI/CD on Azure DevOps, and a RAG feature whose evals gate the build.

### I1 — C# depth, concurrency and the rest of DSA

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Dometrain: ZTH: Asynchronous Programming; ZTH: Parallel Programming; ZTH: Dependency Injection; ZTH: Configuration and Options; ZTH: Logging; Mastering: C#; the rest of Hands-On: Data Structures & Algorithms in C#. HackerRank: the rest of the Interview Preparation Kit | A `Channel<T>` pipeline; a race condition reproduced and fixed; a trie for street-name search; Dijkstra on a ward graph | A concurrent worker that finds near-duplicate reports by location and time window, with benchmarks | Pass HackerRank Problem Solving (Intermediate) |

### I2 — Data access depth and legacy code

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Dometrain: ZTH: Entity Framework Core, chapters 7–9; ZTH: Dapper; Hands-On: Learn PostgreSQL, from "Indexes" on; ZTH: Integration Testing in ASP.NET Core; Migrating: ASP.NET Web APIs to ASP.NET Core. Udemy: Phillip Burton, DP-800 prep | Scan to seek; parameter sniffing; a deadlock reproduced and fixed; the same query in EF Core and Dapper; vector search in SQL Server | **API v2**: accountability dashboards on tuned queries, integration tests against SQL Server in a container | Read an unfamiliar execution plan and explain the fix. Pass HackerRank SQL (Intermediate) |

### I3 — Architecture

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Dometrain: Hands-On: Creational, Structural and Behavioral Design Patterns; GS and DD: Clean Architecture; ZTH: Vertical Slice Architecture; GS and DD: Domain-Driven Design; GS and DD: Modular Monoliths | Three patterns on real code; a CQRS read model; an event-storming board for report intake | The tracker as a modular monolith (Reports, Wards, Finance, Notifications), with decision records and the Open311 contract | Defend the module boundaries, with two options stated fairly |

### I4 — Angular and end-to-end testing

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Udemy: Maximilian Schwarzmüller, *Angular – The Complete Guide*; Karthik K.K., *Playwright in C# .NET* | A signals-based component; a reactive form; the same screen in React and Angular; a Playwright page-object suite | An Angular console where councillors and associations triage, assign and escalate; Playwright over both front ends | The Playwright suite green in CI |

### I5 — Azure and CI/CD with Azure DevOps

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Dometrain: ZTH: Deploying .NET Applications to Azure; DD: Azure for Developers; GS: Aspire; Exam Prep: AZ-104. Udemy: Phillip Burton, AZ-900; Scott Duffy, AZ-104; Zeal Vora, Terraform Associate | A multi-stage YAML pipeline; a slot swap; Blob and queue integration; one sprint in Azure DevOps Boards | Azure DevOps multi-stage deploys (dev, then prod with an approval) to App Service, Azure SQL, Blob and a queue, infrastructure in Terraform | Roll back a bad deploy |

### I6 — RAG and evals

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Dometrain: ZTH: Microsoft.Extensions.AI; Let's Build It: AI Chatbot with RAG in .NET. DeepLearning.AI: *Vector Databases*; *Building and Evaluating Advanced RAG*; *Evaluating AI Agents* | An embeddings search; chunking strategies compared; an LLM-as-judge harness in xUnit; a prompt-injection test set | **The Intermediate gate**: "Ask your municipality", RAG over by-laws, IDPs and budget data, with citations, evals gating CI, and cost and latency tracked | Report the eval results honestly, failures included |

**Certificates:** AZ-104, DP-800 and Terraform Associate.

## Senior

**The gate:** I design and run distributed, secure, cloud-native .NET systems with agentic AI,
can work in Python for AI services, and mentor through code review.

### S1 — Messaging, resilience and observability

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Dometrain: GS: Messaging with MassTransit; ZTH: Event-Driven Architecture; ZTH: Background Processing; GS and DD: Caching; GS and DD: Microservices Architecture; GS: Event Sourcing; ZTH: OpenTelemetry. Udemy: Stephane Maarek, *Apache Kafka for Beginners* | An outbox; a saga with compensation; retry, timeout and circuit breaker; the same flow on RabbitMQ and Kafka; Redis caching with correct invalidation | Event-driven SMS and email notifications through provider sandboxes, with an outbox, escalation sagas and end-to-end traces; Open311 contract tests | Kill the provider mid-run: nothing is lost and nothing is sent twice |

### S2 — Security, identity and POPIA

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Dometrain: GS: Authentication and Authorization in .NET; Mastering: Azure for Developers. Udemy: Aref Karimi, *Modern Identity and Security for ASP.NET Core*; an OWASP API Top 10 course; SC-500 prep | An insecure API, then fixed; strict JWT validation; managed identity to Key Vault | Entra ID sign-in through a BFF; managed identity and no secrets anywhere; each association an isolated tenant; POPIA controls for consent, blurring, retention and residency | Walk through the token flow; a cross-tenant request is refused |

### S3 — Cloud-native IaC, Kubernetes and GraphQL

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Dometrain: GS: Bicep for Azure; ZTH: Kubernetes for Developers; ZTH: Serverless with Azure Functions; ZTH: Cloud Architecture in Azure; GS: GraphQL. Udemy: Mumshad Mannambeth, CKA; Alan Rodrigues, AZ-400 | A Bicep module and the same in Terraform; a Helm chart; a GraphQL endpoint; an SLO alert | A Bicep-built environment on AKS, a GraphQL API for civic partners, integration tests against floci-az in CI | From an empty subscription to a live system, and back |

### S4 — Python for AI services

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Dometrain: Hands-On: Learn Python. DeepLearning.AI: *AI Python for Beginners*. Udemy: Eric Roby, *FastAPI – The Complete Course* | A typed CLI; a FastAPI service tested with pytest; an async file processor | A containerised FastAPI service that tags fault type from report photos, called by the .NET pipeline, in the same CI | Rebuild it from a blank repo |

### S5 — Agents and MCP

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Dometrain: GS: Microsoft Agent Framework in .NET; GS: Model Context Protocol. Udemy: Mehmet Ozkaya, *Agentic AI Development with Agent Framework, MCP and .NET*. DeepLearning.AI: *Agentic AI*; *MCP with Anthropic*; *Agent Skills with Anthropic*; *Reasoning with o1* | An MCP server in C# over the tracker's API; a tool-calling agent with human approval; agent traces in OpenTelemetry; an agent eval suite; promptfoo red-team runs | **The Senior gate**: a triage agent working through MCP tools, with approval before any action, evals and a cost budget, plus a peer PR reviewed | Present its design and failure modes to another person |

**Certificates:** SC-500 and CKA.

## Mastery

**The gate:** I set technical direction, lead architecture and delivery, go deep on the runtime,
understand models from the ground up, and mentor.

| Phase | Learn | Capstone |
|---|---|---|
| M1 — Performance and the runtime | Dometrain: ZTH: Garbage Collection; ZTH: Benchmarking; ZTH: 1 Billion Row Challenge; ZTH: Source Generators | Measured speed-ups on the tracker's hot paths, with before and after benchmarks |
| M2 — System design leadership | Dometrain: Hands-On: System Design, Beginners → Intermediate → Azure → Advanced; GS and DD: Solution Architecture; Career: Making High-Impact Decisions with AI | A design doc for taking the tracker national; the tender-discovery module on the eTenders OCDS API |
| M3 — ML foundations | DeepLearning.AI: *Machine Learning Specialization*; *Generative AI with LLMs*; *Retrieval Augmented Generation* | A classical model, a fine-tuned model and an LLM compared on report classification, with cost, latency and accuracy reported honestly |
| M4 — Lead and ship | Dometrain: Career: Nailing the Behavioral Interview; GS: C# Interview Questions. Udemy: PSM I prep (optional) | An open-source contribution; a real residents' association onboarded; an on-call runbook and a staged incident's postmortem; a log of code reviews given |

**Certificates:** SC-100 and CKS.

---

## What this curriculum still will not prove

Kept here for the same reason `NON-CLAIMS.md` is kept at top level.

- Working inside a large team's codebase with competing priorities
- Operating a system at a scale an employer would call scale
- That the flagship has users until an association actually uses it
- That I am employable. It proves I can learn and ship, which is necessary and not sufficient

## When to reassess

- **At every level gate.** Did the exit test pass, honestly, or did I talk myself past it?
- **Every `horizon/` entry.** Re-read current postings. The ones in `research/` are snapshots and
  will go stale.
- **If an exit test fails three attempts running.** That's information about the plan, not about
  me. Cut the scope of the phase, never the standard of the test.
- **If `decisions/` has fewer records than there have been real decisions.** Write the missing
  ones, dated the day they're written and marked late.
- **Never by elapsed time.**

## Sources

- `research/2026-09-29-curriculum-sources.md`: the postings, level counts, certification
  statuses, flagship evidence, course choices and reference repos this file rests on
- `research/2026-09-29-dometrain-catalogue.md`: every relevant Dometrain course, with gaps
- `research/2026-09-29-learning-platforms.md`: Dometrain against Coursera and other platforms
- `research/2026-09-23-full-stack-tooling.md`: C# and .NET as the largest local backend ask
- `research/2026-09-26-github-profile-landing.md`: the profile page, and what should leave it
- Earlier direction, superseded but kept for the record: `2026-09-22-sa-target-roles.md`,
  `2026-09-22-data-role-example.md`, `2026-09-23-data-stack-and-certifications.md`,
  `2026-09-23-fraud-and-bank-apis.md`, `2026-09-28-sa-fintech-target-roles.md`,
  `2026-09-29-fintech-knowledge-sources.md`, `2026-09-17-openai-target-roles.md`,
  `2026-09-17-floci-local-build.md`
