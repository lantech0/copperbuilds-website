# CopperBuilds.com — SEO Audit Report

**Date:** 2026-07-09
**Trigger:** Zero organic traffic reported by site owner
**Data sources:** Google Search Console (live, OAuth-connected this session), live crawl/curl of the production site, Common Crawl web graph, WHOIS. No DataForSEO or GA4 data (see Gaps below).

---

## Executive Summary

**This is not primarily a technical SEO failure — it's a brand-new domain with an indexing gap on 2 key pages and zero backlinks.** The site is not broken, blocked, or penalized. It is 7 weeks old, mostly indexed, and has not yet had time or external signal to rank for anything.

- **Domain age: 7 weeks.** Registered 2026-05-20 (Cloudflare Registrar). Google's data for this property covers the domain's *entire life* — there is no "before" period being missed.
- **Search visibility: 0 clicks, 1 impression, 0 query rows** — over both the last 30 days and the last 90 days (identical numbers; confirms this is the full history, not a truncated window).
- **Indexing: 4 of 6 core pages indexed** (home, /about, /contact, /pricing). **2 are not** (/services, /blog) — "URL is unknown to Google."
- **Backlinks: zero.** Common Crawl's web graph returns no referring domains for copperbuilds.com in the latest release.
- **No GA4 or any analytics tag installed on the live site.** Even once traffic starts, nothing is currently measuring it.
- **A real technical defect found:** `sitemap.xml` lists `.html` URLs that 308-redirect to the site's actual canonical clean URLs (e.g. sitemap says `/services.html`, but that permanently redirects to `/services`, which is the real canonical). This adds an unnecessary redirect hop on every sitemap URL except the homepage and is very likely contributing to the 2 undiscovered pages.
- **A secondary technical risk found:** nav and footer links are injected entirely via deferred JavaScript (`/js/nav.js`, `/js/footer.js`) with zero server-rendered `<a href>` fallback in the raw HTML. Googlebot can still render JS, but this pushes internal-link discovery into a slower, lower-priority rendering wave — worse for a brand-new, zero-authority domain than for an established one.

### Top 5 Critical/High Issues
1. **Sitemap references non-canonical `.html` URLs that 308-redirect** — fix the sitemap to list final canonical URLs directly.
2. **`/services` and `/blog` are unindexed** — likely compounding effect of #1 + weak/JS-only internal linking + no backlinks.
3. **Zero backlinks** — expected at 7 weeks old, but nothing is currently underway to change that.
4. **No GA4/analytics installed** — there is currently no way to measure traffic even after these fixes land.
5. **Internal nav/footer links are 100% client-side JS-injected**, no static anchors — raises reliance on Google's secondary render pass for discovering every page beyond the homepage.

### Top Quick Wins
- Regenerate `sitemap.xml` to list canonical URLs (no `.html`, no redirect hop) — 15-minute fix.
- Manually request indexing for `/services` and `/blog` via Search Console or the (now-connected) Indexing API — same day.
- Install GA4 — 15-minute fix, unblocks all future measurement.
- Add a handful of real server-rendered `<a href>` links to key inner pages somewhere in the static HTML (even in a `<noscript>` block or a simple always-rendered nav skeleton before JS enhances it) so first-wave crawl doesn't depend on JS rendering.

---

## Findings by Category

### 1. Domain & Search Visibility (Critical)
| Metric | Value |
|---|---|
| Domain registered | 2026-05-20 (Cloudflare, Inc.) |
| Domain age | ~7 weeks |
| GSC data range checked | 2026-04-10 to 2026-07-06 (90 days) |
| Clicks | 0 |
| Impressions | 1 |
| CTR | 0% |
| Query rows returned | 0 |

**What this means:** There has essentially been no organic search exposure at all — not "low rankings," but no measurable presence. This is consistent with domain age + indexing gaps + zero backlinks, not with a penalty or a broken site.

### 2. Indexation (Critical)
Checked via GSC URL Inspection API (live data, not estimated):

| URL | Status | Last Crawl | Referring URL (internal) |
|---|---|---|---|
| `/` (home) | ✅ Indexed | 2026-07-03 | — |
| `/about` | ✅ Indexed | 2026-07-03 | `/blog/local-seo-2026` |
| `/contact` | ✅ Indexed | 2026-07-02 | — |
| `/pricing` | ✅ Indexed | 2026-06-16 | — |
| `/services` | ❌ Unknown to Google | never crawled | none found |
| `/blog` | ❌ Unknown to Google | never crawled | none found |

`/about` was discovered via a real internal link inside a blog post's server-rendered HTML — direct evidence that pages **without** a static internal link pointing at them are the ones failing to get discovered. `/services` and `/blog` currently have no confirmed static internal links pointing to them anywhere on the site.

