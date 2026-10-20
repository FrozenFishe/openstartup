# Startup and founder visas

One file per region, `research/visas/<region>.json`, holding a JSON array. One item per visa route a foreign founder can use to build a startup in that country:

```json
{
  "country": "Netherlands",                     // exactly as in research/batches.json
  "name": "Startup visa (residence permit for start-ups)",
  "type": "startup_visa | entrepreneur_visa | talent_visa | investor_visa | digital_nomad",
  "status": "open | paused | closed | pilot",
  "for": "innovative early-stage founders with a recognised facilitator",
  "endorsement": "approved facilitator (mentor) | government committee | accelerator or VC | none",
  "min_investment": "none | €4,500 living funds | US$100k | …",
  "duration": "1 year",
  "renewal": "switch to self-employed permit after 1 year",
  "pr_path": "yes, after 5 years | no | unclear",
  "family": "yes | no | unclear",
  "processing": "up to 90 days | unknown",
  "gov_fee": "€390 | unknown",
  "url": "https://ind.nl/…",                    // the government's own page for this route
  "verified": "2026-10-20",
  "notes": "short caveats, e.g. 'DHS proposed to rescind in 2025'"
}
```

## Rules

- **Today is 20 October 2026.** Record the current status. A paused or closed route stays in the list with that status and the date it stopped, since founders still look for it.
- Every item needs the government's own page (immigration ministry, startup agency, or official programme site) that you opened. No guessed URLs or figures; use `unknown` instead.
- `type` meanings:
  - `startup_visa`: a dedicated route for founders of innovative startups, usually with an endorsement (e.g. UK Innovator Founder, Netherlands, Estonia, Ireland STEP, Japan, Chile Tech Visa, Thailand SMART-S).
  - `entrepreneur_visa`: a general self-employment or business-owner route usable by founders (e.g. Germany §21, Austria Red-White-Red for startup founders).
  - `talent_visa`: a talent or golden route that founders commonly use (e.g. UK Global Talent, Taiwan Gold Card, UAE Golden Visa for entrepreneurs, Hong Kong Top Talent Pass).
  - `investor_visa`: needs a stated investment (e.g. US E-2, Australia's investor streams).
  - `digital_nomad`: remote-work residence that allows building a company from there; include only where founders can run their own company on it.
- Keep strings short and the JSON valid (no comments, no trailing commas).
