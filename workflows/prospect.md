# Workflow: CopperBuilds Client Prospecting

**Skill:** `/prospect`
**Saves to:** `projects/prospects/` (local backup) + Google Drive "Lantech Agency → Prospects" folder (ID: `1J8Of3xcIt8ZU0LTuPuafrpXVi4Vl2hQZ`) (primary)

---

## Objective
Find, score, and write personalized outreach for businesses that need a website and digital presence. Deliver a complete Google Sheet with all scored leads, outreach messages, benchmarks, and contact info — nothing missing.

## Required Inputs
- Mode (ask first): Discovery / Ghost
- Sector and location (Discovery) — or let Claude choose the best US market if not specified
- OR specific business name + details (Ghost)
- Volume of leads wanted (Discovery default: 20)

---

## Steps

### Step 1 — Mode Selection
Ask the user which mode before doing anything else:
1. **Discovery** — search Google Maps + multi-source for leads in a sector + location
2. **Ghost** — specific business with zero online presence (no GMB, no website, no Facebook)

### Step 1.5 — Do-Not-Duplicate Check
Before starting research, check `projects/prospects/` for existing files in this sector + location. List all businesses already researched in prior sessions. Record at the top of the output: **"Already researched: [list or None]"**

### Step 1.6 — Lead-First Ordering (Discovery Mode Override)

**Why this exists:** Running keyword research (Step 2.5, Step 4) before confirming real no-website leads exist in the target city risks spending API credits and effort on a market that turns out to be a dead end. In a large, saturated metro, nearly every findable business — even ones surfaced through Craigslist or Nextdoor — already has a website and Facebook page by default; the true target (zero web presence) may only exist in smaller suburbs or less-saturated markets, and you don't know which until you've actually looked.

**Revised order for Discovery mode:**
1. Run Step 5 (Lead Discovery — user-pasted Google Maps results is the primary method, see Step 5) **first**, broadly across the target area (city + surrounding suburbs — see note below on what counts as "the area"), before Step 2, Step 2.5, or Step 4.
2. Run Step 6 (Owner Lookup), Step 6.5 (Contact Info), and Step 7 (Digital Presence Audit) on candidates as you find them, to confirm which are genuinely no-website / zero-presence — not just weak.
3. **Threshold to trigger keyword research:** once **3 confirmed no-website leads** are found within a single city, run Step 2.5 (SERP report) and Step 4 (DataForSEO) for that specific city. Do not run either before this threshold is met. If after a reasonable search pass fewer than 3 are found in the original target city, widen to a named suburb (see below) before concluding the market is a dead end.
4. Step 2 (Area Research) and Step 3 (Gold Standard) still apply, but run **after** the threshold is met, scoped to the city that actually produced the leads — not necessarily the city originally requested.

**Suburb geography note:** a business physically based in a suburb (e.g., Plano, Garland, Mesquite) generally ranks in Google's local map pack for its own city's searches, not the core city's searches (e.g., "HVAC Plano" not "HVAC Dallas"), unless it's explicitly set up as a service-area business covering the core city. Keyword research and outreach stats must be scoped to whichever city the lead is actually based in — do not cite core-city search volume for a suburb-based lead.

**Ghost mode is unaffected** — Ghost mode already starts from a specific known business, so this ordering override does not apply; run Ghost mode's steps in their existing order.

### Step 2 — Area Research (if location not specified)
If the user has no specific location in mind, research the best US market for the sector. Evaluate 3–5 cities and pick the best based on: population, digital adoption gap (% of local businesses without websites), market growth, competition level for web agencies, sector-specific demand reason.

Output an **Area Selection Rationale** — save to Tab 3 of the Google Sheet:
- Area: [City, State]
- Population: [N]
- Why this sector here: [specific market condition]
- Digital adoption gap: [% or description]
- Competition level: [Low / Medium / High]
- Expected lead quality: [Hot/Warm ratio and why]

### Step 2.5 — SERP Visibility Report

**Discovery mode: deferred until Step 1.6's 3-lead threshold is met — do not run this before then.**

Run `/generate-report` for the target trade + city once real no-website leads are confirmed there.

**Why it comes first (once leads are confirmed):** The report pulls live SERP data — who owns Local Pack, which features fire, which competitors appear across every keyword. That data feeds the Gold Standard (Step 3), pitch angles (Step 9.5), and outreach credibility (Step 10).

