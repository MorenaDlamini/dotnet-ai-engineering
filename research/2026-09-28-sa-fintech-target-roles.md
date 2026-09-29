# Target roles, part two: what South African fintech engineering employers actually ask for

Primary-source extraction of 45 engineering postings from South African fintechs, payment
companies and banks, plus three remote-first fintechs that hire in South Africa. All were read in full
on 2026-09-28, on the employer's own careers page or through its ATS's public JSON API
(Greenhouse, Lever, Workable, SmartRecruiters, Workday CXS, SuccessFactors, HiBob,
simplify.hr). Recruiter boards were not used. Everything quoted is the posting's own wording.
Inference is marked **Unverified**. Sources that could not be reached are listed, not guessed.

This file builds on `2026-09-22-sa-target-roles.md`, which it follows in method and format. It
is the requirements source for the fintech rebuild of `CURRICULUM.md`. It does not rebuild the
curriculum. It also builds on `2026-09-23-fraud-and-bank-apis.md` (bank APIs, open banking,
the thin fraud market), `2026-09-23-full-stack-tooling.md` (C# as the largest local backend
ask), `2026-09-23-data-stack-and-certifications.md`, and `2026-09-26-github-profile-landing.md`.
It does not repeat what those files already say.

**The counts below are a one-day snapshot, and the method biases them.** Each employer's ATS was
searched for "engineer", "developer", "software" and "data". So any count is a count of what
was open and keyword-reachable on 2026-09-28, not a measure of the market. Yoco, Stitch, Peach,
Luno, VALR and Paystack had no open engineering roles that day. That says nothing about their
stacks, and they are among the most interesting employers on the list.

---

## The verdict

**The realistic target is a data engineer at a South African bank or fintech, with a backend
payments engineer as the second door. The data spine holds. The cloud does not: this market is
AWS, not Azure. C# stays as the service language, but it is not the fintech default; the JVM
is. `platform` and `parity` stay and get reframed as reconciliation. `product` keeps its stack
and changes its domain, from a municipal finance explorer to a small payments ledger that is
reconciled with `parity`. No fifth system.**

In seven sentences:

1. **Data is the biggest engineering family in the sample.** 11 of 45 postings are data roles. Capitec alone has five open. Python appears in 10 of those 11, and SQL in all 11.
2. **AWS is the cloud.** It is named in 22 of 45 postings, and it is the primary platform at
   Capitec, Ozow, Jumo, Lesaka, iKhokha, Moniepoint and Mama Money. Among the postings that
   name a primary cloud, only Nedbank is Azure-first. The curriculum's "Azure throughout" is
   written for a different audience.
