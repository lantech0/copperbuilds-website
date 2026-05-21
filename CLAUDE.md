# CLAUDE.md — CopperBuilds Agency Website

## Session Start — Run This First
**On the first message of every session, before responding to anything else:**
Run `workflows/session-start.md` — read client and prospect files, check page rebuild status, then display the session dashboard. Do this automatically. Do not wait to be asked.

## Workstation Purpose
Building and maintaining the **CopperBuilds** web agency website targeting small local businesses.
Stack: Static HTML/CSS/JS · Hosted on Hostinger · `serve.mjs` dev server at localhost:3000

## WAT Workflows
Read the relevant workflow before starting any process — it defines every required output.

| Workflow | When to use |
|----------|-------------|
| `workflows/session-start.md` | **Automatic — run on every session open before anything else** |
| `workflows/prospect.md` | Before running `/prospect` — any prospecting session |
| `workflows/discovery-call.md` | When a prospect agrees to a call — pre-call prep, call structure, close |
| `workflows/project.md` | When a lead closes — creates client folder, queues onboarding |
| `workflows/revisions.md` | After build passes QA — preview delivery, feedback, revision tracking |
| `workflows/deploy.md` | After client approves — FTP upload, go-live, handover |
| `workflows/post-launch.md` | 30 days after launch — check-in, testimonial, upsell |
| `workflows/portfolio-capture.md` | After every launch — screenshot, case study, portfolio page update |
| `workflows/proposal.md` | When prospect wants a written proposal before signing — bridges discovery-call and project.md |
| `workflows/offboarding.md` | When a client ends the relationship — file handover, access transfer, graceful close |
| `workflows/copywriting.md` | When writing marketing copy from a brief — service pages, landing pages, homepage sections, about pages, hero copy — WITHOUT immediately building HTML |
| `workflows/analytics-setup.md` | Immediately after live site smoke test — GA4 + GSC setup, tagging, conversions, access |
| `workflows/monthly-report.md` | Start of each month — generate and deliver client performance report |
| `workflows/maintenance.md` | Start of each month — run maintenance retainer checks and updates |
| `workflows/seo-retainer.md` | Start of each month for any client on Local Presence, Lead Machine, or Market Leader retainer — collect client assets, execute GBP/blog/citations/links, feed into monthly-report.md |
| `workflows/client-build-standards.md` | During every client site build — UX standards, Core Web Vitals gates, pre-launch smoke test |

---

## Always Do First
- **Read `DESIGN.md`** before writing any frontend code — it is the single source of truth for all visual decisions.
- **Invoke the `frontend-design` skill** before writing any frontend code, every session, no exceptions.

## Page Rebuild Process — FOLLOW THIS EXACTLY

This is the correct process for rebuilding any page — Lantech site and all client builds. Do NOT skip to coding directly.

**Three-Layer Copy Framework:** Every page is built in this order — SEO Seed first, Marketing Copy second, Grammar & Structure third. Never reverse the order. Full framework documented in `COPY-STANDARDS.md`.

1. **Invoke `frontend-design` skill** — required before any frontend work (every session)

2. **Layer 1 — SEO Seed**: Establish the keyword target before writing a single word
   - Client builds: run `/lantech-seo [client-slug]` — validates real keyword volumes via DataForSEO, outputs target phrases, titles, meta, schema, and SEO action plan
   - Lantech site pages: identify the primary keyword cluster for this page (e.g., "web design for home service businesses", "local SEO for HVAC contractors")
   - Every H1, H2, and first body paragraph must contain or directly support the seed keywords
   - The seed is the thesis — the rest of the copy proves it

3. **Layer 2 — Marketing Copy**: Draft copy using the SEO seed as the spine
   - Read `COPY-STANDARDS.md` — readability targets, AIDA/PAS frameworks, headline rules, CTA rules
   - Client builds: also read `clients/active/[slug]/BRAND-VOICE.md` — brand voice and vocabulary override Lantech defaults for client work
   - Run `/impeccable craft` — shape discovery interviews establish page purpose and target reader, design brief is confirmed before code starts, copy is drafted using seed keywords + marketing framework + brand voice

