# University startup programs

One file per region, `research/universities/<region>.json`, holding a JSON array. Each item is one program (an accelerator, incubator, pre-accelerator, venture fund, fellowship or pitch competition) run by or at a university:

```json
{
  "country": "Australia",                  // exactly as in research/batches.json
  "university": "UNSW Sydney",
  "name": "UNSW Founders 10x Accelerator",
  "kind": "accelerator | pre_accelerator | incubator | venture_fund | fellowship | competition | venture_studio",
  "city": "Sydney",
  "who": "students, staff and alumni | anyone | researchers | women founders | …",
  "investment": "A$20k grant, no equity | US$150k SAFE | none | unknown",
  "sectors": "generalist | health | climate | deep tech | …",
  "deadline": "2026-11-14 | rolling | annual, usually March | last: 2026-03-01 | unknown",
  "next_cohort": "2027-02 | unknown",
  "status": "open | upcoming | rolling | closed | unknown",
  "url": "https://…",                       // the program's own page
  "qs_rank": 19                             // QS World University Rankings 2026 position if in the top 500, else null
}
```

## Rules

- **Today is 20 October 2026.** Give the next application deadline on or after today if one is published. Otherwise give the pattern, `last: YYYY-MM-DD`, `rolling` or `unknown`. Never invent a date.
- Real, current programs only, each with its own official page that you opened. If a program has no page of its own, use the university's entrepreneurship hub page and say so in `name`.
- Cover every program at each university, not just the flagship one (e.g. UNSW: 10x Accelerator and its Health and Climate tracks, Pre-Accelerator, New Wave, Peter Farrell Cup).
- Keep strings short and the JSON valid (no comments, no trailing commas).
