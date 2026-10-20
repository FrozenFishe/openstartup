# Wellfound: startups hiring by country

`startups_by_country.json` maps each atlas country to:

```json
{"count": 105, "url": "https://wellfound.com/startups/location/australia", "scope": "country", "checked": "2026-10-20"}
```

- **Source:** Wellfound's public location pages, `https://wellfound.com/startups/location/<slug>`. The count is the page's "N results total" figure.
- **What it measures:** companies with open roles in that country, including global companies with a local office. Read it as a hiring signal, not a census of local startups.
- **Validation:** a count is kept only when the page heading names the country. Wellfound serves its global list for slugs it doesn't recognise, so those rows were retried with alternative slugs (`macedonia`, `swaziland`, `myanmar-burma`, …). Wellfound has no country page for Canada, South Korea, Pakistan or Georgia (its `georgia` is the US state), so those use the main tech city (`scope: "city"`: Toronto, Seoul, Karachi, Tbilisi) and are lower bounds. North Korea, Laos, Somaliland and Guinea-Bissau have no page and are `null`.
- **Method:** pages were fetched one at a time, about one per second, from a signed-in browser on 2026-10-20. No candidate, applicant or personal data was collected.
