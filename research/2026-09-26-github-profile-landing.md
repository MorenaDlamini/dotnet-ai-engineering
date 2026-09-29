# From status report to landing page: the GitHub profile, measured against steipete

Primary-source research, done on 2026-09-26, to answer one question: how should the profile
at `github.com/MorenaDlamini` grow toward the style of `github.com/steipete`? The complaint is
that the current profile "shows too much of what I am doing, where I am". It reads like a
progress report on learning, when it should be a landing page for work.

A source here is the GitHub REST or GraphQL API, read as `MorenaDlamini` with `gh api` on
2026-09-26, or a docs.github.com page, or the rendered page itself. The API endpoints are
quoted inline so every number can be checked again. Local files are cited by path. Anything I
am inferring rather than reading is marked **Inference** or **Unverified**. Star and follower
counts are a snapshot from one day and will go stale.

---

## The verdict

**Copy steipete's discipline, not his volume. The page's problem is not that it is too short
or too plain. It is that three surfaces point at the plan rather than the work: the website
field, the pins, and the lower half of the README. Fix those three. The `platform` and
`product` ships will fill the rest over time.**

1. **steipete's profile is not minimalist. It is curated.** His profile README exists, and it
   is long: about 80 project links in nine groups. What makes it work is the rule behind it.
   A `VISION.md` in the profile repo says the README must stay "a concise, current map of who
   Peter is, what he is building, and where people can find the canonical projects". Every
   entry is a shipped thing with its own homepage and a one-line benefit. Nothing on the page
   describes what he is learning.
2. **The MorenaDlamini page's "where I am" signal mostly comes from outside the README.** The
   profile's website field (`blog`) points at `CURRICULUM.md`. Two stale side projects are
   pinned (last pushed 2026-03-09) and `worked-examples` is not pinned at all. The README ends
   with "What I'm working toward". A visitor who clicks the one link in the sidebar lands on a
   study plan.
3. **The profile currently names the employer, twice.** The `company` field is
   `[employer]`, and the README's first line is "Software engineer at [employer],
   Johannesburg — a [employer industry] manufacturer". This breaks the standing rule
   that the profile does not name or reference the employer. It is the first thing to fix,
   ahead of any matter of style.
4. **What can be copied now:** structure (Start here → what I build → contact), tone (one line
   per item, stated as a benefit), repo descriptions written as product lines, a homepage on
   every repo that has one, topics, and a `VISION.md`-style rule for the profile repo.
   **What has to be earned:** stars, followers, vanity domains that people type, a TED talk,
   and an 80-item map. For this account, the way to earn them is to ship `parity` and then
   `municipal-money` to PyPI, with each ship adding one line and one pin.

---

## 1. What steipete's profile actually consists of

### Sidebar fields

From `gh api users/steipete`:

| Field | Value |
|---|---|
| `bio` | "Came back from retirement to mess with AI. Clawdfather @OpenClaw\r\n\r\nPreviously: Founder of @PSPDFKit." |
| `company` | `OpenAI` |
| `location` | `London / San Francisco` |
| `blog` | `http://steipete.me` |
| `hireable` | `null` |
| `followers` / `public_repos` | 52,897 / 218 |

Social accounts (`gh api users/steipete/social_accounts`): X, Mastodon, Bluesky. The rendered
page (fetched from `https://github.com/steipete`) also showed a status line, "🤖 beep boop".

What to notice: the bio is three short clauses in his own voice. It gives what he does now,
what he runs, and one past credential. Nothing in it says what he is learning. The website
field points at his own site, and that site's tagline is also about output: "AI-powered tools
from Swift roots to web frontiers. Every commit lands on GitHub for you to fork & remix."
(WebFetch of `https://steipete.me`.)

### The profile README exists, and it is a project map

`gh api repos/steipete/steipete/readme` returns a README. It is not a 404, so the idea that
steipete has no README is wrong. In order, it has:

