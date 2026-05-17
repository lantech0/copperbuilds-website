# Client Onboarding Checklist — Internal Use Only

> **For Luis only.** Run this before triggering the build in `workflows/project.md` Step 6.
> Every item must be checked before a single line of code is written.
> Source of answers: `02-onboarding-questionnaire.md` (completed by client)

**Client:** ___________________________
**Package:** [ ] Starter &nbsp; [ ] Growth &nbsp; [ ] Pro
**Date checklist completed:** ___________________________

---

## SECTION A — Contract & Payment

- [ ] Service agreement (`03-service-agreement.md`) signed and returned
- [ ] Invoice (`04-invoice.html`) paid — `PAYMENT-CONFIRMED.md` added to client folder
- [ ] Package and price confirmed — matches what was discussed on the discovery call
- [ ] Delivery deadline confirmed and noted in client folder

---

## SECTION B — Business Information

All of the following must be filled in `06-client-brief.md` before building starts:

- [ ] Exact business name (as it should appear on the site)
- [ ] What the business does — 2–3 sentence description in their words
- [ ] Service area: city, state, and all service locations
- [ ] Business address (street, city, state, ZIP)
- [ ] Business phone number
- [ ] Business email for the contact form
- [ ] Business hours (Mon–Fri, Sat, Sun, closed days)
- [ ] Years in business
- [ ] Google Business Profile URL (if they have one)
- [ ] Top 3 services to highlight
- [ ] Ideal customer description
- [ ] #1 differentiator / selling point
- [ ] Top 2–3 local competitors

---

## SECTION C — Brand Assets

- [ ] Logo: &nbsp; [ ] Received (PNG/SVG) &nbsp; [ ] Not provided — build without logo &nbsp; [ ] Needs to be created
- [ ] Brand colors: &nbsp; [ ] Received (hex codes: _________ ) &nbsp; [ ] Not provided — choose appropriate colors
- [ ] Font preference: &nbsp; [ ] Received (_________ ) &nbsp; [ ] Not provided — use judgment
- [ ] Style reference websites: &nbsp; [ ] Received &nbsp; [ ] Not provided
- [ ] Existing brand guide / marketing materials: &nbsp; [ ] Received &nbsp; [ ] None

**Design don'ts from client** (from Q15 — elements to avoid):
```
[paste client's answer here]
```

---

## SECTION D — Content & Media

- [ ] Photos: &nbsp; [ ] Client sending ✉️ &nbsp; [ ] Stock photos approved &nbsp; [ ] Mix (client sending some)
- [ ] Copy: &nbsp; [ ] Lantech writing all &nbsp; [ ] Client providing all &nbsp; [ ] Mix (client writing: _________ )
- [ ] Testimonials: &nbsp; [ ] Provided (paste in brief) &nbsp; [ ] Pull from Google Reviews &nbsp; [ ] None
- [ ] Founder / team bio: &nbsp; [ ] Provided &nbsp; [ ] Lantech writing (info in questionnaire)
- [ ] Brochures / existing content to reference: &nbsp; [ ] Received &nbsp; [ ] None

**Photos expected from client:**

Send the client this message when requesting photos:
> *"Take photos with your phone in good lighting — horizontal orientation for most shots. Don't worry about professional quality. Authentic beats polished for home service businesses. We'll handle cropping and compression on our end. Send us everything you have and we'll pick the best ones."*

**Universal — all clients, all sectors:**
- [ ] Logo — PNG with transparent background, min 500px wide (SVG preferred; if no logo, note it)
- [ ] Owner headshot — good natural lighting, min 800×800px (used on About page + GBP)
- [ ] Team / crew photo — group shot at job site, shop, or in front of vehicle (if applicable)
- [ ] Branded vehicle / equipment — truck, van, trailer, or equipment with company name visible
- [ ] Crew at work — 2–3 shots of technician/crew actively working on a job (hero images)
- [ ] Completed work — min 3 before/after pairs (before = problem state, after = finished work)
- [ ] Certifications / badges — photo or scan of business license, insurance cert, brand certifications (e.g. GAF, NATE, Carrier dealer logo)

**Sector-specific additions:**

*HVAC:*
- [ ] Installed outdoor condenser unit (clean, branded if possible)
- [ ] Indoor air handler
- [ ] Technician in attic or crawlspace

*Roofing:*
- [ ] Completed roof from the street (full house view)
- [ ] Close-up of shingles / materials
- [ ] Crew on roof with safety gear

*Plumbing:*
- [ ] Technician under sink, at pipe, or with tools
- [ ] Water heater install or replacement shot

*Landscaping:*
- [ ] Seasonal work in progress (mowing, mulching, edging, trimming)
- [ ] Equipment / crew with trailers and mowers

*Pool Service:*
- [ ] Crystal-clear pool — the money shot
- [ ] Technician at poolside with test kit
- [ ] Pump or filter work in progress

