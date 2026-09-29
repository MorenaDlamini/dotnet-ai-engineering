# Where to get deep fintech domain knowledge, and whether Coursera is the place

Research for one question: **where can a C# engineer with five years of production work get the
domain knowledge a bank or payments company expects, and is Coursera a good source for it?**
"Deep" means what the engineer on a ledger, payments or open-banking team needs to know. It does
not mean investor-level or business-school fintech.

The target is fixed by `2026-09-28-sa-fintech-target-roles.md`: a .NET full-stack engineer at a
South African fintech or bank, with SQL Server as the edge. The build is the payments ledger in
`product`: double-entry, an idempotent payments API, an outbox, daily settlement reconciled by
`parity` against a bank statement, an Angular back-office with dual approval, and OIDC-protected
open-banking-style APIs. The Investec postings in section 8 of that file ask for UK Open Banking,
"financial-grade APIs", OAuth2/OIDC and AML/KYC integration. This file finds the sources that teach
those things.

It extends `2026-09-23-fraud-and-bank-apis.md` and does not repeat it. That file already covers
SA open-banking regulation (Directive 2 of 2024, the draft PISP framework, IFWG and FSCA papers),
the Investec Programmable Banking sandbox, and POPIA for a personal project. They are referenced
here, not restated.

Everything was read on **2026-09-29**, on the page that owns the fact. Course pages were read on the
provider's own site. Books are described only from the publisher's or author's page. Inference is
marked **Unverified**. No prices are given, only the access model. Sources that could not be
reached are listed in the Sources section, not guessed at.

---

## The verdict

**Coursera is not where deep fintech knowledge lives. The primary sources are free, and they are
better: first-party engineering writing from ledger and payments companies, the standards
themselves, and the South African regulators' and operators' own documents. Coursera has two
narrow uses. One is Wharton's *Introduction to Financial Accounting*, free to audit, for
debits, credits and journal entries. The other is a three-hour ISO 20022 short course for a first
hands-on look at `camt.053`. Everything else in its fintech catalogue is business-level.**

Why, in five points:

