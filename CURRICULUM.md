# Curriculum

The plan for building, and proving in public, that I'm a C#/.NET full-stack engineer who builds
**new fintech products** in South Africa and is **AI-ready**. Evidence rather than claims.

First written 2026-09-17. Rebuilt on 2026-09-22, 2026-09-29 and 2026-10-01. This version targets
fintech product engineering, based on 27 current C#/.NET adverts and the published engineering
practices of SA fintechs, consultancies and banks (`research/2026-10-01-*.md`). This file is
allowed to be wrong. It is not allowed to be vague.

**No dates, no week counts, no estimated finish.** A phase is over when its capstone's exit test
passes, and not before. How long that takes is an output of the work, not an input to it.

## Purpose

I already ship production C#. What that doesn't give me on its own is a map: which skills SA
fintech employers pay for, in what order to learn them, and a way to prove each one in public.
This file is that map. It's organised in four levels, **1 · Ship, 2 · Own, 3 · Scale and
4 · Lead**, and each level ends in a gate I have to pass cold.

Everything I build goes into one product, **randmatch**. The curriculum is how I get there; the
product is what I want judged.

"AI-ready" means two things here, both taken from the adverts and the employers:

1. **Using AI coding assistants well, and visibly checking what they produce.** This is the one
   that matters most. iOCO's AI-enabled senior post makes it mandatory ("demonstrate practical
   experience using AI as part of the software development lifecycle"). Absa has 1,400+
   developers on GitHub Copilot and Claude Code, and FirstRand 3,000 engineers on AI tools, and
   both always pair it with a control story. So every repo shows what AI proposed, what I
   rejected, and what the tests caught.
2. **One LLM feature built properly in C#:** the break-explainer behind `Microsoft.Extensions.AI`,
   masked, audited and eval-gated. Only 1 of 27 adverts asks for LLM features, so this is the
   differentiator, not the headline.

## What the market asks for

### The adverts

From 27 current SA C#/.NET full-stack adverts read on 2026-10-01
(`research/2026-10-01-csharp-fullstack-postings-to-projects.md`), and 39 E-Merge posts read on
2026-09-29 (`research/2026-09-29-curriculum-sources.md`). The level labels below are the adverts'
own.

| Advert level | What recurs |
|---|---|
| Junior | C#, SQL Server and T-SQL, HTML/CSS/JS. Advantageous: React, .NET Core, EF Core, Azure, CI/CD, containers, "AI tools used responsibly" |
| Intermediate | ASP.NET Core Web API and SQL Server. Angular as often as React. CI/CD, EF, Azure, Docker. DDD, CQRS and Clean Architecture start to appear, and so do legacy MVC, WebForms and Dapper |
| Senior | REST design, SQL tuning, Azure (and some AWS), testing, event-driven design, messaging, Bicep or Terraform, Entra ID, mentoring |
| Lead | Mentoring, architecture, delivery |

Counts from the 27 adverts on 2026-10-01:

| Ask | Count | Ask | Count |
|---|---|---|---|
| C# | 26 | Azure (any) | 17 |
| REST / Web API | 20 | Azure DevOps | 14 |
| SQL Server / T-SQL | 18 | GitHub Actions | 1 |
| Query tuning | 6 | Docker | 9 |
| PostgreSQL | 2 | Code reviews | 15 |
| Angular | 13 | Automated tests | 12 |
| React | 11 | Microservices | 10 |
| Blazor | 11 | Mentoring | 10 |
| TypeScript | 7 | Fintech or payments | 10 |
| AI coding assistants | 5 | LLM features / MCP | 1 |

### The employers

From `research/2026-10-01-sa-fintech-greenfield.md` and
`research/2026-10-01-employer-engineering-practices.md`:

- **Product fintechs are on AWS, and most don't write C#.** Stitch, Peach and iKhokha use
  TypeScript; Luno uses Go. **Ozow is the exception**: ASP.NET Core, SQL Server and Postgres, ECS,
  Terraform and k6, from its own stack page.
- **Most of the .NET hiring in Johannesburg** is at Investec, Nedbank, Discovery Bank and the
  consultancies (Dariel, Entelect, DVT).
  - Nedbank, Discovery and Investec are on Azure.
  - Absa and Capitec have gone AWS-first.
  - Standard Bank runs AI on Amazon Bedrock and runs SAFe (two open Release Train Engineer
    posts). That corrects the 09-29 count of 0 SAFe mentions.
