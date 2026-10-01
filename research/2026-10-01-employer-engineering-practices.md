# Employer engineering practices: what Ozow, Peach/Stitch, Orca, iKhokha, Luno, DVT, Synthesis, Entelect and the big banks build, and how they work

Research for the `randmatch` portfolio: `randmatch-recon`, `randmatch-ledger` and `randmatch-sim`. Every URL below was read on **2026-10-01** unless another date is given. Claims carried over from earlier files keep those files' dates. **Inference** marks my reasoning. **Unverified** marks claims I could not confirm at a primary source. **Secondary** marks aggregators, Glassdoor and press summaries. There are no salaries and no timelines.

This file builds on `2026-09-28-sa-fintech-target-roles.md`, `2026-09-23-fraud-and-bank-apis.md` and `2026-09-29-curriculum-sources.md`. It does not repeat their stack tables.

---

## The verdict

**randmatch is aimed at the right problem, and part of it is in the wrong cloud and the wrong place in the market.**

**The problem is right.** Reconciliation is something SA payment companies sell as a product:
- Stitch sells consolidated reconciliation across channels and banks.
- Peach sells a Recon API and payouts with "automated reconciliation".
- Nedbank is building an enterprise "payment service hub".

A merchant-side, multi-PSP reconciler with a ledger and a break simulator describes these employers' own customers' pain, in their own vocabulary.

**The cloud is wrong.** Every fintech and consultancy on the list that names a cloud is on AWS. Two of the big banks (Absa and Capitec) have publicly gone AWS-first. Standard Bank runs its enterprise AI on Amazon Bedrock. Only Nedbank, Discovery Bank and Investec are visibly Azure-first.

**The market position is wrong.** The PSP startups don't write C#: Peach is TypeScript, Python and Rust; Stitch is TypeScript; Luno is Go; iKhokha is Node and TypeScript. The .NET buyers are Ozow, the Azure banks and the consultancies.

**So:**
- **Deploy `randmatch-ledger` on AWS.** Use ECS Fargate, RDS Postgres and Terraform. That is Ozow's published stack almost exactly.
- **Make `randmatch-sim` emit what PSPs actually emit.** That means settlement API responses, SFTP/S3 file drops, bank reply files and statement files, and webhooks with replay protection.
- **Leave `randmatch-recon` on SQL Server.** It is the Investec, Nedbank and Discovery-shaped piece.
- **Make the AI break-explainer provider-agnostic, masked and audited, with evals as a gate.** That is the shape the banks are publicly converging on.
- **Make spec-before-code visible in the repo history**, using the pattern Luno, FirstRand and DVT describe.

Five findings this run adds:

1. **AI coding tools are rolled out at bank scale, and every bank pairs them with a control story.**
   - Nedbank: GitHub Copilot for "more than 980 developers" (2024 results).
   - Absa: "1,400+ developers" on GitHub Copilot and Claude Code (2026-08-19).
   - Standard Bank: about a third of technology staff, "approximately 20%" productivity (2026-08-25).
   - FirstRand: about 3,000 engineers, with AI grounded on "functional requirements, test plans, architecture standards and security controls" (2026-08-19).
   - Discovery: measuring 20–25%, but "going slow" on agents and building "the harness" (2026-08-06).
2. **Spec-driven development is how the AI-forward shops work.** Luno published a Spec Kit gate that blocks task generation until `spec.md` and `plan.md` are merged by PR. DVT's AI Build Teams turn requirements into "clear, testable specifications before development began". FirstRand's CDO: "the quality of AI-generated code depends … on the quality of the organisation's specifications."
3. **Synthesis has published its internal AI maturity ladder (L0–L4).** Level 3 means "each agent handoff is defined, observable, and repeatable", with gains you "can prove … with numbers". That ladder is the best available rubric for an "AI-review trail".
4. **Peach appears to be building payment orchestration on Juspay's open-source Hyperswitch (Rust).** Its fork has active branches for ACI, Capitec VRP, PayDunya and "external refunds from webhook", the newest dated 2026-07. **Inference:** this is engineering work in progress, not proof of production use.
5. **"ocra" is almost certainly Orca Fraud** (Cape Town, real-time fraud monitoring, Ozow is a client). **"pitch" has no exact SA match.** The top candidate is Peach Payments; Stitch is a close second. Both are covered below.

---

## 0. Resolving the names

