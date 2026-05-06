# Workflow: Preview Delivery → Client Feedback → Revisions → Approval

**Triggered by:** Build passes all quality gates in `CLAUDE.md`
**Template used:** `clients/templates/08-preview-delivery-email.md`
**Handoff to:** `workflows/deploy.md` after final approval

---

## Objective

Deliver the preview to the client, collect structured feedback, complete revision rounds, get written approval, and hand off to deployment — without losing track of revision count or letting the client approve something informally.

---

## Step 1 — Prepare the Preview

Before sending anything:

1. Deploy the site to a staging URL on Hostinger (subdomain: `preview.[clientdomain].com` or use the hosting file manager to upload to a `/preview/` path)
   — OR if staging is not available: upload to the client's domain in a `/preview/` subfolder
   — Do NOT send a localhost link or a `file:///` path — the client cannot open these
2. Test the preview URL yourself first: all pages load, nav links work, contact form submits, mobile layout correct at 375px
3. Screenshot all pages at 1280px and 375px for your own reference

---

## Step 2 — Send the Preview Email

Use `clients/templates/08-preview-delivery-email.md`.

Key things the email must include:
- The live preview URL
- A clear list of what was built (pages, features)
- Instructions for how to give feedback (one consolidated list, not drip feedback)
- The revision round count: *"This is round 1 of your [2] included revision rounds."*
- The review deadline: *"Please send feedback within 3 business days. After that, this round is considered approved."*
- What counts as a revision vs. a new feature (out of scope = new quote)

---

## Step 3 — Revision Tracking

Maintain a revision log in the client folder: `clients/active/[slug]/REVISIONS.md`

Format:
```
## Round 1
Sent: [DATE]
Deadline: [DATE + 3 business days]
Feedback received: [DATE or PENDING]
Changes requested:
- [ ] [Change 1]
- [ ] [Change 2]
Completed: [DATE or PENDING]
Preview link updated: [DATE or PENDING]

## Round 2
...
```

Rules:
- A revision round = one consolidated list from the client. Multiple emails with scattered changes still count as one round.
- Changes that fall outside the original scope (new pages, new features, structural redesigns) are flagged as out of scope and quoted separately.
- After 2 rounds: any further changes are billed at $75–150/round. Inform the client before starting.

---

## Step 4 — Applying Revisions

For each round:

1. Copy the client's feedback into the revision log and check off items as you address them
2. Apply changes following the same build process from `CLAUDE.md` (screenshot → quality gates)
3. Re-run the full quality gate checklist after every round — not just the changed sections
4. Update the preview URL with the revised build
5. Send the round-complete email (template below in `08-preview-delivery-email.md`)

---

## Step 5 — Final Approval

After the last revision round (or whenever the client is satisfied):

Send the approval confirmation email asking for written sign-off:

*"Does the site look good to go? Reply 'approved' and we'll move to launch."*

Save their reply in the client folder as `APPROVAL.md` with the date.

Do not deploy without written approval.

---

## Step 6 — Trigger Deployment

With written approval in hand, run `workflows/deploy.md`.

---

## Required Outputs Before Considering Revisions Done

- [ ] Preview deployed to a URL the client can access (not localhost)
- [ ] Preview delivery email sent with revision count and deadline
- [ ] `REVISIONS.md` created in client folder
- [ ] All feedback items checked off after each round
- [ ] Quality gate re-run after each revision round
- [ ] Written approval saved as `APPROVAL.md`
- [ ] `workflows/deploy.md` triggered after approval