- **The AI-forward shops work spec-first:**
  - Luno's Spec Kit gate blocks task generation until `spec.md` and `plan.md` are merged.
  - DVT's AI Build Teams write testable specifications before development.
  - FirstRand grounds its AI on requirements, test plans and standards.
- **Synthesis has published an AI maturity ladder (L0–L4).** At L3, each agent handoff is
  defined, observable and repeatable, and you prove the gains with numbers.
- **Reconciliation is something employers sell as a product.** Stitch, Peach, Transaction
  Junction and Ecentric all do. Stitch's payouts run on three file types: instruction, reply and
  statement.

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

Udemy ratings and dates in the research files are unverified, because Udemy blocks automated
reads.

## The product: randmatch

**Payout reconciliation for South African merchants who take payments through several providers**
(Yoco, Payfast, Peach, Paystack, Ozow, plus EFT and PayShap) **and close their books in Excel,
Xero or Sage.** Bookkeepers serving many such merchants are the multiplier.

Why this problem (from `research/2026-10-01-fintech-problems-validated.md`):

- **No provider's payout matches a single sale.** Each one pays a net, batched deposit: Yoco pays
  daily, Peach makes "one consolidated deposit", and Paystack splits payouts into batches.
- **Each provider reconciles only itself.** Yoco's Xero app matches Yoco payouts, and Paystack's
  covers invoices only. A merchant on three providers gets three partial answers.
- **People pay for this.** Stitch, Transaction Junction, Ecentric and Precium sell it to
  enterprise. Ecentric cites mid-market retailers needing "two and three weeks" to see their
  month-end position.
- **Draft regulation is heading the same way.** The SARB's draft Authorisation Framework would
  require money remitters to reconcile segregated client funds to individual transactions.
- **Ledger failures are expensive.** Synapse's records did not match its partner banks', leaving
  a $60–90m shortfall.
- **Honest limit:** no survey measures how badly SMEs suffer from this. Five conversations with
  bookkeepers are the first validation step.

### Three repos, one product

| Repo | Role | Stack and deployment |
|---|---|---|
| `randmatch-recon` | **The product.** Ingests provider exports, bank CSV and OFX, and `camt.053` XML with XSD validation. Breaks payouts down into sales, fees, refunds, chargebacks and holds, with many-to-one matching. Matching rules are pluggable, one class per break type. File ingestion has bounded parallelism. Exceptions queue. Data is processed locally, and personal data is stripped on import | ASP.NET Core and EF Core; **SQL Server**, with tuning write-ups in `docs/perf/`; **React + TypeScript + Tailwind**. **Azure:** Container Apps, Azure SQL, Key Vault, App Insights, a Function for file-drop ingest, Service Bus. **Bicep** and **Azure DevOps** multi-stage (UAT → approval → prod), alongside GitHub Actions |
| `randmatch-ledger` | **The clearing ledger.** One clearing account per provider, and every movement is a double-entry posting. Idempotent posting API. Xero and Sage journal export. A client-funds safeguarding view. A hash-chained, tamper-evident audit log | ASP.NET Core; **Postgres** (EF Core + Npgsql, hand-written posting SQL); an **Angular** operator console (journal browser, export-batch approval, idempotency-key lookup). **AWS:** ECS Fargate, RDS Postgres, **Terraform**, a **k6** load test proving idempotency under concurrent retries. This is Ozow's stack |
| `randmatch-sim` | **The test-data generator.** Emits instruction, reply and statement files (MT940 and `camt.053`), provider exports, a settlement API, and signed webhooks with replay protection. Webhooks arrive out of order, duplicated, or as `uncertain` → `Successful`. **Breaks are planted between sources**, and they become the answer key the evals score against | .NET worker; Postgres; outbox with a transport-agnostic publisher (Kafka or Redpanda locally, Service Bus when deployed); an optional **Blazor** control panel |

The planted breaks:
- rejected in the reply file but booked as paid;
- a statement credit with no instruction;
- one bank down mid-batch;
- a refund that arrives only by webhook;
- a fee netted from settlement;
- a cut-off timing break.

**The AI layer** lives in recon:
- **The break-explainer** sits behind `IChatClient`, with Azure OpenAI, Anthropic and Bedrock as
  backends.
  - It masks references and personal data before any prompt.
  - It writes one audit row per call: who asked, model, prompt version, tokens, cost, and the
    rows it cited.
  - It is eval-gated in CI against the planted breaks.
  - **It can never post an adjustment.** A human approves every suggestion.
