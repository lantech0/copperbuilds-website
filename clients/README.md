# Lantech — Client Document System

## Folder Structure

```
clients/
  templates/       ← master templates (never edit these directly)
  active/          ← one folder per active client project
  completed/       ← archived completed projects
```

---

## Templates

| File | When to use |
|------|-------------|
| `01-welcome-email.md` | Send immediately after payment is received |
| `02-onboarding-questionnaire.md` | Attached to welcome email — client fills this out |
| `03-service-agreement.md` | Sign before work begins (send with invoice) |
| `04-invoice.html` | Open in browser, print to PDF, send to client |
| `05-handover-package.md` | Complete and send on launch day |
| `06-client-brief-template.md` | Fill from questionnaire answers before starting the build |
| `07-discovery-call-script.md` | Pre-call confirmation, post-call follow-up, and objection cheat sheet |
| `08-preview-delivery-email.md` | Preview delivery, revision round updates, and approval confirmation |
| `09-post-launch-emails.md` | 30-day check-in, testimonial request, upsell follow-up, 90-day reactivation |

---

## Full Client Lifecycle

| Stage | Workflow | Templates used |
|---|---|---|
| Prospect replies to outreach | `workflows/discovery-call.md` | `07-discovery-call-script.md` |
| Lead closes | `workflows/project.md` | `03`, `04`, `01`, `02`, `06` |
| Build complete | `workflows/revisions.md` | `08-preview-delivery-email.md` |
| Client approves | `workflows/deploy.md` | `05-handover-package.md` |
| 30 days post-launch | `workflows/post-launch.md` | `09-post-launch-emails.md` |
| Portfolio | `workflows/portfolio-capture.md` | — |

---

## How to Use for a New Client

1. **Lead closes → run `workflows/project.md`** — it creates the folder and queues the right documents automatically

2. **Fill in all [PLACEHOLDERS]** in each document before sending

3. **Send documents in this order:**
   - Day 0 (deal closed): Service Agreement + Invoice
   - Day 0 (payment received): Welcome Email + Onboarding Questionnaire
   - After build: Preview link via `08-preview-delivery-email.md`
   - Launch day: Handover Package

4. **When project is complete:**
   Move `active/[client-name]/` → `completed/[client-name]/`

---

## Naming Convention for Client Folders

Use: `active/[business-name-slug]-[YYYY-MM]/`

Example: `active/joes-plumbing-2026-04/`
