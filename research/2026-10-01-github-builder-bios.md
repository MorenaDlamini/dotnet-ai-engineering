# GitHub profile bios that say "I build things": research and drafts for Morena Dlamini

Researched 2026-10-01. Every bio below was pulled with `gh api users/<login> --jq '{login,name,bio,company,blog,location}'`. README openings came from `gh api repos/<login>/<login>/readme --jq .content | base64 -d | head`. Each profile is also at `https://github.com/<login>`. Character counts were measured with `wc -m`. All drafts are plain ASCII, so characters and bytes match.

## 0. Two problems to fix before the bio

1. **No public repo backs the fintech claim yet.** Your public repos are `Codecast`, `rentscape`, `dotnet-ai-engineering`, `groundbreak` (Python, no description) and the profile repo (`gh api users/MorenaDlamini/repos`). None is about payments, ledgers or reconciliation. A bio that says "in my public repos: payments, ledgers" would overclaim today. Drafts 1, 3, 4, 5, 6 and 8 below are safe now. Drafts 2 and 7 need a pinned ledger or reconciliation repo first.
2. **Your "Start here" repo undercuts any new bio.** `dotnet-ai-engineering` is described as *"a Junior-to-Mastery curriculum"*. Your `blog` field and the first link in your README both point to it. That is the same "aspiring" signal you're removing from the bio, so rewrite the description too, e.g. "C#/.NET + AI engineering notes; every claim links to tests, ADRs, postmortems."

## 1. Profiles read (31)