1. `# Hi, I'm Peter 👋`, then one line of three badges-as-text ("📍 Vienna ↔ London | 🤖
   Polyagentmorous builder | 🚀 Ex-PSPDFKit Founder"), then one sentence: "Now at OpenAI,
   working on agents; stewarding OpenClaw as open and independent."
2. A row of nine shields.io technology badges (Swift, TypeScript, … macOS, Web).
3. **Start Here**: seven items. Each one is emoji + linked name + coarse star count + a benefit
   of a few words, for example "🎚️ **CodexBar** (20k+ stars) - keep agent limits in view".
4. **Current Projects**: about 70 items in eight themed groups ("Agent Runtime & Dev Tools",
   "Local Archives & Crawlers", "macOS, Swift & Native Automation", …). Each item has the same
   shape as above, minus the star count. Most items link to a product domain (`gogcli.sh`,
   `mcporter.sh`, `crabbox.sh`), not to the repo.
5. **Legacy Work**: older projects, kept but labelled, with one exit credential (PSPDFKit,
   "exited 2021").
6. A contribution graph image, a four-bullet **What I'm Doing** section (all about output:
   "Rapid prototyping - Full apps in days, not months"), and **Latest Blog Posts** between
   `<!-- BLOG-POST-LIST:START -->` markers. **Inference:** the markers mean an automated feed
   fills this section.
