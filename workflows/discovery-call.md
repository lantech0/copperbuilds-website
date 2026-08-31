# Workflow: Discovery Call → Close

**Triggered by:** A prospect replies to outreach and agrees to a call (from `workflows/prospect.md`)
**Runs first:** `workflows/lite-audit.md` — run immediately once the call is booked, before Pre-Call Prep
**Template used:** `clients/templates/07-discovery-call-script.md`
**Handoff to:** `workflows/project.md` when closed

---

## Objective

Run a structured 20-minute call that qualifies the prospect, surfaces their real pain, and closes them on a CopperBuilds package — or identifies why they're not a fit right now.

## Pre-Call Prep (5 minutes before the call)

1. Pull the prospect's entry from `projects/prospects/[file].md`
2. Confirm `workflows/lite-audit.md` has already run for this prospect (it should have run right after the call was booked) — if not, run it now before continuing
3. Open their Google Business Profile
4. Note the top 2–3 specific gaps from the lite audit (missing schema / broken sitemap / slow LCP / no meta descriptions / etc. — or no website / dormant Facebook if `lite-audit.md` didn't apply)
5. Note the Gold Standard competitor you researched and the revenue opportunity figure
6. Know which package you're recommending before the call starts — don't figure it out on the call

---

## Call Structure

### Opening (2 min)
- Introduce yourself: *"Hi [Name], I'm [Your Name] from CopperBuilds — thanks for taking the time."*
- Set the agenda: *"I wanted to spend about 20 minutes learning more about your business and showing you what we found. Sound good?"*

### Discovery (8 min)
Ask these 4 questions. Listen more than you talk.

1. **"How are customers finding you right now?"**
   — You want to hear: word of mouth, referrals, repeat business. That's a person who needs online presence.

2. **"Have you ever had a website, or tried any marketing before? How did it go?"**
   — Surfaces past bad experiences. If they were burned before, address it directly.

3. **"If you had 5 new customers a month coming in from Google, what would that mean for your business?"**
   — Gets them to say the revenue number out loud. Makes the price feel small.

4. **"What's holding you back from having a professional web presence right now?"**
   — Surfaces real objections before you pitch. You want to hear them now, not after your pitch.

### The Pitch (6 min)
Lead with the gap you found. Be specific — never generic.

*"Here's what we found when we looked at your situation:*
*[Competitor name] is ranking for '[primary keyword]' and they're pulling in an estimated [N,NNN] searches a month. You're not showing up at all — which means those customers are going to them.*
*Based on the [sector] search volume in [location], you're missing roughly [revenue opportunity] a month in customers who can't find you."*

Then introduce the solution:
*"What we do is build you a professional, fast website that ranks on Google for your local keywords — and we do it in 14 days, not months. No templates, no AI-generated junk. A real site built for your business specifically."*

Present one recommended package. Don't offer all three at once.

*"For your situation, I'd recommend our [PLAN] at $[PRICE]/mo. That includes [KEY INCLUSIONS]. It's month-to-month — cancel anytime with 30 days notice, no annual contract."*

**Show the design demo (30 seconds):**
Before moving to objections, pull up the portfolio demo that matches their trade. Browse `copperbuilds/portfolio/` for the closest trade match. One sentence:
*"Here's an example of a [trade] site we built — this is the style we'd use for you."*
Do not show more than one demo. One direction, one demo, move on. Showing options creates doubt.

### Handle Objections (2 min)

| Objection | Response |
|---|---|
| "Too expensive" | *"I hear you. Compare it to what [competitor] is making off those [N,NNN] monthly searches — $[PRICE] is one or two jobs you're already losing every month."* |
| "I'll think about it" | *"Totally fair. What specifically do you want to think over? I want to make sure you have the right information."* — then book a follow-up before hanging up |
| "I'll do it myself" | *"Most of our clients tried that first. The issue isn't building the site — it's getting it to rank on Google. That's where we add the real value."* |
| "I don't trust online agencies" | *"That's exactly why we're month-to-month — no annual contracts, cancel with 30 days notice. You pay for results every month. You own all your site files and can move them anywhere. We don't survive on lock-in."* |
| "I already have a website" | *"I took a look at it. [Specific finding — e.g. 'It's not mobile-friendly' / 'It's missing local schema' / 'It loads in 6 seconds on mobile']. That's costing you Google rankings right now."* |
| "Not right now" | See follow-up sequence below |

### Close (2 min)
If they're ready:
*"Great — here's how it works: I'll send you the service agreement and invoice today. Once that's signed and payment is in, you'll get a welcome email with the onboarding questionnaire. Fill that out and we start building within 24 hours. Your site goes live in [TIMELINE]."*

If they want to think:
Book a specific follow-up: *"When's a good time to reconnect — would [DATE/TIME] work?"*
Then send the follow-up email from `clients/templates/07-discovery-call-script.md` within 1 hour.

---

## Post-Call Actions

**If closed:**
1. Send service agreement + invoice (same day) → `clients/templates/03-service-agreement.md` + `clients/templates/04-invoice.html`
2. Run `workflows/project.md` to create the client folder
3. Mark lead status in prospect file: `[x] Call Booked → [x] Closed`

**If not closed (follow-up):**
1. Send follow-up email within 1 hour (see script template)
2. Note the specific objection and follow-up date in the prospect file
3. Mark lead status: `[x] Call Booked → [ ] Closed / [ ] Dead`
4. Set a calendar reminder for the follow-up date

**If not a fit:**
1. Mark lead: `[ ] Dead` with a reason note
2. No further contact

---

## Required Outputs Before Considering the Call Done

- [ ] Call notes added to the prospect file (outcome, objections raised, follow-up date if applicable)
- [ ] Lead status updated in prospect file
- [ ] If closed: service agreement + invoice sent same day
- [ ] If not closed: follow-up email sent within 1 hour and reminder set
- [ ] `workflows/project.md` triggered if closed