| User's word | Candidates checked | Finding | Confidence |
|---|---|---|---|
| **ocra** | Orca Fraud; "OCRA"; Ukheshe/Oneblock | **Orca Fraud**: same four letters, transposed. It is a Cape Town fraud-prevention fintech founded January 2024 by ex-Stitch engineers Thalia Pillay and Carla Wilby. It raised a $2.35m seed in March 2026. Early clients include **Ozow**, Sling Money and Cauridor ([Launch Base Africa, 2026-03-10](https://launchbaseafrica.com/2026/03/10/stay-in-it-how-over-200-interviews-and-a-linkedin-post-led-to-a-2-35m-seed-round-for-orca/)). A search for an SA company called "OCRA" found none ([web search](https://www.google.com/search?q=OCRA+South+Africa+software+company+payments)). Ukheshe doesn't fit the letters and wasn't pursued | **High.** It sits in the same cluster as the rest of the list (Ozow client, Stitch alumni) |
| **pitch** | Peach Payments; Stitch; pitch.com; an SA fintech called "Pitch" | No SA fintech called "Pitch" turned up ([search results](https://www.google.com/search?q=%22Pitch%22+South+African+startup+Johannesburg+fintech)). **Peach Payments** is the closest sound-alike ("peach" /piːtʃ/ against "pitch" /pɪtʃ/). It is a Cape Town PSP with a payouts team and a Recon API, so it is directly relevant to randmatch. **Stitch** rhymes, is a Cape Town PSP, and is where Orca's founders came from. pitch.com is presentation software; **Unverified**, from background knowledge, and irrelevant here | **Medium.** Peach is the top candidate and Stitch is flagged. Both are covered |

`orcafraud.com` redirects to a GoDaddy parked-domain page. The live site is [orca-fraud.com](https://www.orca-fraud.com), and its `/careers` page returned 404.

---

## 1. The fintechs

### Ozow

**What they're building now**
- Pay-by-bank plus PayShap Request ([Tech Africa News](https://techafricanews.com/2025/07/31/ozow-launches-payshap-request-for-instant-mobile-payments/)).
- Embedded credit through partners: SME funding with Lula in the Merchant Portal, and BNPL with Happy Pay ([Ozow blog](https://www.ozow.com/blog); [IOL, 2026-05-11](https://iol.co.za/business-report/2026-05-11-happy-pay-ozow-partner-to-expand-zero-deposit-buy-now-pay-later-across-south-africa/)).
- Fraud monitoring bought from Orca rather than built ([Launch Base Africa](https://launchbaseafrica.com/2026/03/10/stay-in-it-how-over-200-interviews-and-a-linkedin-post-led-to-a-2-35m-seed-round-for-orca/)).
- No public GitHub org was found. `ozow` returns 404 and `ozowpay` has 0 repos (`gh api orgs/...`).

**How they engineer**
- Their [tech-stack page](https://www.ozow.com/tech-stack) adds two practice points beyond the stack table already recorded: "Jira facilitates our smooth navigation through backlogs and ongoing sprints within our internal Agile workflow", and a test toolchain of Selenium, Playwright, Postman, JMeter and **k6**.
- The security posting asks to "embed security into engineering practice, pipelines, and workflows (DevSecOps)" ([Greenhouse API](https://boards-api.greenhouse.io/v1/boards/ozow/jobs?content=true)).
- Neither [Life at Ozow](https://www.ozow.com/life-at-ozow) nor the tech-stack page mentions on-call, deployment or AI practice.

**What the interview tests (first-party):** "Our process may include **psychometric and technical assessments**" (Senior Data Engineer and Senior Security Analyst postings, [Greenhouse API](https://boards-api.greenhouse.io/v1/boards/ozow/jobs?content=true)). The board now has 5 roles, 2 of them technical, against more on 2026-09-28.

**Portfolio implication:** Ozow is the one fintech whose published stack matches randmatch: ASP.NET Core, SQL Server *and* Postgres, ECS, Terraform, k6. A ledger on ECS plus RDS Postgres with Terraform, and a k6 test proving idempotency under concurrent retries, would read as "already works the way we work". **Inference.**

### Peach Payments (top candidate for "pitch")

**What they're building now**
- **RTC payouts** (2025-08-19): float top-ups from settlement or EFT, one API for bulk payments, "automated reconciliation", and batches "not held up if the merchant's bank's systems are down", with failed payments highlighted for reprocessing ([Peach](https://www.peachpayments.com/scale/peach-payments-announces-real-time-clearance-payouts/)).
- **Recon API** (2024-10-29): replaces "monthly CSV exports and manual data checks" and "outdated SFTP" with real-time discrepancy detection ([Peach](https://www.peachpayments.com/scale/revolutionising-reconciliation-think-bigger-summit-2024/)).
- 2025–26 product notes (Embedded Express wallets, PayJustNow on POS, PayDunya acquisition) come from a search summary of Peach's blog. **Secondary.**
- **GitHub:** [`peach-payments/hyperswitch`](https://github.com/peach-payments/hyperswitch) is a fork of `juspay/hyperswitch`, an open-source payments switch written in Rust. Its branches include `feat/capitec/vrp-latest` (last commit 2026-06-30, "[capitecvrp]: Add connector recipient ID"), `feat/peach-apm-connector` (2026-02-01, "add APM refunds and comprehensive tests"), `feat/refunds/from-webhook` (2026-03-11) and `hotfix-2026.06.10.0-peach` (2026-07-08, PayDunya connector). The org also forks Hyperswitch's card vault, encryption service, control centre, Helm and CDK repos (`gh api orgs/peach-payments/repos`). **Inference:** Peach is building an orchestration layer with per-acquirer connectors on Hyperswitch. Whether it is in production is **Unverified**.

**How they engineer**
- A Peach Senior Software Engineer (Full Stack) posting on the Payouts team, located in Nairobi and dated 2026-07-28, names:
  - TypeScript and Python.
  - "AWS (primarily Lambda, API Gateway, S3 and Serverless)".
  - Postgres, DynamoDB, MySQL and Mongo.
  - GitLab Pipelines and Cypress.
  - Grafana, Sentry and Datadog.
  - "Comfortable using AI coding tools (e.g. Cursor, Copilot, ChatGPT)".
  - "pairing, and knowledge sharing".

  **Secondary:** read on [jobwebkenya](https://jobwebkenya.com/jobs/senior-software-engineer-full-stack-peach-payments/). The `startup.jobs` copy returned 403.
- OfferZen's profile lists Terraform, Kafka and Jenkins as well ([OfferZen](https://www.offerzen.com/companies/peach-payments-1), **Secondary**).

**Interview:** not published anywhere I could read.

**Portfolio implication:** Peach's payouts product is randmatch's subject matter seen from the PSP side: float, batches, partial bank failure, failed-payment reprocessing and reconciliation. A randmatch-sim that reproduces those failure modes, and a recon that catches them, is directly legible to them. The stack is not: they would read the .NET as foreign. **Inference.**

### Stitch (alternative candidate for "pitch")

**What they're building now**
- **Omnichannel reconciliation** (2025-04): "a single, standardised report, in a single format" across channels, payment methods and banks. It is delivered by "SFTP, S3 buckets, or secure hosted storage" or a **Settlement API**, with monitoring that "continuously tracks reconciliation data" and alerts ([Stitch](https://stitch.money/blog/how-stitch-streamlines-omnichannel-reconciliation)).
- **PayShap Request with smart routing** (2026-08): "active connections to multiple acquirers at once"; transactions route "based on real-time availability, performance and success rates" ([Stitch](https://stitch.money/blog/stitch-offers-payshap-request-with-redundancies-smart-routing)).
- PayShap context: more than R100bn over 136m transactions since launch, 12 banks, a R50,000 cap ([Stitch](https://stitch.money/blog/real-time-payments-in-south-africa-the-state-of-payshap-in-2026)).
- **GitHub** ([stitch-money](https://github.com/stitch-money)) has 2025 forks of Debezium and `transfer` (CDC to warehouses). **Inference:** CDC-based data replication. Its `tech-radar` fork still carries Zalando's default radar data (ZMON, Skipper, Nakadi), so **it is not evidence of Stitch's choices. Don't cite it.**

**How they engineer**
- The **Payouts deep dive** describes:
  - A monorepo.
  - A "Money Movement Engine" with an API and BullMQ workers.
  - Batch payout instruction files uploaded host-to-host over SFTP.
  - Three file types: instructions, **reply files** (accept or reject) and **statement files**, in "MT940, XML, and others".
  - Statement files with "millions of line items … parsed in chunks" in parallel.

  ([Stitch](https://stitch.money/blog/technical-deep-dive-payouts-at-stitch))
- **Testing:** a hackathon ("Stitch Labs") produced Codespaces replicas of the local Kubernetes environment, built on Kind, Tilt, Helm and Traefik, so a PR can spin one up "in about 10 minutes" ([Stitch, 2025-02-10](https://stitch.money/blog/implementing-codespaces-to-thoroughly-test-at-stitch)).

**Interview:** no engineering roles open (Workable, 2026-09-28 file).

**Portfolio implication:** Stitch's three-file payout model (instruction, reply, statement) is the most concrete public description of SA payout plumbing. randmatch-sim should generate all three, with planted breaks *between* them, such as a reply-file rejection with no matching statement line. **Inference.**

### Orca Fraud ("ocra")

**What they're building now**
- Real-time transaction monitoring "embedded directly into payment flows".
- Anomaly detection, network analysis of linked identities (cards, phones, accounts, fingerprints) and real-time account profiles.
- A rules engine.
- Claimed "integration time: hours".
- "5bn+ monthly transactions monitored", "99.99% uptime", Ozow case study.

([orca-fraud.com](https://www.orca-fraud.com))

AML Intelligence: "adaptive intelligence directly into live payment flows" ([AML Intelligence, 2026-03](https://www.amlintelligence.com/2026/03/news-orca-fraud-raises-2-35m-to-scale-real-time-fraud-intelligence-tech/)).

**How they engineer:** two engineer founders and a small team. Pillay: "finding world-class engineering talent in Cape Town when US and European companies are fishing in the same pool has proven to be exceptionally hard" ([Launch Base Africa](https://launchbaseafrica.com/2026/03/10/stay-in-it-how-over-200-interviews-and-a-linkedin-post-led-to-a-2-35m-seed-round-for-orca/)). Stack, practices and interview are **not published**. The careers page is 404, and the [`orcafraud`](https://github.com/orcafraud) GitHub org has 0 public repos.

**Portfolio implication:** Orca is a fraud company, not a reconciliation company. Per `2026-09-23-fraud-and-bank-apis.md`, don't chase fraud ML. What would interest a small, senior, real-time team is evidence of latency-aware, replay-deterministic event handling, and the ledger's outbox stream is exactly that. **Inference.**

### iKhokha

**What they're building now:** card machines (iK Flyer, Tap on Phone), payment links, gateway and webstore, iK POS, cash advance and prepaid ([iKhokha careers](https://www.ikhokha.com/careers)). Its GitHub has `ber-tlv` (2025-11) and `octet-buffer` (2026-01) in TypeScript. **Inference:** EMV TLV parsing for card-present work. It also has a new `microservices-wiki` (2026-07), a Mintlify docs starter whose README tells you to install the docs skill for "Claude Code, Cursor, Windsurf" ([github.com/ikhokha](https://github.com/ikhokha)).

**How they engineer** (Senior Software Engineer posting, released 2026-08-31, [SmartRecruiters API](https://api.smartrecruiters.com/v1/companies/iKhokha/postings/744000146477539)):
- "Participate in and drive high-quality code reviews".
- "Design Patterns" and "Solid Principles".
- Layered architecture ("Presentation, Application, Service, Integration and Database layers").
- "Serverless compute (e.g. AWS Lambda …)".
- "Telemetry Integration (Datadog, or similar)".
- "Scrum or Kanban".
- "Take ownership of systems in production, including monitoring, troubleshooting".

The SDM posting asks for "frequent and faster deployments" ([SmartRecruiters API](https://api.smartrecruiters.com/v1/companies/iKhokha/postings/744000146475750)). No AI tools are named.

**What the interview tests (first-party)**
- The careers page lists five steps: application review, first interview ("skills assessment"), cultural interview "with senior leadership exposure", offer, onboarding ([iKhokha careers](https://www.ikhokha.com/careers)).
- Their **public tech check** [`ikhokha/tech-check-fullstack`](https://github.com/ikhokha/tech-check-fullstack) (2022, Java) has three tasks:
  1. Debug a report that "only shows the last day's comments" and undercounts multi-product comments.
  2. Refactor the matcher to be "extensible/pluggable" and add new metrics.
  3. Process files concurrently, with the bonus caveat that "thousands of comment files … might crash the app if we spawn threads uncontrollably".

  **Unverified** whether it is still in use.

**Portfolio implication:** iKhokha tests debugging, open/closed extensibility and **bounded** concurrency. randmatch-recon's matcher should be pluggable (one rule per break type, added without editing a switch). Its ingestion should process PSP files with a bounded degree of parallelism, with a test that proves the bound. **Inference.**

### Luno

**What they're building now**
- Restructured in July 2026: cut "20% of global workforce" and is scaling B2B. Discovery Bank is named as an institutional partner. CEO James Lanigan: "material investments in automation … rapidly changing the resource model" ([BusinessTech, 2026-07-28](https://businesstech.co.za/news/finance/867780/south-african-crypto-giant-cutting-20-of-jobs/)).
- **ZARU**, a rand stablecoin consortium led by Luno with Sanlam, Standard Bank (custody), EasyEquities and Lesaka. Reserves are audited monthly by Moore Johannesburg ([Daily Maverick, 2026-02-08](https://www.dailymaverick.co.za/article/2026-02-08-this-might-be-the-randbacked-stablecoin-weve-been-waiting-for/)).
- **The richest public GitHub org on the list** ([github.com/luno](https://github.com/luno), all pushed in the last week):
  - [`workflow`](https://github.com/luno/workflow) (259 stars): "type-safe, event-driven workflow orchestration" in Go, with state machines, Kafka streamer, SQL store, **`outbox.go`**, automatic retries and topics including `idempotent` and `tdd`.
  - `reflex` (event streaming) and `shift` (FSM persistence).
  - `rink` (role scheduling on etcd) and `jettison` (structured errors over gRPC).
  - [`luno-mcp`](https://github.com/luno/luno-mcp) (2025-05): an MCP server documented for Claude Code, VS Code and Cursor, with SonarCloud gates.

**How they engineer**
- [`spec-kit-plan-review-gate`](https://github.com/luno/spec-kit-plan-review-gate) (2026-03): blocks `/speckit.tasks` unless "`spec.md` and `plan.md` have been merged to the default branch via a merge request".
- [`spec-kit-preset-jira`](https://github.com/luno/spec-kit-preset-jira) (2026-04): turns `tasks.md` into Jira epics, stories and blocking links, including a "Claude Code plugin" path.
- **Inference:** Luno runs spec-driven AI development with a human review gate on the spec and plan, and keeps Jira as the system of record.
- Org structure is "Fleets" and "Pods" (**Secondary**, search summary).

**What the interview tests:** no first-party description; `luno.com/en/careers` returned 404. Glassdoor summaries mention a 1.5-hour live-coding session with three developers (**Secondary**; Glassdoor returned 403). Greenhouse has 1 role, a non-engineering OTC Trader ([Greenhouse API](https://boards-api.greenhouse.io/v1/boards/luno/jobs?content=true)).

**Portfolio implication:** Luno open-sourced the exact pattern randmatch-sim uses (outbox into Kafka with idempotent state-machine steps), and the exact AI workflow (spec, then plan, then PR-gated tasks). Mirroring both, and citing `luno/workflow` in an ADR as prior art, is the strongest single signal you could send them. The Go gap remains. **Inference.**

---

## 2. The consultancies

### DVT (Johannesburg)

**What they're building now:** "AI Build Teams" are the headline offer: "AI-augmented teams with expert oversight that ship production-grade code faster" ([dvtsoftware.com](https://www.dvtsoftware.com); [AI services](https://www.dvtsoftware.com/services/artificial-intelligence)). The Clippd case study gives a "fixed 13-week window", **"spec-driven development … clear, testable specifications before development began"**, and "experienced specialists retained responsibility for architecture, quality and delivery decisions". It also reports that feature preparation "took 48 hours" in sprint one and "eight hours" by the end ([DVT case study](https://dvt.co.za/case-study-clippd-2026)). Financial-services case studies include an ATM operational-monitoring solution and a loans management system ([case studies](https://www.dvtsoftware.com/news-insights/case-studies)). GitHub has a series of `ai-assessment-tool-test-*` repos (2024-09 to 2025-07) across Jakarta EE, Spring Boot, Quarkus and Helidon ([github.com/dvt](https://github.com/dvt)). **Inference:** test fixtures for an AI legacy-assessment tool.

**How they engineer:** the open roles are mostly Johannesburg and Gauteng: AI Architect, AWS Platform Engineer, Azure Cloud Security, Data Engineering Lead, Java Lead, Lead Full Stack AI Python Developer, Microsoft DevOps, and Senior .NET/Vue Full Stack ([DVT careers](https://dvtcareers.recruitee.com)). The .NET/Vue role asks for:
- .NET/C# with 7+ years.
- "Azure (preferred) or AWS".
- Docker, Kubernetes and Azure DevOps.
- xUnit/NUnit and integration testing.
- Clean Architecture.
- "GitHub Copilot or AI-assisted development" (nice-to-have).

([posting](https://dvtcareers.recruitee.com/o/senior-net-vue-full-stack-developer-cape-town)). Its title says Cape Town but the board lists it as Johannesburg.

**What the interview tests (first-party):** "From the initial screening call to the **technical challenge**, interview, and offer stage; you will be provided with feedback at every turn" ([DVT careers](https://dvtcareers.recruitee.com)). Search summaries add a challenge "in a language of their choice", a ".NET coding challenge" on HackerRank or as a take-home, and a panel on architecture and ".NET best practices" (**Secondary**; Glassdoor 403).

**Portfolio implication:** DVT sells spec-driven, AI-augmented delivery to clients. A repo whose history shows spec, then testable acceptance criteria, then AI-assisted implementation, then human-reviewed PRs is a portfolio version of their pitch. Expect a take-home: a clean README, tests and a short "decisions" section are what a feedback-giving reviewer reads first. **Inference.**

### Synthesis Software Technologies

**What they're building now**
- Synthesis is part of **Araxi** (formerly Capital Appreciation), which completed a R1bn acquisition of Pay@ in May 2026 and reports "payments processing and software solutions" divisions ([BusinessDay, 2026-05-11](https://www.businessday.co.za/companies/2026-05-11-araxi-concludes-r1bn-takeover-of-pay/)).
- It is an "AWS Advanced Consulting Partner". Its lines are RegTech (Regstream, TXstream), a Payments CoE, SoftPOS, Cryptography and "AI Launchpad" ([synthesis.co.za](https://www.synthesis.co.za/)).
- It claims a PayShap project with "sub-5-second transaction times" on "modular, API-driven platforms that support ISO 20022", and a BankservAfrica cloud migration; clients are unnamed ([Synthesis](https://www.synthesis.co.za/from-legacy-to-cloud-synthesis-architects-the-digital-core-of-modern-banking/)).
- Oracle-to-AWS and VMware-to-AWS migration offers (2025) ([articles](https://www.synthesis.co.za/articles/)).

**How they engineer: the strongest first-party AI-practice evidence in this file.** The GitHub repo [`synthesis-software-technologies/techteam-content`](https://github.com/synthesis-software-technologies/techteam-content) (created 2026-04) holds three documents. The GitHub Pages renders came back empty to the fetcher, so the sources were read through `gh api`.

- **"AI Maturity Levels — A Field Guide"** (v1.0, 2026, owner "Technology Office"). It defines five levels:
  - **L2 Selective**: "AI not yet wired into CI/CD or PR review gates".
  - **L3 Integrated**: "specialist sub-agents handling discrete tasks: requirements analysis, test generation, code review, security scanning, and documentation"; "each agent handoff is defined, observable, and repeatable"; "Tracks and reports measurable gains — sprint velocity, defect rates, review turnaround, and time-to-deploy … you can prove it with numbers".
  - **L4 Strategic**: seniors "Own the AI toolchain standards for their squad … set the quality bar for AI-generated output"; principals "ensur[e] every agent deployment has safety, observability, and escalation built in by design".
- **Code Connect Summit keynote** (Tom Wells, 2026-06-05):
  - "Everything is a Pipeline. So treat it like a codebase."
  - "Every step traceable, diffable, reviewable."
  - "Humans in the loop (maybe thru PRs, quality gates, etc)."
  - "Claude Code + Git + Skills".
  - A Kotlin CQRS/event-sourcing aggregate: "4 pure functions describe a full CQRS write & read abstraction".
- **Tech Update, Sept 2026**:
  - "Agentic development is real."
  - "Software design matters! … counts for more now."
  - "Agents assisting humans → Humans assisting agentic teams."
  - "Reporting must be automated and repeatable. No manual human work."

**What the interview tests:** not first-party. `synthesis.co.za/careers/` returned 404. [Our People](https://www.synthesis.co.za/our-people/) points to `synthesis.simplify.hr`, which shows "no open jobs". A Glassdoor summary describes coding "a solution for a simple made-up scenario" and three interviews (**Secondary**).

**Portfolio implication:** Synthesis effectively published the rubric. A repo that shows L3 behaviour wins here: defined agent roles (spec reviewer, test writer, code reviewer, security scan), observable handoffs (PR comments, CI logs) and numbers (review turnaround, defects caught by evals). An event-sourced ledger with pure decide/evolve functions also echoes their own keynote. **Inference.**

### Entelect

**What they're building now**
- End-to-end delivery for "Banking, Financial Services, Insurance …".
- Case studies with Capitec, Investec, FNB, Old Mutual and Sanlam.
- AWS, Azure and Backbase partnerships ([entelect.co.za](https://www.entelect.co.za)).
- "Premier partner for Backbase in Southern Africa", running bank digital-banking rollouts ([Entelect](https://entelect.co.za/entelects-premier-partnership-with-backbase/)).
- GitHub ([github.com/entelect](https://github.com/entelect)): `spring-incubator` (2026-02), an `azure-openai-rag-workshop-java` fork (2025-02), an empty `kyber` (2026-04), and older Java, .NET and Go incubators and "Dojo" repos (BDD, message queues, unit testing, IaC). **Inference:** they train internally in kata and dojo form.

**How they engineer**
- Open roles span Java, JavaScript, Mobile, .NET and Salesforce at Intermediate, Senior, Tech Lead and Team Lead levels ([positions](https://culture.entelect.co.za/current-available-positions/)).
- The career ladder uses role titles: Software Engineer "The Commando", Tech Lead "The Technologist", Team Lead "The Commodore", Development Manager "The Centurion" ([culture site](https://culture.entelect.co.za/)).
- The graduate programme is a 10-week bootcamp. There is a "Credit and Criminal check … due to the sensitivity of the data and systems we work with" ([graduate programme](https://culture.entelect.co.za/the-entelect-graduate-programme/)).
- Senior .NET asks for .NET, JavaScript and **Angular** as must-haves, and AWS, Azure, React and EF as nice-to-haves (**Secondary**, search summary; the OfferZen posting is 404).

**What the interview tests:** no first-party description; `entelect.co.za/careers` is 404. Search summaries describe:
- An online technical interview.
- A group collaboration day.
- A leadership 1:1.
- "SOLID principles are assessed through a live code review".
- System-design discussion.

(**Secondary**; Glassdoor 403.)

**Portfolio implication:** expect to defend your own code live. Pick one randmatch class with a real SOLID story (the pluggable break-rule set) and be ready to refactor it in front of someone. Angular is a gap for Entelect's .NET roles, as it was for Investec in the 2026-09-28 addendum. **Inference.**

---

## 3. The big corporates

| Bank | Building now (2025–26) | How they engineer | Source |
|---|---|---|---|
| **Standard Bank** | 78% of migratable compute in cloud by H1 2026; enterprise AI on **Amazon Bedrock**, "deliberate multi-model"; 72% of staff active GenAI users; about 1/3 of technology staff on AI coding tools, "approximately 20%" productivity | **SAFe is live**: two "Release Train Engineer" postings released 2026-09-28, "Guide the team through PI Planning … SAFe 4 framework". Software Engineer template (2026-09-29): "Agile Engineering, API Engineering, Automation, Cloud Computing, Continuous Delivery". Earlier AWS preferred-cloud deal; SAP banking on Azure | [Standard Bank press release, 2026-08-25](https://www.standardbank.com/sbg/standard-bank-group/newsroom/press-releases/weve-positioned-ai-as-long-term-competitive-capability); [TechCentral, 2026-08-17](https://techcentral.co.za/inside-standard-banks-multi-model-ai-bet/284924/); [RTE posting](https://api.smartrecruiters.com/v1/companies/StandardBankGroup/postings/744000152157299); [SE posting](https://api.smartrecruiters.com/v1/companies/StandardBankGroup/postings/744000152450669); [FinTech Futures](https://www.fintechfutures.com/partnerships/standard-bank-extends-microsoft-partnership-to-boost-cloud-migration) |
| **Absa** | AWS made "preferred cloud provider" (2025-09-08); Amazon Connect contact centre; agentic chatbot (1.6m users) | **"1,400+ developers" on GitHub Copilot and Anthropic's Claude Code**; 30,000+ on M365 Copilot; 3,800+ staff-built agents in production. No productivity number disclosed | [Absa media statement](https://www.absa.africa/media-statements/2025/absa-group-collaborates-with-amazon-web-services/); [TechCentral, 2026-08-19](https://techcentral.co.za/absas-ai-is-writing-its-code-and-answering-its-calls/285065/) |
| **FNB / FirstRand** | Core banking moving to Fiserv Finxact (cloud-native core); presented at AWS Summit Johannesburg (2026-08-19) | **About 3,000 engineers on AI coding tools.** CDO Kevin Mitchell: tools grounded on "functional requirements, test plans, architecture standards and security controls"; "AI can accelerate the work, but it does not determine the outcome"; rolled out through workshops on real projects | [Sowetan, 2026-08-19](https://www.sowetan.co.za/news/2026-08-19-watch-this-is-how-firstrand-is-using-ai-to-help-its-3000-engineers-work-faster-and-better/); [Finextra](https://www.finextra.com/pressarticle/104240/firstrand-group-signs-for-finxact-from-fiserv); [AWS Summit agenda](https://aws.amazon.com/events/summits/johannesburg/agenda) |
| **Nedbank** | **Managed Evolution "fundamentally completed" end-2024.** Next: "accelerating our cloud migration strategy", and an "enterprise payment service hub … fully componentised and cloud-enabled"; NIHA AI programme over R375m annualised value (H1 2026) | **GitHub Copilot for "more than 980 developers"**; M365 Copilot rolled out. Azure-first (Microsoft partnership) | [Nedbank 2024 annual results booklet](https://group.nedbank.co.za/content/dam/group/pdf/20_financial-results/2024/annual-results/2024-annual-results-booklet-nedbank.pdf) (parsed with `pdftotext`); [ITWeb, 2026-08-04](https://www.itweb.co.za/article/nedbanks-ai-strategy-unlocks-r375m-in-value/Pero3MZ3J5AqQb6m); [Microsoft](https://news.microsoft.com/source/features/digital-transformation/nedbank-speeds-toward-a-digital-future/) |
| **Capitec** | R6.3bn replatforming over three years, "systems moved to Amazon Web Services"; cloud fees up 39% | **Open source on GitHub**: [`capitec/pg-proxy`](https://github.com/capitec/pg-proxy) (Go, pushed 2026-07) does "AI-powered query efficiency analysis via Portkey LLM gateway (**Claude on AWS Bedrock**)", "Data Masking", "Audit Trail: JWT user identity injected into `application_name`", RDS IAM auth and Kubernetes probes. [`capitec/dsp-decision-engine`](https://github.com/capitec/dsp-decision-engine) (Python, pushed 2026-10-01) is "decision pipelines as versioned, deployable micro-services", with "Versioned configs … hot-swappable without redeployment". 2026-09-28 file: a Linux lead posting lists "AI (Claude Code)" | [BusinessDay, 2025-04-30](https://www.businessday.co.za/bd/companies/financial-services/2025-04-30-capitec-beefs-up-tech-strategy-with-new-recruits/); [The Banking Brief](https://the-banking-brief.beehiiv.com/p/capitec-scales-ai-and-headcount-in-parallel) (**Secondary**: AI to 5,000 staff, agentic AI in business credit) |
| **Investec** | Microsoft Copilot for all 8,000 staff, "800+ AI agents" (2026-06-24); Programmable Banking community active: [`investec-dev-quest`](https://github.com/investec-developer-community/investec-dev-quest) (v2, pushed 2026-10-01), with "replay protection, SSRF-safe callbacks, tamper-evident audit logs"; [`ai-sandbox`](https://github.com/investec-developer-community/ai-sandbox) is a mock API "with … chaos testing"; DevConf 2026 sponsor | Azure: [`investec/home-run`](https://github.com/investec/home-run), "local development environments for Azure apps", TypeScript strict, Codecov. Postings (2026-09-29 addendum): C#, OAuth2/OIDC, Azure DevOps, Angular | [TechCentral, 2026-06-24](https://techcentral.co.za/investec-deploying-ai-tools-to-every-employee/282997/); [DevConf](https://www.devconf.co.za/) |
| **Discovery Bank** | Discovery AI assistant (pay by photographing an invoice; about 55% first-contact resolution); TRUST Alert, "85% decline in confirmed fraud" (2026-05-14) | **Azure**: Databricks, ADF, Container Apps, APIM, Event Hubs, Azure OpenAI, Azure DevOps (case study 2025-04-23). Group CIO Derek Wilcocks: 20–25% measured from AI coding assistants, but going slow on agents because of "explainability … efficiency … maintainability"; the winners build "the harness" | [Microsoft case study](https://www.microsoft.com/en/customers/story/23562-discovery-bank-azure); [Discovery press release](https://www.mynewsdesk.com/za/discovery-holdings-ltd/pressreleases/discovery-bank-says-ai-driven-security-has-stopped-estimated-r100m-in-fraud-as-it-rolls-out-enhanced-security-ai-powered-payments-and-dstv-rewards-3448437); [TechCentral, 2026-08-06](https://techcentral.co.za/why-discovery-is-going-slow-on-ai-coding-agents/284618/) |

**What bank interviews test:** no bank publishes an engineering interview process that I could reach. The 2026-09-28 file's warning stands: bank adverts are templates. The usable first-party signals are conditions: Capitec's "clear criminal and credit record" and Entelect's credit and criminal check for bank work, plus the practices above.

---

## 4. Synthesis table

| Company | What they're building now | How they engineer | What they'd value in a portfolio | Source |
|---|---|---|---|---|
| Ozow | PayShap Request; embedded BNPL and SME credit; fraud via Orca | ASP.NET Core, SQL Server and Postgres, ECS, Terraform, k6; Jira sprints; DevSecOps; psychometric and technical assessments | .NET ledger on ECS and RDS with Terraform; k6 idempotency load test; secure webhook handling | [tech stack](https://www.ozow.com/tech-stack), [Greenhouse](https://boards-api.greenhouse.io/v1/boards/ozow/jobs?content=true) |
| Peach | RTC payouts with float and automated recon; Recon API; Hyperswitch connectors (**Inference**) | TS and Python, AWS Lambda; GitLab CI, Cypress; Datadog and Sentry; AI tools expected; pairing | Payout-batch failure modes reproduced and reconciled; connector-per-PSP design | [RTC](https://www.peachpayments.com/scale/peach-payments-announces-real-time-clearance-payouts/), [fork](https://github.com/peach-payments/hyperswitch) |
| Stitch | Omnichannel recon reports and Settlement API; multi-acquirer PayShap routing | TS monorepo, BullMQ, K8s, Tilt, Codespaces, hackathons | Instruction, reply and statement file model; parallel chunked statement parsing | [recon](https://stitch.money/blog/how-stitch-streamlines-omnichannel-reconciliation), [payouts](https://stitch.money/blog/technical-deep-dive-payouts-at-stitch) |
| Orca | Real-time fraud scoring in payment flows | Small senior team; nothing published | Low-latency, replayable event handling; honest non-claims about fraud ML | [orca-fraud.com](https://www.orca-fraud.com) |
| iKhokha | Card machines, Tap on Phone, TLV parsing, gateway | Node and TS, Lambda, DynamoDB, Datadog; SOLID, layered; production ownership | Pluggable matcher; bounded concurrency; debugging story | [posting](https://api.smartrecruiters.com/v1/companies/iKhokha/postings/744000146477539), [tech check](https://github.com/ikhokha/tech-check-fullstack) |
| Luno | B2B crypto and ZARU stablecoin; MCP server | Go, event-driven, outbox, FSMs; Spec Kit with PR gate and Jira | Outbox → Kafka idempotent workflow; spec and plan merged before tasks | [workflow](https://github.com/luno/workflow), [gate](https://github.com/luno/spec-kit-plan-review-gate) |
| DVT | AI Build Teams; bank ops and loans systems | Spec-driven, AI-augmented, humans own architecture; technical challenge with feedback | Spec → tests → AI-assisted PR trail; clean take-home habits | [Clippd](https://dvt.co.za/case-study-clippd-2026), [careers](https://dvtcareers.recruitee.com) |
| Synthesis | Payments CoE, PayShap and ISO 20022, RegTech; Araxi plus Pay@ | AI maturity L0–L4; "everything is a pipeline"; Kotlin CQRS | L3 evidence: defined agent roles, observable handoffs, measured gains | [techteam-content](https://github.com/synthesis-software-technologies/techteam-content) |
| Entelect | Bank delivery (Capitec, Investec, FNB); Backbase | Dojos and incubators; live SOLID code review (**Secondary**) | Code you can defend live; Angular for .NET roles | [entelect.co.za](https://www.entelect.co.za), [culture](https://culture.entelect.co.za/) |
| Standard Bank | 78% cloud; Bedrock multi-model AI | SAFe ARTs and PI Planning; about 1/3 of tech staff on AI coding tools | Governed multi-model AI; API and CD vocabulary | [press release](https://www.standardbank.com/sbg/standard-bank-group/newsroom/press-releases/weve-positioned-ai-as-long-term-competitive-capability) |
| Absa | AWS preferred; agentic chatbot | 1,400+ devs on Copilot and Claude Code | AI-assisted work with a visible review trail | [TechCentral](https://techcentral.co.za/absas-ai-is-writing-its-code-and-answering-its-calls/285065/) |
| FirstRand | Finxact core; AI for 3,000 engineers | Specs, test plans and standards as AI grounding; human accountability | Specs and test plans in the repo that an agent demonstrably used | [Sowetan](https://www.sowetan.co.za/news/2026-08-19-watch-this-is-how-firstrand-is-using-ai-to-help-its-3000-engineers-work-faster-and-better/) |
| Nedbank | Payment service hub; cloud migration; NIHA | Azure; Copilot for 980+ devs | Payments hub vocabulary; Azure plus SQL Server | [results booklet](https://group.nedbank.co.za/content/dam/group/pdf/20_financial-results/2024/annual-results/2024-annual-results-booklet-nedbank.pdf) |
| Capitec | AWS replatform; AI in credit and fraud | Go and Python OSS; Claude on Bedrock; masking and audit trail | PII masking before LLM calls; audited model use; versioned rule configs | [pg-proxy](https://github.com/capitec/pg-proxy), [decider](https://github.com/capitec/dsp-decision-engine) |
| Investec | Copilot for 8,000; Programmable Banking community | Azure, C#, Angular; security-first dev quests | Replay protection, SSRF-safe callbacks, tamper-evident audit log | [dev quest](https://github.com/investec-developer-community/investec-dev-quest) |
| Discovery Bank | Discovery AI payments; TRUST Alert | Azure, Databricks; constrained agents ("the harness") | Constrained, explainable AI with evals | [TechCentral](https://techcentral.co.za/why-discovery-is-going-slow-on-ai-coding-agents/284618/) |

---

## 5. Patterns

**Banks**
- **Cloud:** AWS is preferred at Absa and Capitec. Standard Bank runs AWS plus Azure, with AI on Bedrock. Nedbank, Discovery and Investec are Azure.
- **AI coding tools at scale, always framed as governed.** "Human first" (Investec), "does not determine the outcome" (FirstRand), "the harness" (Discovery), "govern … open or closed models" (Standard Bank).
- **Claude is named inside two banks.** Absa uses Claude Code for developers. Capitec runs Claude on Bedrock in OSS tooling.
- **SAFe is real at Standard Bank.** This corrects `2026-09-29-curriculum-sources.md`, which found SAFe in none of 48 recruiter-board postings. The difference is the source: bank ATSs against E-Merge.
- **Payments modernisation is the bank-side twin of randmatch:** Nedbank's hub, FirstRand's Finxact core, and Standard Bank's payments focus area.

**Startups**
- Small teams on AWS with a non-.NET language: TS (Peach, Stitch, iKhokha), Go (Luno), Rust (Peach's Hyperswitch work).
- Product velocity and ownership: "take ownership of systems in production" (iKhokha), hackathons (Stitch).
- They open-source infrastructure patterns (Luno) and expect AI tool fluency (Peach).
- Reconciliation, payouts and routing are **products** they sell, not back-office chores.

**Consultancies**
- They sell AI-augmented, spec-driven delivery (DVT AI Build Teams, Synthesis L3/L4) on both clouds.
- They assess candidates directly: technical challenge (DVT), live SOLID review and group day (Entelect, **Secondary**), a coded scenario (Synthesis, **Secondary**).
- Breadth and client communication are the implicit filter.
- They're the main Johannesburg .NET buyers, alongside Investec and Nedbank. **Inference.**

---

## 6. Fit test for randmatch, bluntly

**Does it match what they build?**
- **PSPs and payments consultancies: yes.** Peach, Stitch, Ozow and Synthesis's Payments CoE all build the thing randmatch reconciles, and two of them sell reconciliation itself.
- **Banks: partly.** Their payments hubs and core moves need the same correctness thinking. A bank reviewer reads it as domain literacy, not as their product.
- **Orca: mostly no.** It is fraud. Don't stretch the pitch.

**What's wrong or missing**

1. **The simulator emits the wrong shapes if it only emits CSV exports.** Real SA payout plumbing has three file types (instruction, reply, statement) in formats such as MT940 and XML, plus Settlement-API reads and SFTP/S3 delivery (Stitch). It also has floats, batches and per-bank partial failure (Peach). Plant breaks **between** these:
   - A payout rejected in the reply file but booked as paid.
   - A statement credit with no instruction.
   - A batch partly failed because one bank was down.
   - A refund that arrives only by webhook (Peach's `refunds/from-webhook` branch).
   - A fee netted from settlement.
   - A duplicate or out-of-order webhook.
   - A settlement cut-off timing break.
2. **The cloud.** Fintechs read "Azure-only" as "not us". **Deploy one component on AWS, and make it `randmatch-ledger`:** ASP.NET Core on ECS Fargate, RDS Postgres, Terraform, k6. That is Ozow's own stack page line for line. Keep `randmatch-recon` on SQL Server/Azure for the Investec, Nedbank and Discovery audience. Have `randmatch-sim` drop files to S3, as Stitch delivers reports, so the AWS piece is load-bearing rather than decorative. The deployment cost of ECS plus RDS is **Unverified**; check it before committing.
3. **Language.** Don't rewrite anything. C# is the right core: Ozow, the Azure banks, Entelect and DVT. **Optional and considered:** `randmatch-sim` is the one component where TypeScript on Lambda would be legible to Peach, iKhokha and Stitch at low risk, because it's a generator and not the correctness core. That is the user's call. The cost is a second toolchain.
4. **The AI break-explainer has to look like the banks' AI, not a demo:**
   - Provider-agnostic behind `IChatClient`, with Bedrock as one backend. Standard Bank and Capitec both route through Bedrock.
   - PII and reference masking before any prompt (Capitec `pg-proxy`).
   - An audit row for every model call: who, what, model, tokens, decision.
   - Evals as a CI gate.
   - It **cannot** post an adjustment. A human approves (FirstRand, Investec, Discovery).

   The MCP server holds up: Luno ships one, and Investec's sandbox targets AI assistants.
5. **Security features that are cheap and on-message:** signed webhooks with timestamp and nonce replay protection, SSRF-safe callback registration, and a hash-chained, tamper-evident audit log. These are Investec dev-quest Season 3 topics, and an outbox stream already gives you the ordering.
6. **Prior art, cited.** Put `luno/workflow` (outbox, idempotent FSM steps) and Stitch's payout file model in the ADRs as references. Showing you know how SA teams solved it is itself a signal. **Inference.**

---

## 7. Workflow evidence the repos should carry

Each item is mapped to the employer practice it mirrors.

| Evidence | Mirrors | Concretely |
|---|---|---|
| **Spec, then plan, merged by PR before implementation** | Luno plan-review gate; DVT spec-driven; FirstRand "quality of … specifications" | `specs/<feature>/spec.md` and `plan.md` in their own merged PR, then implementation PRs that link back to them |
| **ADRs** | Synthesis "every step traceable"; consultancy design defence | MADR files for: cloud split (Azure recon / AWS ledger), outbox over dual-write, matching-rule plugin design, LLM provider abstraction |
| **Tests that encode invariants** | iKhokha tech check; Ozow k6; Stitch Codespaces | Property tests (journals net to zero); concurrency test on idempotency keys; bounded-parallelism test on file ingestion; k6 script against the deployed ledger |
| **AI-review trail at Synthesis L3** | Synthesis maturity guide; Absa and FirstRand scale; Discovery harness | Named agent roles in `AGENTS.md`/`CLAUDE.md` (spec reviewer, test writer, code reviewer, security scan); PR comments showing human accept or reject of AI suggestions; a short metrics note in the README (review turnaround, eval pass rate, defects caught pre-merge) |
| **Evals as a gate** | Discovery explainability; Standard Bank governance | CI fails if break-explanation citations don't exist or don't support the claim |
| **Postmortems** | Startup production ownership (iKhokha, Peach) | One blameless postmortem per real incident during development, such as a webhook replay bug or an outbox stall, in a standard template |
| **Deployments as code** | Ozow Terraform; Lesaka and Capitec (2026-09-28 file) | Terraform for the AWS ledger; Bicep or Terraform for the Azure recon; a CI deploy job with environment protection |
| **Observability** | iKhokha and Peach Datadog; Discovery observability role (2026-09-28 file) | OpenTelemetry traces across sim → ledger → recon; a dashboard screenshot in the README |
| **Non-claims** | Banks' governance framing | "Synthetic data only. No cardholder data, no PCI scope. LLM never posts adjustments." |
| **Ways-of-working literacy (light)** | Standard Bank SAFe; Luno Jira preset; Ozow Jira sprints | Issues grouped into epics with dependencies. Don't simulate PI Planning |

**Interview preparation this implies:**
- Defend one class's SOLID design live (Entelect, **Secondary**).
- Explain bounded concurrency (iKhokha).
- Be ready for a feedback-reviewed take-home in .NET (DVT).
- Expect psychometrics (Ozow, first-party).
- For Luno and Synthesis, be able to walk the spec → plan → PR trail.

---

## 8. Corrections to earlier files

- **SAFe:** `2026-09-29-curriculum-sources.md` found "Kanban, SAFe: 0". Standard Bank has two open SAFe RTE postings dated 2026-09-28. Agency boards under-count bank ways of working.
- **Azure is wider than "only Nedbank" in banking.** That was `2026-09-28` finding 2. Discovery Bank (Microsoft case study, 2025-04-23) and Investec (postings and `home-run`) are Azure. Absa's AWS-preferred statement (2025-09-08) strengthens the AWS side.
- **AI coding tools are a bank-scale reality, not just a recruiter-posting mention.** The 980 / 1,400 / about 1/3 of tech staff / 3,000 figures above update the "8 of 39 postings" framing in `2026-09-29-curriculum-sources.md`.
- **Ozow's board shrank** to 5 roles, 2 technical. **Luno** cut 20% of staff in July 2026; its board is still non-engineering.
- **Don't cite `stitch-money/tech-radar`.** It is unmodified Zalando data.

---

## 9. Could not fetch or verify

- `orcafraud.com` redirects to a parked-domain page. `orca-fraud.com/careers` returned 404.
- `synthesis.co.za/careers/`, `entelect.co.za/careers`, `luno.com/en/careers` and the OfferZen Entelect posting all returned 404.
- `startup.jobs` (Peach), all Glassdoor pages, and newsghana returned 403. Interview claims from those sources are search-summary level and labelled **Secondary**.
- The Synthesis GitHub Pages decks rendered empty. I read their sources through `gh api`.
- DevConf 2026 agendas showed "Loading…" placeholders. Only the sponsors were confirmed: Entelect, Luno, Investec Developer and DVT ([devconf.co.za](https://www.devconf.co.za/)).
- The AWS Summit Johannesburg agenda listed no bank or fintech speakers at read time. FirstRand's appearance comes from Sowetan.
- `capitec.github.io/open-source` rendered empty.
- No GitHub org was found for Ozow, Standard Bank, FNB or Discovery. `ozowpay`, `absa`, `absa-group` and `nedbank` exist with 0 public repos.
- **Unverified:** whether Peach's Hyperswitch connectors are in production; Capitec's primary-source annual report wording (cited through BusinessDay); Entelect's, Luno's and Synthesis's current interview formats.

---

## Sources

Read 2026-10-01 unless noted. Carried-over context comes from `research/2026-09-28-sa-fintech-target-roles.md`, `research/2026-09-23-fraud-and-bank-apis.md` and `research/2026-09-29-curriculum-sources.md`.

**Name resolution and fintechs**
- Orca Fraud: [Launch Base Africa, 2026-03-10](https://launchbaseafrica.com/2026/03/10/stay-in-it-how-over-200-interviews-and-a-linkedin-post-led-to-a-2-35m-seed-round-for-orca/) · [AML Intelligence](https://www.amlintelligence.com/2026/03/news-orca-fraud-raises-2-35m-to-scale-real-time-fraud-intelligence-tech/) · [orca-fraud.com](https://www.orca-fraud.com)
- Stitch: [omnichannel reconciliation](https://stitch.money/blog/how-stitch-streamlines-omnichannel-reconciliation) · [payouts deep dive](https://stitch.money/blog/technical-deep-dive-payouts-at-stitch) · [Codespaces](https://stitch.money/blog/implementing-codespaces-to-thoroughly-test-at-stitch) · [PayShap smart routing](https://stitch.money/blog/stitch-offers-payshap-request-with-redundancies-smart-routing) · [state of PayShap 2026](https://stitch.money/blog/real-time-payments-in-south-africa-the-state-of-payshap-in-2026) · [github.com/stitch-money](https://github.com/stitch-money)
- Peach: [RTC payouts](https://www.peachpayments.com/scale/peach-payments-announces-real-time-clearance-payouts/) · [Recon API](https://www.peachpayments.com/scale/revolutionising-reconciliation-think-bigger-summit-2024/) · [peach-payments/hyperswitch](https://github.com/peach-payments/hyperswitch) · [jobwebkenya posting](https://jobwebkenya.com/jobs/senior-software-engineer-full-stack-peach-payments/) (**Secondary**) · [OfferZen profile](https://www.offerzen.com/companies/peach-payments-1) (**Secondary**)
- Ozow: [tech stack](https://www.ozow.com/tech-stack) · [Greenhouse API](https://boards-api.greenhouse.io/v1/boards/ozow/jobs?content=true) · [Life at Ozow](https://www.ozow.com/life-at-ozow) · [blog](https://www.ozow.com/blog) · [IOL, 2026-05-11](https://iol.co.za/business-report/2026-05-11-happy-pay-ozow-partner-to-expand-zero-deposit-buy-now-pay-later-across-south-africa/)
- iKhokha: [careers](https://www.ikhokha.com/careers) · [Senior SE posting](https://api.smartrecruiters.com/v1/companies/iKhokha/postings/744000146477539) · [SDM posting](https://api.smartrecruiters.com/v1/companies/iKhokha/postings/744000146475750) · [tech-check-fullstack](https://github.com/ikhokha/tech-check-fullstack) · [github.com/ikhokha](https://github.com/ikhokha)
- Luno: [workflow](https://github.com/luno/workflow) · [luno-mcp](https://github.com/luno/luno-mcp) · [spec-kit-plan-review-gate](https://github.com/luno/spec-kit-plan-review-gate) · [spec-kit-preset-jira](https://github.com/luno/spec-kit-preset-jira) · [Greenhouse API](https://boards-api.greenhouse.io/v1/boards/luno/jobs?content=true) · [BusinessTech, 2026-07-28](https://businesstech.co.za/news/finance/867780/south-african-crypto-giant-cutting-20-of-jobs/) · [Daily Maverick, 2026-02-08](https://www.dailymaverick.co.za/article/2026-02-08-this-might-be-the-randbacked-stablecoin-weve-been-waiting-for/)

**Consultancies**
- DVT: [home](https://www.dvtsoftware.com) · [AI services](https://www.dvtsoftware.com/services/artificial-intelligence) · [Clippd case study](https://dvt.co.za/case-study-clippd-2026) · [case studies](https://www.dvtsoftware.com/news-insights/case-studies) · [careers](https://dvtcareers.recruitee.com) · [Senior .NET/Vue](https://dvtcareers.recruitee.com/o/senior-net-vue-full-stack-developer-cape-town) · [github.com/dvt](https://github.com/dvt)
- Synthesis: [techteam-content](https://github.com/synthesis-software-technologies/techteam-content) (AI Maturity guide, Code Connect 2026 keynote, Sept 2026 tech update) · [home](https://www.synthesis.co.za/) · [articles](https://www.synthesis.co.za/articles/) · [legacy to cloud](https://www.synthesis.co.za/from-legacy-to-cloud-synthesis-architects-the-digital-core-of-modern-banking/) · [bank of the future](https://www.synthesis.co.za/we-built-the-bank-of-the-future-darren-bak/) · [Our People](https://www.synthesis.co.za/our-people/) · [BusinessDay, Araxi/Pay@](https://www.businessday.co.za/companies/2026-05-11-araxi-concludes-r1bn-takeover-of-pay/)
- Entelect: [home](https://www.entelect.co.za) · [culture](https://culture.entelect.co.za/) · [positions](https://culture.entelect.co.za/current-available-positions/) · [graduate programme](https://culture.entelect.co.za/the-entelect-graduate-programme/) · [Backbase](https://entelect.co.za/entelects-premier-partnership-with-backbase/) · [github.com/entelect](https://github.com/entelect)

**Banks**
- Standard Bank: [press release, 2026-08-25](https://www.standardbank.com/sbg/standard-bank-group/newsroom/press-releases/weve-positioned-ai-as-long-term-competitive-capability) · [TechCentral, 2026-08-17](https://techcentral.co.za/inside-standard-banks-multi-model-ai-bet/284924/) · [ITWeb, 2026-08-13](https://itweb.africa/article/ai-tool-usage-reaches-72-at-standard-bank/kLgB1MezYrPq59N4) · [RTE posting](https://api.smartrecruiters.com/v1/companies/StandardBankGroup/postings/744000152157299) · [SE posting](https://api.smartrecruiters.com/v1/companies/StandardBankGroup/postings/744000152450669)
- Absa: [AWS statement, 2025-09-08](https://www.absa.africa/media-statements/2025/absa-group-collaborates-with-amazon-web-services/) · [TechCentral, 2026-08-19](https://techcentral.co.za/absas-ai-is-writing-its-code-and-answering-its-calls/285065/) · [Microsoft story, 2024](https://microsoft.com/en/customers/story/1783172439597920946-absa-github-copilot-banking-and-capital-markets-en-south-africa)
- FirstRand: [Sowetan, 2026-08-19](https://www.sowetan.co.za/news/2026-08-19-watch-this-is-how-firstrand-is-using-ai-to-help-its-3000-engineers-work-faster-and-better/) · [Finextra, Finxact](https://www.finextra.com/pressarticle/104240/firstrand-group-signs-for-finxact-from-fiserv) · [AWS Summit Johannesburg agenda](https://aws.amazon.com/events/summits/johannesburg/agenda)
- Nedbank: [2024 annual results booklet](https://group.nedbank.co.za/content/dam/group/pdf/20_financial-results/2024/annual-results/2024-annual-results-booklet-nedbank.pdf) · [ITWeb, 2026-08-04](https://www.itweb.co.za/article/nedbanks-ai-strategy-unlocks-r375m-in-value/Pero3MZ3J5AqQb6m) · [Nedbank H1 2026 press release](https://group.nedbank.co.za/news-and-insights/press/2026/nedbank-group-strengthens-focus-on-growth.html)
- Capitec: [pg-proxy](https://github.com/capitec/pg-proxy) · [dsp-decision-engine](https://github.com/capitec/dsp-decision-engine) · [BusinessDay, 2025-04-30](https://www.businessday.co.za/bd/companies/financial-services/2025-04-30-capitec-beefs-up-tech-strategy-with-new-recruits/) · [The Banking Brief](https://the-banking-brief.beehiiv.com/p/capitec-scales-ai-and-headcount-in-parallel) (**Secondary**)
- Investec: [TechCentral, 2026-06-24](https://techcentral.co.za/investec-deploying-ai-tools-to-every-employee/282997/) · [investec-dev-quest](https://github.com/investec-developer-community/investec-dev-quest) · [ai-sandbox](https://github.com/investec-developer-community/ai-sandbox) · [home-run](https://github.com/investec/home-run) · [DevConf](https://www.devconf.co.za/)
- Discovery: [Microsoft case study, 2025-04-23](https://www.microsoft.com/en/customers/story/23562-discovery-bank-azure) · [press release, 2026-05-14](https://www.mynewsdesk.com/za/discovery-holdings-ltd/pressreleases/discovery-bank-says-ai-driven-security-has-stopped-estimated-r100m-in-fraud-as-it-rolls-out-enhanced-security-ai-powered-payments-and-dstv-rewards-3448437) · [TechCentral, 2026-08-06](https://techcentral.co.za/why-discovery-is-going-slow-on-ai-coding-agents/284618/)

