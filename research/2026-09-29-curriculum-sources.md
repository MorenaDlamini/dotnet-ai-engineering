# Curriculum sources: what the 2026-09-29 rebuild of `CURRICULUM.md` rests on

Primary-source research, read on 2026-09-29, to answer one question: what do South African
employers ask of a C#/.NET full-stack engineer at each level, and what's the best way to learn
and prove it using Dometrain, Udemy and DeepLearning.AI?

Postings were read in full on the recruiter's own site. Certification statuses come from the
certifying bodies' own pages. Course facts come from the platforms' own pages, except Udemy,
which blocks automated reads. **Every Udemy rating, student count and date here is unverified**,
taken from search results. Inference is marked **Unverified**.

**The counts are a one-day snapshot.** Postings get reposted, retitled and closed. Re-read
current ones at every `horizon/` entry.

---

## The verdict

**Target C#/.NET full stack, AI-ready, with SQL Server as the edge.** That's what the market
pays for at every level. The AI that C# postings ask for is mostly fluency with coding
assistants, plus some LLM integration. AI-engineer postings are all Python-first, so Python
belongs at Senior, for AI services, and not at the start.

Five findings:

1. **SQL Server is the constant.** It appears at every level, and tuning and indexing are named
   explicitly from Intermediate up.
2. **Angular and React are level.** 16 and 17 mentions across 39 postings. React goes first
   because the user chose it; Angular follows at Intermediate.
3. **AI coding assistants are the AI skill C# postings name.** 8 of 39, Claude or Claude Code
   6 times, 2 as a requirement. LLM API integration is required in only 1.
4. **Agile is a minority mention.** 13 of 48 unique postings (27%). Scrum is named in 5, Kanban
   and SAFe in none.
5. **Juniors are scarce.** Only 4 junior C# postings since December 2025, and none since March
   2026. **Unverified inference:** the Junior level is a foundation to pass through, not a
   market to target.

---

## 1. Postings

### Method

