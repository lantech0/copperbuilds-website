# client-build-standards.md — Lantech Client Website Build Standards

## Objective

Define the non-negotiable UX, performance, and design standards that every Lantech client website must meet before it can be marked launch-ready. These standards are drawn from research into top home services agencies (Hook Agency, Scorpion, KickCharge, Rival Digital, Built-Right Digital, BlackStorm) and enforced as hard quality gates in the build process.

**Scope: one-time website build only (Step 1 — Starter / Growth / Pro).** The monthly retainer (Step 2 — Local Presence / Lead Machine / Market Leader) is a separate product that manages the site after launch. Do not mix build deliverables with retainer deliverables. If something is an ongoing monthly task, it belongs in `workflows/monthly-report.md` or `workflows/maintenance.md`, not here.

---

## Trigger

Run this workflow during every client site build, starting from Step 2 of the page build process (after `/impeccable craft` drafts the design brief). Use it as the acceptance checklist before any page goes live. Also reference it when reviewing or revising an existing client site.

Before drafting any copy: read `COPY-STANDARDS.md` (universal grammar and copywriting standards) and the client's `BRAND-VOICE.md` (client-specific tone and vocabulary). Both are required — standards set the floor, brand voice sets the personality.

---

## Required Inputs

- Client discovery notes (trade type, service area, emergency services flag, page count)
- Client photos (trucks, team, job site) — confirm existence before build starts
- Agreed tier (Local Presence / Lead Machine / Market Leader)
- Target city/cities and primary trade keyword (e.g., "plumber Denver")
- Client `BRAND-VOICE.md` — read before drafting any copy. If none exists yet, create one from the discovery call notes before starting the build.

---

## Steps

### Step 1 — Confirm Photo Assets

Before building any page, ask the client:

> "Do you have photos of your team, trucks, and job sites I can use? Real photos outperform stock images for trust and local search rankings."

**If yes:** Use client photos throughout. Place real team/truck photos in the hero and gallery sections.
**If no:** Proceed with placeholder images only. Flag in the handover notes that real photos should replace placeholders within 30 days of launch.

**Standard: Zero stock photography in production.** Stock images are permitted only as temporary placeholders — never as a finished state.

---

### Step 2 — Apply Dual Visitor Architecture

Every page (especially Home and Service pages) must serve two visitor types simultaneously:

**Emergency caller layer:**
- Phone number visible without scrolling (hero + sticky header)
- Click-to-call `<a href="tel:...">` on every phone number
- "Available now" or "24-hour service" messaging near the phone number if the client offers emergency service
- Sticky header persists on scroll with the phone number always visible

**Planned buyer layer:**
- Lead capture form (max 4 fields: name, phone, service type, message)
- Service gallery showing real work
- Trust signals (years in business, licenses, reviews count)
- Service-area coverage map or list of cities

Both layers must be present on the homepage. Service pages must have at least the emergency layer above the fold.

---

### Step 3 — Apply the Above-Fold Formula

The first visible screen (no scroll required) must contain all three of these elements:

| Element | Requirement |
|---|---|
| **Headline** | Names the trade + location OR the primary customer outcome (e.g., "Plumbing Repair in Denver — Fast & Reliable") |
| **Contact method** | Phone number (click-to-call) OR a 4-field lead form |
| **Trust signal** | One of: years in business, review count, license number, or "licensed & insured" badge |

If any element is missing from the first screen, the page fails this gate.

---

### Step 4 — Enforce Navigation Rules

Max 5 nav items. Standard structure for home services sites:

```
Home | Services | About | Reviews | Contact
```

Or for multi-service businesses:
```
Home | Services (dropdown) | Service Areas | About | Contact
```

**Banned patterns:**
- More than 5 top-level nav items (analysis paralysis kills conversions)
- No phone number in the nav/header
- Dropdown menus with more than 8 items

The phone number must appear in the nav bar itself, right-aligned, as a click-to-call button.

---

### Step 5 — Build Lead Forms to Spec

Every form on the site must follow these rules:

