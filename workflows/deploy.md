# Workflow: FTP Deploy → Go Live

**Triggered by:** Written client approval saved in `APPROVAL.md` (`workflows/revisions.md`)
**Handoff to:** `workflows/post-launch.md` (30-day follow-up) after launch confirmed

---

## Objective

Deploy the approved static HTML site to Hostinger via FTP, verify the live site is correct, and send the handover package to the client on launch day.

---

## Pre-Deploy Checklist

Run this before touching FTP. All items must pass.

- [ ] `APPROVAL.md` exists in client folder with written approval and date
- [ ] All revision rounds complete — no open feedback items in `REVISIONS.md`
- [ ] Local build passes full quality gate from `CLAUDE.md` (visual + structural + performance + launch smoke test)
- [ ] `sitemap.xml` exists in the project root
- [ ] `robots.txt` exists in the project root
- [ ] `favicon.png` exists in the project root
- [ ] Contact form tested locally — submits without error
- [ ] No placeholder text, no lorem ipsum, no `href="#"` links, no fake phone numbers
- [ ] All images have alt text
- [ ] Google Analytics tag installed (if client provided GA4 ID in questionnaire)

---

## Step 1 — Collect Hosting Credentials

You need:
- Hostinger hPanel login (email + password)
- Domain the site is going on
- FTP host, username, and password (from hPanel → Hosting → FTP Accounts)

These should be in one of two places:
- The client's questionnaire (`02-onboarding-questionnaire.md`) — if they have existing hosting
- Your own Hostinger account — if you're hosting it under CopperBuilds' plan

**Never store credentials in a committed file.** Keep them in your password manager only.

---

## Step 2 — Upload via Hostinger File Manager

Option A (recommended for first launch — no FTP client needed):

1. Log in to [hpanel.hostinger.com](https://hpanel.hostinger.com)
2. Select the domain → **Files** → **File Manager**
3. Navigate to `public_html/`
4. If there's an existing site: rename the old folder to `_old-site-backup/` — do not delete it yet
5. Upload all project files:
   - `index.html`
   - `services.html`, `about.html`, `contact.html`, etc.
   - `sitemap.xml`
   - `robots.txt`
   - `favicon.png`
   - Any image files (`/images/` folder if applicable)
6. Confirm file permissions: HTML and XML files should be `644`, folders `755`

Option B (FTP client — FileZilla):

1. Open FileZilla
2. Connect: Host = `ftp.[clientdomain].com`, Username = [FTP user], Password = [FTP password], Port = `21`
3. In the remote panel, navigate to `public_html/`
4. Drag all project files from local panel to remote `public_html/`
5. Confirm upload completes with no errors

---

## Step 3 — Verify the Live Site

After upload, wait 2–5 minutes for DNS/cache to propagate, then verify:

- [ ] Homepage loads at `https://[DOMAIN]/` (not http — must have SSL padlock)
- [ ] All nav links work — click every page
- [ ] Contact form submits successfully (send a test message to yourself)
- [ ] Mobile layout at 375px — check with browser dev tools
- [ ] No console errors (F12 → Console in Chrome)
- [ ] SSL certificate is active (green padlock in address bar)
- [ ] `https://[DOMAIN]/sitemap.xml` loads correctly
- [ ] `https://[DOMAIN]/robots.txt` loads correctly

If anything fails: fix it before sending the handover package. Do not tell the client it's live until all items pass.

---

## Step 4 — Analytics & Search Console Setup

Run `workflows/analytics-setup.md` in full. This covers:
- Google Analytics 4: property creation, tag installation, conversion setup, client access
- Google Search Console: property creation, ownership verification, sitemap submission, indexing requests, GSC ↔ GA4 link, client access

Do not abbreviate or skip steps in that workflow — every item feeds into monthly reporting. The client's first monthly report is only as good as what gets set up here.

After completing `analytics-setup.md`: confirm the `LAUNCH-SUMMARY.md` has all IDs and access details logged before moving to Step 5.

---

## Step 5 — Remove the Preview Subdomain / Folder

If you deployed a preview earlier:
- Delete or unpublish the `/preview/` folder from `public_html/`
- If it was a subdomain: remove the subdomain from hPanel → Domains → Subdomains

---

## Step 6 — Send the Handover Package

Fill in all placeholders in `clients/templates/05-handover-package.md`:
- Live URL
- Launch date
- Hosting credentials (masked — direct client to password manager or include separately)
- GSC property URL and sitemap URL
- GA4 tracking ID (if installed)
- GBP status (if included in package)
- 30-day support expiry date
- Google Drive folder URL (from `DRIVE-FOLDER.md`) — tell them this is where all their documents live

Upload the completed handover package to the client's Google Drive folder:
1. Read the Drive folder ID from `clients/active/[slug]/DRIVE-FOLDER.md`
2. Use `mcp__claude_ai_Google_Drive__create_file` to upload `05-handover-package.md`

Send via email with subject: `[Business Name] is live — your handover package`

---

## Step 7 — Archive the Project

1. Move client folder from `clients/active/[slug]/` → `clients/completed/[slug]/`
   Also move the client's Google Drive folder from "Lantech Agency → Clients" → "Lantech Agency → Completed" (ID: `1vdoX-BqzvheszHFUaP-Zw2ney48QCk5G`)
2. Add a `LAUNCH-SUMMARY.md` to the completed folder:
   ```
   Business: [Business Name]
   Package: [PACKAGE]
   Launch date: [DATE]
   Live URL: [URL]
   Pages built: [N]
   Revision rounds used: [N of 2]
   Notable details: [anything useful for portfolio or case study]
   ```
3. Trigger `workflows/portfolio-capture.md` — don't skip this step

---

## Step 8 — Trigger Post-Launch Follow-Up

Set a calendar reminder for 30 days from launch date to run `workflows/post-launch.md`.

---

## Required Outputs Before Considering Deploy Done

- [ ] Pre-deploy checklist fully passed
- [ ] All files uploaded and live at `https://[DOMAIN]/`
- [ ] Live site smoke test passed (all 7 items)
- [ ] GSC property added and sitemap submitted
- [ ] Preview subdomain/folder removed
- [ ] Handover package sent to client
- [ ] Project archived to `clients/completed/`
- [ ] `LAUNCH-SUMMARY.md` created
- [ ] `workflows/portfolio-capture.md` triggered
- [ ] 30-day follow-up reminder set