**Run:** `/generate-report --trade [trade] --city [city] --state [state]`
- No `--domain` flag during prospecting — this is the no-website prospect map mode
- If `/generate-report` was already run for this exact trade+city combination this session: skip the run, use the existing report URL

**Extract from the report after it generates:**
- Top 5 competitors by SERP ownership score → these are your Gold Standard candidates (Step 3)
- Local Pack prevalence % → use as the anchor stat in outreach ("X% of [trade] searches in [city] trigger a Local Pack")
- SERP ownership scores → use in pitch angles (Step 9.5) to show exactly who is dominating and by how much
- Published report URL → save it; use in Step 10 outreach as a credibility leave-behind

**If DataForSEO is unavailable or user declines:** note it and proceed to Step 3 without report data. Flag in the session summary that outreach lacks the report URL.

---

### Step 3 — Gold Standard Research + Sector Benchmark Table
Find the top 1–2 competitors in the sector + location with the strongest digital presence. Record:
- Business name
- Website quality (fast, mobile-friendly, professional?)
- Google Maps rating + review count
- Social media activity (posting frequency, follower count)
- GMB profile completeness (photos, services, Q&A, review responses)
- What they're doing right digitally

Save as **"The Gold Standard"** — referenced by name in every outreach message.

Then produce the **Sector Benchmark Table**:

| Metric | Gold Standard | Avg Local Business | Target Lead Profile |
|--------|---------------|--------------------|---------------------|
| Website | Fast, mobile, modern | Outdated or none | No website / poor |
| Google Rating | 4.5–5.0 stars | 3.5–4.2 | 4.0+ (high demand, low visibility) |
| Review Count | 200+ | 15–60 | Any — gap is digital presence |
| Social Media | Active (weekly+) | Dormant or none | Dormant or none |
| GMB Profile | Fully optimized | Incomplete | Incomplete / missing |

Save Gold Standard + Benchmark Table to Tab 3 of the Google Sheet.

### Step 4 — Keyword Research (Discovery and Ghost)

**Discovery mode: deferred until Step 1.6's 3-lead threshold is met — do not run this before then.** Ghost mode is unaffected (already knows its target city).

DataForSEO charges per call — batch the entire session before calling, not per prospect.

**Before calling DataForSEO:**
1. Collect the sector + location pair for every prospect in this session first
2. Confirm with the user: *"Ready to run keyword research for [N] sector+location combos. One DataForSEO call. Proceed?"*
3. If user declines → fall back to WebSearch or `deep-research` for estimates (free, less precise)

**If approved — one batched call:**
- Batch all sector+location combos into a single request: `"[sector] [location]"` and `"[sector] near me"` variants for every prospect at once
- Pull: monthly search volume, keyword difficulty, CPC per keyword, top 5–10 keywords per combo
- Save raw results to `.tmp/YYYY-MM-DD-dataforseo-prospect-[location].json` immediately after the call
- Do not call again for the same sector+location in the same session — reuse the cached result

**From the results, extract per prospect:**
- Total Monthly Search Traffic = sum of top keyword volumes → save as: *"[N,NNN] people search for [sector] in [location] every month"* — use in outreach
- Top 3 keywords by volume → use in the pitch and in the client brief at build time

Calculate **Total Monthly Search Traffic** = sum of top keywords.
Save as: **"[N,NNN] people search for [sector] in [location] every month."** — use in outreach.

### Step 5 — Lead Discovery (Discovery only)

**Primary method: ask the user to paste the expanded Google Maps results.** This is the method that actually works — proven 2026-07-02 in Dallas, where it found 11 real no-website leads in two pastes after WebSearch-based methods (below) spent dozens of queries and found close to zero. The reason: WebSearch can only surface businesses that are already indexed somewhere on the web, which structurally excludes true zero-presence businesses by definition. Google Maps' own "Website" field is ground truth that no search-engine proxy can substitute for, and Claude has no reliable tool access to browse Maps directly (a plain fetch returns nothing — it's a JS-rendered app; browser automation may not be available or the user may not want to connect it).