*Electrical:*
- [ ] Panel work (before/after)
- [ ] Completed lighting or outlet installation

**GBP photos (Growth / Pro packages only):**
- [ ] Exterior — from the street showing building/signage (home-based = branded vehicle from street; required by Google)
- [ ] Interior — office or shop interior (optional for home services)
- [ ] Cover photo — landscape orientation, min 1080×608px (main GBP banner)
- [ ] At-work shot — separate from website version (GBP displays these in its own "At work" category)

*GBP format note: JPG or PNG, minimum 720×720px, max 5MB per photo.*

**Minimum viable set to start the build** (if client can only send a few before kickoff):
- [ ] Logo (or confirm building without one)
- [ ] Owner headshot
- [ ] Branded vehicle photo
- [ ] 1–2 crew-at-work shots
- [ ] 2–3 completed job photos

*Remaining photos can be added during the 30-day support window or first maintenance cycle — do not hold up the build for them.*

**Tracking:**
- [ ] All photos received (or minimum viable set confirmed)
- [ ] Photos saved to `clients/active/[slug]/assets/photos/`
- [ ] Stock photos approved for any gaps

---

## SECTION E — Website Structure

- [ ] Primary CTA confirmed (call / form / booking / other): ___________________________
- [ ] Pages list confirmed and mapped to package:

| Page | Included in Package |
|---|---|
| Home | ✅ all packages |
| Services | ✅ all packages |
| About | ✅ all packages |
| Contact | ✅ all packages |
| [Page 5] | ✅ Growth + Pro |
| [Page 6+] | Pro only |

- [ ] Any special functionality needed? (booking widget, PDF download, map embed): ___________________________
- [ ] Domain: &nbsp; [ ] Client owns it (domain: _________ ) &nbsp; [ ] Needs one — advise client
- [ ] Financing offered? &nbsp; [ ] Yes &nbsp; [ ] No &nbsp; Provider: ___________________________
  - If yes — asset received? &nbsp; [ ] Embed code/widget &nbsp; [ ] Apply link only &nbsp; [ ] Pending (do NOT build financing band until received)
  - Asset saved to `clients/active/[slug]/assets/financing-embed.txt`

---

## SECTION F — SEO Setup

- [ ] Target keywords noted in `06-client-brief.md` (from Q24 — client's own words)
- [ ] Keyword research complete — `_keyword-map.md` created with primary keyword per page
- [ ] GBP optimization: &nbsp; [ ] Included (Growth/Pro) &nbsp; [ ] Not included (Starter)
- [ ] **Google Alerts setup** (Growth/Pro only — set up at onboarding, runs passively throughout retainer):
  - Go to `google.com/alerts` and create two alerts for the client:
    1. `"[exact business name]"` — catches any new web mention of the business
    2. `"[trade] [city] recommendation"` — catches community discussions in the client's market (e.g., `"plumber Cape Coral recommendation"`)
  - Set delivery to: Luis's email, frequency: as-it-happens
  - Confirms the client's community reputation monitoring is live from Day 1 of the retainer
  - [ ] Alert 1 (business name) created
  - [ ] Alert 2 (trade + city) created
- [ ] Existing GA4 property: &nbsp; [ ] Yes (ID: _________ ) &nbsp; [ ] No — set up at launch
- [ ] Existing GSC property: &nbsp; [ ] Yes &nbsp; [ ] No — set up at launch
- [ ] Client Google account email (for analytics access): ___________________________

---

## SECTION G — Communication Preferences

- [ ] Client's preferred contact method: &nbsp; [ ] Email &nbsp; [ ] WhatsApp/text &nbsp; [ ] Other: ___
- [ ] Preview delivery method: email with preview link (standard)
- [ ] Revision feedback method: &nbsp; [ ] Email comments &nbsp; [ ] Call &nbsp; [ ] Other: ___
- [ ] Client knows: 2 revision rounds included, additional rounds $75–150/round

---

## SECTION H — Post-Launch Services

- [ ] Maintenance retainer discussed: &nbsp; [ ] Yes — interested &nbsp; [ ] Yes — not interested &nbsp; [ ] Not discussed
- [ ] If interested: &nbsp; [ ] Basic $99/mo &nbsp; [ ] Standard $199/mo &nbsp; [ ] Pro $299/mo
- [ ] 30-day free support window explained to client

---

## GO / NO-GO DECISION

**Before triggering the build, all of these must be true:**

- [ ] All of Section A checked (contract signed, payment confirmed)
- [ ] All of Section B filled into `06-client-brief.md`
- [ ] All brand assets received or "not provided" decision made
- [ ] Content plan locked (who is writing what)
- [ ] Keyword map created
- [ ] Pages list and primary CTA confirmed
- [ ] Financing: either confirmed "not offered" OR embed code/apply link received and saved

**If any item is unchecked:** send one clarifying email listing exactly what's missing. Do not start the build until resolved.

**Build triggered by:** _________________________ **on:** _________________________
