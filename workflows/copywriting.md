# Workflow: copywriting — Standalone Marketing Copy Production

**Triggered by:** Any copy-only request — service page, landing page, homepage section, about page, CTA block, or hero copy — when HTML building is NOT the immediate next step.
**Handoff to:** `workflows/client-build-standards.md` (or `workflows/project.md`) when copy is approved and HTML build begins.

---

## Objective

Produce finished, ready-to-paste marketing copy from a brief, using the three-layer framework: SEO seed → AIDA/PAS draft → Vale gate + manual checklist.

---

## Trigger

Run this workflow when:
- User asks to "write copy for" or "draft the copy for" any page or section
- User asks for a homepage, services page, landing page, about page, or hero copy without immediately building HTML
- A client brief exists and copy needs to be written before the build starts
- Copy needs to be revised or rewritten as a standalone deliverable (not inside an active HTML file)

Do NOT run this workflow when:
- The user asks to rebuild an existing HTML page end-to-end — use the Page Rebuild Process in `CLAUDE.md` instead
- The user asks to audit or score existing copy at a URL — use `/market copy <url>` instead

---

## Required Inputs

Before starting, confirm all of these exist or can be derived from the conversation:

| Input | Source | Required? |
|---|---|---|
| Page type | User's request | Required |
| Target reader | User's request or `06-client-brief.md` | Required |
| Primary service + location | User's request or `06-client-brief.md` | Required |
| Brand voice | `BRAND-VOICE.md` (Lantech site) or `clients/active/[slug]/BRAND-VOICE.md` (client builds) | Required |
| Primary CTA | User's request or `06-client-brief.md` | Required |
| Keyword target | User's request, or derive from Layer 1 if not provided | Required — derive if missing |
| Home services buyer intelligence | `memory/research_home_services_marketing.md` | Load for all home services clients |
| Trade vocabulary | `memory/research_home_services_marketing.md` → relevant trade section | Load for all home services clients |

If a required input is missing and cannot be derived: ask one focused question before proceeding.

---

## Steps

### Step 1 — Load Context

Read in parallel:
- `COPY-STANDARDS.md` — readability targets, AIDA/PAS frameworks, Layer 3A/3B gates
- `BRAND-VOICE.md` (or `clients/active/[slug]/BRAND-VOICE.md` for client work)
- `memory/research_home_services_marketing.md` — buyer psychology, trade vocabulary, trust signals, CPL benchmarks

Extract from the brief:
- Page type and purpose (what should the reader DO after reading this page?)
- Target reader (homeowner? facility manager? general contractor?)
- Trade (HVAC? Roofing? Plumbing? etc.)
- Location (city + service area)
- Primary differentiator (what makes this business the right choice?)
- Primary CTA (call / form / booking?)

---

### Step 2 — Layer 1: SEO Seed

Establish what this page ranks for BEFORE writing a word of copy.

**For client builds:** Check `clients/active/[slug]/_keyword-map.md` — use the primary keyword already assigned to this page type. If the keyword map doesn't exist yet, derive from the client brief and note it in the output.

**For Lantech site pages:** Identify the keyword cluster based on the page purpose (e.g., "HVAC web design", "local SEO for plumbers", "home service website design").

Output a one-paragraph SEO seed before drafting copy:

```
SEO SEED
Primary keyword: [keyword]
Supporting keywords: [2-3 variants]
Search intent: [informational / navigational / transactional]
Page focus: [one sentence — what this page must answer for a searcher to click "satisfied"]
H1 target: [draft H1 that contains the primary keyword naturally]
```

The H1, first body paragraph, and at least two H2s must contain or directly support the seed keywords. The seed is the structural spine — all copy must prove it.

---

### Step 3 — Layer 2: Marketing Copy Draft

Draft the full copy using the SEO seed as the spine.

**Pick the framework that fits the reader's awareness stage (from `COPY-STANDARDS.md`):**
- Cold traffic (unaware/problem-aware) → PAS (Problem → Agitation → Solution)
- Warm traffic (solution-aware) → AIDA (Attention → Interest → Desire → Action)
- Comparison traffic (most-aware) → Lead with proof + differentiator

