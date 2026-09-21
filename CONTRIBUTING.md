# Contributing

Thanks for helping keep this the best student-offers list on GitHub. Offers expire fast — community updates are what keeps it accurate.

## Ways to contribute

- **Add a new offer** → pull request
- **Report an expired/changed offer** → issue with the *Expired offer* template
- **Add or expand a country section** → pull request
- **Fix a link or price** → pull request

## Offer format

Every offer must be a table row with **all five fields**:

```markdown
| **Offer name** | What you get (duration, discount, value) | Verification method | [official link](https://...) |
```

Rules:

- **Link to the official page only** — no referral/affiliate links, no third-party resellers.
- **Always state the verification method**: `School email`, `SheerID`, `UNiDAYS`, `Student Beans`, `GitHub Pack`, `ISIC`, `Student card`, `ID (age)`, `Application`, or `—` if no status is needed.
- **Prefer durations/values over vague text**: "12 months free (~$240)" not "great deal".
- Mark top value/effort offers with ⭐.
- If an offer is **not** for students (free for everyone), it goes in the *Free for everyone* section.

## Where an offer goes

| Offer type | Section |
|---|---|
| Works in most countries | `🌍 International offers` |
| Country-specific (transport, banking, gov aid, local retail) | `🗺️ Offers by country → your country` |
| No student status needed | `🆓 Free for everyone` |
| Expired / restricted / misleading | `⚠️ Pitfalls & deadlines` |

## Adding a new country

1. Copy an existing country's structure (`<details>` block + table).
2. Include local specifics: transport passes, banking, government aid, local streaming/retail.
3. Add the country to the `🗺️ Offers by country` index in the README.
4. Mark it 🚧 if it's a work in progress.

## Before submitting

- [ ] Link points to the **official** offer page
- [ ] Verification method is filled in
- [ ] Terms verified within the last 3 months (note the date in your PR description)
- [ ] No personal information, school names, or referral links

## What NOT to add

- Referral/affiliate links
- Offers requiring paid memberships to access (unless the membership itself is the offer)
- Anything that can't be verified on an official page
- Personally identifiable information — this repo is anonymous by design
