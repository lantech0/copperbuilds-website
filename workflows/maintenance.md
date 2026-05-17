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

## Maintenance Plan

This workflow covers the **Care plan — $120/mo**. The Care plan applies to clients who have completed a one-time website build (Starter / Growth / Pro) and want ongoing hosting and maintenance without an SEO retainer.

Clients on a monthly SEO retainer (Local Presence / Lead Machine / Market Leader) do NOT run this workflow — their monthly work is handled by `workflows/monthly-report.md`, which already includes a speed check and link check as part of standard reporting.

| Plan | Monthly Fee | Included |
|---|---|---|
| Care | $120/mo | Managed hosting (Hostinger) · security updates + uptime monitoring · monthly backup · performance check (PageSpeed + CWV) · up to 1 hour bug fixes · status email |

Confirm the client is on the Care plan from their folder before starting. Log anything beyond 1 hour of bug fixes as out-of-scope and quote separately.

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

### Step 3 — Security Headers Check

Check `https://securityheaders.com/` for the client's domain. Note any headers rated C or below. Log findings in the maintenance log.

Do not modify server configuration without explicit user approval. Flag any serious gaps to Luis for follow-up.

### Step 4 — Content Updates

Apply updates within the included plan scope:
- Business hours, pricing, phone number, or address changes (if client sent updates)
- New photos swapped in (if client provided them)
- Copy errors or outdated information spotted during the check

Track time spent on content updates. The Care plan includes up to 1 hour of bug fixes and minor updates. Do not exceed 1 hour without flagging it and quoting separately.

### Step 5 — Spot-Check Key Pages

Open the live site and visually check: homepage, contact page, and the top service page.
- All click-to-call links still work
- Contact form submits without error
- No obvious layout breaks on mobile (375px)
- No outdated promotions or expired offers visible

Log any issues found in Step 6. Fix anything within scope (under 1 hour total for Step 4 + Step 5 combined).

### Step 6 — Log the Work

Add a maintenance log entry to: `clients/active/[slug]/maintenance-log.md`

Use this format exactly:

```
## [Month YYYY]
Plan: Care — $120/mo
Date completed: YYYY-MM-DD

Checks:
- Broken links: [X found and fixed / 0 found]
- Speed (mobile): [score] — LCP [Xs] / CLS [X] / INP [Xms] — [pass / flagged: detail]
- Security headers: [pass / flagged: detail]
- Content updates: [what was changed, or "none this month"]
- Key page spot-check: [pass / issues found: detail]

Time spent: X minutes (of 60 min included)
Out-of-scope items flagged: [yes: detail / none]
```

### Step 7 — Client Status Email

Send a brief update email:

Subject: `[Business Name] — Monthly Maintenance Done — [Month YYYY]`

Body:
*"Hi [Name], your site maintenance for [Month] is done. Quick summary:*

*— Speed (mobile): [score] — [all clear / flagged: detail]*
*— Links: [all clear / X fixed]*
*— [Notable update if any: 'Updated your hours on the contact page' / 'Fixed a broken button on Services']*

*(Note: Full SEO performance reporting is part of the monthly retainer plans — Local Presence, Lead Machine, Market Leader. The Care plan covers hosting and maintenance only.)*

*Let me know if anything needs attention. — Luis"*

Keep it under 100 words. The client wants to know their site is healthy — not a full breakdown.

---

## Required Outputs Before Considering Maintenance Done

- [ ] Broken link check completed — all broken links fixed or noted
- [ ] Speed check completed — mobile score and CWV values logged
- [ ] Security headers checked and logged
- [ ] Content updates applied within 1-hour scope — time logged
- [ ] Key page spot-check completed (homepage, contact, top service page)
- [ ] Maintenance log updated at `clients/active/[slug]/maintenance-log.md`
- [ ] Client status email sent

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
