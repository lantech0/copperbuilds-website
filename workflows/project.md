# Workflow: /project — New Client Project Intake

**Triggered by:** Lead closes on a discovery call (`workflows/discovery-call.md`)
**Skill:** Run as `/project "[Business Name]"` from the copperbuilds workstation
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
- Expected delivery date: today + [7 business days for Starter / 10 business days for Growth / 14 business days for Pro]
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
3. **Populate `client.env` from the questionnaire answers:**
   - Copy `clients/templates/client.env` into the client folder
   - Fill every field Claude can derive from the questionnaire:
     - Business info: name, phone, email, address, hours
     - Services list (SERVICE_1..N)
     - Cities served (CITY_1..N)
     - Emergency service flag
     - Years in business, license number, review count
     - External links: GMB, Facebook, Yelp, Nextdoor, BBB, Instagram
     - TRADE_KEYWORD: derive from SERVICE_1 (e.g. "Drain Cleaning" -> "plumber")
     - WEBSITE_URL: client's existing domain if they have one
   - Generate SEO fields using the formula in `docs/superpowers/specs/2026-05-10-client-config-build-system-design.md`
   - Generate internal links using the SEO strategy in that same spec
   - Leave `WEB3FORMS_KEY=` blank — collected after account setup
4. **Populate `styles/Client/Vocab.yml` for Vale:**
   - Copy `clients/templates/vale-vocab-template.yml` to `copperbuilds/styles/Client/Vocab.yml`
   - Fill the `tokens:` list with banned/off-brand terms from the client's brief and brand voice:
     - Competitor names (if client doesn't want them in copy)
     - Outdated service names or old brand names
     - Off-brand adjectives (e.g., "cheap" for a premium client)
   - Remove the placeholder line `- 'REPLACE_THIS_WITH_ACTUAL_BANNED_TERMS'`
   - If the client has no brand restrictions, leave the tokens list empty (delete the placeholder line)
5. Show the populated `client.env` to the user for review and confirmation.
6. If any required fields are missing, send one clarifying email. Do not start the build until confirmed.
6. Upload completed `02-onboarding-questionnaire.md` and `06-client-brief.md` to the client's Drive folder.
7. Confirm receipt to the client.

---

## Step 6 — Trigger the Build

With `client.env` confirmed and the brief complete:

1. **Run `/lantech-build`** using `client.env` and `06-client-brief.md` as data sources.
   - Build all HTML pages using `{{PLACEHOLDER}}` syntax for every variable value
     (phone numbers, SEO fields, nav links, external links, colors, form key).
   - Save all source files to `clients/active/[slug]/_source/`.
   - Required source files: `index.html`, `services.html`, `about.html`,
     `contact.html`, `blog.html`, `city.html`, `blog-post.html`.
2. **Render the final site:**
   ```
   python build.py clients/active/[slug]-[YYYY-MM]/
   ```
3. Review the build output. Warnings about missing source files must be resolved before QA.
4. Run the full QA process in `workflows/client-build-standards.md`.
5. **Post-launch changes:** edit `client.env` -> rerun `python build.py` -> FTP upload changed files.

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

## Plan Reference

| Plan | Price | City Pages | Key Inclusions |
|---|---|---|---|
| Local Presence | $997/mo | Up to 3 | City pages maintained monthly, emergency page, GBP managed, 150 directory listings, call tracking, review requests, monthly report |
| Lead Machine | $1,997/mo | Up to 8 | Everything in Local Presence + GBP monthly posts, 2 articles/mo, seasonal content, 4 links/mo, 10 competitors tracked, monthly strategy call |
| Market Leader | $3,497/mo | Up to 20 | Everything in Lead Machine + 4 articles/mo, 5–8 links/mo, Google LSA management, AI search optimization, 20 competitors tracked, dedicated account manager, 1 strategy call/mo |

**Billing:** Month-to-month. Cancel anytime with 30 days notice. No annual contracts.
**Revisions:** Initial site build includes 2 revision rounds. Monthly content updates do not require revision rounds.
**Ownership:** Client owns all site files and can move to any host at any time.
