# How credible engineers show their stack on a GitHub profile

Primary-source research, done on 2026-09-29. It follows on from
`research/2026-09-26-github-profile-landing.md`, whose fintech framing this note replaces with
the settled C#/.NET full-stack, AI-ready target. The question here is narrower: how do respected
.NET, AI and full-stack engineers present their tech stack, and what should this profile copy?

Sources are the GitHub REST and GraphQL APIs, read with `gh api` on 2026-09-29: `users/<u>`,
`repos/<u>/<u>/readme` and `pinnedItems`. Anything inferred rather than read is marked
**Inference**.

## The verdict

**Don't have a stack section. Put the stack in one sentence in the opening. Give a technology
its own link only when a public artifact uses it. No badges, icons or widgets.**

## What the profiles show

### .NET

| Profile | README | How the stack appears | Widgets |
|---|---|---|---|
| stephentoub | none | The pins *are* the stack: dotnet/extensions, modelcontextprotocol/csharp-sdk, microsoft/agent-framework | none |
| davidfowl, jbogard, andrewlock, JeremyLikness | none | Pins, a book or a blog | none |
| jasontaylordev | short | One sentence: "I specialise in building and deploying cloud-based enterprise applications with .NET and Azure." Then a featured-projects table | streak |
| timdeschryver | short | Prose: "focused on **Angular** and **.NET**", backed by pinned NgRx and Angular Testing Library contributions | none |
| martinothamar | medium | Inside project lines, with numbers: "[Mediator] – a fast (close to 0 overhead) sourcegenerator-based mediator…" | stats |
| Aaronontheweb | short | Prose: "I build OSS .NET technologies…" | none |
| lukencode | short | None. SQL Server skill is shown through published SQL Server scripts | none |
| m-jovanovic, iammukeshm, meysamhadeli | long | Template bullets, a badge table, a 14–17 logo devicon wall | stats, streak, view counters |

### AI and full stack

| Profile | README | How the stack and AI work appear |
|---|---|---|
| simonw | yes | No stack. Auto-updated releases, blog and TIL columns |
| karpathy, shadcn, leerob, swyx | minimal or none | The pinned repos are the claim |
| jxnl | yes | "Creator of [Instructor]…" plus a third-party outcome |
| eugeneyan, hamelsmu | yes | Outcomes: "…AI-powered experiences that serve customers at scale", "35+ AI products" |
| t3dotgg | yes | Bold link — one line — star count, per project. No stack section |
| owainlewis (mid-career) | yes | Start here → What I work on (4 plain bullets) → Useful repos → Contact. No badges |
| SteveSandersonMS, luisquintanilla, the SK core team | none | Pins: semantic-kernel, agent-framework, dotnet/extensions, runnable MEAI samples |
| dluc | yes | Named products, then two github-readme-stats cards |
| steipete | yes | A 9-badge row, but every badge maps to a shipped project listed right below it |

## Patterns

1. **At the top end, there is no stack section.** The stack is implied by pinned repos and by one
   noun phrase or sentence.
2. **Where it is stated, it is prose**, and it names two to four things ("Angular and .NET",
   ".NET and Azure").
3. **Every claim links to a repo, a package or a post.** Luke Lowrey's SQL Server skill shows
   through the scripts he published, not through a logo.
4. **AI is framed as artifacts and outcomes, never as interest.**
5. **Private work is stated as a fact, by domain and outcome**, without naming anyone. Jason
   Taylor's sentence about the sectors he builds for is the model.

## What reads as junior, template or hype

- Logo and badge walls, especially ones that include technologies with no public repo behind them.
- github-readme-stats, streak, trophy and visitor-counter widgets. None of the top-tier profiles
  above use them. **Inference:** a streak card also punishes people whose work is in private repos.
- GitHub's default emoji template ("🔭 currently working on / 🌱 currently learning"). These are
  status lines, which the profile's VISION.md bans.
- Bios that stack labels ("Django | Flask | MERN | ML | AI"), "enthusiast", follower-count badges.
- Stats cards that mix private and public counts under one label. steipete's VISION.md: "Do not
  combine public and private-derived values under a misleading label."

## What this means for the MorenaDlamini profile

- **Bio:** B, "C# / .NET full-stack engineer building AI features in .NET, on SQL Server. Learning
  in public." Three named things, in the style of sindresorhus's "Focused on Swift & JavaScript".
- **README opening:** one or two sentences carrying the stack in prose. No separate Stack line
  yet. dotnet-ai-engineering has no public C# artifact so far, so a linked stack line would link
  to nothing (**Inference** from the current repo contents).
- **When artifacts land:** each layer (ASP.NET Core API, SQL Server schema and migrations,
  React portal, Microsoft.Extensions.AI and MCP usage) earns a link to the specific folder or
  commit that uses it. Until then it stays in the sentence.
- **Pins over prose.** A merged PR to dotnet/extensions, modelcontextprotocol/csharp-sdk or
  microsoft/agent-framework would say more than any README line (**Inference**). If one happens,
  it earns a pin.
- **Optional later:** a self-updating feed of commits or releases (simonw, eugeneyan). It shows
  activity without anyone writing a status update.