- **4 fields maximum:** Name, Phone, Service Type (dropdown), Message/Job Description
- **No required email field** — phone converts better for home services, and email gates cause abandonment
- **Submit button copy:** Use action-oriented labels: "Get a Free Estimate", "Book a Visit", "Call Me Back" — never just "Submit"
- **Form placement:** Above the fold on the homepage, at the bottom of every service page
- **Mobile:** Full-width, large tap targets (min 44px height per field)

---

### Step 6 — Meet Core Web Vitals Thresholds

Every page must pass these Google performance standards before launch:

| Metric | Required threshold | What it measures |
|---|---|---|
| **LCP** (Largest Contentful Paint) | < 2.5 seconds | How fast the main content loads |
| **CLS** (Cumulative Layout Shift) | < 0.1 | How much the layout shifts during load |
| **INP** (Interaction to Next Paint) | < 200ms | How fast the page responds to taps/clicks |

**How to check:** Run PageSpeed Insights on the staging URL before delivery (mobile tab, Slow 4G).

**Mandatory performance implementation — apply these during build, not as a fix-up:**

**Images (biggest LCP factor):**
- Convert every image to WebP before adding it to the site — use PIL (`img.save(dst, "WEBP", quality=82, method=6)`) or Squoosh
- Full-page screenshots used as card thumbnails must be cropped to the visible above-fold area (max 1440×900) before converting
- The first above-fold image (hero or LCP candidate) gets: `loading="eager" fetchpriority="high"` and a matching `<link rel="preload" as="image" href="..." fetchpriority="high">` in `<head>`
- Every other image gets `loading="lazy"`
- Every `<img>` tag must have explicit `width` and `height` matching the intrinsic image dimensions
- Target: total homepage payload under 1 MB

**Fonts:**
- Never link Google Fonts externally — it adds 2–4 external round-trips (DNS + TLS × 2 hosts) before any text renders
- Self-host all fonts: download WOFF2 files from Google Fonts, save to `/fonts/`, serve via a local `fonts.css` with `@font-face` rules
- Use the script at `copperbuilds/.tmp/selfhost_fonts.py` as the reference pattern
- Include `font-display: swap` in every `@font-face` rule

**JavaScript:**
- Every `<script src="...">` tag in `<head>` or early `<body>` must have `defer` — no render-blocking JS

**Accessibility (contrast + landmark):**
- Every page must have a `<main>` element wrapping the primary content (between nav and footer)
- Text colors must achieve ≥ 4.5:1 contrast ratio on the background — `#6B6560` on `#FAFAF7` passes (4.97:1); `#A8A29E` on `#FAFAF7` fails (2.3:1)

**If still failing LCP after the above:** check for render-blocking CSS, third-party embeds, or unoptimized web fonts. Do not launch with a failing LCP.

---

### Step 7 — Implement Trust Strip

Every page must have a trust strip — a row of 3–5 short trust signals — placed directly below the hero section. This is standard on 90%+ of high-converting home services sites.

**Trust strip elements (choose 3–5):**
- Licensed & Insured ✓
- [X] Years in Business
- [X]+ 5-Star Reviews
- Same-Day Service Available
- Serving [City/Region] Since [Year]
- BBB Accredited (if applicable)
- Response Time (e.g., "Respond within 1 hour")

**Implementation:** A horizontal strip with icon + label format. Should be scannable in under 3 seconds.

---

### Step 8 — Configure Mobile Click-to-Call

Mobile is the primary device for home services searches (60–75% of traffic). Mobile configuration is mandatory:

- **Floating call button:** Fixed-position button at bottom of mobile viewport linking to `tel:` — must be present on all pages
- **Touch targets:** All tap targets (buttons, nav links, form fields) must be at least 44×44px
- **Phone number tappable:** Every phone number on the page must be wrapped in `<a href="tel:+1XXXXXXXXXX">`
- **No phone number as plain text** — it must always be a tap-to-call link

---

### Step 9 — Build Service-Area Pages (Growth and Pro builds)

Service-area pages are built as part of the one-time website build, not the monthly retainer. The number of city pages included depends on the build tier:

| Build tier | City pages included |
|---|---|
| Starter ($1,200) | None — just the core service page |
| Growth ($1,699) | 3 city pages — one per top city the client serves |
| Pro ($1,999) | Full city coverage — one dedicated page per city served |

