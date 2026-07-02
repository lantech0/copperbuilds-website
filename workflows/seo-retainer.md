# Workflow: Monthly SEO Retainer Execution

**Triggered by:** Start of each calendar month for any client on Local Presence, Lead Machine, or Market Leader
**Handoff from:** `workflows/post-launch.md` (once 30-day window closes and client converts to retainer)
**Handoff to:** `workflows/monthly-report.md` (end of month — work log and data collected here feed the report)

---

## Objective

Execute all monthly SEO retainer deliverables for a client, collect the assets and information needed from the client, and log everything so the monthly report can be generated accurately.

---

## Trigger

Run at the start of each calendar month for every active retainer client, or when the user says "run retainer for [client]" or "what do I need to do for [client] this month."

---

## Required Inputs

Before starting, confirm these exist:

- [ ] Client folder at `clients/active/[slug]/`
- [ ] `client.env` — for business info, package tier, cities, services
- [ ] `seo-brief.md` — for keyword targets, blog topic formula, action plan
- [ ] `06-client-brief.md` — for USPs, brand voice notes, client preferences
- [ ] `_keyword-map.md` — for current ranking targets (used in monthly-report.md)
- [ ] `maintenance-log.md` — to log this month's work (create if first month)
- [ ] Client's package tier confirmed: **Local Presence / Lead Machine / Market Leader**

Read `client.env` to confirm the tier — it drives which steps below apply.

---

## Step 1 — Client Asset Checklist (Do This First, Every Tier)

Before executing any tasks, identify what you need from the client this month. Check each item — if it's missing and needed for this month's work, flag it to Luis to request from the client.

### Photos (needed every month for all tiers)

- [ ] **2–4 job site photos from recent work** — for GBP posts; phone photos are fine
  - What makes a good job photo: clear before/after, identifiable trade work (not just a truck), shot at the job location
  - If client hasn't sent any: flag to Luis — GBP posts this month will use older photos or stock; note it in the log
- [ ] **Short video clip** (15–60 seconds) — job walkthrough, before/after sequence, or a quick team intro. Google weights video above photos in 2026. Phone video is fine. Even one clip per month makes a difference.
- [ ] **Team/crew photo** (request quarterly, not every month) — refreshes the GBP profile and About page
- [ ] **Any new equipment or vehicle photos** — useful for GBP and social proof on the site

### Business Updates (check every month)

- [ ] Any change to **hours** (holiday closures, extended summer hours, etc.)
- [ ] Any change to **services** — new service added, old one dropped, pricing changed
- [ ] Any change to **contact info** — new phone, new email, address change
- [ ] Any **active promotion or seasonal offer** coming up this month (e.g., "Spring HVAC tune-up special", "Free drain inspection in June")
- [ ] Any **awards, certifications, or press mentions** received — these go on the site and GBP

### Blog / Content Inputs (Lead Machine and Market Leader only)

For each blog post this month, collect at least one of these from the client:
- [ ] **A specific job story** — what was the problem, what did they find when they got there, what was the fix, what was the outcome? Even 3 sentences is enough to build a post from.
- [ ] **A common customer question** they heard this month — becomes the basis of a FAQ or how-to post
- [ ] **A before/after photo with context** — becomes the centerpiece of a transformation or case study post

If the client can't provide job stories: use the blog topic formula from `seo-brief.md` (pricing guides, how-to explainers, hiring guides) — these don't require client input.

### Review Inputs (all tiers)

- [ ] **New customers from the past month** — names and phone numbers (or confirmation that post-job SMS review requests were sent via the review workflow)
- [ ] Any **negative review** received — flag to Luis immediately for a response strategy; do not respond without Luis seeing it first

---

## Step 1.5 — Market Leader Only: LSA Setup (First Month)

> **⚠️ PARKED — Do not execute.** LSA is on standby — quote case by case only. This block is kept for reference when a client specifically requests LSA. Do not include LSA in any retainer proposal or service agreement unless the client asks and Luis approves the quote.

### What LSA Is

Google Local Services Ads place the client at the very top of Google search results — above regular Google Ads and organic results — with a **"Google Verified" blue checkmark** (the old "Google Guaranteed" green badge was retired October 20, 2025; the $2,000 money-back guarantee was discontinued November 7, 2025). The checkmark tells searchers the business passed Google's license, insurance, and background checks. The client pays Google **per verified lead** (a connected phone call or message for the correct service and area), not per click. Budget is controlled by the client via a weekly cap inside the LSA dashboard. All LSA management is at `ads.google.com/localservices` — the mobile app was discontinued January 6, 2025.

