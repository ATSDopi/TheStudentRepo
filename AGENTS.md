# AGENTS.md — Student Offers repo

## What this is

A community-maintained, **international** list of student discounts, credits and freebies. Single-file documentation repo — no code, no build.

## Files

- `README.md` — the entire list. Structure:
  - `🔑 Step 0` — verification methods (SheerID, UNiDAYS, Student Beans, GitHub Education, ISIC…)
  - `⭐ Top 10`
  - `🌍 International offers` — works in most countries (incl. the full GitHub Student Developer Pack tables)
  - `🗺️ Offers by country` — local perks per country (🇫🇷 🇺🇸 🇬🇧 🇩🇪 🇨🇦 🇪🇺 + stub for others)
  - `🆓 Free for everyone` — no student status needed
  - `⚠️ Pitfalls & deadlines`, `🚀 Action plan`
- `CONTRIBUTING.md` — offer format and rules
- `LICENSE` — MIT
- `.github/ISSUE_TEMPLATE/` — expired-offer and new-offer templates

## Conventions

- Language: **English** (international audience)
- Every offer = a table row: `| **Name** | What you get | Verify via | [link](...) |`
- Verification column is **mandatory** — that's the repo's differentiator
- Official links only — never referral/affiliate links
- ⭐ = best value/effort ratio
- Country sections use `<details>` blocks; new countries copy an existing structure

## Hard rules

- **No personal information.** This repo was anonymized — never add names, school names, personal emails or account details.
- **No invented offers.** Only add offers verifiable on an official page. If unsure, flag it in the PR.
- Don't renumber manually — rows are not numbered; insert alphabetically or by value within a table.

## When the list changes

- Update the `checked` badge date in the README header
- Keep the offers-count badge roughly in sync
