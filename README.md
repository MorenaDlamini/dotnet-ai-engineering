# dotnet-ai-engineering

[![modules](https://github.com/MorenaDlamini/dotnet-ai-engineering/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/MorenaDlamini/dotnet-ai-engineering/actions/workflows/ci.yml)

How I engineer C#/.NET and AI, in the open. It holds the specs, decision records, tests that
name their risk, and postmortems behind the product I'm building,
[randmatch](https://github.com/MorenaDlamini/randmatch-recon). Every claim links to evidence.

Each topic I go deep on becomes a **module**: a written explanation, a set of failing tests, my
solutions, and an honest note about what it doesn't cover yet. CI runs every module's tests on
every push. A module isn't finished because I say so. It's finished when the tests pass and the
checklist in `CONTRIBUTING.md` is met.

## Why it's built this way

- **Evidence over claims.** A green CI badge over every module says something different from a
  green commit graph. A progress item counts only when it links to a merged PR, a green run, or a
  certificate.
- **Produce, don't consume.** Explaining a topic well enough to write its exercises is how
  knowledge sticks, and the result is something a reviewer can actually check.
- **AI is visible, not hidden.** `AI_USAGE.md` sets the rules. Each PR records what an assistant
  proposed, what I kept and rejected, and which tests caught what.

## Tiers

Borrowed from how good course catalogues stage material, renamed for honesty about what
each level actually proves.

| Tier | Question it answers | Proof required |
|---|---|---|
| `getting-started` | Can I use this at all? | 3+ exercises passing |
| `hands-on` | Can I do it under pressure, without notes? | 6+ exercises, one timed |
| `deep-dive` | Do I know how it works underneath? | An implementation from scratch, or a benchmark |
| `build-it` | Can I ship one end to end? | A working thing with a README and failure handling |

A topic can have several modules at rising tiers. `deep-dive` is where most of the value is,
and where almost everybody stops short.

## Layout

```
modules/NNN-tier-topic/
  README.md        the lesson, written by me, for someone who does not know this yet
  NOTES.md         my working understanding, updated over time
  INTERVIEW.md     20-second and 90-second spoken answers
  exercises/       stubs that fail
  solutions/       my solutions
  tests/           pytest that verifies both
challenges/        the build ladders, gated stage by stage (phase-00 is phase 1.0)
decisions/         one record per real decision, written at the time
designs/           one page before any service starts
scenarios/         ambiguous tickets, practised the way they actually arrive
horizon/           quarterly review: what is changing in .NET and AI
research/          the postings and the evidence the curriculum answers to
templates/         module scaffold
tools/             new_module.py, status.py, challenges.py
.local/            private, gitignored: weak attempts, half-formed thinking
```

## Commands

```bash
make new t=hands-on topic=window-functions   # scaffold a module
make test                                    # run every module's tests
make test m=012                              # run one module
make status                                  # regenerate the progress table below
make challenge p=0 s=01                      # run one challenge stage
make challenges                              # run every started stage
make ladder                                  # regenerate the ladder table
```

## Progress

<!-- STATUS:START -->
| Module | Tier | Topic | State |
|---|---|---|---|
| `m001_getting_started_log_parsing` | getting-started | log parsing | done |
<!-- STATUS:END -->

## Curriculum

`CURRICULUM.md` is the plan: C#/.NET full stack for fintech products, AI-ready. It runs in four
levels, **1 · Ship, 2 · Own, 3 · Scale and 4 · Lead**. Each phase ends in a capstone, and each
level ends in a gate passed cold.

Every capstone adds to one product, **randmatch**: payout reconciliation for South African
merchants who take payments through several providers.
[`randmatch-recon`](https://github.com/MorenaDlamini/randmatch-recon) is the product,
[`randmatch-ledger`](https://github.com/MorenaDlamini/randmatch-ledger) its clearing ledger, and
[`randmatch-sim`](https://github.com/MorenaDlamini/randmatch-sim) the simulator whose planted
breaks are the answer key.

## Progress through the levels

<!-- PROGRESS:START -->
**Now:** Level 1 · Ship · 1.0 — Linux, Git, SDLC and Scrum

| Level | Progress | Phases |
|---|---|---|
| Level 1 · Ship | `░░░░░░░░░░░░` 0/75 | 0/6 |
| Level 2 · Own | `░░░░░░░░░░░░` 0/74 | 0/6 |
| Level 3 · Scale | `░░░░░░░░░░░░` 0/64 | 0/5 |
| Level 4 · Lead | `░░░░░░░░░░░░` 0/22 | 0/4 |

Every item links to its evidence in [PROGRESS.md](PROGRESS.md), and on the [dashboard](https://morenadlamini.github.io/dotnet-ai-engineering/).
<!-- PROGRESS:END -->

## Challenges

Modules teach a topic. `challenges/` builds each phase's project in numbered stages, each gated
by an acceptance test, in the shape CodeCrafters uses. A stage is done when its test passes on
a push, so finishing one always leaves a commit behind. Stages nobody has started are skipped
rather than failed, which is why the badge above still means something.

Acceptance tests are Python and black-box wherever the thing being built is not: shell stages
are graded through `tools/shelltest.py`, and services are graded over HTTP against a running
container. See `challenges/README.md` for the rules and the current ladder.

## Standards

See `CONTRIBUTING.md` for the bar every module must clear, `AI_USAGE.md` for the rules I
hold myself to when using an assistant, and `NON-CLAIMS.md` for what this repository does
not prove.
