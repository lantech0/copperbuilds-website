# Workflow: Monthly Performance Report

**Triggered by:** Start of each month for any client with an active retainer or recurring reporting agreement
**Template used:** `clients/templates/10-monthly-report-template.md`
**Handoff from:** `workflows/deploy.md` (sets the monthly cadence) / `workflows/maintenance.md` (Standard/Pro plans)

---

## Objective

Generate and deliver a clear, concise monthly performance report that shows the client measurable progress, explains what was done this month, and builds confidence in the ongoing relationship.

---

## Trigger

Run at the start of each calendar month for every client with reporting in their plan, or when the user says "generate monthly report for [client]."

---

## Required Inputs

Before starting, confirm these exist:
- Client folder at `clients/active/[slug]/` or `clients/completed/[slug]/`
- Client's target keywords from `06-client-brief.md`
- Access to Google Search Console (GSC) — if missing, note it and request access in the email
- Access to Google Analytics 4 (GA4) — if missing, note it and request access in the email
- Google Business Profile access (local clients only)

---

## Steps

### Step 1 — Pull This Month's Data

Collect the following for the previous full calendar month:

**Google Search Console — Overview metrics:**
- Total clicks (organic)
- Total impressions
- Average CTR
- Average position
- Coverage issues (any new indexing errors?)

**Google Search Console — Target Keyword Rankings (primary method):**

Open GSC → Performance → Search results. Set date range: previous full calendar month.

For each target keyword in the client's `_keyword-map.md`, pull its position:
1. Click **+** → **Query** → **Exact query** → type the target keyword → Apply
2. Note the **Average position** and **Total clicks** for that keyword
3. Clear the filter → repeat for the next keyword

Record each result in the Target Keyword Rankings table in the report (see template). Note the position from last month's report to calculate the change.

**DataForSEO fallback — run through all 3 gates before touching the API:**

DataForSEO charges per call. A missed gate is real money wasted. Check in order:

**Gate 1 — Is GSC available with data for this month?**
If yes → use GSC only. Skip DataForSEO entirely. It is not a supplement when GSC is working.

**Gate 2 — Does a cache exist?**
Check for: `clients/active/[slug]/monthly-reports/YYYY-MM-dataforseo-rankings.json`
If the file exists → load it and use it. Do not call the API again this month for this client, even if asked to re-run.

**Gate 3 — Has the user approved this call in the current session?**
If not explicitly confirmed → ask before calling: *"GSC doesn't have full data for [Month] yet. DataForSEO can pull rankings for [N] keywords in one call. Run it?"*
Wait for a yes before proceeding.

**If all 3 gates clear — one call, tightly scoped:**
1. Read `_keyword-map.md` — collect every target keyword for this client
2. Batch ALL of them into a single SERP request — never one call per keyword
3. Parameters: location = client's city + state (from `06-client-brief.md`), device = desktop, depth = 10 (page 1 only)
4. Pull ONLY the SERP rankings endpoint — do not run keyword ideas, backlinks, on-page analysis, or domain overview
5. Save the full raw response immediately: `clients/active/[slug]/monthly-reports/YYYY-MM-dataforseo-rankings.json`
6. Add one line to the bottom of the report: `DataForSEO: called YYYY-MM-DD — [N] keywords batched — cached at monthly-reports/YYYY-MM-dataforseo-rankings.json`

**Top 5 queries (informational — separate from target keywords):**
After pulling target keyword data, also note the top 5 queries by clicks this month. These may reveal unexpected ranking wins or branded traffic that isn't in the keyword map.

**Google Analytics 4:**
- Total sessions
- Organic sessions (Channel: Organic Search)
- Top pages by sessions
- Goal completions / conversions (if configured)

**Google Business Profile (local clients only):**
- Profile views
- Website clicks from GBP
- Direction requests
- Phone calls
- New reviews received this month

**Core Web Vitals — PageSpeed Insights (mobile):**
- Performance score
- LCP, INP, CLS values
- Flag any regression vs. last month

### Step 2 — Check What Was Done Last Month