3. **The fintech backend language is the JVM.** Java, Kotlin or Scala appear in 17 of 45
   postings. They are *required* in 4 of the 6 payments backend roles that name a language
   (Entersekt, Moniepoint, Jumo, Capitec). The other two are Lesaka ("Go, Java, C++, Rust, or
   similar") and iKhokha (Node.js and TypeScript preferred). C# appears in two postings, both
   times as one option in a list. Its strongest evidence is first-party: Ozow's own tech-stack page names ASP.NET
   Core as its "go to server-side" framework.
4. **The domain words that recur are transaction integrity, settlement and reconciliation, not
   ledgers.** "Idempotency", "ordering", "settlement", "reconciliation" and "transaction
   integrity" each appear in real engineering bodies. "Ledger" and "double-entry" appear in none.
   Card and scheme work (EMV, ISO 8583, 3DS, Postilion, PCI) appears in 8 postings. It is a
   closed specialism, the same shape as SAS AML.
5. **Compliance is named, and it is named as scope, not as a skill.** PCI DSS appears in 6
   postings. Explicit POPIA, GDPR, SARB, SOX, ISO 27001 and NIST mentions are rare, and they sit
   in security, cloud and card roles. The FIC Act, the FSCA and KYC appear in no engineering body
   at all.
6. **Applied AI shrinks.** One posting of 45 (Discovery's AI Developer) requires integrating
   AI into applications. Six more mention AI as readiness, security or tooling. The assistant in
   `product` stops being a headline and becomes the part with evals.
7. **Location is a real constraint.** 15 postings are in the Western Cape, 9 are remote-SA and
   17 are in Gauteng. Nearly all the modern-stack, non-template roles are in Cape Town,
   Stellenbosch or remote. Johannesburg's postings are mostly bank templates, legacy platforms
   (RPG, Murex, IBM ACE, Postilion) or leadership.

**Happening / Consolidating / Noisy**, applied to what was asked:

| | Label | Why |
|---|---|---|
| Data engineering on AWS (Python, SQL, Spark or a warehouse, Airflow, Terraform, Kubernetes) at SA banks and fintechs | **Happening** | 11 of 45, at five employers, with real bodies and concrete stacks |
| JVM backends for payments | **Happening** | Required wherever a payments backend names a language |
| Reconciliation and settlement as engineering work | **Consolidating** | Named in engineering bodies at Lesaka, Nedbank and Capitec. Mama Money asks Data and Tech to "build automated/custom recons" |
| Double-entry ledgers as an advertised skill | **Noisy** | Zero engineering bodies name one. **Unverified inference:** the ledger work exists inside these companies, but it is not what they advertise for |
| LLM integration as a requirement in SA fintech engineering | **Noisy** | 1 of 45 |

---

## Method

Read 2026-09-28. For each employer I tried the public ATS APIs first, then the careers page
itself, following it to whatever ATS it embeds:

- **Greenhouse** (`boards-api.greenhouse.io/v1/boards/<co>/jobs?content=true`): Ozow,
  Entersekt, Moniepoint and Luno returned boards.
- **Lever** (`api.lever.co/v0/postings/<co>`): Mama Money.
- **Workable** (`apply.workable.com/api/v1/widget/accounts/<co>`): Kuda. It returned boards
  with zero jobs for Stitch, VALR, Paystack, Tymeglobal and Flutterwave.
- **SmartRecruiters** (`api.smartrecruiters.com/v1/companies/<co>/postings`): Standard Bank
  Group and iKhokha.
- **Workday CXS** (`<co>.wd3.myworkdayjobs.com/wday/cxs/<co>/<site>/jobs`): Absa
  (`ABSAcareersite`) and FirstRand (`FRB`).
- **SuccessFactors career sites**, by scraping the search pages: Capitec
  (`careers.capitecbank.co.za`), Nedbank (`jobs.nedbank.co.za`) and Discovery
  (`careers.discovery.co.za`).
- **HiBob**: Jumo embeds full job bodies in `jumo.world/careers`. Yoco's page calls
  `/api/careers`, which returned four sales roles.
- **simplify.hr**: Lesaka (`lesakatech.simplify.hr/vacancy/vacancies`).

A posting counts if it is an engineering, data, QA, security, platform or engineering-leadership
role located in South Africa or open to remote workers in South Africa, and if its body was read
in full. Nedbank's three "Software Developer" postings share an identical template body and are
counted once. Non-engineering postings read for domain evidence (a fraud manager, a
reconciliation manager and two analysts) are listed separately and never counted.

Salary is stated on none of the 45.

---

## 1. Postings read

"Remote-SA" means the posting names South Africa as a remote location, or says it is remote-first
within a timezone band that includes South Africa. Seniority is the posting's own floor.

### Payments and fintech, not banks (19)

| # | Company | Title | Seniority | Location | Stack named | Domain | Compliance | URL |
|---|---|---|---|---|---|---|---|---|
| 1 | Ozow | Senior Data Engineer | 5+ yrs | Cape Town | SQL, Python, AWS (preferred), Databricks (preferred); streaming advantageous | "fintech, payments, or high-volume transactional environments is a plus" | Boilerplate compliance paragraph | [link](https://job-boards.greenhouse.io/ozow/jobs/7750853003) |
| 2 | Ozow | Senior Test Engineer | 7+ | Cape Town | SoapUI, Selenium, JMeter; ISTQB "not negotiable" | — | — | [link](https://job-boards.greenhouse.io/ozow/jobs/7513803003) |
| 3 | Ozow | Technical Support Engineer | 2–4 | Cape Town | APIs, Postman, logs; 24/7 shifts | Merchant integrations; "payment gateways is a nice to have" | — | [link](https://job-boards.greenhouse.io/ozow/jobs/7765969003) |
| 4 | Ozow | Senior Security Analyst | 8+ | Cape Town | AWS security, SIEM, EDR, WAF, IDS/IPS, pentest | Bank and merchant due diligence | **PCI DSS, ISO 27001, POPIA, "relevant SARB directives"**, NIST, CIS, OWASP | [link](https://job-boards.greenhouse.io/ozow/jobs/8000434003) |
| 5 | Entersekt | Senior Software Engineer: 3DS Payments | 5–8+ | Remote-SA | **Java 11+**, Tomcat, MySQL, REST; AWS, Docker, K8s nice | 3-D Secure payment authentication; "cardholder data or PII" | **PCI DSS, GDPR**, OWASP Top 10 | [link](https://job-boards.greenhouse.io/entersekt/jobs/6008895004) |
| 6 | Entersekt | QE & Automation Team Lead | 6+ | Remote-SA | Java, Playwright, Selenium, TestNG, Maven, Appium, GitLab CI | 3DS Access Control Server, "scheme certification obligations" | "audit evidence" | [link](https://job-boards.greenhouse.io/entersekt/jobs/6142019004) |
| 7 | Jumo | Software Engineer (Intermediate) | not stated | Remote-SA | **Kotlin / Java / Scala**, AWS; Python advantage. Stack: "Kotlin + Spring Boot … TypeScript + React … Docker, Terraform, Kubernetes, Kafka, Flink, Datadog, GitHub Actions + ArgoCD" | Banking-as-a-service, loans and savings; "high-volume/low-latency services" | — | [link](https://jumo.careers.hibob.com/jobs/8ef3d748-1da1-4a0b-bba8-04b84f0c3e37) |
| 8 | Jumo | Junior Data Engineer | "Junior"; body asks for real production experience | Remote-SA | **Spark, Kafka**, Python (preferred) or Kotlin, SQL, Airflow, AWS Redshift, Docker, K8s | Lending data for "Portfolio Managers and Decision Scientists" | — | [link](https://jumo.careers.hibob.com/jobs/a7cfa2ca-d8fe-4fff-968f-3a836ea542ee) |
| 9 | Jumo | Analytics Engineer | 3–5 | Remote-SA | SQL, MySQL/Postgres/Redshift/SQL Server; Airflow, NiFi, BI tools advantageous | "Experience in the FinTech industry" advantageous | Data governance | [link](https://jumo.careers.hibob.com/jobs/2fcc741b-8e61-42e5-8fd9-fd336056df2b) |
| 10 | Jumo | Security Engineer | 3+ | Remote, UTC+0–3 (listed as Portugal) | AWS EKS, Terraform, Kotlin services, Python, Semgrep, Okta, GuardDuty | "Help secure JUMO's use of AI tooling" | — | [link](https://jumo.careers.hibob.com/jobs/43926fa0-59be-44e0-bff9-1a3264e6bab2) |
| 11 | Lesaka (EasyPay) | Junior Data Engineer | 1–2 | Cape Town, hybrid | SQL, Python, Snowflake/BigQuery/Redshift, Git, CI; Airflow/Dagster, Kafka/Kinesis nice | "move **transaction, merchant and reconciliation data** from source systems into our warehouse" | — | [link](https://lesakatech.simplify.hr/Vacancy/193194) |
| 12 | Lesaka | Senior Backend Engineer (Switching Systems) | 5–8+ | Cape Town | "Go, Java, C++, Rust, or similar"; gRPC, TCP/IP; Kafka nice | "Ensure **correctness, ordering, and idempotency** in transaction flows"; retry, backoff, circuit breaking; ISO 8583 nice | "regulated or mission-critical environments" nice | [link](https://lesakatech.simplify.hr/Vacancy/182780) |
| 13 | Lesaka | Senior Cloud Engineer (AWS) | 3+ | Cape Town, hybrid | AWS, Terraform/OpenTofu, Terragrunt, Atlantis, K8s, ArgoCD/FluxCD, Datadog, Aurora MySQL, Postgres; Python/Bash/Go | "on-premise and Azure migrations to AWS"; on-call | **"PCI DSS 3.2.1 and 4.0.0, SOX ITGC 404, NIST"**; SOC reports; BCP | [link](https://lesakatech.simplify.hr/Vacancy/174971) |
| 14 | iKhokha | Senior Software Engineer | 7+ ("deal breakers") | uMhlanga; hybrid or remote | Node.js, TypeScript, React, AWS Lambda, DynamoDB, S3, Jest, Datadog | "card payment integrations (Card Present and Card Not Present)"; "secure payment flows" | — | [link](https://jobs.smartrecruiters.com/IKhokha/744000146477539-senior-software-engineer) |
| 15 | iKhokha | Full Stack Software Development Manager | 10+ | uMhlanga | "Java, C#, Python etc." | — | — | [link](https://jobs.smartrecruiters.com/IKhokha/744000146475750-full-stack-software-development-manager) |
| 16 | Kuda | Software Development Engineer in Test | 5+ | Cape Town, hybrid | Java, JavaScript, "working knowledge of C# and Groovy"; Selenium, Playwright, Rest Assured, JDBC, Jenkins, Azure DevOps | "automate complex financial user journeys" | — | [link](https://apply.workable.com/j/4FB4F99F50) |
| 17 | Moniepoint | Head of Engineering, Payment Gateway | 10+, with 5+ writing Java | Remote-SA | **Java, Spring Boot**, Docker, K8s, PostgreSQL, DynamoDB, Elasticsearch, AWS | Payment gateway, payouts, multi-currency; "a working understanding of payment flows and compliance" | "regulated environment" | [link](https://job-boards.eu.greenhouse.io/moniepoint/jobs/4971819101) |
| 18 | Moniepoint | Mobile Architect | 10+ | Remote-SA (among others) | Flutter/Dart, Android/Java, iOS/Swift | — | — | [link](https://job-boards.eu.greenhouse.io/moniepoint/jobs/4330952101) |
| 19 | Mama Money | Senior QA Automation Engineer | 5–8+ | Remote | REST, SQS, SQL, AWS EKS/RDS/SQS/API Gateway, JavaScript | Remittances; "queues" as integration points | — | [link](https://jobs.lever.co/mamamoney/e3646fe1-b2d1-46f8-90d1-9aab28105984) (first posted 2025-08-13, still open) |

### Banks and bank-adjacent financial services (26)

| # | Company | Title | Seniority | Location | Stack named | Domain | Compliance | URL |
|---|---|---|---|---|---|---|---|---|
| 20 | Capitec | Software Engineer: Back-End II (Android / Payments) | 3+ | Stellenbosch | Android Java/Kotlin, AIDL, REST, SQL/NoSQL, K8s, AWS/Azure, microservices, event-driven | Card machines. "EMV and ISO 8583 messaging … back-end services that authorise, **settle** and report on every transaction"; "**transaction integrity** … the code you write processes real money" | PCI PTS / PA-DSS, DUKPT / MK-SK (ideal) | [link](https://careers.capitecbank.co.za/job/Stellenbosch-Software-Engineer-Back-End-II-%28Android-Payments%29/1437424833/) |
| 21 | Capitec | Data Engineer (Regulatory Reporting Automation) | 5 | Stellenbosch | "**Advanced Python — the core technical requirement**", SQL, AWS, Django, K8s, IaC, orchestration; Snowflake advantage | "automates the preparation, validation, and submission of regulatory returns required by the **South African Reserve Bank**"; "configurable rules engines"; "auditability" | SARB returns | [link](https://careers.capitecbank.co.za/job/Stellenbosch-Data-Engineer/1428315333/) |
| 22 | Capitec | Data Engineer (Client Engagement) | 5 | Stellenbosch | SQL, Python, Java, Spark, Hadoop, a cloud; ETL "with error handling and recovery mechanisms" | "pipelines for financial data analytics"; campaign data to Salesforce | — | [link](https://careers.capitecbank.co.za/job/Stellenbosch-Data-Engineer/1438443233/) |
| 23 | Capitec | Data Engineer (Client Engagement, senior) | 8–10 | Stellenbosch | Expert SQL, Python, Spark, AWS, **Kafka topics**, K8s, GitOps, IaC | Batch and streaming architecture | — | [link](https://careers.capitecbank.co.za/job/Stellenbosch-Data-Engineer/1439384533/) |
| 24 | Capitec | Data Engineer (talent community) | all levels | ZA | Python, SQL, AWS, Redshift, Terraform, Glue, Spark, streaming, Power BI exposure | Risk, product and client data | — | [link](https://careers.capitecbank.co.za/job/Data-Engineer/1425926633/) |
| 25 | Capitec | Analytics Engineer (talent pipeline) | 5 | ZA | Advanced SQL, Python, Airflow/Prefect, CI/CD, testing | Semantic layers, "well-tested data foundations" | Governance | [link](https://careers.capitecbank.co.za/job/Analytics-Engineer/1383766933/) |
| 26 | Capitec | Cyber Security Engineer (Incident Response) | 5 | Stellenbosch | AD, SQL, SharePoint, Windows/Red Hat | — | — | [link](https://careers.capitecbank.co.za/job/Stellenbosch-Cyber-Security-Engineer/1408756033/) |
| 27 | Capitec | Systems Engineer III (Linux Tech Lead) | 7+ | Sandton | RHEL, Satellite, AWS; Terraform, K8s, Python, **"AI (Claude Code)"** advantageous | — | — | [link](https://careers.capitecbank.co.za/job/Sandton-System-Engineer-III/1437691133/) |
| 28 | Capitec | Software Development Manager | 8+, 3–5 leading | Century City | AWS, event-driven architecture, observability, IaC | — | AWS certifications | [link](https://careers.capitecbank.co.za/job/Century-City-Software-Development-Manager-WC/1426851433/) |
| 29 | Capitec | Software Development Manager: Cash Devices | 8+ ATM | Stellenbosch | Postilion, ISO 8583, NCR/Diebold; Kafka, Azure, K8s advantageous | ATM switching, transaction flows | **PCI DSS, PCI PIN** | [link](https://careers.capitecbank.co.za/job/Stellenbosch-Software-Development-Manager/1428555833/) |
| 30 | Standard Bank | Engineer, Software JAVA | 5–7 / 8–10 | Johannesburg | Template: "API Engineering, Automation, Cloud Computing, Continuous Delivery" | — | — | [link](https://jobs.smartrecruiters.com/StandardBankGroup/744000149296020-engineer-software-java) |
| 31 | Standard Bank | Engineer, Business Support & Development, Murex | 5–7 / 8–10 | Johannesburg | Murex vendor platform | Market risk and collateral | "regulatory & risk management requirements" | [link](https://jobs.smartrecruiters.com/StandardBankGroup/744000151379049-engineer-business-support-development-murex-global-markets-technology-) |
| 32 | FirstRand (FNB, FR Life) | Developer | 7+ RPG | Johannesburg | RPG IV/ILE, IBM i, DB2 for i | — | — | [link](https://firstrand.wd3.myworkdayjobs.com/FRB/job/Johannesburg/Developer_R53844) |
| 33 | FirstRand (RMB) | UI Developer | 7+ | Johannesburg | Angular, NgRx, TypeScript, Node.js, Docker, Jenkins | — | Web security, XSS | [link](https://firstrand.wd3.myworkdayjobs.com/FRB/job/Johannesburg/UI-Developer_R53092) |
| 34 | FirstRand | Solutions Architect | senior | Johannesburg | APIs, cloud-native, DevSecOps | — | "regulatory compliance requirements" | [link](https://firstrand.wd3.myworkdayjobs.com/FRB/job/Johannesburg/Solutions-Architect_R53836) |
| 35 | FirstRand | Technology Platform Lead, DPMM | 10+ | Johannesburg | "Java (0 GC), C++ (low latency …), co-location, FIX Protocol" | Electronic trading, market making | Platform governance | [link](https://firstrand.wd3.myworkdayjobs.com/FRB/job/Johannesburg/Technology-Platform-Lead---DPMM--Digital-Pricing---Market-Making-_R53421-3) |
| 36 | Nedbank | Data Engineer | 3–6 | Johannesburg | **Azure Databricks, ADF, ADLS Gen2**, Ab Initio, SAS, Denodo, Netezza, **Kafka**, Hadoop, "IBM InfoSphere Data Replication", DB2/Postgres/MSSQL; Python, Java, SQL | "Regulatory Marts and Compliance Marts" | "data security and privacy" | [link](https://jobs.nedbank.co.za/job/Johannesburg-Data-Engineer/1408566533/) |
| 37 | Nedbank | Software Developer / Software Developer II (×3, one template) | 3+ | Johannesburg | **None named.** "IT Data structures, Application systems, Agile Development, SDLC" | — | — | [1](https://jobs.nedbank.co.za/job/Johannesburg-Software-Developer/1408728033/) · [2](https://jobs.nedbank.co.za/job/Johannesburg-Software-Developer/1410424233/) · [3](https://jobs.nedbank.co.za/job/Johannesburg-Software-Developer-II/1439362833/) |
| 38 | Nedbank | ACE Software Developer | 3 | Johannesburg | IBM App Connect Enterprise, Java, MQ, REST/SOAP, TLS | Integration flows | — | [link](https://jobs.nedbank.co.za/job/Johannesburg-ACE-Software-Developer/1366577033/) (closing date shown as 23 Feb 2026, still listed) |
| 39 | Nedbank | Engineering Lead (Architecture & Solution Design) | 8+ | Sandown | API-led integration, cloud-native/hybrid; TOGAF, Azure/AWS Solutions Architect, CKAD preferred | Digital mobile app and APIs | Governance forums | [link](https://jobs.nedbank.co.za/job/Johannesburg-Engineering-Lead-%28Architecture-&-Solution-Design%29/1437942233/) |
| 40 | Nedbank | Engineering Lead I | 6 | Johannesburg | Generic ("IT Architecture") | — | — | [link](https://jobs.nedbank.co.za/job/Johannesburg-Engineering-Lead-I/1408461633/) |
| 41 | Nedbank | Platform Owner: Postilion | 10+ payments | Johannesburg | ACI Postilion Realtime, PostBridge, Postilion Office | "transaction switching, acquiring, issuing … **clearing, settlement, reconciliation**"; "settlement integrity, **balancing controls, reconciliation processes**, and cryptographic key management" | **Visa, Mastercard, PCI-DSS, EMV, BankservAfrica** | [link](https://jobs.nedbank.co.za/job/Johannesburg-Platform-Owner-Postilion/1428715033/) |
| 42 | Absa | Senior Data Scientist (Advanced Coding Focus) | 7+ | Johannesburg | Python, R, TensorFlow/PyTorch/scikit-learn, SQL, Hadoop/Spark; MLOps advantageous | — | "Enterprise Wide Risk Management Framework" | [link](https://absa.wd3.myworkdayjobs.com/ABSAcareersite/job/Johannesburg/Senior-Data-Scientist--Advanced-Coding-Focus-_R-15989514) |
| 43 | Absa | QA Domain Lead | 8–12 | Randburg | CI/CD quality gates, API/UI automation, service virtualisation | Digital Business Bank | "regulated environment" | [link](https://absa.wd3.myworkdayjobs.com/ABSAcareersite/job/Randburg/QA-Domain-Lead_R-15991244-1) |
| 44 | Discovery (Group IS) | AI Developer | 3+ | Sandton | Java (certification), WebLogic, SOAP/REST, Azure/GCP, Git, unit testing; "**Ability to integrate AI into applications, APIs, automation, and data workflows**" | Group-wide, not bank-specific | — | [link](https://careers.discovery.co.za/job/Sandton-1-Discovery-Place-AI-Developer-GP-2196/1437629633/) |
| 45 | Discovery (Central Services) | Observability Engineer | 5+ | Gauteng | Dynatrace, Prometheus, Grafana, ELK, Datadog, OpenTelemetry, AWS, Azure, K8s; SLIs/SLOs/error budgets | Group-wide | ITIL | [link](https://careers.discovery.co.za/job/Matlala-Observability-Engineer-GP-2196/1436585933/) |

Rows 30 to 45 are bank templates. Rows 37, 30 and 40 name no stack at all, so their teams' stacks
cannot be inferred from the advert. That is itself a finding: **at the big four banks, the job
advert is a weak signal of the stack. At fintechs, it is a strong one.**

### Read for domain evidence, not counted

| Company | Title | What it contributes | URL |
|---|---|---|---|
| Ozow | Fraud Manager | "file Suspicious Activity Reports (SARs) in line with **FIC Act** obligations"; "FIC Act, POPIA, PASA/SARB oversight" as advantageous; "back-testing, tuning, and retirement of rules" | [link](https://job-boards.greenhouse.io/ozow/jobs/7986278003) |
| Mama Money | Recon & FinOps Manager | "own the daily reconciliation of payments and aggregator flows across multiple corridors and currencies"; "work closely with Data/Technology to **build automated/custom recons using partner data and internal transaction data**"; "variance reports"; "suspense items and outstanding exceptions" | [link](https://jobs.lever.co/mamamoney/5204d9c2-e552-44fb-bc95-216ec9acee40) |
| Mama Money | Senior BI / Data Analyst | dbt, dimensional models, semantic layers, "fraud patterns" | [link](https://jobs.lever.co/mamamoney/603e1e3e-2fda-4c4e-88ad-ef1fb299f679) |
| Moniepoint | Senior Data Analyst – Fraud (Poland) | SQL take-home; rule-based mitigations | [link](https://job-boards.eu.greenhouse.io/moniepoint/jobs/4943306101) |
| Discovery | Developer (clinical models, C/C++) | Health, out of domain | [link](https://careers.discovery.co.za/job/Sandton-1-Discovery-Place-Developer-GP-2196/1439522633/) |

### First-party stack pages

| Company | Source | What it says |
|---|---|---|
| Ozow | [ozow.com/tech-stack](https://www.ozow.com/tech-stack), read 2026-09-28 | "**ASP.NET Core**: Our go to server-side cross platform development framework"; "SQL Server & Postgres"; "DynamoDB & Redis … as our caching layers"; React and React Native; Docker, **ECS**, **AWS** (EC2, S3, RDS), TeamCity, Terraform; Selenium, Playwright, Postman, JMeter, k6 |
| Stitch | [Introducing the Stitch Tech Stack](https://stitch.money/blog/introducing-the-stitch-tech-stack) (published 2022-05-12, updated 2024-10-18) | TypeScript with Nact (an actor framework) and Koa; XState; Kubernetes, Helm, Tilt; GitHub Actions; Turborepo and pnpm; "Our OAuth2 and OpenId Connect framework is currently based on **Identity Server 4**" (a .NET library) |

### Unreachable, or nothing open

| Employer | Result |
|---|---|
| Yoco | Careers page reachable. Its `/api/careers` (HiBob) feed returned 4 roles, all sales. **No engineering open** |
| Stitch | Workable account `stitchmoney` exists; **0 jobs** |
| Peach Payments | BambooHR board reachable; 2 roles (COO, People Partner); no engineering |
| Luno | Greenhouse board reachable; 1 role (OTC Trader) |
| VALR, Paystack, Flutterwave | Workable accounts exist; 0 jobs. `paystack.com/careers` returned HTTP 403 |
| PayFast (Network International) | `payfast.io/careers/` returned HTTP 403 |
| Adumo | Careers page links to `adumo.bamboohr.com`, which now redirects to BambooHR's marketing site |
| TymeBank / Tyme | Careers pages reachable, but no job links and no ATS found. Tyme's engineering adverts found by search are in Vietnam (TymeX) |
| Bank Zero | No careers page found (404) |
| Retail Capital | The careers path redirects into the GoTyme business funding site |
| Investec | `investec.com` careers returned 403. The `careers.investec.co.za` search returns HTTP 202 with an empty body (a bot challenge). The one direct posting found, "Software Engineer (12764)", reads "Vacancy Closed". **Unreachable.** A search engine summary mentions a "Principal Full Stack .NET Engineer / Platform Architect" in Private Client Lending, but I could not read the body, so it is not counted |
| Capitec (older roles) | Five back-end and full-stack postings surfaced by search engines, whose summaries mention "C# and .NET Core", now return a closed page. Not counted. **Unverified** that the current back-end teams still use C# |
| Absa | Workday reachable. Only 2 technical postings open |

Reachability changed since 2026-09-23. Capitec's site returned a bot interstitial then and
worked today.

---

## 2. Reduced requirements

Counts are out of 45 unless a family is named. "Named" means required or preferred anywhere in
the body.

### By role family

| Family | n | Rows |
|---|---|---|
| **Data engineering, analytics engineering, data science** | **11** | 1, 8, 9, 11, 21–25, 36, 42 |
| Backend and software engineering (IC) | 10 | 5, 7, 12, 14, 20, 30, 32, 37, 38, 44 |
| Engineering leadership, architecture, platform ownership | 9 | 15, 17, 28, 29, 34, 35, 39, 40, 41 |
| QA and SDET | 5 | 2, 6, 16, 19, 43 |
| Security | 3 | 4, 10, 26 |
| Platform, cloud, SRE, observability | 3 | 13, 27, 45 |
| Frontend and mobile | 2 | 18, 33 |
| Vendor-platform engineering | 1 | 31 |
| Support engineering | 1 | 3 |

### Languages

| Language | Named in | Notes |
|---|---|---|
| **SQL** | 18 | All 11 data roles. The strongest single signal |
| **Java / Kotlin / Scala (JVM)** | 17 | *Required* in 4 of the 6 payments backends that name a language: Entersekt (Java 11+), Moniepoint (Java, 5+ years hands-on), Jumo (Kotlin/Java/Scala), Capitec (Java/Kotlin). The other two: Lesaka takes "Go, Java, C++, Rust, or similar"; iKhokha prefers Node.js. Also in QA roles, bank data roles as one of several, and trading |
| **Python** | 16 | 10 of the 11 data roles. In backend roles only once, as "an added advantage" (Jumo). Capitec's regulatory reporting role calls it "the core technical requirement" |
| TypeScript / JavaScript / Node | 5 | iKhokha (Node.js and TypeScript preferred), Jumo (TS + React in the stack), FirstRand (Angular), plus two QA roles |
| **C#** | **2** | iKhokha SDM ("Java, C#, Python etc.") and Kuda SDET ("working knowledge of C#"). First-party: Ozow backend on ASP.NET Core; Stitch auth on Identity Server 4 |
| Go | 2 | Lesaka switching (one of four), Lesaka cloud (scripting) |
| C / C++ | 2 | Lesaka switching, FirstRand trading |
| Legacy and vendor | 4 | RPG on IBM i, IBM ACE, Murex, Postilion |

The C# finding needs saying carefully. `2026-09-23-full-stack-tooling.md` found C# and .NET to
be the largest single backend ask across all South African listings. That is still true of the
general market. **In fintech and payments engineering specifically, on this day, the JVM
dominates and C# is a minority.** Both can be true. The sample includes no insurers and no
corporate or IT consultancies, which is where much of the local .NET demand probably sits
(**Unverified**).

### Data and platform

| Item | Named in | Notes |
|---|---|---|
| **AWS** | **22** | Primary cloud at Capitec, Ozow (first-party), Jumo, Lesaka, iKhokha, Moniepoint, Mama Money. Named services: Redshift, Glue, EKS, ECS, Lambda, DynamoDB, S3, RDS, Aurora, SQS, API Gateway, GuardDuty, Security Hub |
| Azure | 9 | Primary only at Nedbank (Databricks, ADF, ADLS Gen2). Elsewhere it is "AWS, Azure or GCP", or a migration source ("on-premise and Azure migrations to AWS", Lesaka) |
| Kubernetes | 14 | Much higher than in the 2026-09-22 postings |
| Terraform / IaC | 10 | Terraform is named, OpenTofu once, Terragrunt and Atlantis once |
| Kafka / streaming | 9 | Kafka by name in 6; Flink once; Kinesis once |
| **Spark** | **7** | Jumo, Capitec ×3, Nedbank, Absa, plus Ozow's Databricks |
| Databricks | 2 | Ozow (preferred), Nedbank (Azure Databricks) |
| **Delta Lake** | **0** | Not named anywhere |
| Warehouses | 5 | Redshift (Jumo, Capitec, Lesaka), Snowflake (Capitec advantage, Lesaka), BigQuery (Lesaka) |
| Airflow / orchestration | 6 | Airflow ×4, Prefect, Dagster, NiFi |
| Postgres | 5 | MySQL 4, SQL Server 3, DynamoDB 3 |
| dbt | 0 engineering | 1 analyst |
| Observability | 6 | Datadog ×4, OpenTelemetry, Prometheus, Grafana, Dynatrace; SLOs and error budgets ×2 |

### Domain concepts

| Concept | Named in | Where |
|---|---|---|
| Card, scheme and terminal (EMV, ISO 8583, 3DS, Postilion, card present / not present) | 8 | Entersekt ×2, Capitec ×2, Lesaka, iKhokha, Nedbank, Moniepoint |
| **Settlement and reconciliation** | **3 engineering** (+1 domain) | Lesaka "reconciliation data"; Nedbank "settlement integrity, balancing controls, reconciliation processes"; Capitec "authorise, settle and report". Mama Money's recon role asks Tech to build recons |
| **Idempotency, ordering, transaction integrity** | **3** | Lesaka "correctness, ordering, and idempotency"; Capitec "transaction integrity"; Moniepoint "high-throughput, distributed transactional systems" |
| Lending and credit | 2 | Jumo ×2 |
| Regulatory reporting | 2 | Capitec (SARB returns), Nedbank ("Regulatory Marts") |
| Multi-currency, cross-border | 2 | Moniepoint, Mama Money |
| **Ledger, double-entry** | **0** | — |
| Fraud as engineering | 0 | Only the Ozow Fraud Manager (non-engineering). Consistent with `2026-09-23-fraud-and-bank-apis.md` |
| KYC / AML / FICA in an engineering body | 0 | — |
| Open banking, PayShap | 0 | Ozow sells PayShap Request on its product pages. No posting names it |
| LLM integration as a requirement | 1 | Discovery AI Developer |

### Compliance

| Regime | Engineering postings | Where |
|---|---|---|
| **PCI DSS** (and PCI PIN, PTS, PA-DSS) | **6** | Ozow security, Entersekt backend, Lesaka cloud, Capitec ×2, Nedbank |
| POPIA | 1 | Ozow security. Plus the non-counted Ozow Fraud Manager |
| GDPR | 1 | Entersekt |
| SARB | 2 | Ozow ("relevant SARB directives"), Capitec (regulatory returns) |
| SOX | 1 | Lesaka ("SOX ITGC 404") |
| ISO 27001, NIST, CIS, OWASP | 3 | Ozow, Lesaka, Entersekt |
| Card schemes, BankservAfrica | 2 | Nedbank, Entersekt ("scheme certification") |
| FIC Act, FSCA, FICA | **0** | Only in the non-counted fraud role |
| "Clear criminal and credit record" | 10 | Every Capitec posting, as a condition of employment |
| "Regulated environment", unqualified | 6 | Moniepoint, Entersekt, Lesaka, Absa ×2, Discovery |

### What the regulators' own pages say, for the ones the postings name

- **PCI DSS.** PCI SSC published v4.0.1 on 11 June 2024. "PCI DSS v4.0 will be retired on 31
  December 2024. After that point, PCI DSS v4.0.1 will be the only active version." The
  future-dated requirements took effect on 31 March 2025
  ([PCI SSC blog](https://blog.pcisecuritystandards.org/just-published-pci-dss-v4-0-1)).
  **Lesaka's advert asks for "PCI DSS 3.2.1 and 4.0.0". Both are now retired versions.** It is
  a useful reminder that adverts lag the standard.
- **SARB and the NPS.** The SARB states it has "legal responsibility for the national payment
  system (NPS)", and that PASA "organizes, manages and regulates the participation of its
  members in the payment system"
  ([SARB payments and settlements](https://www.resbank.co.za/en/home/what-we-do/payments-and-settlements)).
  Its Payments Ecosystem Modernisation programme describes a new RTGS "capable of … providing
  richer data within payment messages"
  ([PEM](https://www.resbank.co.za/en/home/what-we-do/payments-and-settlements/pem)).
  **Unverified inference:** that is the ISO 20022 migration. Open banking status is as recorded
  in `2026-09-23-fraud-and-bank-apis.md` Q2. The SARB describes PayShap, launched 13 March 2023
  under BankservAfrica (now PayInc) and PASA, as supporting its NPS reforms
  ([SARB press release](https://www.resbank.co.za/content/dam/sarb/publications/media-releases/2023/payshap-/Press%20release%20on%20the%20launch%20of%20Payshap%20-%20a%20digital%20payment%20service.pdf)).
- **Cyber resilience.** The FSCA and PA published Joint Standard 2 of 2024 on 15–16 May 2024.
  "The Joint Standard is envisaged to commence on 1 June 2025"
  ([Joint Communication 2 of 2024](https://www.resbank.co.za/content/dam/sarb/publications/prudential-authority/pa-public-awareness/covid-19-response/2024/joint-comms-2-of-2024/Joint%20Communication%202%20of%202024%20-%20Publication%20of%20the%20Joint%20Standard%20-%20Cybersecurity%20and%20cyber%20resilience.pdf)).
  **Unverified inference:** this is the likely referent of Ozow's "relevant SARB directives"
  alongside Directive 2 of 2024.
- **POPIA.** The Information Regulator: "the responsible party must secure the integrity and
  confidentiality of the personal information by taking reasonable, technical and
  organisational measures". A compromise must be notified to the Regulator and to data subjects
  "as soon as reasonably possible", through its eServices portal
  ([inforegulator.org.za/popia](https://inforegulator.org.za/popia/)).
- **FIC Act.** Accountable institutions keep "transactional information for a period of 5 years
  from the date a transaction is concluded". They file cash threshold reports for "cash received
  or issued exceeding R49 999.99", plus suspicious and unusual transaction reports under section
  29. They maintain a risk management and compliance programme under section 42
  ([FIC reference guide for all accountable institutions](https://www.fic.gov.za/wp-content/uploads/2023/09/2022.12-CG-FIC-Act-reference-guide.pdf)).
  No engineering posting names these. Record-keeping and auditability do recur (Capitec
  "auditability", Entersekt "audit evidence", Lesaka "SOC … reports").

### Must-haves and nice-to-haves, weighted

**Must-have** means it recurs as a requirement across the family the user would target. It is
not a count of every mention.

| Must-have | Evidence |
|---|---|
| SQL at depth (modelling, query optimisation, indexing) | 18 of 45; all 11 data roles; Entersekt backend ("Schema design, Query optimisation and indexing") |
| Python (data) or a JVM language (payments backend) | Python in 10 of 11 data roles; JVM required in 4 of 6 language-named payments backends |
| AWS, used in production | 22 of 45; primary at 7 of the 8 employers that name a primary cloud (Nedbank, on Azure, is the exception) |
| Production pipelines with error handling, recovery and data quality | Capitec ×4 ("error handling and recovery mechanisms"), Lesaka, Jumo, Nedbank, Ozow |
| Containers and Kubernetes; CI/CD; Git | K8s 14; CI/CD in most bodies |
| Infrastructure as code (Terraform) | 10 |
| Transaction correctness: idempotency, ordering, integrity, settlement, reconciliation | Every payments backend and payments-data role that describes its domain |
| Secure coding and handling of sensitive data (OWASP, PII, cardholder data) | Entersekt, Ozow, iKhokha, Capitec |
| Years in production, stated as a floor | 30 of 45 set a floor of 5+ years |

| Nice-to-have | Evidence |
|---|---|
| Spark / Databricks | 7 / 2, all data |
| Kafka or streaming | 9 |
| Airflow or another orchestrator | 6 |
| A warehouse: Redshift, Snowflake | 5 |
| Datadog / OpenTelemetry / SLOs | 6 |
| Payments or fintech experience "a plus" | Ozow, Entersekt, Jumo, Lesaka |
| AWS certifications (Cloud Practitioner, Solutions Architect, Security Specialty) | Capitec ×2, Lesaka, Ozow, Discovery, Nedbank |
| PCI DSS familiarity | 6, concentrated in security, cloud and card roles |
| AI in the product | 1 required, 6 mentions |

---

## 3. Role archetypes

### Target 1: Data engineer at a bank or fintech (primary)

It is the largest family in the sample. It is the only family with openings at every level, from
Lesaka's 1–2 years to Capitec's 8–10. It is the family whose stack most closely matches the
curriculum's deepest pillar (Python, SQL, Spark, streaming, orchestration). It is also where the
fintech-specific work is data-shaped: regulatory returns with "auditability" (Capitec), moving
"reconciliation data" (Lesaka), "Regulatory Marts" and data replication (Nedbank), lending data
(Jumo). Capitec's regulatory reporting role is the single closest match in the whole sample to
what `platform` and `parity` already are: "replaces manual, spreadsheet-driven processes with a
scalable, Python-based solution that enhances data quality, **auditability**", with "configurable
rules engines" and "error handling and recovery mechanisms".

The honest gap is the same one `2026-09-22-sa-target-roles.md` names, with AWS added. The floors
are 5 years in data engineering, AWS in production, and Python-first. The day job supplies
production years in C#, not in AWS data engineering.

### Target 2: Backend engineer on transactional or payments services (secondary)

This family carries the most fintech-specific content: idempotency, ordering, settlement,
transaction integrity, card flows. It also rewards the production C# years most directly, but
only at the minority of shops that run .NET (Ozow is the one first-party confirmation). Most
payments backends in this sample demand the JVM, and demand it in years. Lesaka's "or similar" and
iKhokha's Node.js are the exceptions. This is the door to
keep open, not the one to build the whole plan around.

### Target 3, conditional: platform or cloud engineer at a fintech

Lesaka's Senior Cloud Engineer (3+ years AWS, Terraform, K8s, ArgoCD, PCI DSS) and Jumo's stack
are reachable if Phase 10 is built on AWS rather than Azure. Keep it as a side door. It is not a
third target to plan for.

### Avoid

| Archetype | Why |
|---|---|
| Card, terminal and ATM engineering (EMV, ISO 8583, Postilion, PCI PIN) | A closed loop, like SAS AML. "8+ years of direct ATM domain experience", "Postilion (Essential)", "Practical experience with EMV protocol". Hardware and scheme certification can't be learned outside an acquirer. Know the vocabulary; don't target it |
| Fraud engineering | Still absent as an engineering family. `2026-09-23-fraud-and-bank-apis.md` stands |
| Low-latency trading | "Java (0 GC), C++ … co-location, FIX Protocol" and 10+ years |
| Vendor and legacy platforms (Murex, IBM ACE, RPG on IBM i, Ab Initio) | Years in the vendor product is the filter |
| Security analyst or pentester | 8+ years offensive at Ozow; 5 years incident response at Capitec |
| Leadership, architecture and platform-owner roles | 9 of 45, with floors of 8–10+ years and "managing managers" |
| QA and SDET | Real and reachable, but a detour from all four pillars |
| Generic bank "Software Developer" templates | They name no stack, so no portfolio can be aimed at them. Apply if they appear; don't plan for them |

---

## 4. Stack implications, directly

**C# for `product`: keep it, and stop describing it as the market default for this target.**
The five production years in C# are the only production years there are. Postings count years in
the stack they name, so a Kotlin repository with no Kotlin years would not get past the filters
that make the JVM matter. C# on ASP.NET Core and Postgres is what Ozow runs (first-party), and a
C# transactional service is legible to every JVM shop: the concepts, not the syntax, are what
Entersekt's and Moniepoint's bodies describe. What changes is the claim. The curriculum's line
that C# is "the largest single backend ask in South Africa" is true of the general market and
false of payments. Say so on the page. **If the user chooses Target 2 as primary, a Kotlin +
Spring Boot module in `worked-examples` is the one addition to consider** (see open questions).
It would be a module, not a rewrite of `product`.

**Python for data: confirmed.** 10 of 11 data roles.

**PySpark and Delta: Spark holds, and Delta is a free choice, not a market signal.** Spark is
named in 7 postings, all of them data roles at employers the user would target. Delta is named in
none. Databricks is named twice, once on Azure. The warehouse vocabulary is Redshift and
Snowflake. Keep Delta as the table format: it is what Databricks uses, and the choice is already
recorded. But add a warehouse-shaped gold layer (Redshift-compatible SQL, or Snowflake as the
comparison) to the replatform's write-up, because that is what these data teams load into.

**Kafka, via Redpanda: holds.** 9 postings name streaming. Kafka is the only broker named by
product.

**The cloud: flip it to AWS.** This is the largest stack change the evidence forces. The
curriculum runs "Azure throughout, with AWS equivalents noted". It targets DP-750 (Azure
Databricks) and AI-200 (Azure), and Phase 10 deploys to Azure Container Apps. For this audience
it should be the other way around. AWS is primary (ECS or EKS, RDS Postgres, S3, Glue or EMR for
Spark, MSK or Kinesis for streaming, Lambda). Azure equivalents go in the notes. The data
certification becomes AWS-shaped (**Unverified** which exam; the postings name only AWS Cloud
Practitioner, Solutions Architect, Security Specialty, "AWS Glue" learning and Terraform
Associate). Nedbank is the one Azure-Databricks employer. It is also the one Johannesburg data
role with a real stack, which is a reason to keep the Fabric and Databricks module rather than
delete it.

**Kubernetes and Terraform: promote them.** 14 and 10 mentions. The curriculum treats Terraform
as a Phase 10 item and Kubernetes as a Phase 10 reading. The fintech postings treat both as
baseline.

**React and TypeScript: holds, as the front.** React is Ozow's and Jumo's front-end (both
first-party). Angular appears once (RMB). No change to the `2026-09-23-full-stack-tooling.md`
position.

**Applied AI: demote from pillar-with-headline to evals-as-craft.** One requirement in 45. Keep
the evals discipline, because it is testable and rare. Stop leading with it.

---

## 5. Project implications

### `platform`: keep it, reframe `parity` as reconciliation, and keep WideWorldImporters

**The replatform stays as specified.** Its oracle, the shipped warehouse matched to the cent, is
the reason it is worth building, and nothing in the fintech sample offers a better public oracle.
Replatforming bank SQL to Spark is live work: Nedbank lists MSSQL, DB2 and Ab Initio next to
Azure Databricks, and Capitec is replacing "spreadsheet-driven processes" with Python. That
WideWorldImporters is a wholesale distributor, not a bank, costs one sentence in the README, not
a rebuild.

**`parity` is already a reconciliation engine. Say so.** What Nedbank calls "balancing controls,
reconciliation processes", Mama Money calls "custom recons using partner data and internal
transaction data", and Lesaka calls "reconciliation data" is the same operation `parity` does:
compare two SQL-queryable sources with tolerances, and report matches, breaks and their causes as
evidence a sceptic accepts. The change is vocabulary and one use case, not architecture:

- Document both uses: *migration parity* (old warehouse against new gold) and *transaction
  reconciliation* (internal ledger against an external statement or settlement file).
- Add the reconciliation terms to the report: matched, unmatched on each side, amount breaks,
  timing breaks (T+n), duplicates, aged exceptions, and a suspense total that must net to zero.
- Keep the evidence report CI-shaped. "Auditability" and "audit evidence" are the fintech words
  for what the report already is.

**The ingestion service stays.** CDC into Redpanda into Delta, with idempotent merge, replay and
dead letters, is the "correctness, ordering, and idempotency in transaction flows" line from
Lesaka's switching role, done on data. Change one thing: add the ledger's event stream (below)
as a second source next to Municipal Money. If Municipal Money polling no longer feeds a product,
drop it.

### `product`: same stack, new domain. A payments ledger, reconciled

**The municipal finance explorer does not survive a fintech reader, and polishing it will not
fix that.** It proves the full-stack, OIDC and assistant mechanics, but none of the domain words
the postings use: idempotency, ordering, settlement, reconciliation, transaction integrity,
audit, sensitive data. A read-only explorer over public Treasury figures cannot force them. So
`product` keeps its repository, its stack (C#, ASP.NET Core, Postgres, React, OIDC, one
assistant with evals) and its place as system two of two. Its domain changes.

**Recommendation: `product` becomes a small merchant payments service with a double-entry ledger
at its core, reconciled daily against an external statement using `parity`.** In thin vertical
slices, as the curriculum already demands:

1. **A double-entry ledger** in Postgres. Accounts, journal entries, append-only postings;
   balances derived, never stored as the source of truth.
2. **An idempotent payments API**. `Idempotency-Key` on every write, a payment state machine
   (created, authorised, captured, settled, refunded, reversed), and optimistic concurrency.
3. **Outbound events** via a transactional outbox into the ingestion service's Redpanda, and
   webhooks to merchants with at-least-once delivery and signed payloads.
4. **Daily settlement**: generate a settlement file, then reconcile it with `parity` against an
   external statement. Use two statement sources. The first is a seeded simulated
   acquirer/bank statement, with injected breaks the generator knows about. The second is the
   **Investec Programmable Banking sandbox**, which `2026-09-23-fraud-and-bank-apis.md` confirmed
   is open, with published credentials, and callable from Johannesburg. It is used as a real SA
   bank API shape, not as real money.
5. **A React back-office**: payments, breaks queue, audit trail, OIDC login with roles (operator,
   approver). Manual adjustments need a second approver. That is Mama Money's "valid business
   reason, complete supporting evidence, appropriate approval", as a feature.
6. **The assistant, demoted and sharpened**: it explains a reconciliation break, with citations
   to the ledger rows and statement lines it read, gated by evals. It keeps the Phase 8
   mechanics and loses the headline.

**The oracle is stronger than the explorer's was**, which is the curriculum's fourth test:

| Check | Pass/fail answer |
|---|---|
| Every journal entry nets to zero | Invariant, property-tested |
| Derived balances equal the replay of all postings from zero | Byte-for-byte replay |
| Retrying any write with the same idempotency key produces exactly one posting | Concurrency test under fault injection |
| Reconciliation finds exactly the breaks the generator injected, and no others | Seeded ground truth |
| The assistant's cited rows exist and support its explanation | Eval set, judge limits written down |

**What this costs, stated honestly.** It fails half of the curriculum's second test ("someone
else could use it") as strongly as the explorer passed it: journalists were real users, and a
reference payments ledger has developers at most. **Unverified inference:** a fintech reviewer
weighs "the domain I hire for, done correctly" above "real users in an unrelated domain". The
user should decide that (open question 5).

**What it must not become:** a card processor. No PANs, no EMV, no ISO 8583, no PCI scope. The
README's non-claims say so first: "no cardholder data, no PCI DSS scope; synthetic data only;
POPIA-conscious by construction". Those lines are themselves evidence of judgement, because the
postings treat PCI and POPIA as scope, and scope is exactly what a careful engineer states.

**What happens to Municipal Money:** it leaves `product`. The typed client
(`MunicipalMoney.Client` on NuGet, or `municipal-money` on PyPI) can survive as a small
standalone package if the user wants to keep it. It stops being a system.

**No fifth system.** The ledger replaces the explorer inside `product`. The fraud deep-dive's
stream becomes the ledger's event stream, which is more realistic than the one it had.

---

## 6. Profile implications, updating `2026-09-26-github-profile-landing.md`

That file's structure stands: remove the employer, stop pointing at the plan, and let each ship
add one line and one pin. What changes is the order and the words, for a fintech reader.

1. **The bio line.** Change it from "I build data pipelines and the products that sit on them —
   Python and Spark underneath, C# and React on top, model APIs where they earn their place" to
   something that leads with correctness. Draft: "Software engineer in Johannesburg. I build
   data pipelines and transactional services that have to add up — Python, Spark and SQL for
   data; C# and Postgres for services." Add "on AWS" only once something ships on AWS.
2. **The day-job bullets, reordered.** "Offline-first desktop and tablet apps that keep working
   without signal and **reconcile when it returns**" is the most fintech-relevant sentence on the
   page: idempotent sync and conflict reconciliation. Move it first. Move "ERP-to-cloud
   integration so operational data stops being re-keyed" second. That is data integrity between
   systems of record. Keep the employer unnamed, as before.
3. **Pins and the ship ladder, re-ranked.**
   - `parity` stays first. Its start-here line becomes: "**parity** — prove two systems agree:
     row-level reconciliation with tolerances, and an evidence report a reviewer can check".
   - `platform` second.
   - `product` third, with a new line: "**product** — a double-entry payments ledger with
     idempotent APIs, reconciled daily; OIDC back-office; an assistant that explains breaks, gated
     by evals".
   - `municipal-money` drops off the ladder, or becomes "earlier work".
4. **A non-claims line on the profile, not only in the repo.** "Synthetic data only. No
   cardholder data, no PCI scope." For this audience it reads as competence (**Unverified**
   inference, consistent with the 2026-09-26 file's rule that the page never shows a rung before
   it is reached).
5. **No "fintech" in the title until something fintech ships.** Same rule as the badges.
6. **Topics on the repos**: `reconciliation`, `double-entry`, `idempotency`, `payments`,
   `aws`, `pyspark`, `kafka`. These are the words the postings use.

---

## 7. Open questions only the user can answer

1. **Is Cape Town, Stellenbosch or KwaZulu-Natal possible, or is it Johannesburg and remote
   only?** 15 of 45 postings are in the Western Cape, 2 in KZN, 9 remote-SA, and 17 in Gauteng.
   The Gauteng ones skew towards bank templates, legacy and leadership. If relocation is out,
   the realistic list is remote-first fintechs (Jumo, Entersekt, Moniepoint) plus the few modern
   Johannesburg data roles (Nedbank on Azure Databricks). That changes whether the Azure material
   stays.
2. **Data engineer first, or payments backend first?** The recommendation is data first. If
   the user's own preference is backend, the JVM question becomes live: add a Kotlin + Spring
   Boot module, or accept a .NET-shop-only backend target.
3. **Is there any production AWS at the day job, or only Azure?** The AWS flip is cheap if some
   exists and expensive if none does. It also decides which certification replaces DP-750 and
   AI-200.
4. **Banks, fintechs, or both?** Banks carry conditions the fintechs don't: "clear criminal and
   credit record" on every Capitec posting, employment-equity clauses on most bank postings, and
   template adverts with no stack. Whether any of that matters is the user's call.
5. **Is replacing the municipal finance explorer acceptable?** It had real users. The ledger
   has a stronger oracle and the right domain, but developers at most as users. That trade is
   the user's, not the evidence's.
6. **Keep the Municipal Money client package at all?** It is a real South African public-data
   niche. It is also no longer on the path.
7. **Where does SQL Server sit?** The replatform starts from T-SQL. Several SA banks run MSSQL
   or DB2. Ozow runs SQL Server and Postgres. Nobody in this sample names T-SQL as a
   requirement, but the day job may already give production T-SQL years. If it does, they are
   worth stating.

---

## 8. Addendum, 2026-09-29: Investec, from postings the user supplied

Investec was unreachable on 2026-09-28 (bot challenge). On 2026-09-29 the user pasted the full
text of five earlier Investec postings. Two are duplicates, so there are **three distinct
roles**. They were not read on Investec's site, their open and close dates are unknown, and
they are **not counted** in the tables above. They are, however, full bodies in the employer's
own wording, which is the standard this file uses.

| # | Title | Team | Location | Required stack | Domain and compliance |
|---|---|---|---|---|---|
| I-1 | .NET Engineer / Software Engineer (same body under two titles) | Client Digital Experience | Sandton | C#, .NET Core / Framework REST APIs; **OAuth2, OIDC, token management**; Apigee or **Azure API Management**; unit and integration testing; Angular or React | "externally facing APIs that power Investec's **UK Open Banking** ecosystem … share data, **initiate payments**"; "financial-grade APIs"; rotational standby. Advantageous: Azure, Terraform/ARM/**Bicep**, Cosmos DB/MongoDB, PowerShell, "responsible" AI tooling |
| I-2 | Fullstack Engineer | Business and Commercial Banking | not stated (BCB Technology) | 5+ years Microsoft stack; C#, .NET Core APIs and microservices; **SQL Server / Azure SQL "data modelling and performance optimisation"**; Angular (v8+) and/or React; TypeScript; Azure App Services, Functions, containers; **Azure DevOps** pipelines; Docker, Kubernetes; Terraform or Bicep; GitOps | "Integrate solutions with internal platforms (e.g. D365, **AML, KYC**)"; client life-cycle journeys; production support |
| I-3 | Full Stack Engineer / Software Developer (same body under two titles) | not stated | Sandton | 5+ years; C# ASP.NET APIs (.NET Framework, Core, 6+); **TypeScript with Angular 2+**; git; REST; unit and integration tests; CI/CD; Kubernetes and Azure | Helpful: Azure DevOps, MSSQL. Advantageous: Jasmine/Karma/Jest/NUnit/**xUnit**, **Playwright**, Azure and AWS, Docker |

What this changes:

- **A Microsoft-stack fintech target exists, and it is in Johannesburg.** All three are C# and
  .NET on Azure, and the two with a stated location are in Sandton. That answers the section 7
  worry that Gauteng is only bank templates and legacy work. The 45-posting sample under-counted
  .NET because Investec, the most .NET-shaped employer on the list, could not be read.
- **Angular is in all three, and React is only ever the alternative.** I-3 requires Angular 2+
  and does not mention React. The curriculum's React-over-Angular choice costs something at
  Investec.
- **None of them is a data role.** The data asked for is I-2's SQL Server modelling and
  performance work. At Investec, "C# engineer who is strong in data" means strong SQL Server
  inside a full-stack role, not Spark.
- **Security is concrete and matches the plan:** OAuth2/OIDC, token handling, API gateways.
  I-1 is open banking, which ties back to the Investec sandbox in `2026-09-23-fraud-and-bank-apis.md`.
- **The recurring baseline across all three:** Azure DevOps pipelines, containers and Kubernetes,
  Terraform or Bicep, unit and integration tests (xUnit or NUnit), production support.

---

## Sources

All read 2026-09-28. Posting URLs are in the tables above; the load-bearing ones are repeated
here.

**ATS endpoints used**
- Greenhouse boards: `boards-api.greenhouse.io/v1/boards/{ozow,entersekt,moniepoint,luno}/jobs?content=true`
- Lever: `api.lever.co/v0/postings/mamamoney`
- Workable: `apply.workable.com/api/v1/widget/accounts/{kuda,stitchmoney,valr,paystack,tymeglobal,flutterwave,luno}`
- SmartRecruiters: `api.smartrecruiters.com/v1/companies/{StandardBankGroup,iKhokha}/postings`
- Workday CXS: `absa.wd3.myworkdayjobs.com/wday/cxs/absa/ABSAcareersite/jobs`, `firstrand.wd3.myworkdayjobs.com/wday/cxs/firstrand/FRB/jobs`
- SuccessFactors search: `careers.capitecbank.co.za/search/`, `jobs.nedbank.co.za/search/`, `careers.discovery.co.za/search/`
- HiBob via the employer's page: [jumo.world/careers](https://jumo.world/careers/); Yoco `www.yoco.com/api/careers`
- simplify.hr: `lesakatech.simplify.hr/vacancy/vacancies`
- BambooHR: `peachpayments.bamboohr.com/careers/list`

**Load-bearing postings**
- Capitec, Data Engineer, Regulatory Reporting Automation: <https://careers.capitecbank.co.za/job/Stellenbosch-Data-Engineer/1428315333/>
- Capitec, Software Engineer: Back-End II (Android / Payments): <https://careers.capitecbank.co.za/job/Stellenbosch-Software-Engineer-Back-End-II-%28Android-Payments%29/1437424833/>
- Lesaka, Senior Backend Engineer (Switching Systems): <https://lesakatech.simplify.hr/Vacancy/182780>
- Lesaka, Junior Data Engineer (EasyPay): <https://lesakatech.simplify.hr/Vacancy/193194>
- Lesaka, Senior Cloud Engineer (AWS): <https://lesakatech.simplify.hr/Vacancy/174971>
- Jumo, Software Engineer: <https://jumo.careers.hibob.com/jobs/8ef3d748-1da1-4a0b-bba8-04b84f0c3e37>
- Entersekt, Senior Software Engineer: 3DS Payments: <https://job-boards.greenhouse.io/entersekt/jobs/6008895004>
- Moniepoint, Head of Engineering, Payment Gateway (Remote, South Africa): <https://job-boards.eu.greenhouse.io/moniepoint/jobs/4971819101>
- Nedbank, Platform Owner: Postilion: <https://jobs.nedbank.co.za/job/Johannesburg-Platform-Owner-Postilion/1428715033/>
- Nedbank, Data Engineer: <https://jobs.nedbank.co.za/job/Johannesburg-Data-Engineer/1408566533/>
- Mama Money, Recon & FinOps Manager: <https://jobs.lever.co/mamamoney/5204d9c2-e552-44fb-bc95-216ec9acee40>
- Ozow, Senior Security Analyst: <https://job-boards.greenhouse.io/ozow/jobs/8000434003>

**First-party stack**
- Ozow tech stack: <https://www.ozow.com/tech-stack>
- Stitch, "Introducing the Stitch Tech Stack": <https://stitch.money/blog/introducing-the-stitch-tech-stack>

**Regulators and standards bodies**
- PCI SSC, "Just Published: PCI DSS v4.0.1": <https://blog.pcisecuritystandards.org/just-published-pci-dss-v4-0-1>
- SARB, payments and settlements: <https://www.resbank.co.za/en/home/what-we-do/payments-and-settlements>
- SARB, Payments Ecosystem Modernisation: <https://www.resbank.co.za/en/home/what-we-do/payments-and-settlements/pem>
- SARB, PayShap launch press release: <https://www.resbank.co.za/content/dam/sarb/publications/media-releases/2023/payshap-/Press%20release%20on%20the%20launch%20of%20Payshap%20-%20a%20digital%20payment%20service.pdf>
- FSCA and PA, Joint Communication 2 of 2024 (Joint Standard 2 of 2024, cybersecurity and cyber resilience): <https://www.resbank.co.za/content/dam/sarb/publications/prudential-authority/pa-public-awareness/covid-19-response/2024/joint-comms-2-of-2024/Joint%20Communication%202%20of%202024%20-%20Publication%20of%20the%20Joint%20Standard%20-%20Cybersecurity%20and%20cyber%20resilience.pdf>
- Information Regulator, POPIA: <https://inforegulator.org.za/popia/>
- FIC, Reference guide for all accountable institutions: <https://www.fic.gov.za/wp-content/uploads/2023/09/2022.12-CG-FIC-Act-reference-guide.pdf>

**Earlier files this extends**
- `research/2026-09-22-sa-target-roles.md`
- `research/2026-09-23-fraud-and-bank-apis.md` (Investec sandbox, open banking status, fraud market)
- `research/2026-09-23-full-stack-tooling.md` (C# as the general-market backend ask)
- `research/2026-09-23-data-stack-and-certifications.md`
- `research/2026-09-26-github-profile-landing.md`
