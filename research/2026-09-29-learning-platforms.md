# Learning platforms against the target: what to add to Dometrain, and what not to

Primary-source comparison of learning platforms for the settled target: **a .NET full-stack
engineer at a South African fintech or bank, with data as the edge.** The target evidence is
section 8 of `2026-09-28-sa-fintech-target-roles.md` (Investec I-1, I-2, I-3). The Dometrain
baseline, and its gaps and partials, come from `2026-09-29-dometrain-catalogue.md`. This file
answers five questions: can Coursera replace or extend Dometrain; which other hands-on
platforms are worth adding; where Angular and React should come from; where the security gap
gets filled; and where Azure DevOps Pipelines gets learned.

The user has five years of production C#, holds an active Dometrain subscription, plans React
on Scrimba later, and wants hands-on learning: labs, graded exercises, projects and sandboxes,
not only video. **This file records no prices.** It states the access model in words (free,
subscription, per-course purchase) only where that changes the recommendation.

**Method.** Everything was read on 2026-09-29.

- **Coursera.** Course and certificate pages are server-rendered. Each carries a
  `window.__APOLLO_STATE__` JSON block with every module, every item (typed `LECTURE`,
  `ASSIGNMENT`, `UNGRADED_LAB`, `PLUGIN` for the "Guided Lab" items, `PEER_REVIEW`), each
  module's total and lecture duration, the instructor record, and a `launchedAt` timestamp. I
  ran 13 catalogue searches through `coursera.org/search?query=…`. For every Microsoft-authored
  .NET, SQL Server, Azure developer and DevOps programme they turned up, I downloaded the
  programme page and all 25 component course pages. I then searched every module, item title
  and description for the Dometrain skill keywords. Coursera's public `api.coursera.org`
  search finder returns "not implemented", so the search pages are the source.
- **Microsoft Learn.** I read the public catalog API (`learn.microsoft.com/api/learn/catalog`:
  3,382 modules, 817 learning paths, 37 Applied Skills, 152 certifications). I read unit pages
  for the exercise wording, the certification pages for status, and the Learn FAQ.
- **Pluralsight.** I used `pluralsight.com/sitemap.xml` (29,712 URLs, 2,170 of them labs). Path
  pages embed each course's title, author, level and duration as JSON, and lab pages show
  "Last updated".
- **Frontend Masters and the others.** Frontend Masters course pages are server-rendered, and
  the catalogue page lists 415 course slugs. Codecrafters exposes
  `backend.codecrafters.io/api/v1/courses?include=language-configurations.language`. For
  Scrimba, the sitemap and each page's meta tags were all that could be read, because course
  bodies are JS-rendered. Exercism, Educative, Brent Ozar, Duende, Andrew Lock, angular.dev and
  react.dev pages were read directly.
- **Unreachable.** Udemy returned 403. Erik Darling's course store is JS-rendered with no
  sitemap. See Sources.

Anything inferred is marked **Inference** or **Unverified**. No third-party reviews or
listicles were used.

---

## The verdict

**Keep Dometrain as the back-end spine. Do not add Coursera. Fill the gaps with free
first-party sources, each of which has its own hands-on form, plus one paid SQL Server
specialist.** Recommended stack:

| Need | Primary source | Hands-on form | Access |
|---|---|---|---|
| C# and .NET back end: APIs, EF Core, Dapper, testing, messaging, architecture, caching, OTel, Azure app services, TypeScript | **Dometrain** (already held) | Video, plus Dometrain's "Hands-On" and "Let's Build It" series | Subscription (held) |
| **Angular** (primary front end) | **angular.dev**: the in-browser "Learn Angular" tutorial, plus the signals, signal forms and deferrable-views tutorials and "first app" | Interactive in-browser steps with "Reveal answer" | Free |
| Angular, paid depth (optional) | **Frontend Masters Angular path** (Mark Techson of Google; Alex Okrushko, NgRx and Angular GDE, 2026, Angular 21) | Video with a code-along project repo | Subscription |
| React (second, notes-level) | **react.dev/learn** first. Scrimba "Learn React" (Bob Ziroll) is a sound choice if you want the interactive scrim format | react.dev: in-page code challenges. Scrimba: interactive screencasts | Free (react.dev); the Scrimba course is labelled free |
| **SQL Server indexing, plans, Query Store** (I-2) | **Microsoft SQL docs** (index design guide, Query Store, execution plans) and **Microsoft Learn DP-300 path "Optimize query performance in Azure SQL"**, then **Brent Ozar's Fundamentals of Index Tuning and Query Tuning** | Learn exercises in your own Azure subscription. Brent's classes have optional labs on the Stack Overflow database | Free; Brent is per-class purchase or a season pass |
| **OAuth2, OIDC, Identity, JWT** | **Microsoft Learn ASP.NET Core security docs** (Identity, JWT bearer, OIDC, all updated 2026-09-18) plus the **Duende IdentityServer quickstarts**, on top of the specs already listed in the Dometrain file | Quickstarts with reference solutions; Duende runs in trial mode for development | Free |
| **Azure DevOps Pipelines** (I-2) | **Microsoft Learn**: the "Implement security through a pipeline using Azure DevOps" path and the AZ-400 CI and CD paths, then the matching **Applied Skills** credential | Lab units in your own Azure DevOps organisation and Azure subscription. The credential is assessed in an interactive lab | Free learning; you need an Azure subscription |
| Build-it-yourself data-edge practice (optional) | **Codecrafters** "Build your own SQLite / Redis / Kafka" in C# | Test-driven staged challenges run against your repo | Subscription (C# track is beta) |

Five findings change earlier assumptions:

1. **Coursera cannot cover what Dometrain covers.** Microsoft's own Coursera certificates are
   labelled **Beginner** and say "You don't need any background knowledge". Across 25 Microsoft
   course syllabi, **none** mentions Dapper, MassTransit, RabbitMQ, Service Bus, Polly or
   resilience, OpenTelemetry, Serilog, DDD, CQRS, API versioning, idempotency, NUnit, Moq,
   Testcontainers, `Span<T>`, LINQ or Query Store. Coursera goes further than Dometrain on two
   things only: SQL Server execution plans, DMVs and isolation levels (the Microsoft SQL Server
   certificate), and ASP.NET Core Identity. Microsoft's free docs and Brent Ozar teach both more
   deeply. See section 1.
2. **Microsoft Learn sandboxes no longer exist.** The Learn FAQ says: "Sandboxes are no longer
   available. To complete exercises in training modules, you'll need access to an Azure
   subscription." The brief assumed free sandboxes. Plan for a free Azure trial or a
   pay-as-you-go subscription, and tear resources down after each lab.
3. **AZ-204 is retired.** The certification page says "This certification and the renewal
   assessment are retired". Microsoft's Skills Hub post lists AZ-204's retirement as **July 31,
   2026**, with **AI-200 (Azure AI Cloud Developer Associate)** as the replacement. The AI-200
   certification page lists "Python programming" among its required skills. AZ-204 is no longer
   a target, and AI-200 is a poor fit for a C# engineer. AZ-400 (DevOps Engineer Expert) is live,
   but it requires Azure Administrator (AZ-104) or the retired Azure Developer Associate first.
4. **Scrimba has no Angular course.** None of the 3,980 URLs in Scrimba's sitemap contains
   "angular". Scrimba can only ever be the React source.
