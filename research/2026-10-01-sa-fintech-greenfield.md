# SA fintech, greenfield: who builds, what they hire for, what to prove

Primary-source research for one question: **where does a Johannesburg C#/.NET full-stack engineer build new fintech products in South Africa, what do those employers ask for, and which portfolio would prove fit?** Everything was read on **2026-10-01**. Where possible it was read on the employer's own careers page or ATS (Greenhouse, Workable, BambooHR, Breezy, HiBob, simplify.hr, Recruitee, SmartRecruiters, Workday, SuccessFactors, Teamtailor), engineering blog, developer docs or regulator site. OfferZen company profiles are used where nothing else could be read. They are company-curated but **undated**, and several still list ".NET Core 2.0", so they are flagged as possibly stale. Secondary sources (law-firm notes, trade press, vendor blogs) are used only for news and status facts, and are labelled. Inference is marked **Inference**. Anything that could not be confirmed on the page that owns it is marked **Unverified**. No salaries are quoted. None were read.

This file builds on `2026-09-28-sa-fintech-target-roles.md`, `2026-09-29-fintech-knowledge-sources.md` and `2026-09-23-fraud-and-bank-apis.md`, and does not repeat them. Corrections to those files are collected in section 0.

**The counts are a one-day snapshot.** Several of the most interesting employers (Stitch, Yoco, VALR, Ozow backend) had no open engineering roles today. That says nothing about their stacks.

---

## The verdict

