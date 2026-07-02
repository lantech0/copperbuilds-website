# Lantech — Client Document System

## Read This First

This file maps every template AND every named section inside each file.
**Always read this before searching.** Important content lives inside files — not in filenames.

---

## Quick Lookup — Find Anything

| What you're looking for | File | Section |
|---|---|---|
| Objection cheat sheet | `07-discovery-call-script.md` | OBJECTION CHEAT SHEET |
| Optional add-ons overview (LSA, ADA) | `07-discovery-call-script.md` | OPTIONAL ADD-ONS |
| LSA detail + how to handle | `07-discovery-call-script.md` | Google LSA — Full Detail |
| ADA compliance detail + risk | `07-discovery-call-script.md` | ADA Compliance — Full Detail |
| Pre-call confirmation email | `07-discovery-call-script.md` | PRE-CALL CONFIRMATION EMAIL |
| Post-call follow-up emails (3 versions) | `07-discovery-call-script.md` | POST-CALL FOLLOW-UP (1hr / 3-day / 7-day) |
| Retainer tier descriptions + prices | `02-onboarding-questionnaire.md` | Section 8, Q37 |
| Delivery timeline (client-facing) | `02-onboarding-questionnaire.md` | WHAT HAPPENS NEXT |
| Delivery timeline (contract) | `03-service-agreement.md` | Section 2 — Timeline |
| 30/60/90 day plan | `13-30-60-90-roadmap.md` | Day 1–30 / Day 31–60 / Day 61–90 |
| 90-day success benchmarks table | `13-30-60-90-roadmap.md` | What "success" looks like at 90 days |
| Maintenance plan prices + features | `11-maintenance-agreement.md` | Plan Selected table |
| Maintenance cancellation terms | `11-maintenance-agreement.md` | Cancellation Terms |
| Photo checklist (universal + by trade) | `12-onboarding-checklist.md` | Section D — Content & Media |
| Go / No-Go build decision gate | `12-onboarding-checklist.md` | GO / NO-GO DECISION |
| Handover package (all logins + access) | `05-handover-package.md` | Sections 1–8 |
| Post-launch first-30-days checklist | `05-handover-package.md` | Section 11 — What Happens Next |
| Testimonial request email | `09-post-launch-emails.md` | TESTIMONIAL REQUEST EMAIL |
| 30-day check-in + upsell email | `09-post-launch-emails.md` | 30-DAY CHECK-IN EMAIL |
| 90-day reactivation email | `09-post-launch-emails.md` | 90-DAY REACTIVATION EMAIL |
| Monthly report template | `10-monthly-report-template.md` | Full document |
| Invoice (PDF-ready) | `04-invoice.html` | Open in browser → Print to PDF |
| SEO client guide | `seo-guide.html` | Open in browser → send to client |

---

## All Templates — Full Map

### `01-welcome-email.md`
Sections: Welcome email body · Project summary table · What we need from you
Key data: delivery timeline placeholder, package name, Lantech email

### `02-onboarding-questionnaire.md`
Sections: Business info (S1) · Brand (S2) · Services (S3) · Target customers (S4) · Competitors (S5) · Website goals (S6) · Design (S7) · Existing assets (S8) · **Retainer tier descriptions Q37** · Add-ons Q38 · **Delivery timeline — WHAT HAPPENS NEXT**
Key data: retainer tier descriptions and prices (Q37) · delivery timeline ("14 days")

### `03-service-agreement.md`
Sections: Scope of work · Timeline · Payment · Revisions · Ownership · Warranties · Limitation of liability · Signatures
Key data: delivery clause ("14 days / custom") · revision rounds

### `04-invoice.html`
HTML invoice, open in browser and print to PDF. Fill all placeholders before sending.

### `05-handover-package.md`
Sections: Live website credentials (S1) · Domain credentials (S2) · SSL (S3) · File backup (S4) · Google Search Console (S5) · Google Analytics (S6) · Google Business Profile (S7) · Contact form (S8) · Financing widget (S8a) · How to update the site (S9) · 30-day support window (S10) · **First 30 days checklist** (S11) · Contact (S12)
Key data: Lantech email · phone placeholder (pending Google Voice number)

### `06-client-brief-template.md`
Internal build brief. Filled from questionnaire answers before build starts.