The monthly retainer then **maintains** these pages (keeps them current, adds keywords, refreshes content). The retainer does not build new city pages from scratch — that is a build-tier deliverable.

**URL structure:** `/[city]-[trade]/` (e.g., `/denver-plumber/`, `/aurora-hvac-repair/`)

**Each service-area page must have:**
- Title tag: "[Trade] in [City] | [Business Name]"
- H1: "[Trade] Services in [City]" or "[City]'s Trusted [Trade] Pros"
- 300+ words of unique, localized copy (mention landmarks, neighborhoods, zip codes)
- The client's real phone number with click-to-call
- A lead capture form
- Local business schema markup (LocalBusiness + Service)

**Do not duplicate the homepage** — each SAP must have unique copy. Thin SAPs with copy-paste content will be penalized by Google.

---

### Step 10 — Implement the Schema Stack

Structured data is mandatory on every client site. It is not optional and not a post-launch task. Add schema during the build, validate before delivery, fix all errors before launch.

**Schema by page type:**

| Page type | Required schema types |
|---|---|
| Every page | `Organization` · `BreadcrumbList` |
| Homepage | `LocalBusiness` (or trade sub-type — see below) |
| Service page | `Service` · `FAQPage` (if FAQ section present) |
| Service-area page | `LocalBusiness` with `areaServed` · `Service` |
| Blog post | `BlogPosting` · `FAQPage` (if FAQ section) · `HowTo` (if step-by-step guide) |
| Contact page | `ContactPage` |
| About page | `Organization` (expanded with `foundingDate`, `numberOfEmployees` if known) |

**Trade-specific LocalBusiness sub-types (use the most specific match):**

| Trade | Schema sub-type |
|---|---|
| Plumbing | `Plumber` |
| HVAC | `HVACBusiness` |
| Electrical | `Electrician` |
| Roofing | `RoofingContractor` |
| General contracting | `GeneralContractor` |
| Landscaping / lawn | `LandscapeService` |
| Painting | `Painter` |
| Pool service | `PoolService` |
| Pest control | `PestControlService` |
| Cleaning | `HousePainter` → use `HomeAndConstructionBusiness` if no exact match |

Always use the most specific sub-type available. `LocalBusiness` alone is a fallback, not a first choice.

**FAQPage — when to add it:**
Add `FAQPage` JSON-LD whenever a page has a Q&A section with 2+ questions. Each question must have a corresponding `acceptedAnswer`. Add it to:
- Any service page with an FAQ accordion
- Any blog post with a FAQ section
- The homepage if it has a "Common Questions" or "FAQ" block

**HowTo — when to add it:**
Add `HowTo` JSON-LD whenever a page walks through numbered or sequential steps. This is the highest-value schema for featured snippet capture on how-to queries. Add it to:
- Blog posts structured as step-by-step guides (e.g., "How to get Google reviews", "How to choose an HVAC contractor")
- Service pages that explain a multi-step process

**Featured snippet implementation — mandatory on blog posts and service pages:**
Featured snippets are captured by content structure, not just schema. Both elements are required:

1. **Question-format headings:** Phrase H2s and H3s as questions where the page is targeting informational queries (e.g., "How long does a roof replacement take?" not "Roof Replacement Timeline")
2. **Direct answer paragraph:** The first paragraph after a question-format heading must be a direct, complete answer in 40–60 words. No preamble, no "it depends" opener — answer first.
3. **Schema confirms the structure:** `FAQPage` or `HowTo` schema should mirror what the content already says. Do not add schema for Q&A that doesn't exist in the visible HTML.

**Validation — mandatory before launch:**
- Validate every page's schema at `https://validator.schema.org/` — zero errors required
- Warnings are acceptable if they are about optional recommended fields
- Errors block launch — fix them before the smoke test

---

### Step 11 — Run the Pre-Launch Smoke Test

Before marking any page done, run every item in this checklist:

**Performance:**
- [ ] LCP < 2.5s on mobile — PageSpeed Insights, Slow 4G throttling (must be green, not orange or red)
- [ ] CLS < 0.1
- [ ] INP < 200ms
- [ ] All images are WebP format (no JPG or PNG in production except favicon/OG image)
- [ ] Hero/LCP image has `loading="eager" fetchpriority="high"` + `<link rel="preload">` in `<head>`
- [ ] All non-hero images have `loading="lazy"`
- [ ] Every `<img>` has explicit `width` and `height` attributes
- [ ] Fonts are self-hosted from `/fonts/` — no `fonts.googleapis.com` link in any page
- [ ] Every `<script src>` has `defer` attribute
- [ ] Every page has a `<main>` landmark element
- [ ] Total homepage payload < 1 MB (check Network tab in DevTools)

**UX:**
- [ ] Phone number in header, click-to-call works on mobile
- [ ] Floating call button present on mobile
- [ ] Lead form max 4 fields, submit button has action label
- [ ] Above-fold contains: headline + contact method + trust signal
- [ ] Trust strip present below hero
- [ ] Nav has max 5 items + phone number

**SEO:**
- [ ] Unique `<title>` tag per page — 60 chars max; count before finalising, never eyeball it
- [ ] Unique meta description per page — 160 chars max; count before finalising
- [ ] H1 present exactly once per page
- [ ] Every `<img>` has an `alt` attribute — descriptive text or `alt=""` for decorative only; zero bare `<img src>` tags
- [ ] `sitemap.xml` present at site root; every URL uses the live domain — grep for any non-live domain before delivery: `grep -v "[clientdomain].com" sitemap.xml`
- [ ] `robots.txt` present at site root with `Sitemap:` directive pointing to the live sitemap URL
- [ ] Canonical tag on every page
- [ ] Any dev, staging, or internal HTML file (not in sitemap, not in nav) has `<meta name="robots" content="noindex, follow">` — add at file creation time

**Schema (must pass `validator.schema.org` with 0 errors before launch):**
- [ ] `Organization` schema on every page
- [ ] `BreadcrumbList` schema on every page (except homepage)
- [ ] `LocalBusiness` (or trade sub-type) on homepage — use most specific sub-type (Plumber, HVACBusiness, etc.)
- [ ] `Service` schema on every service page
- [ ] `LocalBusiness` + `areaServed` on every service-area page
- [ ] `FAQPage` schema on any page with a visible Q&A section (2+ questions)
- [ ] `HowTo` schema on any blog post or page structured as a step-by-step guide
- [ ] `BlogPosting` schema on every blog post
- [ ] All schema validated at `https://validator.schema.org/` — zero errors
- [ ] Question-format H2s present on pages targeting informational queries
- [ ] Direct 40–60 word answer paragraph immediately follows each question-format heading

**Copy Quality — Vale (mechanical gate):**
- [ ] `vale --config=.vale-client.ini [client-source-dir]` returns 0 errors
- [ ] Lantech/Delivery rule passed — no stale delivery time claims
- [ ] Lantech/Pricing rule passed — no stale tier names
- [ ] Lantech/BannedPhrases passed — no agency jargon
- [ ] Lantech/Substitutions passed — consistent terminology
- [ ] Lantech/WeakCTAs passed — no "Submit", "Click Here", "Learn More", "Contact Us" as CTA labels
- [ ] proselint.Hedging passed — no hedging language weakening claims
- [ ] Client/Vocab passed — no off-brand client terms

**Copy Quality — Layer 2 manual checklist (judgment gate):**
- [ ] No "We" sentence openers — sentences restructured to lead with client or outcome
- [ ] No dangling modifiers — opening phrases modify the correct grammatical subject
- [ ] No ambiguous pronoun antecedents — every "he/she/it/they" has one clear referent
- [ ] No incomplete comparisons — "better/faster/cheaper" followed by "than [something specific]"
- [ ] AIDA structure intact — each page section moves reader: Attention → Interest → Desire → Action
- [ ] Headline passes Ogilvy test — promises benefit, states problem, delivers news, or makes specific claim
- [ ] Hero passes 5-second test — who/what/for whom answerable without scrolling
- [ ] Every CTA names a specific outcome — passes the stand-alone read test
- [ ] No accidental sentence fragments in body paragraphs
- [ ] All sentences under 25 words — nothing over 35 words
- [ ] Awareness stage matches the audience — copy written for cold traffic unless client confirms otherwise