Review the client folder and any session notes from the previous month:
- What SEO work was completed?
- Were any pages updated, added, or rebuilt?
- Technical fixes deployed?
- Blog posts published?

This becomes the "What We Did" section of the report.

### Step 3 — Identify the Key Win

Pick ONE result that represents the most meaningful progress this month:
- A keyword moved from page 2 to page 1
- Organic traffic up X% vs. prior month
- GBP phone calls increased noticeably
- A newly indexed page is already driving clicks

Lead the report with this one sentence. Clients remember one clear win — not a data dump.

### Step 4 — Fill the Report Template

Open `clients/templates/10-monthly-report-template.md` and fill every field:
- Client name, reporting period, date sent
- Key win (one sentence, at the top)
- GSC data table
- GA4 data table
- GBP table (local clients only — remove section if not applicable)
- CWV status
- What we did last month (specific actions, not generic)
- What we're doing next month (specific, not generic)
- Action items from the client (if any — or "None this month")

No blank fields. If data is unavailable (no GSC access), write "Access not yet granted — requested in this email."

### Step 5 — Save the Report

Save the completed report locally to:
`clients/active/[slug]/monthly-reports/YYYY-MM-report.md`

Create `monthly-reports/` if it doesn't exist yet.

Then upload to the client's Google Drive folder:
1. Read the Drive folder ID from `clients/active/[slug]/DRIVE-FOLDER.md`
2. Use `mcp__claude_ai_Google_Drive__search_files` to find or create a `Monthly Reports` subfolder inside the client's Drive folder
3. Upload the report using `mcp__claude_ai_Google_Drive__create_file`
4. Copy the uploaded file's URL and add it to the bottom of the local report file:
   `Drive link: https://drive.google.com/file/d/[ID]`

The client receives the report via email (Step 6), but having it in Drive means they can always find past reports without digging through their inbox.

### Step 6 — Deliver to Client

Email subject: `[Business Name] — Monthly Report — [Month YYYY]`

Keep the email body to 3–4 sentences max:
*"Hi [Name], here's your [Month] performance report. The headline this month: [one-sentence key win]. Full details are below / attached. Let me know if you have any questions."*

Paste the report inline or attach as PDF (print the .md to PDF). Do not send a raw markdown file.

---

## Required Outputs Before Considering Report Done

- [ ] Data for the full previous month collected (GSC, GA4, GBP if applicable)
- [ ] Report template fully filled — zero blank fields
- [ ] Key win identified and placed at top — one sentence, specific
- [ ] "What We Did" reflects actual completed work — not generic
- [ ] "What's Next" is specific — not "continue optimizing"
- [ ] Report saved to `clients/active/[slug]/monthly-reports/YYYY-MM-report.md`
- [ ] Report uploaded to client's Drive folder → Monthly Reports subfolder
- [ ] Drive link added to bottom of local report file
- [ ] Email sent to client

---

## Edge Cases

**Client hasn't granted GSC or GA4 access:**
Note each missing data source in the report. In the email, request access: *"To give you a fuller picture next month, could you add [your email] as a viewer in Google Search Console and Google Analytics? Takes about 2 minutes — happy to send instructions."*

**First report (no prior month for comparison):**
Skip all month-over-month comparison columns. Write "Baseline established" in trend fields. State this clearly: *"This is your first report — we're establishing your baseline now. Month 2 will show your first comparison."*

**New site with very low traffic (< 3 months old):**
Lead with indexing status and crawl coverage instead of traffic data. Frame expectations clearly: *"New sites typically take 60–90 days to build meaningful organic traffic. Your site is indexed and ranking for [X keywords] — we'll see this grow over the next 2–3 months."*

**Client asks a data question you can't answer from the report:**
Answer it directly in a reply email. If answering requires site changes or additional research, log it as a task in the client folder and address it in next month's work.

**Data shows a significant drop:**
Lead with it — do not bury it after the wins. Explain the likely cause (algorithm update, seasonal dip, a page going offline) and what you're doing about it.