5. **If one extra paid subscription is taken, Pluralsight covers the most gaps at once.** Its
   paths are on ASP.NET Core 10, and it has Kevin Dockx's "Securing ASP.NET Core 10 with OAuth2
   and OpenID Connect" (3h43m, Advanced), graded in-browser code labs updated this month, an
   AZ-400 path, and an Angular fast track. **Inference:** it overlaps Dometrain heavily on the
   back end. It is only worth it if graded labs matter more to you than the cost of a second
   subscription. The free stack above covers the same gaps.

---

## 1. Can Coursera cover everything Dometrain does, and more?

**No. Coursera's .NET catalogue is beginner-level Microsoft certificates plus republished
third-party video. It is broad where Dometrain is broad, but much shallower, and it has no
authored depth on the distributed-systems, observability and performance topics where Dometrain
is strongest.**

### 1.1 What Microsoft publishes on Coursera

All courses below list the instructor as "Microsoft", an organisation record with no named
person. All are marked Beginner unless stated. "Launched" is the course's `launchedAt` date in
the page data.

| Programme | Level (Coursera's label) | Courses | Stated length |
|---|---|---|---|
| [Microsoft Back-End Developer](https://www.coursera.org/professional-certificates/microsoft-back-end-developer) | Beginner. "You don't need any background knowledge" | Foundations of Coding Back-End; Introduction to Programming With C#; Back-End Development with .NET; Database Integration and Management; Security and Authentication; Performance Optimization and Scalability; Data Structures and Algorithms; Deployment and DevOps | "approximately 6 months … 10 hours a week" |
| [Microsoft Full-Stack Developer](https://www.coursera.org/professional-certificates/microsoft-full-stack-developer) | Beginner | The back-end set, plus Introduction to Web Development, **Blazor** for Front-End Development, Full-Stack Integration (Blazor and SignalR) and a capstone | not re-read |
| [Microsoft Front-End Developer](https://www.coursera.org/professional-certificates/microsoft-front-end-developer) | Beginner | C#, web development, **Blazor**, UI/UX, web app security | not re-read |
| [Microsoft Getting Started with ASP.NET Core](https://www.coursera.org/professional-certificates/microsoft-aspnet-core-developer) | Intermediate | Introduction to ASP.NET Core Framework; Data Management and Application Features; Security, Testing, and Deployment | P3M in the page's JSON-LD |
| [Microsoft SQL Server](https://www.coursera.org/professional-certificates/microsoft-sql-server) | Beginner | SQL Foundations; Data Manipulation and Transactions in SQL Server; Relational Database Design and Advanced Querying; Indexing, Performance Optimization & Functions in SQL Server; Security, Maintenance & Integration with BI Tools | P3M |
| [Microsoft Azure Developer Associate (AZ-204) Exam Prep](https://www.coursera.org/professional-certificates/azure-developer-associate) | Intermediate | Seven Azure courses plus "Prepare for AZ-204" | The prep course launched **2021-10-19**, and **the exam is retired** (verdict, point 3) |
| [Microsoft DevOps Engineering](https://www.coursera.org/professional-certificates/devops-engineering) | **Advanced** | DevOps Platforms & Source Control; Pipeline Engineering & Automation; Cloud Native & IaC Management; Observability & Metrics; career course | Courses launched 2026-07-08 to 2026-07-10 |
| [Beginners Guide to C# Fundamentals](https://www.coursera.org/professional-certificates/beginners-guide-to-c-sharp-fundamentals) | Beginner | Four C# courses, including [Professional C# Development Practices](https://www.coursera.org/learn/professional-c-development-practices) (launched 2026-01-16) | P4M |

**Currency.** Launch dates run from 2024-10-30 (Introduction to Programming With C#) to
2026-07 (DevOps Engineering). Only one outline names a .NET version: [Introduction to ASP.NET
Core Framework](https://www.coursera.org/learn/introduction-to-aspdotnet-core-framework)
(launched 2025-11-21) says learners "set up the .NET 9.0 SDK". No outline names .NET 10.

**How hands-on it is.** The item types are consistent across the Microsoft courses. As an
example, [Security and Authentication](https://www.coursera.org/learn/security-and-authentication)
(launched 2025-02-05) totals **39.1 hours of estimated effort, of which 5.0 hours is video**. The
rest is 27 assignments (practice quizzes, "Activity" write-ups and one graded quiz per module,
which the page labels "AI Graded"), 10 "You Try It!" ungraded labs, 10 "Guided Lab" plugins of
about 15 minutes each, and one peer-reviewed capstone. The other courses follow the same shape:

| Course | Effort / video | Ungraded labs | Guided labs | Assignments |
|---|---|---|---|---|
| Back-End Development with .NET | 43.5h / 9.1h | 10 | 10 | 26 |
| Database Integration and Management | 26.3h / 4.3h | 7 | 7 | 23 |
| Performance Optimization and Scalability | 44.5h / 4.3h | 8 | 7 | 43 |
| Deployment and DevOps | 37.3h / 5.4h | 7 | 7 | 37 |
| Security, Testing, and Deployment | 29.6h / 4.0h | 15 | 1 | 20 |
| Indexing, Performance Optimization & Functions in SQL Server | 18.9h / 1.1h | 1 | 0 | 9 |
| Pipeline Engineering & Automation (DevOps Engineering) | 6.4h / 0.2h | 0 | 0 | 13 ("Hands-on Activity" and quizzes) |

So Coursera is more exercise-heavy than Dometrain by item count. **Unverified:** what the
"Guided Lab" plugins run on (an in-browser IDE, or instructions for local work). The page shows
only a "Completing the Guided Labs" lecture and a "Navigating the Guided Labs" reading. The labs
are ungraded, and the graded items are quizzes and AI-graded activities, not automated test
suites on your code.

**Access model.** The programme JSON-LD shows `isAccessibleForFree: true` with an offer category
of "Subscription", and the page says "Enroll for free". **Unverified:** which items are locked
without the subscription.

### 1.2 Skill by skill against the Dometrain back-end rows

"Found" means the skill appears in module or item titles or descriptions of the Microsoft
courses above. "None" means none of the 25 syllabi mention it.

| Skill (Dometrain rating) | Dometrain | Coursera (Microsoft) | Deeper? |
|---|---|---|---|
| Async (covered) | Async and Parallel ZTH courses, internals | "Asynchronous Programming in C#" modules in Intro to C# and Professional C# Development Practices | Dometrain |
| LINQ, generics, records, memory/`Span<T>` | Covered or partial | **None** for LINQ, records or `Span`/`Memory` | Dometrain |
| Dependency injection, configuration (covered) | DI ZTH, Config and Options ZTH | "Dependency Injection and Configuration" module (6.5h) in Data Management and Application Features | Dometrain |
| ASP.NET Core Web APIs, Minimal APIs (covered) | REST APIs ZTH, Minimal APIs ZTH | Back-End Development with .NET; "Creating Your First ASP.NET Core Application" (Minimal APIs, EF Core) | Dometrain (versioning, idempotency, HATEOAS are absent on Coursera) |
| EF Core (covered) | 8h32m ZTH with performance and concurrency | Database Integration and Management; "Data Access with Entity Framework Core" module | Dometrain |
| Dapper (covered) | ZTH Dapper | **None** | Dometrain |
| xUnit, integration testing (covered) | Several ZTH courses | "Testing ASP.NET Core Applications" module: unit, integration, TDD; the only mentions of xUnit and `WebApplicationFactory` | Dometrain |
| NUnit (gap), Testcontainers (partial), mocking (covered) | as mapped | **None** for any of them | Neither closes the gap |
| Clean architecture, vertical slice, DDD, design patterns, microservices (covered) | Dedicated courses | One "Clean Architecture" mention; "microservice" twice | Dometrain |
| MassTransit, Service Bus, background jobs (covered or partial) | Dedicated courses | **None** | Dometrain |
| Polly / resilience (partial) | Lessons | **None** | Neither; use Microsoft Learn's resilience docs |
| Caching / Redis (covered) | 7h and 23h courses | "Caching Strategies With .NET Core" (in-memory, Redis, expiration) | Dometrain |
| OpenTelemetry, Serilog (covered) | ZTH courses | **None**; generic "logging" lessons only | Dometrain |
| Performance / benchmarking (covered) | BenchmarkDotNet, GC, 1BRC | None for BenchmarkDotNet or GC | Dometrain |
| **ASP.NET Core Identity (gap)** | none | **Found:** "Securing APIs with ASP.NET Identity" (registration, roles, claims, token auth, external providers); "Authentication and Authorization" module in Security, Testing, and Deployment | **Coursera** is ahead of Dometrain here. Microsoft's Identity docs are the primary source anyway |
| OAuth2 / OIDC (partial) | Entra ID configuration | One 10-minute reading, "Using OAuth 2.0 and OpenID Connect for External Authentication" | Neither teaches the protocol |
| JWT (partial) | REST APIs lessons | "Role-Based Access Control and JWT Authentication" module, 4 guided labs | Coursera is broader. Microsoft docs and Duende go deeper |
| **SQL Server indexing and plans (gap)** | EF Core lesson only | **Found:** "Optimizing Database Queries" (clustered and non-clustered indexes, bottlenecks); SQL Server certificate course 4 ("Understanding Execution Plans", "Execution Plan Problem Patterns", DMVs); course 2 (isolation levels, deadlocks and blocking) | **Coursera** is ahead of Dometrain. Brent Ozar and the Microsoft docs go deeper (section 2) |
| Azure DevOps Pipelines (gap) | none | "Setting Up CI/CD Pipelines With GitHub Actions and Azure DevOps": one "Overview of Azure DevOps Tools" and two integration lectures. The DevOps Engineering certificate covers YAML template governance, agent sizing and DORA | Coursera is ahead of Dometrain. Microsoft Learn's own labs are the better hands-on source |
| .NET Aspire (covered) | GS Aspire | "How to Convert Applications to .NET Aspire and Deploy to Azure" | Dometrain |

**The answer.** Coursera gets ahead of Dometrain on three gap rows: Identity, SQL Server plans
and indexes, and Azure DevOps. It is behind or absent on every other back-end row. In all three
of those rows the owning vendor's free material (section 2) or a specialist teaches it more
deeply, and against a real environment. **Inference:** given five years of production C#, the
beginner framing would mean skipping most of each Coursera course to reach the parts that
matter. It is not worth a second subscription for this target.

### 1.3 Non-Microsoft .NET content on Coursera

The searches also surfaced programmes from Packt, Board Infinity, EDUCBA, Edureka, LearnKartS and
LearnQuest. Examples: "ASP.NET Core MVC [.NET 8] – The Complete Guide", ".NET 8 Microservices –
DDD, CQRS & Clean Architecture" and "Angular 17", all Packt or LearnQuest. **Inference:** the
Packt items are republished video courses whose original authors are not named in the search
results. They fail the "named authoritative author" bar and I did not assess them further.
Coursera also hosts Scrimba's own specialisations, such as "Become a Professional React
Developer". Scrimba is covered in section 3.

---

## 2. Better or complementary hands-on platforms

### 2.1 Microsoft Learn (free)

- **What matters here.** The catalog API lists learning paths for exactly the gaps:
  - [Optimize query performance in Azure SQL](https://learn.microsoft.com/en-us/training/paths/optimize-query-performance-sql-server/)
    (236 min, updated 2026-08-05). Modules: "Explore query performance optimization", "Explore
    performance-based database design", "Evaluate performance improvements".
  - [Monitor and optimize operational resources in Azure SQL](https://learn.microsoft.com/en-us/training/paths/monitor-optimize-operational-resources-sql-server/) (169 min).
  - The AZ-400 paths (section 5).
  - [Implement security through a pipeline using Azure DevOps](https://learn.microsoft.com/en-us/training/paths/implement-security-through-pipeline-using-devops/) (438 min).
  - [Create cloud-native apps and services with .NET and ASP.NET Core](https://learn.microsoft.com/en-us/training/paths/create-microservices-with-dotnet/)
    (265 min). It includes resiliency, OpenTelemetry and an Azure Pipelines deploy exercise, but
    was last updated 2023-12-22 and its modules name .NET 8.
- **How hands-on it is.** Modules contain "Exercise" or "Lab" units:
  - "Evaluate performance improvements" has "Exercise: Isolate problem areas in poorly
    performing queries". It launches a DP-300 lab at `microsoftlearning.github.io/dp-300-database-administrator/`
    and says "you'll need an Azure subscription".
  - "Configure pipelines to securely use variables and parameters" has a lab at
    `microsoftlearning.github.io/implement-security-through-pipeline-using-devops/`, needing
    an Azure subscription and a validated lab environment.
  - [Create a web API with ASP.NET Core controllers](https://learn.microsoft.com/en-us/training/modules/build-web-api-aspnet-core/)
    has four exercises and "uses the .NET 8.0 SDK".
  - **Sandboxes are gone** ([Learn FAQ](https://learn.microsoft.com/en-us/training/support/faq)).
- **Applied Skills.** Two of the 37 credentials fit the target:
  - [Implement security through a pipeline using Azure DevOps](https://learn.microsoft.com/en-us/credentials/applied-skills/implement-security-through-pipeline-using-devops/)
    (updated 2025-10-15). It evaluates pipeline resource access, permissions, repo structure,
    multi-template pipelines and pipeline identity.
  - [Develop data-driven applications by using Microsoft Azure SQL Database](https://learn.microsoft.com/en-us/credentials/applied-skills/develop-data-driven-applications-by-using-microsoft-azure-sql-database/)
    (updated 2025-09-25). It evaluates developing a database, a data API, a read-only replica,
    REST import, Azure Function export and securing the database.

  Both pages say "This assessment will use an interactive lab to evaluate your performance",
  with a 72-hour wait between launches. This is the closest thing to a graded practical exam on
  any platform read. **No Applied Skill covers ASP.NET Core or C# beyond "Get started with
  classes, properties, and methods in C#"**, which is beginner-level. **Unverified:** the cost
  of an Applied Skills assessment. The pages I read do not state it.
- **Certifications.**
  - [Azure Developer Associate](https://learn.microsoft.com/en-us/credentials/certifications/azure-developer/) (AZ-204): **retired**.
  - [DevOps Engineer Expert](https://learn.microsoft.com/en-us/credentials/certifications/devops-engineer/) (AZ-400): live.
  - [Azure Database Administrator Associate](https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/)
    (DP-300): live. The English version "will be updated on October 27, 2026".
  - [SQL AI Developer Associate](https://learn.microsoft.com/en-us/credentials/certifications/developing-ai-enabled-database-solutions/)
    (DP-800): new. It covers "writing T-SQL code and developing databases in Microsoft SQL
    platforms" plus CI/CD in GitHub and embeddings. Its English version is updated October 19,
    2026.
- **Authorship and currency.** Microsoft owns the product, and the catalog records each item's
  `last_modified`. The .NET modules are mostly beginner-level. The SQL and AZ-400 paths were
  updated in June to August 2026.

### 2.2 Pluralsight (subscription)

- **What matters here** (from path-page JSON):
  - [ASP.NET Core 10 Web API](https://www.pluralsight.com/paths/aspnet-core-10-web-api): 30
    items, most by Kevin Dockx. It includes "Securing ASP.NET Core 10 with OAuth2 and OpenID
    Connect" (Kevin Dockx, Advanced, 3h43m), "Building Resilient ASP.NET Core 10 Web APIs",
    "Versioning ASP.NET Core 10 Web APIs" and "Testing ASP.NET Core 10 Web APIs".
  - [ASP.NET Core 10](https://www.pluralsight.com/paths/aspnet-core-10): 28 items. It includes
    "Securing Applications with IdentityServer" (Roland Guijt), "Secure Coding in ASP.NET Core
    10" and "Guided: Implementing JWT Authorization in ASP.NET Core 10".
  - [Entity Framework Core 10](https://www.pluralsight.com/paths/entity-framework-core-10),
    including "EF Core 10 Interactions and Performance" (Chris Behrens, Advanced).
  - [AZ-400](https://www.pluralsight.com/paths/az-400-designing-and-implementing-microsoft-devops-solutions),
    including "Build and Release Pipelines" (Henry Been, 8h11m).
  - [Angular Fast Track for Experienced Developers](https://www.pluralsight.com/paths/angular-fast-track-for-experienced-developers)
    (Jim Cooper and others).
  - [Advanced Performance and Data Engineering in SQL Server 2025](https://www.pluralsight.com/paths/advanced-performance-and-data-engineering-in-sql-server-2025).
- **How hands-on it is.** The sitemap lists 697 "codeLabs" and 319 Azure labs. Two examples:
  - [Guided: Securing an ASP.NET Core 10 API with OAuth2 Client Credentials Flow](https://www.pluralsight.com/labs/codeLabs/guided-securing-an-aspnet-core-10-api-with-oauth2-client-credentials-flow)
    (37 min, "Last updated Sep 22, 2026"). It configures JWT bearer validation against "a local
    identity provider built into the application" and is structured as challenges.
  - [Build Reactive Applications with Signals in Angular](https://www.pluralsight.com/labs/codeLabs/build-reactive-applications-with-signals-in-angular)
    (updated Sep 17, 2026). It covers `signal`, `computed`, `linkedSignal` and `httpResource`.

  Lab pages say labs sit in "Lab Libraries". **Unverified:** which plan includes them.
- **Authorship and currency.** Named authors, several of them Microsoft MVPs (Kevin Dockx, Steve
  Gordon, Shawn Wildermuth, Roland Guijt). Paths target ASP.NET Core 10 and EF Core 10, the
  newest named versions on any platform read. Kevin Dockx also authors Dometrain's Azure
  courses.

### 2.3 Frontend Masters (subscription; pages now branded "Master.dev")

- **What matters here.** The [Angular learning path](https://frontendmasters.com/learn/angular/)
  (20h1m core):
  - [Angular Fundamentals](https://frontendmasters.com/courses/angular-fundamentals/): Mark
    (Techson) Thompson, Google, 4h35m, published 2024-01-29.
  - [Intermediate Angular: Signals & Dependency Injection](https://frontendmasters.com/courses/intermediate-angular/):
    Alex Okrushko, "NgRx, Angular GDE", 4h46m, published 2026-02-12. Covers Signal Forms and
    route guards.
  - [Advanced Angular: Performance & Enterprise State](https://frontendmasters.com/courses/advanced-angular/):
    Okrushko, 5h26m, published 2026-02-13. It "focuses on Angular 21" and covers zoneless
    change detection, SSR, SignalStore and NgRx, and Vitest.

  React: [Complete Intro to React v9](https://frontendmasters.com/courses/complete-react-v9/)
  and [Intermediate React v6](https://frontendmasters.com/courses/intermediate-react-v6/) (Brian
  Holt; React 19, Server Components). There are also .NET courses: [C# and .NET Basics](https://frontendmasters.com/courses/csharp-dotnet/)
  and [Building APIs with C# and ASP.NET Core](https://frontendmasters.com/courses/dotnet-apis/)
  (Spencer Schneidenbach, Microsoft MVP, published 2024-11-05). Both are below Dometrain's
  depth. **Inference.**
- **How hands-on it is.** Video. Pages offer "Quiz Mode", and the Advanced Angular description
  "encourages coding along with provided project code". There are no graded exercises.
- **Authorship.** The strongest Angular authorship found: a Google Angular team member and an
  NgRx maintainer.

### 2.4 Scrimba

React only (section 3). No Angular, C#, SQL Server or Azure DevOps content in its sitemap,
except "Intro to DevOps" and "Learn SQL". The format is interactive screencasts in which you
edit the instructor's code in place; the meta tags describe "the most interactive, hands-on
way possible".

### 2.5 Educative (subscription)

Text lessons with an in-browser code editor ("Learn by building with project-based lessons and
in-browser code editor"). The sitemap lists C#, ASP.NET Core, EF Core and Angular courses. Two
examples:

- [Developing Applications with ASP.NET Core](https://www.educative.io/courses/developing-applications-with-asp-net-core):
  40 lessons, 2 quizzes, published 2020-09-29, modified 2024-11-21.
- [Learning Angular](https://www.educative.io/courses/learning-angular): 172 lessons, 2
  projects, modified 2026-05-11. Its JSON-LD names Packt as a contributor.

**Inference:** authorship is mixed and often book-derived, and the .NET currency is older than
Pluralsight's or Dometrain's. It is not recommended as a primary source for anything here.

### 2.6 Exercism, C# track (free)

[exercism.org/tracks/csharp](https://exercism.org/tracks/csharp): "178 exercises grouped into
62 C# Concepts, with automatic analysis of your code and personal mentoring, all 100% free", run
by 975 contributors and 1,960 mentors. It is the best free graded-exercise option for C# idiom.
**Inference:** at five years of production C# it is a warm-up or kata tool, not a curriculum
pillar. It has nothing on ASP.NET Core, SQL Server or Azure.

### 2.7 Codecrafters (subscription; some challenges free for limited periods)

The course API shows **C# as a "beta" language track**, supported on the live challenges Redis,
SQLite, Kafka, HTTP server, Git, Shell, grep, DNS server, BitTorrent and Interpreter. Each
challenge is a series of stages checked by a remote tester against your own repository. The
SQLite challenge ("Build your own SQLite", hard) teaches B-tree pages and index lookups from the
inside. **Inference:** this is the most hands-on way to deepen the data edge beyond query
tuning, and it produces a portfolio artefact. It is optional.

### 2.8 LinkedIn Learning (subscription)

The [ASP.NET Core topic page](https://www.linkedin.com/learning/topics/asp-dot-net-core) lists
565 results. The newest full courses are Christian Wenz's "Building Web APIs with ASP.NET Core 8"
(released Apr 9, 2024) and "Advanced Web APIs with ASP.NET Core 8" (Apr 23, 2024). Other popular
items date from 2020 to 2022 ("ASP.NET Core: Token-Based Authentication", Aug 27, 2021).
**Inference:** it is older and shallower than Dometrain or Pluralsight, and it offers no
hands-on advantage I could verify. Skip it.

### 2.9 Udemy

**Unreachable**: `udemy.com` returned HTTP 403 to non-browser requests. No authors, dates or
syllabi could be verified, so nothing from Udemy is recommended.

### 2.10 SQL Server specialists

- **Microsoft's own SQL docs (free).**
  - [Index Architecture and Design Guide](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide) (ms.date 2026-09-14).
  - [Monitor Performance by Using the Query Store](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store) (2025-08-21).
  - [Best Practices for Monitoring Workloads with Query Store](https://learn.microsoft.com/en-us/sql/relational-databases/performance/best-practice-with-the-query-store) (2026-01-26).
  - [Execution Plan Overview](https://learn.microsoft.com/en-us/sql/relational-databases/performance/execution-plans) (2026-01-26).
  - [Intelligent Query Processing](https://learn.microsoft.com/en-us/sql/relational-databases/performance/intelligent-query-processing) (2026-09-01).

  These are the owning reference. They are not exercises. Pair them with a local SQL Server and
  the WideWorldImporters database the `platform` repo already uses. **Unverified:** that SQL
  Server Developer edition is still a free download. Microsoft's downloads page returned 403.
- **Brent Ozar Unlimited (per-class purchase or season pass; one free course).**
  - [Fundamentals of Index Tuning 2026](https://www.brentozar.com/classes/fundamentals-of-index-tuning-2026/):
    modules on missing-index requests and on designing indexes for WHERE, ORDER BY and JOINs,
    with "Brent Does Your First Hands-On Lab" and a final lab.
  - [Fundamentals of Query Tuning 2026](https://www.brentozar.com/classes/fundamentals-of-query-tuning-2026/):
    "How SQL Server Builds Query Plans", "Execution Plans are Lying Liars", and a cardinality
    lab of four stored-procedure fixes.
  - Mastering Index Tuning and Mastering Query Tuning, which have lab assignments.

  Labs are "optional" and need "your own SQL Server lab (any edition, or Azure SQL DB / Amazon
  RDS) with the Stack Overflow database, or rent a lab VM". Recordings are on
  training.brentozar.com. [How to Think Like the SQL Server Engine](https://www.brentozar.com/training/think-like-sql-server-engine/)
  is free. The class list names Brent as the teacher of every SQL Server tuning class
  (index, query, server, columnstore, TempDB). Drew Furgiuele teaches the Python, Azure
  networking and PowerShell classes.
- **Erik Darling (Darling Data).** His site describes "self-paced video courses", and a blog
  footer references an "Everything Bundle — over 100 hours of performance tuning content". The
  course store (training.erikdarling.com) is JS-rendered with no sitemap, so **the catalogue is
  unreachable**. His free open-source procedures are directly useful hands-on tools for the
  Query Store gap: [sp_QuickieStore](https://erikdarling.com/sp_quickiestore/),
  [sp_PressureDetector](https://erikdarling.com/sp_pressuredetector/),
  [sp_IndexCleanup](https://erikdarling.com/sp_indexcleanup/) and
  [sp_HumanEventsBlockViewer](https://erikdarling.com/sp_humaneventsblockviewer/).

**Recommended order for the SQL Server gap** (**Inference**). First the Dometrain Postgres
course, from "Indexes" on, for the concepts. Then the Microsoft index guide and Query Store
pages. Then Brent's Fundamentals of Index Tuning and Query Tuning, doing the labs against the
Stack Overflow database. Then sp_QuickieStore against your own `platform` workload. Take the
Microsoft Learn DP-300 query-performance path if you want Microsoft's structured exercises too.

---

## 3. Front end

### Angular (primary; required in I-3)

**Use angular.dev, and it is enough on its own.** Add Frontend Masters' Angular path only if you
want expert-led video on top.

- [angular.dev/tutorials](https://angular.dev/tutorials) lists "Learn Angular in your browser via
  the Playground", "Build your first Angular app locally via npm", "Learn signals", "Deferrable
  views", "Learn signals forms" and an "Angular AI Tutor via MCP Server".
- [Learn Angular](https://angular.dev/tutorials/learn-angular) is "This interactive tutorial"
  with in-browser steps: "If you get stuck, click 'Reveal answer'". It is the only free,
  first-party, interactive Angular source.
- The [releases page](https://angular.dev/reference/releases) shows **v22 Active** (released
  2026-06-03), v21 and v20 in LTS, v22.2 in the week of 2026-09-21, and v23 due around June
  2027. The tutorials track the current major because the owner writes them. **Inference.**
- **Frontend Masters** (section 2.3) is the best paid complement. Its path runs from a Google
  Angular team member's Fundamentals (Angular 17+ era, January 2024) to Okrushko's 2026
  Intermediate and Advanced courses on Angular 21: Signal Forms, SignalStore, zoneless change
  detection, Vitest. That covers the "enterprise Angular" material angular.dev's tutorials stop
  short of.
- **Pluralsight** is the alternative if graded labs matter: an Angular fast-track path plus
  code labs on signals, routing, template forms, "auth flow essentials" and unit testing.
- **Scrimba** has none. **Coursera** has only Packt, LearnQuest and Edureka programmes, such as
  "Angular 17", plus Johns Hopkins' AngularJS course. The Microsoft certificates teach Blazor,
  not Angular.

### React (second, notes-level)

**react.dev first. Scrimba is a fine choice for the interactive layer, and Frontend Masters is
the pick only if you already hold that subscription for Angular.**

- [react.dev/learn](https://react.dev/learn) is the owning docs. Pages end with "Try out some
  challenges": for example "Challenge 1 of 4: Complete the gallery" on the state page, run in
  embedded Sandpack editors. [react.dev/versions](https://react.dev/versions) reads "Latest
  version: 19.3". That already meets the brief's hands-on requirement at no cost.
- Scrimba's [Learn React](https://scrimba.com/learn-react-c0e) is "Free Interactive React
  Tutorial: Learn modern React in this extensive course lead by Bob Ziroll". Scrimba also has
  [What's New in React 19](https://scrimba.com/whats-new-in-react-19-c03d),
  [React Challenges: 40 Hands-On React Exercises](https://scrimba.com/react-challenges-c02n) and
  [Advanced React](https://scrimba.com/advanced-react-c02h). **Unverified:** course length and
  last-updated dates. The course bodies are JS-rendered.
- **Inference:** since React is notes-level and Investec treats it only as the alternative,
  react.dev's challenges alone may be enough. Scrimba earns its place if its format keeps you
  practising. If you take Frontend Masters for Angular, Brian Holt's React v9 comes with it, and
  a Scrimba subscription becomes redundant.

---

## 4. The security gap: OAuth2, OIDC, ASP.NET Core Identity, JWT

Dometrain teaches the ASP.NET Core auth pipeline and Entra ID configuration, but not the
protocols or Identity (Dometrain file, section 2). The hands-on sources, in order:

1. **Microsoft Learn ASP.NET Core security docs (free, owning source).** All updated 2026-09-18
   except the SPA page:
   - [Introduction to Identity on ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/identity)
   - [Configure JWT bearer authentication](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/configure-jwt-bearer-authentication)
   - [Configure OpenID Connect Web (UI) authentication](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/configure-oidc-web-authentication)
   - [Use Identity to secure a Web API backend for SPAs](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/identity-api-authorization) (2026-03-23)

   These are docs with sample code, not labs. The hands-on part is building each one into the
   `product` repo.
2. **Duende IdentityServer quickstarts (free to learn with).** The [quickstart overview](https://docs.duendesoftware.com/identityserver/quickstarts/0-overview/)
   (updated 2026-06-04) is a graded sequence. It adds IdentityServer to an ASP.NET Core app,
   issues tokens for various clients (starting with "Protecting An API With Client
   Credentials"), secures web apps and APIs, and then adds EF-based configuration and ASP.NET
   Identity. "Every quickstart has a reference solution". Setup is `dotnet new install
   Duende.Templates`. Two more free resources:
   - The [docs home](https://docs.duendesoftware.com/) links a live demo server for testing
     OAuth 2.0, OIDC and SAML flows.
   - The [BFF docs](https://docs.duendesoftware.com/bff/) cover securing SPAs "without storing
     tokens in the browser", which matters for an Angular front end.

   The [licensing page](https://docs.duendesoftware.com/general/licensing/) says trial mode is
   available for development and testing, and a paid licence is needed for production.
   Duende's paid [training](https://duendesoftware.com/training) is workshops: a 3-day
   "Identity & Access Control for Modern Applications and APIs using ASP.NET Core" and a 1-day
   "OAuth, OpenID Connect and .NET – the Good Parts". Duende is the IdentityServer vendor, so
   this is first-party protocol teaching in .NET.
3. **Andrew Lock ([andrewlock.net](https://andrewlock.net/)).** Current, and writing about .NET
   11 previews, including Device Bound Session Credentials in ASP.NET Core (2026-09-22). His
   book "ASP.NET Core in Action, Third Edition" "supports .NET 7.0", so it is dated for API
   specifics. The blog is sponsored by Dometrain, as its banner states. Use it as reading, not
   as a hands-on source.
4. **Pluralsight (optional, paid).** Kevin Dockx's "Securing ASP.NET Core 10 with OAuth2 and
   OpenID Connect" (Advanced, 3h43m) plus the OAuth2 client-credentials and JWT guided code
   labs. This is the only graded, lab-based protocol practice in .NET found on any platform.
5. **The specs** (from the Dometrain file): RFC 9700, FAPI 2.0 Security Profile, OWASP API Top 10.
   The Investec developer portal's 3-legged OAuth is the target employer's own example.

**Inference, proposed build sequence.** First the Microsoft Identity and JWT bearer docs,
applied in the `product` API. Then the Duende quickstarts from client credentials through to
interactive login with PKCE and BFF. Then map the result against RFC 9700 and FAPI 2.0. That
yields a working OAuth/OIDC system in the portfolio, which is the evidence I-1 asks for.

---

## 5. Azure DevOps Pipelines

**Use Microsoft Learn, and have your own Azure DevOps organisation.**

- **Learning paths.**
  - [AZ-400: Implement CI with Azure Pipelines and GitHub Actions](https://learn.microsoft.com/en-us/training/paths/az-400-implement-ci-azure-pipelines-github-actions/)
    (396 min). Modules: Explore Azure Pipelines; Manage Azure Pipeline agents and pools;
    Describe pipelines and concurrency; Design and implement a pipeline strategy; Integrate with
    Azure Pipelines; plus GitHub Actions and container builds.
  - [AZ-400: Implement a secure continuous deployment using Azure Pipelines](https://learn.microsoft.com/en-us/training/paths/az-400-implement-secure-continuous-deployment/)
    (253 min). Blue-green, canary, feature toggles, configuration data.
  - [Implement security through a pipeline using Azure DevOps](https://learn.microsoft.com/en-us/training/paths/implement-security-through-pipeline-using-devops/)
    (438 min, updated 2026-06-17). Seven modules, several ending in a "Lab" unit, for example
    "Lab - Extend a pipeline to use multiple templates".
  - [Deploy a cloud-native .NET microservice automatically with GitHub Actions and Azure Pipelines](https://learn.microsoft.com/en-us/training/modules/microservices-devops-aspnet-core/)
    has "Exercise - Create an Azure DevOps pipeline to deploy your cloud-native app". It runs in
    a GitHub Codespace or locally, against your Azure subscription.
- **Graded credential.** The [Applied Skill for that path](https://learn.microsoft.com/en-us/credentials/applied-skills/implement-security-through-pipeline-using-devops/)
  is assessed in an interactive lab.
- **Lab instructions.** The path's labs are published at
  `microsoftlearning.github.io/implement-security-through-pipeline-using-devops/`. The older
  [AZ-400 lab repo](https://github.com/MicrosoftLearning/AZ400-DesigningandImplementingMicrosoftDevOpsSolutions)
  (15 labs, including "Enable Continuous Integration with Azure Pipelines" and "Configure
  Pipelines as Code with YAML") is **archived** on GitHub, with its last push on 2025-11-13.
  [azuredevopslabs.com](https://azuredevopslabs.com/) is still up, but its pages reference Azure
  DevOps Server 2019. **Unverified:** whether its labs are maintained.
- **Running pipelines for free.** The [parallel jobs page](https://learn.microsoft.com/en-us/azure/devops/pipelines/licensing/concurrent-jobs)
  says:
  - "The self-hosted free tier is automatically granted, but you must enable the
    Microsoft-hosted free tier". Enabling it gives one job of up to 60 minutes, with a monthly
    limit of 1,800 minutes.
  - "To receive the free grant of parallel jobs, link your Azure DevOps organization to a valid
    Azure subscription."
  - "Public projects are retired. New public projects can no longer be created."

  **Inference:** the simplest setup is a free Azure DevOps organisation, with a self-hosted
  agent on your own machine or the Microsoft-hosted grant once billing is linked. Then build a
  YAML pipeline for the `platform` repo from [Create your first pipeline](https://learn.microsoft.com/en-us/azure/devops/pipelines/create-first-pipeline).
- **Certification.** AZ-400 is live, but its prerequisite is Azure Administrator Associate or
  the now-retired Azure Developer Associate. **Inference:** for someone without AZ-204, AZ-400
  now means sitting AZ-104 first. The Applied Skill is the cheaper proof of the specific I-2
  ask.
- **Paid alternatives.** Pluralsight's AZ-400 path (Henry Been, "Build and Release Pipelines",
  8h11m). Coursera's DevOps Engineering certificate (Advanced; governance, YAML template
  libraries, agent sizing). Its activities are assignments. **Unverified:** whether they involve
  running real pipelines.

---

## 6. Skill → best source, for the Dometrain gaps and partials

Rows follow the Dometrain file's section 2. "Carried over" means the primary source is the one
already named in `2026-09-29-dometrain-catalogue.md` section 3, which was not re-checked here.

| Skill | Dometrain rating | Best source | Hands-on form | Complement |
|---|---|---|---|---|
| **Angular** | gap | angular.dev tutorials (Learn Angular, signals, signal forms, deferrable views, first app) | In-browser interactive steps | Frontend Masters Angular path (Angular 21); Pluralsight Angular code labs |
| **React** | gap | react.dev/learn | In-page Sandpack challenges | Scrimba Learn React (Bob Ziroll); FM Complete Intro to React v9 |
| Front-end testing (Jasmine/Karma/Jest, Playwright) | partial | angular.dev testing guide (carried over) | Tests in your own repo | FM Advanced Angular (Vitest); Pluralsight "Implement unit testing in Angular" lab |
| **SQL Server indexing, plans, performance** | gap | Microsoft index design guide, Query Store and execution-plan docs | Your own SQL Server with WideWorldImporters or Stack Overflow DB | Brent Ozar Fundamentals of Index Tuning and Query Tuning (labs); Learn DP-300 query-performance path (labs in your Azure subscription); sp_QuickieStore |
| Azure SQL | partial | Learn Applied Skill "Develop data-driven applications by using Azure SQL Database" | Lab-assessed credential | Learn "Monitor and optimize operational resources in Azure SQL" path |
| Data modelling | partial | Dometrain Postgres and DDD; Microsoft SQL Server certificate course 3 on Coursera is the only structured SQL Server option, and it is beginner-level | none | **Inference:** model the payments ledger in the `product` repo |
| **Azure DevOps Pipelines** | gap | Learn "Implement security through a pipeline using Azure DevOps" path and AZ-400 CI and CD paths | Lab units in your own Azure DevOps org and Azure subscription | Matching Applied Skill (lab-assessed); Pluralsight AZ-400 path |
| **ASP.NET Core Identity** | gap | Microsoft Learn Identity docs; "Use Identity to secure a Web API backend for SPAs" | Build into `product` | Duende quickstart "adding support for ASP.NET Identity" |
| OAuth2 / OIDC | partial | Duende IdentityServer quickstarts plus the Microsoft OIDC docs; RFC 9700 and FAPI 2.0 (carried over) | Quickstarts with reference solutions; demo server | Pluralsight Kevin Dockx OAuth2/OIDC course and client-credentials lab |
| JWT, token handling | partial | Microsoft "Configure JWT bearer authentication" | Build into `product` | Duende Access Token Management docs; Pluralsight JWT guided lab |
| OWASP | partial | OWASP ASVS and API Security Top 10 (carried over) | Checklist against your API | FM Web Security v2 (Steve Kinney, 2024; JWT and browser security) |
| NUnit | gap | nunit.org docs (carried over, not checked) | Port one xUnit suite | none needed. **Inference:** the concepts transfer |
| Testcontainers | partial | dotnet.testcontainers.org (carried over) | Tests in your repo | none |
| Resilience (Polly) | partial | Microsoft Learn .NET resilience docs (carried over) | Build | Learn module "Implement resiliency in a cloud-native .NET microservice" (two exercises); Pluralsight "Building Resilient ASP.NET Core 10 Web APIs" |
| Azure Service Bus | partial | Microsoft Learn Service Bus docs (carried over) | Your Azure subscription | none |
| Container Apps / AKS | partial | Microsoft Learn (carried over) | Your Azure subscription | Applied Skill "Deploy cloud-native apps using Azure Container Apps" (updated 2026-07-28) |
| Terraform | partial | HashiCorp Azure tutorials (carried over) | Tutorials in your subscription | none |
| Cosmos DB | partial | Learn paths "Define and implement an indexing strategy" and "Optimize query and operation performance" for Cosmos DB for NoSQL | Exercises in your subscription | none |
| Memory / `Span<T>`, generics | partial | Microsoft Learn "Memory and spans" and C# guide (carried over) | Benchmarks in your repo with Dometrain's BenchmarkDotNet course | Exercism C# track for idiom drills |
| Idempotency (and for payments) | partial | IETF idempotency-key draft and Stripe docs (carried over) | Build into `product` | none |
| MongoDB | gap | MongoDB docs (carried over) | n/a | Low priority. I-1 lists it only as advantageous |
| Data engineering | gap | Microsoft Learn ADF, DP-750, Databricks (carried over) | n/a | Codecrafters "Build your own SQLite / Kafka" in C# for internals |
| Semantic Kernel | gap | Microsoft Learn SK overview (carried over) | n/a | none |
| Ledgers, reconciliation, payments, open banking, POPIA | gap | Carried over: Investec portal, UK Open Banking standards, Information Regulator | Build material, not courses | No platform read here teaches the fintech domain |

---

## 7. Open questions

1. **Do you have, or will you open, an Azure subscription for learning?** Microsoft Learn
   sandboxes are gone. Every Learn exercise for the SQL, pipeline and Azure gaps now needs one,
   and so does the Microsoft-hosted Azure Pipelines free grant.
2. **Is a certification still a goal, now that AZ-204 is retired?** The options are AZ-104 then
   AZ-400, DP-300 (the SQL Server edge), the new DP-800 SQL AI Developer, or Applied Skills only.
   The answer changes which Learn paths are primary.
3. **One extra paid subscription, or none?** The free stack covers every gap. The candidates, in
   order: Pluralsight (graded labs for security, Angular and pipelines), Frontend Masters (the
   best Angular authorship), Scrimba (React only). Holding any two of them alongside Dometrain
   duplicates a lot.
4. **Brent Ozar classes are sold per class or as a season pass, with recordings available until
   a fixed date.** Is a one-off SQL Server spend acceptable? It is the strongest hands-on SQL
   Server tuning source found.
5. **Does Scrimba still earn its place?** react.dev's own challenges already give hands-on React
   practice for free, and React is notes-level for Investec.
6. **Will you build the security work on Duende IdentityServer (trial licence) or on Entra
   ID?** Dometrain teaches Entra ID configuration; Duende teaches the protocol. Investec's
   choice of provider is unknown.

---

## Sources

All read 2026-09-29.

**Coursera**
- Programmes: <https://www.coursera.org/professional-certificates/microsoft-back-end-developer>, <https://www.coursera.org/professional-certificates/microsoft-full-stack-developer>, <https://www.coursera.org/professional-certificates/microsoft-front-end-developer>, <https://www.coursera.org/professional-certificates/microsoft-aspnet-core-developer>, <https://www.coursera.org/professional-certificates/microsoft-sql-server>, <https://www.coursera.org/professional-certificates/azure-developer-associate>, <https://www.coursera.org/professional-certificates/devops-engineering>, <https://www.coursera.org/professional-certificates/beginners-guide-to-c-sharp-fundamentals>
- Courses, all at `https://www.coursera.org/learn/<slug>`: foundations-of-coding-back-end, introduction-to-programming-with-c-sharp, back-end-development-with-dotnet, database-integration-and-management, security-and-authentication, performance-optimization-and-scalability, msft-data-structures-and-algorithms, deployment-and-devops, full-stack-integration, full-stack-developer-capstone-project, blazor-for-front-end-development, introduction-to-aspdotnet-core-framework, data-management-and-application-features, security-testing-and-development, sql-foundations, data-manipulation-and-transactions-in-sql-server, relational-database-design-and-advanced-querying, indexing-performance-optimization-and-functions-in-microsoft-sql-server, security-maintenance-and-integration-with-bi-tools, az-204-developing-solutions-for-microsoft-azure, devops-platforms-and-source-control, pipeline-engineering-and-automation, cloud-native-and-iac-management, professional-c-development-practices, microsoft-sql-server-performance-tuning-essentials (Starweaver and Luca Berton, not Microsoft)
- Searches: `https://www.coursera.org/search?query=` with asp.net core, entity framework, c#, .net, azure devops, sql server, angular, az-204, oauth, xunit, t-sql, microservices .net, scrimba
- Not usable: `https://api.coursera.org/api/courses.v1?q=search` ("finder 'search' not implemented")

**Microsoft Learn and Microsoft**
- Catalog API: <https://learn.microsoft.com/api/learn/catalog?locale=en-us>
- Learn FAQ (sandboxes): <https://learn.microsoft.com/en-us/training/support/faq>
- Certifications: <https://learn.microsoft.com/en-us/credentials/certifications/azure-developer/>, <https://learn.microsoft.com/en-us/credentials/certifications/devops-engineer/>, <https://learn.microsoft.com/en-us/credentials/certifications/azure-database-administrator-associate/>, <https://learn.microsoft.com/en-us/credentials/certifications/developing-ai-enabled-database-solutions/>, <https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-cloud-developer-associate/>
- Retirement schedule: <https://techcommunity.microsoft.com/blog/skills-hub-blog/the-ai-job-boom-is-here-are-you-ready-to-showcase-your-skills/4494128>
- Applied Skills: <https://learn.microsoft.com/en-us/credentials/applied-skills/implement-security-through-pipeline-using-devops/>, <https://learn.microsoft.com/en-us/credentials/applied-skills/develop-data-driven-applications-by-using-microsoft-azure-sql-database/>
- Paths and modules: <https://learn.microsoft.com/en-us/training/paths/optimize-query-performance-sql-server/>, <https://learn.microsoft.com/en-us/training/paths/monitor-optimize-operational-resources-sql-server/>, <https://learn.microsoft.com/en-us/training/paths/implement-security-through-pipeline-using-devops/>, <https://learn.microsoft.com/en-us/training/paths/az-400-implement-ci-azure-pipelines-github-actions/>, <https://learn.microsoft.com/en-us/training/paths/az-400-implement-secure-continuous-deployment/>, <https://learn.microsoft.com/en-us/training/paths/create-microservices-with-dotnet/>, <https://learn.microsoft.com/en-us/training/modules/evaluate-performance-improvements/>, <https://learn.microsoft.com/en-us/training/modules/configure-pipelines-securely-use-variables-parameters/>, <https://learn.microsoft.com/en-us/training/modules/build-web-api-aspnet-core/>, <https://learn.microsoft.com/en-us/training/modules/microservices-devops-aspnet-core/>, <https://learn.microsoft.com/en-us/training/modules/host-a-web-app-with-azure-app-service/>
- Lab hosts: `https://microsoftlearning.github.io/dp-300-database-administrator/`, `https://microsoftlearning.github.io/implement-security-through-pipeline-using-devops/` (via aka.ms redirect), <https://github.com/MicrosoftLearning/AZ400-DesigningandImplementingMicrosoftDevOpsSolutions> (archived; read via the GitHub API)
- Azure Pipelines docs: <https://learn.microsoft.com/en-us/azure/devops/pipelines/licensing/concurrent-jobs>, <https://learn.microsoft.com/en-us/azure/devops/pipelines/create-first-pipeline>
- SQL docs: <https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide>, <https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store>, <https://learn.microsoft.com/en-us/sql/relational-databases/performance/best-practice-with-the-query-store>, <https://learn.microsoft.com/en-us/sql/relational-databases/performance/execution-plans>, <https://learn.microsoft.com/en-us/sql/relational-databases/performance/intelligent-query-processing>
- ASP.NET Core security docs: <https://learn.microsoft.com/en-us/aspnet/core/security/authentication/identity>, <https://learn.microsoft.com/en-us/aspnet/core/security/authentication/configure-jwt-bearer-authentication>, <https://learn.microsoft.com/en-us/aspnet/core/security/authentication/configure-oidc-web-authentication>, <https://learn.microsoft.com/en-us/aspnet/core/security/authentication/identity-api-authorization>
- Azure DevOps Labs: <https://azuredevopslabs.com/>

**Pluralsight**
- Sitemap: <https://www.pluralsight.com/sitemap.xml>
- Paths: <https://www.pluralsight.com/paths/aspnet-core-10>, <https://www.pluralsight.com/paths/aspnet-core-10-web-api>, <https://www.pluralsight.com/paths/entity-framework-core-10>, <https://www.pluralsight.com/paths/az-400-designing-and-implementing-microsoft-devops-solutions>, <https://www.pluralsight.com/paths/angular-fast-track-for-experienced-developers>, <https://www.pluralsight.com/paths/advanced-performance-and-data-engineering-in-sql-server-2025>, <https://www.pluralsight.com/paths/efficient-performance-tuning-in-sql-server>
- Labs: <https://www.pluralsight.com/labs/codeLabs/guided-securing-an-aspnet-core-10-api-with-oauth2-client-credentials-flow>, <https://www.pluralsight.com/labs/codeLabs/build-reactive-applications-with-signals-in-angular>, <https://www.pluralsight.com/labs/azure/tune-a-slow-data-warehouse-query-in-sql-server>

**Front end**
- angular.dev: <https://angular.dev/tutorials>, <https://angular.dev/tutorials/learn-angular>, <https://angular.dev/playground>, <https://angular.dev/reference/releases>
- react.dev: <https://react.dev/learn>, <https://react.dev/learn/state-a-components-memory>, <https://react.dev/versions>
- Frontend Masters: <https://frontendmasters.com/courses/>, <https://frontendmasters.com/learn/angular/>, <https://frontendmasters.com/learn/react/>, <https://frontendmasters.com/courses/angular-fundamentals/>, <https://frontendmasters.com/courses/intermediate-angular/>, <https://frontendmasters.com/courses/advanced-angular/>, <https://frontendmasters.com/courses/complete-react-v9/>, <https://frontendmasters.com/courses/intermediate-react-v6/>, <https://frontendmasters.com/courses/csharp-dotnet/>, <https://frontendmasters.com/courses/dotnet-apis/>, <https://frontendmasters.com/courses/web-security-v2/>
- Scrimba: <https://scrimba.com/sitemap.xml>, <https://scrimba.com/learn-react-c0e>, <https://scrimba.com/advanced-react-c02h>, <https://scrimba.com/react-challenges-c02n>, <https://scrimba.com/whats-new-in-react-19-c03d>, <https://scrimba.com/learn-typescript-c03c>, <https://scrimba.com/fullstack-path-c0fullstack> (meta tags only; bodies are JS-rendered)

**Other platforms**
- Educative: <https://www.educative.io/sitemaps/general/sitemap.xml>, <https://www.educative.io/courses/developing-applications-with-asp-net-core>, <https://www.educative.io/courses/entity-framework-core-for-data-access-and-relational-mapping>, <https://www.educative.io/courses/learning-angular>
- Exercism: <https://exercism.org/tracks/csharp>
- Codecrafters: <https://backend.codecrafters.io/api/v1/courses?include=language-configurations.language>, <https://backend.codecrafters.io/api/v1/languages>, <https://codecrafters.io/challenges/sqlite>
- LinkedIn Learning: <https://www.linkedin.com/learning/topics/asp-dot-net-core>

**SQL Server specialists**
- Brent Ozar: <https://www.brentozar.com/training/>, <https://www.brentozar.com/classes/fundamentals-of-index-tuning-2026/>, <https://www.brentozar.com/classes/fundamentals-of-query-tuning-2026/>, <https://www.brentozar.com/classes/mastering-index-tuning-2026/>, <https://www.brentozar.com/classes/mastering-query-tuning-2026/>, <https://www.brentozar.com/training/think-like-sql-server-engine/>
- Erik Darling: <https://erikdarling.com/training/> (blog category), <https://erikdarling.com/page-sitemap.xml>, <https://erikdarling.com/sp_quickiestore/>, <https://training.erikdarling.com/> (store; JS-rendered)

**Security**
- Duende: <https://docs.duendesoftware.com/>, <https://docs.duendesoftware.com/identityserver/quickstarts/0-overview/>, <https://docs.duendesoftware.com/bff/>, <https://docs.duendesoftware.com/general/licensing/>, <https://duendesoftware.com/training>, <https://duendesoftware.com/products/communityedition>
- Andrew Lock: <https://andrewlock.net/>

**Unreachable**
- Udemy (`https://www.udemy.com/course/the-complete-guide-to-angular-2/` returned 403). No Udemy course is assessed.
- Erik Darling's course catalogue (JS-rendered store, sitemap 404).
- Microsoft SQL Server downloads page (`https://www.microsoft.com/en-us/sql-server/sql-server-downloads` returned 403), so the Developer edition's terms are unverified.
- Scrimba course bodies (JS-rendered); only meta tags were read.
- The Exercism API (`/api/v2/tracks` returned non-JSON); the track page was used instead.

**Earlier files this extends**
- `research/2026-09-29-dometrain-catalogue.md` (baseline, gap sources marked "carried over")
- `research/2026-09-28-sa-fintech-target-roles.md` (section 8, Investec)
- `research/2026-09-23-full-stack-tooling.md` (house style, Angular and React evidence)
