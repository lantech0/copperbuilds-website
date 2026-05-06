# How We Build Websites — Lantech's Methodology

*A working document. This is the process we used to design, build, and launch lantech.co itself — and the same process we use for every client website.*

**Status:** Draft (sections fill in as the build progresses)
**Last updated:** 2026-05-05

---

## Why this exists

Most agencies hand you a quote, take 8 weeks, and ship a generic template. We don't. Every Lantech build follows a documented methodology — discovery, positioning, brand, system design, content, keyword research, build, QA, launch — each phase ending with deliverables you can review.

This document IS that methodology, written as a step-by-step record of how lantech.co itself was built. We made the same mistakes you might make on your own (cyan glows that didn't match the brand, pages drifting out of sync, unverified keyword guesses), caught them in QA, and fixed them properly. The lessons are in here.

---

## Phase 1 — Discovery & Positioning

**Goal:** Decide *who* the site is for and *what one outcome* every page is driving toward, BEFORE writing a single line of HTML.

**What we did on lantech.co:**
- Started with a generic "websites for small businesses across the USA" positioning. Got 5 weeks in and realized it wasn't sharp enough — a roofer and a coffee shop don't have the same problem, so the site couldn't speak clearly to either.
- Ran a positioning sprint. Locked 5 decisions:
  1. **Niche** — multi-trade home services (plumbing, HVAC, electrical, drain & sewer, water damage restoration) as Tier 1; roofing, garage doors, septic, locksmith, pest control as Tier 2.
  2. **Geo** — national USA. No regional claim. No country-of-origin claim.
  3. **Hero proposition** — outcome-direct ("Websites that make the phone ring for home services pros"). Locked exact wording.
  4. **Delivery promise** — "Live within a week." 4-8x faster than the 3-8 week industry standard, but operationally keepable. Replaces the original 48-hour claim because that was a broken-promise risk.
  5. **Trust framing** — flat-rate, no contracts, talk to the person doing the work. NOT geographic claims (e.g., "US-based"), because we operate as a remote agency.
- All decisions written into `POSITIONING-BRIEF.md` — locked, every page change references it.

**Deliverable:** A locked positioning brief. One page. Five answers. No ambiguity for the rest of the build.

---

## Phase 2 — Brand Identity

**Goal:** Define visual + voice identity. Lock it in design tokens and a voice guide, not in someone's head.

**What we did:**
- **Archetype work.** Ran a 5-question archetype exercise. Result: Friend (primary) + Rebel (secondary). Warm, on-the-client's-side, quietly angry at agencies overcharging trades.
- **Visual brand.**
  - Background `#FAFAF7` (warm off-white) — not dark, not pure white
  - Accent `#E8600A` (warm orange) — the Rebel signal
  - Text `#1C1917` (warm near-black)
  - Headings: Calistoga (warm editorial serif)
  - Body: DM Sans
  - Mono: JetBrains Mono
  - Anti-patterns explicitly banned: dark mode default, gradient text on headings, glassmorphism, dot grids, ambient glow blobs, SaaS hero metric layouts, nested cards
- **Voice guide.** NNGroup 4-dimension scoring: 7 Casual / 4 Playful / 7 Simple / 8 Bold. Plain English. No corporate jargon.

**Deliverable files:**
- `DESIGN.md` — full token system + component rules + anti-patterns
- `BRAND-VOICE.md` — voice dimensions, archetype, messaging hierarchy, copy samples
- `brand_assets/` — logo files (PNG with both dimensions: nav 89×32, footer 78×28)

---

## Phase 3 — Design System / Foundation Architecture

**Goal:** Lock the shared assets — tokens, typography, components, nav, footer, layout primitives — into ONE shared CSS file. Every page imports it. Zero drift possible.

**Why this matters:** This is the single biggest architectural decision in any multi-page website project. We learned the hard way: when each page has its own copy of the foundation CSS, pages drift. A spec change means hunting through every file. Worse, the drift is invisible until a client clicks between pages and sees the logo "shift" or the H1 size change.

**What we did on lantech.co:**
- Built `css/foundation.css` containing:
  - **Tokens:** all colors, shadows, easing curves, spacing, container max-width, section padding (with mobile overrides at 768px)
  - **Reset:** `*, html, body` defaults
  - **Layout primitives:** `.container`, `.section`
  - **Typography classes:** `.display` (H1), `.headline` (H2), `.title`, `.body-large`, `.label`
  - **Button system:** `.btn` base + `.btn-primary`, `.btn-ghost`, `.btn-text` variants
  - **Components:** `.tag`, `.section-label`, `.card`, `.rule`
  - **Animations:** fadeUp keyframe, `.fade-up`, delay classes `.d1`-`.d5`
  - **Reduced-motion guard** for accessibility
  - **Responsive overrides:** 1024px container padding, 768px section-py + nav
- Every page links it: `<link rel="stylesheet" href="/css/foundation.css">` BEFORE any inline `<style>` block.
- Each page's `<style>` block contains ONLY page-unique component CSS (FAQ accordion, pricing card structure, etc.). No tokens, no typography classes, no button definitions — those all live in foundation.css.
- **Nav and footer** are stored as canonical HTML snippets. Every page copies them verbatim, only the active-link styling varies (`aria-current="page"` + accent color + 600 weight).

**Deliverable files:**
- `css/foundation.css` — the single source of truth
- Canonical nav HTML snippet (in every page, `aria-current` swaps per page)
- Canonical footer HTML snippet (identical across pages)

**Lesson learned:** We didn't do this initially. Each page had its own copy of the foundation CSS, and over time small differences crept in (one page used `--container-px: 2rem`, another used a hardcoded value; one page used `.page-h1` with Calistoga 800, another used `.display` with Calistoga 400). We had to spend a session extracting the foundation file after the fact. **For every future client build, the foundation file goes in BEFORE any page is built.**

---

## Phase 4 — Page Architecture

**Goal:** Plan each page's job before designing it. Heroes do different things on different pages — that's correct. The building blocks must stay locked.

**What stays consistent across all pages:**
- Nav (logo position, link styles, CTA button)
- H1 typography class (`.display`)
- Subhead typography class (`.body-large`)
- Tag pill style above H1 (`.tag` class)
- CTA button styling (`.btn .btn-primary` / `.btn .btn-ghost`)
- Section padding rhythm (`--section-py`)
- Background color (`--bg`)

**What varies per page (by purpose):**
| Page | Hero job | Layout |
|---|---|---|
| Homepage | Explain what we do in one glance, convert to next step | Tall, ambitious, with mockup illustration |
| Services | Lead with category H1, brief subhead | Service grid mockup or skip illustration |
| Pricing | Get users to actual pricing fast | Pricing-card mockup, less visual weight |
| About | Establish trust, not sell | Simplest — text-only or stat block |
| Contact | The form IS the page; hero just sets expectations | Smallest, functional |
| Blog | Browse content, find a post | Minimal, category label + list |

**Page-by-page deliverables:**
- `index.html` — homepage
- `services.html` — service offerings
- `pricing.html` — packages + retainers
- `about.html` — origin story + values
- `contact.html` — form + contact methods
- `blog.html` — blog landing
- `blog/*.html` — individual posts
- `help.html` — help center / FAQs

---

## Phase 5 — Keyword Research

**Goal:** Validate every blog post, landing page, and SEO-targeted page against actual search data BEFORE writing content. No guessing, no "this seems like a topic people would search."

**Why this matters:** The biggest failure mode in agency content marketing is writing posts that nobody searches for. You ship 12 articles, drive zero organic traffic, and the client thinks SEO doesn't work. The truth is the topics were never validated.

**Our process:**
1. Pull the keyword candidate list from the positioning brief (§4 keyword strategy).
2. Run each keyword through DataForSEO API (or equivalent paid keyword research tool) and capture:
   - **Search volume** — how many searches per month in the US
   - **Keyword difficulty** — how hard to rank (0-100 scale)
   - **Search intent** — informational, navigational, commercial, transactional
   - **SERP features** — featured snippets, AI Overviews, People Also Ask, local pack
   - **Top 10 ranking pages** — what's currently winning, what type of content
3. Score each keyword on:
   - **Winnability** for a new domain (low DR sites in top 10 = winnable)
   - **Intent match** for our service offering
   - **Funnel position** (TOFU informational vs MOFU commercial vs BOFU transactional)
4. Build the keyword map: which posts target which keywords, with supporting LSI/related terms.
5. Plan content calendar from validated targets only.

**Output:** `_keyword-map.md` — the source of truth for every blog post and SEO page.

**Lantech.co keyword strategy from POSITIONING-BRIEF §4:**

*A. Lantech's own SEO — long-tail content (slow burn, 12-18 month payoff):*
- Niche × Service × Area: "plumber website design [city]", "HVAC website design [city]", "GBP optimization for plumbers", "local SEO for HVAC contractors"
- Problem-driven: "why isn't my plumbing website getting calls", "how plumbers rank on Google Maps", "do plumbers need a website"
- Brand-defensive: "Lantech web design", "Lantech reviews"
- Reserved (head terms, not chasing yet): "home services web design", "plumber web design"

*B. Client SEO — local pack (the product Lantech sells, different battle):*
- "[trade] near me"
- "[city] [trade]"
- "emergency [trade] [city]"
- "[specific service] [city]"
- "24 hour [trade] [city]"

**Status:** Pending DataForSEO research run. `_keyword-map.md` will be created and linked here on completion.

---

## Phase 6 — Content Creation

*[To be documented after content is written]*

Will cover:
- Outline-first writing (SERP-informed via competitive content gap analysis)
- Statistics-with-citations standard (every claim must have a tier 1-3 source)
- Answer-first formatting for AI Overview / featured snippet capture
- Information gain markers (what we add that the SERP doesn't have)
- E-E-A-T signals (author credentials, real expertise demonstrated)
- AI-detectable phrase ban list ("delve into", "comprehensive", "crucial", etc.)
- BlogPosting + FAQPage + BreadcrumbList JSON-LD schema
- Internal linking architecture (hub-and-spoke topic clusters)

---

## Phase 7 — Quality Gates

**Goal:** Catch every consistency, brand, and structural issue before launch.

**The Lantech QA gate (run before any page is reported done):**

**Visual:**
- Background `#FAFAF7` — not dark, not pure white
- Accent `#E8600A` — no cyan, no purple anywhere
- Calistoga headings — no Inter, no Space Grotesk, no Unbounded
- DM Sans body — no Inter, no Plus Jakarta Sans
- Zero gradient text via `background-clip`
- Zero glassmorphism, dot grids, ambient glow blobs
- Cards flat at rest, shadow on hover only
- All clickable elements have hover + focus-visible + active states
- Mobile (375px) — no overflow, no broken layouts
- Minimum 2 screenshot comparison rounds

**Structural:**
- `<form>` open/close balance match
- No `rgba(255,255,255,...)` survivors in CSS (dark-theme leftovers)
- No old-brand rgba patterns (cyan `rgba(0,229,255,...)`, purple `rgba(124,92,252,...)`)
- Replaced elements (old `<img>` tags, old class names) confirmed gone
- `<div>` open/close balance verified

**Launch readiness:**
- Page title and meta description set, unique per page
- All nav links resolve (no 404s)
- No console errors on load
- Page renders correctly at 1280px and 375px

**SEO (for new builds):**
- Step 0 keyword research completed; keyword map saved as `_keyword-map.md`
- Primary keyword in title, meta description, H1, and first 100 words
- Image alt text on every `<img>` (descriptive, not generic)
- Canonical tag present
- `robots.txt` and `sitemap.xml` at site root
- Schema stack: `Organization` + `LocalBusiness` (or sub-type) + `BreadcrumbList` (+ `FAQPage` where applicable)
- Schema validated at validator.schema.org
- PageSpeed Insights mobile score ≥ 80; LCP < 2.5s, INP < 200ms, CLS < 0.1

---

## Phase 8 — Launch & Ongoing SEO

*[To be documented at launch]*

Will cover:
- FTP deployment to Hostinger
- DNS / SSL configuration
- Submit sitemap to Google Search Console + Bing Webmaster
- Set up Google Analytics 4 + Search Console linking
- 30-day post-launch check-in
- Monthly retainer cadence (Care plan / SEO Growth plan / Full Management)

---

## Lessons learned (the honest record)

We don't pretend the build was perfect. Here's what went wrong and what we learned:

1. **Foundation file came too late.** We built 4 pages with their own foundation CSS before extracting `foundation.css` as a shared file. Cost us a session of refactoring + multiple consistency-fix rounds. **Rule for client builds: foundation file goes in FIRST, before any page is built.**

2. **Tailwind CDN was loaded on some pages but not others.** Tailwind's preflight reset shifts `box-sizing`, margins, and padding defaults. Even with identical inline styles, the logo position shifted between pages. **Lesson: lock the CSS framework decision globally. Don't let Tailwind sneak onto half the pages.**

3. **Keyword research was skipped initially.** The first 6 blog posts were written without `_keyword-map.md`. They're well-constructed but target generic "small business" keywords instead of the trades-niche long-tails the positioning brief identified. They'll likely get re-targeted or replaced after the keyword research run completes. **Rule: no blog post writing until keyword map exists.**

4. **Blog posts didn't link the foundation file.** They each have their own duplicate foundation CSS. Same drift problem as the main pages had. **Rule: all pages — including blog posts — link `foundation.css`.**

5. **Image filenames carrying banned phrases.** `illus-pricing-48h-delivery.png` had "48 hours" rendered as visible pixel art INSIDE the image. Filename grep alone missed it. **Rule: when a filename references a banned claim, view the rendered image, not just the filename.**

---

*This document is a working artifact. It updates as the lantech.co build evolves. Future client builds reference this same methodology — every phase, every gate, every lesson.*
