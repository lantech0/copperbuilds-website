# Workflow: Monthly Maintenance Retainer

**Triggered by:** Start of each month for any client on a maintenance retainer plan
**Handoff from:** `workflows/post-launch.md` (upsell path) or standalone sale after launch

---

## Objective

Run a structured monthly site health check, fix any issues found within the plan scope, and deliver a brief status update to the client — so they know their site is actively maintained without needing to chase you.

---

## Trigger

Run at the start of each calendar month for every active maintenance retainer client, or when the user says "run maintenance for [client]."

---

## Maintenance Plans

| Plan | Monthly Fee | Included |
|---|---|---|
| Basic | $99/mo | Broken link check · Speed check · 1 minor content update · Status email |
| Standard | $199/mo | Basic + security headers check · monthly performance report · 2 hrs content/design updates |
| Pro | $299/mo | Standard + full technical SEO re-audit · GBP post draft · blog post or page update |

Confirm the client's plan from their folder before starting. Only do work included in their plan — log anything out of scope and quote it separately.

---

## Required Inputs

- Client folder at `clients/active/[slug]/`
- Live site URL (from `06-client-brief.md`)
- Client's retainer plan: Basic / Standard / Pro
- Hosting/FTP credentials if updates are needed (from `05-handover-package.md`)

---

## Steps

### Step 1 — Broken Link Check

Check every link on the live site:
- All navigation links (desktop and mobile nav)
- Footer links
- CTA buttons ("Contact Us", "Get a Quote", "Call Now", "Book Now")
- Any external links in blog posts or body copy

Fix broken internal links immediately. For broken external links: remove or replace with a working source. Log every fix in Step 7.

### Step 2 — Speed Check

Run PageSpeed Insights on the homepage (and top landing page if different from homepage):
- Mobile performance score
- LCP, INP, CLS values

If any Core Web Vital has regressed by more than 10 points vs. last month: stop and investigate the cause before proceeding. Check for newly added large images, embed scripts, or third-party widgets.

### Step 3 — Security Headers Check (Standard / Pro only)

Check `https://securityheaders.com/` for the client's domain. Note any headers rated C or below. Log findings in the maintenance log.

Do not modify server configuration without explicit user approval. Flag any serious gaps to Luis for follow-up.

### Step 4 — Content Updates

Apply updates within the included plan scope:
- Business hours, pricing, phone number, or address changes (if client sent updates)
- New photos swapped in (if client provided them)
- Copy errors or outdated information spotted during the check

For Standard/Pro: track time spent on content updates. Do not exceed the included 2 hours without flagging it.

### Step 5 — Full Technical SEO Re-Audit (Pro only)

Invoke `/seo-technical` on the client's site. Compare findings against last month's log entry. Fix any issues within scope (meta tags, heading structure, schema errors, sitemap issues). Log new issues and whether they were fixed or flagged.

### Step 6 — GBP Post Draft (Pro only)

Draft one Google Business Profile post for the client to publish this month. Save to:
`clients/active/[slug]/gbp-posts/YYYY-MM-gbp-post.md`

Post topics (pick what's most relevant):
- A seasonal tip related to their trade
- A service highlight with a specific benefit
- A recent result or customer outcome (without naming the client)
- A local event or community connection

The client publishes the post — we draft and recommend, we do not post directly to their GBP unless they have explicitly granted posting access.

### Step 7 — Log the Work

Add a maintenance log entry to: `clients/active/[slug]/maintenance-log.md`

Use this format exactly:

```
## [Month YYYY]
Plan: [Basic / Standard / Pro]
Date completed: YYYY-MM-DD

Checks:
- Broken links: [X found and fixed / 0 found]
- Speed (mobile): [score] — LCP [Xs] / CLS [X] / INP [Xms] — [pass / flagged: detail]
- Security headers: [pass / flagged: detail] (Standard/Pro only)
- Content updates: [what was changed, or "none this month"]
- Technical SEO: [pass / issues found: detail / fixed or flagged] (Pro only)
- GBP post: [saved to gbp-posts/YYYY-MM / n/a]

Time spent: X minutes
Out-of-scope items flagged: [yes: detail / none]
```

### Step 8 — Client Status Email

Send a brief update email:

Subject: `[Business Name] — Monthly Maintenance Done — [Month YYYY]`

Body:
*"Hi [Name], your site maintenance for [Month] is done. Quick summary:*

*— Speed (mobile): [score] — [all clear / flagged: detail]*
*— Links: [all clear / X fixed]*
*— [Notable update if any: 'Updated your hours on the contact page' / 'Fixed a broken button on Services']*

*[Standard/Pro: Your full monthly report is attached.]*

*Let me know if anything needs attention. — Luis"*

Keep it under 100 words. The client wants to know their site is healthy — not a full breakdown.

---

## Required Outputs Before Considering Maintenance Done

- [ ] Broken link check completed — all broken links fixed or noted
- [ ] Speed check completed — mobile score and CWV values logged
- [ ] Security headers checked and logged (Standard/Pro)
- [ ] Content updates applied within plan scope — time logged
- [ ] Technical SEO re-audit run (Pro only)
- [ ] GBP post drafted and saved (Pro only)
- [ ] Maintenance log updated at `clients/active/[slug]/maintenance-log.md`
- [ ] Client status email sent
- [ ] Monthly report generated and attached (Standard/Pro — run `workflows/monthly-report.md`)

---

## Edge Cases

**Speed score regressed significantly (> 10 points drop):**
Stop. Investigate before doing anything else. Likely causes: large new image, a new embed, a plugin or script the client added without telling you. If the cause is outside our scope, flag it to the client clearly and quote the fix separately.

**Client requests work outside their plan:**
Note it, confirm it's out of scope, quote additional hours at the standard hourly rate. Do not do out-of-scope work without approval and a new invoice. Log the request in the client folder.

**No hosting access to make fixes:**
Flag it in the client status email. Ask the client to send updated credentials or to apply the specific fix themselves (provide exact instructions). Do not guess credentials or work around access issues.

**Client hasn't responded in 2+ consecutive months:**
Log it in the client folder. At 3 months of non-response, flag to Luis: the retainer may be worth reviewing. Do not cancel unilaterally.

**Client's site is down during the check:**
This is urgent. Contact the client immediately by phone or text — do not wait for the monthly email. Check their host's status page and report what you find.
