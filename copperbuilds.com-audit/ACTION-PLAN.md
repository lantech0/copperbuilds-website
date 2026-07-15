# CopperBuilds.com — Action Plan

Prioritized off `FULL-AUDIT-REPORT.md`. Every item below traces to a specific verified finding — nothing here is speculative.

## Phase 1: Critical Fixes (This Week)

- [ ] **Regenerate `sitemap.xml` to list canonical URLs, not `.html` paths.** Replace every `https://copperbuilds.com/services.html`-style entry with `https://copperbuilds.com/services` (and same for about, pricing, contact, blog, and any other redirecting paths). Removes an unnecessary 308 hop from every sitemap URL except the homepage.
- [ ] **Manually request indexing for `/services` and `/blog`** via Search Console → URL Inspection → "Request Indexing" (now that GSC is connected, this can also be scripted via `gsc_inspect.py`/the Indexing API — confirm scope covers regular pages, not just job/livestream schema, before relying on it as the only method).
- [ ] **Install GA4** on the live site (measurement ID currently blank in `copperbuilds.env` and absent from the live HTML). Without this, none of the traffic gains from the other fixes will be measurable.
- [ ] **Add real server-rendered `<a href>` links** for services/about/blog somewhere in the static HTML (not solely inside `nav.js`/`footer.js`) — e.g. a plain-HTML nav skeleton that JS then enhances, rather than JS building the entire nav from nothing. This gives Googlebot's first-wave (non-JS) crawl a path to every page without waiting on the render queue.

## Phase 2: High-Impact Improvements (Weeks 2-3)

- [ ] Start basic backlink acquisition — directory listings (Clutch, GoodFirms, local chamber of commerce, trade-association directories), since Common Crawl currently shows zero referring domains.
- [ ] Set up PageSpeed Insights/CrUX properly — just needs a `GOOGLE_API_KEY` (API key only, no OAuth) enabled in the same Cloud project (`lantechai-mcp`) already used for GSC. Gives real LCP/INP/CLS field data instead of a spot `curl` timing check.
- [ ] Deep-validate schema on every page type (home, service, blog post) at `validator.schema.org` — only the homepage's presence was confirmed this pass, not correctness or completeness across page types.

## Phase 3: Content & Authority (Month 2)

- [ ] Once GA4 is live and indexing gaps are closed, re-run this audit's GSC checks to confirm `/services` and `/blog` have moved from "unknown" to indexed, and check for any new query impressions.
- [ ] Begin structured content/link-building cadence appropriate to a brand-new domain — this is normal ramp-up work, not a fix for a broken site.

## Phase 4: Monitoring & Iteration (Ongoing)

- [ ] Re-check GSC indexation status for all core pages monthly until stable.
- [ ] Track backlink count via Common Crawl (or Moz/Bing if keys are added) monthly.
- [ ] Track GA4 organic sessions once installed.

---

## Explicitly Deferred (surfaced, not silently skipped)
- **DataForSEO-based keyword/SERP/competitor analysis** — connector wasn't active this session; user can reconnect it for live keyword volume and ranking-position data.
- **Full 500-page site crawl** (blog archive, portfolio pages) — this pass focused on the 6 core pages plus the indexation/backlink/analytics diagnosis most relevant to "zero traffic."