### 3. Sitemap / Redirect Mismatch (Critical — root cause candidate)
`sitemap.xml` lists these URLs:
```
https://copperbuilds.com/services.html
https://copperbuilds.com/pricing.html
https://copperbuilds.com/about.html
https://copperbuilds.com/contact.html
https://copperbuilds.com/blog.html
... (and more .html paths)
```
Every one of these returns **HTTP 308** and redirects to the extensionless clean URL (Cloudflare Pages' default clean-URL behavior):
```
/services.html → 308 → /services   (canonical: /services)
/about.html    → 308 → /about      (canonical: /about)
/pricing.html  → 308 → /pricing    (canonical: /pricing)
/contact.html  → 308 → /contact    (canonical: /contact)
/blog.html     → 308 → /blog       (canonical: /blog)
```
The redirect target's own canonical tag confirms the clean URL is authoritative. The sitemap should list the canonical URLs directly — submitting a redirecting URL in a sitemap is a well-documented crawl-efficiency anti-pattern (Google has to resolve every hop before it can even start evaluating the real page), and it's an easy, no-risk fix.

### 4. Internal Linking / JS Dependency (High)
- `robots.txt` correctly allows crawling (`Disallow` only on `/clients/` and `/brand_assets/`) and explicitly allows GPTBot, ClaudeBot, PerplexityBot, Google-Extended, CCBot, Bytespider.
- Nav (`/js/nav.js`) and footer (`/js/footer.js`) are loaded with `defer` and inject all their links via JavaScript — the raw HTML homepage response contains **no `<nav>` or `<footer>` anchor tags at all** for services/about/blog/help.
- The only static `.html` links found in the raw homepage HTML are to `contact.html`, `pricing.html`, `portfolio.html`, and 3 portfolio case pages.
- This isn't necessarily fatal (Googlebot does render JS), but it means every non-hardcoded nav link depends on the secondary render queue — a queue that is slower and lower-priority for new, zero-authority domains. Combined with the sitemap defect above, this plausibly explains why `/services` and `/blog` specifically have not been discovered yet.

### 5. Backlinks (Critical, but expected at this stage)
Common Crawl web graph (latest release, cc-main-2026-25): **no referring domains found**. Zero external link equity. Fully consistent with a 7-week-old domain that has not yet done outreach, directory listings, or citation building.

*(Moz/Bing Webmaster keys are not configured — only free-tier Common Crawl + verification crawler were available this session. See Gaps.)*

### 6. Analytics (High)
- `GA4_MEASUREMENT_ID` is blank in `copperbuilds.env`.
- Confirmed directly against the live homepage HTML: **no `gtag`, no `G-` measurement ID, no `googletagmanager.com`, no GTM container** anywhere in the page source.
- There is currently no way to measure sessions, conversions, or channel performance on the live site at all, independent of the SEO issues above.

### 7. Technical Basics Checked — Passing, No Action Needed
- `robots.txt`: correctly configured, no accidental blocks on public content.
- `sitemap.xml`: well-formed, 0 XML errors per GSC (structural issue is the URL choice, not the XML itself).
- Homepage response: HTTP 200, 0.34s, 47.5KB — fast.
- Images (homepage): 100% have descriptive `alt` text, WebP format, explicit `width`/`height`, correct `loading="eager"`/`fetchpriority="high"` on the LCP image and `loading="lazy"` elsewhere.
- Canonical tags: self-referencing correctly and matching Google's own canonical choice on every indexed page checked.
- Schema: at least one JSON-LD block present on the homepage (not deep-validated this pass — see Gaps).

---

## Gaps in This Audit (be aware before treating this as exhaustive)
- **No DataForSEO data.** Credentials are saved in `copperbuilds.env` but the DataForSEO MCP connector was not active this session — no live keyword volumes, SERP position tracking, or paid backlink/spam-score data (Moz/Bing).
- **No GA4 data** — not installed on the site (see Finding #6), so there was nothing to pull even with credentials.
- **No PageSpeed Insights/CrUX field data** — needs a separate simple `GOOGLE_API_KEY` (no OAuth required); not set up this session. Homepage load was only spot-checked with `curl` timing, not a full Core Web Vitals (LCP/INP/CLS) measurement.
- **Schema was not deep-validated** page-by-page against `validator.schema.org` — only confirmed present on the homepage.
- **Full 500-page crawl was not run** — this audit targeted the 6 core pages plus the technical/indexation/backlink checks most relevant to "zero traffic." A full crawl of blog posts and portfolio pages was not performed.

---

## Bottom Line

The site is not being penalized or blocked — it's young, thinly linked internally in two spots, and has no external link signal yet. That combination fully explains zero measurable traffic on its own; nothing here points to a deeper problem. The fixes below are what shorten the runway to real visibility.
