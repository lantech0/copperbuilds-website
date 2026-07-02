# Workflow: Client Offboarding

**Triggered by:** Client requests to end the relationship, maintenance retainer is cancelled, or project is fully complete with no ongoing services
**Handoff from:** `workflows/post-launch.md` (upsell declined at 90 days) or direct client request

---

## Objective

Close the client relationship cleanly — hand over every file and access they own, remove CopperBuilds from their accounts, send a graceful goodbye, and archive everything so nothing is left dangling.

---

## Trigger

Run this workflow when:
- A client confirms they are cancelling their maintenance retainer
- A client says they no longer need services and requests their files
- A one-time project client (no retainer) has had their 30-day support window expire and you're formally closing the file
- The user says "offboard [client name]"

---

## Required Inputs

- Client folder at `clients/active/[slug]/` or `clients/completed/[slug]/`
- `05-handover-package.md` — contains site files, credentials, and access details
- `LAUNCH-SUMMARY.md` — GA4 ID, GSC property URL, hosting details
- Client's Google account email (from `02-onboarding-questionnaire.md`)
- Outstanding invoice status

---

## Steps

### Step 1 — Confirm Offboarding Is Intentional

Before doing anything irreversible, confirm this isn't a billing issue or a misunderstanding:

Send a brief reply:
*"Hi [Name], just want to confirm — are you looking to cancel your [maintenance plan / services] entirely, or is there something specific we can fix? Happy to chat for 5 minutes if anything isn't working."*

Wait for explicit confirmation before proceeding. If it's a billing issue, resolve it and do not offboard.

If they confirm offboarding: note the date and reason in the client folder — add `OFFBOARDING.md`:
```
Date requested: YYYY-MM-DD
Reason: [their words or summary]
Outstanding balance: [$X / none]
Final service date: YYYY-MM-DD
```

---

### Step 2 — Settle Any Outstanding Balance

Check for any unbilled work:
- Out-of-scope hours logged in maintenance log
- Any revision rounds beyond the included 2
- Final month's retainer (pro-rated if mid-month cancellation)

If a balance exists: send a final invoice before delivering files. Do not release assets until payment is confirmed.

If no balance: proceed to Step 3.

---

### Step 3 — Share the Google Drive Folder with the Client

Before preparing the file handover, give the client access to their own Drive folder so they have all documents in one place — agreements, reports, brief, handover package — without needing to dig through emails.

1. Read the Drive folder ID from `clients/active/[slug]/DRIVE-FOLDER.md`
2. Open the folder in Google Drive
3. Share it with the client's Google account email (from Q27a in `02-onboarding-questionnaire.md`)
   - Permission: **Editor** (so they can download everything)
4. Make sure all documents are present in the folder before sharing:
   - Service agreement ✅
   - Invoice ✅
   - Completed questionnaire ✅
   - Client brief ✅
   - Handover package (upload now if not already there)
   - All monthly reports (if applicable)
   - Maintenance agreement (if applicable)
5. In the offboarding email (Step 8), include the Drive folder link so they know it exists.

---

### Step 3b — Prepare the File Handover Package

Gather everything the client owns:
- All HTML/CSS/JS source files (zip the full project folder)
- All images used on the site
- Logo files (if CopperBuilds designed or stored them)
- `06-client-brief.md` — their business brief
- The keyword map (`_keyword-map.md`)
- Any blog posts written for them
- Any GBP post drafts from maintenance

Save the zip as: `clients/active/[slug]/handover/[slug]-full-handover.zip`

Email subject: `[Business Name] — Your Website Files`

Body:
*"Hi [Name], attached are all your website files — you own these outright. Everything is included: HTML pages, images, and your keyword research. Any developer you work with in the future can host these as-is.*

*I'll be removing CopperBuilds' access from your Google Analytics and Search Console over the next 24 hours. If you need anything from us in the future, we're always here."*

---

### Step 4 — Transfer Platform Access

Transfer ownership of all tools where the client should be the primary owner:

**Google Analytics 4:**
1. GA4 → Admin → Account → Account Access Management
2. Change client's role from Viewer → **Administrator**
3. Remove `luis.copperbuilds@gmail.com` from the property

**Google Search Console:**
1. GSC → Settings → Users and permissions
2. If CopperBuilds is the verified owner: add client as an **Owner** first, then remove CopperBuilds
3. Confirm client can see the property before you remove yourself — if they lose access, verification is gone

