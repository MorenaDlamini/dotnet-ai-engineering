# Turning SA C#/.NET full-stack postings into portfolio projects: what randmatch covers and what it misses

Research only. Every posting was read on **2026-10-01**. Postings change and close often, so treat these numbers as a one-day snapshot.

---

## Verdict

**One fintech product is enough, but randmatch as planned isn't.** It needs five changes before it covers what these posts ask for. A second, different project would not close the gaps any more cheaply.

1. **Add Angular.** It is the front-end named most often: 13 of 27 posts, against 11 for React and 11 for Blazor. Post 2 is built around it: "strong focus on Angular for the front-end" ([P2]). The plan only has React. The smallest fix is to give `randmatch-ledger` an operator console written in Angular. Optionally, give `randmatch-sim` a Blazor control panel.
2. **Name and deploy specific Azure services.** 17 of 27 posts name Azure. Post 1 lists "App Services / Container Apps / Azure Functions / Azure SQL / Azure OpenAI / Key Vault / Application Insights" ([P1]). Two other posts ask for Service Bus, Functions and API Management ([W3], [W26]). The plan names no Azure services at all.
3. **Add Azure DevOps pipelines.** 14 of 27 posts name Azure DevOps. Only 1 names GitHub Actions, and only as an advantage ([W25]).
4. **Make SQL Server the deep database, not Postgres.** 16 of 27 name SQL Server or T-SQL, and 6 name query tuning. Only 2 name PostgreSQL: [P1], which requires "3+ years PostgreSQL experience", and [W25]. The Postgres ledger is fine to keep, but the T-SQL depth has to be visible in `randmatch-recon`.
5. **Make the AI-assisted workflow visible in the repos.** Only [P1] makes it the core of the job, but it is explicit there: "The ideal candidate must demonstrate practical experience using AI as part of the software development lifecycle" and "Evaluate AI-generated code for security, performance, maintainability, and compliance" ([P1]).

**Where randmatch over-delivers.** The break-explainer with citations and evals, the MCP server and the Kafka outbox go beyond what the market asks. LLM features appear in 1 of 27 posts, MCP in 1 (as "Preferred"), and Kafka in 1 (as an advantage). Keep them as the differentiator, but don't let them crowd out items 1–5.

**What no portfolio can prove.** 10 of 27 posts want legacy work: .NET Framework 4.7.2, ASP.NET MVC 5, WebForms, VB.NET or WPF. Two want mobile (Flutter, MAUI). That evidence has to come from your CV, not from a new build. **Inference.**

---

## Method and sources

**How the pages were read.**
- **The fetch tool worked but summarised.** Fetching the PNet pages directly returned text that the tool's summariser had rewritten, so it was not verbatim.
- **The reader proxy gave verbatim text.** `curl https://r.jina.ai/<url>` worked for every PNet page. All quotes below come from that route.
- **Recruitee and E-Merge** were read through their JSON APIs.
- **Dariel** was read through the reader proxy, skipping the cookie banner.

**Not counted:**
- **Ozow:** the Greenhouse board lists 8 jobs, none of them developer roles (Senior Test Engineer is the closest) — https://boards-api.greenhouse.io/v1/boards/ozow/jobs
- **Investec:** the .NET Engineer page says "Vacancy Closed" — https://careers.investec.co.za/jobs/vacancy/net-engineer-13748-sandton/13766/description/
- **OfferZen:** it is a profile-based marketplace with no public .NET listings to read — https://www.offerzen.com/jobs
- **BBD:** the careers page returned nothing readable.
- **Arid, Pretoria (4281797):** it is a Java role.
- **Datafin "C#, Java, Cloud, Data" (4276659):** it names no stack.
- **Entelect's Senior and Intermediate .NET pages:** these are evergreen ("We are always Hiring"), and their tech section is a menu headed "THE TECH STACKS WE USE *Popular but not limited to". They are reported separately and kept out of the counts.

**Duplicate ads merged into one role:**
- Three ads with identical requirements (IBM MQ, .NET 4.7.2, "Payment Systems") are counted as **one role, [W8]**: Recru-IT 4280354, multiSEARCH 4279417 and Recruitco 4279106. **Inference** that it is the same client.
- Belay 4269337 and Fourier 4269193 describe the same Centurion company and services list. They are counted as **one role, [W23]**. **Inference.**

**Overlap with `2026-09-29-curriculum-sources.md`.**
- E-Merge's WordPress API shows **no new C# posts after 2026-09-29**. The newest C#-related posts are 40503 (Backend C# Sandton, 09-23), 40494 (Software Developer C# Sandton, 09-21) and 40491, which is post 2 (09-21) — https://e-merge.co.za/wp-json/wp/v2/posts
- **Post 2 was probably among the 39 counted on 09-29.** That is **Unverified**, because the notes list only the 11 cited URLs, not all 39.
- E-Merge ads that also appear on PNet were not re-read: 4269258, 4276640, 4270696 and 4270494.
- **New in this sample:** every PNet, Careers24, DVT, Dariel and iOCO role below.

**Sample size.** The brief asked for 12–20 postings. After dedupe I found 25 current ones, plus the 2 primary posts, so **N = 27**. Both reach the count. By level: 17 senior or lead, 9 intermediate, 1 with no level stated.

### Source register (all read 2026-10-01)

Each ID below is used for inline citation. "Pub" is the publication date shown by PNet or the ATS.

