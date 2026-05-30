# Workflow: Session Start Dashboard

**Triggered by:** Opening the copperbuilds workstation (first message of every session)
**Output:** Displayed in chat — not saved to a file

---

## Steps

### Step 0 — Load Memory + Wiki Context

1. Read `C:\Users\User\.claude\projects\C--Users-User-LantechAI\memory\MEMORY.md` — scan the index, pull any entries relevant to today's work.
2. Read `C:\Users\User\LantechAI\claude-obsidian\wiki\hot.md` — recent cross-session context. Load silently. Skip if missing.

---

### Step 1 — Read Active Client Builds
List all folders in `clients/active/`. For each:
- Client name and slug
- Check if `06-client-brief.md` is complete (build started = yes)
- Check if `APPROVAL.md` exists (approved for deploy = yes)
- Check if `REVISIONS.md` exists (in revision stage = yes)
- Determine stage: Brief → Build → Revisions → Approved → Deploying

### Step 2 — Read Pending Prospects
Scan `.md` files in `projects/prospects/`. Look for leads where status shows `[x] Call Booked` or `[x] Replied` but NOT `[x] Closed` or `[x] Dead`. Note the business name and next action.

### Step 2.5 — Check Recurring Clients

Scan `clients/active/` and `clients/completed/` for clients with ongoing services:

**Monthly reports due:** For each client folder that contains a `monthly-reports/` subfolder, check if a report for the current month (YYYY-MM) exists. If not, it's due.

**Maintenance due:** For each client folder that contains a `maintenance-log.md`, read the last entry. If it doesn't contain the current month, maintenance is due.

**Proposals awaiting response:** Scan `clients/prospects/` for files containing `[x] Proposal Sent` but NOT `[x] Closed` or `[x] Dead`. Calculate days since sent.

---

### Step 3 — Check CopperBuilds Site Page Status
The CopperBuilds site has 7 pages: `index.html`, `services.html`, `about.html`, `contact.html`, `blog.html`, `help.html`, `pricing.html`.
Check which are present and up to date (look for `--bg: #FAFAF7` and `CopperBuilds` in each file).
Report each as: ✅ OK | ⚠️ Needs attention

### Step 4 — Check Recent Completions
List the most recently modified folder in `clients/completed/`. Note client name and what was delivered.

### Step 5 — Display the Dashboard

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  COPPERBUILDS AGENCY — SESSION DASHBOARD
  [Today's date]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ORCHESTRATOR
  /luisweb [job]  ← use this for all jobs

  Examples:
    /luisweb build website for [client]
    /luisweb rebuild [page] page
    /luisweb prospect [sector] in [location]
    /luisweb qa [page].html
    /luisweb blog [topic]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ACTIVE CLIENT BUILDS ([N] total)

  [Client name]
    Stage:   [Brief / Build / Revisions / Approved / Deploying]
    Package: [Launch / Starter / Growth / Pro]
    Action:  [e.g. "Run workflows/revisions.md — preview ready to send"]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PENDING PROSPECTS ([N] awaiting action)

  [Business name] — [🔥 Hot / ⚡ Warm]
    Status:  [e.g. "Replied — book a call"]
    Action:  [e.g. "Run workflows/discovery-call.md"]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RECURRING CLIENTS

  REPORTS DUE THIS MONTH ([N])
    [Client name] — [Basic/Standard/Pro] — no report yet for [Month YYYY]
    Action: Run workflows/monthly-report.md

  MAINTENANCE DUE THIS MONTH ([N])
    [Client name] — [Basic/Standard/Pro] — last check: [Month YYYY]
    Action: Run workflows/maintenance.md

  PROPOSALS AWAITING RESPONSE ([N])
    [Business name] — sent [X] days ago — follow-up due [date]
    Action: Send follow-up email (see workflows/proposal.md Step 5)

  [If nothing in any of the 3 sub-sections: "No recurring tasks this month"]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
COPPERBUILDS SITE — PAGE STATUS

  index.html      [✅ Rebuilt / ⚠️ Needs rebuild]
  services.html   [✅ Rebuilt / ⚠️ Needs rebuild]
  about.html      [✅ Rebuilt / ⚠️ Needs rebuild]
  contact.html    [✅ Rebuilt / ⚠️ Needs rebuild]
  blog.html       [✅ Rebuilt / ⚠️ Needs rebuild]
  help.html       [✅ Rebuilt / ⚠️ Needs rebuild]
  pricing.html    [✅ Rebuilt / ⚠️ Needs rebuild]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RECENT WORK

  [Client name or page] — [What was completed]
  [Or: "No recent completions found"]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
UPCOMING

  [Any visible deadlines from active client files]
  [Or: "Nothing scheduled — check active client files"]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Edge Cases
- `clients/active/` empty → "No active builds"
- `projects/prospects/` missing → "No prospect files found"
- File read fails → note "Could not read [file]" rather than skipping silently
- Page file missing → mark as "⚠️ File not found"
