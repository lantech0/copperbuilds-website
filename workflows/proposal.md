# Workflow: Proposal Delivery

**Triggered by:** A discovery call ends with "send me something in writing" / "let me show my partner" / prospect asks for a quote before agreeing to a call
**Skill used:** `/market-proposal`
**Template:** `clients/templates/03-service-agreement.md` (after acceptance)
**Handoff to:** `workflows/project.md` when accepted

---

## Objective

Deliver a concise, personalized written proposal within 24 hours of the discovery call — one that reinforces the specific pain identified, presents one clear recommendation, and makes saying yes as easy as possible.

---

## Trigger

Run this workflow when:
- A discovery call ends without an immediate close and the prospect asks for something in writing
- The user says "generate proposal for [client name]"
- A prospect replies to outreach asking for a quote or pricing before agreeing to a call

---

## Required Inputs

Before writing a word:
- Prospect file at `clients/prospects/[file].md` — business name, owner name, contact info, gaps found, recommended plan, Est. Tier from service area capture
- Discovery call notes — objections raised, the revenue figure they mentioned, specific pain points in their words
- Recommended plan decided (Local Presence / Lead Machine / Market Leader) — do not write the proposal without a clear recommendation

If the recommended plan is not decided: use the Est. Tier from the prospect file (based on city count). If still unclear, decide from budget signals on the call. Do not present all three options.

---

## Steps

### Step 1 — Pull the Prospect File

Read `clients/prospects/[file].md`. Confirm you have:
- Business name and owner name
- Top 2–3 specific gaps found during the audit (specific — not "your SEO needs work")
- The revenue opportunity figure (from search volume research or the number they said on the call)
- Recommended plan and monthly price
- Any objection they raised on the call

Fill any missing fields from your call notes before proceeding.

### Step 2 — Invoke `/market-proposal`

Invoke the `/market-proposal` skill with these inputs:
- Business name and owner
- The 2–3 specific gaps (be concrete: "your site loads in 7s on mobile" beats "site speed issues")
- Revenue opportunity figure
- Recommended plan, monthly price, and its key inclusions
- Delivery timeline for the chosen package
- What happens next: agreement + invoice → questionnaire → build starts within 24 hours

**Proposal must be 1–2 pages max.** No filler, no agency jargon. Write to the business owner, not a boardroom. The prospect should be able to read it in 2 minutes and know exactly what they're getting and what it costs.

### Step 3 — Save the Proposal

Save the completed proposal to:
`clients/prospects/[slug]-proposal-YYYY-MM-DD.md`

Update the prospect file status: `[x] Proposal Sent — [YYYY-MM-DD]`

### Step 4 — Send Within 24 Hours of the Call

The faster the follow-up, the higher the close rate. Same day is ideal. Next morning is acceptable. Beyond 24 hours, momentum dies.

Email subject: `Your Lantech Proposal — [Business Name]`

Email body (keep it under 6 lines):
*"Hi [Name], great speaking with you [today/earlier this week]. Here's the proposal we discussed.*

*One page — covers what we found, what we'd build, and what it costs.*

*If you'd like to move forward, just reply and I'll send the agreement and invoice today. Your site would be live by [DATE based on package timeline].*

*Happy to answer any questions. — Luis"*

Paste the proposal inline if it's short. For longer proposals, attach as PDF (print `.md` to PDF first).

### Step 5 — Set Follow-Up Reminders

Set two reminders in the prospect file:

**3-business-day follow-up** (if no reply):
*"Hi [Name] — just checking in on the proposal. Any questions I can answer? Happy to jump on a quick call if that's easier."*

**7-business-day follow-up** (if still no reply after first follow-up):
*"Hi [Name] — last follow-up from me. The proposal is still valid if the timing works — just reply whenever you're ready."*

After 14 days with no response: mark as cold. No further contact unless they reach out.

### Step 6 — On Acceptance

When the prospect accepts (any version of "yes" / "let's do it" / "send me the paperwork"):

1. Send service agreement + invoice same day → `clients/templates/03-service-agreement.md`
2. Run `workflows/project.md` to create the client folder
3. Update prospect file: `[x] Closed — [YYYY-MM-DD]`

### Step 7 — On Decline or No Response (14 days)

1. Update prospect file: `[ ] Dead — [reason: declined / no response after 14 days]`
2. Send a graceful close (only if they declined actively — not for cold prospects):
   *"No worries at all — if anything changes down the road, we're here. Best of luck with [their business]. — Luis"*
3. No further contact.

---

## Required Outputs Before Considering Proposal Done

- [ ] Prospect file reviewed — all required inputs confirmed
- [ ] Recommended package decided before writing begins
- [ ] Proposal written via `/market-proposal` — specific, no placeholders, max 2 pages
- [ ] Proposal saved to `clients/prospects/[slug]-proposal-YYYY-MM-DD.md`
- [ ] Prospect file status updated: `[x] Proposal Sent — [date]`
- [ ] Email sent within 24 hours of discovery call
- [ ] 3-day and 7-day follow-up reminders noted in prospect file

---

## Edge Cases

**Prospect asks for multiple package options:**
Present maximum two — the recommended package and the one above it. Never list all three. Three options creates indecision. One clear recommendation with an upgrade option is enough.

**Prospect wants a discount:**
Do not discount the price. Adjust scope instead: *"I can't move on price, but I can start with the Starter package and we add local SEO in Phase 2 once you see results."* This protects your margin and gives them a path in.

**Prospect got a lower quote from someone else:**
*"I've seen cheaper quotes. The difference is what's built in — our sites include on-page SEO, proper schema markup, and Core Web Vitals optimization from day one. A $400 site that doesn't rank doesn't save you money."*

**Prospect wants to negotiate inclusions:**
Scope negotiation is fine. Price negotiation is not. You can add or remove items from the package — you cannot lower the package price.

**Prospect asks for a proposal before a discovery call:**
Send a brief intro and pricing overview, not the full proposal. Full proposals are personalized to the audit — you need the call first. Reply: *"Happy to share pricing — before I send a full proposal, I'd love to spend 15 minutes learning about your business so I can make sure the recommendation fits. Can we do a quick call this week?"*
