# GMB Setup & Quick Verification Workflow

## Objective
Set up and verify a Google Business Profile for CopperBuilds or a new client using the GSC instant verification method to skip the 2-week postcard wait.

## Trigger
Run this workflow when:
- Setting up CopperBuilds' own GBP listing
- Onboarding a new client who has no existing Google Business Profile
- A client's GBP listing was suspended or removed and needs to be recreated

## Required Inputs
- [ ] Business name (exact — must match website and schema)
- [ ] Website live and accessible
- [ ] Google account to own the listing (use client's account for client builds)
- [ ] US phone number (client's number for client builds)
- [ ] Business description drafted (750 char max — see Step 5)
- [ ] 5+ photos ready (logo, work samples/photos, workspace)
- [ ] Service area cities/states decided (SAB) or physical address (brick-and-mortar)
- [ ] Google Search Console access for the domain

---

## Steps

### Phase 1 — Pre-Setup (complete before touching GBP)

**Step 1: Verify the domain in Google Search Console**

This unlocks instant verification in GBP — do this first.

1. Go to `search.google.com/search-console`
2. Add property → select **Domain** (not URL prefix) → enter the domain
3. Copy the DNS TXT record provided
4. In Hostinger (or client's host): DNS Zone Editor → Add TXT record → paste value → save
5. Back in GSC → click Verify
6. Wait 15–60 minutes for DNS propagation, then re-verify
7. Confirm: property shows as "Verified" in GSC

> GSC and GBP must use the same Google account. If the client owns the GSC property, use their account throughout.

**Step 2: Prepare the NAP**

Confirm Name, Address/Service Area, Phone is consistent across:
- Website footer
- Contact page
- LocalBusiness schema (run `/seo-schema <url>` if not yet set up)

Any mismatch here will cause citation inconsistencies later. Fix before creating GBP.

---

### Phase 2 — Create the Listing

**Step 3: Create or claim**

1. Go to `business.google.com`
2. Search the exact business name
3. If a ghost/unverified listing appears → **Claim it** (do not create a duplicate)
4. If nothing found → Create new listing

**Step 4: Select business type**

| Client type | Select |
|---|---|
| CopperBuilds (web agency, remote) | Service Area Business |
| Home services (HVAC, plumbing, roofing, electrical) | Service Area Business or Hybrid if office/showroom exists |
| Client with physical storefront | Brick-and-Mortar |

For SABs: hide the address during setup — do not enter a street address that will be shown publicly.

**Step 5: Select categories**

Primary category is the single most important GBP ranking factor (Whitespark 2026, score: 193). Choose carefully — incorrect primary is the #1 negative factor.

**CopperBuilds:**
- Primary: `Web Design Company`
- Secondary: `Digital Marketing Agency` · `Internet Marketing Service` · `Marketing Agency`

**Common client categories:**

| Trade | Primary | Secondary |
|---|---|---|
| HVAC | `HVAC Contractor` | `Air Conditioning Contractor` · `Heating Contractor` |
| Plumbing | `Plumber` | `Drainage Service` · `Water Treatment Supplier` |
| Roofing | `Roofing Contractor` | `Gutter Cleaning Service` · `Siding Contractor` |
| Electrical | `Electrician` | `Lighting Contractor` · `Generator Shop` |
| Landscaping | `Landscaper` | `Lawn Care Service` · `Tree Service` |
| Painting | `Painter` | `House Painter` · `Commercial Painter` |
| General Contractor | `General Contractor` | `Construction Company` · `Home Builder` |

Optimal: 1 primary + up to 4 secondary categories (BrightLocal benchmark).

---

### Phase 3 — Quick Verification

**Step 6: Attempt instant verification via GSC**

1. When the verification screen appears in GBP, look for **"Instant verification"**
2. If it appears → click it → done, verified immediately
3. If it does not appear → proceed to Step 7 (fallback options)

Instant verification appears when: the domain is verified in GSC AND the same Google account owns both GSC and GBP. If it doesn't appear, the accounts are mismatched — resolve that first before trying fallbacks.

**Step 7: Fallback verification (in order)**

1. **Email verification** — if the business has a domain email set up, select this option; code arrives in minutes
2. **Phone verification** — SMS or automated call to the business phone number; fastest if US number available
3. **Video verification** — Google's primary fallback since 2024; record a 30-second video showing:
   - The workspace or office environment
   - Business name visible on screen (website, logo, or document)
   - No storefront required for SABs
   - Upload directly in GBP — reviewed within 5 business days
4. **Postcard** — last resort; 7–14 business days; only use if all above fail

---

### Phase 4 — Profile Optimization (complete within 48h of verification)

**Step 8: Write the business description**

- 750 character maximum; first 250 chars are the most visible in search
- Lead with primary value prop + keyword in the first sentence
- No URLs or phone numbers (Google strips them)
- No promotional language ("best", "#1", "cheapest")

CopperBuilds template:
> *CopperBuilds builds lead-generating websites for home service contractors across the US — HVAC, plumbing, roofing, and electrical. Fast builds, local SEO included, no enterprise bloat.*

Client template structure:
> *[Business name] provides [primary service] for [target customer] in [city/region]. [Key differentiator]. [Trust signal: licensed/insured/years in business]. Call [phone] for a free estimate.*

**Step 9: Add services**

Add each service as a named item with a 300-character description. More services = more keyword coverage in local search.

- CopperBuilds: Website Design · Local SEO · Google Business Profile Setup · Website Maintenance · Lead Generation Websites
- Include relevant keywords naturally in each service description

**Step 10: Upload photos**

| Photo type | Spec | Notes |
|---|---|---|
| Cover photo | 1080×608 | Brand visual or best work sample |
| Profile photo | 250×250 min | Logo only |
| Work samples | Any | Client website screenshots for CopperBuilds; job site photos for trades |
| Workspace/team | Any | Builds trust for SABs with no physical location |

No stock photos — Google detects and devalues them.

**Step 11: Set business hours**

Businesses open at search time rank higher (Whitespark factor #5). Set hours that are accurate and realistic.

- CopperBuilds: set hours that overlap US Eastern mornings (9AM–5PM EST)
- Clients: use their actual operating hours; set special hours for holidays

**Step 12: Set the website link**

Per Sterling Sky Diversity Update: **do NOT link GBP to the page you're trying to rank organically** — it risks suppressing that page's rankings. Link to:
- Homepage (default safe choice)
- A dedicated `/from-google` landing page (best practice — tracks GBP traffic separately)

**Step 13: Set service areas (SABs only)**

- Add up to 20 service area locations
- CopperBuilds: add "United States" or target specific states first
- Clients: primary city + surrounding cities within 15–20 mile service radius

---

### Phase 5 — Go-Live Actions (same session as verification)

**Step 14: Publish first GBP post**

- Post type: What's New
- Include a photo (posts without photos underperform)
- CTA: link to homepage or key service page
- Content: brief intro + primary service + call to action
- Note: What's New posts expire after 7 days — set a recurring reminder to post weekly

**Step 15: Claim supporting profiles (do not skip)**

Do this in the same session while NAP info is fresh. These platforms feed AI search results directly.

| Platform | Why it matters |
|---|---|
| **Bing Places** (`bingplaces.com`) | Powers ChatGPT, Copilot, Alexa — most overlooked |
| **Apple Business Connect** (`register.apple.com/business`) | Usage doubled to 27% of searches (BrightLocal 2026) |
| **Yelp** (`biz.yelp.com`) | Primary ChatGPT local recommendation source |
| **BBB** (`bbb.org/accreditation`) | Trust signal + ChatGPT source + Google uses BBB for business verification |

Use identical NAP across all platforms — any variation creates citation inconsistencies.

---

## Required Outputs

- [ ] GBP listing verified and live (status: "Verified" in business.google.com)
- [ ] All profile fields complete: description, services, hours, website link, service areas, photos
- [ ] First GBP post published with photo and CTA
- [ ] Bing Places claimed and NAP entered
- [ ] Apple Business Connect claimed and NAP entered
- [ ] Yelp business page claimed and NAP entered
- [ ] BBB listing claimed (accreditation optional)
- [ ] GSC property verified for the domain (prerequisite — must exist)
- [ ] NAP identical across GBP, Bing Places, Apple, Yelp, and website footer

---

## Edge Cases

| Scenario | Action |
|---|---|
| Ghost/duplicate listing exists | Claim and merge — never create a second listing for the same business. Report duplicate to Google via the "suggest an edit" flag on the unwanted listing. |
| Instant verification doesn't appear | Check that GSC and GBP use the same Google account. If accounts differ, either transfer GSC ownership or create GBP under the GSC account. |
| Phone verification requires US number but client has none | Use video verification. Record workspace + business name on screen. Upload in GBP. Reviewed within 5 business days. |
| Client already has a GBP but lost access | Use the "request ownership" flow in GBP — Google emails the current owner; if no response within 7 days, ownership transfers. |
| Client has multiple locations | Create one GBP per location. Each listing needs a unique address and phone number. Service areas can overlap. |
| Category not found | Choose the closest match — never leave primary category blank. Submit feedback to Google for missing categories if needed. |
| Listing suspended after verification | Do NOT create a new listing. Submit a reinstatement request via the GBP support form with proof of business legitimacy (website, utility bill, business registration). |
