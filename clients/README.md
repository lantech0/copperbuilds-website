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

---

## How to Use for a New Client

1. **Deal closed → copy the templates folder:**
   Duplicate `templates/` into `active/[client-business-name]/`

2. **Fill in all [PLACEHOLDERS]** in each document

3. **Send documents in this order:**
   - Day 0 (deal closed): Service Agreement + Invoice
   - Day 0 (payment received): Welcome Email + Onboarding Questionnaire
   - Day 5 (launch day): Handover Package

4. **When project is complete:**
   Move `active/[client-name]/` → `completed/[client-name]/`

---

## Naming Convention for Client Folders

Use: `active/[business-name-slug]-[YYYY-MM]/`

Example: `active/joes-plumbing-2026-04/`
