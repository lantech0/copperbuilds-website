# SEO-STANDARDS.md — Universal SEO & Local SEO Standards

Read this before any SEO work — CopperBuilds' own site AND all client builds/retainers.
This is the single source of truth for SEO/local SEO **rules and facts**. Workflows
(`seo-retainer.md`, `offpage-strategy.md`, `gmb-setup.md`, `client-build-standards.md`)
hold the **execution steps and checklists** — they reference this doc instead of
restating the rules inline.

**Last verified:** 2026-07-09, via live web research (Whitespark 2026 Local Search
Ranking Factors, Google Search Central, BrightLocal, Sterling Sky, Thrive Agency, Search
Engine Land, and other sources cited inline below). Re-verify factual claims below
against a fresh search before treating them as current more than ~12 months from that date.

---

## 1. On-Page & Technical SEO

### Schema — mandatory, never post-launch
Structured data is required on every page, added during the build, validated before
delivery. Zero errors at `https://validator.schema.org/` before launch — warnings on
optional fields are acceptable, errors are not.

| Page type | Required schema |
|---|---|
| Every page | `Organization` + `BreadcrumbList` (inner pages) |
| Homepage | `LocalBusiness` (most specific trade sub-type available) + `WebSite` |
| Service page | `Service` + `FAQPage` (if FAQ section present) |
| Service-area page | `LocalBusiness` with `areaServed` + `Service` |
| Blog post | `BlogPosting` + `FAQPage` (if FAQ section) + `HowTo` (if step-by-step) |

**Do:** use the most specific `LocalBusiness` sub-type available (`Plumber`,
`HVACBusiness`, `Electrician`, `RoofingContractor`, etc.) — plain `LocalBusiness` is a
fallback, not a first choice. Required properties on every `LocalBusiness` block: `name`,
`address`, `telephone`, `openingHoursSpecification` — confirmed current against Google
Search Central guidance.

**Don't:** add `FAQPage` or `HowTo` schema for Q&A/steps that don't visibly exist in the
HTML. Google's spam filters now actively match visible page content against schema —
mismatched or hidden schema is penalized more heavily in 2026 than in prior years.
(Google Search Central, structured-data guidelines)

**Forward-looking — no client needs this yet, document before it's needed:** for any
future multi-location client, each location page needs its own `LocalBusiness` schema
with consistent NAP, all sharing one canonical `Organization @id`.

### Featured Snippets
Two elements are both required — schema alone does not capture a snippet:
1. Question-format H2s/H3s on pages targeting informational queries
2. A direct 40–60 word answer immediately following the heading — no preamble, no
   "it depends" opener

### Core Web Vitals
| Metric | Threshold |
|---|---|
| LCP (Largest Contentful Paint) | < 2.5s mobile |
| CLS (Cumulative Layout Shift) | < 0.1 |
| INP (Interaction to Next Paint) | < 200ms |

**2026 update:** INP is now the most commonly failed Core Web Vital — 43% of sites still
fail it. Measurement methodology weights *sustained* latency more heavily than before: a
single stuttering interaction can fail a page even if most interactions are fast. Test
with the `web-vitals` JS library v4+, not just a single PageSpeed snapshot. (WebVitals.tools,
2026)

### Launch Smoke Test — essentials
- Unique `<title>` ≤ 60 chars and unique `<meta description>` ≤ 160 chars per page —
  count, don't eyeball
- Every `<img>` has an `alt` attribute (`alt=""` only for purely decorative)
- Canonical tag on every page
- `sitemap.xml` + `robots.txt` at site root, sitemap URLs all on the live domain
- Any page not in the sitemap/nav gets `<meta name="robots" content="noindex, follow">` —
  added at file creation, not as later cleanup
- Text contrast ≥ 4.5:1 on background

---

## 2. Local SEO — Google Business Profile (GBP)

### Ranking Factor Weights (2026)
| Factor group | Weight |
|---|---|
| GBP signals | 32% |
| Reviews | 20% |
| On-page signals | 19% |
| Links | 15% |
| Proximity to searcher | ~55% of the actual decision — separate from the category weights above, and **uncontrollable** |

*(Whitespark 2026 Local Search Ranking Factors)* — set client expectations explicitly on
hyper-local queries: we cannot out-rank a closer competitor purely on optimization.

**Primary category is the single most important individual GBP factor** — current score
227 (Whitespark 2026). Choosing the wrong primary category is the #1 negative factor.
Optimal: 1 primary + up to 4 secondary categories (BrightLocal benchmark).

**Ranking has shifted from "prominence" toward "popularity."** Backlink history and
account age used to dominate; Google now weights CTR, dwell time, and review engagement
more heavily. A newer, active business can outrank an established but inactive one —
this is the reason behind the weekly GBP posting cadence in `seo-retainer.md`. (EmbedSocial,
2026)

