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
- [ ] Confirmed received (or confirmed using stock)
- [ ] Saved to client folder at `clients/active/[slug]/assets/`

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

---

## SECTION F — SEO Setup

- [ ] Target keywords noted in `06-client-brief.md` (from Q24 — client's own words)
- [ ] Keyword research complete — `_keyword-map.md` created with primary keyword per page
- [ ] GBP optimization: &nbsp; [ ] Included (Growth/Pro) &nbsp; [ ] Not included (Starter)
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

**If any item is unchecked:** send one clarifying email listing exactly what's missing. Do not start the build until resolved.

**Build triggered by:** _________________________ **on:** _________________________