**Hosting (Hostinger):**
- If the site is under CopperBuilds' Hostinger plan: transfer the files to the client's own hosting account, or arrange transfer of the hosting plan
- Provide full FTP credentials to the client in the handover email
- If the site is already on the client's own hosting: confirm they have all login credentials

**Domain:**
- If the domain is registered under CopperBuilds' account: initiate a domain transfer to the client
- Hostinger: Domains → select domain → Transfer domain → follow instructions
- If already under client's account: no action needed

---

### Step 5 — Revoke CopperBuilds Access

After confirming the client has full access to everything:
- Remove `luis.copperbuilds@gmail.com` from GA4 (Step 4 above)
- Remove from GSC (Step 4 above)
- Delete stored hosting/FTP credentials from CopperBuilds' password manager
- Remove client's Google account email from any internal tracking files

---

### Step 6 — Trigger Portfolio Capture (if not done)

If a case study hasn't been written yet: run `workflows/portfolio-capture.md` before archiving. You want the result on record while the project is still fresh.

---

### Step 7 — Archive the Client Folder

Move client folder from `clients/active/[slug]/` → `clients/completed/[slug]/` (if not already there).

Also move the client's Google Drive folder from `Lantech Agency — Active Clients` → `Lantech Agency — Completed Clients` (folder ID: `1vdoX-BqzvheszHFUaP-Zw2ney48QCk5G`):
1. Use `mcp__claude_ai_Google_Drive__move_item_to_folder` (or search for the move equivalent) to relocate the client folder
2. Update `DRIVE-FOLDER.md` with the new location note: `Archived: YYYY-MM-DD`

Add a final note to `OFFBOARDING.md`:
```
Offboarding completed: YYYY-MM-DD
Files delivered: yes
Access transferred: GA4 ✅ / GSC ✅ / Hosting ✅ / Domain ✅
Outstanding balance: settled / none
Case study: done / skipped (reason)
```

---

### Step 8 — Send the Graceful Goodbye

Within 24 hours of completing Steps 3–5:

Subject: `Thank you — [Business Name]`

*"Hi [Name], everything is wrapped up on our end. Your files are on their way / delivered, and I've transferred all account access to you.*

*It's been a pleasure working with [Business Name]. If you ever need anything down the road — new pages, SEO help, or a refresh — we're here.*

*Best of luck. — Luis"*

Keep it warm and short. No guilt-tripping, no last-ditch sales pitch.

---

## Required Outputs Before Considering Offboarding Done

- [ ] Client confirmed offboarding is intentional (not a billing issue)
- [ ] `OFFBOARDING.md` created in client folder with date, reason, and balance status
- [ ] Outstanding balance settled (invoice sent and paid, or confirmed as zero)
- [ ] Google Drive folder: all documents present and confirmed
- [ ] Google Drive folder shared with client (Editor access) — folder link noted
- [ ] Site files packaged and delivered to client (zip + Drive)
- [ ] GA4: client promoted to Admin, CopperBuilds removed
- [ ] GSC: client added as Owner, CopperBuilds removed
- [ ] Hosting credentials provided or transfer initiated
- [ ] Domain transfer initiated (if domain is under CopperBuilds' account)
- [ ] CopperBuilds access revoked from all platforms
- [ ] `workflows/portfolio-capture.md` triggered (if case study not yet done)
- [ ] Client local folder archived to `clients/completed/`
- [ ] Google Drive folder moved to Completed Clients folder — `DRIVE-FOLDER.md` updated
- [ ] `OFFBOARDING.md` updated with completion notes
- [ ] Goodbye email sent — Drive folder link included

---

## Edge Cases

**Client is unreachable and stops paying:**
Send one final email: *"Hi [Name] — I haven't heard back in [X weeks]. I'm closing your account and retaining your files for 90 days in case you'd like to restart. After that, your files will be deleted."* Archive immediately. Do not chase further.

**Client wants to stay on hosting but end the retainer:**
No problem — just offboard the retainer relationship (Steps 1, 2, 8). Keep the site live, hand over FTP credentials, remove yourself from the project. The site stays up, you just stop being responsible for it.

**Domain is close to expiry:**
Flag it explicitly in the goodbye email: *"Note: your domain [domain.com] expires on [DATE]. Make sure you renew it through [registrar] before then — if it lapses, you could lose the domain."* This is a goodwill move that they'll remember.

**Client asks to come back:**
Treat them like a new prospect — run `workflows/discovery-call.md`. Don't give a loyalty discount unprompted, but don't penalize them either.
