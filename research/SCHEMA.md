# OpenStartup research schema

Output: one JSON file per batch, `research/countries/<batch>.json`, holding a JSON **array** with one object per country, in this shape:

```json
{
  "country": "Estonia",                       // exactly as given in the batch list
  "iso2": "EE",
  "ecosystem_tier": "established",            // nascent | emerging | established | global_hub
  "summary": "1–3 sentences: size of ecosystem, hubs, strengths, notable exits.",
  "startup_visa": "Estonia Startup Visa (Startup Estonia committee approval), https://...  — or 'none'",
  "company_setup": "Typical entity, whether a foreigner can incorporate remotely (e.g. e-Residency), cost/time.",
  "grants": [
    {"name": "", "agency": "", "amount": "€ / US$ range as stated", "amount_usd_max": 50000,
     "eligibility": "short", "deadline": "2026-11-30 | rolling | annual (usually Mar) | closed | unknown",
     "status": "open | upcoming | rolling | closed | unknown", "url": ""}
  ],
  "accelerators": [
    {"name": "", "city": "", "type": "accelerator | incubator | venture_studio | corporate | university | government",
     "investment": "e.g. US$125k for 7% / no equity / grant", "sectors": "generalist | fintech, ...",
     "deadline": "2026-11-14 | rolling | cohort twice yearly (Jan, Jul) | unknown",
     "next_cohort": "2027-01 | unknown", "status": "open | upcoming | rolling | closed | unknown", "url": ""}
  ],
  "vcs": [
    {"name": "", "city": "", "stage": "pre-seed | seed | series A | growth | multi", "check_size": "US$100k–1M | unknown",
     "sectors": "generalist | ...", "type": "vc | cvc | angel_network | government_fund | venture_debt | family_office", "url": ""}
  ],
  "resources": [
    {"name": "", "type": "government_agency | startup_association | coworking_hub | database | community | event | legal_tax | other", "url": "", "note": "short"}
  ],
  "sources": ["https://..."],
  "confidence": "high | medium | low",
  "notes": "Dated caveats, e.g. 'Sanctions: international VC effectively unavailable.'"
}
```

## Rules

- **Today is 20 October 2026.** For each deadline, give the **next** application deadline on or after today if one is published, otherwise the pattern ("rolling", "annual, usually March") or "unknown". Never invent a date. If only a past date is known, write it as `"last: 2026-03-15"` and set `status` to `closed` or `upcoming`.
- **Real, current entities only**, each with its own official URL. Skip anything defunct or not active since 2025. No guessed URLs: if you can't confirm one, leave the entity out.
- **Coverage targets per country** (do as many as you can actually verify):
  - global hubs (US, UK, China, India, etc.): up to 25 VCs, 20 accelerators, 12 grants, 10 resources
  - established: up to 15 VCs, 12 accelerators, 8 grants, 8 resources
  - emerging: 5–10 of each where they exist
  - nascent or fragile states: whatever exists (it's fine to have 0 VCs). Always include the national investment or SME agency, any World Bank or UNDP programs, regional funds that invest there (e.g. Partech Africa, Seedstars), and the diaspora or remote-incorporation route.
- Government grants include national, state or provincial programs, R&D tax credits with cash refunds, innovation agencies (e.g. Innovate UK, Business Finland, BPI, EXIST, SBIR) and soft-loan or equity schemes run by the government.
- Prefer primary sources (agency, fund or program site). Put 2–6 key URLs in `sources`.
- Keep strings short. No markdown in values. Valid JSON only (no comments, no trailing commas).
- `amount_usd_max` is a number (convert at rough Oct 2026 rates) or `null`.
