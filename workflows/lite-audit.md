# Workflow: Lite Audit (Pre-Call)

**Triggered by:** A prospect replies to outreach and agrees to a call (same trigger as `workflows/discovery-call.md`) — run this FIRST, before Pre-Call Prep
**Reuses:** The target-company audit process validated in `job-hunter/CLAUDE.md` §3 (Homaera application, 2026-08-31), scaled down for a warm prospect instead of a job application
**Feeds into:** `workflows/discovery-call.md` Pre-Call Prep (steps 2-4) and, if the call doesn't close, `workflows/proposal.md`'s "specific gaps" input

---

## Objective

Produce 2-3 specific, real findings about the prospect's existing web presence — fast enough to run on every warm lead before a call, thorough enough to sound credible when read back to the owner on the call.

This is NOT the full job-hunter-depth audit (that one took a full session and hit rate limits from an exhaustive 28-page crawl). It is NOT run on cold prospects — only on leads who have already replied and agreed to a call.

---

## When to Run

Immediately after a prospect is marked `[x] Call Booked` in `clients/prospects/[file].md`, before the call happens. If a call gets booked with less than a few hours' notice, run this workflow first regardless — the findings are what make Pre-Call Prep step 3 possible.

---

## Required Inputs

- Prospect's website URL (from `clients/prospects/[file].md` — if they have no site, this workflow doesn't apply; `workflows/prospect.md` already covers no-website leads)
- Prospect's trade/sector and location (for the Gold Standard competitor comparison already required by `discovery-call.md` Pre-Call Prep step 4)

---

## The 4 Core Checks

Run only these four. Do not add Keyword Planner or NAP grep passes — those need data a warm-but-not-yet-signed prospect wouldn't hand over pre-close, and they're what made the job-hunter version session-length.

### 1. Technical
- Fetch `robots.txt` and the sitemap (or crawl for one if missing)
- Flag: missing/broken sitemap, blocked pages that shouldn't be blocked, no `robots.txt` at all

### 2. On-Page (sampled, not full-crawl)
- Sample ~5-10 key pages: home, services/products, contact, and 1-2 top category or location pages
- Check title tag, meta description, H1 presence and uniqueness on each sampled page
- Flag: missing/duplicate titles, missing meta descriptions, missing or multiple H1s

### 3. Schema
- Check for structured data presence and type via `https://validator.schema.org/` on the homepage and one inner page
- Flag: no schema at all, wrong/generic type (e.g. `Organization` where `LocalBusiness` or a trade sub-type fits), validation errors

### 4. Core Web Vitals
- Manual PageSpeed Insights run — browser (Playwright) against `pagespeed.web.dev` for the homepage, mobile
- If the API is available and not quota-exhausted, use it directly instead — the manual browser run is the fallback, not the default
- Flag: LCP outside the green zone on mobile, CLS issues

---

## Writing the Findings

Do not hand back a raw audit log with line numbers or hedged paragraphs. Write:
- A 1-2 sentence summary of what's working and what isn't
- 2-3 labeled findings, each with the specific fact (not "SEO needs work" — "your site has no meta description on any of the 6 pages we checked")
- No roadmap section here — that's the proposal's job (`workflows/proposal.md`), not this workflow's

Save to: `clients/prospects/[slug]-lite-audit-YYYY-MM-DD.md`

Update the prospect file (`clients/prospects/[file].md`) with the top 2-3 gaps inline, so `discovery-call.md` Pre-Call Prep can pull them directly without re-opening the audit file.

---

## Required Outputs Before Considering This Workflow Done

- [ ] All 4 core checks run (technical, on-page sampled, schema, Core Web Vitals)
- [ ] Findings written as clean prose — summary + 2-3 labeled findings, no raw audit log
- [ ] Saved to `clients/prospects/[slug]-lite-audit-YYYY-MM-DD.md`
- [ ] Top 2-3 gaps copied into the prospect file for Pre-Call Prep to consume
- [ ] Gold Standard competitor + revenue opportunity figure noted (feeds `discovery-call.md` Pre-Call Prep step 4 — sourced separately, not part of the 4 core checks above)

---

## Edge Cases

**Prospect has no website:** This workflow doesn't apply — that's a `workflows/prospect.md` lead (no-website segment), a different and complementary case.

**Site is fully JS-rendered / blocks fetching:** Fall back to WebFetch and label those findings lower-confidence, same rule as the job-hunter version.

**Less than 2 hours before the call:** Run only checks 1-3 (technical, on-page, schema) and skip the PSI browser run if there's no time — note in the prospect file that CWV wasn't checked, don't fabricate a result.
