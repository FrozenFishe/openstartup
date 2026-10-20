# Research patches

Corrections and additions made after the first research pass. `build.py` applies every `*.json` file here, in filename order, on top of `research/countries/`.

Each file is a JSON array of country patches:

```json
[
  {
    "country": "Qatar",
    "add": {
      "vcs": [{"name": "", "city": "", "stage": "", "check_size": "", "sectors": "", "type": "vc", "url": ""}],
      "accelerators": [], "grants": [], "resources": []
    },
    "set": [
      {"list": "accelerators", "name": "QSTP XLR8", "fields": {"deadline": "2026-12-01", "status": "open"}}
    ],
    "remove": [{"list": "vcs", "name": "Defunct Fund", "reason": "site parked since 2026"}],
    "country_fields": {"confidence": "medium", "summary": "…"},
    "notes_append": "2026-10-20 gap-fill: …",
    "sources": ["https://…"]
  }
]
```

- `add` items use the same fields as `research/SCHEMA.md`. Items whose name already exists in that list are ignored.
- `set` changes fields on an existing item, matched by `list` and case-insensitive `name`.
- `remove` drops an item, with a reason.
- `country_fields` overwrites top-level fields (`summary`, `startup_visa`, `company_setup`, `confidence`, `ecosystem_tier`).
- `notes_append` adds a line to the country's notes; `sources` are added to its sources.