| login | bio (verbatim) | company / blog | what it signals |
|---|---|---|---|
| davidfowl | "Distinguished Engineer 🧐 at Microsoft" | Microsoft / hachyderm.io/@davidfowl | Title plus employer, nothing else |
| stephentoub | "Distinguished Engineer at Microsoft" | Microsoft | Same; one line is enough |
| JamesNK | "Software Developer. Author of Json.NET." | @microsoft / james.newtonking.com | **Names the artefact.** Plain job title, then the thing everyone uses |
| andrewlock | "Read my book ASP.NET Core in Action, Third Edition: http://mng.bz/69Ry" | andrewlock.net | Artefact-first: points straight at the book |
| Elfocrash (Nick Chapsas) | "Content creator for C# & .NET" | dometrain.com | Says plainly what he does |
| m-jovanovic | "Software Architect, Microsoft MVP, .NET Tech YouTuber" | milanjovanovic.tech | Credential list. README is badge-heavy and says "currently working on: Mastering…", which reads as learning |
| jbogard | "The Barley Architect, Architect Consultant" | Jimmy Bogard Consulting, LLC | Wordplay only works because he's well known |
| ardalis | "Software developer, training, architect with over 25 years of experience. Parallel entrepreneur. Cofounded NimblePros w/wife Michelle." | NimblePros / ardalis.com | Years of experience plus a company he founded |
| jasontaylordev | "Solutions Architect • Microsoft MVP" | @Particular / jasontaylor.dev | Title plus credential. README opens with "25 years of experience across legal, government, logistics, **financial services**…" |
| kgrzybek | "Husband. Father. Head Of Software Engineering \| Software Architect \| Team Leader \| Developer. Enthusiast. Software Architecture & Design. Domain-Driven Design." | kamilgrzybek.com | Title pile-up; weaker than one clear claim |
| damianh | "DDD/SOA/ES/IDENTITY/.NET" | @DuendeSoftware | Keywords only. README is the untouched GitHub template ("Hi there 👋"), which hurts |
| Aaronontheweb | "CEO @petabridge … Maintainer: @akkadotnet" | Petabridge, LLC | Founder plus the OSS he maintains. README: "I build OSS .NET technologies aimed at making it easier to build large-scale applications." |
| Mpdreamz | "@editorconfig board member. Principal Engineer @elastic." | @elastic / localghost.io | Two concrete roles |
| khalidabuhakmeh | "Loves @NicoleAbuhakmeh. #Photoshop Whisperer. #OSS supporter. @dotnet developer. @dotnet-foundation member." | @DuendeSoftware | Personality; relies on being known |
| steipete | "Came back from retirement to mess with AI. Clawdfather @OpenClaw … Previously: Founder of @PSPDFKit." | OpenAI / steipete.me | **"Previously: Founder of X"** as the credential. README then has a wall of skill badges |
| simonw | *(null)* | Datasette / simonwillison.net | No bio. README line 1: "Currently working on Datasette, LLM…", then auto-generated **Recent releases** with dates |
| mitchellh | *(null)* | @superlogical / mitchellh.com | Work is famous enough to need nothing |
| rauchg | *(null)* | vercel.com | Same |
| tj | *(null)* | Apex | Same |
| swyx | *(null)* | none | Same |
| karpathy | "I like to train Deep Neural Nets on large datasets." | twitter.com/karpathy | Plain first-person description of what he does |
| antirez | "Computer programmer based in Sicily, Italy. I mostly write OSS software. Born 1977. Not a puritan." | Redis Labs / invece.org | Plain and personal, no buzzwords |
| levelsio | "Chief Shitposting Officer @ Levels Synergies & Co" | levels.io | Joke bio; only works at that fame |
| t3dotgg | "I'm just here for the vibes, man" | CEO @ Ping.gg / t3.gg | Same; the company field does the work |
| leerob | "Teaching developers about AI" | Cursor / leerob.com | Says what he does now |
| fabpot | "Founder and project lead at Symfony / CTO at Upsun" | Symfony/Upsun | Founder plus role |
| brandur | "APIs, Go, terminal productivity, running, and metal. Engineering @ @riverqueue. Ex-@heroku, **ex-@stripe**, ex-@crunchydata…" | @riverqueue / brandur.org | **Past employers as credentials**, including a payments one |
| jorangreef | "Creator, Founder and CEO of @TigerBeetle, the financial transactions database for mission critical safety and performance." | @tigerbeetle | **Fintech domain-first**: one line on what the product does |
| patio11 | "Working for the Internet." | kalzumeus.com | Understatement |
| **South Africa / fintech** | | | |
| theronic | "Staff Engineer at Peach Payments. Full-stack entrepreneur. Clojure enthusiast. Previously: CTO of CloudAfrica, CTO of weFix South Africa (@iFix)." | @peach-payments | SA payments engineer: current role plus "Previously:" CTO roles. README: "Making software professionally for 20+ years… Author of EACL." |
| yashiels | "Engineer @Stitch-Money" | @Stitch-Money / yashiel.dev | README line 1: "**I build companies and ship products.**" Line 2: "Payments infrastructure powering Africa's biggest brands." |
| jeremywagemans | "Engineering @Stitch-Money, @evervault, @stripe & @touch-tech-payments" | Evervault | Payments track record listed as orgs |
| kialanpillay | "Founding Engineer & Chief AI Officer @ Amorphous AI. Ex Stitch Money, AWS / Oxford MSc" | Amorphous AI | "Ex-" credentials |
| DanielVenter | "Quantitative Developer at Investec" | none | Plain role |
| igitur | ".NET full stack developer. Actuarial / quantitative finance background. Jack of all trades - master of none." | none | Strong domain line, then self-deprecation that undoes it |
| mattleibow | "Home is where the [.NET] compiler is..." | @Microsoft @xamarin @mono | The company field does the work |
| govert | *(null)* | Excel-DNA | The artefact *is* the company field |
| **Junior-signal examples (SA search)** | | | |
| KabeloDev | "Software Engineer. **Passionate about** building clean, scalable, and user-friendly applications. Feel free to take a look at my projects." | none | "Passionate", generic adjectives, asks for attention |
| Thabangmontja | "Software Engineer \| Backend Developer \| Power Platform Developer🧑‍🚀🚀📚. **Perfecting my craft**⌛📈. Empowering Progress Through Code 💡." | none | Emoji wall, slogan, learning frame |
| Sam-Boleke | "👨‍💻 Full-Stack Developer \| Flutter • Next.js • Node.js 🤖 **Exploring** AI/ML & SaaS products 🌍 **Passionate about tech, learning** & impact" | none | Stack soup plus exploring, passionate, learning |
| 3arlN3t | "**Continuously learning** web development. Favorite technologies ASP.NET" | Personal | Learner frame, nothing shipped |
| ArnoldT01 | "Full-Stack Software Engineer \| 3+ years exp \| .NET \| C# \| Java ..." | none | Pipe-separated keyword soup |
| siyavuyachagi | "Software Developer \| Specializing in C# \| TypeScript \| Vuejs/Nuxtjs \| **Passionate about** clean code and software architecture." | Kinetic Studios | Same |

