# Contributing

Thanks for helping keep this the best student-offers list on GitHub. Offers expire fast — community updates are what keeps it accurate.

## Ways to contribute

- **Add a new offer** → pull request
- **Report an expired/changed offer** → issue with the *Expired offer* template
- **Suggest a free resource** (course, tool, site) → issue with the *New resource* template
- **Add or expand a country section** → pull request
- **Fix a link or price** → pull request

## Offer format

Every offer must be a table row with **all fields**:

```markdown
| **Offer name** | What you get (duration, discount, value) | Verification method | [official link](https://...) |
```

Rules:

- **Link to the official page only** — no referral/affiliate links, no third-party resellers.
- **Always state the verification method**: `School email`, `SheerID`, `UNiDAYS`, `Student Beans`, `GitHub Pack`, `ISIC`, `Student card`, `ID (age)`, `Application`, or `—` if no status is needed.
- **Prefer durations/values over vague text**: "12 months free (~$240)" not "great deal".
- Mark top value/effort offers with ⭐.

## Where an entry goes

| Entry type | File |
|---|---|
| AI tools & assistants | `docs/ai.md` |
| Anything unlocked by GitHub Education | `docs/github-pack.md` |
| Cloud, hosting, dev free tiers | `docs/dev.md` |
| Design, 3D, video, gamedev | `docs/design.md` |
| Courses, textbooks, academic tools | `docs/learning.md` |
| CVs, internships, interview prep, fellowships | `docs/career.md` |
| Study/productivity tools, useful websites, OSS alternatives | `docs/productivity.md` |
| Streaming, press, games | `docs/entertainment.md` |
| Banking, budgeting, money | `docs/money.md` |
| Scholarships & grants | `docs/scholarships.md` |
| Country-specific offers | `docs/countries.md` |
| Expired / restricted / misleading | `README.md` → ⚠️ Pitfalls |

## Adding a new country

1. Copy an existing country's structure in `docs/countries.md` (`<details>` block + table).
2. Include local specifics: transport passes, banking, government aid, local streaming/retail.
3. Mark it 🚧 if it's a work in progress.

## Before submitting

- [ ] Link points to the **official** offer page
- [ ] Verification method is filled in
- [ ] Terms verified within the last 3 months (note the date in your PR description)
- [ ] No personal information, school names, or referral links
- [ ] Legal sources only — no piracy, shadow libraries or grey-market sellers

## What NOT to add

- Referral/affiliate links
- Offers requiring paid memberships to access (unless the membership itself is the offer)
- Anything that can't be verified on an official page
- Pirated content (LibGen, Z-lib, cracked software) — this repo stays 100% legal
- Personally identifiable information — this repo is anonymous by design
