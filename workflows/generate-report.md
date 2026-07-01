# Workflow: SERP Visibility Report Generation

**Skill:** `/generate-report`
**Script:** `copperbuilds/generate_report.py`
**Output:** `copperbuilds/reports/{trade}-seo-report-{city}-{state}-{year}/index.html`

---

## Objective

Generate a self-contained static SERP visibility report for a specific trade + city. Each report shows who owns Google in that market, which keywords drive the most traffic, the revenue at stake, and where the openings are — used as both a prospect pitch leave-behind and a long-term SEO traffic page at `copperbuilds.com/reports/`.

---

## When to use

| Context | Note |
|---|---|
| **Step 2.5 of `workflows/prospect.md`** | Run before lead research. Use `--no domain` (prospect map mode). Report URL feeds Step 10 outreach. |
| **Standalone pitch prep** | Run for any trade+city before a discovery call or cold outreach push. |
| **Client audit** | Run with `--domain` to show client's position vs. competitors. |
| **SEO traffic play** | Publish reports for high-volume trade+city pairs to rank for "[trade] seo report [city]" searches. |

---

## Required inputs

| Input | Format | Example |
|---|---|---|
| Trade | One of the 10 supported values | `hvac` |
| City | City name | `dallas` |
| State | Two-letter abbreviation | `tx` |
| Domain | Optional — client domain for audit mode | `acmehvac.com` |

**10 supported trades:** hvac, plumbing, roofing, electrical, landscaping, painting, cleaning, concrete, pool, general_contractor

---

## Steps

### Step 1 — Collect inputs

If running via `/generate-report` skill: ask trade, city, state (and optionally domain) in one message before doing anything else.

If running standalone from CLI: confirm all three required args are present before running.

---

### Step 2 — Run the generator

From inside `copperbuilds/`:

```
python generate_report.py --trade {trade} --city {city} --state {state}
```

With domain audit: add `--domain {domain}`
Dry run (no API credits, mock data): add `--dry-run`

**Cache behavior:** DataForSEO results are cached for 30 days in `reports/_cache/`. If all 15 keywords are cached, the run takes ~10 seconds and costs $0. If any keyword is missing from cache, a live API call is made.

**After running:** confirm the output file exists at `reports/{trade}-seo-report-{city}-{state}-{year}/index.html`. If the script errors, read the full error before attempting any fix.

---

### Step 3 — Extract key numbers from the report

Open the generated `index.html` and pull these values for the hub card:

| Value | Where it appears |
|---|---|
| Local Pack rate % | Hero stat card ("X of 15 searches show a map pack") |
| Total monthly searches | Hero stat card |
| Revenue estimate | Hero stat card ("$XX,XXX estimated monthly revenue") |
| Market leader name | Market Ownership section — leader card |
| Leader slot-1 count | Position Breakdown insight line ("holds slot 1 on N of 15 searches") |
| Open opportunity count | Opportunity Keywords section footer note |

---

### Step 4 — Update the hub page

Open `copperbuilds/reports/index.html` and add a card to the `.reports-grid` section.

**Hub card format:**

```html
<a href="/reports/{trade}-seo-report-{city}-{state}-{year}/" class="report-card">
  <div class="report-trade">{TRADE LABEL}</div>
  <div class="report-title">Who's Winning Google for {Trade} in {City}, {STATE}?</div>
  <div class="report-meta">{City}, {STATE} &middot; {Month Year} &middot; 15 keywords analyzed</div>
  <div class="report-stats">
    <div class="report-stat">
      <div class="report-stat-num">{lp_pct}%</div>
      <span class="report-stat-label">Local Pack rate</span>
    </div>
    <div class="report-stat">
      <div class="report-stat-num">{total_searches}</div>
      <span class="report-stat-label">Monthly searches</span>
    </div>
    <div class="report-stat">
      <div class="report-stat-num">${revenue}</div>
      <span class="report-stat-label">Revenue at stake/mo</span>
    </div>
  </div>
  <div class="report-link">View report</div>
</a>
```

Use the values pulled in Step 3. Never use placeholder numbers.

---

### Step 5 — Update sitemap.xml

Add two entries to `copperbuilds/sitemap.xml` if not already present:

```xml
<url>
  <loc>https://copperbuilds.com/reports/</loc>
  <lastmod>{YYYY-MM-DD}</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.7</priority>
</url>
<url>
  <loc>https://copperbuilds.com/reports/{trade}-seo-report-{city}-{state}-{year}/</loc>
  <lastmod>{YYYY-MM-DD}</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.7</priority>
</url>
```

After adding, grep to confirm all URLs use `copperbuilds.com`:
```
grep -v "copperbuilds.com" sitemap.xml
```
Zero output = clean.

---

### Step 6 — Commit and deploy

