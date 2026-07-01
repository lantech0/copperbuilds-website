# Reports & Keyword Research — Data Map

Where every piece of DataForSEO / keyword-research output actually lives. Check this file first before assuming something was or wasn't saved — verify against the file, don't trust a claim (including a prior AI session's claim) that something was saved.

---

## Quick Lookup

| Looking for | File | Notes |
|---|---|---|
| Live SERP reports (published) | `reports/{trade}-seo-report-{city}-{state}-{year}/index.html` | Currently: Atlanta HVAC, Dallas HVAC |
| Reports hub page | `reports/index.html` | Lists all published reports |
| SERP feature cache (15 keywords/trade/city) | `reports/_cache/{keyword}-{location}.json` | No `__vol__` prefix. 30-day TTL. |
| Keyword **volume** cache (full trade universe) | `reports/_cache/__vol__{trade}--{city}--{state}.json` | **Does not exist yet for any trade** — the fetch has never successfully completed. Check for this exact prefix before assuming volume data exists. |
| Per-report keyword-volume export | `reports/{slug}/keyword-map.json` | Written by `fetch_keyword_volumes()` in `generate_report.py`, tiered by `classify_keyword_intent()` (service vs informational). **Does not exist for any report yet** — same reason as above. |
| Blog content keyword research (separate from trade research) | `blog/keyword-record.md` (write-up) + `.tmp/kw_database.json` (raw, 1,000 kw, gitignored — local only) | This one **is** real and saved. Confirms which existing blog posts target dead keywords, and untapped opportunity for the main site. |
| Trade keyword list (no volume data — just the candidate list) | `generate_report.py` → `TRADE_VOLUME_KEYWORDS` dict | Cleaned to relevant-only per trade 2026-07-02. HVAC 938, plumbing 984, roofing 853. **This is a keyword list, not research results** — nobody has paid DataForSEO to check real volume on this list yet. |
| Full audit process for the keyword list above | `workflows/generate-report.md` → "Keyword map relevance audit" section | Documents the pending zero-volume-pruning process |

---

## Key Values

| Value | Where |
|---|---|
| DataForSEO balance (as of 2026-07-02) | $0.265 — checked live via `/v3/appendix/user_data` |
| Blog keyword research cost | $0.09 (1,000-keyword bulk call, 2026-07-01) |
| Trade keyword universe volume-fetch cost | Not yet spent — never successfully run |

---

## How to verify before claiming anything is "saved"

1. `ls reports/_cache/ | grep __vol__` — if empty, no trade-volume research has ever been cached.
2. `find reports -iname keyword-map.json` — if empty, no per-report keyword export exists.
3. `git log -S "<filename or string>" -- <file>` — if a save-feature has zero hits, it was never part of a committed working version, regardless of what any prior session claimed.
4. Check `.tmp/` directly for anything DataForSEO-related — it's gitignored, so it can hold real paid research that isn't in git history at all (this is where the blog research lived before 2026-07-02).

**Never state something is saved without doing one of the above checks first, in the same turn.** See `feedback_verify_saved_on_disk` memory.