1. **Every Coursera fintech programme on the first page of its own search is labelled Beginner.**
   That covers Michigan, HKUST, Oxford Saïd, Duke, UCT, INSEAD and Copenhagen Business School
   ([Coursera search "fintech"](https://www.coursera.org/courses?query=fintech)). What you do in
   them is quizzes, peer-graded essays, value propositions and business plans. None has you build
   or model a ledger, a payment state machine or a reconciliation.
2. **The best-known payments course is gone.** The Wharton FinTech specialization and its
   *FinTech: Foundations, Payments, and Regulations* course return HTTP 404 on coursera.org
   ([specialization](https://www.coursera.org/specializations/wharton-fintech),
   [course](https://www.coursera.org/learn/wharton-fintech-overview-payments-regulations)).
   **Unverified:** retired or moved.
3. **The regulation courses teach US, Hong Kong and generic policy.** Duke's *FinTech Law and
   Policy* teaches "Banking Regulation in the U.S." HKUST's RegTech teaches KYC and AML in
   general, and the UK open-banking initiative as a module
   ([Duke](https://www.coursera.org/learn/fintechlawandpolicy),
   [HKUST RegTech](https://www.coursera.org/learn/regtech)). None of them covers the SARB, PASA,
   the FIC Act, POPIA or the Joint Standards.
4. **The local university options are also business-level.** UCT's Coursera specialization and
   its GetSmarter short course both end in a business plan and a pitch
   ([UCT on Coursera](https://www.coursera.org/specializations/fintech-startups-emerging-markets),
   [UCT GetSmarter](https://www.getsmarter.com/products/uct-fintech-disruption-in-finance-online-short-course)).
   Wits' MCom Financial Technology requires "an average of at least 65% for Honours in Finance"
   ([Wits](https://www.wits.ac.za/course-finder/postgraduate/clm/mcom-financial-technology/)).
5. **The engineering knowledge the ledger needs is published first-party and free.** Modern
   Treasury has a three-part *Accounting for Developers* series and a six-part *How to Scale a
   Ledger* series. TigerBeetle documents debit-credit, two-phase transfers and correcting
   transfers. Square has published its immutable double-entry *Books* design. Stripe documents
   exactly how its idempotency keys behave. The SA payment system is best learned from the
   SARB, PayInc and PASA Academy.

**The recommended set, one per need:**

| Need | Source | Access |
|---|---|---|
| Accounting for engineers | Modern Treasury *Accounting for Developers* I–III, then Kleppmann's *Accounting for Computer Scientists*. Wharton's *Introduction to Financial Accounting* for drill | Free / free / free to audit |
| Ledger design | TigerBeetle docs (Debit-Credit, Two-Phase Transfers, Correcting Transfers, Reliable Transaction Submission), Square *Books*, Modern Treasury *How to Scale a Ledger* | Free |
| Idempotency and exactly-once | Stripe *Idempotent requests*, Brandur Leach *Implementing Stripe-like Idempotency Keys in Postgres*, *Designing Data-Intensive Applications* 2nd ed. | Free / free / paid book |
| Money types and rounding | Microsoft Learn `System.Decimal` and `Math.Round`, Fowler's *Money* pattern | Free |
| Reconciliation | Modern Treasury *Recon Diaries* and *Reconciliation is a Knapsack Problem* | Free |
| SA payments | PASA Academy *Introduction to Payments* (now PayInc), the SARB PSMB-transition page, the PayInc *Business Report 2025*, the SARB ISO 20022 FAQ | Paid course, free documents |
| International vocabulary | CPMI glossary and PFMI (BIS), ISO 20022 message sets, Glenbrook's payments books | Free, free, paid |
| Open banking and FAPI | UK Open Banking Standard site, OpenID FAPI 2.0 Security Profile (final), Investec developer portal | Free |
| Regulation, engineer depth | PCI SSC scoping supplement, FIC Revised Guidance Note 7A (chapter 3, record keeping), the Information Regulator's security-compromise fact sheet, Joint Standard 1 of 2023, Joint Standard 2 of 2024, Joint Communication 2 of 2025 | Free |

**The one paid thing worth considering is PASA Academy's *Introduction to Payments*.** It is the
only structured, South Africa-specific payments course found. It is online-only and self-paced,
and individuals can enrol ([PASA](https://pasa.org.za/industry-learning/pasa-academy/introduction-to-payments/)).
PASA's own site says "PASA Academy and PIPC have moved to PayInc" ([pasa.org.za](https://pasa.org.za/)).

**Happening / Consolidating / Noisy**, applied to the sources:

| | Label | Why |
|---|---|---|
| First-party ledger and idempotency engineering writing (Modern Treasury, TigerBeetle, Stripe, Square) | **Consolidating** | They agree: double-entry, append-only, corrections are new entries, client-generated idempotency keys |
| SA payment-system knowledge | **Happening**, and moving | PASA handed its functions to the SARB and PayInc in August and September 2026. RTC is scheduled to sunset in March 2027. Anything learned from a 2024 source needs a date check |
| Coursera and edX "fintech" | **Noisy** for this purpose | Beginner-level, crypto- and strategy-heavy, US or Asian regulation, graded by quiz and pitch |

---

## Method

Read 2026-09-29.

- **Course platforms.** For Coursera I used its own search page for "fintech" and then opened
  each course or specialization page. From each page I recorded the institution, instructor,
  level, modules, assessment and access wording. The same was done for edX, GetSmarter, Wits and
  PASA Academy. Coursera pages were read through a fetch tool that renders the page; two Wharton
  URLs returned 404.
- **Engineering practice.** I read first-party engineering posts and docs from Stripe, Modern
  Treasury, TigerBeetle, Square, Formance (its GitHub README), Increase and Moov, plus the
  authors' own pages for Brandur Leach, Martin Kleppmann and Martin Fowler.
- **SA payments.** SARB pages and PDFs, the PayInc *Business Report 2025* (downloaded and
  text-extracted; page numbers are PDF pages), and PASA's site.
- **Regulation.** PCI SSC PDFs, the FIC's Revised Guidance Note 7A, the Information Regulator's
  fact sheet, and the Prudential Authority's Joint Communications. All were downloaded and
  text-extracted.
- **Books.** Only the publisher or author page. A book with no publisher page I could read is
  listed as unverified or dropped.

**Bias.** Coursera's catalogue is large and search-ranked. "Every programme is Beginner" is a
claim about the first-page results for "fintech" plus the payments, open-banking and ISO 20022
searches. It is not a census. A later search could surface an intermediate course I missed.

---

## 1. Topic to best source

"Hands-on?" means whether the source itself has you do the thing, not whether you could.

| Topic | Best source (primary) | Hands-on? | Where it shows up in the ledger |
|---|---|---|---|
| **Double-entry basics**: debit-normal and credit-normal accounts, journal entries, balancing | Modern Treasury, *Accounting for Developers, Part I* (Lucas Rocha, 17 Aug 2022, updated 13 Aug 2025): "Every transaction should record both where the money came from and what the money was used for." Parts II and III model a Venmo-style app and a lending marketplace ([MT](https://www.moderntreasury.com/journal/accounting-for-developers-part-i)). Kleppmann, *Accounting for Computer Scientists* (7 Mar 2011): "basic accounting is just graph theory" ([kleppmann.com](https://martin.kleppmann.com/2011/03/07/accounting-for-computer-scientists.html)) | No. Worked examples to copy | Chart of accounts, and the "every journal entry nets to zero" invariant |
| **Accounting drill**: T-accounts, adjusting entries, closing entries | Wharton, *Introduction to Financial Accounting* (Brian Bushee). Module 1 has "Debit-credit bookkeeping fundamentals", "Journal entry practice" and "T-account applications"; module 2 covers adjusting and closing entries. Free to audit ([Coursera](https://www.coursera.org/learn/wharton-accounting)) | **Yes**: 10 assignments, a case and a final exam | Test fixtures: hand-worked journal entries become property-test examples |
| **Ledger design**: immutability, append-only, derived balances | Square, *Books, an immutable double-entry accounting database service* (Łukasz Strzałkowski, 16 Oct 2019): "all transactions (which we call 'journal entries') must balance to 0" and data is "effectively append-only and immutable once stored" ([Square](https://developer.squareup.com/blog/books-an-immutable-double-entry-accounting-database-service/)). Modern Treasury, *How to Scale a Ledger*, six parts (Matt McNierney, from 10 Nov 2022) ([MT](https://www.moderntreasury.com/journal/how-to-scale-a-ledger-part-i)) | No | Accounts, journal entries and append-only postings in SQL Server; the "balances derived, never the source of truth" rule |
| **Corrections and reversals** | TigerBeetle, *Correcting Transfers*: "Transfers in TigerBeetle are immutable, so once they are created they cannot be modified or deleted." Corrections are "more transfers to reverse or adjust" ([TigerBeetle](https://docs.tigerbeetle.com/coding/recipes/correcting-transfers/)) | Recipe-level | The `reversed` and `refunded` states; manual adjustments under dual approval |
| **Holds, pending vs posted** | TigerBeetle, *Two-Phase Transfers* (listed in its docs, [TigerBeetle](https://docs.tigerbeetle.com/)). Increase: "Pending Transactions … impact your available balance, but not your current balance" ([Increase](https://increase.com/documentation/api/pending-transactions)) | Recipe-level | The `authorised` → `captured` states, and available vs current balance |
| **A reference implementation to read** | Formance Ledger, MIT licence: "a programmable financial core ledger", "atomic multi-postings transactions", on PostgreSQL ([GitHub](https://github.com/formancehq/ledger)) | **Yes**: runnable | Compare its schema with yours. It is Go, not C# |
| **Idempotency keys** | Stripe, *Idempotent requests*: it saves "the resulting status code and body of the first request … regardless of whether it succeeds or fails". Keys are "up to 255 characters", may be pruned "after they're at least 24 hours old", and a parameter mismatch errors ([Stripe docs](https://docs.stripe.com/api/idempotent_requests)) | No | `Idempotency-Key` on every write, and what a retry returns |
| **Idempotency in a relational DB** | Brandur Leach, *Implementing Stripe-like Idempotency Keys in Postgres* (27 Oct 2017): atomic phases, recovery points, "foreign state mutations", and "API backends should aim to be passively safe" ([brandur.org](https://brandur.org/idempotency-keys)). Background: Stripe blog, *Designing robust and predictable APIs with idempotency* (22 Feb 2017) ([Stripe](https://stripe.com/blog/idempotency)) | Code in the article | Translate to SQL Server; the outbox is his "staged jobs" |
| **The exactly-once illusion** | TigerBeetle, *Reliable Transaction Submission*: the client generates the `id` and persists it first, and a retry returns `exists`, so a transfer is recorded "once and only once" ([TigerBeetle](https://docs.tigerbeetle.com/coding/reliable-transaction-submission/)). *Designing Data-Intensive Applications*, 2nd ed., Kleppmann and Riccomini, O'Reilly (search listing only; the O'Reilly page returned 403) | No | The fault-injection test: "retry with the same key produces exactly one posting" |
| **Money types and rounding** | Microsoft Learn: `Decimal` "is appropriate for financial calculations that require large numbers of significant integral and fractional digits and no round-off errors", and "does not eliminate the need for rounding" ([System.Decimal](https://learn.microsoft.com/en-us/dotnet/api/system.decimal)). `Math.Round`: "rounding to nearest even is the standard in financial and statistical operations" and is the default ([Math.Round](https://learn.microsoft.com/en-us/dotnet/api/system.math.round)). Fowler, *Money* pattern: "it's easy to lose pennies … because of rounding errors" ([martinfowler.com](https://martinfowler.com/eaaCatalog/money.html)) | No | A `Money` value type (amount plus currency), stated rounding, allocation that never loses a cent |
| **Reconciliation as engineering** | Modern Treasury, *Recon Diaries, Entry II* (22 Dec 2022): "Bank transaction reports do not contain sufficient data to properly reconcile all transactions", from batching, timing and data limits ([MT](https://www.moderntreasury.com/journal/recon-diaries-entry-ii-banks-are-the-enigma)). *Reconciliation is a Knapsack Problem* (Sean Bolton, 24 Oct 2023): 10 payments and 3 batches give 302,400 possible solutions ([MT](https://www.moderntreasury.com/journal/reconciliation-is-a-knapsack-problem)) | No | `parity`'s break taxonomy: timing breaks (T+n), many-to-one batch matches, and why "totals equal" is the fallback |
| **ISO 20022 statements and messages** | Coursera short course *Implement ISO 20022 NEFT/RTGS Mapping*: validation against pacs/camt schemas, "MT940-to-camt.053 conversion", reconciliation-report analysis, in VS Code. Intermediate, 3 hours, India-focused ([Coursera](https://www.coursera.org/learn/implement-iso-20022-neftrtgs-mapping)). ISO's own site returned 403 | **Yes**, small | **Unverified inference:** make the simulated bank statement `camt.053`-shaped, so `parity` reads a real standard |
| **Clearing vs settlement, and FMI vocabulary** | BIS CPMI glossary ([BIS](https://www.bis.org/committees/cpmi/glossary)) and the *Principles for financial market infrastructures* (16 Apr 2012) ([BIS](https://www.bis.org/cpmi/publ/d101.htm)). The definition text could not be extracted | No | README and ubiquitous language: clearing, settlement, netting, finality |
| **Card schemes, vocabulary level** | PCI SSC *Awareness* training: "Understand the transaction steps involved in card processing". Its listed audience includes "Senior Developer, Software Engineer". Paid eLearning ([PCI SSC PDF](https://listings.pcisecuritystandards.org/pdfs/PCI_Awareness_Training_Course_Description.pdf)). US-centric book: Glenbrook, *Payments Systems in the U.S.*, 3rd ed. ([Glenbrook](https://glenbrook.com/product/payments-systems-in-the-us-a-guide-for-the-payments-professionals/)) | Quizzes | Only the non-claim: no PANs, no card rails |
| **Open banking APIs** | UK Open Banking Standard: Read/Write API (v4.0.1 referenced), Dynamic Client Registration, security profiles, Customer Experience Guidelines, all public ([standards.openbanking.org.uk](https://standards.openbanking.org.uk/)) | Specs to implement against | Resource shapes for the open-banking-style API (accounts, transactions, payment consents) |
| **Financial-grade API security** | OpenID Foundation, *FAPI 2.0 Security Profile*, Final, 22 Feb 2025. It requires `response_type=code`, PAR (RFC 9126), PKCE with `S256`, sender-constrained tokens (mTLS RFC 8705 or DPoP RFC 9449), and client auth by mTLS or `private_key_jwt` ([openid.net](https://openid.net/specs/fapi-security-profile-2_0-final.html)) | Spec; conformance suite not checked | The OIDC setup: PAR, PKCE, DPoP, `private_key_jwt`. See the note below the table on UK OB using FAPI 1 |
| **PCI DSS scope** | PCI SSC, *Guidance for PCI DSS Scoping and Network Segmentation* (Dec 2016, v1.1 May 2017): "To be considered out of scope, a system component must not have access to any system in the CDE" ([PCI SSC PDF](https://listings.pcisecuritystandards.org/documents/Guidance-PCI-DSS-Scoping-and-Segmentation_v1.pdf)). Current standard is v4.0.1 ([PCI SSC blog](https://blog.pcisecuritystandards.org/just-published-pci-dss-v4-0-1)) | No | The README non-claim "no cardholder data, no PCI DSS scope", said precisely |
| **FICA, AML and KYC record keeping** | FIC, *Revised Guidance Note 7A* (1 Sep 2025). Chapter 3 is record keeping: CDD records, transaction records, manner and period. Records must "enable the reconstruction" of transactions ([FIC PDF](https://www.fic.gov.za/wp-content/uploads/2025/09/Revised-Guidance-Note-7A-%E2%80%93-Implementation-of-various-aspects-of-the-FIC-Act.pdf)) | No | Why the ledger is append-only and replayable, and a retention note in the README |
| **POPIA breach handling** | Information Regulator, *Fact Sheet on handling of Security Compromises*: "POPIA does not have a threshold for reporting", and reports go through the eServices Portal ([IR PDF](https://inforegulator.org.za/wp-content/uploads/2025/08/Fact-Sheet-on-security-compromises-2.pdf)) | No | Synthetic data only; PII kept out of idempotency keys (Stripe says the same) and out of logs |
| **IT, cyber and cloud rules for SA financial institutions** | Joint Standard 1 of 2023 (IT governance and risk management), commenced 15 Nov 2024 ([Joint Communication 4 of 2023](https://www.resbank.co.za/content/dam/sarb/publications/prudential-authority/pa-public-awareness/covid-19-response/2023/joint-communication-4-of-2023/Joint%20Communication%204%20of%202023-%20Publication%20of%20the%20Joint%20Standard%20-%20IT%20Gov%20and%20Risk.pdf)). Joint Standard 2 of 2024 (cyber), as recorded in `2026-09-28-sa-fintech-target-roles.md`. Joint Communication 2 of 2025 on cloud and data offshoring ([PDF](https://www.resbank.co.za/content/dam/sarb/publications/prudential-authority/pa-public-awareness/covid-19-response/2025/Joint%20Communication%202%20of%202025%20-%20Cloud%20computing%20and%20offshoring%20of%20data.pdf)) | No | Interview talk: where the data lives, and who approves a cloud move |

**A correction worth making now: UK Open Banking does not use FAPI 2.0.** The UK standard's
security-profile page says that with v4 "it was determined by a vote at the Technical Design
Authority to implement the final release of the **FAPI 1 Advanced specification**", and that v3
used "FAPI 1 Implementers Draft 2"
([UK OB security profiles](https://standards.openbanking.org.uk/security-profiles/)). FAPI 2.0 is
final, but it is not what the UK ecosystem runs. So Investec's "financial-grade APIs" for UK Open
Banking probably means FAPI 1 Advanced (**Unverified**: Investec's UK open-banking page returned
403). For the ledger, **Unverified recommendation:** implement FAPI 2.0 (PAR, PKCE, DPoP,
`private_key_jwt`) and write one README paragraph on how it differs from FAPI 1 Advanced. That
difference is what an Investec interviewer would test.

**On Joint Communication 2 of 2025**, dated 28 July 2025, the Authorities say that "the only
regulatory framework-related instruments/documents focused on cloud computing" so far are the
PA's **Directive 3 of 2018** and **Guidance Note 5 of 2018** for banks. They also say that "the
draft regulatory instrument will be published for public consultation in due course." The
communication defines offshoring as "the storage and/or processing of data outside the borders of
South Africa." Separately, the SARB's National Payment System Department (NPSD) published a
consultation paper, *Cloud computing and data offshoring in the national payment system*, in March
2025 ([SARB PDF](https://www.resbank.co.za/content/dam/sarb/what-we-do/payments-and-settlements/regulation-oversight-and-supervision/document-for-comments/doc-for-comments-2025/Cloud%20computing%20and%20offshoring%20of%20data%20consultation%20paper_March%202025.pdf)).

---

## 2. South African payments, specifically

This section extends `2026-09-23-fraud-and-bank-apis.md` Q2, which covers open banking and the
end of PASA. It adds the rails, the operator, and where to learn them.

### Who does what, as of September 2026

- **The SARB owns the NPS and settles it.** The SARB defines the NPS as "a set of instruments,
  procedures and rules that enable funds to be transferred from one financial institution to
  another". It operates SAMOS, the RTGS in which interbank settlement is final
  ([SARB payments and settlements](https://www.resbank.co.za/en/home/what-we-do/payments-and-settlements)).
- **PASA has handed over its functions.** Per the SARB's PSMB-transition page: "Effective 11 August
  2026, the responsibility for some payment clearing houses (PCHs) and rule-related functions
  … transferred to the SARB, while functions transitioning to PayInc did so on 2 September 2026."
  - **The SARB took:** "Rules and standards for the national payment system", licensing, and the
    PCHs for "card, immediate settlement, cash settlement, equities, bonds, derivatives and money
    market".
  - **PayInc took:** "EFT credit, EFT debit, Authenticated Collections, PayShap (Rapid Payments),
    Registered Mandate and real-time clearing (RTC)".

  ([SARB PSMB](https://www.resbank.co.za/en/home/what-we-do/payments-and-settlements/psmb))
- **BankservAfrica is now PayInc, and half of it belongs to the SARB.** "This year, BankservAfrica
  was rebranded to PayInc". "In November 2025, the South African Reserve Bank (SARB) acquired a
  50% stake in PayInc … that transitioned PayInc into the national payments utility"
  ([PayInc Business Report 2025](https://businessreports.payinc.co.za/pdf/PayInc_Business_Report_2025.pdf), pp. 4–5).

### The rails, in PayInc's own FY2025 words

From the PayInc Business Report 2025, p. 20:

| Rail | What PayInc says | Engineering meaning |
|---|---|---|
| **EFT** (credit and debit) | "bulk payment and collections … 29 active banks". EFT credit was "over 1 billion transactions" in FY2025. "With the EFT service being on legacy rails, growth … is slowing" | Batch files, deferred settlement, T+n timing breaks. This is the realistic shape for the simulated statement |
| **PayShap** | "built on the Rapid Payment Rails using ISO 20022 standards", 329 million transactions, 12 banks. The limit was raised "from R3 000 to R50 000 in October 2024". PayShap Request went live in December 2024 (p. 24) | Real-time, proxy-addressed, ISO 20022. Settlement arrives quickly but is still a separate step from clearing |
| **RTC** | "Some volume has migrated from RTC to PayShap … **RTC is scheduled to sunset in March 2027**" | Do not model RTC as a future rail |
| **DebiCheck** (Authenticated Collections) | Registered Mandate Services "separated from DebiCheck and launched as a standalone payment system" in May 2025 | Mandate-based pulls. Out of scope for a merchant ledger, but the vocabulary matters |
| **Card** | "facing significant challenges due to the increasing presence of international payment solution providers" | Card switching is a closed specialism. Keep it a non-claim |
| **TCIB** (SADC cross-border) | "This multi-currency enabled ISO 20022 platform" | Cross-border context only |

**ISO 20022 in SA.** The SARB's FAQ of 3 November 2022 has three findings
([SARB ISO 20022 FAQ](https://www.resbank.co.za/content/dam/sarb/publications/media-releases/2022/iso-20022/ISO%2020022%20FAQ.pdf)):

- SAMOS moved to ISO 20022 "on the weekend of 17–19 September 2022", with a translation service.
- "The EFT debit system has already embedded the ISO 20022 format with the introduction of the
  DebiCheck service".
- The format is "critical to reforming … the EFT debit system, the EFT credit system as well as
  SAMOS".

**Strategy documents.** *Vision 2025* (2018) set nine goals
([PDF](https://www.resbank.co.za/content/dam/sarb/what-we-do/payments-and-settlements/Vision%202025.pdf)).
Its successor is out for comment as the *National Payment System Vision 2030+ Consultation Paper*
of February 2026. Responses were due "by no later than 31 March 2026". Its trends include "The rise
of wallets", "Shifting fraud risks", "Unbundled banking" and "Federated networks"
([PDF](https://www.resbank.co.za/content/dam/sarb/what-we-do/payments-and-settlements/consultation-documents/2026/vision-2030--/NPS%202030+%20Consultation%20Paper%20-%2024%20February%202026.pdf)).
The SARB Annual Report 2024/25 payments chapter adds that the PEM plan includes "designing new
RTGS systems, expanding the fast payment system (FPS) and creating a comprehensive fraud
management framework", and that the NPS Bill has "promulgation expected in 2026"
([PDF](https://www.resbank.co.za/content/dam/sarb/publications/reports/annual-reports/2025/chapters/the-sarb's-performance/payments-24-25.pdf)).

### Where to learn it

| Source | What it is | Access | Verdict |
|---|---|---|---|
| **PASA Academy, *Introduction to Payments*** | Seven modules: "Money and the National Payment System", "National Payment System (NPS) Basics", "Payment System Concepts", "Clearing and Settlement", "NPS Stakeholders", "Payment Systems in South Africa", "Innovation and Modernisation". Online-only, self-paced, quizzes; individuals can enrol ([PASA](https://pasa.org.za/industry-learning/pasa-academy/introduction-to-payments/)) | Paid | **The best structured SA source.** It is entry-level by its own description |
| PASA Academy, *Certificate in Foundational Payments* | Designed for 12 weeks. LMS, "scheduled Connect sessions", summative assessments, 70% pass mark. It leads to the Advanced Certificates in Electronic Payments or High Value Payments ([PASA](https://pasa.org.za/industry-learning/pasa-academy/pasa-certificate-in-foundational-payments/)) | Paid | Deeper and slower. Worth it only if the user wants a credential SA payments teams recognise (**Unverified** that they do) |
| PASA Academy, *Advanced Certificate in Electronic Payments* | Listed on the Academy page ([PASA Academy](https://pasa.org.za/industry-learning/pasa-academy/)); its own page returned 404 | Paid | Unverified |
| SARB PSMB page, PayInc Business Report, ISO 20022 FAQ, Vision 2030+ paper | Primary documents, cited above | Free | **Read these regardless.** They are current. Most 2024 teaching material predates PASA's handover and the RTC sunset |
| UCT on Coursera, *Financial Regulation in Emerging Markets and the Rise of Fintech Companies* | Has a "Fintech Regulation in South Africa" item and a "Payment Services - Yoco" case ([Coursera](https://www.coursera.org/learn/financial-regulation)) | Free to enrol | Local context, not rails |
| IOBSA, CISI | IOBSA is a professional body with designations and CPD ([iob.co.za](https://www.iob.co.za/)). No CISI payments qualification was found | — | Not an engineering source |

**The Academy's future is unclear.** PASA's site says "PASA Academy and PIPC have moved to PayInc",
and that its information "will remain available on the PASA website until further notice"
([pasa.org.za](https://pasa.org.za/)). PayInc's own site returned an Angular shell with no content
to fetch. **Unverified:** whether the 2027 intake runs under the PASA name or PayInc's.

---

## 3. Coursera, course by course

Level and access are as each course page states them. "Engineer-relevant" is my judgement against
the ledger's needs.

| Course or specialization | Institution | Level | Hands-on | Payments or ledger depth | Engineer-relevant? |
|---|---|---|---|---|---|
| *Introduction to Financial Accounting* ([page](https://www.coursera.org/learn/wharton-accounting)) | Wharton (Penn) | Beginner | 10 assignments and a final exam. Journal entries, T-accounts | Double-entry mechanics, done properly | **Yes, narrowly.** Free to audit. The only Coursera course that teaches something the ledger needs |
| *Implement ISO 20022 NEFT/RTGS Mapping* ([page](https://www.coursera.org/learn/implement-iso-20022-neftrtgs-mapping)) | Coursera, "Professionals in the Industry" | Intermediate, 3 h | **Yes.** XML schema validation, MT940 → `camt.053`, reconciliation reports; AI-graded | Real message types, Indian rails | **Partly.** Useful for `camt.053`; the audience is business analysts and the author is not named |
| Wharton FinTech specialization / *Foundations, Payments, and Regulations* | Wharton | — | — | — | **404, not available** |
| *Financial Technology (Fintech) Innovations* ([page](https://www.coursera.org/specializations/financialtechnology)) | Michigan | Beginner | "storytelling approach"; value propositions and portfolios | Payments course: cheques, ACH, wallets, cards, M-Pesa and UPI ([page](https://www.coursera.org/learn/paytech)) | No. A business survey |
| *FinTech: Finance Industry Transformation and Regulation* ([page](https://www.coursera.org/specializations/fintech)) | HKUST | Beginner | Peer-graded projects with "recommendations to executives" | KYC/AML, BCP/DR, UK OB API module | No. Policy vocabulary only |
| *FinTech Law and Policy* ([page](https://www.coursera.org/learn/fintechlawandpolicy)) | Duke | Beginner | 15 quizzes, final exam | US bank regulation, account aggregation | No. US law |
| *Designing the Future of Finance* ([page](https://www.coursera.org/learn/designing-the-future-of-finance)) | Oxford Saïd | Beginner | 5 assignments, a strategy capstone | Open banking to open finance; an API-layer module | Weak. Explains why AIS and PIS exist, not how to secure them |
| *Fintech Startups in Emerging Markets* ([page](https://www.coursera.org/specializations/fintech-startups-emerging-markets)) | UCT | Beginner | Business model canvas and pitch | Some SA regulation, Yoco case | No, beyond local context |
| *Banking Payments and Financial Services* ([page](https://www.coursera.org/learn/banking-payments-financial-services)) | EDUCBA | Foundational | 15 assignments | RBI (India) | No |
| DeFi, blockchain, AI-in-finance programmes (Duke, INSEAD, Oxford, CBS) | various | Beginner | — | Crypto and strategy | No |

**Plain answer: audit the Wharton accounting course if a quiz-driven drill helps. Optionally do
the ISO 20022 short course. Skip the rest.** A certificate from any of them tells a bank reviewer
nothing the ledger repository does not show better. **Unverified**, but consistent with
`2026-09-28-sa-fintech-target-roles.md`: no posting of 45, and none of Investec's three, names a
fintech certificate.

**edX** had the same shape as far as could be seen. There are fintech professional certificates
from Toronto ("Future of Payments"), UT Austin, HKU and ACCA
([edX fintech](https://www.edx.org/learn/fintech)). But their pages returned only navigation
chrome, so level, syllabus and hands-on content could not be verified. They are listed as
unreachable below.

---

## 4. What to read first

In order, with no dates. Each step feeds the next ledger slice.

1. **Modern Treasury, *Accounting for Developers* I–III**, then **Kleppmann's graph essay**.
   Optionally, Wharton's accounting course, audited, modules 1–2 only.
2. **Square *Books*** and **TigerBeetle's Debit-Credit, Two-Phase Transfers and Correcting
   Transfers pages**. Then write the ledger's invariants down before the schema.
3. **Stripe *Idempotent requests***, **Brandur's Postgres article** and **TigerBeetle *Reliable
   Transaction Submission***. Then the payments API and outbox.
4. **Microsoft Learn `Decimal` and `Math.Round`**, and **Fowler's *Money***. Then the `Money` type.
5. **SARB PSMB page**, **PayInc Business Report 2025 p. 20**, **SARB ISO 20022 FAQ**. Optionally,
   PASA Academy *Introduction to Payments*. Then decide what the simulated statement looks like:
   EFT-batch timing, and **Unverified** whether it should be `camt.053`-shaped.
6. **Modern Treasury *Recon Diaries* II and *Knapsack***. Then `parity`'s reconciliation mode and
   its break taxonomy.
7. **UK Open Banking Standard** (Read/Write API, security profiles), then the **FAPI 2.0 Security
   Profile**. Then the OIDC-protected open-banking-style API.
8. **PCI scoping supplement**, **FIC Guidance Note 7A chapter 3**, **Information Regulator
   fact sheet**, **Joint Standard 1 of 2023** and **Joint Communication 2 of 2025**. Then the
   README non-claims and a short "regulatory posture" section.
9. **Modern Treasury *How to Scale a Ledger*** and **DDIA 2nd edition**, as depth once the ledger
   works.

---

## 5. Open questions

1. **Is the PASA Academy credential worth it?** Nothing read here shows that SA payments teams
   ask for it. No posting in the 2026-09-28 sample named it. Only the user, or someone on a
   Johannesburg payments team, can say whether it carries weight.
2. **Who runs the Academy now, and under what name?** PASA says it has moved to PayInc. PayInc's
   site could not be read.
3. **FAPI 1 Advanced or FAPI 2.0?** The UK standard runs FAPI 1 Advanced. The recommendation above
   (build FAPI 2.0, document the difference) is a judgement. Investec's UK developer
   documentation would settle it and could not be reached.
4. **`camt.053` for the simulated statement?** It is attractive, because a real standard makes
   `parity` look like bank work. No SA bank's statement format was checked. Investec's
   programmable-banking statement shape (in `2026-09-23-fraud-and-bank-apis.md`) is JSON, not
   `camt`.
5. **Glenbrook's global book.** Glenbrook Press lists *Global Payments and the Fintech Innovations
   Changing the Industry* ([Glenbrook Press](https://glenbrook.com/books/)), but its product page
   was not read. Its edition, year and contents are unverified.
6. **The final cloud and offshoring instrument.** Joint Communication 2 of 2025 promises a draft
   "in due course". Whether it has since been published was not checked.

---

## Sources

All read 2026-09-29.

**Course platforms**
- Coursera search "fintech": https://www.coursera.org/courses?query=fintech
- Wharton, Introduction to Financial Accounting: https://www.coursera.org/learn/wharton-accounting
- ISO 20022 NEFT/RTGS Mapping: https://www.coursera.org/learn/implement-iso-20022-neftrtgs-mapping
- Michigan, Fintech Innovations: https://www.coursera.org/specializations/financialtechnology ; The Future of Payment Technologies: https://www.coursera.org/learn/paytech
- HKUST, FinTech specialization: https://www.coursera.org/specializations/fintech ; RegTech: https://www.coursera.org/learn/regtech
- Duke, FinTech Law and Policy: https://www.coursera.org/learn/fintechlawandpolicy
- Oxford Saïd, Designing the Future of Finance: https://www.coursera.org/learn/designing-the-future-of-finance
- UCT, Fintech Startups in Emerging Markets: https://www.coursera.org/specializations/fintech-startups-emerging-markets ; Financial Regulation in Emerging Markets: https://www.coursera.org/learn/financial-regulation
- EDUCBA, Banking Payments and Financial Services: https://www.coursera.org/learn/banking-payments-financial-services
- UCT GetSmarter, Fintech: Disruption in Finance: https://www.getsmarter.com/products/uct-fintech-disruption-in-finance-online-short-course
- Wits MCom Financial Technology: https://www.wits.ac.za/course-finder/postgraduate/clm/mcom-financial-technology/
- PASA: https://pasa.org.za/ ; Academy: https://pasa.org.za/industry-learning/pasa-academy/ ; Introduction to Payments: https://pasa.org.za/industry-learning/pasa-academy/introduction-to-payments/ ; Certificate in Foundational Payments: https://pasa.org.za/industry-learning/pasa-academy/pasa-certificate-in-foundational-payments/
- IOBSA: https://www.iob.co.za/

**Engineering practice**
- Stripe, Idempotent requests: https://docs.stripe.com/api/idempotent_requests
- Stripe blog, Designing robust and predictable APIs with idempotency: https://stripe.com/blog/idempotency
- Brandur Leach, Implementing Stripe-like Idempotency Keys in Postgres: https://brandur.org/idempotency-keys
- Modern Treasury, Accounting for Developers Part I: https://www.moderntreasury.com/journal/accounting-for-developers-part-i
- Modern Treasury, How to Scale a Ledger Part I: https://www.moderntreasury.com/journal/how-to-scale-a-ledger-part-i
- Modern Treasury, Reconciliation is a Knapsack Problem: https://www.moderntreasury.com/journal/reconciliation-is-a-knapsack-problem
- Modern Treasury, Recon Diaries Entry II: https://www.moderntreasury.com/journal/recon-diaries-entry-ii-banks-are-the-enigma
- TigerBeetle docs: https://docs.tigerbeetle.com/ ; Correcting Transfers: https://docs.tigerbeetle.com/coding/recipes/correcting-transfers/ ; Reliable Transaction Submission: https://docs.tigerbeetle.com/coding/reliable-transaction-submission/
- Square, Books: https://developer.squareup.com/blog/books-an-immutable-double-entry-accounting-database-service/
- Formance Ledger: https://github.com/formancehq/ledger
- Increase, Pending Transactions: https://increase.com/documentation/api/pending-transactions
- Moov ACH: https://github.com/moov-io/ach (US NACHA files; noted, not recommended for SA)
- Martin Kleppmann, Accounting for Computer Scientists: https://martin.kleppmann.com/2011/03/07/accounting-for-computer-scientists.html
- Martin Fowler, Money: https://martinfowler.com/eaaCatalog/money.html
- Microsoft Learn, System.Decimal: https://learn.microsoft.com/en-us/dotnet/api/system.decimal ; Math.Round: https://learn.microsoft.com/en-us/dotnet/api/system.math.round

**SA payments and regulators**
- SARB payments and settlements: https://www.resbank.co.za/en/home/what-we-do/payments-and-settlements
- SARB PSMB transition: https://www.resbank.co.za/en/home/what-we-do/payments-and-settlements/psmb
- SARB ISO 20022 FAQ (3 Nov 2022): https://www.resbank.co.za/content/dam/sarb/publications/media-releases/2022/iso-20022/ISO%2020022%20FAQ.pdf
- SARB Vision 2025: https://www.resbank.co.za/content/dam/sarb/what-we-do/payments-and-settlements/Vision%202025.pdf
- SARB NPS Vision 2030+ consultation paper (Feb 2026): https://www.resbank.co.za/content/dam/sarb/what-we-do/payments-and-settlements/consultation-documents/2026/vision-2030--/NPS%202030+%20Consultation%20Paper%20-%2024%20February%202026.pdf
- SARB Annual Report 2024/25, payments chapter: https://www.resbank.co.za/content/dam/sarb/publications/reports/annual-reports/2025/chapters/the-sarb's-performance/payments-24-25.pdf
- SARB NPSD, Cloud computing and data offshoring in the NPS (Mar 2025): https://www.resbank.co.za/content/dam/sarb/what-we-do/payments-and-settlements/regulation-oversight-and-supervision/document-for-comments/doc-for-comments-2025/Cloud%20computing%20and%20offshoring%20of%20data%20consultation%20paper_March%202025.pdf
- PayInc Business Report 2025 (fetched with curl; WebFetch was refused): https://businessreports.payinc.co.za/pdf/PayInc_Business_Report_2025.pdf
- Joint Communication 4 of 2023 (Joint Standard 1 of 2023): https://www.resbank.co.za/content/dam/sarb/publications/prudential-authority/pa-public-awareness/covid-19-response/2023/joint-communication-4-of-2023/Joint%20Communication%204%20of%202023-%20Publication%20of%20the%20Joint%20Standard%20-%20IT%20Gov%20and%20Risk.pdf
- Joint Communication 2 of 2025, cloud and offshoring: https://www.resbank.co.za/content/dam/sarb/publications/prudential-authority/pa-public-awareness/covid-19-response/2025/Joint%20Communication%202%20of%202025%20-%20Cloud%20computing%20and%20offshoring%20of%20data.pdf
- FIC Revised Guidance Note 7A (1 Sep 2025): https://www.fic.gov.za/wp-content/uploads/2025/09/Revised-Guidance-Note-7A-%E2%80%93-Implementation-of-various-aspects-of-the-FIC-Act.pdf
- Information Regulator, security compromises fact sheet: https://inforegulator.org.za/wp-content/uploads/2025/08/Fact-Sheet-on-security-compromises-2.pdf
- BIS CPMI glossary: https://www.bis.org/committees/cpmi/glossary ; PFMI: https://www.bis.org/cpmi/publ/d101.htm

**Standards and cards**
- UK Open Banking Standard: https://standards.openbanking.org.uk/ ; security profiles: https://standards.openbanking.org.uk/security-profiles/
- OpenID FAPI 2.0 Security Profile (Final): https://openid.net/specs/fapi-security-profile-2_0-final.html
- Investec Developer portal: https://developer.investec.com/
- PCI SSC, v4.0.1: https://blog.pcisecuritystandards.org/just-published-pci-dss-v4-0-1
- PCI SSC, Scoping and Segmentation supplement: https://listings.pcisecuritystandards.org/documents/Guidance-PCI-DSS-Scoping-and-Segmentation_v1.pdf
- PCI SSC, Awareness training description: https://listings.pcisecuritystandards.org/pdfs/PCI_Awareness_Training_Course_Description.pdf

**Books (publisher or author pages)**
- Glenbrook, Payments Systems in the U.S., 3rd ed.: https://glenbrook.com/product/payments-systems-in-the-us-a-guide-for-the-payments-professionals/ ; Glenbrook Press list: https://glenbrook.com/books/
- *Designing Data-Intensive Applications*, 2nd ed. (O'Reilly): https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/ (403; title and authors from the search listing only)
- *The Anatomy of the Swipe* (Ahmed Siddiqui): no publisher page found, so not recommended here

**Unreachable or empty**
- Coursera Wharton FinTech specialization and payments course: 404
- UCT Coursera specialization at `/fintech-startups-in-emerging-markets` (404); read at `/fintech-startups-emerging-markets` instead
- edX Toronto *FinTech: Future of Payments* and UT Austin *Fintech: The Future of Finance*: navigation only, no syllabus
- PASA *Advanced Certificate in Electronic Payments* page: 404
- PayInc homepage (payinc.co.za): 403 to WebFetch; curl returned an Angular shell with no content
- iso20022.org: 403. Swift ISO 20022 learning and Swift Smart pages: 403. **Unverified**, from search snippets only: Swift Smart is for "Swift users with a swift.com account linked to their institution's BIC", so not open to individuals
- BIS glossary definitions and the PFMI PDF: bot-protected; landing pages only
- Investec UK open-banking page (investec.com/en_gb): 403
- Increase `/documentation/transactions`: 404. Formance docs: empty render; GitHub README used instead