**How to run it:**
1. Ask the user: "Can you open Google Maps, search '[sector] in [location]', click through to the expanded results list (not just the 3-pack), and paste the results here?"
2. From the pasted text, extract every entry that does **not** show a "Website" link (only "Directions" and/or "Schedule") — these are the real no-website candidates.
3. Note name, rating, review count, phone, years in business, and category for each from the pasted text directly — this is often the *only* place that data exists for a truly zero-presence business, so capture it now rather than assuming it can be re-verified later.
4. Deprioritize entries with no reviews and no phone number — too weak to verify or contact.
5. Cross-check each candidate via WebSearch (`"[business name]" Yelp BBB website`) before treating it as confirmed — the Maps card can occasionally be stale, and this same query pattern reliably confirms or refutes real website presence (proven both directions this session: correctly found real sites for businesses wrongly assumed to have none, and correctly confirmed zero presence for the genuine no-website leads).

**Fallback method (only if the user can't paste Maps results): WebSearch-based sources below.** These are unreliable for *discovering* true zero-presence leads (they mostly resurface businesses that already have a site) but remain useful for supplementary research — verifying a specific named lead, or finding Gold Standard competitor detail.

| Source | How to use | Best for |
|--------|-----------|----------|
| **Yelp** | Search by category + city; filter no-website listings | All sectors |
| **Angi / HomeAdvisor / Thumbtack** | Browse provider listings by trade + city | HVAC, plumbing, roofing, electrical, landscaping |
| **BBB (bbb.org)** | Search by industry + state/city; cross-check for website | Established businesses — high close rate |
| **Chamber of Commerce directories** | Find city chamber → member list → audit each for website | Local retail, professional services |
| **Craigslist Services** | Browse services section for target city | Listings expire within days — treat any details found as unverifiable soon after; low reliability |
| **Nextdoor Business** | Browse local business listings by city | Home services, retail — but most Nextdoor-recommended businesses already have a site, proven this session |
| **Google "[sector] in [city]" listicles** | Click every business in roundup articles; audit web presence | Pre-vetted, reputation-verified leads |
| **Local Facebook Groups** | "[City] Small Businesses" — businesses posting via phone/DM only | Ghost leads with zero web presence |

Collect same fields as the Maps method above. Mark source per lead (e.g. `Source: Yelp` vs `Source: Google Maps (user-pasted)`).

---

### Data Reliability Notes (learned 2026-07-02, apply throughout Steps 5–7)

- **DataForSEO's `local_pack` `domain`/`url` fields are NOT a reliable website-presence signal.** They reflect where that SERP entry's link goes (often a Google-hosted redirect), not the business's actual configured GBP "Website" field. Two real leads were wrongly marked "no website" this way before being corrected. Use the WebSearch `"[name]" Yelp BBB website` cross-check or the Maps card's own "Website" field instead.
- **WebSearch's AI-generated summary can state an unsourced phone-number-to-business match with no actual citation behind it.** This happened twice for the same number in one session, both times unverifiable. Treat any phone/business identity claim from a WebSearch summary as unconfirmed unless a specific source URL backs it directly.
- **WebFetch cannot read Google Maps** — it returns an empty shell (confirmed by direct test). Maps requires a rendered browser or the user's own manual check.

### Step 6 — Owner Name Lookup
For each lead, search in order:
1. Google: `"[business name]" "[location]" owner` or `founder`
2. Facebook page → About section
3. LinkedIn: business name + location + owner/founder
4. Google Maps — owner responses to reviews
5. Instagram bio

Record: ✅ Found / ⚠️ First name only / ❌ Not found (use "Hi [Business Name] Team")

### Step 6.5 — Contact Info Collection
For each lead, collect ALL of the following (required for outreach):
- **Email address** — website /contact, /about, footer. Record exact or "Find on [URL]/contact"
- **Facebook page URL** — full URL or "None found"
- **Instagram profile URL** — full URL or "None found"
- **LinkedIn page URL** — company page URL or "None found"
- **Phone number** — from GMB if not already collected

Never leave a field blank. "None found" is a valid entry.

### Step 7 — Digital Presence Audit
For each lead, grade each channel:
- **Website:** ❌ None / ⚠️ Poor (outdated, not mobile, no CTA) / ✅ Decent
- **Facebook:** ❌ None / ⚠️ Dormant (1–3 months) or Dead (3+ months) / ✅ Active
- **Instagram:** same grades as Facebook
- **LinkedIn:** ❌ No page / ✅ Has company page
- **GMB:** ❌ Missing / ⚠️ Incomplete / ✅ Optimized

**Service Area Capture — check these sources in order, stop when you have enough cities:**

| Source | Where to look | What to grab |
|--------|--------------|--------------|
| **GMB** | Profile → "Service area" field | Every city listed |
| **GMB reviews** | 10 most recent reviews | Any city/neighborhood mentioned by customers |
| **Yelp** | Profile → "Areas Served" or "Location & Hours" | Listed service cities |
| **Angi / HomeAdvisor** | Provider profile → service area section | Explicit radius or city list |
| **Thumbtack** | Pro profile → "Serves" field | Exact radius they set |
| **Facebook About tab** | Business Page → About → "Areas Served" | Listed cities |
| **Houzz** | Pro profile → "Serves" | City list (contractors/remodelers) |
| **BBB** | Business listing → service area | Address + any listed coverage |

Combine all sources → deduplicate → record as comma-separated city list in `Service Area`.

Count total unique cities → assign `Est. Tier`:
   - 1–3 cities → **Local Presence** ($997/mo)
   - 4–8 cities → **Lead Machine** ($1,997/mo)
   - 9–20 cities → **Market Leader** ($3,497/mo)
   - Can't determine after checking all sources → **Unknown** (note in cell)

Use `Est. Tier` in the pitch angle and outreach — naming their plan tier shows you already understand their market scope before the first call.

### Step 8 — Lead Scoring
Score each lead out of 100 using the scoring table in `/prospect`. Sort by score.
- 🔥 Hot (70–100) — no website, no social. Go hard.
- ⚡ Warm (40–69) — poor website or dormant social. Easy sell.
- 🌱 Cold (under 40) — decent presence. Lower priority.

**Est. Tier bonus — add to base score after digital presence scoring:**
- Market Leader potential (9–20 cities) → **+15 pts** — large coverage, high contract value
- Lead Machine potential (4–8 cities) → **+10 pts** — solid multi-city operator
- Local Presence (1–3 cities) → **+5 pts** — standard single-area business
- Unknown → **+0 pts**

A business with a good digital presence but large service area can still be Hot. A single-city ghost lead stays warm unless gaps are severe.

**Always show the scoring breakdown — point-by-point, not just the total:**
```
No website (+40) | No Facebook (+20) | No Instagram (+15) | High rating 4.5★ (+5) | GMB incomplete (+5) | Lead Machine tier (+10) = 95
```

### Step 9 — Revenue Opportunity Calculation
For each lead, **always show the full formula — not just the final number:**
```
([total reviews] ÷ [years in biz] ÷ 12) × 75 = [Z] clients/mo
[Z] × $[avg transaction value] = $[monthly revenue]/mo
$[monthly revenue] × 30% = $[revenue opportunity]/mo   (Discovery Mode)
$[monthly revenue] × 40% = $[revenue opportunity]/mo   (Ghost Mode — starting from zero)
```

### Step 9.5 — Pitch Angle
For every Hot and Warm lead, write a Pitch Angle before writing outreach. This is 3–5 sentences of internal reasoning:
- What specific gap this business has
- What the Gold Standard competitor is earning/doing that this lead is missing
- Why this lead is a strong target right now

This is NOT the outreach message. It is the thinking that makes the message specific and non-generic. Write the Pitch Angle first, then write outreach from it.

### Step 10 — Outreach Message Generation
For every Hot and Warm lead, generate all 3 messages:
- **Template A** — Cold Email (with subject line)
- **Template B** — Facebook/Instagram DM
- **Template C** — LinkedIn Message

Rules:
- Use owner name if found
- Reference Gold Standard by exact name
- Include exact revenue number and search volume
- Mention the specific digital gap (no website, dormant social, incomplete GMB)
- **Include the SERP report URL** (from Step 2.5) as a credibility signal — frame it as: "I ran an analysis of [trade] businesses in [city] — here's what the data shows: [URL]". Only include if the report was generated this session; never fabricate a URL.
- **Reference their service area** — name how many cities they cover; frame the gap as lost leads across all of them, not just one city (e.g. "you serve 6 cities — that's [N × search volume] people a month who can't find you")
- **Name their tier** only if it makes the pitch stronger; never lead with price — use it to show you've done your homework (e.g. "businesses your size typically need X city pages to show up where their customers search")
- No price in message 1
- Low-friction CTA — one question or a 15-min call offer, nothing more
- Sign as: **CopperBuilds | copperbuilds.com**
- Delivery claim: **14 days** (never "48–72 hours" — matches pricing page)

### Step 11 — Save Output

#### Primary Output: Google Sheet
Create a new Google Sheet in "Lantech Agency → Prospects" Drive folder (ID: `1J8Of3xcIt8ZU0LTuPuafrpXVi4Vl2hQZ`). Name: `[Sector] [Location] — Prospect Tracker [YYYY-MM-DD]`

**Tab 1: Leads** (one row per lead)
`#` | `Business Name` | `Score` | `Scoring Breakdown` | `Tier` | `Sector` | `Owner` | `Phone` | `Email` | `Website` | `Website Grade` | `Google Rating` | `Reviews` | `Yrs in Biz` | `Facebook` | `Facebook URL` | `Instagram` | `Instagram URL` | `LinkedIn URL` | `GMB Status` | `Service Area` | `Est. Tier` | `Rev Opp/mo` | `Revenue Calculation` | `Outreach Sent` | `Replied` | `Call Booked` | `Closed` | `Notes` | `Pitch Angle` | `Address` | `Source`

**Tab 2: Outreach Messages** (3 rows per lead: Email / FB DM / LinkedIn)
`#` | `Business Name` | `Tier` | `Template` | `Email Subject` | `Message`

**Tab 3: Benchmarks & Gold Standards**
- Area Selection Rationale
- Gold Standard profile
- Sector Benchmark Table
- Keyword Traffic Summary
- Session summary (date, totals, total revenue opportunity, priority outreach order)
- Do-not-duplicate list

**Formatting (non-negotiable):**
- Header rows: `#212121` background + white bold text
- HOT rows: `#FFE0E0` (light red)
- WARM rows: `#FFFAD2` (light yellow)

#### Local Backup
Save `.md` file to `projects/prospects/[mode]-[sector]-[location]-[date].md`

### Step 12 — Session Summary
Display in chat: sector, location, date, totals (Hot/Warm/Cold), total revenue opportunity, Google Sheet link, local backup path, priority outreach order (Hot leads ranked by revenue opportunity).

---

## Required Outputs — Claude MUST produce ALL of these before finishing

- [ ] Do-not-duplicate check completed — prior leads listed (or "None")
- [ ] Area Selection Rationale written (if Claude chose the area)
- [ ] Gold Standard profile (name, website, GMB, social, what they do right)
- [ ] Sector Benchmark Table (Gold Standard vs. avg local vs. target lead profile)
- [ ] Keyword traffic summary table (total monthly searches calculated)
- [ ] For every lead: score + tier + **scoring breakdown (point-by-point)**
- [ ] For every lead: owner lookup result (✅ / ⚠️ / ❌)
- [ ] For every lead: contact info (email, Facebook URL, Instagram URL, LinkedIn URL)
- [ ] For every lead: full digital presence audit (Website, Facebook, Instagram, LinkedIn, GMB)
- [ ] For every lead with a GMB: `Service Area` (city list from GMB + reviews) and `Est. Tier` recorded
- [ ] For every HOT/WARM lead: **Pitch Angle** (3–5 sentences, specific to this lead)
- [ ] For every HOT/WARM lead: **revenue calculation shown as full formula**
- [ ] For every HOT/WARM lead: 3 outreach messages (Email with subject + DM + LinkedIn)
- [ ] Google Sheet created in Drive folder with all 3 tabs + correct formatting
- [ ] Local `.md` backup saved to `projects/prospects/`
- [ ] Session summary displayed in chat with Google Sheet link

**Call Prep Cheat Sheet** (triggered separately when a lead books a call):
- [ ] Full HTML cheat sheet saved to `projects/prospects/cheatsheets/[business-slug]-cheatsheet.html`

---

## Edge Cases
- Owner name not found after 3 searches → use "Hi [Business Name] Team", mark ❌
- Email not publicly listed → note "Find on [website]/contact" — never leave blank
- Business has partial presence (Ghost mode) → note what exists, adjust outreach angle
- `seo-dataforseo` unavailable → fall back to WebSearch or `deep-research` for keyword estimates
- Paid API calls needed → check with user before running
- No Hot leads found via search → flag prominently; Hot leads require direct Google Maps browsing (zero-presence businesses are invisible to search tools)

---

## Handoff
When a lead agrees to a call → run `workflows/discovery-call.md`. Use `clients/templates/07-discovery-call-script.md` for the call script and pre-call prep.
When a lead closes on the call → run `workflows/project.md` to create the client folder and start onboarding.