### Do's
- Post to GBP weekly minimum — text-only posts underperform, always include a photo
- Link the GBP website field to the homepage or a dedicated `/from-google` landing page —
  **never** to the exact page you're trying to rank organically (Sterling Sky Diversity
  Update: this risks suppressing that page's own rankings)
- Businesses open at search time rank higher — keep hours accurate, set holiday hours
- WhatsApp is now a native GBP contact channel (2026) — offer it to clients who already
  use WhatsApp for lead intake
- Use identical NAP across GBP, the website footer, contact page, and schema — any
  variation creates citation inconsistencies

### Don'ts
- Never enter a public street address for a Service Area Business — hide it during setup
- Never use stock photos on GBP — Google detects and devalues them
- Never leave the primary category blank or guess — pick the closest real match

---

## 3. Local SEO — Reviews

- **Velocity target: 4–8 new reviews/month, consistently.** Review recency is the #11
  local ranking factor (up sharply in recent years) — consistent monthly velocity
  outperforms any single volume spike. (Whitespark 2026 — confirmed current)
- The "18-day review drought" figure (Sterling Sky) is *not independently reconfirmed*
  as of this pass — it's directionally consistent with the confirmed review-recency
  weighting, so it's kept as a working guideline, not treated as freshly verified.
- **Spam filter warning:** a sudden spike (20+ reviews in one week) risks suppression.
  Stagger requests at 20–30/week max, never bulk-send.
- Respond to every review within 24–48 hours — responding within 24h measurably
  amplifies the ranking benefit vs. slower responses.

### Review Gating — Hard Don't
Never pre-screen customer satisfaction before directing them to the review link. This is
"review gating" and is prohibited by both Google and the FTC.

- **FTC fine: $53,088 per violation** (2026 inflation-adjusted figure, finalized Consumer
  Review Rule, 16 CFR Part 465). *(Corrected from a previously-documented $50,088 figure.)*
- **April 2026 Google enforcement wave** explicitly bans: review kiosks/shared-tablet
  review stations, incentivized reviews, staff review quotas, and review requests that
  name or target a specific employee.
- Google is now **retroactively removing** previously-gated reviews, not just blocking
  new ones going forward — a legacy gated-review campaign is a live risk, not a closed one.

### Negative Reviews
Never respond without the account owner's approval on the wording first. Flag
immediately with the review text and star rating; hold the response until approved.

---

## 4. Citations & NAP

**NAP consistency standard:** every citation must match the business's canonical record
exactly — same phone format, same business name abbreviation, same address style ("St."
vs. "Street", "LLC" present or absent). Even minor discrepancies trigger verification
flags in Google's Knowledge Graph. When a citation is fixed, also verify the website's
`LocalBusiness` schema matches.

