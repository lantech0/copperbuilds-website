# Design Spec — Client Config + Build System
**Date:** 2026-05-10
**Status:** Awaiting user review

---

## Goal

Replace the current process of hardcoding all client data into HTML files with a single `client.env` config file per client. Claude reads the config during the build, generates a fully designed static HTML site, and uses the config as a single source of truth for all post-launch changes.

---

## Problem Being Solved

Today, client data (phone, SEO fields, nav links, external links) is baked into every HTML file. Changing one thing requires editing multiple pages manually. The config system separates content from structure — one file per client, all data in one place.

---

## Folder Structure

```
clients/active/priority-plumbing-2026-05/
  client.env                  ← config file (Claude populates, user reviews)
  01-welcome-email.md
  02-onboarding-questionnaire.md
  03-service-agreement.md
  06-client-brief.md
  index.html                  ← generated files live directly in the client folder
  services.html
  about.html
  contact.html
  blog.html
  cape-coral-plumber.html     ← one file per city in CITY_1..N
  blog-drain-cleaning.html    ← one file per blog post in BLOG_1..N
  sitemap.xml
```

---

## Config File — Full Format

Saved as `client.env` inside the client folder. Plain text, label=value format.

```bash
# ════════════════════════════════════════════════
#  LANTECH CLIENT CONFIG
#  [Business Name] — [City, State]
#  Claude populates this from the questionnaire.
#  Review and confirm before triggering the build.
# ════════════════════════════════════════════════

# ── BUSINESS INFO ────────────────────────────────
BUSINESS_NAME=
TAGLINE=
PHONE=
EMAIL=
ADDRESS=
HOURS=
YEARS_IN_BUSINESS=
LICENSE_NUMBER=
REVIEW_COUNT=
EMERGENCY_SERVICE=        # yes / no

# ── BRAND ────────────────────────────────────────
PRIMARY_COLOR=
ACCENT_COLOR=
FONT=

# ── EXTERNAL LINKS ───────────────────────────────
# Leave blank to hide the icon/link on the site
GOOGLE_BUSINESS=
FACEBOOK=
YELP=
NEXTDOOR=
BBB=
INSTAGRAM=

# ── FORM ─────────────────────────────────────────
WEB3FORMS_KEY=
FORM_BUTTON=Get a Free Estimate

# ── SERVICES ─────────────────────────────────────
SERVICE_1=
SERVICE_2=
SERVICE_3=
SERVICE_4=
SERVICE_5=
SERVICE_6=

# ── CITIES SERVED ────────────────────────────────
# A dedicated SEO page is auto-generated per city
CITY_1=
CITY_2=
CITY_3=
CITY_4=
CITY_5=

# ── SEO — HOME ───────────────────────────────────
HOME_TITLE=
HOME_META=

# ── SEO — SERVICES ───────────────────────────────
SERVICES_TITLE=
SERVICES_META=

# ── SEO — ABOUT ──────────────────────────────────
ABOUT_TITLE=
ABOUT_META=

# ── SEO — CONTACT ────────────────────────────────
CONTACT_TITLE=
CONTACT_META=

# ── SEO — BLOG INDEX ─────────────────────────────
BLOG_TITLE=
BLOG_META=

# ── INTERNAL LINKS — HOME ────────────────────────
HOME_LINK_1_TEXT=
HOME_LINK_1_URL=
HOME_LINK_2_TEXT=
HOME_LINK_2_URL=
HOME_LINK_3_TEXT=
HOME_LINK_3_URL=

# ── INTERNAL LINKS — SERVICES ────────────────────
SERVICES_LINK_1_TEXT=
SERVICES_LINK_1_URL=
SERVICES_LINK_2_TEXT=
SERVICES_LINK_2_URL=
SERVICES_LINK_3_TEXT=
SERVICES_LINK_3_URL=

# ── BLOG POSTS ───────────────────────────────────
# Claude writes the content file; enter details here after
BLOG_1_TITLE=
BLOG_1_META=
BLOG_1_FILE=
BLOG_2_TITLE=
BLOG_2_META=
BLOG_2_FILE=
BLOG_3_TITLE=
BLOG_3_META=
BLOG_3_FILE=
```

---

## What Claude Populates vs. What the User Confirms