SA lists come from `gh api search/users -X GET -f q='location:"South Africa" language:C#'` and `-f q='<company> in:company'`, run for Stitch, Peach Payments, Investec, Paystack, Yoco, Ozow, Floatpays and TymeBank. The Yoco, Ozow and TymeBank searches turned up no engineers with real bios. `mjovanovictech` and `pieterlevels` don't exist; the real logins are `m-jovanovic` and `levelsio`. `dhh` returned 404.

**GitHub Docs:**
- "The bio field is limited to 160 characters" ([Personalizing your profile](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/personalizing-your-profile)).
- Up to four social account links (same page).
- You can @mention organizations you're not a member of, e.g. a past employer (same page).
- Pins: "Select up to six repositories and gists, combined" ([Pinning items](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/pinning-items-to-your-profile)).
- The profile README shows when a public repo has your username as its name ([Managing your profile README](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme)).

## 2. Patterns

1. **Name the artefact, not the trait.** "Author of Json.NET" (JamesNK). "Read my book ASP.NET Core in Action" (andrewlock). "Author of EACL" (theronic). Nobody strong describes themselves with adjectives like "clean, scalable, user-friendly".
2. **Domain plus outcome in one plain clause.** "the financial transactions database designed for mission critical safety and performance" (jorangreef, tigerbeetle). "Payments infrastructure powering Africa's biggest brands" (yashiels README). This is the model for your fintech positioning.
3. **"Previously:" / "Ex-" carries past credentials.** steipete, theronic, brandur, kialanpillay. You can't name your employer, so describe the *kind* of system instead: "Shipped: offline-first apps…".
4. **Declarative first person, present tense.** "I build OSS .NET technologies…" (Aaronontheweb). "I build companies and ship products." (yashiels). "I like to train Deep Neural Nets…" (karpathy). "I mostly write OSS software" (antirez).
5. **Short is fine; blank or joke bios need fame.** simonw, mitchellh, rauchg, tj and swyx leave the bio empty. levelsio, t3dotgg and jbogard use jokes. Their work is already known. Someone less known needs the bio to do the work, so copy their plainness, not their emptiness.
6. **The company and blog fields work alongside the bio.** govert ("Excel-DNA") and mattleibow do more there than in the bio. You can't use `company`, so `blog` should point at the strongest proof of what you build, not a curriculum.
7. **Junior signals in this sample:** "passionate", "learning", "exploring", "perfecting my craft", emoji runs, pipe-separated stack lists, "feel free to look at my projects", self-deprecation ("master of none"). Every bio with these came from the unknown/junior group.
8. **READMEs: the strong ones show proof by line 2–3; weak ones are template or decoration.**
   - Strong: simonw, line 1 "Currently working on…", then dated releases. theronic: years, degree, current role, authored project. jasontaylordev: years, domains including financial services, what he specialises in. yashiels: a one-line claim, then three domains.
   - Weak: damianh's untouched template; m-jovanovic's view counter and "Mastering…"; rmaclean's animated banner; steipete's skill-badge wall (survivable only because of line 2).

## 3. Eight draft bios