### `07-discovery-call-script.md`
Sections: **PRE-CALL CONFIRMATION EMAIL** · **POST-CALL FOLLOW-UP — "THINKING IT OVER"** (send within 1hr) · **POST-CALL FOLLOW-UP — 3-DAY BUMP** · **POST-CALL FOLLOW-UP — 7-DAY CLOSE OR DEAD** · **OBJECTION CHEAT SHEET** (reference during call — don't read aloud) · **OPTIONAL ADD-ONS** quick-reference table + full detail sections for each (LSA, ADA)
Key data: objection responses · LSA and ADA detail · Lantech email in all email signatures · GHL automation is bundled in Lead Machine and Market Leader — not a separate add-on

### `08-preview-delivery-email.md`
Preview delivery email, revision round updates, and approval confirmation.

### `09-post-launch-emails.md`
Sections: **30-DAY CHECK-IN EMAIL** (with upsell options) · **TESTIMONIAL REQUEST EMAIL** · **UPSELL FOLLOW-UP — 7-DAY BUMP** · **90-DAY REACTIVATION EMAIL**

### `10-monthly-report-template.md`
Sections: Month's headline · Keyword rankings table · GSC organic search overview · GA4 traffic · GBP metrics · Site speed (CWV) · What we did last month · What we're doing next month · Action items from client

### `11-maintenance-agreement.md`
Sections: **Plan selected (Basic $99 / Standard $199 / Pro $299)** · What's included per plan · What's not included · Payment terms · Cancellation terms (30 days written notice) · Access requirements
Key data: maintenance plan prices · cancellation terms · Lantech email

### `12-onboarding-checklist.md`
Sections: **Section A — Contract & Payment** · **Section B — Business info** · **Section C — Brand assets** · **Section D — Photos & content** (with trade-specific lists) · **Section E — Website structure** · **Section F — SEO setup** · **Section G — Communication** · **Section H — Post-launch services** · **GO / NO-GO DECISION**
Key data: photo requirements by trade · go/no-go gate checklist

### `13-30-60-90-roadmap.md`
Sections: Day 1–30 Foundation · Day 31–60 Google Starts Noticing · Day 61–90 Traction Builds · **90-day success benchmarks table** · What we need from you monthly
Key data: GBP post frequency (4/mo) · citation cadence · tier-specific deliverables by month · benchmark ranges table · Lantech email

---

## Folder Structure

```
clients/
  templates/       ← master templates (never edit these directly for a client — copy to active/)
  active/          ← one folder per active client: active/[business-slug]-[YYYY-MM]/
  completed/       ← archived completed projects
```

---

## Client Lifecycle — Which Template, When

| Stage | Workflow | Templates |
|---|---|---|
| Prospect agrees to call | `workflows/discovery-call.md` | `07` (pre-call email) |
| Call done, didn't close | `workflows/discovery-call.md` | `07` (post-call follow-ups + cheat sheet) |
| Lead closes | `workflows/project.md` | `03` agreement · `04` invoice · `01` welcome · `02` questionnaire |
| Build starting | `workflows/project.md` | `06` client brief · `12` onboarding checklist |
| Build complete | `workflows/revisions.md` | `08` preview delivery email |
| Client approves | `workflows/deploy.md` | `05` handover package |
| 30 days post-launch | `workflows/post-launch.md` | `09` post-launch emails |
| Monthly (retainer clients) | `workflows/seo-retainer.md` · `workflows/monthly-report.md` | `10` monthly report |
| Ongoing maintenance | `workflows/maintenance.md` | `11` maintenance agreement |
| Client offboards | `workflows/offboarding.md` | Final file handover (from `05`) |

---

## Key Values — Sitewide Consistency Check

Any time a value below changes, grep all templates for it and update every occurrence.

| Value | Current | Lives in |
|---|---|---|
| Lantech email | `luis.copperbuilds@gmail.com` | 01, 05, 07, 09, 10, 11, 12, 13 |
| Lantech phone | `+63 977 329 3969` (pending Google Voice US number) | 05 (placeholder) |
| Delivery timeline | `14 days` | 02, 03 |
| Retainer tiers | Local Presence $997 · Lead Machine $1,997 · Market Leader $3,497 | 02 |
| Maintenance plans | Basic $99 · Standard $199 · Pro $299 | 11, 12 |
| One-time build plans | Starter $1,200 · Growth $1,699 · Pro $1,999 | 02 (Section 8) |
