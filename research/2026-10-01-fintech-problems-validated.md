# What the three repos actually solve, checked against South African evidence

Research for one question: **"What are these actually solving? Are they real-world problems?"** It covers `ledger`, `rails` and `recon`. All pages were read on **2026-10-01**, on the page that owns the fact wherever possible. If a page could not be fetched, the text says so. **Inference** marks my own reasoning. **Unverified** marks a claim I could not confirm from a primary source. There are no salaries and no timelines.

This file builds on `2026-09-28-sa-fintech-target-roles.md`, `2026-09-23-fraud-and-bank-apis.md` and `2026-09-29-fintech-knowledge-sources.md` and does not repeat them. Those files already cover SABRIC card and digital-crime totals, the Investec sandbox, POPIA for personal projects, PASA's handover to the SARB and PayInc, PayInc's FY2025 rail figures, and the fact that "ledger" appears in zero SA engineering postings while "reconciliation" appears in several. No `2026-10-01-*` file existed before this one.

---

## The verdict

**Of the three, only `recon` solves a problem a South African user would pay to have solved. Even `recon` is commoditised at both ends. Each PSP already reconciles its own payouts into Xero, and enterprise multi-provider reconciliation is already sold locally by Stitch, Transaction Junction, Ecentric and Precium. The gap left is small and mid-sized merchants who take money through two or more PSPs plus EFT or PayShap and reconcile into Xero or Sage. No vendor page read today serves that segment across providers.**

**`ledger` solves a real and expensive problem, but as a product it is a commodity. Formance, Blnk and TigerBeetle are open source, Modern Treasury sells it, and Uber runs it internally. It should become recon's internal clearing sub-ledger, not a headline.**

**`rails`, as a PayShap simulator, is a learning exercise. The people who suffer ISO 20022 state problems are about a dozen banks and a few sponsored non-banks. Merchants never see a `pacs.008`, because their PSP absorbs it. `rails` earns its place only as the fault-injecting simulator that generates recon's ground truth.**

**Recommended framing: payout reconciliation for SA merchants who take payments through several PSPs and close their books in Excel or Xero.** It is the only framing in which a real user can try the product with their own data.

Per repo:

| Repo | Real problem? | Who suffers it in SA | Already solved by | Verdict |
|---|---|---|---|---|
| `ledger` | **Yes, and costly.** Synapse's records did not match its partner banks', leaving a $60–90m shortfall ([CFPB](https://www.consumerfinance.gov/enforcement/actions/synapse-financial-technologies-inc/)) | Every fintech, internally. No SA posting advertises it (prior file) | Formance, Blnk, TigerBeetle, Modern Treasury, in-house builds | **Commodity. Keep it as a component** |
| `rails` | **Yes, but narrow.** Peach documents an `uncertain` status that can later turn `Successful` ([Peach](https://developer.peachpayments.com/docs/checkout-webhooks)) | PayShap participants and PSPs. Not merchants: Ozow says PayShap Request needs "no additional development" for existing merchants ([Ozow](https://ozow.com/our-products/instant-payments-with-payshap-request)) | PayInc, Electrum, sponsor banks, the PSPs themselves | **Learning exercise unless it becomes recon's test harness** |
| `recon` | **Yes, and paid for.** Ecentric says mid-market retailers needed "two and three weeks" to see their month-end position ([Bizcommunity, Ecentric release](https://www.bizcommunity.com/article/automation-efficiency-and-accuracy-for-sa-retailers-its-time-for-reconassist-561290a)) | Merchants, their bookkeepers, PSP and remittance finance teams | Per-PSP Xero apps; Stitch, TJ Recon Pro, ReconAssist, Precium for enterprise | **Real. Aim at the multi-PSP SME gap** |

Three findings shaped this:

1. **Each PSP reconciles only itself.** Yoco's Xero app creates bank rules so "your payouts are automatically matched, and any Yoco fees are neatly separated" ([Xero App Store](https://apps.xero.com/za/app/yoco)). Paystack's covers only invoice payments ([Xero App Store](https://apps.xero.com/za/app/paystack)). Stitch Express covers Shopify and WooCommerce sales on Stitch ([Stitch](https://stitch.money/express-accounting)). **Inference:** a merchant on Yoco in-store, Payfast or Paystack online, and EFT or PayShap for invoices gets three partial answers and no single one.
2. **SME bank statements are CSV and OFX, not `camt.053`.** Standard Bank's business online banking exports "CSV, OFX, QFX, QBO, PDF, and XLSX" ([Standard Bank OB4B guide](https://www.standardbank.co.za/static_file/South%20Africa/PDF/How%20To%20Guides/OB4B%20How-to%20guide%20-%20Downloading%20transaction%20history.pdf)). **Inference:** `camt.053` is the corporate host-to-host shape. An SME tool must read CSV and OFX first.
3. **The strongest regulatory hook is client-funds reconciliation.** The SARB's draft Authorisation Framework (May 2026) says a money remitter "must at all times demonstrate that it can reconcile the funds paid into its clients' segregated bank account with a specific client transaction executed" (para 39.8, p. 69). Acquirers must hold payee funds in segregated accounts (17.1.9), and their payee agreements must cover a "reconciliation process" (17.1.1(h)) ([SARB draft, Annexure D](https://www.resbank.co.za/content/dam/sarb/publications/prudential-authority/pa-public-awareness/communication/2026/prudential-communication-10-of-2026/Annexure%20D-%20Draft%20Authorisation%20Framework.pdf)). That is `ledger` plus `recon`, required by draft law. **Unverified:** I could not find whether the final framework had been published by 2026-10-01. Webber Wentzel reported it was expected in Q3 2026 ([Polity](https://www.polity.org.za/article/south-africas-payments-regulatory-framework-third-draft-of-authorisation-framework-published-for-comment-2026-05-22)).

---

## 1. Who in SA suffers each problem, and how badly

### 1a. Reconciliation: PSP payouts net of fees, several PSPs, matching to the bank

**How the PSPs settle.** Every PSP pays a net, batched deposit that matches no single sale.

| PSP | Settlement mechanics, in the PSP's words | Source |
|---|---|---|
| Yoco | "19h00 as the end of the business day"; payout initiated at 05h00 next business day; funds in "1 – 2 business days"; worked example deducts a 3.39% fee (2019 article) | [Yoco blog](https://www.yoco.com/za/blog/when-will-i-get-my-money/) |
| Yoco (Checkout API) | Reconcile by exporting a CSV from Payouts History and matching the "Online Reference" column to the API's Checkout ID. The guide does not cover fees or the bank-statement reference | [Yoco developer guide](https://developer.yoco.com/guides/online-payments/reconciliation/reconciling-checkout-api-payments-with-daily-payouts) |
| Peach | "one consolidated deposit" per business day for the previous day's transactions (T+1), with "A unique deposit reference". Funds may be "temporarily withheld or delayed" for fraud review, excessive chargebacks or volume spikes | [Peach support](https://support.peachpayments.com/support/solutions/articles/47001250592-understanding-your-peach-payments-settlements) |
| Peach | The settlement file shows "which payments Peach settled in which settlement batch". The separate dashboard reconciliation reports "cover card transactions for Absa and Nedbank" | [Settlements](https://developer.peachpayments.com/docs/dashboard-reporting-settlements), [Reconciliation reports](https://developer.peachpayments.com/docs/dashboard-reporting-reconciliation) (search summary) |
| Ozow | Settlement = cleared transactions minus refunds minus transaction and refund fees minus "a settlement cost". A sliding-scale fee forecast is corrected by "a fee adjustment on the next settlement" | **Search summary only.** `oldhub.ozow.com/docs/settlements` did not resolve (DNS failure) |
| Paystack | Payout is "the sum of all the payments made to you minus transaction fees". A payout can be split into several "Batches" ("tranches") | [Paystack support](https://support.paystack.com/hc/en-us/articles/360012149479-When-will-I-receive-my-payouts). The SA "2 working days" schedule appeared only in search snippets (**Unverified**) |

Modern Treasury states the general problem: banks "process payments in aggregate batches", clearing takes "anywhere from one to seven days", and "Bank transaction reports do not contain sufficient data to properly reconcile all transactions" ([Recon Diaries II](https://www.moderntreasury.com/journal/recon-diaries-entry-ii-banks-are-the-enigma)).

**What accounting tools already do.**

- **Xero** now auto-reconciles with its JAX agent by "Rule", "Match", "Memory" and "Prediction" ([Xero ZA](https://www.xero.com/za/accounting-software/reconcile-bank-transactions)). The AI tools were announced for South Africa on 25 June 2026 ([Xero release](https://www.xero.com/media-releases/xero-unveils-new-ai-powered-tools-south-africa/)).
- **Xero's SA bank-feed list** (Absa, Capitec Business, FNB, Investec, Nedbank, Standard Bank) came only from a search summary. `xero.com/za/connect-banks/` returned 404. **Unverified.**
- **Sage** has had direct FNB feeds since 2021 ([Sage press release](https://www.sage.com/en-za/news/press-releases/2021/05/fnb-and-sage-partnership-enables-smes-to-securely-automate-their-business-accounting/), search summary). Standard Bank and Nedbank publish Sage feed guides.
- **Inference:** one-to-one bank-line matching is commoditised. Breaking a net PSP deposit back into sales, fees, refunds and holds is not, except inside each PSP's own integration.

**Per-PSP integrations, and their limits.**

- **Yoco to Xero:** auto-matches payouts but requires the Yoco Pro Plan at R499/month. Its only review (1 star) asks "how do you reconcile the amounts" ([Xero App Store](https://apps.xero.com/za/app/yoco)).
- **Paystack to Xero:** invoice payments only ([Xero App Store](https://apps.xero.com/za/app/paystack)).
- **Ozow to Xero:** says it reconciles "in real time" but does not say whether it reaches settlements ([Ozow](https://www.ozow.com/integrations/xero)).
- **Payfast to Xero:** needs a separate clearing account. A user complaint that net settlement "makes bank reconciliation extremely difficult" came only from a search summary (**Unverified**). The Payfast reviews page returned 404.
- **Global tools:** Reconcile.ly lists South Africa but supports Shopify payouts only ([Xero App Store](https://apps.xero.com/za/app/reconcilely)). A2X covers PayPal, Amazon and others. Search found no Payfast, Yoco or Peach connector for it (**Unverified**).

**How badly it hurts.**

- **Mid-market and enterprise: badly, and they pay.** Ecentric (vendor claim, 26 Feb 2024) cites "two and three weeks" to see month-end, and one team cut "from over 100 staff to just 12" ([Bizcommunity](https://www.bizcommunity.com/article/automation-efficiency-and-accuracy-for-sa-retailers-its-time-for-reconassist-561290a)). Transaction Junction sells "three-way reconciliation" across "client, switch, and provider data" to "single-lane outlets to large corporates" ([TJ Recon Pro guide](https://transactionjunction.co.za/wp-content/uploads/2025/09/The-Retailers-Guide-to-Financial-Precision_TJ-Recon-Pro.pdf)). Mama Money's recon manager role (prior file) asks Tech to "build automated/custom recons".
- **SMEs: real but unmeasured.** I found **no SA survey that measures reconciliation time or how many PSPs SMEs use.**
  - Sage's often-quoted "202 working days per year on admin" comes from a January 2018, 11-country study and does not isolate reconciliation ([Sage ZA](https://www.sage.com/en-za/blog/small-business-admin/)).
  - Visa's October 2024 SA SME study (4Sight) lists the barriers as "perceived costs", card-fraud worry ("65% of card-accepting merchants") and "complex onboarding". Reconciliation is not among them ([Visa VoA SA](https://africa.visa.com/content/dam/VCOM/regional/cemea/genericafrica/run-your-business/value-of-acceptance/voa-designed-generic-report-south-africa.pdf)).
  - Netcash's guide says SA businesses "lose millions annually because of slow invoice payments and reconciliation delays" but gives no data ([Netcash](https://netcash.co.za/blog/invoice-to-cash-in-days-a-practical-guide-to-faster-reconciliation-in-sa/)).

**Is there a gap a small tool could fill?** **Inference: yes, narrowly.** It would be multi-PSP payout decomposition for merchants on two or more providers, reading each PSP's real export and the bank's CSV or OFX, and posting clearing-account journals to Xero or Sage. The risks:

- **Stitch could move down-market**, since it already does multi-provider reconciliation for enterprise.
- **Xero's AI could absorb part of it.**
- **The size of the segment is Unverified.**

### 1b. Failed, duplicate and "pending" payments

- **NFO (Banking division).** 12,461 banking complaints. The top product category is "Current accounts: 3 439" ([NFO](https://nfosa.co.za/nfos-second-year-surge-r442-9-million-restored-to-consumers/)). Mobile and internet banking fraud made up "39% of all cases", and online-banking fraud complaints rose 15% on 2024 ([NFO, 16 Dec 2025](https://nfosa.co.za/nfo-banking-division-returns-r60-million-to-consumers-in-2025/)). **The NFO pages read publish no subcategory for duplicate debits, failed EFTs or PayShap.** That is an absence, not a zero. The full annual-report PDF was not located.
- **System-error duplicates reach the ombud.** In an NFO 2024 case, a payment was reversed by "a system error", the customer paid again, and "the beneficiary received both payments" ([IOL](https://iol.co.za/personal-finance/financial-planning/2025-06-28-words-on-wealth-report-reveals-shocking-admin-failures-by-banks-and-credit-firms/)).
- **Recent SA duplicate incident.** On 4 March 2026 FNB customers were charged up to three times, mostly on Takealot: "A technical processing error affecting a number of our virtual cards has resulted in some duplicated transactions" ([Stuff](https://stuff.co.za/2026/03/06/fnb-customers-duplicate-charges-can-rest-easy/)). Capitec and Nedbank had duplicated card debits in 2020 ([City Press](https://www.news24.com/citypress/business/capitec-and-nedbank-scramble-to-reverse-duplicated-card-payments-20200911), search result). **Root causes were not published, so these cannot be attributed to idempotency bugs (Inference).**
- **Wrong-account EFTs are unrecoverable without the recipient.** The ombud said that if a reversal "can't be successfully processed, the bank cannot become involved" ([EWN, R63k case](https://www.ewn.co.za/2024/10/23/bank-cant-reverse-r63k-i-paid-into-wrong-account-after-recipient-refused-to-return-the-money)).
- **Fraud is social engineering, not message bugs.** SABRIC's 2025 release (summary) says digital banking crime is "driven by social engineering … rather than criminals directly attacking banking systems" ([SABRIC](https://www.sabric.co.za/?p=4450), search summary; the figures are in the prior file).
- **Debit orders.** The dispute window on all low-value debits (EFT debit orders, DebiCheck, Registered Mandates) fell "from 365 days to 60 calendar days", effective 13 April 2026, "to improve fairness and balance" between payers and collectors ([PASA DODE FAQ](https://pasa.org.za/wp-content/uploads/2026/04/PASA_DODE_FAQ_v3.pdf)). The "800,000 disputed a month of 56 million" figure is an old BusinessTech secondary with no date I could confirm (**Unverified**).
- **PayShap reversals.** **No consumer-complaint data on PayShap reversals was found.**

**What this means for `rails`.** **Inference:** consumer harm in SA is mostly authorised fraud and bank processing errors. A simulator addresses neither. The engineering problem `rails` models is real, though. Peach documents "Pending -> Successful, cancelled, or uncertain" and "Uncertain or cancelled -> Successful". It also warns it "cannot guarantee the order of webhooks" and retries for "30 days" ([Peach checkout webhooks](https://developer.peachpayments.com/docs/checkout-webhooks)). That is the "unknown state", in a local PSP's own documentation.

### 1c. Instant payments and Request-to-Pay adoption

- **Volumes, and a conflict.** Stitch (vendor, 28 Jul 2026) says "over R100 billion across more than 136 million transactions" since launch, and also "45 million PayShap transactions per month" by late 2025 ([Stitch](https://stitch.money/blog/real-time-payments-in-south-africa-the-state-of-payshap-in-2026)). Those two figures don't fit together, and both conflict with PayInc's own 329 million in FY2025 (prior file). **Use PayInc's figure. Stitch's cumulative number is Unverified.**
- **Merchant barriers, as vendors see them.**
  - Stitch: "The registration requirement remains a real friction point", the bank experience is inconsistent, and recurring payments are still on the roadmap.
  - Hyphen's CFO (8 Apr 2026): "asking consumers to cover a fee … is a difficult expectation to set", and RTP lacks DebiCheck's reliability for recurring collections ([Hyphen](https://hyphen.co.za/news/payshap/)).
  - Both are vendor opinion. Neither names integration complexity as the merchant's problem.
- **Integration complexity sits with participants, not merchants.**
  - In 2024 "PayShap is open only to banks". MTN joined via Investec, which "found a commercial model to make that work", with Electrum as technology provider ([BusinessDay, 25 Apr 2024](https://www.businessday.co.za/bd/companies/telecoms-and-technology/2024-04-25-mtn-finds-a-way-to-join-payshap/)).
  - The draft Authorisation Framework lists the activities as e-money issuing, acquiring, clearing and settlement, payment initiation, third-party payments, schemes management and money remittance ([Webber Wentzel via Polity](https://www.polity.org.za/article/south-africas-payments-regulatory-framework-third-draft-of-authorisation-framework-published-for-comment-2026-05-22)).
  - **Unverified:** no primary source quantifies ISO 20022 integration cost for small non-bank entrants.

### 1d. Ledger correctness at fintechs

| Evidence | What it shows |
|---|---|
| CFPB v. Synapse (complaint 21 Aug 2025) | "failing to maintain adequate records of the location of consumers' funds and failing to ensure those records matched the records maintained by its partnering banks"; shortfall "between $60 and $90 million" ([CFPB](https://www.consumerfinance.gov/enforcement/actions/synapse-financial-technologies-inc/)). **This is the canonical ledger-plus-reconciliation failure** |
| Stripe, *Ledger* (Ganelin, 16 Feb 2024) | Five billion events a day. Checks for clearing, timeliness and completeness; "over 99.9999% explainability of money movement" ([stripe.dev](https://stripe.dev/blog/ledger-stripe-system-for-tracking-and-validating-money-movement)) |
| Uber, *Payments Platform* (6 Aug 2026) | "ledger balances for more than 1.2 billion entities". Ledger-as-a-Service, multi-tenant ledgers "operating reliably for over 7 years" ([Uber](https://www.uber.com/us/en/blog/ubers-payments-platform/)) |
| Modern Treasury, *How and Why Homegrown Ledgers Break* (2022) | "incorrect payouts, incorrect user balances, missing funds, or money created out of nothing" ([MT](https://www.moderntreasury.com/journal/how-and-why-homegrown-ledgers-break)) |
| Airbnb, Orpheus idempotency framework | "five 9s … of consistency" is from secondary summaries; the Medium original returned 403. **Unverified at source** |

**SA examples.** No SA fintech has published a ledger postmortem that I could find. The SA incidents above are bank-side and have no stated root cause.

---

## 2. Existing solutions and competitors

| Layer | South Africa | Global | Commoditised? |
|---|---|---|---|
| Double-entry ledger | None advertised (prior file) | Formance (MIT, Go; prior file); **Blnk** ("open-source, double-entry ledger", Apache-2.0, Go, includes matching against "bank statements or payment processor exports") ([README](https://raw.githubusercontent.com/blnkfinance/blnk/main/README.md)); TigerBeetle; Modern Treasury | **Yes** |
| Idempotent API, signed webhooks | Every PSP (Peach retries and timestamps, above) | Stripe pattern (prior file) | **Yes, as knowledge** |
| PayShap access | PayInc; Electrum; sponsor banks (Investec); PSPs (Ozow PayShap Request) | — | **Not a market for an outsider** |
| Enterprise reconciliation | **Stitch Reconciliation**: "Reconcile payments across methods and providers", exception management, "daily reporting across banks, providers and methods" ([Stitch](https://stitch.money/reconciliation)). **TJ Recon Pro** (Reconciliation-as-a-Service on AWS, CSV/JSON/Kafka, exceptions you can "snooze, resolve, annotate, and audit"). **Ecentric ReconAssist**. **Precium** ("multi-channel reconciliation, exception management", search summary). SmartStream TLM at "one of South Africa's largest banks" ([Finextra](https://finextra.com/pressarticle/16772/smartstream-reports-south-african-bank-deal), search result) | Duco, SmartStream, Simetrik (LatAm; one PSP "consolidated reconciliation across 25 partners", vendor claim via search), Modern Treasury (1-to-1 and many-to-1, Expected Payments, rules, manual exceptions; [docs](https://docs.moderntreasury.com/reconciliation/docs)), Formance Reconciliation | **Yes, for enterprise** |
| SME reconciliation | Xero JAX, bank feeds, per-PSP Xero apps, Stitch Express | A2X, Reconcile.ly (Shopify-centric) | **Per-PSP, yes. Across SA PSPs, no evidence found** |
| AI break explanation | Xero JAX "Memory" and "Prediction" categorise; they do not explain breaks with citations | — | **Inference:** still a differentiator, but Xero is moving into the space |

**Where the real gap is (Inference):**

1. **SME and mid-market multi-PSP payout decomposition into Xero or Sage**, using local export formats. This is the strongest gap.
2. **Explaining why a payout is short** (fees, refunds, chargebacks, holds, a sliding-scale fee adjustment, timing), with evidence.
3. **Client-funds reconciliation for small payment institutions**, if the Authorisation Framework is finalised as drafted.

---

## 3. Verdict per project

| | `ledger` | `rails` | `recon` |
|---|---|---|---|
| Real problem? | Yes (Synapse, Stripe, Uber) | Yes for participants; not for merchants | Yes; vendors sell it locally |
| Who pays? | Fintechs, internally; Modern Treasury and Formance customers | PayInc participants and PSPs, internally | Enterprise via Stitch, TJ, Ecentric; SMEs via Xero and Sage subscriptions and PSP plans (Yoco Pro R499/month) |
| Standalone portfolio version | **Exercise.** Nobody adopts a portfolio ledger over Formance or Blnk | **Exercise.** No outsider can test against PayShap; participants use PayInc's own environment (**Unverified**) | **Credible** if real users can run it |
| How to make it credible | Make it the clearing sub-ledger: one clearing account per PSP; fees, refunds, chargebacks, holds as postings; a "client funds" view matching draft Annexure A 9.1.2. Keep the invariants and property tests from the prior file | Rename it and make it the **ground-truth generator**: emit Yoco, Peach and Paystack-shaped exports, bank CSV and OFX, and webhook streams with `uncertain`→`Successful`, out-of-order and duplicate events. The ISO 20022 messages stay as one adapter, not the pitch | Read each PSP's real export columns (Yoco "Online Reference", Peach settlement batch, Paystack batches), Standard Bank CSV and OFX, and Investec sandbox JSON. Handle many-to-one matches. Publish match rate against injected ground truth. Get a handful of real merchants or bookkeepers to run it locally on their own exports |

`camt.053` stays in, but as the corporate path. **Inference from Standard Bank's export list:** CSV and OFX are what SMEs can actually download.

---

## 4. Sharper framings

### Framing 1 (recommended): payout reconciliation for SA merchants on several PSPs

- **User:** small and mid-sized merchants who take money through two or more of Yoco, Payfast, Peach, Paystack and Ozow, plus EFT or PayShap, and close into Xero or Sage. Also the bookkeepers who serve many such clients. **Inference:** bookkeepers are the multiplier.
- **Pain (cited):**
  - Every PSP pays net, batched deposits (§1a).
  - Each Xero integration covers one PSP, or only invoices.
  - Mid-market reconciliation takes weeks (Ecentric).
  - Enterprise buys tools (Stitch, TJ).
  - **SME severity is Unverified.** No survey quantifies it.
- **What the three repos become:**
  - `recon` is the product: ingest exports and bank files, decompose payouts, exceptions queue, AI explainer with citations to the rows it read.
  - `ledger` is its clearing sub-ledger and the journal export to Xero or Sage.
  - `rails` is the simulator that produces the seeded breaks the evals score against.
- **Employers it speaks to:** Stitch (sells exactly this upmarket), Yoco, Peach, Paystack, Ozow, and Investec through the programmable-banking feed. Also Dariel and Entelect, if they build reconciliation for clients (**Unverified**). It matches the "reconciliation" wording the prior file found in postings.
- **Can real users try it?** **Yes.** This is the only framing where they can.
  - POPIA: PSP exports can carry customer names (Peach's reconciliation reports include "customer name").
  - Design to process locally or in the browser, strip PII columns on import, and store nothing.
  - If it is ever hosted, the operator contract under s21 and the s72 cross-border rules apply (prior file).

### Framing 2: client-funds safeguarding for a small non-bank payment institution

- **User:** third-party payment providers, small PSPs, money remitters and e-money issuers preparing for the Authorisation Framework.
- **Pain (cited):** draft Annexure A 9.1 (segregate client funds and "properly identify" them in the books), 17.1.9 (acquirer segregated accounts), 39.8 (remitters must "at all times" reconcile segregated funds to transactions), and Synapse as the failure case.
- **What the three repos become:**
  - `ledger`: separates own funds from client funds.
  - `rails`: a sponsored-participant PayShap simulator with timeouts.
  - `recon`: a daily safeguarding reconciliation (segregated-account statement against client liabilities) with shortfall alerts.
- **Employers it speaks to:** Ozow, Stitch, Peach, Paystack, Mama Money, Precium, Investec as sponsor bank.
- **Can real users try it?** **No.** It is a reference implementation; no institution uploads client-funds data to a stranger. There is also a risk that the final framework changes the rules.

### Framing 3: a lender or collector reconciling disbursements and collections

- **User:** small lenders, collection agencies and insurers on DebiCheck or EFT debit orders who pay out by PayShap or EFT.
- **Pain (cited):** the 60-day dispute window from 13 April 2026 (PASA), and failure classification by cause ([Stitch, 14 Aug 2026](https://stitch.money/blog/debit-order-debicheck-best-practices-for-south-african-debt-collection-agencies)).
- **What the three repos become:**
  - `ledger`: a loan sub-ledger.
  - `rails`: a mandate, unpaids and disputes simulator.
  - `recon`: collections against bank, unpaid reasons and a dispute-window tracker.
- **Employers it speaks to:** Jumo, Precium, Stitch, Capitec.
- **Can real users try it?** **Hard.** National Credit Act scope, account-number offences under POPIA ss105–106 (prior file), and DebiCheck can't be tested without a sponsor.

**Recommendation: Framing 1, with Framing 2's client-funds view as one extra chapter.** It costs little because it uses the same ledger. Framing 1 is the only one with users who can try it, it matches the prior file's evidence on postings, and vendors already selling it upmarket shows people pay for it. "Measured results" would be three numbers:

1. Match rate and false-match rate against seeded ground truth.
2. A pilot user's month-close effort against their own Excel baseline, self-reported and labelled as such.
3. Eval pass rate for break explanations whose cited rows exist and support the claim.

---

## 5. Name ideas for Framing 1

For every name, `gh api repos/MorenaDlamini/<name>` returned **404 Not Found** (unused). The account has 5 public repos (Codecast, dotnet-ai-engineering, groundbreak, MorenaDlamini, rentscape), and none collide. These were web searches, **not a CIPC trademark search**. **Unverified for trademarks.**

| Name | Meaning | Web check | Verdict |
|---|---|---|---|
| **randmatch** | Rand plus match; says what it does | Only Rand Stadium and currency results | **First choice** |
| **sluit** | Afrikaans "close", as in close the books | No app or fintech found | Good. Non-Afrikaans readers may not get it |
| **payoutline** | Payout line items | No product found; "PayOut API" (AOPAY) is unrelated | Clear but generic |
| **netoff** | Netting-off accounting term | Only an Odoo module feature name | Accurate; hard to own as a brand |
| **balans** | Afrikaans "balance" | No SA fintech found. Close to Balanz (Argentine broker) and Balance (US B2B payments) | Usable, with mild confusion risk |

Rejected (also 404 on GitHub, but they collide with existing brands):

- **klaar** — sounds like Klar, the Mexican neobank ([Retail Banker International](https://www.retailbankerinternational.com/news/neobank-klar-raises-90m/)).
- **tickey** — an existing TICKEY transport-ticketing app, plus a ClimateLaunchpad "Tickey".
- **kasbook** — KashBook, a Nigerian shop-ledger app.
- **tallyrand** — leans on Tally, a heavily trademarked accounting brand.
- **settlebook** — Settle, a US B2B payments company.

---

## Open questions

1. **How big is the multi-PSP SME segment?** No source counts merchants on two or more PSPs. Five conversations with SA bookkeepers would answer it better than more desk research.
2. **Is the final Authorisation Framework out?** It was promised for Q3 2026, and no final was found on 2026-10-01. Framing 2 depends on it.
3. **Is there an A2X or Synder connector for Payfast, Yoco or Peach?** Not found. If one exists, the Framing 1 gap shrinks.
4. **What exactly is in Ozow's settlement report?** The docs host did not resolve.
5. **Should `rails` keep the PSP sandbox adapters (Peach, Yoco)?** Only if they produce real export shapes for recon. Otherwise they are integration exercises.

---

## Sources

All read 2026-10-01 unless marked "search summary" (figures taken from a search engine's digest, not the page itself).

**PSPs and vendors**
- Yoco, *When will I get my money?*: https://www.yoco.com/za/blog/when-will-i-get-my-money/
- Yoco, reconciling Checkout API payments: https://developer.yoco.com/guides/online-payments/reconciliation/reconciling-checkout-api-payments-with-daily-payouts
- Peach, settlements: https://support.peachpayments.com/support/solutions/articles/47001250592-understanding-your-peach-payments-settlements ; https://developer.peachpayments.com/docs/dashboard-reporting-settlements ; checkout webhooks: https://developer.peachpayments.com/docs/checkout-webhooks
- Paystack, payouts: https://support.paystack.com/hc/en-us/articles/360012149479-When-will-I-receive-my-payouts
- Ozow, Xero: https://www.ozow.com/integrations/xero ; PayShap Request: https://ozow.com/our-products/instant-payments-with-payshap-request
- Stitch, Reconciliation: https://stitch.money/reconciliation ; Express accounting: https://stitch.money/express-accounting ; State of PayShap 2026: https://stitch.money/blog/real-time-payments-in-south-africa-the-state-of-payshap-in-2026 ; DebiCheck best practices: https://stitch.money/blog/debit-order-debicheck-best-practices-for-south-african-debt-collection-agencies
- Hyphen, *Three years of PayShap*: https://hyphen.co.za/news/payshap/
- Transaction Junction, TJ Recon Pro: https://transactionjunction.co.za/wp-content/uploads/2025/09/The-Retailers-Guide-to-Financial-Precision_TJ-Recon-Pro.pdf
- Ecentric ReconAssist (Bizcommunity): https://www.bizcommunity.com/article/automation-efficiency-and-accuracy-for-sa-retailers-its-time-for-reconassist-561290a
- Netcash: https://netcash.co.za/blog/invoice-to-cash-in-days-a-practical-guide-to-faster-reconciliation-in-sa/
- Visa, Value of Acceptance SA (2024): https://africa.visa.com/content/dam/VCOM/regional/cemea/genericafrica/run-your-business/value-of-acceptance/voa-designed-generic-report-south-africa.pdf
- Sage ZA, admin burden: https://www.sage.com/en-za/blog/small-business-admin/

**Accounting tools and banks**
- Xero App Store: Yoco https://apps.xero.com/za/app/yoco ; Paystack https://apps.xero.com/za/app/paystack ; Reconcile.ly https://apps.xero.com/za/app/reconcilely
- Xero ZA bank reconciliation: https://www.xero.com/za/accounting-software/reconcile-bank-transactions ; AI release: https://www.xero.com/media-releases/xero-unveils-new-ai-powered-tools-south-africa/
- Standard Bank OB4B export guide: https://www.standardbank.co.za/static_file/South%20Africa/PDF/How%20To%20Guides/OB4B%20How-to%20guide%20-%20Downloading%20transaction%20history.pdf

**Ombud, regulators, industry**
- NFO: https://nfosa.co.za/nfo-banking-division-returns-r60-million-to-consumers-in-2025/ ; https://nfosa.co.za/nfos-second-year-surge-r442-9-million-restored-to-consumers/
- PASA, DODE FAQ: https://pasa.org.za/wp-content/uploads/2026/04/PASA_DODE_FAQ_v3.pdf
- SARB, draft Authorisation Framework (Annexure D): https://www.resbank.co.za/content/dam/sarb/publications/prudential-authority/pa-public-awareness/communication/2026/prudential-communication-10-of-2026/Annexure%20D-%20Draft%20Authorisation%20Framework.pdf
- Webber Wentzel via Polity: https://www.polity.org.za/article/south-africas-payments-regulatory-framework-third-draft-of-authorisation-framework-published-for-comment-2026-05-22
- SABRIC 2025 release (search summary): https://www.sabric.co.za/?p=4450
- CFPB, Synapse: https://www.consumerfinance.gov/enforcement/actions/synapse-financial-technologies-inc/

**News**
- IOL (NFO cases): https://iol.co.za/personal-finance/financial-planning/2025-06-28-words-on-wealth-report-reveals-shocking-admin-failures-by-banks-and-credit-firms/
- EWN (wrong-account EFT): https://www.ewn.co.za/2024/10/23/bank-cant-reverse-r63k-i-paid-into-wrong-account-after-recipient-refused-to-return-the-money
- Stuff (FNB duplicates): https://stuff.co.za/2026/03/06/fnb-customers-duplicate-charges-can-rest-easy/
- BusinessDay (MTN and PayShap): https://www.businessday.co.za/bd/companies/telecoms-and-technology/2024-04-25-mtn-finds-a-way-to-join-payshap/
- Klar: https://www.retailbankerinternational.com/news/neobank-klar-raises-90m/

**Engineering**
- Stripe Ledger: https://stripe.dev/blog/ledger-stripe-system-for-tracking-and-validating-money-movement
- Uber Payments Platform: https://www.uber.com/us/en/blog/ubers-payments-platform/
- Modern Treasury: https://www.moderntreasury.com/journal/how-and-why-homegrown-ledgers-break ; https://www.moderntreasury.com/journal/recon-diaries-entry-ii-banks-are-the-enigma ; https://docs.moderntreasury.com/reconciliation/docs
- Blnk README: https://raw.githubusercontent.com/blnkfinance/blnk/main/README.md

**Search summary only (not read at source):** Ozow settlements guide; Paystack SA payout schedule; Xero SA bank-feed list; Sage–FNB feeds; Payfast–Xero clearing-account complaints; Simetrik; Formance Reconciliation; Precium; SmartStream SA deal; Airbnb Orpheus; Capitec/Nedbank 2020 duplicates; debit-order dispute volumes.

**Unreachable:**
- `oldhub.ozow.com` (DNS failure)
- `xero.com/za/connect-banks/` (404)
- Payfast Xero reviews (404)
- Stitch support article (403)
- Standard Bank–Precium article (403)
- Airbnb Medium post (403)
- SARB *NPS Regulatory and Oversight Report 2025–2026*: too large for WebFetch, and curl returned a bot page, so it is unread
- BIS Nexus investigation page (404)