1. **Greenfield fintech product work in SA is mostly in Cape Town payments companies, and their stated backends are mostly not .NET.** Stitch is TypeScript ([Stitch blog](https://stitch.money/blog/introducing-the-stitch-tech-stack)). Peach is Python and TypeScript ([Peach posting](https://peachpayments.bamboohr.com/careers/163/detail)). Paystack is TypeScript and Node first ([Paystack](https://careers.paystack.com/jobs/7862204-senior-backend-engineer)). Jumo is Kotlin ([Jumo careers](https://jumo.world/careers/)). Luno is Go ([GitHub](https://github.com/luno)). Yoco and VALR are Kotlin, Scala, Node and Python per their OfferZen profiles.
2. **.NET is a minority in innovative fintech, but it is real, and part of it is in Johannesburg.**
   - Ozow's own stack page names ASP.NET Core as its "go to" server framework ([Ozow](https://www.ozow.com/tech-stack)).
   - Investec's Sandton teams post .NET platform roles. They can't be read today (bot challenge), but the user-supplied postings from 2026-09-29 stand.
   - Precium (formerly Revio) and Purple Group (EasyEquities) list C#/.NET on OfferZen.
   - Paystack's Cape Town full-stack advert accepts C# as one of six languages ([Paystack](https://careers.paystack.com/jobs/7862201-senior-full-stack-engineer-south-africa)).
   - The Johannesburg consultancies that serve banks have open .NET roles today: Dariel in Bramley ([Dariel](https://darielsoftware.simplify.hr/Vacancy/194714)) and Entelect ([Entelect](https://culture.entelect.co.za/current-available-positions/)).
3. **The domain words in today's adverts are transaction flows, orchestration, settlement, payouts, ledgers and reconciliation, not ISO 20022 or PayShap.**
   - Paystack's Financial Systems team owns "settlements, merchant payouts, refunds, disputes, treasury flows and ledger products" and gives bonus points for "Ledger design or double-entry accounting" ([Paystack](https://careers.paystack.com/jobs/8463678-product-manager-financial-systems)). That is a PM role in Nigeria, not an engineering role.
   - Peach asks for "Comprehensive knowledge of transaction flows, the regulatory landscape" ([Peach](https://peachpayments.bamboohr.com/careers/163/detail)).
   - No engineering advert read today names ISO 20022, PayShap, open finance or card issuing.
4. **AI shows up as tooling, not as LLM product features.** Peach lists "Agential AI (Gemini, Claude)" among its tools. Lula wants "AI tooling (Cursor, v0, or equivalent) as a core part of your workflow" ([Lula](https://lulalend.breezy.hr/p/4d0feee1ab86-ai-native-frontend-engineer)). Paystack's DBA role wants "AI-assisted database tooling" ([Paystack](https://careers.paystack.com/jobs/7862199-senior-database-administrator)). None of today's fintech adverts requires building an LLM feature.
5. **What an engineer building products here needs to know:**
   - **PayShap and PayShap Request are the live greenfield rail.** They are ISO 20022-based, alias (ShapID) addressed, run by 12 participating banks, and allow up to R50,000 a transaction ([Nedbank FAQ](https://personal.nedbank.co.za/bank/digital-banking/needs/payments/payshap/payshap-request-faqs.html)).
   - **The SARB now owns NPS rules and licensing**, and PayInc operates PayShap ([SARB PSMB](https://www.resbank.co.za/en/home/what-we-do/payments-and-settlements/psmb)).
   - **Licensing is moving to an "activity-based regulatory model"** that would let non-banks "access clearing systems directly" ([SARB PEM](https://www.resbank.co.za/en/home/what-we-do/payments-and-settlements/pem)). It is still a draft.
   - **Account-data open finance still has no instrument.**
6. **Postgres and MySQL are the norm at product fintechs. SQL Server lives in the .NET shops** (Ozow, Investec, Purple Group). Build the ledger on Postgres and keep SQL Server where it earns its place (section 4).
7. **The portfolio is three connected projects, all buildable in C#:**
   - a double-entry ledger with an idempotent payments API and signed webhooks;
   - an ISO 20022 instant-payment and Request-to-Pay simulator with real PSP sandbox adapters;
   - a reconciliation engine over `camt.053`, CSV and bank-API statements, with an AI break-explainer gated by evals.
8. **Free sandboxes are thinner than they look.** Two need no merchant account: Investec (published sandbox credentials) and Open Bank Project (self-registration). Peach gives sandbox access "when you sign up". Yoco test keys need a Yoco account. Stitch credentials are "issued to you by the Stitch team". Ozow needs a merchant account.

| | Label | Why |
|---|---|---|
| Payments product engineering in Cape Town (TS, Python, Kotlin, Go) | **Happening** | Paystack, Peach, Lula, Jumo hiring; Stitch shipping new products |
| .NET greenfield in SA fintech | **Consolidating, narrow** | Ozow, Investec, Precium, Purple Group, plus Johannesburg consultancies serving banks |
| ISO 20022 / PayShap as an advertised engineering skill | **Noisy** | Central to the rails, absent from today's engineering adverts |
| LLM features as a fintech requirement | **Noisy** | AI appears as tooling fluency only |

---

## 0. What in the earlier notes is stale or wrong

| Earlier claim | File | What the primary source says today |
|---|---|---|
| Paystack: "Workable accounts exist; 0 jobs"; `paystack.com/careers` 403 | 09-28 | **Wrong ATS.** Paystack's board is Teamtailor at `careers.paystack.com`. It lists Senior Full Stack Engineer (South Africa), Senior Backend Engineer, Senior Data Engineer, Senior DBA, QA, platform security and others ([list via reader proxy](https://paystack.com/careers)) |
| Peach: "no engineering" | 09-28 | A **Technical Engineering Manager** role, posted 3 Sep 2026, is open ([Peach](https://peachpayments.bamboohr.com/careers/163/detail)). **Unverified** whether it was missed on 09-28 or re-listed |
| "Ledger, double-entry" in no posting | 09-28 | Still true of engineering bodies read today. But Paystack's Financial Systems PM role names "ledger products" and "double-entry accounting" ([Paystack](https://careers.paystack.com/jobs/8463678-product-manager-financial-systems)). Stitch sells "Reconciliation & reporting" ([Stitch](https://stitch.money/)). The work exists and is starting to be named |
| Revio as a target | brief | Revio is now **Precium** ([OfferZen](https://www.offerzen.com/companies/precium-fka-revio)). Its BambooHR board redirects to BambooHR's marketing site, so it is unreachable |
| Stitch is TypeScript with Identity Server 4 | 09-28 | The blog source dates from 2022 and was updated in 2024. OfferZen lists ".NET Core 2.0" next to Node and TS. **Unverified** whether any .NET remains at Stitch |
| `product` on Postgres with a React back-office | 09-28 | **Conflicts** with 09-29, which says "SQL Server as the edge" and an "Angular back-office". The database evidence in section 4 favours Postgres for the ledger. Angular vs React is still the user's call (Investec requires Angular) |
| Joint Standard 2 of 2024 "envisaged to commence 1 June 2025" | 09-28 | Secondary sources say commencement was confirmed for 1 June 2025, with 12 months to comply ([Moonstone](https://www.moonstone.co.za/cybersecurity-joint-standard-commencement-date-confirmed/), secondary) |
| Final PISP / authorisation framework "promised Q3 2026" | 09-23 | **Not found published** as of 2026-10-01. The SARB regulation page lists only the November 2025 drafts ([SARB](https://www.resbank.co.za/en/home/what-we-do/payments-and-settlements/regulation-oversight-and-supervision)). **Unverified**: search only |
| PayShap volumes | 09-29 (PayInc: 329m in FY2025) | Stitch's 2026 blog and Ozow press coverage both quote "R100 billion across 136+ million transactions". The numbers conflict. Prefer PayInc's own report; the vendor figure is probably older (**Inference**) |
| Ozow docs | — | `oldhub.ozow.com` no longer resolves (DNS failure). The current hub says "You need an Ozow merchant account before you can integrate" ([hub.ozow.com](https://hub.ozow.com/)) |
| The 09-28 verdict: data engineer first, AWS | 09-28 | This brief's goal is **greenfield product backend**, which is the 09-28 file's "second door". The two goals pull in different directions. The user should choose |

---

## 1. Who builds greenfield fintech in SA in 2026

"Greenfield?" means building new products or platforms, judged from the company's own wording. Stack is what the employer states. Source age matters, so it is given.

### Product companies

| Company | What they build | Greenfield? | Stated backend stack | DB | .NET? | Source |
|---|---|---|---|---|---|---|
| **Stitch** | Online and in-person payments, card acquiring "via Stitch + Efficacy Payments", payouts, "Reconciliation & reporting", "Embedded fraud solution — Real-time, rule-based", orchestration; "ISO 27001 + PCI DSS Level 1" | Yes. New product lines | TypeScript, Koa, Nact actors, XState, K8s; Identity Server 4 for auth (2022/2024 post) | Postgres (OfferZen) | **Minor/unclear** | [stitch.money](https://stitch.money/), [blog](https://stitch.money/blog/introducing-the-stitch-tech-stack), [OfferZen](https://www.offerzen.com/companies/stitch). Workable: 0 jobs |
| **Peach Payments** | Payment orchestration, merchant onboarding, PSP | Yes ("Payment orchestration") | **Python, TypeScript**; AWS Lambda, API Gateway, EKS, Kafka; Terraform | MySQL, MongoDB | No | [Peach TEM posting](https://peachpayments.bamboohr.com/careers/163/detail) (posted 2026-09-03) |
| **Paystack (SA)** | Payments, recurring, direct bank payments, chargebacks, financial systems/ledger | Yes | TS preferred; JS, Python or Go (backend). SA full-stack: "Typescript, Javascript, Java, C++, C#, Python", Nest/Express | MySQL, MongoDB, Redis | **Accepted, not primary** | [Full Stack SA](https://careers.paystack.com/jobs/7862201-senior-full-stack-engineer-south-africa), [Backend](https://careers.paystack.com/jobs/7862204-senior-backend-engineer), [DBA](https://careers.paystack.com/jobs/7862199-senior-database-administrator) |
| **Ozow** | Pay-by-bank, PayShap Request ("no extra setup required"), payouts, refunds | Yes, but no backend roles open today | **ASP.NET Core**; AWS ECS, TeamCity, Terraform | **SQL Server & Postgres**, DynamoDB, Redis | **Yes (first-party)** | [tech-stack](https://www.ozow.com/tech-stack), [PayShap Request](https://ozow.com/our-products/instant-payments-with-payshap-request), [Greenhouse](https://boards-api.greenhouse.io/v1/boards/ozow/jobs): 8 roles, none backend |
| **Yoco** | Card machines, POS, payments, capital; "AI is built into everything we create" | Yes | OfferZen: Node, Python, Scala, Kotlin, TS | Postgres | No | [careers](https://www.yoco.com/za/careers/), [OfferZen](https://www.offerzen.com/companies/yoco). Its `/api/careers` returned 4 ads whose titles could not be rendered (HiBob SPA) |
| **Jumo** | Banking-as-a-service, lending | Yes | "Kotlin + Spring Boot … TypeScript + React … Kafka, Flink … AWS" | — | No | [jumo.world/careers](https://jumo.world/careers/) |
| **Lula (Lulalend)** | SME lending | Yes ("converting high-value ideas into production-ready capabilities fast") | Data/frontend: "Azure, Snowflake, DBT, Python, SQL"; DevOps: Azure, Terraform/Pulumi/**Bicep**. Backend language not stated | Snowflake | **Unknown**; Azure-first | [Frontend](https://lulalend.breezy.hr/p/4d0feee1ab86-ai-native-frontend-engineer), [DevOps](https://lulalend.breezy.hr/p/a1a76285dfa9-devops-platform-engineer), [ML](https://lulalend.breezy.hr/p/83182e9bce3d-senior-machine-learning-engineer). The OfferZen "lula" profile is a different company (shuttles) |
| **Precium (fka Revio)** | "payment orchestration and revenue optimization platform" | Yes | OfferZen: "PostgreSQL, Python, JavaScript, **C#, ASP.NET, .NET Core**"; React, Next.js; AWS | Postgres | **Yes (OfferZen, undated)** | [OfferZen](https://www.offerzen.com/companies/precium-fka-revio). Careers page points to a BambooHR board that no longer exists. A search snippet mentions "dotnet (C#)… Next.js" (**Unverified**, page 404) |
| **Purple Group / EasyEquities** | Fractional investing, EasyCrypto, RISE | Product | OfferZen: **C#**, Kafka, Elasticsearch | **MS SQL** | **Yes (OfferZen, undated)** | [OfferZen](https://www.offerzen.com/companies/purple-group-limited). No careers page found |
| **Paymenow** | Earned-wage access | Product | OfferZen: **ASP.NET, ".Net Core 2.0"**, Angular | **MS SQL** | **Yes, probably stale** | [OfferZen](https://www.offerzen.com/companies/paymenow). The careers URL redirects to a malformed host |
| **Luno** | Crypto exchange and wallet | Product | Go (event streaming `reflex`, `workflow`) | MySQL (OfferZen) | No | [GitHub](https://github.com/luno), [Greenhouse](https://boards-api.greenhouse.io/v1/boards/luno/jobs): 1 role (OTC Trader) |
| **VALR** | Crypto exchange | Product | OfferZen: TS, Node, Kotlin; GCP; RabbitMQ | Postgres | No | [OfferZen](https://www.offerzen.com/companies/valr). Workable: 0 jobs |
| **Lesaka** | Switching, EasyPay, merchant | Mixed | "Go, Java, C++, Rust, or similar" (switching) | Aurora MySQL, Postgres | No | [simplify.hr](https://lesakatech.simplify.hr/vacancy/vacancies): same two engineering roles as 09-28 |
| **iKhokha** | Card machines, POS | Product | Node/TS (09-28) | DynamoDB | No | [SmartRecruiters](https://api.smartrecruiters.com/v1/companies/iKhokha/postings): same two engineering roles |
| **Entersekt** | 3DS authentication | Product | Java 11+ | MySQL | No | [Greenhouse](https://boards-api.greenhouse.io/v1/boards/entersekt/jobs): 1 role |
| **TymeBank / GoTyme** | Digital bank | — | A Breezy full-stack posting (Python, Postgres, AWS, per search snippet) is **closed** | — | No | [Breezy](https://tyme-bank.breezy.hr/p/e2c6bffe436901-full-stack-software-engineer); `gotyme.com/careers` failed a TLS check |
| **Discovery Bank** | Digital bank | — | Nothing found. The Discovery "Developer (Junior)" ad is **Discovery Health**, Java/Oracle, implementing "specifications into existing systems" | Oracle | No | [Discovery](https://careers.discovery.co.za/job/Matlala-Developer-%28Junior%29-GP-2196/1442922133/) |
| **Bank Zero** | Digital mutual bank | — | No careers page (404). IBM LinuxONE core, per press (secondary, **Unverified**) | — | — | [bankzero.co.za/careers](https://www.bankzero.co.za/careers) 404 |
| **Capitec** | Retail bank | Mixed | The open back-end role is Android Java/Kotlin, payments. The rest are data roles | — | Not in current ads | [SuccessFactors search](https://careers.capitecbank.co.za/search/?q=software+engineer) |
| **Investec** | Private and business banking, UK open banking, lending platforms | **Yes**, per snippets: "rebuilding its credit application and decision platform… embedding AI capabilities"; "creation of the Transactional Banking Platform" | C#/.NET, Azure (user-supplied postings, 09-29) | SQL Server / Azure SQL | **Yes** | Careers search returns HTTP 202 with an empty body. Direct postings show "Vacancy Closed" ([13766](https://careers.investec.co.za/jobs/vacancy/net-engineer-13748-sandton/13766/description/), [12670](https://careers.investec.co.za/jobs/vacancy/-net-engineer-uk-offshore---corporate-banking-technology-12652-sandton/12670/description)). The greenfield wording comes from search snippets only: **Unverified** |
| **Standard Bank / Absa / FNB digital** | — | **Unverifiable from adverts** | Templates: Standard Bank "Software Engineer" names "API Engineering, Automation, Cloud Computing" only ([SR](https://api.smartrecruiters.com/v1/companies/StandardBankGroup/postings/744000152450669)). Absa's "AWS Developer / Engineer" "does not involve application feature development" ([Workday](https://absa.wd3.myworkdayjobs.com/ABSAcareersite/job/Johannesburg/AWS-Developer---Engineer_R-15982845-1)) | — | — | — |

Not verified at all: **Float, Franc, Ctrl, OneCard/Melon, Mukuru**.
- Float's site has no careers content ([float.co.za](https://www.float.co.za/careers)).
- Mukuru's ".NET Core… MySQL… AWS" senior role (Pretoria) is on an aggregator and was removed 2025-12-15 ([Built In](https://builtin.com/job/software-engineer-net/7509119)). It is not counted.
- Revio's site was blocked by a local web filter (Fortinet "Web Page Blocked").

### Consultancies

| Firm | Fintech evidence | Greenfield? | Stack, own words | .NET? | Source |
|---|---|---|---|---|---|
| **Dariel** (Bramley, Johannesburg) | "business-critical systems for clients across banking, telecoms, healthcare" | Mixed; not stated in ads | "Large team" in .NET and Java. Open: **Senior Dot Net Developer** ("C# and .NET Core / .NET 6+", EF Core, Angular or React, Docker/K8s, 6+ yrs) and **Full Stack Engineer** (".NET", 4+ yrs). Both posted 20 Jul 2026, closing 31 Dec 2026 | **Yes, open today in Johannesburg** | [careers](https://www.dariel.co.za/careers), [194714](https://darielsoftware.simplify.hr/Vacancy/194714), [194596](https://darielsoftware.simplify.hr/Vacancy/194596) |
| **Entelect** | Projects: Capitec "banking data migration", Investec "cloud modernization"; Backbase partner | Mixed | Evergreen Senior and Intermediate **.NET Software Engineer**: Azure/AWS/GCP; "MS SQL, PostgreSQL… Cosmos DB"; Angular, Blazor, React; 6+ yrs | **Yes** | [entelect.co.za](https://www.entelect.co.za/), [positions](https://culture.entelect.co.za/current-available-positions/), [Senior .NET](https://culture.entelect.co.za/position/senior-net-software-engineer/) |
| **DVT** | Clients include FNB, Nedbank, Standard Bank, Investec, SARB; "banking sector and the payments industry" | Mixed | Open: Azure Cloud SecOps (banking client), Senior Azure DevOps (".NET / C# web APIs"), AI Architect, AWS DevOps | **Some** | [careers](https://www.dvt.co.za/careers), [Recruitee](https://dvtcareers.recruitee.com/api/offers/) |
| **Synthesis** | "Payments Centre of Excellence", RegTech (Regstream, TXstream), HSMs; clients: all big four banks plus Investec and Capitec; AWS Advanced Partner | Yes | Kafka, K8s, AWS, GCP, Flink, Confluent | **Not .NET-flavoured** | [synthesis.co.za](https://www.synthesis.co.za/), [our-people](https://www.synthesis.co.za/our-people/). [simplify.hr](https://synthesis.simplify.hr/vacancy/vacancies): "no open jobs" |
| **BBD** | Banking and insurance named | Mixed | Open: Python & Django Backend (Johannesburg), Java Engineer (Johannesburg), Platform Engineer | No | [bbdsoftware.com/careers](https://bbdsoftware.com/careers/) |
| **Retro Rabbit** (Pretoria) | Absa, Nedbank, FNB, Standard Bank, Capitec, Discovery; "forex transaction platforms", "digital onboarding", "legacy system modernization" | Mixed, leaning modernisation | Not stated; "Java-based core systems" in case studies | Unknown | [retrorabbit.co.za](https://www.retrorabbit.co.za/). Careers page 404 |
| **Global Kinetic** | FutureBank BaaS platform (search snippet only) | Yes, by its description | Not readable | **Unverified** | [globalkinetic.com](https://www.globalkinetic.com/) rendered a tagline only |

**Inference:** consultancy greenfield work is client-dependent. The open .NET roles at Dariel and Entelect are evergreen bench roles, not named fintech products. They are the most reachable .NET doors in Johannesburg. Whether a given placement is greenfield is something to ask in the interview.

---

## 2. Current open roles (read today)

| Employer | Title | Level | Location | Required stack | Domain / nice-to-have | AI | Source |
|---|---|---|---|---|---|---|---|
| Paystack | Senior Full Stack Engineer – South Africa | Senior | **Cape Town (strict)** | TS/JS/Java/C++/**C#**/Python; Express, Sails, Nest; React/Angular/Vue; MySQL, MongoDB, Redis, K8s, AWS | "financial data", "distributed systems at scale" | None | [link](https://careers.paystack.com/jobs/7862201-senior-full-stack-engineer-south-africa) |
| Paystack | Senior Database Administrator | 5+ yrs | Multi incl. SA | MySQL (replication, partitioning, HA), Redis, MongoDB, RDS/Aurora, Terraform | — | "AI-assisted database tooling" | [link](https://careers.paystack.com/jobs/7862199-senior-database-administrator) |
| Paystack | Senior Backend Engineer | 4+ yrs | Nigeria | TS preferred; JS/Python/Go; AWS, K8s | Recurring payments, direct bank payments, chargebacks | None | [link](https://careers.paystack.com/jobs/7862204-senior-backend-engineer) |
| Paystack | PM – Financial Systems (non-eng.) | — | Nigeria | SQL a bonus | "settlements, merchant payouts, refunds, disputes, treasury flows and ledger products"; "records do not reconcile"; "Ledger design or double-entry accounting" | — | [link](https://careers.paystack.com/jobs/8463678-product-manager-financial-systems) |
| Peach | Technical Engineering Manager | EM | Remote-first, Cape Town HQ | Python, TS; AWS Lambda/API GW/EKS/RDS; Kafka; MongoDB, MySQL; GitLab | "transaction flows, the regulatory landscape"; Scrum | "Agential AI (Gemini, Claude)" | [link](https://peachpayments.bamboohr.com/careers/163/detail) |
| Lula | AI Native Frontend Engineer | Senior | Cape Town | React; Azure, Snowflake, dbt, Python, SQL | "fintech or regulated industries" advantage | "Cursor, v0… core part of your workflow" | [link](https://lulalend.breezy.hr/p/4d0feee1ab86-ai-native-frontend-engineer) |
| Lula | DevOps & Platform Engineer | 3–5 yrs | Cape Town (Remote) | Docker, Azure managed services; Terraform/Pulumi/Bicep; schema migrations with rollback | regulated-environment advantage | "agentic or AI-assisted development workflows" | [link](https://lulalend.breezy.hr/p/a1a76285dfa9-devops-platform-engineer) |
| Lula | Senior ML Engineer | Senior | Cape Town | Python, Terraform, Kafka, K8s, Spark/Flink, MLflow | FinTech | None | [link](https://lulalend.breezy.hr/p/83182e9bce3d-senior-machine-learning-engineer) |
| Jumo | Software Engineer | Intermediate | SA | Kotlin + Spring Boot, TS + React, Kafka, Flink, AWS | BaaS lending | — | [link](https://jumo.careers.hibob.com/jobs/8ef3d748-1da1-4a0b-bba8-04b84f0c3e37) |
| Dariel | Senior Dot Net Developer | 6+ yrs | **Bramley, Johannesburg** | C#, .NET 6+, EF Core, Angular/React, Docker/K8s | Multi-industry | None | [link](https://darielsoftware.simplify.hr/Vacancy/194714) |
| Dariel | Full Stack Engineer (.NET) | 4+ yrs | **Bramley, Johannesburg** | .NET; React/Angular, Azure/AWS nice | "banking" among domains; microservices | None | [link](https://darielsoftware.simplify.hr/Vacancy/194596) |
| Entelect | Senior .NET Software Engineer | 6+ yrs | SA, hybrid | .NET; MS SQL/Postgres/Cosmos; Azure DevOps | Enterprise | None | [link](https://culture.entelect.co.za/position/senior-net-software-engineer/) |
| DVT | Senior Azure DevOps | — | Johannesburg | ".NET / C# web APIs" infra | — | — | [Recruitee](https://dvtcareers.recruitee.com/api/offers/) |
| Lesaka, Entersekt, iKhokha, Capitec | Same roles as 09-28 | — | — | See 09-28 | — | — | as cited above |

What the nice-to-haves say about domain knowledge:
- **Payments flows and money movement:** Peach, Paystack.
- **Ledgers and reconciliation:** Paystack, but only in a PM role.
- **PCI DSS:** only in the security and cloud roles from 09-28.
- **Card issuing, ISO 20022, open finance, crypto:** not named in any engineering advert read today.

**Inference:** employers expect payments knowledge to be learned on the job, or shown by a portfolio. They don't list it as a filter.

---

## 3. Domain knowledge that matters now (official sources)

What a product engineer must be able to talk about. Restating the earlier notes is avoided. New or changed facts are marked.

**Who runs what (new detail).** From 11 August 2026 the SARB took "Rules and standards for the national payment system" and "Licensing, authorising and registering NPS payment institutions". From 2 September 2026 PayInc took the PCHs for "EFT credit, EFT debit, Authenticated Collections, PayShap (Rapid Payments), Registered Mandate and real-time clearing (RTC)". Standards moved to the SARB's Oversight and Supervision Division from 1 September 2026 ([SARB PSMB](https://www.resbank.co.za/en/home/what-we-do/payments-and-settlements/psmb)).

**Payments Ecosystem Modernisation (new detail)** ([SARB PEM](https://www.resbank.co.za/en/home/what-we-do/payments-and-settlements/pem)):
- **High-value payments:** enhancing SAMOS and SADC-RTGS, and new infrastructure supporting multiple currencies and "richer payment data".
- **National payments utility:** the SARB owns 50% of PayInc.
- **Low-value payments:** PayShap and TCIB.
- **PEMKey:** a "Payment Credential Ecosystem".
- **QR+ Standard 1.2.**
- **Licensing:** an "activity-based regulatory model" letting non-banks "participate in payments activities and access clearing systems directly".
- **Industry dialogues:** April, August and December 2025, and September 2026.

**PayShap and Request-to-Pay.**
- Bank-side facts ([Nedbank PayShap Request FAQ](https://personal.nedbank.co.za/bank/digital-banking/needs/payments/payshap/payshap-request-faqs.html)):
  - A ShapID is "an easy-to-remember alias… usually your cellphone number", and you get one ShapID per account.
  - Requests expire by default "14 days from the day the request is created", adjustable up to 45 days.
  - Requests can be up to R50,000 a transaction.
  - Nedbank's own payment limit is R5,000 by default, R10,000 with Approve-it and R50,000 with biometrics.
  - Participating banks: Absa, Al Baraka, African Bank, Capitec, Discovery, FNB, HBZ, Investec, Nedbank, OM Bank, Standard Bank, TymeBank.
- Ozow sells PayShap Request to existing merchants with "no extra development needed", and says refunds go directly to the customer's bank account ([Ozow](https://ozow.com/our-products/instant-payments-with-payshap-request)).
- PayShap's own site returned a CloudFront 403 to every fetch. **The PayShap ISO 20022 message set and its usage guidelines are not public** (**Unverified**). Any simulator is "PayShap-shaped", not PayShap-conformant. Say so in its README.

**ISO 20022 vocabulary.** The message names were read from the ISO 20022 catalogue, through a reader proxy because iso20022.org returns 403 directly ([iso20022.org](https://www.iso20022.org/iso-20022-message-definitions)):
- `pain` is Payments Initiation, `pacs` is Payments Clearing and Settlement, `camt` is Cash Management.
- Current versions: `pain.001.001.13` CustomerCreditTransferInitiation, `pain.013.001.12` CreditorPaymentActivationRequest (the Request-to-Pay request), `pacs.008.001.14` FIToFICustomerCreditTransfer, `pacs.002.001.16` FIToFIPaymentStatusReport, `camt.053.001.14` BankToCustomerStatement, `camt.054.001.14` BankToCustomerDebitCreditNotification.

**ISO 20022 in SA:**
- The SARB set targets of "ISO 20022 for Domestic RTGS (SAMOS) – September 2022" and "CBPR+… November 2022", and said MT and MX "can coexist and be dealt with through translation rules" ([SARB, ISO 20022 Migration, April 2022](https://www.resbank.co.za/content/dam/sarb/what-we-do/payments-and-settlements/rtgs-renewal/articles/ISO%2020022%20Migration%20April%202022.pdf)).
- SAMOS went live on 17–19 September 2022, and DebiCheck already uses ISO 20022 (SARB FAQ, in 09-29).
- RTC is scheduled to sunset in March 2027 (PayInc, in 09-29).
- **No dated SARB or PayInc timeline for moving EFT credit to ISO 20022 was found** (**Unverified**).

**Non-bank authorisation and the NPS Bill.**
- The SARB's regulation page lists ([SARB](https://www.resbank.co.za/en/home/what-we-do/payments-and-settlements/regulation-oversight-and-supervision)):
  - a *Draft Payment Activities Exemption Notice* and *Authorisation Framework* (14 November 2025, comments due 5 December 2025);
  - a 2026 draft directive on offshore-merchant issuing and acquiring (comments due 17 July 2026);
  - the TPPP and system-operator registers (May and July 2026);
  - Notice 7455 of 2026, varying Efficacy Payments' designation as a clearing system participant.
- Efficacy is Stitch's card-acquiring partner per Stitch's homepage. **Inference:** this is a live example of a fintech getting closer to clearing.
- The third draft framework (May 2026, comments closed 15 June 2026) is in 09-23. Its final version was not found today.
- **NPS Bill:** ENS (secondary, 8 September 2025) said it "has not yet been introduced" in Parliament ([ENS](https://www.ensafrica.com/news/detail/10690/when-will-south-africas-nps-bill-come-into-fo)). Its status on 2026-10-01 is **Unverified**.

**Open finance.** Unchanged from 09-23. There is no account-information instrument. Treasury's Budget Review 2026 says the IFWG "will continue with work to develop an appropriate regulatory framework". Stitch frames open finance as formalising "what products like Capitec Pay and Pay by bank have already been demonstrating" ([Stitch blog, 10 July 2026](https://stitch.money/blog/the-enterprise-cfos-2026-payments-readiness-checklist-pem-vision-2030-open-finance-and-ai-in-one-map); vendor opinion). **Inference:** in SA, "open banking" in practice means payment initiation plus consent, not data aggregation.

**FSCA crypto (CASP) licensing** ([FSCA press release, 15 December 2025](https://jutacomplinews.co.za/media/filestore/2026/01/FSCA_Press_Release-Update_on_licensing_and_supervision_of_crypto_asset_service_providers_._2.pdf), FSCA text on a mirror):
- Licensing under FAIS has run since 1 June 2023.
- As at 12 December 2025: 512 applications, 300 approved, 14 declined, 121 withdrawn.
- CASPs are supervised for AML/CFT under the FIC Act.
- "The South African Reserve Bank does not currently recognise crypto assets as currency."
- As at 31 March 2026, 533 applications and 310 approved (secondary, [FAnews](https://www.fanews.co.za/article/compliance-regulatory/2/financial-sector-conduct-authority-fsca-was-fsb/1059/update-on-licensing-and-supervision-of-crypto-asset-service-providers/43764)).

**Conduct (Twin Peaks).** The FSCA *Conduct Standard for Banks* (3 of 2020 (BA)) phased in from July 2020 to July 2021. It covers product design, disclosures, complaints and closure ([text](https://lawlibrary.org.za/akn/za/act/standard/fsca/2020/3/eng@2020-07-03)). Engineering relevance: auditability of disclosures and complaint flows.

**Security and privacy.**
- **PCI DSS v4.0.1** has been the only active version since 31 December 2024, and its future-dated requirements took effect on 31 March 2025 ([PCI SSC](https://blog.pcisecuritystandards.org/just-published-pci-dss-v4-0-1)).
- **Joint Standard 2 of 2024** (cyber) commenced on 1 June 2025, with 12 months to comply (secondary, above).
- **POPIA** breach reports must go through the Information Regulator's eServices portal from 1 April 2025 ([Covington](https://www.insideprivacy.com/data-security/data-breaches/south-africa-introduces-mandatory-e-portal-reporting-for-data-breaches/), secondary; the IR fact sheet is in 09-29).

---

## 4. Portfolio projects that prove fit, and the database question

### What employers say about databases

| DB | Who states it | Kind of shop |
|---|---|---|
| **Postgres** | Yoco, VALR, Stitch, Precium (OfferZen); Ozow (with SQL Server); Lesaka; Moniepoint (09-28); Entelect (one of many) | Product fintechs. Precium pairs it with .NET |
| **MySQL / Aurora** | Paystack, Peach, Luno, Entersekt, Lesaka | Payments product companies |
| **SQL Server** | **Ozow** (first-party), **Investec** I-2 ("SQL Server / Azure SQL data modelling and performance optimisation"), Purple Group, Paymenow (OfferZen), Entelect | .NET shops and banks |
| MongoDB, DynamoDB, Redis | Peach, Paystack, iKhokha, Ozow | Side stores |

**Inference:** Postgres is the safer default for a payments ledger read by product fintechs. SQL Server is a real asset at the .NET employers (Ozow, Investec, Purple Group). One SQL Server component is worth keeping on purpose. Section 7 does that.

### Candidate projects, scored

| Project | Mirrors (cited) | Fundamentals proved | C#/.NET? | DB |
|---|---|---|---|---|
| Double-entry ledger + idempotent payments API + signed webhooks | Paystack "ledger products… settlements, merchant payouts, refunds, disputes"; Stitch payouts; Lesaka "correctness, ordering, and idempotency"; Yoco's own `Idempotency-Key` (24h, `Idempotent-Replayed: true`) and Standard Webhooks HMAC-SHA256 ([Yoco idempotency](https://developer.yoco.com/docs/checkout-api/idempotency.md), [webhooks](https://developer.yoco.com/docs/api/webhooks/verifying-events.md)) | Invariants, concurrency, exactly-once illusion, outbox, at-least-once delivery | Yes | Postgres |
| ISO 20022 instant-payment / RTP simulator | Ozow PayShap Request; Stitch PayShap; Peach and Precium "orchestration"; SARB PEM non-bank access | Message schemas, state machines, timeouts, proxy resolution, limits, expiry | Yes (`System.Xml.Schema`) | Postgres |
| Reconciliation engine (`camt.053` + CSV + bank JSON) | Paystack "records do not reconcile"; Stitch "Reconciliation & reporting… finance-ready exports"; Mama Money and Lesaka recon (09-28) | Matching, tolerances, timing breaks, many-to-one, audit evidence | Yes | SQL Server fits |
| Open-finance aggregation with consent | Stitch's original data API (OfferZen) | OAuth/consent | Yes | — |
| Merchant checkout with webhooks | Yoco, Peach, Ozow | Integration hygiene | Yes | — |
| Fraud rules on a stream | Stitch "Embedded fraud solution — Real-time, rule-based" | Pure-function rules, backtesting | Yes | — |
| AI-assisted recon and disputes, with evals | Peach, Lula and Paystack AI-tooling signals; Paystack disputes | Grounded LLM output, evals | Yes (`Microsoft.Extensions.AI`) | — |

Two of these are weak as standalone projects:
- **Aggregation**, because SA has no account-information regime (09-23), and Stitch's homepage no longer lists data products. **Inference:** Stitch has moved to payments.
- **Fraud on its own**, because it has no oracle (09-23).

Both become modules inside the projects in section 7.

---

## 5. Public sandboxes a portfolio can use

| Provider | Access, from its docs | Account needed? | Use in the portfolio | Source |
|---|---|---|---|---|
| **Investec Programmable Banking** | Sandbox "bearing mock client data for testing purposes" (Terms 6.1); "You can explore our APIs using the sandbox environment" | **No** (published credentials; called successfully on 2026-09-23, **not re-called today**) | Real SA bank transaction shape for recon | [terms](https://developer.investec.com/terms-of-use), [individuals](https://developer.investec.com/individuals) |
| **Peach Payments** | "When you sign up with Peach Payments, you gain access to the sandbox Dashboard"; "No real money is ever transferred"; multi-currency tests need amounts of 92.00 or 15.99 | Peach sign-up (**Unverified** whether individuals qualify) | PSP adapter: card, 3DS test cards, webhooks | [dashboard-sandbox](https://developer.peachpayments.com/docs/dashboard-sandbox), [test-and-go-live](https://developer.peachpayments.com/docs/reference-test-and-go-live) |
| **Yoco** | Test keys from "the Yoco App… Checkout API integration"; test transactions "don't appear on your portal dashboard"; minimum R2.00 | **Yoco account** | Checkout plus idempotency and Standard Webhooks reference | [testing](https://developer.yoco.com/docs/checkout-api/testing.md), [llms.txt](https://developer.yoco.com/llms.txt) |
| **Ozow** | "You need an Ozow merchant account before you can integrate"; `IsTest` and staging (per search snippets of the retired docs) | **Merchant account** | Only if the user can get one | [hub.ozow.com](https://hub.ozow.com/), [prerequisites](https://hub.ozow.com/getting-started/prerequisites-and-onboarding/) |
| **Stitch** | Client ID "will be issued to you by the Stitch team"; IDE is waitlist-only | **Yes, issued by Stitch** | Not self-serve | [client-tokens](https://docs.stitch.money/authentication/client-tokens), [IDE](https://ide.stitch.money/) |
| **Paystack** | Test cards published (e.g. `4084 0840 8408 4081`); how to get test keys not stated on the page read | **Unverified** | Possible second PSP adapter | [test-payments](https://paystack.com/docs/payments/test-payments/) (via reader proxy; direct 403) |
| **Open Bank Project** | Sandbox portal with "Register" and "Get API Key"; AGPL | Self-register | Generic open-banking API shape (not SA) | [openbankproject.com](https://www.openbankproject.com/), [sandbox portal](https://apisandbox-portal.openbankproject.com/) |

Terms beyond Investec's were not read in full. **Unverified** for Peach, Yoco and OBP: whether a public, non-commercial repository built against the sandbox is allowed. Read each terms page before publishing.

---

## 6. What this means for a C#/.NET engineer

- **Be honest about the ratio.** Among product fintechs with a current, readable stack, first-party .NET today is Ozow. Investec, Precium, Purple Group and Paymenow add to that, but through closed postings, user-supplied text or undated OfferZen profiles. Everyone else building new payments products states TypeScript, Python, Kotlin/Java/Scala or Go.
- **The .NET-friendly greenfield doors, in order of fit for a Johannesburg engineer:**
  1. **Investec** (Sandton): .NET, Azure, SQL Server, UK open banking, new lending and transactional platforms. Its careers site is bot-blocked, so it has to be watched by hand.
  2. **Dariel and Entelect** (Johannesburg): open .NET roles with banking clients.
  3. **Ozow** and **Precium** (Cape Town): .NET backends, no readable openings today.
  4. **Purple Group** (Rosebank): C# and MS SQL per OfferZen; current openings **Unverified**.
  5. **Paystack** (Cape Town, strict): accepts C# but runs on TS/Node.
- **Location is the second constraint after language.** Nearly every non-.NET product fintech role read today is in Cape Town or remote. The Johannesburg roles are Investec, the consultancies and bank templates.
- **The concepts transfer, and employers say so in their wording.** Paystack's SA advert names six acceptable languages, and Lesaka's says "or similar". Paystack's Financial Systems role values "how money moves in practice". A C# portfolio that proves ledger invariants, idempotency, ISO 20022 handling and reconciliation reads in any language. The filter that doesn't transfer is "N years in language X" (09-28).
- **If a second language is added, TypeScript is the cheaper one** (**Inference**). It is stated at Stitch, Peach, Paystack, VALR, iKhokha and Jumo's web stack, and the engineer already writes React. Kotlin is stated at Jumo, Yoco, VALR and Capitec. Either is a module, not a rewrite.
- **AI skills:** show AI-assisted engineering (Claude Code, Cursor, MCP) as a working practice, plus one LLM feature with evals. Don't lead with AI features. No fintech advert today requires them.

---

## 7. Recommended portfolio: three connected projects

They connect like this: the ledger records money, the rails move it, and recon proves the two agree with the outside world. **Inference:** this maps onto the existing plan as `product` = ledger (+ rails as a second service) and `parity` = recon, so it needs no new system count.

### 1. `ledger`: merchant ledger and payments API
- **Problem:** record payments, refunds, payouts and fees so that every entry balances, every retry is safe and every merchant gets a signed event.
- **Mirrors:** Paystack Financial Systems ("settlements, merchant payouts, refunds, disputes, treasury flows and ledger products"); Stitch payouts and refunds; Lesaka "correctness, ordering, and idempotency"; Yoco's published idempotency and webhook contracts.
- **Fundamentals:**
  - double-entry with derived balances;
  - `Idempotency-Key` with Yoco-like semantics (24h retention, a replay header);
  - a payment state machine;
  - optimistic concurrency;
  - a transactional outbox;
  - Standard Webhooks HMAC signing with a timestamp tolerance;
  - property tests ("every entry nets to zero").
- **Stack:** ASP.NET Core, **Postgres**, EF Core plus hand-written SQL for postings, Testcontainers. Back-office in React (Ozow, Jumo, Lula) or Angular (Investec). That choice is the user's.

### 2. `rails`: ISO 20022 instant-payment and Request-to-Pay simulator, with PSP adapters
- **Problem:** simulate a PayShap-shaped scheme:
  - alias (ShapID-like) resolution;
  - `pain.013` request-to-pay with 14-day default and 45-day maximum expiry, as Nedbank documents it;
  - `pacs.008`/`pacs.002` clearing and status;
  - `camt.054` notifications;
  - per-bank limits up to R50,000.
- Settled payments post to `ledger`. Adapters call the Peach sandbox (and Yoco test mode, if an account is available) behind one orchestration interface.
- **Mirrors:** Ozow PayShap Request; Stitch PayShap and orchestration; Peach and Precium "payment orchestration"; the SARB PEM "activity-based" non-bank access.
- **Fundamentals:** XSD validation against the official schemas, timeouts and partial states (Paystack: "a transfer times out, a transaction sits in a partial state"), retries with backoff, an inbox for deduplication, and a pure-function fraud-rule module that can be backtested (09-23).
- **Non-claims, in the README:** not PayShap-conformant (its spec isn't public), synthetic data only, no PANs, no PCI scope.
- **Stack:** .NET worker services, Postgres, a broker (Kafka/Redpanda, per 09-28).
- **Unverified:** whether ISO 20022 schema downloads are freely available. iso20022.org blocks automated reads.

### 3. `recon`: reconciliation engine with an evaluated AI break-explainer
- **Problem:** match `ledger` against external statements:
  - a seeded `camt.053` bank statement;
  - a PSP settlement CSV;
  - the **Investec sandbox** transaction JSON.
- **Output:** matched, unmatched, amount, timing and duplicate breaks, aged exceptions and suspense, as an audit-ready report.
- **Mirrors:** Paystack "records do not reconcile"; Stitch "Reconciliation & reporting… finance-ready exports"; Mama Money, Lesaka and Nedbank recon (09-28).
- **Fundamentals:** set-based matching and tolerances, many-to-one batch matching, determinism, and evidence a reviewer can check.
- **AI part:** `Microsoft.Extensions.AI` `IChatClient` (OpenAI or Anthropic) explains a break, citing the ledger rows and statement lines it read. A read-only MCP server exposes the recon queries. An eval set is built from the generator's injected breaks: citations must exist and must support the explanation.
- **Stack:** .NET, **SQL Server** (T-SQL matching and indexing, which is what Investec I-2 and Ozow run), with ledger data replicated in from Postgres. **Inference:** two engines on purpose is a defensible design story ("OLTP on Postgres, recon and reporting on SQL Server"). If it feels like ceremony, choose one.

---

## Sources

All read **2026-10-01** unless stated. "Proxy" means read through `r.jina.ai` because direct fetches were refused.

**Employer careers, ATS and postings**
- Ozow Greenhouse board: https://boards-api.greenhouse.io/v1/boards/ozow/jobs
- Ozow tech stack: https://www.ozow.com/tech-stack
- Ozow PayShap Request: https://ozow.com/our-products/instant-payments-with-payshap-request
- Stitch homepage: https://stitch.money/ ; careers: https://stitch.money/careers-at-stitch ; Workable: https://apply.workable.com/api/v1/widget/accounts/stitchmoney
- Stitch, Introducing the Stitch Tech Stack (2022, updated 2024): https://stitch.money/blog/introducing-the-stitch-tech-stack
- Peach BambooHR list: https://peachpayments.bamboohr.com/careers/list ; Technical Engineering Manager: https://peachpayments.bamboohr.com/careers/163/detail
- Paystack careers (proxy): https://paystack.com/careers
- Paystack postings: https://careers.paystack.com/jobs/7862201-senior-full-stack-engineer-south-africa ; https://careers.paystack.com/jobs/7862204-senior-backend-engineer ; https://careers.paystack.com/jobs/7862199-senior-database-administrator ; https://careers.paystack.com/jobs/8463678-product-manager-financial-systems ; https://careers.paystack.com/jobs/8434292-senior-product-manager-processing
- Paystack Workable (0 jobs): https://apply.workable.com/api/v1/widget/accounts/paystack
- Yoco careers: https://www.yoco.com/za/careers/ ; API (POST): https://www.yoco.com/api/careers
- Jumo careers: https://jumo.world/careers/
- Lula careers: https://lula.co.za/careers ; Breezy feed: https://lulalend.breezy.hr/json
- Lula postings: https://lulalend.breezy.hr/p/4d0feee1ab86-ai-native-frontend-engineer ; https://lulalend.breezy.hr/p/a1a76285dfa9-devops-platform-engineer ; https://lulalend.breezy.hr/p/83182e9bce3d-senior-machine-learning-engineer
- Luno Greenhouse: https://boards-api.greenhouse.io/v1/boards/luno/jobs ; GitHub: https://github.com/luno
- VALR Workable (0 jobs): https://apply.workable.com/api/v1/widget/accounts/valr
- Entersekt Greenhouse: https://boards-api.greenhouse.io/v1/boards/entersekt/jobs
- Lesaka simplify.hr: https://lesakatech.simplify.hr/vacancy/vacancies
- iKhokha SmartRecruiters: https://api.smartrecruiters.com/v1/companies/iKhokha/postings
- Capitec search: https://careers.capitecbank.co.za/search/?q=software+engineer ; https://careers.capitecbank.co.za/search/?q=developer
- Discovery search: https://careers.discovery.co.za/search/?q=developer ; Junior Developer: https://careers.discovery.co.za/job/Matlala-Developer-%28Junior%29-GP-2196/1442922133/
- Standard Bank SmartRecruiters: https://api.smartrecruiters.com/v1/companies/StandardBankGroup/postings?q=engineer&limit=100 ; Software Engineer: https://api.smartrecruiters.com/v1/companies/StandardBankGroup/postings/744000152450669
- Absa Workday, AWS Developer / Engineer: https://absa.wd3.myworkdayjobs.com/ABSAcareersite/job/Johannesburg/AWS-Developer---Engineer_R-15982845-1
- Investec careers (HTTP 202, empty): https://careers.investec.co.za/ ; closed postings: https://careers.investec.co.za/jobs/vacancy/net-engineer-13748-sandton/13766/description/ ; https://careers.investec.co.za/jobs/vacancy/-net-engineer-uk-offshore---corporate-banking-technology-12652-sandton/12670/description
- TymeBank Breezy (closed): https://tyme-bank.breezy.hr/p/e2c6bffe436901-full-stack-software-engineer
- Precium careers: https://www.precium.com/careers
- Dariel: https://www.dariel.co.za/careers ; https://darielsoftware.simplify.hr/vacancy/vacancies ; https://darielsoftware.simplify.hr/Vacancy/194714 ; https://darielsoftware.simplify.hr/Vacancy/194596
- DVT: https://www.dvt.co.za/careers ; https://dvtcareers.recruitee.com/api/offers/
- BBD: https://bbdsoftware.com/careers/
- Entelect: https://www.entelect.co.za/ ; https://culture.entelect.co.za/current-available-positions/ ; https://culture.entelect.co.za/position/senior-net-software-engineer/
- Synthesis: https://www.synthesis.co.za/ ; https://www.synthesis.co.za/our-people/ ; https://synthesis.simplify.hr/vacancy/vacancies
- Retro Rabbit: https://www.retrorabbit.co.za/
- Global Kinetic: https://www.globalkinetic.com/

**OfferZen company profiles (undated; some list ".NET Core 2.0", so possibly stale)**
- https://www.offerzen.com/companies/yoco ; /stitch ; /peach-payments ; /luno ; /valr ; /entelect ; /purple-group-limited ; /paymenow ; /precium-fka-revio ; /investec ; /capitec-bank ; /lula (a different company)

**Developer docs and sandboxes**
- Yoco: https://developer.yoco.com/llms.txt ; https://developer.yoco.com/docs/checkout-api/testing.md ; https://developer.yoco.com/docs/checkout-api/idempotency.md ; https://developer.yoco.com/docs/api/webhooks/verifying-events.md
- Peach: https://developer.peachpayments.com/docs/dashboard-sandbox ; https://developer.peachpayments.com/docs/reference-test-and-go-live
- Ozow: https://hub.ozow.com/ ; https://hub.ozow.com/getting-started/prerequisites-and-onboarding/
- Stitch: https://docs.stitch.money/authentication/client-tokens ; https://docs.stitch.money/authentication/client-secrets ; https://ide.stitch.money/
- Paystack, test payments (proxy): https://paystack.com/docs/payments/test-payments/
- Investec: https://developer.investec.com/terms-of-use ; https://developer.investec.com/individuals
- Open Bank Project: https://www.openbankproject.com/ ; https://apisandbox-portal.openbankproject.com/

**Regulators, operators and standards**
- SARB PEM: https://www.resbank.co.za/en/home/what-we-do/payments-and-settlements/pem
- SARB PSMB transition: https://www.resbank.co.za/en/home/what-we-do/payments-and-settlements/psmb
- SARB regulation, oversight and supervision: https://www.resbank.co.za/en/home/what-we-do/payments-and-settlements/regulation-oversight-and-supervision
- SARB, ISO 20022 Migration (April 2022): https://www.resbank.co.za/content/dam/sarb/what-we-do/payments-and-settlements/rtgs-renewal/articles/ISO%2020022%20Migration%20April%202022.pdf
- SARB RTGS renewal page: https://www.resbank.co.za/en/home/what-we-do/payments-and-settlements/rtgs-renewal (404)
- ISO 20022 message definitions (proxy): https://www.iso20022.org/iso-20022-message-definitions
- Nedbank PayShap Request FAQ: https://personal.nedbank.co.za/bank/digital-banking/needs/payments/payshap/payshap-request-faqs.html
- PayShap: https://www.payshap.co.za/ (CloudFront 403; not read)
- FSCA press release, CASP licensing (15 Dec 2025, FSCA text on a mirror): https://jutacomplinews.co.za/media/filestore/2026/01/FSCA_Press_Release-Update_on_licensing_and_supervision_of_crypto_asset_service_providers_._2.pdf
- FSCA Conduct Standard for Banks 3 of 2020 (text): https://lawlibrary.org.za/akn/za/act/standard/fsca/2020/3/eng@2020-07-03
- PCI SSC, PCI DSS v4.0.1: https://blog.pcisecuritystandards.org/just-published-pci-dss-v4-0-1

**Secondary (news and status only, labelled where used)**
- ENS, NPS Bill status (8 Sep 2025): https://www.ensafrica.com/news/detail/10690/when-will-south-africas-nps-bill-come-into-fo
- Stitch blog, CFO's 2026 checklist (10 Jul 2026): https://stitch.money/blog/the-enterprise-cfos-2026-payments-readiness-checklist-pem-vision-2030-open-finance-and-ai-in-one-map
- Stitch blog, State of PayShap in 2026 (28 Jul 2026): https://stitch.money/blog/real-time-payments-in-south-africa-the-state-of-payshap-in-2026
- FAnews, CASP figures at 31 Mar 2026: https://www.fanews.co.za/article/compliance-regulatory/2/financial-sector-conduct-authority-fsca-was-fsb/1059/update-on-licensing-and-supervision-of-crypto-asset-service-providers/43764
- Moonstone, Joint Standard 2 commencement: https://www.moonstone.co.za/cybersecurity-joint-standard-commencement-date-confirmed/
- Covington, POPIA eServices reporting: https://www.insideprivacy.com/data-security/data-breaches/south-africa-introduces-mandatory-e-portal-reporting-for-data-breaches/
- Built In, Mukuru .NET posting (removed 2025-12-15): https://builtin.com/job/software-engineer-net/7509119

**Unreachable or empty today**
- PayShap site (CloudFront 403), iso20022.org (403 direct), paystack.com docs (403 direct)
- Investec careers (202, empty body)
- `gotyme.com/careers` (TLS certificate failure); `revio.co` (blocked by local Fortinet filter)
- `oldhub.ozow.com` (DNS failure); Precium BambooHR (redirects to bamboohr.com)
- Bank Zero careers (404); Retro Rabbit careers (404); Synthesis `/careers/` (404)
- Investec programmable-banking page on investec.com (403)
- Yoco HiBob job pages (SPA, no content)

**Earlier files this extends**
- `research/2026-09-28-sa-fintech-target-roles.md`
- `research/2026-09-29-fintech-knowledge-sources.md`
- `research/2026-09-23-fraud-and-bank-apis.md`
- `research/2026-09-29-curriculum-sources.md`