- **A read-only MCP server**, scoped to one tenant.
- **Multi-tenancy:** a bookkeeper firm is a tenant, and its merchants sit under it. Entra ID /
  External ID sign-in; roles Owner, Reviewer and Read-only. Isolation tests check both the API
  and the data layer.

**Measured results** each README publishes:
- match rate and false-match rate against the planted breaks;
- eval pass rate;
- k6 numbers;
- review turnaround and defects caught before merge, self-reported in
  `docs/ai-engineering/metrics.md`;
- later, a pilot bookkeeper's month-close effort against their own baseline.

**Non-claims, in every README:**
- synthetic data, or your own exports processed locally;
- not PayShap-conformant (its spec isn't public);
- no card numbers, so no PCI scope;
- the AI never posts;
- unaffiliated with any provider named.

**POPIA.** Provider exports can carry customer names. Process locally, strip personal-data
columns on import, and store nothing personal. If it is ever hosted: Azure South Africa North, an
operator agreement, and the cross-border rules.

**Superseded:** the municipal service-delivery tracker (the 2026-09-29 flagship) and the earlier
`parity` / `platform` / `product` plans. They stay in `research/` for the record.

## How every mini and capstone runs

**The workflow, ten steps.** This is what the iOCO advert, Luno, DVT, FirstRand and Synthesis L3
have in common. Each step leaves an artefact in the repo.

1. **Issue.** `.github/ISSUE_TEMPLATE/feature.yml`, with Given/When/Then acceptance criteria.
   AI drafts the edge cases; I cut any that can't be tested.
2. **Spec and plan first.** `specs/<feature>/spec.md` and `plan.md` are merged in their own PR
   before any code. Diagrams are Mermaid or C4.
3. **Decision record.** `docs/adr/NNNN-*.md` in MADR format, with an **"AI input"** section: what
   was proposed, adopted and rejected, and why. I write the Decision paragraph myself.
4. **Implement.**
   - `CLAUDE.md` / `AGENTS.md` names the agent roles: spec reviewer, test writer, code reviewer,
     security scanner.
   - **The core logic of each concept is mine.** AI scaffolds around it.
   - Warnings are errors, and architecture tests enforce the layers.
5. **Test.**
   - Unit tests.
   - Integration tests via Testcontainers, against SQL Server and Postgres.
   - Property tests ("journals net to zero").
   - Concurrency tests on idempotency keys.
   - Stryker.NET mutation testing on the matcher and the ledger, with the score in the PR.
   - Every test file opens with the risk it covers.
6. **AI review, then security review.** The PR template's **"AI involvement"** section triages
   each AI finding as accepted, rejected or deferred. Each accepted one needs a test or a
   reason. `docs/security/threat-model.md` (STRIDE) is updated, and CodeQL, Dependabot and secret
   scanning run in CI.
7. **PR and CI/CD.** Small PRs with `Closes #n`, `CODEOWNERS`, and self-review comments on the
   risky lines. CI gates: tests, coverage, OpenAPI diff, the LLM eval gate, and one deliberate red
   build kept on record.
8. **Deploy and monitor.** Bicep or Terraform, with `what-if` or `plan` output attached to the PR.
   OpenTelemetry traces run sim → ledger → recon. `docs/slo.md`.
9. **Incident.** A game day where the sim plants a fault. It is written up in
   `docs/incidents/YYYY-MM-DD-*.md`, with a regression test, including which AI hypotheses were
   wrong.
10. **Standards.** `docs/ai-engineering/standards.md` covers what AI may do, the review rules, and
    no real merchant data in prompts. It sits alongside `CONTRIBUTING.md`.

**Around the ten steps:**
- **Board.** GitHub Projects: Backlog → Ready → In progress → Review → Done, WIP limit 2, with
  iterations as sprints. Once, at Level 2, one sprint runs in Azure DevOps Boards and Pipelines,
  because that's the tool SA adverts name most.
- **Release.** A tag, and a changelog from Conventional Commits.
- **Where things live.** Minis live in this repo, under `<level>/<phase>/`. Capstones add
  features to the randmatch repos.
- **Progress.** Every item here is also in `progress/curriculum.yml`. An item counts as done only
  when its `evidence` field holds a URL. `tools/progress.py` builds `PROGRESS.md` and the
  dashboard, and CI rejects a mini or capstone whose evidence isn't on GitHub.
- **Level gate.** Build the level's capstone, pass its exit test cold, and pass the oral check. A
  phase I already know can be tested out of by passing its exit test first.

## Explaining the why, and the break-fix loop

The point is to answer "why did you do it this way?" and "tell me about a time something broke"
from my own work, with evidence.

1. **Why this design.** A decision record for every capstone and any non-trivial mini: the
   constraints, at least two options stated fairly, what I chose, the trade-off I accepted, and
   what would change my mind. Prior art is cited: `luno/workflow`, Stitch's payouts deep dive,
   Blnk and Formance, and the Stripe Ledger post.
2. **Why this test.** Every capstone README has a test strategy table: risk, test type, why that
   type, and what it doesn't catch. A test whose risk I can't name gets deleted.
3. **Why this system design.** Every design doc states the load, the numbers behind it, the
   bottleneck, the failure modes, and what changes at 10×.
4. **The break-fix drill.** Every capstone ends with a planted fault I haven't seen the fix for.
   They get harder:

   | Level | Faults | What I learn to use |
   |---|---|---|
   | 1 · Ship | Null reference, off-by-one, `double` money, wrong status code, broken migration, bad Azure config | Stack traces, the debugger, structured logs, `git bisect` |
   | 2 · Own | A matching query that goes slow after a data change, a deadlock on postings, a race in ingestion, eval quality dropping after a prompt change | Execution plans and Query Store, `dotnet-counters`, `dotnet-trace`, eval regressions |
   | 3 · Scale | Lost or duplicated messages, a replayed webhook, a broken managed identity, a retry storm, an agent calling the wrong tool | OpenTelemetry traces across services, dead-letter queues, chaos tests |
   | 4 · Lead | A memory leak, thread-pool starvation, a capacity limit under load, a cascading failure | `dotnet-dump`, `dotnet-gcdump`, load tests, SLO burn alerts, running the incident |

5. **The postmortem**, in `docs/incidents/`, with these sections:
   - what broke, and what the user saw;
   - how it was detected;
   - why it broke (five whys);
   - how I diagnosed it, dead ends included;
   - the fix, and why that fix;
   - how it's prevented from happening again;
   - what I'd do differently.

   The regression test, alert or guardrail must be merged before the story closes.
6. **Interview answer bank.** At each level gate, three STAR answers go into
   `interview/answers.md`: a design decision, a testing choice, and the incident. Each links to
   the real record.
7. **The oral check.** Someone else, or an AI playing interviewer, picks any file in the capstone.
   I explain why it's written that way, what would break it, and how I'd find out why.
8. **Interview prep the employers imply:**
   - defend one class's SOLID design live and refactor it on the spot (Entelect);
   - explain bounded concurrency (iKhokha's public tech check);
   - a feedback-reviewed .NET take-home (DVT);
   - psychometric and technical assessments (Ozow);
   - walk the spec → plan → PR trail (Luno, Synthesis).

Three habits borrowed from `kablewithak/ai-engineering-interview-vault`:

- **`mistake-patterns/`**: one short file per misconception I correct.
- **`concepts/`**: a page per concept that grows over time: how to explain it, where I applied
  it, how it fails, and how to test it.
- **`review/queue.md`**: active-recall questions from every `NOTES.md`, revisited at every later
  level gate.

## Reference repos

Read for structure and practice, not copied.

| Repo | What to take from it | Level |
|---|---|---|
| `luno/workflow` | Outbox, idempotent state-machine steps, Kafka streamer: the pattern `randmatch-sim` uses | 3 |
| `luno/spec-kit-plan-review-gate` | Spec and plan merged by PR before tasks | All |
| `blnkfinance/blnk`, `formancehq/ledger` | Open-source double-entry ledgers, with Blnk's matching against statements | 1→3 |
| `investec-developer-community/investec-dev-quest` | Replay protection, SSRF-safe callbacks, tamper-evident audit logs | 3 |
| `synthesis-software-technologies/techteam-content` | The L0–L4 AI maturity field guide | All |
| `capitec/pg-proxy` | Data masking and audited LLM calls in front of a database | 2→3 |
| `jasontaylordev/CleanArchitecture`, `ardalis/CleanArchitecture` | Starting templates; compare them in a decision record | 1→2 |
| `kgrzybek/modular-monolith-with-ddd` | A real decision log, C4 diagrams and a glossary next to the code | 2→3 |
| `dotnet/eShop` | Service and test layout at senior level | 3 |
| `dotnet/extensions` (`Microsoft.Extensions.AI.Evaluation`) | .NET-native LLM evals that can gate CI | 2→3 |
| `modelcontextprotocol/csharp-sdk` samples | The protected ASP.NET Core MCP server | 3 |
| `anthropics/anthropic-sdk-csharp`, `openai/openai-dotnet` | SDK examples, and repo hygiene worth copying | 1→2 |
| `adr/madr` | The decision-record format | All |
| `danluu/post-mortems`, `dastergon/postmortem-templates` | Real failures to base drills on | All |
| `donnemartin/system-design-primer` | The worked-example structure for design docs | 2→3 |
| `microsoft/code-with-engineering-playbook` | Definition of Done, code and design reviews | 2 |

The Stripe Ledger post, Stitch's payouts deep dive and Modern Treasury's reconciliation docs are
reading, not repos.

## Certifications

At least one data, security or cloud certificate at every level. Statuses and prerequisites were
checked on each certifying body's own pages on 2026-09-29.

| Level | Certificates | Optional | Prep |
|---|---|---|---|
| 1 · Ship | **DP-900** (data), **SC-900** (security) | AZ-900, GH-900, HackerRank C# and SQL Basic | Phillip Burton |
| 2 · Own | **AZ-104**, **DP-800** SQL AI Developer (data), **Terraform Associate 004** (IaC) | CKAD; HackerRank SQL, Problem Solving and REST API Intermediate | Scott Duffy and Dometrain Exam Prep (AZ-104), Burton (DP-800), Zeal Vora (Terraform) |
| 3 · Scale | **SC-500** (security), **CKA** (containers) | AWS Solutions Architect Associate (the fintechs are on AWS), AZ-400, DP-300 | Alan Rodrigues (AZ-400), Mumshad Mannambeth (CKA); check the instructor for SC-500 and AWS SAA |
| 4 · Lead | **SC-100** (needs SC-500), **CKS** (needs CKA) | AZ-305, Terraform Authoring and Operations Advanced | Alan Rodrigues (SC-100), Zeal Vora (CKS), Scott Duffy (AZ-305) |

Retired, so not to be studied for: AZ-204, AZ-500, AI-102, AI-900 (now AI-901). Several Microsoft
exams get content updates in late October 2026; check that a prep course was updated after its
exam was.

---

## Level 1 · Ship: C# full stack, AI-ready

**The gate:** I can ship a small full-stack product feature with an LLM in it, containerised, in
CI and on Azure, built with an AI coding assistant whose output I reviewed and can defend.

### 1.0 — Linux, Git, SDLC and Scrum

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Udemy: Imran Afzal, *Complete Linux Training Course*; *Complete SDLC (2026)*; 365 Careers, *Complete Agile & Scrum Project Management Course*. Dometrain: Hands-On: Learn Git From Scratch; ZTH: GitHub Actions; GS: Claude Code | A users-and-permissions script and a systemd timer; a `grep`/`sed`/`awk` log report; an Actions workflow; the issue form and PR template every later repo reuses | **`logkit`**, the ladder in `challenges/phase-00-shell-linux-git/`, run as the first full sprint | Explain the CI file line by line to another person |

### 1.1 — C# and the core data structures

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Dometrain: GS: C#; Hands-On: C# for Beginners; ZTH: Working with Null; ZTH: LINQ; Hands-On: LINQ; DD: C#; Hands-On: Data Structures & Algorithms in C#, chapters 1–9. HackerRank: Interview Preparation Kit, first topics | Value objects (`Money` as `decimal` with currency); a bank-statement CSV parser with line-level errors; a linked list, stack and queue from scratch; three sorts, benchmarked | **`statement-cli`**: reads Yoco, Peach and Paystack exports and bank CSV/OFX, validates them, rejects duplicate files by content hash, and prints a payout breakdown | Rebuild it from a blank repo. Pass HackerRank C# (Basic) |

### 1.2 — SQL Server and T-SQL

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Udemy: Phillip Burton, *70-461/761 Querying SQL Server with T-SQL*. Dometrain: GS: SQL Server. HackerRank: SQL track | CTEs and window functions; a `MERGE` upsert; a stored procedure with `TRY`/`CATCH`; a normalised schema from a messy spreadsheet | The `randmatch-recon` schema on SQL Server (sources, files, lines, payouts, matches, exceptions, audit), loaded from `statement-cli`, with many-to-one matching queries | Pass HackerRank SQL (Basic) |

### 1.3 — ASP.NET Core Web API, EF Core and testing

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Dometrain: GS: ASP.NET Core; ZTH: REST APIs; ZTH: Minimal APIs; ZTH: Entity Framework Core; ZTH: Unit Testing; ZTH: Testing with xUnit; Hands-On: Learn PostgreSQL | A provider settlement API client with retries; validation returning Problem Details; EF Core migrations; an `Idempotency-Key` replay test | **Recon API v1** (SQL Server) and **Ledger API v1** (Postgres): idempotent postings, an OpenAPI spec, unit tests | Add an endpoint test-first, explaining each step |

### 1.4 — TypeScript and React

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Dometrain: GS: TypeScript; Hands-On: Learn TypeScript. Udemy: Maximilian Schwarzmüller, *React – The Complete Guide* | A responsive layout; a typed API client generated from OpenAPI; an export upload with per-row validation errors; a searchable, paged payout list | The **recon UI** in React and Tailwind: upload exports, see a payout broken down, work the exceptions queue | Build a new screen from a user story with no tutorial open |

### 1.5 — LLMs in C#, AI coding assistants, and shipping

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Dometrain: GS: AI for .NET Developers; GS: AI Agents in C#; DD: Claude Code; ZTH: Working with GitHub Copilot; ZTH: Docker; ZTH: Docker Compose; GS: Azure for Developers. DeepLearning.AI: *ChatGPT Prompt Engineering for Developers*; *Building Systems with the ChatGPT API* | One break classifier on OpenAI and Anthropic behind one `IChatClient`; structured JSON output; cost logging; a `CLAUDE.md` and a custom command; personal-data masking before any prompt | **The Level 1 gate**: break-explainer v0 explains an unmatched payout, cites the rows it read, writes an audit row per call, and waits for a human to accept. Containerised, in CI, on Azure Container Apps | Demo it, and explain every AI-generated line I kept |

**Certificates:** DP-900 and SC-900.

## Level 2 · Own

**The gate:** I own features end to end in a layered .NET system: tuned SQL, concurrent code,
Angular and React, CI/CD on Azure DevOps, and an AI feature whose evals gate the build.

### 2.1 — C# depth, concurrency and the rest of DSA

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Dometrain: ZTH: Asynchronous Programming; ZTH: Parallel Programming; ZTH: Dependency Injection; ZTH: Configuration and Options; ZTH: Logging; Mastering: C#; the rest of Hands-On: Data Structures & Algorithms in C#. HackerRank: the rest of the Interview Preparation Kit | A `Channel<T>` pipeline; a race condition reproduced and fixed; a trie for merchant-reference prefix matching; a graph of payout, batch and statement links that finds the orphans | A **pluggable matcher** (one rule per break type, added without editing a switch) with **bounded-parallel ingestion**, benchmarked; 100 parallel postings leave the ledger balanced | Pass HackerRank Problem Solving (Intermediate) |

### 2.2 — Data access depth

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Dometrain: ZTH: Entity Framework Core, chapters 7–9; ZTH: Dapper; ZTH: Integration Testing in ASP.NET Core; Migrating: ASP.NET Web APIs to ASP.NET Core. Udemy: Phillip Burton, DP-800 prep | Scan to seek; parameter sniffing; a deadlock reproduced and fixed; the same query in EF Core and Dapper; vector search in SQL Server | `docs/perf/` write-ups on the matching queries (plans, indexes, timings); the Xero and Sage journal export; integration tests against SQL Server and Postgres via Testcontainers | Read an unfamiliar execution plan and explain the fix. Pass HackerRank SQL (Intermediate) |

### 2.3 — Architecture

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Dometrain: Hands-On: Creational, Structural and Behavioral Design Patterns; GS and DD: Clean Architecture; ZTH: Vertical Slice Architecture; GS and DD: Domain-Driven Design; GS and DD: Modular Monoliths | Three patterns on real code; a CQRS read model; an event-storming board for payout reconciliation | `randmatch-ledger` as a modular monolith (Accounts, Postings, Exports, Audit), with architecture tests and decision records | Defend the module boundaries, with two options stated fairly |

### 2.4 — Angular and end-to-end testing

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Udemy: Maximilian Schwarzmüller, *Angular – The Complete Guide*; Karthik K.K., *Playwright in C# .NET* | A signals-based component; a typed reactive form; the same screen in React and Angular; a Playwright page-object suite | The **Angular ledger operator console**: journal browser, export-batch approval, idempotency-key lookup; Playwright over both front ends | The Playwright suite green in CI |

### 2.5 — Azure and CI/CD with Azure DevOps

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Dometrain: ZTH: Deploying .NET Applications to Azure; DD: Azure for Developers; GS: Aspire; GS: Bicep for Azure; ZTH: Serverless with Azure Functions; Exam Prep: AZ-104. Udemy: Phillip Burton, AZ-900; Scott Duffy, AZ-104; Zeal Vora, Terraform Associate | A multi-stage YAML pipeline; a slot swap; Blob and Service Bus integration; one sprint in Azure DevOps Boards | **Recon on Azure**: Bicep for Container Apps, Azure SQL, Key Vault, App Insights, a file-drop Function and Service Bus; Azure DevOps multi-stage (UAT → approval → prod) | Roll back a bad deploy |

### 2.6 — RAG and evals

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Dometrain: ZTH: Microsoft.Extensions.AI; Let's Build It: AI Chatbot with RAG in .NET. DeepLearning.AI: *Vector Databases*; *Building and Evaluating Advanced RAG*; *Evaluating AI Agents* | An embeddings search over past resolved breaks; chunking strategies compared; an LLM-as-judge harness in xUnit; a prompt-injection test set | **The Level 2 gate**: the break-explainer retrieves similar resolved breaks, cites them, and is scored against the planted breaks, with evals gating CI and cost tracked per call | Report the eval results honestly, failures included |

**Certificates:** AZ-104, DP-800 and Terraform Associate.

## Level 3 · Scale

**The gate:** I design and run distributed, secure .NET systems across Azure and AWS with agentic
AI, can work in Python for AI services, and mentor through code review.

### 3.1 — Messaging, resilience and observability

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Dometrain: GS: Messaging with MassTransit; ZTH: Event-Driven Architecture; ZTH: Background Processing; GS and DD: Caching; GS and DD: Microservices Architecture; GS: Event Sourcing; ZTH: OpenTelemetry. Udemy: Stephane Maarek, *Apache Kafka for Beginners* | An outbox written by hand; an inbox for deduplication; retry, timeout and circuit breaker; the same flow on Service Bus and Kafka; Redis caching with correct invalidation | **`randmatch-sim`**: instruction, reply and statement files; signed webhooks arriving out of order and duplicated; an outbox with a transport-agnostic publisher; traces from sim → ledger → recon | Kill the broker mid-run: nothing is lost and nothing is posted twice |

MassTransit v9 and MediatR are now commercially licensed. Learn the concepts from the course, but
build the outbox and consumer by hand, and check current terms before depending on either.

### 3.2 — Security, identity and POPIA

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Dometrain: GS: Authentication and Authorization in .NET; Mastering: Azure for Developers. Udemy: Aref Karimi, *Modern Identity and Security for ASP.NET Core*; an OWASP API Top 10 course; SC-500 prep | An insecure API, then fixed; strict JWT validation; managed identity to Key Vault; webhook signature, timestamp and nonce checks | Entra ID sign-in; each bookkeeper firm an isolated tenant with roles; replay protection; SSRF-safe callback registration; POPIA controls for minimisation, retention and residency | Walk through the token flow; a cross-tenant request is refused at the API and the data layer |

### 3.3 — AWS, Terraform and cloud-native options

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Dometrain: ZTH: Kubernetes for Developers; ZTH: Cloud Architecture in Azure; GS: GraphQL. Udemy: Mumshad Mannambeth, CKA; Alan Rodrigues, AZ-400; an AWS Solutions Architect Associate course (instructor to be checked) | A Terraform module for ECS Fargate and RDS; the same service in Bicep, compared in a decision record; a Helm chart (optional); a GraphQL endpoint (optional); an SLO alert | **`randmatch-ledger` on AWS**: ECS Fargate, RDS Postgres, Terraform, and a k6 load test proving idempotency under concurrent retries | From an empty account to a live ledger, and back, with tear-down scripted |

### 3.4 — Python for AI services

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Dometrain: Hands-On: Learn Python. DeepLearning.AI: *AI Python for Beginners*. Udemy: Eric Roby, *FastAPI – The Complete Course* | A typed CLI; a FastAPI service tested with pytest; an async file processor | A containerised FastAPI **fee-drift and anomaly detector**, called by recon, in the same CI | Rebuild it from a blank repo |

### 3.5 — Agents and MCP

| Learn | Minis | Capstone | Exit |
|---|---|---|---|
| Dometrain: GS: Microsoft Agent Framework in .NET; GS: Model Context Protocol. Udemy: Mehmet Ozkaya, *Agentic AI Development with Agent Framework, MCP and .NET*. DeepLearning.AI: *Agentic AI*; *MCP with Anthropic*; *Agent Skills with Anthropic*; *Reasoning with o1* | A read-only, tenant-scoped MCP server in C# over the recon API; a tool-calling agent with human approval; agent traces in OpenTelemetry; an agent eval suite; promptfoo red-team runs | **The Level 3 gate**: an agent that proposes resolutions for open breaks through MCP tools, with approval before any action, evals and a cost budget, plus a peer PR reviewed | Present its design and failure modes to another person |

**Certificates:** SC-500 and CKA.

## Level 4 · Lead

**The gate:** I set technical direction, lead architecture and delivery, go deep on the runtime,
understand models from the ground up, and mentor.

| Phase | Learn | Capstone |
|---|---|---|
| 4.1 — Performance and the runtime | Dometrain: ZTH: Garbage Collection; ZTH: Benchmarking; ZTH: 1 Billion Row Challenge; ZTH: Source Generators | Measured speed-ups on recon's hot paths, with before and after benchmarks |
| 4.2 — System design leadership | Dometrain: Hands-On: System Design, Beginners → Intermediate → Azure → Advanced; GS and DD: Solution Architecture; Career: Making High-Impact Decisions with AI | A design doc for scaling randmatch; the client-funds safeguarding chapter |
| 4.3 — ML foundations | DeepLearning.AI: *Machine Learning Specialization*; *Generative AI with LLMs*; *Retrieval Augmented Generation* | A classical model, a fine-tuned model and an LLM compared on break classification, with cost, latency and accuracy reported honestly |
| 4.4 — Lead and ship | Dometrain: Career: Nailing the Behavioral Interview; GS: C# Interview Questions. Udemy: PSM I prep (optional) | An open-source contribution; a real bookkeeper pilot on their own exports; an on-call runbook and a staged incident's postmortem; a log of code reviews given |

**Certificates:** SC-100 and CKS.

---

## What this curriculum still will not prove

Kept here for the same reason `NON-CLAIMS.md` is kept at top level.

- Working inside a large team's codebase with competing priorities.
- Operating a system at a scale an employer would call scale.
- That randmatch has users, until a bookkeeper actually uses it.
- Years of experience in a stack. iOCO's post wants "5+ years React" and "3+ years PostgreSQL";
  a portfolio shows capability, not tenure.
- Legacy .NET Framework, WebForms or MVC 5 work, which 10 of 27 adverts mention. That evidence
  comes from my work history.
- That I am employable. It proves I can learn and ship, which is necessary and not sufficient.

## When to reassess

- **At every level gate.** Did the exit test pass, honestly, or did I talk myself past it?
- **Every `horizon/` entry.** Re-read current adverts. The ones in `research/` are snapshots and
  will go stale.
- **If an exit test fails three attempts running.** That's information about the plan, not about
  me. Cut the scope of the phase, never the standard of the test.
- **If `decisions/` has fewer records than there have been real decisions.** Write the missing
  ones, dated the day they're written and marked late.
- **Never by elapsed time.**

## Research behind this file

- `research/2026-10-01-csharp-fullstack-postings-to-projects.md`: 27 adverts, requirement counts,
  and the gap analysis this product answers
- `research/2026-10-01-employer-engineering-practices.md`: what Ozow, Peach, Stitch, Orca,
  iKhokha, Luno, DVT, Synthesis, Entelect and the banks build and how they work
- `research/2026-10-01-sa-fintech-greenfield.md`: who builds greenfield fintech, their stacks,
  regulation, and sandboxes
- `research/2026-10-01-fintech-problems-validated.md`: whether each repo solves a real problem,
  plus the framings and the name
- `research/2026-10-01-github-builder-bios.md`: the profile research
- `research/2026-09-29-curriculum-sources.md`, `2026-09-29-dometrain-catalogue.md`,
  `2026-09-29-learning-platforms.md`: postings, course choices, and platform comparison
- Earlier direction, superseded but kept for the record: `2026-09-22-sa-target-roles.md`,
  `2026-09-22-data-role-example.md`, `2026-09-23-data-stack-and-certifications.md`,
  `2026-09-23-fraud-and-bank-apis.md`, `2026-09-28-sa-fintech-target-roles.md`,
  `2026-09-29-fintech-knowledge-sources.md`, `2026-09-17-openai-target-roles.md`,
  `2026-09-17-floci-local-build.md`, `2026-09-23-full-stack-tooling.md`,
  `2026-09-26-github-profile-landing.md`, `2026-09-29-github-profile-stack.md`