| Tier | Directories |
|---|---|
| Tier 1 (claim first) | Google Business Profile · Bing Places · Apple Business Connect · Yelp · BBB · Clutch.co (agency-specific) · DesignRush (agency-specific) |
| Tier 2 | Angi (formerly HomeAdvisor + Angi's List — **now one platform**, do not claim as two separate directories) · Porch · Thumbtack · Houzz · Nextdoor Business |
| Tier 3 | Data Axle · Manta · Chamber of Commerce (if applicable) · trade association directories |

*(Correction: HomeAdvisor and Angi were previously listed as two separate directory
targets — HomeAdvisor fully redirects to Angi.com and operates as "Angi Leads." Treat as
a single citation.)*

**Data aggregators** (submit once, they distribute to hundreds of downstream directories
over 2–6 weeks): Data Axle, Foursquare, Neustar/TransUnion.

**No deprecations found** for Bing Places, Apple Business Connect, Yelp, BBB, Data Axle,
or Foursquare — all confirmed current and correctly prioritized.

---

## 5. Link Building — Do's and Don'ts

**Counts as a quality link:** a real site, locally relevant or trade-relevant, with a
crawlable page linking to the domain (chamber of commerce, local press, trade
association directories, home improvement media, neighborhood/community sites, guest
posts on relevant trade or small-business publications).

**Does NOT count:** link farms, paid link networks, irrelevant directories.

**"Best of" list placements are the #1 AI visibility factor** (Whitespark 2026) — when
ChatGPT or another AI assistant recommends a business, it's very often sourcing from
these lists. Prioritize getting on existing "best of [trade] in [city]" lists over
generic directory citations, especially in competitive markets.

**Brand mentions correlate roughly 3× more strongly with AI visibility than backlinks**
(Ahrefs correlation: 0.664 vs. 0.218). Unlinked mentions on forums (Reddit, Quora),
communities, and social platforms still build AI-visibility equity even without a link —
don't discount an unlinked mention as wasted effort.

**Never:** buy links, use link farms, or force irrelevant directory placements just to
hit a monthly link count. A documented outreach attempt with no response is a valid
logged effort — a pending or rejected outreach must never be falsely counted as a
secured link.

---

## 6. Local Services Ads (LSA) Rules

- **LSA reviews are fully merged into Google Business Profile** as of **July 11, 2025**
  — there is no separate LSA review system anymore. Managing GBP reviews *is* managing
  LSA reviews. (Confirmed current)
- **Valid lead (do not dispute):** any connected call for the correct trade and service
  area, even if unanswered or not booked. Google charges for the lead, not the outcome.
- **30-second billing rule:** any call lasting 30 seconds or longer is automatically
  billed, no exceptions.
- **Auto-credit:** Google's AI reviews every lead within 72 hours and automatically
  credits clear spam, robocalls, and immediate-hangup wrong numbers — no action needed.
- **Manual dispute path:** the only manual flag available is **"Rate This Lead"** inside
  the LSA dashboard, within 30 days of the lead. The old "Report a Problem" button was
  removed. **Set realistic expectations with clients** — "Rate This Lead" only
  successfully triggers a credit on roughly 20% of leads flagged this way; present it as
  a partial safeguard, not a reliable dispute process.
- **No longer disputable:** "job type not serviced" and "outside service area" were
  removed as credit reasons. Fix these at the profile level instead (service categories,
  service area settings) so mismatched leads stop arriving in the first place.

---

## 7. GEO / AI Search Visibility

- **2026 resource allocation guidance:** roughly 70% traditional SEO / 25% GEO-specific
  work / 5% experimental. Use this as a rough guide for how much retainer time goes to
  the AI-search-spot-check and citation work vs. everything else. (Search Engine Land, 2026)
- **Citing authoritative third-party sources inline in blog content measurably lifts AI
  citation rates** — up to +115% visibility lift documented for lower-ranked sites.
  Actionable: every blog post should cite at least one credible external source inline,
  not just internally link.
- **llms.txt adoption is NOT proven to independently increase AI citation rates.** Don't
  over-invest in it at the expense of the fundamentals above (citations, reviews,
  content structure) — it's a minor, unconfirmed lever, not a core one.
- **Local and AI-search signals have functionally merged** — the same GBP/citation/review
  inputs that drive Google Maps rankings also drive what ChatGPT, Perplexity, and Google
  AI Overviews recommend. There is no separate "AI SEO" input stream to manage.
- **Spot-check process:** search the client's primary keyword pattern ("best [trade] in
  [city]") across ChatGPT, Perplexity, and Google AI Overview. Note whether the client is
  cited and which competitors are. Trends across months matter more than any single
  reading.

---

## 8. Client-Build SEO Standards

Full build-time execution checklist (schema stack, Core Web Vitals implementation,
above-fold formula, dual visitor architecture, pre-launch smoke test) lives in
`workflows/client-build-standards.md` — that file is the **execution gate**, this
document is the **current-facts reference** it should be read alongside. When the two
disagree on a number or rule, this document is the more recently verified one.

---

## Quick Lookup — Where to Execute

| Need to... | Go to |
|---|---|
| Run the monthly SEO retainer (GBP, citations, reviews, links, reporting) | `workflows/seo-retainer.md` |
| Set up a new GBP listing or fix a suspended one | `workflows/gmb-setup.md` |
| Run off-page/citation/link-building program setup | `workflows/offpage-strategy.md` |
| Build or QA a client website (schema, CWV, above-fold, smoke test) | `workflows/client-build-standards.md` |
| Pre-build keyword research and SEO field generation | `/copperbuilds-seo [client-slug]` |
| Standalone SEO audits (page, technical, local, schema, GEO) | `/seo-page` · `/seo-technical` · `/seo-local` · `/seo-schema` · `/seo-geo` |

---

## What NOT to Do — Hard Rules

- **Never** review-gate — pre-screening satisfaction before the review link is illegal
  and actively enforced in 2026
- **Never** add schema for content that isn't visibly present on the page
- **Never** link a GBP profile to the exact page being organically optimized
- **Never** claim HomeAdvisor and Angi as two separate citation wins — same platform
- **Never** present "Rate This Lead" to a client as a reliable dispute mechanism
- **Never** promise a #1 local ranking against a closer competitor — proximity is ~55%
  of the decision and is not something optimization overrides
- **Never** over-invest in llms.txt at the expense of citations, reviews, and content
  fundamentals
- **Never** launch a client page with failing Core Web Vitals, missing schema, or a
  gated review program already running