4. **Layer 3A — Mechanical Gate**: Run `/vale-check` on the copy draft
   - Vale flags passive voice, weak CTAs, banned phrases, corporate jargon, terminology inconsistencies
   - Fix every error before proceeding. Warnings require judgment — classify each one as genuine fix or false positive in context. Document reasoning for any warning left unfixed.

5. **Layer 3B — Judgment Gate**: Run the manual checklist from `COPY-STANDARDS.md`
   - Every item verified explicitly — not by gut feel, not by "looks fine"
   - Key checks: no "We" sentence openers, no dangling modifiers, AIDA structure intact, headline passes Ogilvy test, all CTAs use first-person possessive ("Get My Free Quote" not "Get a Free Quote"), no incomplete comparisons

6. **Build HTML** using DESIGN.md tokens

7. **Start dev server** — `node serve.mjs` in background

8. **Screenshot** — `node screenshot.mjs http://localhost:3000/page.html`

9. **Run quality gates** — user reviews the page in browser; copy reads naturally in context of design

10. **Iterate** — minimum 2 screenshot rounds before calling a page done

**The old wrong process (banned):**
- ~~Read old HTML → write new HTML directly → screenshot → iterate~~
- ~~Draft copy without running the three-layer framework~~
- ~~Skip the SEO seed and start with marketing copy~~
- ~~Skip Vale and the manual checklist because "the copy feels good"~~
- ~~Copy handoff to .tmp/ for grammar approval — Vale + manual checklist replaces this~~
- Reading old HTML for content reference is fine. Jumping to code without the framework is not.

## Brand
- **Name:** CopperBuilds
- **Archetype:** Friend (primary) · Craftsman (secondary) — warm, on the client's side, built with care
- **Style:** Clean editorial · Light mode · Warm tones · Anti-corporate
- **Colors:**
  - `--bg: #FAFAF7` (warm off-white background)
  - `--surface: #FFFFFF` (cards)
  - `--txt: #1C1917` (warm near-black)
  - `--muted: #78716C` (warm stone gray)
  - `--copper: #B87333` (copper — primary brand color, headings and logo mark)
  - `--copper-hover: #9A6129`
  - `--teal: #4E9F7D` (teal — secondary accent, "Builds" wordmark, CTAs)
  - `--border: #E7E0D8` (warm border)
- **Fonts:**
  - Headings: `Calistoga` (warm editorial serif — NOT Unbounded, NOT Space Grotesk)
  - Body: `DM Sans` (approachable sans — NOT Inter, NOT Plus Jakarta Sans)
  - Mono: `JetBrains Mono` (stats, labels, prices)