**Accessibility (WCAG 2.1 AA baseline — legal standard under the ADA):**
- [ ] `<html>` tag has `lang="en"` attribute
- [ ] Every image has a descriptive `alt` attribute — decorative-only images use `alt=""`
- [ ] Every form field has an associated `<label>` — never rely on `placeholder` alone as a label
- [ ] Heading hierarchy is intact — H1 → H2 → H3, no levels skipped (e.g., no H1 → H3)
- [ ] All interactive elements (buttons, links, form fields) have a visible focus state — `outline` not suppressed in CSS
- [ ] No information conveyed by color alone — e.g., required fields need a text marker ("*"), not just a red border
- [ ] Click-to-call links have descriptive text — `<a href="tel:...">Call (239) 555-0101</a>`, not just the number
- [ ] Color contrast passes WCAG AA: 4.5:1 ratio for body text, 3:1 for large text (18px+ or 14px+ bold) — check at [webaim.org/resources/contrastchecker](https://webaim.org/resources/contrastchecker)

**Technical:**
- [ ] All nav links resolve (no 404s)
- [ ] Contact form submits without error
- [ ] No console errors on load
- [ ] Site loads correctly at 375px (mobile) and 1280px (desktop)
- [ ] All internal links are relative, not absolute

---

## Required Outputs

Before closing any build, confirm every item below exists:

- [ ] All pages pass the Step 11 pre-launch smoke test
- [ ] Real photos used (or placeholder flag added to handover notes)
- [ ] Dual visitor architecture confirmed on Home and all Service pages
- [ ] Above-fold formula confirmed on every page
- [ ] Core Web Vitals pass on all pages (PageSpeed score ≥ 80)
- [ ] Click-to-call confirmed on mobile (floating button + header)
- [ ] Trust strip present on every page
- [ ] Service-area pages built (Lead Machine+ only)
- [ ] Full schema stack implemented per Step 10 — all required types present for each page type
- [ ] All schema validated at `validator.schema.org` — zero errors across every page
- [ ] Accessibility baseline passes (all 8 WCAG checks in Step 11)
- [ ] Handover notes document any placeholders or deferred items

---

## Edge Cases

**Client has no photos:**
Use placeholder images (marked with a border and label in dev). Add a note in the handover package: "Replace placeholder images with real photos of your team and trucks within 30 days for best results." Do not launch without flagging this to the client.

**Emergency service flag is unclear:**
Ask during the discovery call: "Do you offer emergency or same-day service?" If yes, add the emergency messaging layer (24-hour availability, prominent phone placement). If no, omit it — do not add "24-hour" messaging for a business that isn't available 24 hours.

**Client is on Local Presence tier but wants SEO content:**
Local Presence includes on-page SEO setup but not ongoing content creation. Explain that service-area pages and monthly blog posts are part of Lead Machine ($1,997/mo). If they want to upgrade, refer to `workflows/project.md` for how to handle a tier change mid-engagement.

**Page fails Core Web Vitals after optimization:**
If a page still fails after image compression and dimension fixes, check for render-blocking scripts. Move all non-critical JS to `defer` or `async`. If a third-party widget (chat, booking) is causing CLS, lazy-load it. If LCP is still slow after all fixes, escalate — do not launch a page with failing Core Web Vitals.

**Client offers financing:**
Add a financing band section between services and reviews. Only build it when the client's embed code or apply link is in hand (confirmed in `12-onboarding-checklist.md` Section E). If the asset is pending at build time, leave a `<!-- FINANCING BAND: insert embed code here when received -->` comment and flag it in the handover notes. Common providers: Hearth (embed widget), GreenSky (apply link), Wisetack (embed widget), Service Finance (apply link), Synchrony Home (apply link). The client must be enrolled with the lender before you can receive the embed code.

**Service area is too broad (nationwide client):**
Build SAPs only for the 5 highest-value target cities in the first month. Prioritize by search volume × competition. Expand coverage monthly as part of the Lead Machine or Market Leader retainer.