7. **Connect** badges, then **Recognition** ("67k+ GitHub stars across personal projects;
   428k+ across OpenClaw projects"), **Media** (a TED 2026 talk, a WIRED article), and a
   collapsed `<details>` block of **Random Facts**.

### The rule behind it: `VISION.md`

`gh api repos/steipete/steipete/contents` lists `README.md`, `VISION.md` and `.gitignore`.
`VISION.md` is the most copyable thing on the account:

> This repository is the public GitHub profile for Peter Steinberger. The README should stay
> a concise, current map of who Peter is, what he is building, and where people can find the
> canonical projects.
>
> - Prefer canonical project domains or current repository URLs over redirects and former names.
> - Preserve Peter's direct voice and editorial control; additions should improve the profile,
>   not merely make it busier.
> - Use coarse, verifiable thresholds for volatile numbers such as stars so they remain truthful
>   between refreshes.
>
> Non-goals: An automated or exhaustive inventory of every repository. Vanity metrics that
> sacrifice accuracy, privacy, or clarity.

The commit log follows the rule. The latest commit is "docs: refresh README star counts to
current whole-thousand floors (#21)… Counts verified against GitHub on 2026-08-28"
(`gh api repos/steipete/steipete/commits`).

### Pins

From the GraphQL `pinnedItems` query, there are six pins. Five are products: CodexBar (21,917★,
`codex.bar`), Peekaboo (5,204★, `peekaboo.boo`), mcporter (5,028★, `mcporter.sh`), oracle
(4,028★, `askoracle.sh`) and Trimmy (744★, `trimmy.app`). The sixth is `steipete/speaking`
(233★), a list of talks. Every pin has a `homepageUrl` and between two and eight topics.
Two of the six (Peekaboo and mcporter) belong to the `openclaw` org, which shows that pins
can point at org repos the user owns or contributes to.

### Repo descriptions, homepages, topics

From `gh api "users/steipete/repos?sort=pushed&per_page=30"`: the descriptions are one
sentence, state a user benefit, and often carry a joke that also names the job:

- CodexBar: "Show usage stats for OpenAI Codex and Claude Code, without having to login."
- summarize: "Point at any URL/YouTube/Podcast or file. Get the gist. CLI and Chrome Extension."
- tokentally: "One tiny lib for LLM token + cost math"
- gifgrep: "Grep the GIF. Stick the landing."

Of his own (non-fork) repos in that list, almost every one has a `homepage`: a product domain,
or `steipete.me` as a fallback for utility repos such as `homebrew-tap` and `agent-scripts`.
Most have topics. The forks (`bun`, `libuv`, `vitest`, `WebKit`) keep upstream descriptions
and are not pinned or listed in the README.

### Repo READMEs read as product pages

The tops of the CodexBar, oracle and Trimmy READMEs (`gh api repos/steipete/<repo>/readme`)
all follow the same shape:

1. `# Name <emoji> — <tagline>` ("Trimmy ✂️ — Paste once, run once.")
2. A badge row covering distribution, not decoration: latest release, CI, platform, Homebrew,
   npm, licence.
3. One paragraph saying what it is and who it is for. From oracle: "Oracle is a CLI and MCP
   server that bundles a prompt with the files you select… It is for developers and coding
   agents that need a second-model review grounded in the actual project."
4. A screenshot or a runnable snippet with its output.
5. `## Install` (one command), then `## Quick start` (three numbered steps and the expected
   output).

CodexBar also has a `## Why` section of four bolded benefits. None of the three opens with
motivation, history or what the author learned.

### Why it works

**Inference** throughout this section. It is a reading of the page, not a fact the API returns.

- **One question, answered at every depth.** Bio, README, pins, descriptions and repo READMEs
  all answer "what does this person ship, and can I use it?". A visitor can stop at any layer
  and still have the answer.
- **Everything links outward to a finished thing.** Homepages and domains make each project
  feel like a product, not a folder.
- **The numbers are coarse and honest.** "20k+" survives a refresh, and the rule is written
  down.
- **Old work is labelled, not deleted.** "Legacy Work" keeps the history without letting it
  set the tone.
- **Personality is rationed.** It lives in the jokes in descriptions and in a collapsed
  `<details>` block, not in the headline.

---

## 2. What the MorenaDlamini profile currently shows

### Sidebar fields

From `gh api users/MorenaDlamini`:

| Field | Value | Reads as |
|---|---|---|
| `bio` | "I build the software a [employer industry] manufacturer runs on: offline-first apps from test bench to field, RFID/NFC traceability, ERP pipelines, live dashboards." | Built work, which is good, but it identifies the employer's industry |
| `company` | `[employer]` | **Names the employer** |
| `blog` | `https://github.com/MorenaDlamini/worked-examples/blob/master/CURRICULUM.md` | **The strongest "where I am" signal on the page.** The only website link is a study plan |
| `location` | `Johannesburg, South Africa` | Fine |
| `hireable` | `true` | Fine. Documented as "The new hiring availability of the user" ([REST: update the authenticated user](https://docs.github.com/en/rest/users/users#update-the-authenticated-user)) |
| `followers` / `public_repos` | 0 / 5 | Earned over time |

Social accounts: LinkedIn only (`gh api users/MorenaDlamini/social_accounts`).

### Pins

From the GraphQL `pinnedItems` query, two pins, both from 2026-03-09 and both with 0 stars:

- `Codecast`: "Podcast player SPA — React, TypeScript, Zustand. Deployed.", homepage
  `codecastpod.netlify.app`
- `rentscape`: "Property listing app in TypeScript with hand-rolled MVC — no framework.", no
  homepage

`worked-examples` is **not pinned**, even though it is the repo the user wants as the only pin.
Pins can be changed only in the web UI, through "Customize your pins" (up to six repositories
and gists combined; [Pinning items to your profile](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/pinning-items-to-your-profile)).

### Public repos

From `gh api "users/MorenaDlamini/repos?sort=pushed"`: `worked-examples`, `MorenaDlamini`
(description "Profile README"), `groundbreak` (public, **no description, no topics, no
homepage**), `rentscape` and `Codecast`. `worked-examples` has topics
(`data-engineering, pytest, python, security`) but no homepage.

### The profile README (`C:\Stuff\Github Readme\README.md`, identical to the remote)

The top half is already a landing page: a "Shipped | For whom | What it does" table of five
real systems. That is the right instinct, and it is closer to steipete than the user may think.
The parts that read as status or position rather than built work:

- "Software engineer at **[employer]**, Johannesburg — a **[employer industry]
  manufacturer**." This names the employer.
- "Internal platform with single sign-on ***(in progress)***". A progress marker in the headline
  table.
- "None of it is at scale, and I say so." A defensive disclaimer in the pitch. It belongs in
  `NON-CLAIMS.md`, which already exists for exactly this.
- "### The other half — worked-examples. Each topic **I study** becomes a module…". This frames
  the only public artifact as study.
- "`CURRICULUM.md` — **the phases, each with the exit test that ends it**." A plan, linked from
  the landing page.
- "### **What I'm working toward.** The requirements that sit under every senior systems role
  I have read: …" This is the clearest "where I am" section. It lists requirements the author
  has not yet met, on the page meant to show what they have.

The git log (`git -C "C:\Stuff\Github Readme" log`) shows nine rewrites between 2026-09-14 and
2026-09-21, each changing the audience or angle: ".NET and fintech roles", "bank hiring
managers with build placeholders", "Point the profile at data infrastructure, APIs and
security", "Lead the profile with shipped work". **Inference:** a page that is repositioned
every few days keeps reading as a status report, because it keeps reporting where the author
is aiming this week. steipete's `VISION.md` exists to stop exactly this.

### The `worked-examples` README (`README.md` in this repo, same as remote apart from line endings)

This is where the status belongs, and most of it is fine *there*. Two lines leak status onto
the page a visitor lands on first:

- "## Progress" shows one row: "`m001_getting_started_log_parsing` | getting-started | log
  parsing | done".
- "A green CI badge over sixty modules is a different claim from a green commit graph." Next
  to a progress table with one row, this reads as a promise that has not been kept yet.

The repo description ("A lesson, a set of failing tests, my solutions and a spoken answer, for
each topic I study…") is precise but inward-facing. It describes the author's process rather
than what a reader gets.

---

## 3. The gap: copyable now vs earned

| steipete has | Copyable now? | The MorenaDlamini equivalent |
|---|---|---|
| Bio in his own voice about what he does now | **Now** | One line: pillars as outputs, no employer, no plan |
| Website field → his own writing and products | **Now** | Point at the profile README or LinkedIn, not `CURRICULUM.md` |
| `VISION.md` rule for the profile repo | **Now** | Same file, a few lines: what the README is for, and its non-goals |
| README structure: Start here → groups → legacy → connect | **Now**, at a smaller scale | Start here (one item today), What I build, Earlier work, Contact |
| One-line benefit per item | **Now** | Rewrite every repo description as a product line |
| Homepage on every repo | **Now**, partly | Codecast has one. `worked-examples` can point at its rendered CI page or a docs page. Future PyPI packages point at PyPI or docs |
| Topics on every repo | **Now** | Add to `rentscape`, `Codecast` and future repos; `groundbreak` is deferred |
| Product-page repo READMEs (tagline, badges, install, quick start) | **Now for new repos**; it is a template | `parity` and `municipal-money` start life in this shape |
| Old work labelled "Legacy" | **Now** | Codecast and rentscape move to "Earlier work", unpinned |
| Pins = products with homepages | Structure now, content **earned** | `worked-examples` alone now; `parity`, `municipal-money`, `platform`, `product` as they ship |
| Coarse star counts ("20k+") | **Earned** | Show nothing until a number is worth showing. A PyPI download count is the first one likely to become meaningful (**Inference**) |
| 52.9k followers, 218 repos, org of his own | **Earned** | Follows from things other people install |
| Product vanity domains | Optional, costs money | Not needed. PyPI and a docs page are the credible homepages for a Python package |
| Blog feed, talks, TED, WIRED | **Earned** | `decisions/` write-ups are the seed; a blog is a later choice |
| Naming his employer | **Not copyable**, by the user's own rule | Describe the work, never the company |

The honest summary: about half of what makes steipete's page work costs nothing but editing.
The other half is about fifteen years of shipped products. The ladder below is how this
account climbs the second half.

---

## 4. A staged path

Ordered. No dates. Each stage is complete in itself and leaves the page better than it found it.

### Stage 1: remove the employer and the plan from the sidebar (web UI and settings only)

1. **Company field:** clear `[employer]`. It can be changed in Settings → Public
   profile, or through `PATCH /user` with `company` ([REST docs](https://docs.github.com/en/rest/users/users#update-the-authenticated-user)).
2. **Bio** (160-character limit, per [Personalizing your profile](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/personalizing-your-profile)).
   Two drafts, both counted:
   - "Software engineer in Johannesburg. Data pipelines, C# and React products, applied AI on model APIs, and auth that holds up under POPIA." (135 characters)
   - "Software engineer, Johannesburg. I build data pipelines and the products on top of them: Python and Spark, C# and React, model APIs, auth done properly." (152 characters)

   Both drop "[employer industry] manufacturer", which identifies the employer's industry and so
   references the employer.
3. **Website field:** replace the `CURRICULUM.md` link. Options, best first: leave it empty
   (the README is the landing page); point it at LinkedIn (already a social account, so this
   duplicates it); later, point it at `product`'s live URL once it exists. Do not point it at
   anything that describes a plan.
4. **Pins:** unpin `Codecast` and `rentscape`, and pin `worked-examples`, through Profile →
   "Customize your pins" → "Save pins". There is no API for this.
5. **Leave `hireable` on.** It is a quiet signal that does not read as status.
6. **Contribution settings.** "Private contributions" shows "anonymized activity from private
   and internal repositories" ([docs](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/managing-contribution-settings-on-your-profile/showing-your-private-contributions-and-achievements-on-your-profile)).
   The API reports 92 commit contributions in the last year and `restrictedContributionsCount`
   0 (GraphQL `contributionsCollection`). **Unverified** whether any day-job work happens in
   private GitHub repos under this account. If it does, turning the toggle on fills the graph
   without exposing names. That is the user's call, and whether it is allowed under the
   employer's policy is their call too.

### Stage 2: add a `VISION.md` to the profile repo, then rewrite the README against it

Proposed `VISION.md` (adapted from steipete's, not copied):

```markdown
# Vision

This repository is the public GitHub profile for Morena Dlamini. The README is a short,
current map of what Morena builds and where to find it. It is not a progress report.

## Rules
- Every item links to something that exists and runs. Nothing planned, nothing "in progress".
- One line per item, stated as what it does for the reader.
- No employer is named or identifiable. Day-job work is described by what it does.
- Numbers only when they are verifiable, stated as coarse floors ("1k+"), refreshed by hand.
- Disclaimers and limits live in worked-examples/NON-CLAIMS.md, not here.

## Non-goals
- A study plan, a curriculum, or a list of requirements not yet met.
- Repositioning the page for each new audience.
- Badges, counters or widgets that do not link to a real thing.
```

Proposed README for **now** (only `worked-examples` exists publicly):

```markdown
# Morena Dlamini

Software engineer in Johannesburg. I build data pipelines and the products that sit on
them — Python and Spark underneath, C# and React on top, model APIs where they earn their
place, and authentication done properly throughout.

## Start here

- **[worked-examples](https://github.com/MorenaDlamini/worked-examples)** — a lesson, failing
  tests, a solution and a spoken answer per topic; CI grades every module on every push.

## What I ship at work

Internal software used on the factory floor and in the field, for people who are not
developers:

- **Offline-first desktop and tablet apps** that keep working without signal and reconcile
  when it returns
- **Scan-based production traceability** — RFID, NFC and barcode at every step
- **ERP-to-cloud integration** so operational data stops being re-keyed
- **Live operations dashboards**
- **Single sign-on** across the company's internal applications

The code is private. The design decisions are not — ask me about any of them.

## Earlier work

- [Codecast](https://codecastpod.netlify.app/) — podcast player SPA, React and TypeScript
- [rentscape](https://github.com/MorenaDlamini/rentscape) — property listings with a hand-rolled MVC, no framework

---

Johannesburg, UTC+2 · [dlaminimorena@gmail.com](mailto:dlaminimorena@gmail.com) · [LinkedIn](https://www.linkedin.com/in/morena-dlamini-b33081169/)
```

What changed from the current README, and why:

- **Employer removed.** The work is described by what it does and who uses it. "Factory floor
  and in the field" is generic enough that it does not identify an employer (**Inference**; see
  open questions).
- **"(in progress)" removed.** SSO is listed as shipped. If it is not yet in production, drop
  the bullet until it is, rather than marking it.
- **"None of it is at scale, and I say so"** moves to `NON-CLAIMS.md`.
- **"What that work taught me"** (four good one-liners) moves to `worked-examples/decisions/`
  or becomes the opening of one module each. Those lines are lessons, and lessons live in the
  lessons repo. **Alternative:** keep them as a collapsed `<details>` block, which is how
  steipete keeps his personal colour out of the headline.
- **"What I'm working toward"** leaves the profile entirely. It already lives in
  `CURRICULUM.md`, which is where a reader who wants the plan will find it.
- **`CONTRIBUTING.md` / `NON-CLAIMS.md` / `CURRICULUM.md` links** move off the profile. They
  are one click away inside `worked-examples`.
- **No tech-badge row.** steipete's badges sit on top of 80 shipped projects. On a page with one
  public artifact, a row of logos would read as a claim, not as evidence (**Inference**). Add
  one when the pinned repos show those languages.

### Stage 3: repo hygiene (descriptions, homepages, topics)

- **`worked-examples` description**, rewritten as what a reader gets: "Worked lessons in data,
  full-stack and security — each with failing tests, a solution and a spoken answer. CI grades
  every module." Set a homepage, for example the Actions page that the badge already links to.
- **`worked-examples` README:** keep the progress table, but move `## Progress` below
  `## Challenges` and `## Standards`, so the first screen describes the system rather than the
  current count. Change "A green CI badge over sixty modules" to wording that does not imply a
  target, for example "A green CI badge over every module…".
- **`rentscape`:** add a homepage if it can be deployed, or leave it as it is. It is labelled
  earlier work now, so the bar is lower.
- **`MorenaDlamini` (profile repo):** description "Profile README" is fine. Add `VISION.md`.
- **`groundbreak`:** public, with no description, and **deferred by the user**. Do not touch
  it. Its safety items (no local git identity, corrupt `.gitignore`) come first, whenever it
  comes back. Note only that a blank public repo shows up in the repository list and the
  contribution graph.
- **Never** create a repo called `learn-in-public` under this account. It would break the 301
  redirect to `worked-examples`.

### Stage 4: what each future ship adds to the page

Each ship adds one **Start here** line, one pin and one homepage, in that order. The template
for every new repo README is steipete's: `# name — tagline`, a badge row (CI, PyPI version,
Python versions, licence), one paragraph on what it is and who it is for, `## Install`
(`pip install …`), `## Quick start` (three steps and the expected output), and `## Why`.

| Ship | Start-here line (draft) | Pin | Homepage | What it proves on the page |
|---|---|---|---|---|
| `parity` on PyPI | "**parity** — prove a replatformed pipeline returns the same rows as the one it replaced" | yes | PyPI page or docs | Data (deepest pillar); something a stranger can install |
| `platform` | "**platform** — a T-SQL warehouse replatformed to PySpark and Delta, with CDC ingestion through Redpanda" | yes | docs or architecture page | Data at system scale |
| `municipal-money` on PyPI | "**municipal-money** — a typed Python client for National Treasury's Municipal Money API" | yes | PyPI page or docs | API design; a South African public-data niche few others fill (**Inference**) |
| `product` | "**product** — explore any South African municipality's finances; OIDC login, and an assistant graded by evals in CI" | yes | **live URL**, which also becomes the profile website | Full-stack, applied AI and security at once |

When `product` is live, the website field points at it, and the page's shape matches
steipete's at a smaller scale: bio → live product → four pinned packages and systems → one line
about day-job work → earlier work → contact. At that point, `worked-examples` moves from
"Start here" into a supporting line such as "How I learn: worked-examples". It stays pinned
only if a slot is free.

### The earned ladder, stated plainly

**Inference.** This is the order in which signals usually accrue, not a measured fact.
PyPI downloads (from people who are not the author) → the first issue or PR from a stranger →
stars on the package repos → followers → being linked from someone else's README or post → a
talk or write-up. steipete's "Recognition" and "Media" sections sit at the top of this ladder.
The profile should never show a rung before it is reached. That is the `VISION.md` rule on
numbers.

---

## 5. Open questions only the user can answer

1. **How much of the day-job work may be described at all?** The draft names only generic
   capabilities. Whether even "factory floor and in the field" plus "RFID/NFC traceability" is
   too identifying depends on the employer's policy and the user's own comfort. Neither of
   those can be checked from here.
2. **Is single sign-on in production yet?** If not, the bullet comes off rather than carrying
   "(in progress)".
3. **What goes in the website field**: empty, LinkedIn, or (later) `product`'s live URL?
4. **Are Codecast and rentscape worth keeping as "Earlier work"**, or should they drop off the
   README entirely and stay only in the repo list?
5. **Do the four "What that work taught me" lines move to `decisions/`**, into a collapsed
   `<details>` block, or out altogether?
6. **Private contributions toggle:** does any day-job work happen in private repos under this
   account, and may it show up as anonymized activity?
7. **Final names** for `platform` and `product` (working names only). The Start-here lines and
   pins wait on them.
8. **`groundbreak`**, when it comes back: it stays public, gets described, or goes private.
   Deferred by the user; the two safety items come first.

---

## Sources

Every source is inline above. The load-bearing ones, grouped:

- **GitHub REST API, read 2026-09-26:** `users/steipete`, `users/MorenaDlamini`,
  `users/{u}/social_accounts`, `repos/steipete/steipete/readme`,
  `repos/steipete/steipete/contents` and `.../contents/VISION.md`,
  `repos/steipete/steipete/commits`, `users/{u}/repos?sort=pushed&per_page=30`,
  `repos/steipete/{CodexBar,oracle,Trimmy}/readme`, `repos/MorenaDlamini/worked-examples`,
  `repos/MorenaDlamini/groundbreak`, `repos/MorenaDlamini/MorenaDlamini/readme`.
- **GitHub GraphQL API:** `user(login){ pinnedItems(first:6) … }` for both users;
  `user(login:"MorenaDlamini"){ contributionsCollection{ totalCommitContributions restrictedContributionsCount } }`.
- **Rendered pages:** `https://github.com/steipete` (sidebar, status line, pins) and
  `https://steipete.me` (homepage tagline).
- **docs.github.com:**
  [Managing your profile README](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme)
  (display conditions: a public repo named after the username with a non-empty root
  `README.md`),
  [Pinning items to your profile](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/pinning-items-to-your-profile),
  [Personalizing your profile](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/personalizing-your-profile)
  (bio limit of 160 characters, status, up to four social accounts),
  [Showing your private contributions and achievements](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/managing-contribution-settings-on-your-profile/showing-your-private-contributions-and-achievements-on-your-profile),
  [REST: update the authenticated user](https://docs.github.com/en/rest/users/users#update-the-authenticated-user)
  (`company`, `blog`, `bio`, `hireable`).
- **Local files:** `C:\Stuff\Github Readme\README.md` and its `git log`; this repo's `README.md`.