| # | Style | Bio | Chars | Safe today? |
|---|---|---|---|---|
| 1 | Outcome-first | I ship C#/.NET software that keeps working when the network doesn't, and reconciles when it comes back. Next: payments and ledgers for South Africa. | 148 | Yes |
| 2 | Domain-first | C#/.NET engineer for systems where the numbers must agree: offline sync, ERP-to-cloud pipelines, and an open-source payments ledger with reconciliation. | 152 | Only once the ledger repo is public |
| 3 | Artefact-first (production) | Shipped in production: offline-first apps that reconcile on reconnect, ERP-to-cloud pipelines, real-time dashboards. C#/.NET, SQL Server, React, Azure. | 151 | Yes |
| 4 | Plain-stack | Full-stack C#/.NET engineer shipping production software. ASP.NET Core, SQL Server, React/TypeScript, Azure, LLM features with Microsoft.Extensions.AI. | 151 | Yes |
| 5 | Problem-first (fintech) | Money has to add up even when the network drops. C#/.NET engineer: offline-first sync, ERP integration, and ledger and reconciliation systems. | 142 | Yes, though "ledger systems" is thin until a repo exists |
| 6 | Minimal | C#/.NET engineer. I build systems where the numbers have to reconcile. | 70 | Yes |
| 7 | Shipped / Building | Production C#/.NET engineer. Shipped: offline-first apps, ERP-to-cloud pipelines, real-time dashboards. Building: a payments ledger in .NET (pinned). | 149 | Only once it's pinned |
| 8 | Availability | C#/.NET engineer shipping offline-first, data-heavy production software. Open to building payments, ledger and reconciliation products in South Africa. | 151 | Yes |

None of them names your employer or uses "learning", "aspiring" or "passionate". "Johannesburg" is left out because your `location` field already shows "Johannesburg, South Africa".

**Top 2:**

- **#1 (outcome-first).** It follows the pattern of the strongest builder bios: first person, one concrete outcome. "Reconciles when it comes back" is true of your shipped work and is exactly what a fintech founder wants to hear, because reconciliation is the core of ledgers and payments. "Next:" states your direction without claiming fintech employment, and it holds up today with no new repo.
- **#7 (Shipped / Building), once the ledger repo is pinned.** It mirrors steipete's and theronic's "Previously:" line without naming the employer. It splits proven work from portfolio work, so it can't be read as overclaiming. And "(pinned)" sends the reader straight to evidence, which is the JamesNK/andrewlock move.
- **Order of use:** #1 now, switch to #7 when the repo ships.

## 4. First three lines of the profile README

```markdown
# Morena Dlamini

I build C#/.NET software that keeps working when the network doesn't: offline-first desktop and tablet apps that reconcile when signal returns, ERP-to-cloud pipelines, and real-time operational dashboards, in production and used every day by people who aren't developers.

Now building payment, ledger and reconciliation systems in .NET for the South African market, starting with **[repo-name](link)**: <one line on what it does, e.g. double-entry ledger, idempotent payment intake, bank-statement matching>.
```

- **Why it works:** line 1 makes a first-person claim with the outcome (as Aaronontheweb and yashiels do). It reuses your existing "At work" facts, so nothing new is claimed. Line 2 points at one artefact by name (as simonw and theronic do).
- **What to remove:** "Learning in public" and the "Junior-to-Mastery" curriculum framing. Move `dotnet-ai-engineering` below the fintech repo, or retitle it as engineering notes with evidence.
- **Until the fintech repo exists:** end line 2 at "…for the South African market." and add the link later.
- **Keep:** the "The code is private. Ask me about any of the design decisions behind it." line from your current README. It's a confident substitute for the employer credential you can't use.

## Outcome

On 2026-10-01 the user chose a minimal bio instead of any draft above: **"C#/.NET Full Stack Software Engineer"**. The drafts stay here for when `randmatch` ships and a Shipped / Building line (#7) is earned.
