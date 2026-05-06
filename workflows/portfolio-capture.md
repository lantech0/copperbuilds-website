# Workflow: Portfolio Capture → Case Study → Update Portfolio Page

**Triggered by:** `workflows/deploy.md` (at launch) and `workflows/post-launch.md` (at 30 days)

---

## Objective

Capture the completed client site as a portfolio entry — screenshot, write the case study, and add it to the Lantech portfolio page so new prospects see real proof of work.

---

## Step 1 — Screenshot the Live Site

1. Navigate to `lantech-website/` (the Lantech workstation)
2. Take full-page screenshots of the client's live site at 1280px and 375px:
   ```
   node screenshot.mjs https://[CLIENT_DOMAIN] desktop
   node screenshot.mjs https://[CLIENT_DOMAIN] mobile
   ```
3. Save screenshots to: `lantech-website/portfolio/[client-slug]/`
   - `desktop-homepage.png`
   - `mobile-homepage.png`
   - Screenshot additional pages if they're visually strong

---

## Step 2 — Pull the Case Study Facts

From `clients/completed/[slug]/LAUNCH-SUMMARY.md`:
- Business name and industry
- Package purchased
- Pages built
- Notable features (GBP, schema, blog, etc.)
- Before state (what their digital presence looked like before)
- After state (what was delivered)
- Any early results (testimonial quote, GSC indexing, client feedback)

From `clients/completed/[slug]/TESTIMONIAL.md` (if exists):
- Pull the client quote for use in the case study

---

## Step 3 — Write the Case Study Entry

Format:

```markdown
## [Business Name] — [Industry] | [City, State]

**Package:** [Starter / Growth / Pro]
**Pages built:** [N]
**Delivered in:** [Timeline]

**The situation:** [1–2 sentences — what their digital presence looked like before. Use the digital audit data from the prospect file: no website / poor mobile / dormant social / no local schema.]

**What we built:** [2–3 sentences — specific pages and features, not generic. Name the keyword they're targeting, the schema type, any GBP work.]

**The result:** [1–2 sentences — what changed. Early search impressions, client quote, inquiries received. Be specific. If no data yet: "Site submitted to Google Search Console — indexing in progress."]

> "[TESTIMONIAL QUOTE]"
> — [Client name], [Business name]

[Screenshot embed]
```

Save to: `lantech-website/portfolio/[client-slug]/case-study.md`

---

## Step 4 — Add to Lantech Portfolio Page

1. Open `lantech-website/portfolio.html` (or the portfolio section of `index.html` if not a separate page)
2. Add the new case study entry following the existing card format
3. Link to the live site and embed the desktop screenshot
4. Run the build → screenshot → QA process for the portfolio page before considering this done

If a portfolio page doesn't exist yet on the Lantech site:
- Flag this to the user — don't add a portfolio page without approval
- Save the case study to `portfolio/[client-slug]/` and note it's pending a portfolio page build

---

## Required Outputs Before Considering Portfolio Capture Done

- [ ] Desktop + mobile screenshots saved to `portfolio/[client-slug]/`
- [ ] Case study written and saved to `portfolio/[client-slug]/case-study.md`
- [ ] Case study added to the Lantech portfolio page (or flagged as pending if no portfolio page exists)
- [ ] Portfolio page QA'd after update
