# Workflow: /project — New Client Project Intake

**Triggered by:** Lead closes on a discovery call (`workflows/discovery-call.md`)
**Skill:** Run as `/project "[Business Name]"` from the lantech-website workstation
**Handoff to:** `workflows/revisions.md` after build is complete

---

## Objective

Create the client project folder, populate all documents from templates, and queue the correct onboarding sequence so nothing falls through the cracks between "deal closed" and "build starts."

---

## Step 1 — Create the Client Folder

Create the folder: `clients/active/[business-name-slug]-[YYYY-MM]/`

Example: `clients/active/joes-plumbing-2026-04/`

Copy all template files into the new folder and rename them:
```
clients/active/[slug]-[YYYY-MM]/
  01-welcome-email.md
  02-onboarding-questionnaire.md
  03-service-agreement.md
  04-invoice.html
  05-handover-package.md
  06-client-brief.md          ← renamed from 06-client-brief-template.md
  07-discovery-call-script.md
```

---

## Step 1.5 — Create the Google Drive Client Folder

Every client gets a dedicated Google Drive folder from day one. This is the single shared location for all client documents across the entire project lifecycle — agreements, briefs, reports, and handover files all live here. The client gets access to it too, so they always have their own copies.

**Create the folder using Google Drive MCP:**

1. Use `mcp__claude_ai_Google_Drive__search_files` to find the parent folder named `Lantech Agency — Active Clients`. If it doesn't exist, create it first with `mcp__claude_ai_Google_Drive__create_file`.

2. Inside that parent folder, create a new subfolder:
   - Name format: `[Business Name] — [Package] — [YYYY-MM]`
   - Example: `Joe's Plumbing — Growth — 2026-05`
   - Use `mcp__claude_ai_Google_Drive__create_file` with `mimeType: application/vnd.google-apps.folder`

3. Save the folder details to the client's local folder as `DRIVE-FOLDER.md`:
   ```
   Drive folder name: [Business Name] — [Package] — [YYYY-MM]
   Drive folder URL: https://drive.google.com/drive/folders/[ID]
   Drive folder ID: [ID]
   Created: YYYY-MM-DD
   ```

The Drive folder ID is referenced in every subsequent step — recording it now prevents hunting for it later.

---

## Step 2 — Fill in Known Placeholders

Using the information from the prospect file (`projects/prospects/[file].md`), pre-fill the following in the service agreement, welcome email, and client brief:

**From the prospect file:**
- Business name
- Owner name
- Phone number
- Website URL (if any)
- Google Business Profile URL (if any)
- Recommended package (Starter / Growth / Pro)
- Package price
- Identified digital gaps

**Determine and set:**
- Expected delivery date: today + [2 business days for Starter / 5 days for Growth / 7 days for Pro]
- Support expiry date: launch date + 30 days
- Project lead: Luis Echarri

Leave any placeholders that require client input (logo, brand colors, copy preferences) blank — the onboarding questionnaire will collect these.

---

## Step 3 — Day 0 Actions (Deal Closed — Before Payment)

Send in this order:

1. **Service Agreement** (`03-service-agreement.md`) — send via email, request signature
2. **Invoice** (`04-invoice.html`) — open in browser, print to PDF, attach to the same email

Email subject: `Your Lantech Agreement & Invoice — [Business Name]`

Do not begin any build work until the agreement is signed and payment is confirmed.

3. Upload both documents to the client's Drive folder (use the ID from `DRIVE-FOLDER.md`):
   - Upload the service agreement PDF
   - Upload the invoice PDF
   Use `mcp__claude_ai_Google_Drive__create_file` for each.

---

## Step 4 — Day 0 Actions (Payment Confirmed)

Once payment is received:

1. Send **Welcome Email** (`01-welcome-email.md`) — attach or link to the onboarding questionnaire
2. Mark payment received in the client folder (add a `PAYMENT-CONFIRMED.md` note with date and amount)
3. Upload `PAYMENT-CONFIRMED.md` to the client's Drive folder
4. Update prospect file status: `[x] Outreach Sent → [x] Replied → [x] Call Booked → [x] Closed`

---

## Step 5 — Questionnaire Received

When the completed questionnaire arrives:

1. Review all answers. Flag any gaps (missing logo, no photos, incomplete address).
2. Fill in `06-client-brief.md` from the questionnaire answers.
3. If any required fields are missing: send one clarifying email listing exactly what's needed. Do not start the build until the brief is complete.
4. Upload both files to the client's Drive folder:
   - Completed `02-onboarding-questionnaire.md`
   - Completed `06-client-brief.md`
5. Confirm receipt to the client: *"We've received your questionnaire and we're starting your build now. You'll have a preview link within [TIMELINE]."*

---

## Step 6 — Trigger the Build

With the brief complete, invoke the build process:

1. **Read `DESIGN.md`** in the lantech-website workstation
2. **Invoke `frontend-design` skill**
3. **Run `/impeccable craft`** with the completed `06-client-brief.md`
4. Follow the full build → screenshot → QA process in `CLAUDE.md`

---

## Step 7 — After Build: Trigger Preview Delivery

When the build passes all quality gates in `CLAUDE.md`, run `workflows/revisions.md`.

---

## Required Outputs Before Considering Intake Done

- [ ] Client folder created at `clients/active/[slug]-[YYYY-MM]/`
- [ ] Google Drive client folder created — ID and URL saved to `DRIVE-FOLDER.md`
- [ ] All template files copied and known placeholders filled
- [ ] Service agreement + invoice sent (Day 0) and uploaded to Drive
- [ ] Welcome email + questionnaire sent (on payment confirmation)
- [ ] `PAYMENT-CONFIRMED.md` created locally and uploaded to Drive
- [ ] Prospect file status updated to Closed
- [ ] `06-client-brief.md` completed from questionnaire and uploaded to Drive
- [ ] Completed questionnaire uploaded to Drive
- [ ] Build triggered with completed brief

---

## Package Reference

| Package | Price | Pages | Includes | Delivery |
|---|---|---|---|---|
| Starter | $1,200 | Up to 5 | Website + on-page SEO + contact form + SSL + GSC submission | 48–72 hours |
| Growth | $1,699 | Up to 10 | Starter + local SEO + Google Business Profile optimization | 5 business days |
| Pro | $1,999 | Up to 20 | Growth + full SEO + social media profile setup + blog setup | 7 business days |

**Revisions included:** 2 rounds for all packages. Additional rounds: $75–150/round.
**Post-launch support:** 30 days free bug fixes. After that: billed at hourly rate.