E-Merge (https://e-merge.co.za/) runs on WordPress. Each vacancy is a post, and
`https://e-merge.co.za/wp-json/wp/v2/posts?per_page=100&page=N` returns the full text. About 300
recent posts (2025-12 to 2026-09-29) were screened, exact reposts removed, and **49 read in
full**: 39 C#/.NET and 10 AI/LLM. Counts come from a keyword pass corrected by hand, so a cell
may be off by one or two. Levels marked "inferred" were not stated and were taken from years of
experience.

Nine more listings were pasted in by the user the same day. They were read, not counted here,
and they agree with the E-Merge picture: C# and SQL Server at the core, React more often than
Angular, AI coding assistants in three of nine.

### C#/.NET postings, by level

| Skill | Junior (4) | Intermediate (14) | Senior (14) | Lead (7) | Total |
|---|---|---|---|---|---|
| C# | 4 | 13 | 14 | 6 | 37 |
| Modern .NET (Core / 6–9 / ASP.NET Core) | 3 | 7 | 11 | 3 | 24 |
| Legacy (MVC, WebForms, WCF, .NET Framework) | 0 | 4 | 2 | 2 | 8 |
| Web API / REST | 1 | 5 | 10 | 2 | 18 |
| SQL Server / T-SQL / Azure SQL | 2 | 7 | 7 | 2 | 18 |
| Entity Framework | 2 | 4 | 3 | 1 | 10 |
| React | 2 | 6 | 8 | 1 | 17 |
| Angular | 0 | 6 | 7 | 3 | 16 |
| Azure | 1 | 4 | 9 | 1 | 15 |
| AWS | 0 | 0 | 5 | 0 | 5 |
| CI/CD | 1 | 6 | 9 | 3 | 19 |
| Testing (xUnit, NUnit, Playwright, TDD) | 1 | 3 | 7 | 1 | 12 |
| DDD / CQRS / event-driven / microservices | 0 | 3 | 5 | 2 | ~7 each |
| Messaging (RabbitMQ, Kafka, Service Bus) | 0 | 1 | 4 | 1 | 6 |
| IaC (Bicep, Terraform) | 1 | 1 | 2 | 0 | 4 |
| Mentoring (giving) | 0 | 0 | 3 | 5 | 8 |
| AI coding assistants | 1 | 3 | 4 | 0 | **8** |
| LLM APIs / RAG / agents | 0 | 3 | 0 | 0 | **3** (1 required) |

### Postings cited in `CURRICULUM.md`

- Junior, the newest (AI tools, Azure, CI/CD, containers):
  https://e-merge.co.za/junior-full-stack-c-software-developer-cape-town-hybrid-up-to-r540k-pa/
- Junior (names Azure DevOps, GitHub issues and Jira):
  https://e-merge.co.za/junior-full-stack-software-engineer-johannesburg-hybrid-up-to-r400k/
- Intermediate, "AI-forward… e.g. Claude Code", required:
  https://e-merge.co.za/intermediate-software-developer-full-stack-enterprise-saas-developer-johannesburg-permanent-up-to-600k-per-annum/
- Backend C#: SQL Server tuning, EF plus raw SQL, BFF, Service Bus, Bicep, Azure DevOps
  multi-stage, OpenAI and Azure OpenAI:
  https://e-merge.co.za/backend-developer-c-asp-net-sandton-hybrid-up-to-r800k-per-annum-2/
- .NET remote: multithreading, Windows services, DSA, XML/XSLT:
  https://e-merge.co.za/intermediate-net-software-developer-remote-permanent-up-to-r800k-per-annum/
- Polyglot consulting: microservices, DDD, TDD, EDA, Clean Architecture, CQRS, saga:
  https://e-merge.co.za/polyglot-developer-net-c-typescript-go-nextjs-nestjs-node-js-remote-up-to-960k-per-annum/
- Senior IoT SaaS: SQL tuning, modular monolith, Bicep, CQRS, idempotency:
  https://e-merge.co.za/senior-full-stack-software-developer-cape-town-tyger-valley-hybrid-up-to-r1-5m-per-annum-4/
- Full-stack .NET with Scrum ceremonies named:
  https://e-merge.co.za/full-stack-net-developer-johannesburg-hybrid-up-to-r900k-per-annum-2/
- Senior, "ideally Claude Code":
  https://e-merge.co.za/senior-full-stack-developer-c-react-remote-up-to-r1-08-mil-per-annum/
- Mid-to-senior, validating AI-generated code required: https://e-merge.co.za/40184-2/
- Lead back end: Agile/Scrum, Azure DevOps, RabbitMQ/Kafka, TDD/DDD:
  https://e-merge.co.za/lead-backend-api-developer-c-hybrid-role-in-centurion-up-to-r1-2mil-per-annum/

### AI postings

All 10 are Python-first. 7 of the 9 unique ones name Cursor, Claude or Claude Code. Evals
(LLM-as-judge, CI regression suites) appear in three. Examples:

- https://e-merge.co.za/senior-ai-llm-engineer-sandton-r1-2m-pa/
- https://e-merge.co.za/full-stack-engineer-python-remote-up-to-r800k-per-annum/
- https://e-merge.co.za/ai-engineer-claude-code-github-copilot-cursor-remote-up-to-r800k-per-annum/

Five full-stack and product postings at Anthropic and OpenAI were skimmed for contrast. They ask
for TypeScript and React, a backend in Python, Go, Rust or TypeScript, end-to-end ownership, and
experience with AI-assisted tools. None names C#, and none names Scrum.

### Agile

| | Count |
|---|---|
| Mention Agile, Scrum or its ceremonies | 13 of 48 unique (11 of 39 C#, 2 of 9 AI) |
| Scrum named explicitly | 5 |
| Kanban, SAFe | 0 |
| Azure DevOps (mostly as pipelines or TFS; once as a tracker) | 7 |
| GitHub, Bitbucket, Jira | 5, 5, 1 |

---

## 2. C# and AI: the libraries

All read on their own repositories or NuGet pages.

| Library | Package | Version (date) | Status |
|---|---|---|---|
| OpenAI .NET | `OpenAI` (github.com/openai/openai-dotnet) | 2.14.0 (Sep 15) | GA; some APIs `[Experimental]` |
| Anthropic C# SDK | `Anthropic` (github.com/anthropics/anthropic-sdk-csharp) | 12.51.0 (2026-09-28) | GA, official. Versions 3.x and below were the community tryAGI package. Implements `IChatClient` |
| Azure OpenAI | `Azure.AI.OpenAI` | stable 2.1.0 (2024-12); 2.9.0-beta.1 (2026-03) | Stable release is old |
| `Microsoft.Extensions.AI.OpenAI` | NuGet | 10.10.1 (2026-09-25) | Stable |
| Microsoft Agent Framework | `Microsoft.Agents.AI` (github.com/microsoft/agent-framework) | 1.22.0 (2026-09-18) | GA. Semantic Kernel's README calls it "the enterprise-ready successor to Semantic Kernel" |
| MCP C# SDK | `ModelContextProtocol` (github.com/modelcontextprotocol/csharp-sdk) | 2.2.0 (2026-08-13) | Stable, maintained with Microsoft |

---

## 3. Courses

### Dometrain (from https://dometrain.com/sitemap.xml and each course page)

- **AI:**
  - GS: Claude Code (Gui Ferreira, 4h42m)
  - DD: Claude Code (Gui Ferreira, 6h59m: hooks, subagents, skills, MCP, permissions, headless
    mode and CI/CD, plugins). No third Claude Code course exists.
  - ZTH: Working with GitHub Copilot, and GS/DD: Boosting Developer Productivity with AI (Kevin
    Dockx)
  - GS: AI for .NET Developers (Ed Charbeneau)
  - ZTH: Microsoft.Extensions.AI (Brandon Minnick; includes evaluating LLM output)
  - GS: Microsoft Agent Framework in .NET (Nico Vermeir)
  - GS: AI Agents in C# (James Charlesworth). The one course that uses both **OpenAI and
    Anthropic**, through `Microsoft.Extensions.AI`.
  - Let's Build It: AI Chatbot with RAG (OpenAI and Pinecone)
  - GS: Model Context Protocol (C# server and client, Entra ID auth)
  - No AI course is in the Hands-On series.
- **DSA:** Hands-On: Data Structures & Algorithms in C# (15h38m, 147 lessons). Big-O, lists,
  stacks, queues, recursion, searching, sorting, trees, heaps, hash tables, graphs including
  Dijkstra, two pointers, sliding window, dynamic programming.
- **TypeScript:**
  - GS: TypeScript (Cory House, 3h30m)
  - DD: TypeScript (Cory House, 6h54m)
  - Hands-On: Learn TypeScript (24h49m)
  - GS: TypeScript Interview Questions (3h03m)
- **Python:** Hands-On: Learn Python (25h20m, 256 lessons, including type hints and async), and
  GS: Python Interview Questions.
- **Playwright:** no dedicated course. ZTH: Integration Testing in ASP.NET Core has a 57-minute
  Playwright section.
- **Exam Prep:** AZ-900, AZ-104 (490 graded questions), AZ-305.
- **Not on Dometrain:** SDLC, Agile, React, Angular.
- **Format:** Hands-On courses run in the browser with instant feedback. Whether the feedback
  comes from unit tests is **Unverified**.

### Udemy (all figures unverified)

| Need | Course | Instructor |
|---|---|---|
| T-SQL | 70-461/761: Querying Microsoft SQL Server with Transact-SQL | Phillip Burton |
| Data and security certificates | AZ-900, DP-900, DP-300, DP-600, DP-700, DP-800, SC-900 prep | Phillip Burton. He has **no AZ-104, AZ-305 or AZ-204** course, per his own site https://filecats.co.uk/ |
| Linux | Complete Linux Training Course; RHCSA EX200 | Imran Afzal |
| React / Angular | React – The Complete Guide; Angular – The Complete Guide | Maximilian Schwarzmüller |
| AZ-104, AZ-305 | Complete Exam Prep | Scott Duffy |
| AZ-400, SC-300, SC-100 | Exam prep | Alan Rodrigues |
| Terraform, CKS | Terraform Associate 2026; CKS | Zeal Vora |
| CKA, CKAD | CKA with Practice Tests; CKAD | Mumshad Mannambeth |
| Kafka | Learn Apache Kafka for Beginners v3 | Stephane Maarek |
| Identity | Modern Identity and Security for ASP.NET Core (.NET 9; OAuth2, OIDC, PKCE, BFF) | Aref Karimi |
| Playwright in C# | Automation Framework Development with Playwright in C# .NET | Karthik K.K. |
| FastAPI | FastAPI – The Complete Course | Eric Roby and Chad Darby |
| Agents in .NET | Agentic AI Development with Agent Framework, MCP and .NET (May 2026) | Mehmet Ozkaya |
| SDLC | Complete SDLC: Software Development Life Cycle (2026), 14h | "Yogesh" |
| Agile and Scrum | The Complete Agile & Scrum Project Management Course (updated 2024-09-04) | Ivan, 365 Careers |

Udemy is thin on SQL Server tuning. The recognised experts publish elsewhere: Brent Ozar on his
own site, Pinal Dave on Pluralsight.

### DeepLearning.AI (https://www.deeplearning.ai/courses)

- **OpenAI:** ChatGPT Prompt Engineering for Developers; Building Systems with the ChatGPT API;
  Reasoning with o1
- **Anthropic:** Claude Code: A Highly Agentic Coding Assistant; Agent Skills with Anthropic; MCP:
  Build Rich-Context AI Apps with Anthropic; Building toward Computer Use with Anthropic
- **RAG and evals:** Vector Databases; Building and Evaluating Advanced RAG; Evaluating AI Agents;
  Retrieval Augmented Generation (26h)
- **Foundations:** AI Python for Beginners; Agentic AI; Machine Learning Specialization;
  Generative AI with LLMs
- Everything is Python. None of it is C#.

### HackerRank (https://www.hackerrank.com/skills-verification)

- **Interview Preparation Kit:** 13 topics.
- **SQL track.**
- C# is supported in Problem Solving.
- **Free certification tests:** C# Basic; SQL Basic, Intermediate and Advanced; Problem Solving
  Basic and Intermediate; REST API Intermediate; the Software Engineer role certificate.

---

## 4. Certifications

Checked on learn.microsoft.com/credentials, developer.hashicorp.com and
training.linuxfoundation.org.

| Cert | Status | Prerequisite |
|---|---|---|
| AZ-900, DP-900, SC-900 | Active | None |
| AI-901 | Active; replaces AI-900 | None |
| AZ-104 | Active | None |
| DP-300 | Active | None |
| DP-800 SQL AI Developer | Bookable: T-SQL, CI/CD, embeddings and vectors. GA **Unverified** | None |
| SC-300, SC-200 | Active | None |
| SC-500 | Active; replaces AZ-500 | None |
| AZ-500 | **Retired 2026-08-31** | — |
| SC-100 | Active | One of SC-200, SC-300 or SC-500 |
| AZ-305 | Active | AZ-104 |
| AZ-400 | Active | AZ-104 (the other route, AZ-204, is retired) |
| AZ-204, AI-102 | **Retired** | — |
| AI-103, AI-200 | Bookable; both expect Python | None |
| Terraform Associate 004 | Current (Terraform 1.12) | None |
| KCNA, CKAD, CKA | Active; Kubernetes v1.35 | None |
| CKS | Active | CKA |
| Docker Certified Associate | Still sold by Mirantis | None |

Several Microsoft exams get English content updates between 2026-10-19 and 2026-10-28: DP-800,
DP-300, SC-900, SC-300, SC-200 and SC-100. Check that a prep course is dated after its exam's
update.

---

## 5. The flagship problem

| Claim | Source |
|---|---|
| 47% of 848 wastewater systems critical (Green Drop 2025); 47.3% of water earns no revenue, 60% in KZN and Mpumalanga | https://mg.co.za/the-green-guardian/2026-03-31-sa-s-water-crisis-deepens-nearly-half-of-wastewater-systems-critical/ |
| About 15% of municipalities had clean audits in 2024–25 | CoGTA statement. **Unverified**: the page failed TLS |
| Metros run separate channels | Cape Town WhatsApp, Tshwane portal, eThekwini WhatsApp (city pages) |
| Municipal Money API: no key, JSON cubes, 292 municipalities, 2008–09 to 2025–26 | https://municipaldata.treasury.gov.za/api |
| Terms: commercial use allowed; attribute Treasury and the date; no personal data; no implied endorsement | https://municipalmoney.gov.za/terms |
| eTenders OCDS data allows any use, including commercial, with a link to the source; public beta; not for critical or legal decisions | https://data.etenders.gov.za/Home/LearnMore |
| POPIA is enforced: around six fines so far, up to R5m | https://mjkinc.co.za/popia/enforcement-tracker |

Considered and ranked lower:

- **Load-shedding.** It has largely ended (https://www.eskom.co.za/power-system-status/), and the
  EskomSePush free tier is small.
- **Youth jobs.** SAYouth.mobi already has millions of users.
- **Clinic stock-outs.** Needs a partner, and there's no open data.
- **Tenant rights.** Legislation data is expensive to license.
- **Grants and NSFAS.** The need is real, but POPIA risk is high. It's kept as an optional
  Mastery tenant.

---

## 6. Reference repos

Metadata read with `gh api repos/...`.

| Repo | Stars | Last push |
|---|---|---|
| dotnet/eShopSupport | 661 | 2025-05-16 |
| mysociety/fixmystreet | 618 | 2026-09-28 |
| dotnet/eShop | 10,913 | 2026-09-28 |
| jasontaylordev/CleanArchitecture | 20,604 | 2026-09-28 |
| ardalis/CleanArchitecture | 18,498 | 2026-09-21 |
| kgrzybek/modular-monolith-with-ddd | 14,040 | 2024-06-04 |
| modelcontextprotocol/csharp-sdk | 4,554 | 2026-09-28 |
| dotnet/extensions | 3,217 | 2026-09-29 |
| adr/madr | 2,521 | 2026-08-28 |
| danluu/post-mortems | 12,484 | 2026-08-31 |
| dastergon/postmortem-templates | 1,450 | 2023-07-12 (stale, canonical) |
| donnemartin/system-design-primer | 372,444 | 2026-09-15 |
| yangshun/tech-interview-handbook | 143,016 | 2026-08-07 |
| alexeygrigorev/ai-engineering-field-guide | 5,674 | 2026-09-23 |
| simonw/til | 1,459 | 2026-09-11 |
| microsoft/code-with-engineering-playbook | 2,736 | 2026-02-03 |
| OpenUpSA/municipal-data | 52 | 2026-09-16 |
| kablewithak/ai-engineering-interview-vault | 7 | 2026-09-04 |

Archived, so not recommended: `dotnet/ai-samples`, `dotnet-architecture/eShopOnWeb`,
`Azure-Samples/openai-dotnet-samples`.

**floci:** the facts are in `2026-09-17-floci-local-build.md`. The org also has `floci-az`, a local
Azure emulator. Whether it has a .NET Testcontainers module is **Unverified**.
