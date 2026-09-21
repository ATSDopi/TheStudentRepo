# AGENTS.md — Student Offers repo

## What this is

A community-maintained, **international** list of student discounts, credits, freebies and free tools. Documentation-only repo — no code, no build.

## Structure

- `README.md` — index: verification guide, Top 10, category table, pitfalls, action plan
- `docs/` — one file per category:
  - `ai.md` — AI tools & assistants (student offers + free tiers)
  - `github-pack.md` — the full GitHub Student Developer Pack (70+ offers)
  - `dev.md` — cloud credits + permanent free tiers for devs
  - `design.md` — design, 3D, gamedev software
  - `learning.md` — free courses (with free-cert flags) + legal textbooks/academic tools
  - `career.md` — CV builders, interview prep, paid fellowships, job boards
  - `productivity.md` — study stack, open-source alternatives, useful websites
  - `entertainment.md` — streaming student plans, free games
  - `money.md` — banking, budgeting, money traps
  - `scholarships.md` — international scholarships + databases
  - `countries.md` — country-specific perks (🇫🇷 🇺🇸 🇬🇧 🇩🇪 🇨🇦 🇪🇺 + stub)
- `CONTRIBUTING.md` — entry format and rules
- `LICENSE` — MIT
- `.github/` — issue templates (expired offer, new offer, new resource) + weekly lychee link-check workflow
- `_config.yml` — GitHub Pages (jekyll-theme-minimal)

## Conventions

- Language: **English** (international audience)
- Every offer = a table row: `| **Name** | What you get | Verify via | [link](...) |`
- Verification column is **mandatory** — the repo's differentiator
- Official links only — never referral/affiliate links
- ⭐ = best value/effort ratio
- Legal sources only — no piracy/shadow libraries, ever
- Country sections use `<details>` blocks; new countries copy an existing structure
- No row numbering — insert alphabetically or by value within a table

## Hard rules

- **No personal information.** This repo was anonymized — never add names, school names, personal emails or account details.
- **No invented offers.** Only add offers verifiable on an official page. If unsure, flag it in the PR.

## CI / infra

- `.github/workflows/link-check.yml` — weekly lychee run over all `*.md`, uploads a report, opens an issue on scheduled failures. `fail: false` until flaky links are triaged; flip to `true` later.
- GitHub Pages: Settings → Pages → Deploy from branch `main` (root). `_config.yml` is already set.

## Publishing metadata (for the GitHub repo settings)

- **About**: `🎓 The ultimate student resource list — every student discount, credit, freebie and free tool, sorted by category and country, with the verification method for each offer.`
- **Topics**: `student` `discounts` `freebies` `awesome-list` `education` `student-developer-pack` `free-resources` `student-discount`

## Roadmap / ideas

- Expand country sections (most are 🚧) — biggest contribution lever
- Once coverage is broad, format could be adapted for the `awesome` list index (sindresorhus/awesome requirements)
- Flip lychee `fail: false` → `true` once the link backlog is clean

## When the list changes

- Update the `checked` badge date in the README header
- Keep the offers-count badge roughly in sync