**Billing — tell the client this before going live:**
LSA ad spend is charged directly to the client's Google account. It is NOT included in CopperBuilds' $3,497/month fee. CopperBuilds' fee covers managing the profile, monitoring leads, and flagging invalid charges. The client funds and controls their own ad budget. Include this explicitly in the service agreement before the client signs. Log the conversation in `maintenance-log.md` under "LSA billing explained — [date]."

A suggested message to send the client:
> "Your LSA ad spend is billed directly by Google — separate from your CopperBuilds retainer. You set the weekly budget and Google charges you per lead received. We manage the profile and flag invalid leads on your behalf. A good starting budget is $150–250/week. We can adjust it up or down once we see lead quality and volume in the first month."

---

### Step-by-Step: Getting the Client Google Verified

Work through these steps in order. Log completion of each in `maintenance-log.md`.

- [ ] **Confirm the client has a Google account** — they need one to access the LSA dashboard. Help them create one if not.
- [ ] **Verify GBP is linked, verified, and in good standing** — a suspended or unverified GBP pauses all LSA ad delivery immediately. Fix any GBP issues before starting the LSA application.
  - **Fast path:** if the GBP listing and GSC property are both under the same Google Account, use GSC instant verification — no postcard or phone call needed. Full steps in `workflows/analytics-setup.md` Part D.
- [ ] **Open the LSA application** — go to `ads.google.com/localservices` and start the setup for the client's business.
- [ ] **Select the correct business category** — choose the primary trade (Plumber, HVAC Technician, Electrician, Roofer, Landscaper, etc.). The category determines which verification documents Google requires.
- [ ] **Upload the business license** — a copy of the contractor's active state or local trade license. The name on the license must match the business name exactly.
- [ ] **Upload proof of insurance** — general liability certificate at minimum; workers' comp is also required if the business has employees. Get these from the client before starting the application.
- [ ] **Complete the background check** — Google uses a third-party provider (Evident). The business owner and any individuals listed on the account must pass. Google initiates this — the client receives an email with instructions.
- [ ] **Set the service area** — enter every city and zip code the client wants to receive leads from. Keep it tight. Overly broad areas dilute impression share and attract out-of-area calls.
- [ ] **Set business hours** — leads only arrive during the hours listed. If the client takes emergency calls 24/7, mark it accordingly.
- [ ] **Verify the phone number** — must match the number on the client's website and GBP exactly (NAP consistency). LSA calls go to this number.
- [ ] **Set the opening weekly budget** — start at $150–250/week for a mid-size market, $300–500/week for a competitive metro. Remind the client this is their Google spend, not CopperBuilds' fee.
- [ ] **Submit and wait for Google approval** — typically 1–5 business days after all documents are verified. Log the submission date.
- [ ] **Confirm the badge is live** — once approved, search the client's primary keyword in Google and confirm the Google Verified blue checkmark appears at the top. Screenshot it and send to the client. Tell the client: "This checkmark means Google confirmed your license, insurance, and background check — it's what searchers see when they decide who to call."

---

## Step 2 — Week-by-Week Execution

Work through the tasks for the client's package tier. All three tiers share the same calendar structure — the tasks differ by tier.

---

### Week 1 — Setup and GBP

**All tiers:**

- [ ] **GBP post #1 of the month** — publish using photos collected in Step 1
  - Post types that work: job spotlight (photo + what was done + city + call to action), seasonal offer, quick tip relevant to the trade
  - Always include: the city name, the service performed, a CTA ("Call us for a free estimate")
  - Character limit: 1,500 max; aim for 150–300 words
  - Add a photo to every post — text-only posts perform worse
- [ ] **Review responses** — respond to every new review posted since last month
  - Positive reviews: mention the specific service and city naturally ("Thanks for trusting us with your drain cleaning in Cape Coral…")
  - Negative reviews: do NOT respond without Luis approving the response first — flag and hold
  - Aim: respond to **80%+ of all reviews within 24 hours** — responding within 24 hours measurably amplifies the ranking boost vs. slower responses
- [ ] **GBP photo + video upload** — add the job site photos from Step 1 directly to the GBP profile (Photos section → "By owner")
  - If the client sent a short video clip (job walkthrough, before/after, team intro — 15–60 seconds), upload it too. Google weights video above static photos in 2026.