**Apply home services buyer psychology from `research_home_services_marketing.md`:**
- Use the exact vocabulary the trade uses (e.g., "air handler" not "indoor unit" for HVAC)
- Lead with fear/pain (something broke, it's getting worse, cost is uncertain)
- Resolve with speed + certainty + trust (licensed, insured, local, same-day)
- Use social proof in the desire section — "X homeowners in [city] have…"
- Make the CTA outcome-specific — what does the reader get, not what they do

**Required copy blocks by page type:**

| Page Type | Required Blocks |
|---|---|
| Homepage | Hero (H1 + deck + CTA) · Services summary (3 cards) · Trust bar · Social proof section · Secondary CTA |
| Service page | H1 + problem opener · How it works (3 steps) · What's included · Why us (3 differentiators) · FAQ (3-5 items) · CTA |
| Landing page | Hero (H1 + deck + CTA) · Problem/agitation · Solution framing · Proof section · Objection-handling · Final CTA |
| About page | Origin story opener · Mission statement · Team/owner bio · Values (3 items) · CTA |
| Hero section only | H1 + deck (2 sentences) + primary CTA + supporting trust line |

**Format output as plain copy — no HTML:**

```
[PAGE TYPE]: [Business name / Lantech]
---
H1: [headline]
HERO DECK: [1-2 sentences]
CTA BUTTON: [button label]

H2: [section heading]
BODY: [paragraph(s)]

[continue for each section]
```

---

### Step 4 — Layer 3A: Vale Gate

Run Vale on the draft copy:

```powershell
vale --config="C:\Users\User\LantechAI\copperbuilds\.vale.ini" --input [paste copy or point to .tmp file]
```

If the copy draft is in a `.tmp/` file:
```powershell
vale --config="C:\Users\User\LantechAI\copperbuilds\.vale.ini" "copperbuilds/.tmp/copy-[slug]-[page].txt"
```

**Save the draft to `.tmp/` first if it isn't already:**
Write the copy to `copperbuilds/.tmp/copy-[slug]-[page].txt` (e.g., `.tmp/copy-joes-plumbing-services.txt`) before running Vale.

**Fix every error before proceeding.** Warnings require judgment:
- Classify each warning as genuine fix or false positive in context
- Document reasoning for any warning left unfixed (e.g., "Vale flagged 'licensed and insured' as a cliché — retained because it's a literal trust signal, not marketing fluff")

---

### Step 5 — Layer 3B: Manual Checklist

Run the full manual checklist from `COPY-STANDARDS.md` § Layer 3B. Every item must be verified explicitly — not by feel.

Go line by line:

- [ ] No "We" sentence openers — restructure to lead with client, outcome, or problem
- [ ] No dangling modifiers
- [ ] No ambiguous pronoun antecedents
- [ ] No incomplete comparisons ("faster" → "faster than [X]")
- [ ] AIDA/PAS structure intact throughout
- [ ] Headline passes Ogilvy test (benefit / problem / news / story / quote)
- [ ] Hero passes 5-second test (Who? What? Who for? — no scrolling needed)
- [ ] Every CTA uses first-person possessive — "Get My Free Estimate" not "Get a Free Quote" not "Contact Us"
- [ ] No accidental fragments in body paragraphs
- [ ] Subject-verb agreement in complex sentences
- [ ] Apostrophe audit (its/it's, possessive plurals)
- [ ] Sentence length scan — split anything over 25 words
- [ ] Awareness stage match — copy entry point matches where cold traffic actually is

Fix every failure before proceeding. After fixing, re-run Vale if edits were substantial.

---

### Step 6 — Deliver for Review

Output the final approved copy in a clean format, ready to paste into HTML:

```
APPROVED COPY — [Page Type]: [Business / Page name]
Vale gate: PASS ([N] warnings — [N] genuine fixes, [N] false positives]
Layer 3B gate: PASS
---
[formatted copy blocks]
```

Also state: what goes into each HTML section (map copy blocks to HTML structure).

If the copy is for a client build: save it to `clients/active/[slug]/copy-[page].md` — not just `.tmp/`.
If the copy is for the Lantech site: save it to `.tmp/copy-[page].txt` only — it will be pulled into HTML at build time.

---

## Required Outputs

- [ ] SEO seed documented (primary keyword, supporting keywords, search intent, H1 target)
- [ ] Full copy draft covering all required blocks for the page type
- [ ] Vale gate: PASS (errors: 0, warnings classified and documented)
- [ ] Layer 3B checklist: all 13 items explicitly verified
- [ ] Final copy delivered in clean labeled format ready for HTML insertion
- [ ] Copy saved to correct path (client folder or `.tmp/` per above)

---

## Edge Cases

**Missing keyword data (no keyword map for client):**
Derive from the client brief (service + location + most common transactional query). State the assumption: "Keyword map not found — using '[keyword]' derived from brief. Verify with `/lantech-seo [slug]` before final approval." Do not block copy production on this.

**Client provides their own copy draft:**
Start at Layer 3A — run Vale on their draft first, then Layer 3B. State at the top: "Client draft received — running quality gates only, not writing from scratch." If the client draft requires heavy revision, flag it before editing extensively.

**Vale is not installed or fails:**
Run `winget install --id errata-ai.Vale` then `vale sync` from `copperbuilds/`. If still failing, run the Layer 3B manual checklist manually and note: "Vale gate skipped — tool unavailable; manual checklist run instead."

**Copy is for an unfamiliar trade or sector:**
Read the relevant trade section in `memory/research_home_services_marketing.md`. If the trade isn't in memory, run `/deep-research [trade] local marketing buyer psychology` before drafting.

**Copy needs to match a client's existing brand voice and the BRAND-VOICE.md is missing:**
Do not invent a brand voice. Ask: "I need [client]'s brand voice file before drafting. Do you have their BRAND-VOICE.md, or should I run `/market brand <url>` to generate one from their existing content?"
