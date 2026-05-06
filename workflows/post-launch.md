# Workflow: Post-Launch Follow-Up

**Triggered by:** 30-day calendar reminder set in `workflows/deploy.md`
**Templates used:** `clients/templates/09-post-launch-emails.md`

---

## Objective

Check in at the 30-day mark, close out the support window, collect a testimonial, and surface the right upsell — without being pushy or missing the natural moment to expand the relationship.

---

## Step 1 — 30-Day Check-In (Day 30 after launch)

1. Pull the client's `LAUNCH-SUMMARY.md` from `clients/completed/[slug]/`
2. Check their Google Search Console (if you have access) for indexing status
3. Send the **30-day check-in email** from `09-post-launch-emails.md`
   — Pick the 1–2 most relevant upsell options based on what's in their package and what you know about their business
   — Do not list every upsell option — pick the ones that actually make sense for them

---

## Step 2 — Testimonial Request

If the client confirms everything is working well in their reply:
- Send the **testimonial request email** from `09-post-launch-emails.md` in the same thread or as a follow-up within 24 hours
- Save any testimonial they provide to `clients/completed/[slug]/TESTIMONIAL.md`
- Copy it to `lantech-website/brand_assets/testimonials.md` (create if it doesn't exist) so it's available for the Lantech site

---

## Step 3 — Upsell Follow-Up

If the client showed interest in an upsell option:
- Follow up 7 days later with the **upsell follow-up email** from `09-post-launch-emails.md`
- If they commit: create a new project entry in `clients/active/` for the add-on work
- If no response: mark as cold in the client file and set a 90-day reactivation reminder

---

## Step 4 — 90-Day Reactivation (if applicable)

If no additional work was bought at 30 days:
- Set a calendar reminder for 90 days from launch date
- Send the **90-day reactivation email** from `09-post-launch-emails.md`

---

## Step 5 — Portfolio: Trigger Case Study

If a case study hasn't been written yet:
- Run `workflows/portfolio-capture.md`

---

## Required Outputs Before Considering Post-Launch Done

- [ ] 30-day check-in email sent
- [ ] Client's support window status noted (any open bugs addressed within window)
- [ ] Testimonial requested (if check-in response was positive)
- [ ] Any testimonial received saved to `clients/completed/[slug]/TESTIMONIAL.md` and to `brand_assets/testimonials.md`
- [ ] Upsell follow-up sent if client showed interest
- [ ] 90-day reminder set if no upsell bought
- [ ] `workflows/portfolio-capture.md` triggered