Stage only the report files (never stage `_cache/` — it's gitignored):

```
git add reports/index.html reports/{trade}-seo-report-{city}-{state}-{year}/index.html sitemap.xml
git commit -m "feat(reports): add {trade} SEO report — {City}, {STATE} {year}"
git push origin main
```

Cloudflare Pages auto-deploys on push. Report goes live at:
`https://copperbuilds.com/reports/{trade}-seo-report-{city}-{state}-{year}/`

---

## What each report section shows

| Section | Data source | Business value |
|---|---|---|
| Hero stat cards | Aggregate of all 15 SERP results + volume API | Quick proof of market size |
| Consumer behavior hooks | Static stats (97% / 83% / 92%) | Anchors urgency before data |
| Keywords + volume table | DataForSEO Keywords Data API | Shows search demand per phrase |
| SERP Feature Analysis | Parsed from live SERP results | Which features fire + at what rate |
| Market Ownership | Aggregated local_pack appearances | Who owns the market + by how much |
| Map Pack Position Breakdown | `rank_group` per business per keyword | Slot 1 vs. 2 vs. 3 — depth of dominance |
| Top Opportunity Keywords | Volume × slot-1 ownership gap | Where a new entrant can win |
| Visibility Gaps | Conditional on feature prevalence | Critical vs. moderate gaps |
| Revenue Opportunity | Industry conversion benchmarks | Money on the table if you rank |
| Customer Questions | PAA boxes across all keywords | Content gap map |
| Pitch section | Static narrative | What to fix + CTA |

---

## Keyword map relevance audit (pending — not yet run)

`fetch_keyword_volumes()` also writes `reports/{slug}/keyword-map.json` — the full per-trade keyword list from `TRADE_VOLUME_KEYWORDS`, each tagged with `tier: "service"|"informational"` (see `classify_keyword_intent()`) and its real DataForSEO search volume for that city.

Topical review (does this phrase make sense for the trade) was already done for `TRADE_VOLUME_KEYWORDS` — brand/product-line checks, no cross-trade contamination, no dealer/manufacturer-facing terms, no filler/speculative "for [niche location]" combos. But topical relevance is not the same as real search demand: a keyword can be legitimate for the trade and still return 0 volume in a given market. The only way to catch that is real data, not more review.

**Process, once there's enough real report volume to make it worthwhile:**
1. Run `/generate-report` normally for a representative city in the trade.
2. Open `reports/{slug}/keyword-map.json`.
3. Filter keywords where `volume == 0`.
4. Cross-check the 0-volume list against 1-2 more cities before removing anything — a single market's 0 doesn't mean the keyword is dead everywhere.
5. Keywords that return 0 across multiple cities/markets are strong candidates to prune from `TRADE_VOLUME_KEYWORDS` in `generate_report.py`.

**Status:** not yet run for any trade. Current `TRADE_VOLUME_KEYWORDS` counts (as of 2026-07-02, post-cleanup): HVAC 938, plumbing 984, roofing 853.

---

## Quality gate

Before reporting done:

- [ ] `reports/{slug}/index.html` exists and opens without errors
- [ ] Hero stat cards show real numbers (not dashes or zeros)
- [ ] Market Ownership section has at least one competitor with reviews/rating/phone
- [ ] Position Breakdown shows stacked bars for top competitors
- [ ] Opportunity Keywords table has at least one "Open" row
- [ ] Hub page card added with correct stats (not placeholder values)
- [ ] Sitemap updated and grep confirms `copperbuilds.com` domain only
- [ ] Git push confirmed — Cloudflare deploy triggered

---

## Edge cases

| Situation | Action |
|---|---|
| Script errors with 403 / auth failed | Check `DATAFORSEO_USERNAME` + `DATAFORSEO_PASSWORD` in `copperbuilds.env`; verify account is verified at `app.dataforseo.com` |
| Location returns empty results | Delete stale cache files for that trade+city and rerun; check location format (must be `City,Full State Name,United States`) |
| Revenue section shows `—` or zeros | Volume fetch failed — check DataForSEO Keywords Data API separately; rerun after fixing |
| Report already exists for this trade+city | Rerunning will overwrite the report with fresh data (or from cache if still valid). Update hub card date. |
| `--dry-run` produces zeros | Expected — mock data doesn't include realistic volumes |
| User declines deploy | Leave report in `reports/` — it will deploy on the next push for any reason |

---

## Handoff to prospect workflow

After generating a report for a trade+city:
- Pull top competitors from Market Ownership → feed to Step 3 (Gold Standard)
- Pull opportunity keywords → feed to Step 9.5 (pitch angles)
- Save published URL → include in Step 10 outreach as credibility leave-behind
- Format: *"I ran a live analysis of [trade] businesses in [city] — here's the data: [URL]"*