| Field group | Who fills it | Source |
|---|---|---|
| Business info (name, phone, email, address, hours) | Claude | Questionnaire answers |
| Services list | Claude | Questionnaire answers |
| Cities served | Claude | Questionnaire answers |
| Emergency service flag | Claude | Questionnaire answers |
| Years in business, license, review count | Claude | Questionnaire answers |
| External links (GMB, Facebook, etc.) | Claude | Questionnaire answers |
| Brand colors + font | Claude | Questionnaire answers or brief |
| SEO titles + meta descriptions | Claude | Generated from business info + trade + city |
| Internal links | Claude | Generated based on SEO strategy (see below) |
| Web3Forms key | User | Provided after account setup |
| Blog post details | User | After Claude writes the blog content |

**User's job:** Review the populated file, confirm it looks right, fill the 1-2 fields Claude can't know (Web3Forms key).

---

## SEO Title + Meta Formula

Claude generates these using a consistent formula per page:

| Page | Title formula | Meta formula |
|---|---|---|
| Home | `[Trade] in [Primary City] \| [Business Name]` | `[USP sentence]. Call [Business Name] for [trade] in [city].` |
| Services | `[Trade] Services in [City] \| [Business Name]` | `[Service 1], [Service 2], and more. Serving [city] since [year].` |
| About | `About [Business Name] \| [City], [State]` | `[Years]-year-old [trade] company serving [city]. Licensed & insured.` |
| Contact | `Contact [Business Name] \| [City]` | `Call or message [Business Name] for fast [trade] service in [city].` |
| City page | `[Trade] in [City] \| [Business Name]` | `Licensed [trade] serving [city]. [USP]. Call [phone].` |

All titles stay under 60 characters. All meta descriptions stay under 160 characters.

---

## Internal Linking Strategy

Internal links are not random — Claude assigns them based on SEO value flow:

**Rule: High-traffic pages link down to conversion pages.**

| Page | Links to | Reason |
|---|---|---|
| Home | All service pages + primary city page | Passes authority to key pages |
| Services | Each individual service → city pages | Connects trade + location for local SEO |
| City pages | Services page + contact page | Drives conversion from location traffic |
| Blog posts | Relevant service page + relevant city page | Converts informational traffic to leads |
| About | Services page + contact page | Secondary trust → conversion path |

**Implementation in config:**
Claude fills `HOME_LINK_1..3`, `SERVICES_LINK_1..3` etc. based on this strategy — not generic "see more" links but specific anchor text with target keywords (e.g., "Drain Cleaning in Cape Coral" linking to `/cape-coral-plumber.html`).

**Anchor text rule:** Always descriptive keyword-rich text. Never "click here" or "learn more."

---

## Build Script Behavior

Script: `python build.py clients/active/[slug]/`

1. Reads `client.env`
2. Validates required fields (warns on blanks, does not crash)
3. Generates standard pages: `index.html`, `services.html`, `about.html`, `contact.html`, `blog.html`
4. Generates one city page per populated `CITY_N` field
5. Wraps each blog file (from `BLOG_N_FILE`) in the site template
6. Generates `sitemap.xml` listing all pages
7. Outputs everything directly into the client folder
8. Prints a checklist of what was generated and flags any blank required fields

---

## Workflow Integration

This slots into the existing `workflows/project.md` at Step 5 (Questionnaire Received):

**Old Step 5:** Fill in `06-client-brief.md` from questionnaire answers.
**New Step 5:** Fill in `06-client-brief.md` AND populate `client.env` from questionnaire answers.

**New Step 6 (Build):**
1. Claude reviews `client.env` — confirms all fields are populated
2. Claude reads config and runs `/lantech-build` using the config data
3. Output goes to `output/` folder
4. `build.py` generates final HTML wrapping Claude's output

**Post-launch changes:**
1. Open `client.env` in any text editor
2. Edit the field
3. Re-run `build.py`
4. FTP upload only the changed files from the client folder

---

## Edge Cases

**Client has no social profiles:** Leave `FACEBOOK=` blank — the icon does not render. No error.

**Client serves only one city:** Leave `CITY_2..5` blank — no extra city pages generated. Home SEO still targets that city.

**Client wants to add a blog post later:** Claude writes the content file, saves it to the client folder, user adds `BLOG_N_TITLE`, `BLOG_N_META`, `BLOG_N_FILE` to the config, reruns build.

**SEO titles exceed 60 characters:** Build script warns in the console output — does not block the build but flags it for manual review.

**Client changes phone number post-launch:** Update `PHONE=` in `client.env`, rerun `build.py`, re-upload all files in `output/`. Takes under 5 minutes.

---

## Out of Scope

- Visual design of pages (handled by `/lantech-build` + `/impeccable craft`)
- Hosting / FTP upload (handled by `workflows/deploy.md`)
- Monthly SEO content updates (handled by `workflows/maintenance.md`)
- The local SEO expert agent (separate build, separate spec)