- [ ] **Booking link check** — confirm the GBP booking URL is set and resolves to a working page. Google auto-displays this link in LSA ads — a broken link loses conversions from both GBP and LSA.
- [ ] **Check GBP for Q&A** — Google's Ask Maps AI (replaced Q&A in Dec 2025) may surface questions about the business; if any are visible, note them and update the site's FAQ section to address them

**Lead Machine and Market Leader, additionally:**

- [ ] **Blog topic confirmed** for post #1 this month — pull from `seo-brief.md` topic formula or use client's job story from Step 1
- [ ] **Competitor review check** — check the top 3 competitors' review counts; if any competitor is within 20 reviews of the client, flag to Luis

---

### Week 2 — Content and Citations

**All tiers:**

- [ ] **GBP post #2 of the month**
- [ ] **Citation check** — pick 2 directories from the citation list below and verify the client's NAP is correct; fix any inconsistencies found
  - Month 1–3: Yelp, BBB, Facebook Business, Apple Business Connect, Bing Places, Foursquare
  - Month 4–6: Angi, Porch, Thumbtack, HomeAdvisor, Houzz, Nextdoor Business
  - Month 7+: Data Axle submission, Manta, Chamber of Commerce (if applicable), trade association directories
  - **NAP consistency standard:** every citation must match `client.env` exactly — same phone format, same business name abbreviation, same address style ("St." vs "Street", "LLC" present or absent). Even minor discrepancies trigger verification flags in Google's Knowledge Graph. When you fix a citation, also verify the website's LocalBusiness schema matches `client.env`.
  - Log each citation checked in `maintenance-log.md`: directory name, NAP status (correct / corrected / claimed this month)
- [ ] **Review velocity check** — how many new reviews in the last 30 days?
  - **Target: 4–8 new reviews/month, consistently.** This is now the #11 local ranking factor (up from #93). Consistent monthly velocity outperforms any volume spike.
  - If below 4: flag to Luis — the post-job review request SMS may not be running consistently
  - If zero for 2+ consecutive months: escalate — this is a confirmed ranking degradation risk
  - **Spam filter warning:** if a sudden spike appears (20+ reviews in one week), flag to Luis — Google may suppress them. Remind the client to stagger requests (20–30/week max, not bulk sends).

**Lead Machine and Market Leader, additionally:**

- [ ] **Blog post #1 — written and published**
  - Invoke `/blog-write` with the confirmed topic from Week 1
  - The post must: have an answer-first opening (40–60 words answering the main question directly), target keyword in title + H1 + first paragraph + meta description, link to one service page and one city page
  - After publishing: update `maintenance-log.md` with post title, URL, target keyword
- [ ] **Link building — Week 2 outreach** (4 links/month for Lead Machine, 8 for Market Leader):
  - Target: local chamber of commerce listing, local press, trade association directories, home improvement media, neighborhood/community sites
  - What counts as a quality link: a real site, locally relevant or trade-relevant, with a crawlable page linking to the client's domain
  - What does NOT count: link farms, paid link networks, irrelevant directories
  - Log each link secured: source domain, anchor text used, target page linked to, date live

---

### Week 3 — Content Continuation and Monitoring

**All tiers:**

- [ ] **GBP post #3 of the month**
- [ ] **Spot-check the live site** — homepage, contact page, top service page
  - Click-to-call links working
  - Contact form submits correctly
  - Hours and contact info match what's in `client.env` (especially important if client reported a change in Step 1)
  - No broken images or layout issues on mobile

**Lead Machine and Market Leader, additionally:**

- [ ] **Blog post #2 — written and published** (same process as Week 2)
- [ ] **Competitor monitoring** (10 competitors for Lead Machine, 20 for Market Leader):
  - Check the client's primary keyword in Google (e.g., "plumber Cape Coral") — who is in the 3-pack? Has anything changed since last month?
  - Note any competitor that entered or left the 3-pack
  - Log the observation in `maintenance-log.md`

**Lead Machine and Market Leader, additionally:**

- [ ] **AI search spot-check** (see above) — run for Lead Machine clients here; Market Leader runs same check

**Market Leader, additionally:**

