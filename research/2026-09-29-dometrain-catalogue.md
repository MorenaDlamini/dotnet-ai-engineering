# Dometrain against the target: what it teaches, and what it does not

Primary-source mapping of Dometrain's catalogue against the skill list for the settled target:
**a .NET full-stack software engineer at a South African fintech or bank, with data as the
edge.** The evidence for the target is the three Investec Sandton postings in section 8 of
`2026-09-28-sa-fintech-target-roles.md`. This file tells the `CURRICULUM.md` rebuild which
Dometrain courses carry which skills, and where another primary source has to carry the load.

**The user holds an active Dometrain subscription, so every course listed here is assumed to be
accessible.** This file records no prices or plan details.

**Method.** Read on 2026-09-29. Dometrain's pages are server-rendered Next.js, so nothing needed
a browser. I pulled `dometrain.com/sitemap.xml` and the `/courses/` catalogue page. Both list
the same **171 course URLs**, and I downloaded every one. For each course I took the title,
author, length and level from the page's own `application/ld+json` block (`id="course-schema"`,
fields `name`, `author`, `courseWorkload`, `educationalLevel`). I took the curriculum outline
from the rendered lesson list and searched all 171 outlines for each skill keyword. I then read
the outlines of the courses that matched. **Course pages show no last-updated date or target
.NET version.** The schema's `datePublished` is `"N/A"` on every page. Where an outline names a
version, I quote it. `/learning-paths/` has no fixed paths: its menu entry reads "A personal
path to your goal, built by AI". I checked the gap sources for reachability on the same day.
Anything I infer is marked **Inference** or **Unverified**. I used no third-party reviews.

This file builds on `2026-09-28-sa-fintech-target-roles.md` (the target), `2026-09-23-fraud-and-bank-apis.md`
(Investec sandbox, open banking) and `2026-09-23-full-stack-tooling.md` (the Angular and React
evidence). It does not repeat them.

---

## The verdict

**Dometrain covers the C# and .NET back end in real depth. It is thin on security and data,
and it has nothing on the front end or the fintech domain. Of the 71 skill rows in section 2,
40 are covered, 17 partial and 14 gaps. Leaving out the six fintech-domain rows, it is 40, 16
and 9. 23 of the 40 covered rows are C# and .NET back end.** Five things matter:

1. **The back end is carried well, and most of it is at intermediate level or deeper.** REST
   and Minimal APIs, EF Core (8h32m, including a performance and concurrency chapter), Dapper,
   integration testing with `WebApplicationFactory`, Docker and WireMock, MassTransit with the
   outbox and sagas, background jobs (Hangfire, Quartz, idempotent jobs), caching with Redis (a
   23h37m deep dive), Serilog, OpenTelemetry, BenchmarkDotNet, clean and vertical-slice
   architecture, DDD, microservices and event-driven architecture all have dedicated courses.