- **Logo:** `brand_assets/logo.svg` — wordmark only: "Copper" (Calistoga, #B87333) + "Builds" (DM Sans Bold, #4E9F7D). NO mark, NO house, NO wifi arcs — user removed these permanently.
- **Tagline:** "Built for small businesses. Not enterprise." — protect this, use on every page
- **Pages:** index.html, services.html, about.html, contact.html, blog.html, help.html

## Design System
- Full token system, component rules, and anti-patterns are in `DESIGN.md` — always read it first.
- Brand voice, copy rules, and messaging hierarchy are in `BRAND-VOICE.md`.

## Brand Assets
- Always check the `brand_assets/` folder before designing. It may contain logos, color guides, style guides, or images.
- If assets exist there, use them. Do not use placeholders where real assets are available.

## Reference Images
- If a reference image is provided: match layout, spacing, typography, and color exactly. Swap in placeholder content (images via `https://placehold.co/`, generic copy). Do not improve or add to the design.
- If no reference image: design from scratch with high craft (see guardrails below).
- Screenshot your output, compare against reference, fix mismatches, re-screenshot. Do at least 2 comparison rounds. Stop only when no visible differences remain or user says so.

## Local Server
- **Always serve on localhost** — never screenshot a `file:///` URL.
- Start the dev server: `node serve.mjs` (serves the project root at `http://localhost:3000`)
- `serve.mjs` lives in this folder. Start it in the background before taking any screenshots.
- If the server is already running, do not start a second instance.

## Screenshot Workflow
- Puppeteer is installed at `C:/Users/User/LantechAI/`. Chrome cache is at `C:/Users/User/.cache/puppeteer/`.
- **Always screenshot from localhost:** `node screenshot.mjs http://localhost:3000`
- Screenshots are saved automatically to `./.tmp/screenshot-N.png` (auto-incremented, never overwritten).
- Optional label suffix: `node screenshot.mjs http://localhost:3000 label` → saves as `screenshot-N-label.png`
- `screenshot.mjs` lives in this folder. Use it as-is.
- After screenshotting, read the PNG from `.tmp/` with the Read tool — Claude can see and analyze the image directly.
- When comparing, be specific: "heading is 32px but reference shows ~24px", "card gap is 16px but should be 24px"
- Check: spacing/padding, font size/weight/line-height, colors (exact hex), alignment, border-radius, shadows, image sizing

## Output Defaults
- Single `index.html` file, all styles inline, unless user says otherwise
- Tailwind CSS via CDN: `<script src="https://cdn.tailwindcss.com"></script>`
- Placeholder images: `https://placehold.co/WIDTHxHEIGHT`
- Mobile-first responsive

## Anti-Generic Guardrails

### Colors
- Use ONLY tokens from `DESIGN.md` — never hardcode hex in components
- Background is `#FAFAF7` — NOT dark, NOT pure white
- Primary is `#B87333` copper — NEVER pure orange, NEVER cyan, NEVER purple
- Secondary is `#4E9F7D` teal — for CTAs, highlights, "Builds" wordmark
- Shadows are warm-tinted `rgba(28,25,23,...)` at max 0.12 alpha — never cold black shadows

### Typography
- Headings: Calistoga only — NOT Inter, NOT Space Grotesk, NOT Unbounded, NOT Poppins, NOT Roboto
- Body: DM Sans only — NOT Inter, NOT Plus Jakarta Sans
- Body line-height: 1.72. Body text max-width: 680px (65–75 chars/line)
- No `letter-spacing` on body text. Labels (JetBrains Mono) get `0.10em` tracking only.

### Animations
- Animate `transform` and `opacity` ONLY — never `width`, `height`, `padding`, `margin`
- Never `transition-all` — always specify properties
- Easing: `cubic-bezier(0.16, 1, 0.3, 1)` for entrances, `ease-in` for exits
- Respect `prefers-reduced-motion`
- Never bounce or elastic easing

### Interactive States
- Every clickable element: hover + focus-visible + active. No exceptions.
- Focus rings: 2px solid `var(--accent)` with 3px offset

### Spacing
- Use spacing scale from `DESIGN.md`: 8/16/24/32/48/80/120px — no arbitrary values

## Hard NEVER Rules (Impeccable Anti-Patterns — Zero Exceptions)
- **NEVER** dark mode as default — site is light mode always
- **NEVER** gradient text via `background-clip: text` on headings
- **NEVER** glassmorphism (blurred translucent cards, glass-border effects)
- **NEVER** dot grid texture backgrounds
- **NEVER** ambient glow radial gradient blobs (cyan or purple glows)
- **NEVER** SaaS hero metric layout (stat row: "50+ clients · 48h · 100%") — use contextual proof instead
- **NEVER** nested cards (card inside card inside card)
- **NEVER** colored left/right border stripes on cards as emphasis
- **NEVER** bounce or elastic easing (`cubic-bezier(0.34, 1.56, ...)` is banned)
- **NEVER** animate layout properties (width, height, padding, margin)
- **NEVER** identical-card feature grids — vary card sizes or weights

## Hard Rules
- Do not add sections, features, or content not in the reference
- Do not "improve" a reference design — match it
- Do not stop after one screenshot pass
- Do not use `transition-all`
- Do not use default Tailwind blue/indigo as primary color

## Quality Gates — DO-CONFIRM Before Marking Any Page Done

IMPORTANT: A page is not done until ALL of these pass:

**Visual (run after every screenshot round):**
- [ ] Background is `#FAFAF7` — NOT dark, NOT pure white
- [ ] Primary is `#B87333` copper, secondary is `#4E9F7D` teal — no raw orange, no cyan, no purple
- [ ] Headings use Calistoga — NOT Inter, NOT Unbounded, NOT Space Grotesk
- [ ] Body uses DM Sans — NOT Inter, NOT Plus Jakarta Sans
- [ ] Zero gradient text via `background-clip`
- [ ] Zero dot grid textures, zero glow blobs, zero glassmorphism
- [ ] Cards flat at rest — shadow only on hover
- [ ] At least 1 anti-grid layout moment on the page
- [ ] All clickable elements have hover + focus-visible + active states
- [ ] Mobile viewport (375px) tested — no overflow, no broken layouts
- [ ] At least 2 screenshot comparison rounds completed

**Performance (run before calling a page "launch-ready"):**
- [ ] LCP < 2.5s (Core Web Vital — use Lighthouse or PageSpeed Insights)
- [ ] CLS < 0.1 (no layout shift on load)
- [ ] No render-blocking scripts in `<head>` (defer or async all non-critical JS)
- [ ] Images have explicit `width` and `height` attributes

**Launch smoke test (5 items — run on final localhost before any deploy):**
- [ ] All nav links resolve (no 404s)
- [ ] Contact form submits without error (or shows correct placeholder state)
- [ ] Page title and meta description are set and unique per page
- [ ] No console errors on load
- [ ] Page looks correct on both desktop (1280px) and mobile (375px)

## Wiki Knowledge Base

**Path:** `C:\Users\User\LantechAI\claude-obsidian`

At session start, `workflows/session-start.md` loads `wiki/hot.md` automatically. For deeper context:
1. Read `wiki/hot.md` first — ~500 words of recent context across all sessions
2. If more context needed, read `wiki/index.md`
3. For domain-specific knowledge, read `wiki/<domain>/_index.md`

After every monthly SEO retainer session, run `/save` to file key findings. Knowledge compounds across all clients.

---

## Relevant Skills
- `frontend-design` — invoke before any frontend work (every session, no exceptions)
- `anti-ai-design` — **invoke before any brand or design work** — universal anti-pattern reference; works alongside DESIGN.md
- `brand-web` — invoke when creating a new brand or rebranding an existing site (tokens, DESIGN.md, SVG logo, grep audit, file-by-file replacement)
- `ai-graphic-design` — use for logo, brand identity, visual asset generation (5-phase briefing workflow)
- `ui-ux-pro-max` — use for design system queries, color/typography recommendations, UX review
- `market-brand` — brand voice analysis and guidelines (see `BRAND-VOICE.md` for Lantech's output)
- `/lantech-seo [client-slug]` — **pre-build SEO** for client builds: reads client.env, validates real keyword volumes via DataForSEO, generates titles/meta/schema/action plan. Run BEFORE `/lantech-build`.
- `/vale-check [file]` — **copy quality gate**: runs Vale grammar/style check against Lantech rules + client brand voice. Mandatory before any page or blog post is marked done. Install once with `winget install --id errata-ai.Vale`, then `vale sync` from this folder.
- `/seo-local <url>` — post-build local SEO audit (GBP, reviews, NAP, citations)
- `/seo-page <url>` — post-build on-page SEO audit
- `/seo-schema <url>` — generate/validate structured data on a live page
- `/seo-technical <url>` — post-build technical SEO audit
- `/seo-geo <url>` — AI search visibility audit (GEO, llms.txt, AI crawler access)