- [ ] **Blog posts #3 and #4** — two more posts this week (total: 6/month = ~1.5/week)
- [ ] **Google LSA (Local Services Ads) management**:
  - Open the LSA dashboard at `ads.google.com/localservices` and review all leads received since last check
  - **LSA reviews are now in GBP** (since July 11, 2025) — there is no separate LSA review system. The client's GBP rating and review volume directly affect LSA ranking. Managing GBP reviews IS managing LSA reviews.
  - **What counts as a valid lead (do NOT dispute):** Connected call for the correct trade and service area, even if the client didn't answer or didn't book the job. Google charges for the lead, not the outcome.
  - **What Google auto-credits (no action needed):** Google AI reviews every lead within 72 hours and automatically credits clear spam, robocalls, and wrong-number calls (immediate hangup, no human on the line).
  - **What you can flag manually:** Use the **"Rate This Lead"** tool inside the LSA dashboard within 30 days of the lead. This is the only manual flag available — the "Report a Problem" dispute button was removed in August 2024.
  - **What is no longer disputable:** "Job type not serviced" and "outside service area" were removed as credit reasons. Fix these at the profile level instead — update service categories and service area settings so mismatched leads stop arriving.
  - **30-second billing rule:** Any call lasting 30 seconds or longer is automatically billed with no exceptions.
  - Check budget pacing — is weekly spend on track, over, or under? Flag to Luis if consistently underspending (area may be too narrow) or overspending (budget may need raising if lead quality is good)
  - Log lead count, disputes filed, and budget status in `maintenance-log.md`
- [ ] **AI search spot-check** — search the client's primary keyword across three platforms:
  - **ChatGPT:** "best [trade] in [city]" — is the client mentioned? Which competitors are cited?
  - **Perplexity:** same query — note any differences in which businesses are cited
  - **Google AI Overview:** search the primary keyword in Google — does an AI Overview appear? Is the client cited in it?
  - Note all results in `maintenance-log.md` — this builds a baseline over months; trends matter more than single readings
  - If a competitor is consistently cited and the client is not: flag to Luis — likely a citation gap, GBP signal gap, or missing FAQ content on the site

---

### Week 4 — Wrap-Up and Report Prep

**All tiers:**

- [ ] **GBP post #4 of the month** — end-of-month post; good time for a seasonal message or a review highlight ("Here's what our Cape Coral customers are saying…")
- [ ] **Review acquisition follow-up** — confirm post-job SMS review requests went out this month; if the client isn't using the review workflow consistently, remind Luis to address it on the next client call
  - The client sends review requests — not CopperBuilds. Your job is to confirm they're doing it. Use the templates below.

**Review Generation Templates** (give these to the client at onboarding — they send from their own phone/email)