2. **There is no Angular course. There is no React course either.** Across 171 courses, the
   word "Angular" appears once, in the Blazor deep dive. React appears as one section of the
   URL-shortener build. Angular is in all three Investec postings and is required in I-3. The
   whole front-end pillar needs angular.dev as its primary source. Dometrain supplies only the
   TypeScript underneath it (Cory House's Deep Dive, 6h54m).
3. **Security is the gap the Investec postings would notice first.** The 12h8m "Getting
   Started: Authentication and Authorization in .NET" course covers cookies, schemes, tickets
   and policy-based authorization. Its outline has **no OAuth2, OIDC, JWT or ASP.NET Core
   Identity**. JWT bearer auth appears only inside the REST APIs course and the URL-shortener
   build. OIDC appears only as Entra ID federation in "Mastering: Azure for Developers". No
   course names OWASP in a developer context, or FAPI. I-1 asks for "OAuth2, OIDC, token
   management" on "financial-grade APIs". That has to come from the specs.
4. **The data edge is Postgres-deep and SQL Server-shallow.** "Getting Started: SQL Server"
   runs 3h5m and stops at joins and views, with no indexes and no query plans. "Hands-On: Learn
   PostgreSQL" runs 17h4m and covers indexes, `EXPLAIN ANALYZE`, scan types, join algorithms,
   window functions and isolation levels. I-2 asks for SQL Server / Azure SQL "data modelling and
   performance optimisation". The concepts transfer from the Postgres course, but the SQL Server
   specifics (execution plans, Query Store, index design) have to come from Microsoft Learn.
   There is no data-engineering content at all: no Spark, Databricks, ADF or ETL.
5. **Platform coverage is Azure-first, but it misses the Investec pipeline tool.** App
   Service, Functions, API Management, Key Vault, Managed Identity, Container Apps and Bicep are
   taught. Kubernetes and Aspire have their own courses. **No course teaches Azure DevOps
   Pipelines**, which I-2 requires. Every CI/CD lesson on the site is GitHub Actions. Terraform
   appears only as the IaC tool inside two build courses.

Fintech domain (ledgers, double-entry, reconciliation, payments, open banking, POPIA):
**confirmed nothing.** No outline in the 171 contains "ledger", "reconciliation", "payment",
"open banking", "POPIA" or "PCI". The nearest are the idempotency lessons (REST APIs, event-driven
architecture, background processing, microservices) and event sourcing.

---

## 1. Catalogue snapshot

The 171 courses include C, C++, Go, Java, PHP, Rust, Swift, F#, .NET MAUI, AWS and GCP system
design, and QA interview banks. None of those are relevant here and they are left out. Level is
Dometrain's own series label (`educationalLevel`), not a difficulty grade. The series are Getting
Started, From Zero to Hero (ZTH), Deep Dive, Mastering, Hands-On, Let's Build It, Design
Patterns in C#, Exam Prep and Career. All URLs are `https://dometrain.com/course/<slug>/`.

### C# language and runtime

| Title | Author | Length | Level | What it covers (from the outline) | Slug |
|---|---|---|---|---|---|
| Deep Dive: C# | Nick Cosentino | 6h28m | Deep Dive | Value vs reference types, records, generics, delegates, LINQ, `Lazy`, events, threads, Task, async/await, cancellation | `deep-dive-csharp` |
| Mastering: C# | Sergey Teplyakov | 3h25m | Mastering | Multi-targeting, TFM vs language version, struct defensive copies, records under the hood, union types, argument validation, "extension everything", closure allocations; lessons on ".NET 10 Delegate De-Abstraction" and "LINQ Performance Improvements in .NET 10" | `mastering-csharp` |
| ZTH: Asynchronous Programming in C# | Brandon Minnick | 3h53m | ZTH | Compiler-generated state machine, async void, `ConfigureAwait`, `IAsyncEnumerable`, `ValueTask`, ExecutionContext, SynchronizationContext | `from-zero-to-hero-asynchronous-programming-in-csharp` |
| ZTH: Parallel Programming in C# | Brandon Minnick | 3h56m | ZTH | Parallel and threading (outline not read in detail) | `from-zero-to-hero-parallel-programming-in-csharp` |
| Hands-On: LINQ in C# | Nick Chapsas | 9h50m | Hands-On | LINQ exercises | `hands-on-linq-in-csharp` |
| ZTH: LINQ in .NET | Hannes Lowette | 4h9m | ZTH | LINQ | `from-zero-to-hero-linq-in-dotnet` |
| ZTH: Working with Null in C# | Ed Charbeneau | 4h38m | ZTH | Nullable reference types | `from-zero-to-hero-working-with-null-in-csharp` |
| ZTH: Garbage Collection in .NET | Salih Cantekin | 3h51m | ZTH | Generations, LOH, escape analysis, "Going Allocation Free", server vs workstation GC, DATAS, No GC Region | `from-zero-to-hero-garbage-collection-in-dotnet` |
| ZTH: 1 Billion Row Performance Challenge in .NET | Salih Cantekin | 8h15m | ZTH | Profiling, streams, multi-threading, memory-mapped files, pointers, custom parsers, SIMD | `from-zero-to-hero-1-billion-row-performance-challenge-in-dotnet` |
| ZTH: Benchmarking code in .NET | Mel Grubb | 7h10m | ZTH | BenchmarkDotNet end to end: MemoryDiagnoser, threading diagnosers, Native AOT, detecting regressions | `from-zero-to-hero-benchmarking-code-in-dotnet` |
| ZTH: Source Generators in C# | Mel Grubb | 4h12m | ZTH | Source generators | `from-zero-to-hero-source-generators-in-csharp` |
| ZTH: Reflection in .NET | Nick Cosentino | 5h19m | ZTH | Reflection | `from-zero-to-hero-reflection-in-dotnet` |
| ZTH: Dependency Injection in .NET with C# | Nick Chapsas | 4h41m | ZTH | Lifetimes, resolving in every host type, open generics, `TryAdd`, decorators, captive dependencies | `from-zero-to-hero-dependency-injection-in-dotnet-with-csharp` |
| ZTH: Configuration and Options in .NET | David Pine | 3h27m | ZTH | Providers, user secrets, Azure Key Vault and App Configuration providers, custom provider | `from-zero-to-hero-configuration-and-options-in-dotnet` |
| ZTH: Logging in .NET | Nick Chapsas | 2h56m | ZTH | Structured logging, scopes, **Serilog** (sinks, enrichment, masking sensitive logs), `LoggerMessage` source generator, App Insights alerts | `from-zero-to-hero-logging-in-dotnet` |

### Web APIs, data access, testing

| Title | Author | Length | Level | What it covers | Slug |
|---|---|---|---|---|---|
| Getting Started: ASP.NET Core | Steve Smith | 7h28m | Getting Started | Middleware, routing, Minimal APIs, OpenAPI, EF Core, Razor Pages and MVC, Aspire support, integration testing, `Directory.Packages.props` | `getting-started-asp-dotnet-core` |
| ZTH: REST APIs in .NET | Nick Chapsas | 4h41m | ZTH | REST constraints, **idempotency**, validation, **JWT auth**, filtering, pagination, HATEOAS, **basic and advanced versioning**, health checks, response and output caching, API-key auth, Refit SDK, migrating to Minimal APIs | `from-zero-to-hero-rest-apis-in-asp-net-core` |
| ZTH: Minimal APIs in .NET with C# | Nick Chapsas | 3h33m | ZTH | Binding, results, CORS, structuring, testing with `WebApplicationFactory` | `from-zero-to-hero-minimal-apis-in-dotnet-with-csharp` |
| Getting Started: GraphQL in .NET | Michael Staib | 7h28m | Getting Started | GraphQL (Hot Chocolate's author) | `getting-started-graphql-in-dotnet` |
| ZTH: gRPC in .NET | Irina Scurtu | 3h24m | ZTH | gRPC | `from-zero-to-hero-grpc-in-dotnet` |
| Migrating: ASP.NET Web APIs to ASP.NET Core | Jonathan Tower | 4h55m | Migrating | Framework-to-Core migration; I-3 lists ".NET Framework, Core, 6+" | `migrating-asp-net-web-apis-to-asp-net-core` |
| ZTH: Entity Framework Core in .NET | Hannes Lowette | 8h32m | ZTH | Modelling, migrations, testing, multi-tenancy, raw SQL, ChangeTracker, **"Slow Queries & DB indices"**, compiled queries, batching, concurrency, scaffolding, **Cosmos DB provider** | `from-zero-to-hero-entity-framework-core-in-dotnet` |
| ZTH: Dapper in .NET | Nick Proud | 3h22m | ZTH | Queries, stored procedures, multi-mapping, bulk ops (Dapper Plus), SQL injection, transactions | `from-zero-to-hero-dapper-in-dotnet` |
| ZTH: Unit testing for C# Developers | Nick Chapsas | 3h39m | ZTH | xUnit, fixtures, Moq vs NSubstitute, coverage | `from-zero-to-hero-unit-testing-for-csharp-developers` |
| ZTH: Testing with xUnit in C# | Gui Ferreira | 6h0m | ZTH | xUnit in depth | `from-zero-to-hero-testing-with-xunit-in-csharp` |
| ZTH: Integration testing in ASP.NET Core | Nick Chapsas | 4h15m | ZTH | `WebApplicationFactory`, "Creating a test container for our database", WireMock, auth and background services in tests, **Playwright** UI tests | `from-zero-to-hero-integration-testing-in-asp-net-core` |
| ZTH: Test-Driven Development in C# | Gui Ferreira | 5h41m | ZTH | TDD | `from-zero-to-hero-test-driven-development-tdd-csharp` |
| ZTH: Writing Testable Code in C# | Gui Ferreira | 4h28m | ZTH | Testability | `from-zero-to-hero-writing-testable-code-in-csharp` |

### Architecture, patterns, distributed systems

| Title | Author | Length | Level | What it covers | Slug |
|---|---|---|---|---|---|
| Getting Started / Deep Dive: Clean Architecture in .NET | Amichai Mantinband | 3h10m / 3h51m | GS / DD | Layers, MediatR pipeline behaviours, domain events, eventual consistency, subcutaneous and integration testing, auth | `getting-started-clean-architecture-in-dotnet`, `deep-dive-clean-architecture-in-dotnet` |
| ZTH: Vertical Slice Architecture | Kevin Dockx | 6h4m | ZTH | Feature folders, REPR, MediatR, Problem Details RFC, CQRS, domain events | `from-zero-to-hero-vertical-slice-architecture` |
| Getting Started / Deep Dive: Domain-Driven Design | Amichai Mantinband | 5h12m / 5h41m | GS / DD | Tactical patterns, aggregates, Result pattern; Event Storming, bounded contexts, context mapping | `getting-started-domain-driven-design-ddd`, `deep-dive-domain-driven-design-ddd` |
| Hands-On: Creational / Structural / Behavioral Design Patterns in C# | Nick Chapsas | 4h45m / 4h5m / 7h35m | Hands-On | GoF patterns as exercises | `hands-on-hands-on-creational-design-patterns-in-csharp`, `hands-on-structural-design-patterns-in-csharp`, `hands-on-behavioral-design-patterns-in-csharp` |
| Design Patterns in C#: (23 single-pattern courses) | Amichai Mantinband | 0h28m–1h16m each | Design Patterns | One GoF pattern each | `design-patterns-in-csharp-<pattern>` |
| Getting Started / Deep Dive: Modular Monoliths in .NET | Steve Smith | 3h11m / 4h21m | GS / DD | Modules, boundaries, "Implementing a Simple Outbox with MongoDB" | `getting-started-modular-monoliths-in-dotnet`, `deep-dive-modular-monoliths-in-dotnet` |
| Getting Started / Deep Dive: Microservices Architecture | James Eastham | 5h21m / 4h18m | GS / DD | Contract testing, gRPC, Consul discovery, CloudEvents, **implementing idempotency**, strangler fig | `getting-started-microservices-architecture`, `deep-dive-microservices-architecture` |
| ZTH: Event-Driven Architecture | James Eastham | 5h33m | ZTH | Outbox, "Idempotency - done better", event versioning, orchestration vs choreography, sagas, messaging semantic conventions, testing for idempotency | `from-zero-to-hero-event-driven-architecture` |
| Getting Started / Deep Dive: Event Sourcing in .NET | Hannes Lowette | 4h1m / 4h45m | GS / DD | Event sourcing, projections, sagas | `getting-started-event-sourcing-in-dotnet`, `deep-dive-event-sourcing-in-dotnet` |
| Getting Started: Messaging in .NET with MassTransit | Irina Scurtu | 5h7m | Getting Started | RabbitMQ, consumers, request/response, error and fault queues, retry and redelivery, filters, **bus and consumer outbox**, **saga state machines** | `getting-started-messaging-in-net-with-masstransit` |
| Getting Started: Messaging in .NET with NServiceBus | Irina Scurtu | 5h10m | Getting Started | NServiceBus, outbox, sagas | `getting-started-messaging-in-dotnet-with-nservicebus` |
| ZTH: Background Processing in .NET | Nick Proud | 5h34m | ZTH | Hosted and worker services, job queue, Hangfire, Quartz, TickerQ, **idempotent jobs**, retries and poison jobs, RabbitMQ, Kafka | `from-zero-to-hero-background-processing-in-dotnet` |
| Getting Started: Caching in .NET | Jody Donetti | 7h11m | Getting Started | MemoryCache, HybridCache, FusionCache, stampede, fail-safe, eager refresh | `getting-started-caching-in-dotnet` |
| Deep Dive: Caching in .NET | Jody Donetti | 23h37m | Deep Dive | **Redis** and RESP, `IDistributedCache`, L1+L2, backplanes, distributed locks, tagging, HTTP caching and ETags, cache security, OTel | `deep-dive-caching-in-dotnet` |
| ZTH: OpenTelemetry in .NET | Gui Ferreira | 4h22m | ZTH | Traces, metrics, logs, Collector, Jaeger, Prometheus, Grafana, Loki, baggage, tail sampling | `from-zero-to-hero-open-telemetry-in-net` |
| Getting Started / Deep Dive: Solution Architecture | James Eastham | 4h47m / 4h35m | GS / DD | Architecture practice, idempotency, outbox | `getting-started-solution-architecture`, `deep-dive-solution-architecture` |
| ZTH: From Microservices to Modular Monoliths | Steve Smith | 2h26m | ZTH | Consolidating services | `from-zero-to-hero-microservices-to-modular-monoliths` |
| Hands-On: System Design for Beginners / Intermediate Engineers / Advanced | Nick Chapsas | 4h10m / 6h54m / 13h27m | Hands-On | Scaling, rate limiting, bulkheads, sharding, replica lag; then consensus, sagas, CDC, circuit breakers, timeout budgets, failover, zero trust, data residency, exactly-once streams | `hands-on-system-design-for-beginners`, `hands-on-system-design-for-intermediate-engineers`, `hands-on-advanced-system-design` |
| Hands-On: System Design for Azure | Nick Chapsas | 6h21m | Hands-On | App Service, APIM, Front Door, WAF, Azure SQL, Redis, Cosmos DB, Service Bus, Event Grid and Hubs, Key Vault, Entra External ID, multi-region | `hands-on-system-design-for-azure` |
| Let's Build It: URL Shortener in .NET | Gui Ferreira | 16h47m | Let's Build It | GitHub Actions, **Bicep**, Key Vault, **Cosmos DB**, Postgres, **Polly retry policy**, **Entra ID JWT auth**, Azure Redis, Azure Functions, **React** with MSAL.js | `lets-build-it-url-shortener-in-dotnet` |

### Security, front end, platform, data, AI

| Title | Author | Length | Level | What it covers | Slug |
|---|---|---|---|---|---|
| Getting Started: Authentication and Authorization in .NET | Tore Nestenius | 12h8m | Getting Started | ClaimsPrincipal, auth middleware operations, schemes, tickets, data protection, cookie handler and lifetimes, role, policy and resource-based authorization, "Broken Access Control" | `getting-started-authentication-and-authorization-in-dotnet` |
| ZTH: Authentication & Authorization in Blazor | Jimmy Engström | 4h21m | ZTH | Claims, policies, Auth0, Entra ID | `from-zero-to-hero-authentication-authorization-in-blazor` |
| Getting Started: TypeScript | Cory House | 3h30m | Getting Started | TypeScript basics | `getting-started-typescript` |
| Deep Dive: TypeScript | Cory House | 6h54m | Deep Dive | Every narrowing technique, discriminated unions, `satisfies`, typing `this`, generics | `deep-dive-typescript` |
| Hands-On: Learn TypeScript | Nick Chapsas | 24h49m | Hands-On | TypeScript exercises | `hands-on-learn-typescript` |
| Let's Build It: Multi-Tenant SaaS App in TypeScript | James Charlesworth | 8h36m | Let's Build It | A TypeScript app with Playwright | `lets-build-it-multi-tenant-saas-app-in-typescript` |
| Getting Started / Deep Dive: Blazor | Jimmy Engström | 7h4m / 6h15m | GS / DD | Blazor | `getting-started-blazor`, `deep-dive-blazor` |
| ZTH: Docker for Developers | Dan Clarke | 3h26m | ZTH | Images, Compose, volumes, networking, non-root, scanning | `from-zero-to-hero-docker-for-developers` |
| ZTH: Kubernetes for Developers | Dan Clarke | 5h46m | ZTH | Deployments, probes, Services, Ingress, ConfigMaps and Secrets, Helm, Kustomize, RBAC, network policies, HPA, OTel stack, managed K8s | `from-zero-to-hero-kubernetes-for-developers` |
| Getting Started: Aspire | Dan Clarke | 5h11m | Getting Started | AppHost, integrations, service discovery, OTel dashboard, testing, deploy to Compose, K8s, App Service and Container Apps; has a "Course update" lesson | `getting-started-dotnet-aspire` |
| Getting Started: Azure for Developers | Kevin Dockx | 4h25m | Getting Started | App Service, Storage, **Azure SQL**, Managed Identity, `DefaultAzureCredential`, App Insights, KQL, Azure Monitor | `getting-started-azure-for-developers` |
| Deep Dive: Azure for Developers | Kevin Dockx | 5h24m | Deep Dive | **Functions** and Durable Functions, Logic Apps, **API Management** (products, policies, securing downstream), Event Grid vs Service Bus | `deep-dive-azure-for-developers` |
| Mastering: Azure for Developers | Kevin Dockx | 12h10m | Mastering | Entra ID app registrations, MSAL and Microsoft.Identity.Web, on-behalf-of, token lifetime, **APIM token delegation**, Managed Identities, External ID, **"Federating with an OpenID Connect Identity Provider"**, **Key Vault** (rotation, signing), ARM, **Bicep** | `mastering-azure-for-developers` |
| ZTH: Serverless with Azure Functions | Mohamad Lawand | 6h19m | ZTH | Functions, **Service Bus**, Terraform, GitHub Actions, dead-lettering, slots | `from-zero-to-hero-serverless-with-azure-functions` |
| ZTH: Deploying .NET Applications to Azure | Mohamad Lawand | 2h16m | ZTH | **Terraform**, ACR, **Container Apps**, Azure SQL, GitHub Actions, DB migrations in the pipeline | `from-zero-to-hero-deploying-dotnet-apps-to-azure` |
| Getting Started: Bicep for Azure | Simon Wåhlin | 4h13m | Getting Started | Bicep syntax, what-if, custom types, modules, lambdas, RBAC, deployment scripts | `getting-started-bicep-for-azure` |
| ZTH: Cloud Architecture in Azure | Kevin Dockx | 5h6m | ZTH | Well-Architected Framework, cloud design patterns (retry, circuit breaker, CQRS, BFF, strangler fig), ADRs | `from-zero-to-hero-cloud-architecture-in-azure` |
| ZTH: GitHub Actions | Scott Sauber | 5h43m | ZTH | PR verify and CI workflows, environments, reusable workflows, zero-downtime deploy, approvals | `from-zero-to-hero-github-actions` |
| ZTH: Git / Hands-On: Learn Git From Scratch | Scott Sauber / Nick Chapsas | 3h24m / 6h55m | ZTH / Hands-On | Git | `from-zero-to-hero-git`, `hands-on-learn-git-from-scratch` |
| Getting Started: SQL Server | Alex Tushinsky | 3h5m | Getting Started | SSMS, types, normalisation, DML, variables, CASE, functions, procs, try/catch and transactions, joins, views | `getting-started-sql-server` |
| Hands-On: Learn PostgreSQL | Nick Chapsas | 17h4m | Hands-On | Joins, CTEs, recursive CTEs, JSONB, constraints, **index types, EXPLAIN ANALYZE, scan types, join algorithms**, window functions, materialized views, isolation levels, lateral joins | `hands-on-learn-postgresql` |
| Hands-On: Learn SQLite | Nick Chapsas | 15h35m | Hands-On | SQLite, including query plans | `hands-on-learn-sqlite` |
| Getting Started: AI for .NET Developers | Ed Charbeneau | 5h12m | Getting Started | Azure AI Foundry, prompt patterns, tokenisation, Microsoft.Extensions.AI, RAG | `getting-started-ai-for-dotnet-developers` |
| ZTH: Microsoft.Extensions.AI in .NET | Brandon Minnick | 3h34m | ZTH | `IChatClient`, tools, **unit testing and evaluating LLMs**, embeddings, vector store, Foundry, Bedrock | `from-zero-to-hero-microsoft-extensions-ai-in-dotnet` |
| Getting Started: Microsoft Agent Framework in .NET | Nico Vermeir | 5h48m | Getting Started | Agents, tools, human in the loop, workflows, OTel tracing, token cost, **prompt-injection defence** | `getting-started-microsoft-agent-framework-in-dotnet` |
| Getting Started: AI Agents in C# | James Charlesworth | 5h41m | Getting Started | LLM basics to agents in C# | `getting-started-ai-agents-in-csharp` |
| Let's Build It: AI Chatbot with RAG in .NET | James Charlesworth | 4h25m | Let's Build It | Embeddings, vector search, Pinecone | `lets-build-it-ai-chatbot-with-rag-in-dotnet-using-your-data` |
| Getting Started: Model Context Protocol | James Charlesworth | 6h11m | Getting Started | MCP | `getting-started-model-context-protocol-mcp` |
| Getting Started / Deep Dive: Claude Code; ZTH: Working with GitHub Copilot; GS / DD: Boosting Developer Productivity with AI | Gui Ferreira; Kevin Dockx | 4h42m / 6h59m; 5h59m; 2h49m / 4h56m | various | AI coding assistants | `getting-started-claude-code`, `deep-dive-claude-code`, `from-zero-to-hero-working-with-github-copilot`, `getting-started-boosting-developer-productivity-with-ai`, `deep-dive-boosting-developer-productivity-with-ai` |
| Getting Started: C# Interview Questions; Career: Nailing the Behavioral Interview | Nick Chapsas; Nick Cosentino, Ryan Murphy | 1h38m; 6h2m | GS; Career | Interview prep | `getting-started-csharp-interview-questions`, `career-nailing-the-behavioral-interview` |

Version currency. Outlines give only these hints: Mastering C# names .NET 10. Hands-On C# for
Beginners has a "C# 13 and C# 14 Features" lesson. The DI course still has "The Startup.cs and
changes after .NET 6". Aspire has a "Course update" lesson and uses the Aspire CLI.
**Unverified:** the other courses may target older .NET versions. Check each course's first
lesson before relying on API details.

---

## 2. Skill → course mapping

**covered** means a dedicated course or a chapter of real depth. **partial** means lessons
inside another course, or the concept without the specific tool the posting names. **gap**
means nothing found in 171 outlines.

### Deepest: C# and .NET

| Skill | Rating | Dometrain courses | Note |
|---|---|---|---|
| Async | covered | ZTH Asynchronous Programming; Deep Dive C# (async section); ZTH Parallel Programming | Internals section (ExecutionContext, SynchronizationContext) is the useful part at five years |
| LINQ | covered | Hands-On LINQ; ZTH LINQ; Mastering C# (.NET 10 LINQ perf) | |
| Generics | partial | Deep Dive C# (one "Generics" lesson); DI course (open generics) | No dedicated variance or constraint depth. Microsoft Learn C# guide |
| Memory / `Span<T>` | partial | GC course ("Going Allocation Free", LOH); 1BRC (pointers, SIMD, memory-mapped files); Mastering C# (struct copies) | **No outline names `Span<T>`, `Memory<T>`, `stackalloc` or `ArrayPool`.** Microsoft Learn "Memory and spans" |
| Records | covered | Mastering C# ("Mastering Records", record structs); Deep Dive C# | |
| Dependency injection | covered | ZTH Dependency Injection | |
| ASP.NET Core Web APIs | covered | ZTH REST APIs; Getting Started ASP.NET Core; Migrating Web APIs | |
| Minimal APIs | covered | ZTH Minimal APIs; REST APIs (migration section) | |
| EF Core | covered | ZTH EF Core (8h32m) | |
| Dapper | covered | ZTH Dapper | |
| xUnit | covered | ZTH Testing with xUnit; ZTH Unit testing | |
| NUnit | gap | none | I-3 names NUnit and xUnit; the concepts transfer. NUnit docs |
| Integration testing (`WebApplicationFactory`) | covered | ZTH Integration testing; Minimal APIs (testing section) | |
| Testcontainers | partial | ZTH Integration testing ("Creating a test container for our database", with docker-compose) | **Unverified** whether it uses the Testcontainers library. Testcontainers for .NET docs |
| Mocking | covered | ZTH Unit testing ("Moq vs NSubstitute"); Integration testing (WireMock) | |
| Clean architecture | covered | GS and DD Clean Architecture | |
| Vertical slice | covered | ZTH Vertical Slice Architecture | |
| Design patterns | covered | Hands-On Creational, Structural, Behavioral; 23 single-pattern courses | |
| DDD | covered | GS and DD Domain-Driven Design | |
| Microservices | covered | GS and DD Microservices; Microservices to Modular Monoliths | |
| MassTransit / RabbitMQ | covered | GS Messaging with MassTransit | |
| Azure Service Bus | partial | Serverless with Azure Functions; Deep Dive Azure (comparison lesson); System Design for Azure | No MassTransit-on-Service-Bus lesson. Microsoft Learn Service Bus docs |
| Resilience (Polly) | partial | URL Shortener ("Adding a retry policy with Polly"); MassTransit retry; Cloud Architecture (retry and circuit breaker patterns); Advanced System Design | **No dedicated Polly or `Microsoft.Extensions.Resilience` course.** Microsoft Learn ".NET resilience" |
| Background jobs | covered | ZTH Background Processing | |
| Caching (Redis) | covered | GS and DD Caching; System Design for Azure (Azure Cache for Redis) | |
| OpenTelemetry | covered | ZTH OpenTelemetry; Aspire; Kubernetes (OTel stack) | |
| Logging (Serilog) | covered | ZTH Logging | |
| Performance / benchmarking | covered | ZTH Benchmarking; 1BRC; GC | |
| API design and versioning | covered | ZTH REST APIs (basic and advanced versioning, HATEOAS, Swagger) | |
| Idempotency | partial | REST APIs ("Understanding Idempotency"); EDA ("Idempotency - done better", testing for it); Microservices DD; Background Processing | Taught for consumers and jobs. **No outline shows an `Idempotency-Key` API endpoint implemented.** See section 3 |

### Security

| Skill | Rating | Dometrain courses | Note |
|---|---|---|---|
| OAuth2 / OIDC | partial | Mastering Azure (Entra ID, MSAL, on-behalf-of, OIDC federation); URL Shortener (Entra ID); Blazor auth (Auth0, Entra ID) | Taught as Entra ID configuration, not as the protocol. **No grant-type, PKCE or FAPI content.** |
| JWT | partial | REST APIs ("What is the JSON Web Token?", token service); URL Shortener | |
| Token handling | partial | REST APIs SDK ("Handling token generation and refreshing"); Mastering Azure (token lifetime, `ITokenAcquisition`, APIM delegation) | |
| ASP.NET Core Identity | gap | none | Auth course is the pipeline underneath it (cookies, schemes, data protection). Microsoft Learn Identity docs |
| Secrets | covered | Config and Options (user secrets, Key Vault provider); Mastering Azure (Key Vault rotation); URL Shortener | |
| OWASP | partial | Auth course ("Broken Access Control"); Dapper (SQL injection); Deep Dive Caching (cache security) | No OWASP-framed course. OWASP ASVS and API Security Top 10 |

### Front end

| Skill | Rating | Dometrain courses | Note |
|---|---|---|---|
| **Angular** | **gap** | none | angular.dev |
| TypeScript | covered | GS TypeScript; Deep Dive TypeScript; Hands-On Learn TypeScript | |
| React | gap (one section) | URL Shortener's "Building the Client Web Application" section only | react.dev |
| Blazor (note only) | covered | GS and DD Blazor; Blazor auth | Named in no Investec posting |
| Front-end testing (Jasmine/Karma/Jest, Playwright) | partial | Integration testing (Playwright section); Multi-Tenant SaaS in TS (Playwright) | Angular testing guide on angular.dev |

### Platform

| Skill | Rating | Dometrain courses | Note |
|---|---|---|---|
| Docker | covered | ZTH Docker; ZTH Docker Compose | |
| Kubernetes | covered | ZTH Kubernetes for Developers | AKS specifics: Microsoft Learn |
| Azure App Service | covered | GS Azure for Developers; GitHub Actions | |
| Azure Functions | covered | Deep Dive Azure; ZTH Serverless with Azure Functions | |
| Container Apps / AKS | partial | Deploying .NET Apps to Azure (Container Apps via Terraform); Aspire (deploy to Container Apps) | No AKS course |
| API Management | covered | Deep Dive Azure (APIM section); Mastering Azure (token delegation in APIM) | I-1 names Apigee or Azure API Management |
| Azure SQL | partial | GS Azure for Developers (Azure SQL with Managed Identity); Deploying .NET Apps | Provisioning and connecting, not tuning |
| Key Vault | covered | Mastering Azure; Config and Options | |
| **Azure DevOps Pipelines** | **gap** | none | Every CI/CD lesson is GitHub Actions. Microsoft Learn Azure Pipelines |
| GitHub Actions | covered | ZTH GitHub Actions; URL Shortener; Deploying to Azure | |
| Bicep | covered | GS Bicep for Azure; Mastering Azure; URL Shortener | |
| Terraform | partial | Deploying .NET Apps to Azure; Serverless with Azure Functions | Inside builds only. HashiCorp Azure tutorials |
| .NET Aspire | covered | GS Aspire | |

### Data edge

| Skill | Rating | Dometrain courses | Note |
|---|---|---|---|
| SQL Server / T-SQL basics | covered | GS SQL Server | Beginner-level |
| **SQL Server indexing, query plans, performance** | **gap** | EF Core's "Slow Queries & DB indices" lesson is the only SQL Server-adjacent perf content | This is I-2's named ask. Microsoft Learn index design guide, Query Store, execution plans |
| Data modelling | partial | GS SQL Server (normalisation, diagrams); EF Core (modelling); Postgres (constraints, table design); DDD (aggregates) | No dimensional or warehouse modelling |
| Postgres | covered | Hands-On Learn PostgreSQL (17h4m) | Deepest data course on the site |
| Cosmos DB | partial | EF Core (Cosmos provider section); URL Shortener (Cosmos with Bicep, change-feed trigger, continuation tokens); System Design for Azure | Partitioning and RU modelling: Microsoft Learn |
| MongoDB | gap (one lesson) | Deep Dive Modular Monoliths ("Implementing a Simple Outbox with MongoDB") | MongoDB docs |
| Data engineering (ETL, Spark, Databricks, ADF) | gap | none | As before: Databricks Academy, Microsoft Learn ADF, DP-750 course |

### Also

| Skill | Rating | Dometrain courses | Note |
|---|---|---|---|
| Git | covered | ZTH Git; Hands-On Learn Git From Scratch | |
| System design | covered | Hands-On System Design Beginners, Intermediate, Advanced, Azure; Cloud Architecture in Azure | |
| AI tooling for .NET developers | covered | GS AI for .NET Developers; ZTH Microsoft.Extensions.AI; GS Microsoft Agent Framework; Claude Code; Copilot | I-1 asks for "responsible" AI tooling |
| Semantic Kernel | gap | none; the Agent Framework course is the nearest | **Unverified:** whether Microsoft now points new work to Agent Framework over Semantic Kernel. Check Microsoft Learn before choosing |

### Fintech domain

| Skill | Rating | Dometrain courses | Note |
|---|---|---|---|
| Ledgers, double-entry | gap | none (Event Sourcing is the nearest mechanism) | |
| Reconciliation | gap | none | |
| Idempotency for payments | partial | see Idempotency above | |
| Payments | gap | none | |
| Open banking | gap | none | |
| POPIA | gap | none | |

---

## 3. Gaps, and the primary source that fills each

All links below were checked and returned HTTP 200 on 2026-09-29.

| Gap | Primary source | Why this one |
|---|---|---|
| **Angular** (primary front end) | angular.dev: [tutorials](https://angular.dev/tutorials), [testing guide](https://angular.dev/guide/testing), [releases](https://angular.dev/reference/releases) | The owning docs. The releases page listed v22.x as current when read. I-2 says "Angular (v8+)" and I-3 "Angular 2+", so any current major meets the ask |
| React (second) | [react.dev/learn](https://react.dev/learn) | Already the Phase 3 source in `CURRICULUM.md` |
| OAuth2 and OIDC as protocols | [RFC 9700, Best Current Practice for OAuth 2.0 Security](https://www.rfc-editor.org/rfc/rfc9700) (BCP 240, updates 6749, 6750, 6819); [ASP.NET Core OIDC web authentication](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/configure-oidc-web-authentication) | Dometrain teaches Entra ID configuration. The posting asks for the protocol |
| "Financial-grade APIs" (I-1) | OpenID Foundation [FAPI 2.0 Security Profile](https://openid.net/specs/fapi-security-profile-2_0-final.html), [FAPI working group](https://openid.net/wg/fapi/) | I-1's exact phrase is the name of this spec family |
| UK Open Banking (I-1) | [standards.openbanking.org.uk](https://standards.openbanking.org.uk/) | I-1 says the APIs "power Investec's UK Open Banking ecosystem" |
| Investec's own API surface | [developer.investec.com](https://developer.investec.com/) | The portal lists "Third Parties: Connect your third party service to Investec via 3-legged OAuth", and a "Medical: Simplifying claim reconciliation" solution. That is OAuth and reconciliation, on the target employer's own page |
| ASP.NET Core Identity | [Microsoft Learn: Identity](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/identity) | |
| OWASP | [ASVS](https://owasp.org/www-project-application-security-verification-standard/), [API Security Top 10](https://owasp.org/API-Security/) | The API Top 10 fits an API-heavy role better than the web Top 10 |
| Resilience (Polly) | [Microsoft Learn: Introduction to resilient app development](https://learn.microsoft.com/en-us/dotnet/core/resilience/) | Microsoft's resilience pipeline is built on Polly |
| `Span<T>` / `Memory<T>` | [Microsoft Learn: Memory and spans](https://learn.microsoft.com/en-us/dotnet/standard/memory-and-spans/) | |
| Testcontainers | [dotnet.testcontainers.org](https://dotnet.testcontainers.org/); [ASP.NET Core integration tests](https://learn.microsoft.com/en-us/aspnet/core/test/integration-tests) | |
| NUnit | nunit.org docs (not checked) | Small gap. The xUnit concepts carry over |
| API versioning library | [dotnet/aspnet-api-versioning](https://github.com/dotnet/aspnet-api-versioning) | The REST APIs course covers the concept |
| Idempotency keys on write APIs | [IETF draft-ietf-httpapi-idempotency-key-header](https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/) (datatracker shows -07, **expired**); [Stripe idempotent requests](https://docs.stripe.com/api/idempotent_requests) as the canonical industry implementation | The draft is the closest thing to a standard, and it is not one. Say so when citing it |
| **SQL Server performance** (I-2) | Microsoft Learn: [index design guide](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide), [Query Store](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store) | The biggest data gap for the target. The Dometrain Postgres course teaches the same concepts on another engine |
| Cosmos DB modelling | [Microsoft Learn: Cosmos DB](https://learn.microsoft.com/en-us/azure/cosmos-db/) | I-1 lists Cosmos DB/MongoDB as advantageous |
| **Azure DevOps Pipelines** (I-2) | [Microsoft Learn: Azure Pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/) | Named as required in I-2 and helpful in I-3 |
| Container Apps, AKS, APIM specifics | Microsoft Learn: [Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/), [AKS](https://learn.microsoft.com/en-us/azure/aks/), [API Management](https://learn.microsoft.com/en-us/azure/api-management/) | |
| Terraform on Azure | [HashiCorp: Azure get-started](https://developer.hashicorp.com/terraform/tutorials/azure-get-started) | |
| Data engineering | [Microsoft Learn: Azure Data Factory](https://learn.microsoft.com/en-us/azure/data-factory/); [DP-750 course](https://learn.microsoft.com/en-us/training/courses/dp-750t00); [Databricks training](https://www.databricks.com/learn/training/home) | Unchanged from `2026-09-23-data-stack-and-certifications.md`. No Investec posting asks for this, so it is the edge, not the baseline |
| Semantic Kernel | [Microsoft Learn: Introduction to Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/overview/) | Read before deciding between SK and Agent Framework |
| POPIA | [Information Regulator: POPIA](https://inforegulator.org.za/popia/) | The regulator's own page |
| Card data (PCI DSS) | [pcisecuritystandards.org](https://www.pcisecuritystandards.org/) | Named in 6 of 45 postings in the fintech file, and in none of Investec's |
| Ledgers, double-entry, reconciliation | **No single owning standard exists.** **Inference:** the best primary material is the Investec portal's reconciliation use case plus the reconciliation language in the posting bodies already quoted in `2026-09-28-sa-fintech-target-roles.md` | The fintech file found "ledger" in zero engineering bodies. Treat it as build material, not a reading gap |

---

## 4. Suggested reading order

The phases below are placeholders shaped like the target. They are not the rebuilt curriculum's
phases. **Inference throughout:** the skip, skim and watch calls assume five years of
production C# and ASP.NET Core. They are guesses about what that experience already covers, and
open question 1 asks the user to correct them. The rule in `CURRICULUM.md` still applies: one
course open at a time, tied to the module being built.

**A. Tooling baseline**
- Skim: ZTH Git; GS Claude Code (then DD Claude Code if it is the daily assistant).
- Skip: Hands-On Learn Git From Scratch.

**B. C# and .NET depth**
- Watch: **Mastering C#** (the most senior-pitched C# course on the site); **ZTH Asynchronous Programming**, from "Async/Await Best Practices" on; **ZTH Garbage Collection**; **ZTH Benchmarking**.
- Skim: Deep Dive C# (the records and async sections only); ZTH Dependency Injection ("Deep dive" and "Advanced techniques" only); ZTH Configuration and Options (Key Vault providers); ZTH Logging (Serilog, masking and high-performance sections).
- Optional: 1BRC, as a stretch performance project.
- Skip: GS C#; Hands-On C# for Beginners; ZTH LINQ and Hands-On LINQ, unless the Mastering C# LINQ lessons expose a gap.

**C. APIs and data access**
- Watch: **ZTH REST APIs** (versioning, idempotency, auth, SDK sections); **ZTH EF Core**, chapters 7 to 9 (bigger solutions, advanced modelling, performance and concurrency).
- Skim: ZTH Minimal APIs (structuring and testing); ZTH Dapper (bulk, transactions); GS ASP.NET Core ("Bonus Tips" only); Migrating Web APIs to ASP.NET Core, if legacy Framework is on the table (I-3 names .NET Framework).

**D. Testing**
- Watch: **ZTH Integration testing** (the real-world and Playwright sections).
- Skim: ZTH Testing with xUnit; ZTH TDD.
- Skip: ZTH Unit testing, if xUnit and mocking are already daily practice.

**E. Data edge**
- Watch: **Hands-On Learn PostgreSQL**, from "Indexes" to the end (query analysis, window functions, transactions). Then Microsoft Learn's SQL Server index and Query Store material, to carry the same ideas onto SQL Server.
- Skip: GS SQL Server. It is below five years of production SQL. **Inference.**

**F. Front end.** Dometrain supplies only the language.
- Watch: **Deep Dive TypeScript**.
- Then angular.dev as the primary source. React through react.dev, after that.
- Skip: GS TypeScript and Hands-On Learn TypeScript.

**G. Architecture**
- Watch: **ZTH Vertical Slice Architecture** or **DD Clean Architecture** (pick the one the codebase will use); **DD Domain-Driven Design** (Event Storming, context mapping).
- Skim: GS DDD; the Hands-On design-pattern courses. Only the patterns a build needs; the 23 single-pattern courses are for reference.

**H. Distributed and reliable systems**
- Watch: **GS Messaging with MassTransit** (outbox and sagas); **ZTH Event-Driven Architecture** (idempotency, versioning, sagas); **ZTH Background Processing**; **GS Caching**, then selected chapters of **DD Caching** (Redis, distributed stampede, resiliency, cache security; 23h37m is too long to watch whole); **ZTH OpenTelemetry**.
- Skim: DD Microservices; GS and DD Event Sourcing (the nearest content to a ledger).

**I. Security**
- Watch: **GS Authentication and Authorization in .NET** (12h8m; the pipeline beneath every token scheme).
- Then the specs from section 3: RFC 9700, FAPI 2.0, UK Open Banking, OWASP API Top 10.
- Then **Mastering Azure for Developers**, the Entra ID and Key Vault sections.

**J. Platform**
- Watch: **GS and DD Azure for Developers** (App Service, Azure SQL, Functions, APIM); **ZTH Kubernetes for Developers**; **GS Bicep for Azure**; **GS Aspire**.
- Skim: ZTH Docker, if containers are already routine; ZTH Deploying .NET Apps to Azure (Terraform and Container Apps); ZTH GitHub Actions.
- Then Microsoft Learn's Azure Pipelines material for the Azure DevOps gap.

**K. System design and a capstone reference**
- Watch: **Hands-On System Design for Intermediate** and **for Azure**, then **Advanced**.
- Skim: **Let's Build It: URL Shortener**, as a worked example of Bicep, Key Vault, Cosmos, Polly, Entra ID and Redis in one repo. Read it after building, not before.
- Skip: Hands-On System Design for Beginners.

**L. AI tooling**
- Watch: **ZTH Microsoft.Extensions.AI** (it has the only LLM evaluation and unit-testing lessons); **GS Microsoft Agent Framework** (prompt-injection defence, OTel tracing).
- Skim: GS AI for .NET Developers.

**Interview practice.** Career: Nailing the Behavioral Interview. GS C# Interview Questions, as
a gap check only, per the existing warning in `CURRICULUM.md`.

The current `CURRICULUM.md` table names **"Learn PostgreSQL"** and **"Docker for Developers"**.
Both exist, as "Hands-On: Learn PostgreSQL" and "ZTH: Docker for Developers". It also names
"Hands-On Learn Linux", "Learn Bash" and several others that exist under the Hands-On series.
No course named there is missing from the catalogue, so the rebuild can keep those names.

---

## 5. Open questions for the user

1. **Which of the "deepest" skills have you already shipped in production?** For example
   EF Core performance work, MassTransit, Polly, Redis, OTel, or Azure DevOps. The skip and skim
   calls in section 4 are guesses. Your answer turns them into facts.
2. **Is angular.dev enough as the Angular source,** or do you want a paid course from another
   provider for first exposure? Dometrain has nothing here.
3. **Does React stay in the curriculum at all?** Investec lists it only as the alternative, and
   I-3 omits it. The earlier remote-work reason for React may no longer apply now that the
   target is Sandton.
4. **How much of the data edge is SQL Server, and how much is Spark/Databricks?** Investec asks
   for the first. The earlier AWS-heavy sample asked for the second. The answer decides whether
   the Postgres course or Microsoft Learn's SQL Server material is primary.
5. **Do you have access to an Azure DevOps organisation** (at work or a free one)? It is the one
   required platform tool that no Dometrain course teaches.
6. **Semantic Kernel or Microsoft Agent Framework?** Dometrain only teaches the latter.
7. **Is Blazor in or out?** It is well covered on Dometrain, and no Investec posting names it.

---

## 6. Sources

All read 2026-09-29.

**Dometrain, first-party**
- Sitemap: <https://dometrain.com/sitemap.xml> (every `<lastmod>` reads 2026-05-01T11:06:17.070Z)
- Catalogue: <https://dometrain.com/courses/> (171 `/course/` links, identical to the sitemap set)
- Learning paths: <https://dometrain.com/learning-paths/> (AI-generated, no fixed paths)
- Workshops: <https://dometrain.com/workshops/> (only "Vibe Coding for Production" conference workshops listed)
- Every course page at `https://dometrain.com/course/<slug>/` for the 171 slugs. Metadata from each page's `course-schema` JSON-LD, outlines from the rendered curriculum. The load-bearing ones:
  - <https://dometrain.com/course/getting-started-authentication-and-authorization-in-dotnet/>
  - <https://dometrain.com/course/mastering-azure-for-developers/>
  - <https://dometrain.com/course/from-zero-to-hero-rest-apis-in-asp-net-core/>
  - <https://dometrain.com/course/from-zero-to-hero-entity-framework-core-in-dotnet/>
  - <https://dometrain.com/course/from-zero-to-hero-integration-testing-in-asp-net-core/>
  - <https://dometrain.com/course/getting-started-sql-server/>
  - <https://dometrain.com/course/hands-on-learn-postgresql/>
  - <https://dometrain.com/course/getting-started-messaging-in-net-with-masstransit/>
  - <https://dometrain.com/course/deep-dive-caching-in-dotnet/>
  - <https://dometrain.com/course/lets-build-it-url-shortener-in-dotnet/>
  - <https://dometrain.com/course/deep-dive-azure-for-developers/>
  - <https://dometrain.com/course/from-zero-to-hero-deploying-dotnet-apps-to-azure/>
  - <https://dometrain.com/course/mastering-csharp/>
  - <https://dometrain.com/course/deep-dive-typescript/>
  - <https://dometrain.com/course/deep-dive-blazor/> (the only outline containing "Angular")

**Gap sources.** All URLs are inline in section 3, grouped by owner:
- Microsoft Learn (ASP.NET Core Identity, OIDC, integration tests, resilience, memory and
  spans, SQL Server index design, Query Store, Azure Pipelines, Cosmos DB, Container Apps, AKS,
  API Management, ADF, DP-750, Semantic Kernel)
- angular.dev, react.dev
- IETF (RFC 9700 via rfc-editor.org, the idempotency-key draft on datatracker)
- OpenID Foundation (FAPI 2.0 Security Profile, FAPI WG)
- UK Open Banking standards
- OWASP (ASVS, API Security Top 10)
- Information Regulator (POPIA), PCI SSC
- Investec Developer Portal, Testcontainers for .NET, dotnet/aspnet-api-versioning, HashiCorp,
  Databricks, Stripe

**Unreachable or not checked:** `https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/yarp`
returned 404 and is not used. nunit.org was not checked.

**Earlier files this extends**
- `research/2026-09-28-sa-fintech-target-roles.md` (section 8, Investec)
- `research/2026-09-23-full-stack-tooling.md`
- `research/2026-09-23-data-stack-and-certifications.md`
- `research/2026-09-23-fraud-and-bank-apis.md`