| ID | Role / employer | Level | Pub | URL |
|---|---|---|---|---|
| P1 | Senior Full Stack Developer – AI-Enabled Software Engineering, iOCO, Cape Town | Senior | 2026-09-30 | https://www.pnet.co.za/jobs--Senior-Full-Stack-Developer-AI-Enabled-Software-Engineering-iOCO0004-Cape-Town-iOCO--4281315-inline.html |
| P2 | Intermediate C# Full Stack, E-Merge (MAT61517), Centurion | Int | 2026-09-21 | https://www.pnet.co.za/jobs--INTERMEDIATE-C-FULL-STACK-SOFTWARE-DEVELOPER-CENTURION-HYBRID-UP-TO-R800K-PER-ANNUM-Centurion-E-Merge-IT-Recruitment--4276609-inline.html |
| W1 | Senior C# .Net Developer – Small Fintech, Be Different, Sandton | Senior | 2026-09-28 | https://www.pnet.co.za/jobs--Senior-C-Net-Developer-Small-Fintech-Sandton-Be-Different-Recruitment--4279321-inline.html |
| W2 | Senior .NET Full Stack (financial services client), Datafin, Sandton | Senior | 2026-09-29 | https://www.pnet.co.za/jobs--Senior-NET-Full-Stack-Developer-Sandton-On-site-6-12-Month-Contract-Johannesburg-Datafin-IT-Recruitment--4280330-inline.html |
| W3 | Senior C# Full Stack (Azure), banking, IQbusiness, Sandton | Senior | 2026-09-21 | https://www.pnet.co.za/jobs--Senior-C-Full-Stack-Developer-Azure-Sandton-IQbusiness--4200242-inline.html |
| W4 | Senior C# Full Stack (mining ERP), Network IT, Pretoria East | Senior | 2026-09-28 | https://www.pnet.co.za/jobs--Senior-C-Full-Stack-Developer-Pretoria-East-Network-IT--4270107-inline.html |
| W5 | C# Blazor Full Stack, Tumaini, JHB/remote | n/s | 2026-10-01 | https://www.pnet.co.za/jobs--C-Blazor-Full-Stack-Developer-Johannesburg-Tumaini-Consulting--4273610-inline.html |
| W6 | Intermediate Fullstack (C#, Blazor, EF Core, SQLite), Datafin, remote | Int | 2026-09-16 | https://www.pnet.co.za/jobs--Intermediate-Fullstack-Developer-Remote-C-Blazor-Entity-Framework-Core-with-SQLite-Cape-Town-Datafin-IT-Recruitment--4263887-inline.html |
| W7 | Senior C#. Net Developer (Blazor), Sabenza, Cape Town (thin ad) | Senior | 2026-09-28 | https://www.pnet.co.za/jobs--Senior-C-Net-Developer-Blazor-Cape-Town-Sabenza-IT-Recruitment--4267717-inline.html |
| W8 | Senior C# API / Integration Developer (one role, 3 ads) | Senior | 2026-09-28/29 | https://www.pnet.co.za/jobs--Senior-C-NET-Integration-Developer-Cape-Town-Recruitco--4279106-inline.html (also 4280354, 4279417) |
| W9 | Senior Application Developer C# .NET, Salix, JHB | Senior | 2026-09-28 | https://www.pnet.co.za/jobs--Senior-Application-Developer-C-NET-JHB-Northern-Suburbs-Salix-Recruitment--4280012-inline.html |
| W10 | Senior .NET Developer (iOCO0133), Cape Town | Senior | 2026-09-16 | https://www.pnet.co.za/jobs--Senior-NET-Developer-iOCO0133-Cape-Town-iOCO--4273403-inline.html |
| W11 | Remote Full Stack .NET Web Developer, Werkie | Int | 2026-09-29 | https://www.pnet.co.za/jobs--Remote-Full-Stack-NET-Web-Developer-Remote-Full-Stack-NET-webontwikkelaar-IT-26-Remote-Werkie--4271901-inline.html |
| W12 | Intermediate Full Stack (C#/.NET + Flutter), Sabenza, JHB | Int | 2026-10-01 | https://www.pnet.co.za/jobs--Intermediate-Full-Stack-Developer-Johannesburg-Sabenza-IT-Recruitment--4281979-inline.html |
| W13 | Full Stack Developer (Technical Lead Focus), Goldman, JHB | Lead | 2026-10-01 | https://www.pnet.co.za/jobs--Full-Stack-Developer-Technical-Lead-Focus-Johannesburg-Goldman-Tech-Resourcing-Pty-Ltd--4281985-inline.html |
| W16 | Senior Dot Net Developer, Dariel, Bramley | Senior | 2026-07-20 (closes 2026-12-31) | https://darielsoftware.simplify.hr/Vacancy/194714 |
| W17 | Full Stack Engineer (Intermediate .NET), Dariel, Bramley | Int | 2026-07-20 (closes 2026-12-31) | https://darielsoftware.simplify.hr/Vacancy/194596 |
| W18 | Senior .NET / Vue Full Stack, DVT | Senior | 2026-07-27 | https://dvtcareers.recruitee.com/o/senior-net-vue-full-stack-developer-cape-town |
| W19 | Senior .Net Developer, DVT | Senior | 2026-07-14 | https://dvtcareers.recruitee.com/o/senior-net-developer-cape-town |
| W20 | Senior .NET Developer (iOCOOO151), remote | Senior | 2026-09-30 | https://www.pnet.co.za/jobs--Senior-NET-Developer-iOCOOO151-Johannesburg-iOCO--4281477-inline.html |
| W21 | Intermediate .NET Developer (iOCOOO150), remote | Int | 2026-09-30 | https://www.pnet.co.za/jobs--Intermediate-NET-Developer-iOCOOO150-Johannesburg-iOCO--4281437-inline.html |
| W22 | .Net Tech Lead (iOCOOO149), remote | Lead | 2026-09-30 | https://www.pnet.co.za/jobs--Net-Tech-Lead-iOCOOO149-Johannesburg-iOCO--4281409-inline.html |
| W23 | .Net Full Stack Software Developer, Centurion (Belay + Fourier ads) | Int | 2026-09-24 | https://www.pnet.co.za/jobs--Net-Full-Stack-Software-Developer-Centurion-Belay-Talent-Solutions-Pty-Ltd--4269337-inline.html (also 4269193) |
| W24 | Senior .NET Developer – Blazor, Psybergate, Cape Town | Senior | 2026-09-25 | https://www.pnet.co.za/jobs--Senior-NET-Developer-CPT-Northern-Suburbs-Psybergate-Pty-Ltd--4278922-inline.html |
| W25 | Backend Software Engineer (.NET), Belay, Centurion/Midrand | Int | 2026-09-29 | https://www.pnet.co.za/jobs--Backend-Software-Engineer-NET-Centurion-Belay-Talent-Solutions-Pty-Ltd--4271600-inline.html |
| W26 | Snr Azure Integration Developer (.NET), Tumaini | Senior | 2026-09-30 | https://www.pnet.co.za/jobs--Snr-Azure-Integration-Developer-NET-KwaZulu-Gauteng-Western-Cape-Tumaini-Consulting--4281344-inline.html |
| W27 | Intermediate .NET Developer (C# / SQL), Being IT, Durbanville (Careers24) | Int | 2026-09-18 | https://www.careers24.com/jobs/adverts/2388361-intermediate-net-developer-c-sql-durbanville/ |
| E1/E2 | Entelect Senior / Intermediate .NET (evergreen, **not counted**) | — | none shown | https://culture.entelect.co.za/position/senior-net-software-engineer/ · https://culture.entelect.co.za/position/intermediate-net-software-engineer/ |

IDs W14 and W15 are unused; they were reserved for Entelect, which is now E1/E2.

**Not read, but worth noting:** PNet's ".net-developer" search also returned five MAUI or mobile .NET ads (4273219, 4275720, 4271408, 4278925, 4265946). Their content is **Unverified**.

---

## Post 1 (iOCO): checking the ChatGPT summary against the post

Verbatim quotes are from [P1]. The post was published 2026-09-30.

| ChatGPT claim | What the post says | Verdict |
|---|---|---|
| React, .NET 8+, PostgreSQL | "React (5+ years)", "C# / .NET 8+ / ASP.NET Core / REST APIs / Entity Framework Core", "PostgreSQL / Database Design / Query Optimization / Performance Tuning". Mandatory: "5+ years React development experience", "3+ years PostgreSQL experience" | **Correct.** ChatGPT left out the hard years, TypeScript, Tailwind CSS and EF Core |
| Azure | "Deploy applications to cloud environments (Azure preferred)". Mandatory: "Experience deploying solutions to cloud environments". Named services: "App Services / Container Apps / Azure Functions / Azure SQL / Azure OpenAI / Key Vault / Application Insights" | **Partly.** Azure is *preferred*; any cloud meets the mandatory line. ChatGPT left out the seven named services |
| Clean Architecture / DDD | "Clean Architecture / Domain-Driven Design (DDD) / Event-Driven Architectures / Microservices (where appropriate)" | **Correct but incomplete.** Event-driven and microservices are left out |
| CI/CD | "Build and maintain CI/CD pipelines", "Implement Infrastructure-as-Code principles", "Git / Azure DevOps / GitHub / CI/CD Pipelines / Docker" | **Correct.** IaC, Docker and Azure DevOps are left out |
| AI throughout the SDLC | "AI Engineering Skills (Mandatory) — The ideal candidate must demonstrate practical experience using AI as part of the software development lifecycle." | **Correct, and it is mandatory** |
| AI-assisted coding, refactoring, testing, debugging, documentation, architectural analysis | "Use AI tools for: Code generation / Refactoring / Documentation generation / Test development / Troubleshooting and debugging / Architectural analysis" | **Correct**, nearly word for word |
| Prompt engineering | "Prompt engineering for software development" (Required Experience); "Create and maintain effective prompts and AI workflows." | **Correct** |
| Critical evaluation of generated code | "Evaluate AI-generated code for security, performance, maintainability, and compliance."; "Ability to critically evaluate AI-generated outputs." | **Correct** |
| MCP / AI agents / workflow orchestration as preferred | "Preferred Experience: AI Agent Frameworks / Model Context Protocol (MCP) / AI Workflow Orchestration". Separately, under "Advantageous": "Experience building AI-native applications. Experience implementing AI agents." | **Correct.** ChatGPT merged two lists, Preferred and Advantageous |

**What the summary left out:**
- **Hard experience minimums:** "7+ years professional software development experience", "5+ years C# and .NET experience", "1+ years using AI-assisted development tools in production environments".
- **Named tools:** "GitHub Copilot / Microsoft Copilot / Claude Code / Cursor AI / ChatGPT Enterprise (where approved)".
- **Leadership:** "Mentor junior and intermediate developers", "Contribute to the organization's AI Engineering standards and best practices".
- **Success measures:** "Demonstrate measurable productivity improvements through responsible AI tool usage".
- **Domain:** "Experience in highly regulated industries" (advantageous).
- **Qualifications:** "Bachelor's Degree … Required".
- **Location:** "Location: Cape Town", with no remote or hybrid option stated. That matters for a Johannesburg candidate.

**The post never names:** a test framework, Playwright, Entra ID, OAuth, RBAC, multi-tenancy, Service Bus, Kafka, Angular or SQL Server. It names Azure SQL only as a cloud service.

## Post 2 (E-Merge, Centurion): verbatim

From [P2], published on PNet 2026-09-21, which matches E-Merge's WordPress post 40491:

- "3+ years of experience in full-stack development, with a strong focus on Angular for the front-end"
- "Proficiency in C# and ASP.NET MVC for back-end development"
- "A good understanding of SQL databases (MSSQL preferred), with experience in writing T-SQL queries"
- "Familiarity with Object-Relational Mapping (ORM) technologies (Entity Framework a plus)."
- "Experience with RESTful APIs is beneficial"
- Soft skills: "Excellent problem-solving and analytical skills", "Strong communication and collaboration skills", "Ability to work independently and as part of a team", "Attention to detail"
- "University degree in Computer Science or similar tertiary qualification"; "Microsoft Certified Solutions Developer (MCSD) beneficial"
- Package as stated: "permanent hybrid position based in Centurion offering a cost to company salary of up to R800k negotiable on experience and ability"

**What it doesn't mention:** cloud, CI/CD, tests or AI. **Inference:** randmatch as planned proves only the C# and SQL parts of this post. Angular is the decisive gap.

**MCSD:** I believe Microsoft retired it in 2021, but I haven't checked. **Unverified.**

---

## 1. How often each requirement appears (N = 27: P1, P2, W1–W13, W16–W27)

A count includes "advantageous" and "nice to have" mentions. "(req)" notes where a requirement is mandatory. Counts were made by hand and may be off by one.

| Requirement | Count / 27 | Example verbatim quote | Source |
|---|---|---|---|
| C# | 26 | "Strong C# and modern .NET experience" | W25 |
| Modern .NET (Core / 6+ / 8+ / 10) | 17 (version named: P1 8+, W2 10/8, W3 6+, W16 6+, W25 8/9) | ".NET 10 (.NET 8 acceptable)" | W2 |
| Legacy .NET (Framework, MVC, WebForms, VB.NET, WPF) | 10 | "DotNet 4.7.2"; "Strong ASP.NET Web Forms experience" | W8; W11 |
| REST / Web API | 20 | "Experience developing RESTful APIs using ASP.NET Core" | W25 |
| EF / ORM | 11 (EF Core named in 4). Dapper: 0 | "Strong experience with Entity Framework Core, LINQ and database migrations" | W24 |
| SQL Server / T-SQL / Azure SQL | 18 (SQL Server named in 16) | "Strong experience with SQL Server, including query optimisation, indexing and stored procedures" | W27 |
| Query tuning / stored procedures | 6 tuning; 4 stored procs | "SQL query optimisation / Stored procedures / Data modelling" | W10 |
| PostgreSQL | 2 (P1 req) | "3+ years PostgreSQL experience" | P1 |
| NoSQL / Cosmos DB | 3 | "Databases: MSSQL, CosmosDB" | W1 |
| Angular | **13** | "Strong Angular experience is a must!" | W20 |
| React | 11 | "Strong front-end development experience with: … React JS" | W23 |
| Blazor | **11** | "Strong hands-on experience with Blazor Server and Blazor WebAssembly" | W24 |
| Vue | 3 | "Strong experience building front-end applications using Vue.js" | W18 |
| TypeScript | 7 | "Angular 21. TypeScript 5." | W2 |
| Azure (any) | 17 | "Extensive hands-on experience with Microsoft Azure cloud services." | W3 |
| App Service | 4 | "Azure App Services and Azure Functions" | W12 |
| Container Apps | 1 | "Container Apps" | P1 |
| Azure Functions | 6 | "Microsoft Serverless Functions, EntryID/Authentication Flows" | W20 |
| Service Bus / Event Hub | 3 | "Azure Service Bus / Event Hub" | W3 |
| Key Vault | 2 | "Azure Key Vault" | W3 |
| Application Insights | 1 | "Application Insights" | P1 |
| API Management | 2 | "Azure API Management" | W26 |
| Azure OpenAI | 1 | "Azure OpenAI" | P1 |
| Azure certs | 5 (W3 req) | "Microsoft Azure certifications are required." | W3 |
| AWS | 6 (all "or" or advantageous) | "AWS experience will be beneficial." | W5 |
| Docker | 9 | "Experience with Docker and containerized applications" | W25 |
| Kubernetes / AKS | 8 (mostly advantageous) | "Azure Kubernetes Service (AKS) advantageous" | W3 |
| CI/CD | 13 | "Create CI/CD pipelines for Azure and on-prem environments" | W19 |
| Azure DevOps | **14** | "Manage Azure DevOps projects (branching strategies and policies)" | W19 |
| GitHub Actions | 1 (adv) | "Azure DevOps or GitHub Actions" | W25 |
| IaC | 1 (E1/E2 menus list Terraform, Bicep and AWS CDK, but aren't counted) | "Implement Infrastructure-as-Code principles." | P1 |
| Automated / unit tests | 12 | "Develop and execute unit and integration tests." | W8 |
| xUnit named | 4 | "Testing: NUnit, xUnit, Cypress, Moq" | W1 |
| Integration testing named | 4 | "Experience with testing frameworks (xUnit, NUnit, integration testing)" | W18 |
| Playwright | **0** (Cypress 1) | — | — |
| Clean Architecture | 6 | "Strong understanding of SOLID principles, Clean Architecture, and Domain-Driven Design (DDD)" | W16 |
| DDD | 2 | (as above) | W16, P1 |
| CQRS / MediatR | 1 | "Build request pipelines using CQRS and MediatR." | W24 |
| Microservices | 10 | "Experience designing microservices and distributed systems" | W16 |
| Event-driven | 2 | "Knowledge of event-driven architectures" | W16 |
| Messaging (Service Bus, IBM MQ, Kafka, generic) | 5 (Kafka 1, adv) | "IBM MQ Client or similar queue services interaction." | W8 |
| Integration formats (SOAP / XML / XSD) | 6 | "Experience with XML messaging and schema validation" | W8 |
| Auth (Entra ID / B2C / API auth) | 3 | "Integrate applications with Azure B2C for authentication and authorisation." | W24 |
| OAuth / OIDC, RBAC, multi-tenancy | **0** | — | — |
| Observability (monitoring, logging) | 2 | "Implement audit logging, error handling and secure coding practices." | W24 |
| Production support / root cause analysis | 5 | "Perform root cause analysis (RCA) on system defects and production issues." | W8 |
| Security (secure coding) | 6. OWASP: **0** | "Understanding of secure software development within banking or financial environments." | W3 |
| Code reviews | **15** | "Participate in code reviews, providing constructive feedback to team members" | W1 |
| AI coding assistants | 5 (P1 req) | "Build familiarity with AI-assisted coding tools, particularly Claude Code" | W6 |
| LLM features (Azure OpenAI, RAG, agents, MCP) | **1** | "Model Context Protocol (MCP)" (Preferred) | P1 |
| Agile / Scrum | 11 (Scrum named in 6, Kanban 1) | "Participate in sprint planning, stand-ups, and regular code reviews." | W21 |
| Mentoring | 10 | "Mentor and guide junior and intermediate developers" | W18 |
| Stakeholder communication | 8 | "suited to both technical and non-technical stakeholders" | W8 |
| Fintech / financial services / payments | 10 (FS employer 3; FS or payments advantageous 7) | "the world's leading banks and money service businesses"; "Payment systems or financial services experience" | W1; W8 |
| Background or credit checks | 2 | "Good Credit Record" | W27 |

### How this compares with the 2026-09-29 E-Merge counts (39 posts)

- **Blazor is the new signal.** The 09-29 notes have no Blazor row. Here it ties React at 11 of 27. **Inference:** E-Merge's client mix under-represents Blazor, or it wasn't counted.
- **Angular now leads React** (13 vs 11). On 09-29 they were level (16 vs 17 of 39).
- **SQL Server is still the constant** (18 here; 18 of 39 on 09-29).
- **AI assistants are similar:** 5 of 27 here, 8 of 39 on 09-29. **LLM integration is still rare:** 1 here, 3 of 39 on 09-29.

---

## 2. What would prove each frequent requirement in a portfolio

| Requirement | Artefact a hiring manager would accept | Why this one |
|---|---|---|
| C# / modern .NET | Target the current LTS. `global.json` plus `Directory.Build.props` with nullable and warnings-as-errors. Show one non-trivial use of modern C#, such as a discriminated-result pattern or `TimeProvider` in tests | W2 asks for ".NET 10 (.NET 8 acceptable)" and "C# 14 (from 10 acceptable)" |
| REST / Web API | An OpenAPI spec checked in (`docs/api/openapi.json`) and diffed in CI. ProblemDetails errors. Versioning. An idempotency-key header with a test showing a replayed POST returns the original result | 20 of 27. W22: "BDD's and Swaggers" |
| SQL Server and tuning | A `db/` folder with migrations. A `docs/perf/` write-up: query before and after, actual execution plan (`.sqlplan`), index added, row counts and timings. One stored procedure where it beats EF, with the reason recorded in an ADR | 16 SQL Server; 6 tuning; W27 names "indexing and stored procedures" |
| EF Core | Migrations in the repo. One `AsNoTracking` or compiled-query optimisation backed by a benchmark (BenchmarkDotNet). Integration tests against real SQL Server via Testcontainers | 11 of 27; W24 "database migrations" |
| Angular | A real feature, not a toy. Standalone components, typed reactive forms, an HTTP interceptor for auth, component tests | 13 of 27; P2's core |
| React + TypeScript | The recon UI, with strict TS, a typed API client generated from OpenAPI, and Tailwind | P1: "React (5+ years) / TypeScript / … Tailwind CSS" |
| Blazor | A small Blazor app with MudBlazor or Fluent UI components | 11 of 27; W24 names MudBlazor and Fluent UI |
| Azure services | `infra/*.bicep` that deploys Container Apps or App Service, Key Vault references (no secrets in config), App Insights connection, and Service Bus. A screenshot or recording of it running, plus `docs/runbooks/deploy.md` | P1's seven services; W3 and W26 add Service Bus, Functions and APIM |
| Azure Functions | One Function with a real reason to exist, e.g. a blob-triggered PSP statement ingester or a webhook receiver that queues to Service Bus | 6 of 27 |
| Azure DevOps | `azure-pipelines.yml`, multi-stage (build, test, deploy to UAT, approval gate, prod), running in a public Azure DevOps project against the GitHub repo | 14 of 27; W20 "Deployments for Production and UAT" |
| Testing | Separate unit, integration and end-to-end test projects. A coverage report. Mutation testing (Stryker.NET) on the matching engine, to show the tests actually catch bugs | 12 of 27; W8 "unit and integration tests" |
| Clean Architecture / DDD | `docs/adr/` explaining the boundaries. An architecture test project (e.g. NetArchTest) that fails the build when Domain references Infrastructure. The ledger's aggregate invariants (debits = credits) as domain tests | 6 Clean Architecture; 2 DDD |
| Microservices / event-driven / messaging | Three repos talking only through messages and HTTP contracts. Outbox with a test proving no message is lost when the DB commits and the broker is down. Consumer idempotency test with a duplicate delivery | 10 microservices; 5 messaging |
| Integration (XML / XSD / SOAP) | One PSP or bank format ingested as XML with XSD validation, and a rejected-file test | W8 (3 ads), W11, W23, W26, W1 |
| Auth | Entra ID (or External ID) sign-in for the UI. JWT validation on the API. Role policies. A test proving an unauthenticated or wrong-role call gets 401/403 | 3 of 27 (W20, W24, W25) |
| Multi-tenancy | Tenant isolation tests that prove a cross-tenant read is refused at the API **and** at the data layer (EF global filter plus a test that bypassing it fails). 0 posts ask, so this is an extra and should be framed as security | Shows authorisation design. **Inference** |
| Observability | OpenTelemetry traces across recon → ledger → message. A saved App Insights query or workbook (`ops/workbooks/*.json`). `docs/slo.md` | P1 "Implement application monitoring and logging"; W24 "audit logging" |
| Production support / RCA | `docs/incidents/YYYY-MM-DD-*.md` blameless postmortem for an induced failure, with a regression test linked | W8, W9, W11, W22, W27 |
| Security | `docs/security/threat-model.md` (STRIDE per trust boundary). CodeQL and Dependabot in CI. Secret scanning. A `SECURITY.md` | 6 of 27; P1 "Secure Software Development" |
| Code reviews | Merged PRs with real review threads: self-review comments explaining trade-offs, plus at least one PR where AI review comments were triaged as accepted, rejected or deferred | 15 of 27, the most-named practice after C#, REST and SQL Server |
| AI throughout the SDLC | See section 3. In short: PR descriptions recording what AI generated, what you rejected and why, and what tests caught; an AI standards document; prompt and agent configuration files in the repo | P1 mandatory |
| LLM features / MCP | The break-explainer, with an eval suite in CI (citation accuracy against planted breaks), and an MCP server with read-only, tenant-scoped tools | P1 only. A differentiator, not a requirement |
| Agile | GitHub issues with acceptance criteria, milestones as iterations, and a CHANGELOG. Keep it light: 11 of 27 mention Agile, but none ask for proof | — |
| Mentoring | `CONTRIBUTING.md`, labelled good-first-issues, and a written guide (blog or `docs/guides/`), e.g. "How to review AI-generated code in this repo" | 10 of 27; P1 "Promote AI-enabled development practices across teams" |
| Fintech domain | Double-entry invariants, idempotent payouts, reconciliation with planted breaks, and Xero/Sage journal export. randmatch already proves this | 10 of 27 mention FS or payments |

---

## 3. The workflow to demonstrate, step by step

What the posts ask for in their own words:
- AI at every step: "Code generation / Refactoring / Documentation generation / Test development / Troubleshooting and debugging / Architectural analysis" ([P1]).
- "Conduct peer code reviews" ([P1]); code reviews appear in 15 of 27.
- "Develop and execute unit and integration tests" ([W8]).
- "Build and maintain CI/CD pipelines" ([P1]).
- "Deployments for Production and UAT" ([W20]).
- "Monitor application performance and reliability" ([P1]).
- "Perform root cause analysis (RCA)" ([W8]).
- "Collaborate on a common (UML) design model" ([W8]).
- "BDD's and Swaggers" ([W22]).

The paths below are suggested conventions, not quotes.

| Step | Artefact in the repo (path convention) | How AI is used | How the AI output is checked |
|---|---|---|---|
| Requirement | GitHub issue from `.github/ISSUE_TEMPLATE/feature.yml`: problem, acceptance criteria as Given/When/Then, out-of-scope. Optionally `docs/requirements/RM-<n>.md` | Draft acceptance criteria and edge cases from a rough note | You cut or rewrite. Each criterion must map to a test name later, so unmappable criteria are deleted |
| Design | `docs/design/<feature>.md` with a Mermaid sequence or C4 diagram (meets W8's "UML design model") and an OpenAPI change | "Architectural analysis" ([P1]): ask for 2–3 options with failure modes | Record which option was rejected and why. Check the AI's claims about a library or Azure limit against docs, and link the doc |
| ADR | `docs/adr/NNNN-<title>.md` in MADR format, with an extra **"AI input"** section: what was proposed, what was adopted, what was rejected and why | Generate the first draft of the alternatives | The decision and its consequences are yours. The ADR is merged only with a human-written "Decision" paragraph |
| Implementation | `src/...`; repo-level agent instructions (`CLAUDE.md` / `AGENTS.md` / `.github/copilot-instructions.md`); reusable prompts in `.claude/commands/` or `prompts/`. This meets P1's "Create and maintain effective prompts and AI workflows" | Code generation and refactoring with Claude Code, Copilot or Cursor | Analyzers and warnings-as-errors. Architecture tests. Note in the PR any code you rewrote (e.g. "AI used `float` for amounts; replaced with `decimal`, added test") |
| Tests | `tests/*.UnitTests`, `tests/*.IntegrationTests` (Testcontainers SQL Server/Postgres), `tests/e2e` (Playwright, optional: no post names it) | "Test development" ([P1]): generate cases from the acceptance criteria | **Mutation testing (Stryker.NET)** on core logic. A test that survives mutation is vacuous and gets rewritten. Paste the mutation score into the PR |
| AI review | PR template section "AI involvement": tools, generated vs hand-written, review comments accepted or rejected | An AI reviewer pass on the diff (security, performance, maintainability: P1's four criteria) | Every accepted AI finding needs a failing test or a reasoned fix. Rejected findings get a one-line reason. This is the "critically evaluate AI-generated outputs" evidence ([P1]) |
| Security review | `docs/security/threat-model.md` updated per feature; CodeQL, Dependabot and secret scanning in CI; `SECURITY.md` | Ask the AI to attack the design: tenant escape, replayed webhook, forged signature | Each claimed vulnerability gets a reproduction test. Unproven claims are recorded as "not reproducible" |
| PR | `.github/pull_request_template.md`; `CODEOWNERS`; small PRs linked to the issue and ADR | Draft the description and release note | Description must list the tests proving each acceptance criterion. Self-review comments on the risky lines |
| CI/CD | `.github/workflows/ci.yml` **and** `azure-pipelines.yml` (14 of 27 name Azure DevOps). Gates: build, tests, coverage, CodeQL, OpenAPI diff, **LLM eval gate** for the explainer | AI helps write pipeline YAML | The pipeline must fail red at least once on purpose, e.g. a broken eval threshold. Keep the screenshot or link |
| Deploy | `infra/main.bicep` + `infra/env/{uat,prod}.bicepparam`; pipeline stages UAT → approval → prod (W20 "Production and UAT") | Draft Bicep | `what-if` output attached to the PR. No secrets in params; Key Vault references only |
| Monitor | OpenTelemetry → App Insights; `ops/workbooks/*.json`; `docs/slo.md`; alert rules in Bicep | Ask for KQL queries over traces | Each query validated against a known induced event, e.g. a planted break from `randmatch-sim` |
| Incident | `docs/incidents/YYYY-MM-DD-<slug>.md` (blameless: timeline, impact, root cause, contributing factors, actions) with a linked regression test and PR | "Troubleshooting and debugging" ([P1]): AI summarises logs and traces and proposes hypotheses | Root cause is accepted only once a test reproduces it and passes after the fix. Note any AI hypothesis that was wrong |
| Productivity evidence | `docs/ai-engineering/metrics.md`: per-PR notes on time, rework and defects caught by tests in AI-generated code | — | Label it self-reported. P1 asks to "Demonstrate measurable productivity improvements through responsible AI tool usage", and honest numbers beat impressive ones. **Inference** |
| Standards | `docs/ai-engineering/standards.md`: what AI may and may not do in this repo, review rules, data rules (no real merchant data in prompts, POPIA) | — | Meets "Contribute to the organization's AI Engineering standards and best practices" ([P1]). Doubles as mentoring evidence |

---

## 4. Gap analysis: randmatch against the posts

| Requirement (count / 27) | Covered by randmatch? | Gap | Smallest change |
|---|---|---|---|
| C#, modern .NET, ASP.NET Core, REST (26 / 17 / 20) | **Yes**: recon and ledger APIs | Nothing material | Target the current LTS (W2 names .NET 10) |
| SQL Server, T-SQL, tuning (18 / 6) | **Partly**: recon on SQL Server | Depth isn't planned or visible | `docs/perf/` write-ups with execution plans, one stored procedure justified in an ADR, and indexing on the matching query |
| PostgreSQL (2, P1 req 3+ yrs) | **Yes**: ledger | A portfolio can't create "3+ years" ([P1]) | Keep. Be honest on the CV |
| EF Core (11) | **Unspecified** in plan | — | EF Core plus migrations in recon. Dapper or raw SQL for ledger hot paths with a recorded reason |
| Angular (13) | **No** | **Largest stack gap.** Decisive for P2, W2, W20, W21, W22 | Build the **ledger operator console** in Angular: journal browser, export-batch approval, idempotency-key lookup |
| React + TS (11 / 7) | **Yes**: recon UI | Tailwind not stated (P1 names it) | Use Tailwind in recon |
| Blazor (11) | **No** | Second-largest front-end gap | Optional: `randmatch-sim` control panel in Blazor (MudBlazor) for configuring planted breaks and starting streams. Internal tooling is a natural fit for Blazor. **Inference** |
| Azure named services (17 any; P1 lists 7) | **No services named in plan** | Large gap for P1, W3, W10, W12, W20, W26 | Bicep: Container Apps or App Service (recon), Key Vault, App Insights, Azure SQL. One Azure Function (statement-file or webhook ingest) |
| Azure OpenAI (1) | **Partly**: explainer exists, provider unstated | — | Put the explainer behind `Microsoft.Extensions.AI` `IChatClient` and ship an Azure OpenAI config. The 09-29 notes list `Microsoft.Extensions.AI.OpenAI` 10.10.1 and the official Anthropic C# SDK implementing `IChatClient` |
| Messaging: Service Bus (3) vs Kafka (1, adv) | **Partly**: outbox → Kafka | The market names Service Bus 3× Kafka; IBM MQ appears in one 3-ad role | Make the outbox publisher transport-agnostic. **Deploy on Service Bus**; keep Kafka for local docker-compose |
| Docker (9) / Kubernetes (8, mostly adv) | Docker implied by sim; no Kubernetes | Kubernetes is mostly advantageous | Container Apps covers containers in the cloud. Skip Kubernetes unless a target post requires it |
| CI/CD (13), Azure DevOps (14), GitHub Actions (1) | **Unspecified** | Azure DevOps missing | `azure-pipelines.yml` (multi-stage with UAT approval) for recon, alongside GitHub Actions |
| IaC (1 counted) | **No** | Small market ask, but P1 names it | Bicep under `infra/` (same change as Azure above) |
| Testing: unit, integration (12 / 4) | **Partly**: evals planned | Unit, integration and mutation testing not stated | Testcontainers integration tests in all three repos; Stryker.NET on the matching engine and ledger invariants |
| Clean Architecture / DDD / CQRS (6 / 2 / 1) | **Implied**: ledger is naturally DDD | Not explicit | Architecture tests plus ADRs. Optional: MediatR-style pipeline in recon (W24) |
| Microservices / event-driven (10 / 2) | **Yes**: three repos plus outbox | — | Contract tests between sim → recon → ledger |
| XML / XSD / SOAP integration (6) | **No** | Formats in the plan are CSV exports and webhooks | Have `randmatch-sim` emit one bank-statement feed as XML (ISO 20022 camt.053-style) with an XSD, validated in recon. Covers W8's "XML messaging and schema validation". camt.053 being in use at SA banks is **Unverified** |
| Auth: Entra ID / B2C / API auth (3) | **No** | — | Entra ID (or External ID) sign-in, JWT on the APIs, role policies. Azure AD B2C's status for new tenants is **Unverified**, so check before choosing |
| Multi-tenancy / RBAC (0) | **No** | No post asks | Bookkeeper firm → client merchants is the natural tenant model. Add it as a **security** demonstration with cross-tenant refusal tests. Don't market it as a posting requirement |
| Observability (2) / RCA (5) | **No** | — | OpenTelemetry → App Insights; a "game day" where the sim plants a broker outage or duplicate webhook, written up as a postmortem |
| Security (6) | **No** | — | Threat model, CodeQL and Dependabot, webhook signature verification tests, and a POPIA data-handling note |
| Code reviews (15) | **No** (process not planned) | — | PR template plus visible review threads, including triage of AI review comments |
| AI coding assistants (5; P1 mandatory) | **Not planned as artefacts** | P1 cares most about this | Section 3: `CLAUDE.md`/`AGENTS.md`, PR "AI involvement" sections, `docs/ai-engineering/standards.md` and `metrics.md` |
| LLM features / MCP / agents (1) | **Yes, over-covered** | — | Keep scope tight: explainer, citations, eval gate, read-only MCP. That is already more than any post asks |
| Fintech domain (10) | **Yes, strongly** | — | Add one transactional-systems angle: idempotent payout posting under concurrent duplicate webhooks (W27 names "POS or transactional systems") |
| Legacy .NET Framework / MVC / WebForms (10) | **No** | Can't be proven in greenfield code | CV and work history. Optionally an ADR on how you'd strangle a WebForms module, which is talk, not proof. **Inference** |
| Mobile: Flutter, MAUI (1 counted; ~5 unread MAUI ads) | **No** | Out of scope | Leave it |
| Power Platform, SSRS (1 each) | **No** | Niche | Leave it |
| Mentoring (10) | **No** | — | `CONTRIBUTING.md`, good-first-issues, a written guide (e.g. on reviewing AI output) |

### The ChatGPT "AI Operations Platform" suggestion

I have only the two elements the brief names, not the full text, so anything beyond them is **Unverified**.

| Element | Can randmatch absorb it? | How |
|---|---|---|
| Multi-tenant workspaces with RBAC | **Yes** | A bookkeeper firm is a tenant; merchants are sub-tenants; roles are Owner, Reviewer and Read-only. Include isolation tests at API and data layers |
| AI assistant that queries application data | **Yes, already planned** | Break-explainer plus an MCP server exposing read-only, tenant-scoped tools (`get_break`, `list_unmatched`, `get_journal`) |
| What such platforms usually also include: prompt and version tracking, per-call audit log, cost and token tracking, human approval before AI-proposed actions. **Inference** about typical scope | **Yes** | Store every explanation with model, prompt version, citations, tokens and cost. Require human approval before any AI-suggested correcting journal reaches the ledger. That also gives the eval suite real data |

**Conclusion:** the AI Operations Platform adds no market-demanded capability that randmatch can't hold. A separate product would mean two half-finished repos instead of one finished one. **Inference.**

---

## 5. Recommendation

**Build one product, randmatch, with the five changes from the verdict.** A second, different project would only make sense for a segment randmatch can't credibly serve:

- **Legacy MVC, WebForms or .NET 4.7.2 maintenance roles** (10 of 27): no portfolio fixes this; your work history does.
- **Mobile .NET (MAUI, Flutter):** out of scope for this target.

Neither justifies a second build. **Inference.**

### Priority order, by how many of the 27 posts each change unlocks

1. **Azure services plus Bicep:** 17 posts mention Azure, and P1 names seven services.
2. **Azure DevOps pipeline:** 14 posts.
3. **Angular operator console on the ledger:** 13 posts, including post 2.
4. **SQL Server tuning evidence in recon:** 16–18 posts.
5. **The AI-SDLC artefacts from section 3:** P1 mandatory; 5 posts name AI assistants.
6. **Visible review threads and an incident write-up:** 15 posts name code reviews; 5 name production RCA.
7. **Blazor sim panel, XML/XSD feed, Service Bus transport:** 11, 6 and 3 posts.

### Two blunt points

- **Post 1 is a stretch on years, not on stack.** It is mandatory-years heavy ("5+ years React", "3+ years PostgreSQL") and is in Cape Town with no remote option stated ([P1]). randmatch can show capability but not tenure.
- **Post 2 is mostly an Angular job.** It wants Angular, ASP.NET MVC and T-SQL ([P2]). Without the Angular change, randmatch proves almost nothing that post asks for beyond C# and SQL.