*One-time setup — get the GBP review link:*
1. Sign in to [business.google.com](https://business.google.com) as the client → click the business → **Ask for reviews** → copy the short link
2. Format: `https://g.page/r/[PLACE_ID]/review` — save to `client.env` as `GBP_REVIEW_LINK=`
3. Send the link to the client — they paste it into their templates below

*Timing rule: send within 2 hours of job completion, never the next day. Reviews that name the specific service and city carry more ranking weight than generic ones.*

**Template 1 — SMS/text:**
> Hi [First Name], thanks for having us out today! If you're happy with the [service], a quick Google review means a lot to a small business like ours: [GBP_REVIEW_LINK] — if you can mention the service and your neighborhood, that helps us a lot. Thanks! — [Owner Name]

**Template 2 — Email:**
> Subject: Quick favor — how did we do today?
>
> Hi [First Name], thanks for choosing [Business Name] for [service] today. If you're satisfied with the work, a quick Google review means a lot: [GBP_REVIEW_LINK]. Only takes a minute — if anything wasn't right, just reply and I'll fix it personally. Thanks — [Owner Name]

**Template 3 — WhatsApp:**
> Hey [First Name]! Thanks for letting us handle the [service] today. If you're happy with it, a quick Google review helps us a lot: [GBP_REVIEW_LINK] — even a few words makes a difference. Really appreciate it! — [Owner Name]

*Tell the client: "Every time your team finishes a job, someone sends this within 2 hours. No app needed. Aim for 4–8 a month and your Google ranking improves noticeably within 90 days."*
- [ ] **Community reputation scan** — check if the client's business was mentioned in local community platforms this month (see Step 2.5 below for process)
- [ ] **Performance data pull** — collect the metrics needed for `monthly-report.md`:
  - GSC: clicks, impressions, CTR, average position for the past full month
  - GA4: sessions, organic sessions, top pages, goal completions
  - GBP: profile views, website clicks, direction requests, phone calls, new reviews
  - PageSpeed Insights: homepage mobile score, LCP, INP, CLS
- [ ] **Work log review** — read through `maintenance-log.md` for this month; confirm all tasks are logged before generating the report
- [ ] **Run `workflows/monthly-report.md`** — generate and deliver the monthly performance report

**Lead Machine and Market Leader, additionally:**

- [ ] **Link tally** — count links secured this month; confirm Lead Machine hit 4+, Market Leader hit 8+; if short, log the gap and note what outreach is still pending

**Market Leader, additionally:**

- [ ] **Geo-grid rank scan** — run a DataForSEO Maps geo-grid scan using the existing DataForSEO account
  - Center point: client's GBP address. Grid: 7×7, 1-mile spacing for urban markets (2–3 miles for suburban/rural)
  - Cost: ~$0.15/scan via DataForSEO at $0.015 per 5×5 scan
  - Output: color-coded rank map — green (positions 1–3), yellow (4–10), red (10+)
  - Add the map to the monthly report. Note which zones improved or declined vs. last month.
- [ ] **Strategy call prep** (2 calls/month): prepare a one-page agenda from the month's data: what improved, what didn't, what the next month's focus should be

---

## Step 2.5 — Community Reputation Scan (All Tiers, Monthly)

Run once per month during Week 4. This scans local community platforms for mentions of the client's business — positive mentions are flagged for the monthly report; negative ones trigger an immediate response recommendation before they affect reputation or rankings.

Community platforms and forums are now a live local SEO signal: Google surfaces these discussions in search results, and AI systems (ChatGPT, Perplexity, Google AI Overviews) pull from them when answering "who should I call for [trade] in [city]?" questions. A positive mention is a citation. A negative thread left unmanaged can outrank the client's own website.

### What to Check

**Reddit (Claude can run this directly):**
Search: `site:reddit.com "[client business name]"` and `site:reddit.com "[trade] [city]"` (e.g., "plumber Cape Coral").
- Look for threads mentioning the client by name
- Look for recommendation threads in the client's city where competitors are named but the client is not — flag to Luis as an opportunity

**Google general mentions:**
Search: `"[client business name]" -site:[client domain]`
- Surfaces forum posts, neighborhood blogs, news articles, and any community site mentions not caught by the Reddit search

**Nextdoor, Facebook Groups, local forums:**
Claude cannot access these directly (login required). These are monitored passively via Google Alerts — see setup below.

### Google Alerts Setup (One-Time, Per Client)

Set up at `google.com/alerts` during onboarding. Two alerts per client:
1. `"[client business name]"` — catches any new web mention of the business name
2. `"[trade] [city]" recommendation` — catches community discussions in the client's market

Alerts deliver to Luis's email when new results are indexed. Check the inbox as part of Week 4 wrap-up and log any relevant mentions.

### How to Log Results

In `maintenance-log.md`:
```
### Community Reputation Scan
- Reddit: [no mentions found / positive mention in r/[subreddit] — link / negative thread — flagged to Luis]
- Google Alerts: [no new alerts / [N] new mentions — summary]
- Action taken: [none / response drafted / flagged to Luis]
```

### What to Do With Findings

- **Positive mention:** Screenshot it, note in the monthly report — "Your business was recommended in [community platform] this month." Clients love seeing this.
- **Negative mention or complaint thread:** Flag to Luis immediately with the link and text. Do not respond without Luis approving the wording.
- **Recommendation thread where client is absent:** Flag to Luis — client can authentically respond if they serve that area, or it informs the next blog topic or FAQ update.

---

## Required Outputs Before Considering the Month Done

**All tiers:**

- [ ] Client asset checklist reviewed — missing items flagged to Luis
- [ ] 4 GBP posts published (one per week)
- [ ] All new reviews responded to (or flagged for negative review strategy)
- [ ] GBP photos uploaded (minimum: whatever was received from client in Step 1); video uploaded if received
- [ ] Booking link on GBP verified — correct URL, resolves to working page
- [ ] 2 citation entries checked and corrected if needed — NAP verified against `client.env` and schema — logged in `maintenance-log.md`
- [ ] Review velocity confirmed — flagged if below 4 new reviews this month; escalated if zero for 2+ months
- [ ] Live site spot-check completed
- [ ] Performance data collected (GSC, GA4, GBP, PageSpeed)
- [ ] Community reputation scan completed — Reddit + Google Alerts checked, findings logged in `maintenance-log.md`
- [ ] `maintenance-log.md` updated with all work done this month
- [ ] `workflows/monthly-report.md` triggered — report generated and delivered

**Lead Machine, additionally:**

- [ ] 2 blog posts published — titles and URLs logged
- [ ] 4+ quality links secured — sources logged with anchor text and target URLs
- [ ] Competitor 3-pack check logged

**Market Leader, additionally:**

- [ ] 6 blog posts published
- [ ] 8+ quality links secured
- [ ] LSA lead review completed — invalid leads flagged via "Rate This Lead" within 30 days
- [ ] AI search spot-check logged (ChatGPT + Perplexity + Google AI Overview)
- [ ] Geo-grid scan run and map added to monthly report
- [ ] Strategy call agenda prepared (2nd call of the month)

**All tiers — after monthly report is delivered:**

- [ ] Run `/save` — files this month's key findings and patterns as a structured wiki note in the knowledge base (`C:\Users\User\LantechAI\claude-obsidian`). The wiki compounds across all clients — what worked for one HVAC client informs the next.

---

## Maintenance Log Format

Add a new section to `clients/active/[slug]/maintenance-log.md` each month:

```
## [Month YYYY] — [Package tier]
Completed: YYYY-MM-DD

### Client Assets Received
- Photos: [X received / none — GBP posts used older photos]
- Business updates: [what changed, or "none"]
- Blog inputs: [job story / customer question / none — used formula topics]

### GBP
- Posts published: 4 (dates: W1, W2, W3, W4)
- Reviews responded to: [N] (flagged negative reviews: [N or none])
- Photos uploaded: [N]

### Citations Checked This Month
- [Directory name]: NAP correct / corrected [what was wrong]
- [Directory name]: NAP correct / corrected [what was wrong]

### Blog Posts (Lead Machine / Market Leader)
- "[Title]" — [URL] — target KW: [keyword]
- "[Title]" — [URL] — target KW: [keyword]

### Link Building (Lead Machine / Market Leader)
- [Source domain] → [target page] — anchor: "[text]" — live: [date]

### Competitor Notes
- 3-pack unchanged / [competitor entered or left — detail]

### AI Search (Market Leader)
- ChatGPT result for "[query]": [client mentioned Y/N] — competitors cited: [list]
- Perplexity result for "[query]": [client mentioned Y/N] — competitors cited: [list]

### LSA (Market Leader)
- Leads received: [N] — disputed: [N] — budget pacing: [on track / over / under]

### Review Velocity
- New reviews this month: [N] — [on track / below target — flagged]

### Community Reputation Scan
- Reddit: [no mentions found / positive mention — link / negative thread — flagged]
- Google Alerts: [no new alerts / [N] new mentions — summary]
- Action taken: [none / response drafted / flagged to Luis]

### Time spent: [X hours]
```

---

## Edge Cases

**Client sends no photos all month:**
Don't skip GBP posts — use a relevant stock photo from Pexels (same approach as `/copperbuilds-build` Step 1.5) or reuse an older client photo. Log "no client photos received this month" in the maintenance log. After two consecutive months with no photos, flag to Luis: the client needs a reminder that photos directly impact GBP performance.

**Client reports a change (new phone, new hours) mid-month:**
Update the live site immediately — don't wait for the monthly cycle. Update `client.env` to match. Then log the change in the maintenance log under "Business updates."

**Negative review received:**
Do not respond without Luis seeing it first. Flag immediately with the review text and star rating. Hold the response until Luis approves the wording. Log the date received and date responded in the maintenance log.

**Review velocity is zero for 2+ consecutive months:**
Escalate to Luis. The review acquisition workflow (post-job SMS) is not running. Suggest a client call to reinstate it — this is a ranking risk (18-day review drought rule from `seo-local`).

**Blog post can't be written — no topic and no client input:**
Use the emergency topic formula from `seo-brief.md`: pricing guide for the most common service in the primary city. These require no client input and consistently target high-value informational queries. Never skip a blog post without logging why.

**Link target rejected or unavailable:**
Document the outreach attempt (who was contacted, what was requested, the response). Count it as a valid outreach even if the link wasn't secured. Move to the next target on the list. Don't falsely count a pending outreach as a secured link.

**Client on Market Leader asks why they're not ranking for a keyword after 1 month:**
Refer to the timeline expectations in `seo-brief.md` action plan. New content typically takes 60–90 days to show ranking movement. Pull GSC data to show impressions are growing even if position hasn't moved yet. If a page has zero impressions after 60 days, investigate indexing — don't promise faster results.

**Client wants to pause the retainer for a month:**
Log the pause in the client folder with the date. Do not run the monthly workflow that month. Note that a review drought and GBP inactivity will likely impact rankings within 4–6 weeks — communicate this to the client factually, not as a scare tactic.
