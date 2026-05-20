---
name: CopperBuilds
description: Professional websites for the trades. Built to generate leads.
colors:
  accent: "#B87333"
  accent-hover: "#96602A"
  accent-dim: "#B8733314"
  accent-border: "#B8733338"
  accent-shadow: "#B8733338"
  patina: "#4E9F7D"
  patina-hover: "#3D8B6C"
  patina-dim: "#4E9F7D14"
  patina-border: "#4E9F7D38"
  warm-parchment: "#FAFAF7"
  surface: "#FFFFFF"
  elevated: "#F5F0EA"
  ink: "#1C1917"
  warm-stone: "#78716C"
  subtle: "#A8A29E"
  parchment-border: "#E7E0D8"
  rule: "#1C191714"
typography:
  display:
    fontFamily: "Calistoga, Georgia, serif"
    fontSize: "clamp(2.2rem, 5vw, 3.75rem)"
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: "normal"
  headline:
    fontFamily: "Calistoga, Georgia, serif"
    fontSize: "clamp(1.75rem, 3vw, 2.5rem)"
    fontWeight: 400
    lineHeight: 1.12
    letterSpacing: "normal"
  title:
    fontFamily: "DM Sans, sans-serif"
    fontSize: "1.25rem"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "normal"
  body:
    fontFamily: "DM Sans, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.72
    letterSpacing: "normal"
  body-large:
    fontFamily: "DM Sans, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: "normal"
  label:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: "0.68rem"
    fontWeight: 500
    lineHeight: 1
    letterSpacing: "0.10em"
rounded:
  sm: "4px"
  md: "6px"
  lg: "12px"
  xl: "20px"
  pill: "100px"
spacing:
  1: "8px"
  2: "16px"
  3: "24px"
  4: "32px"
  5: "48px"
  6: "80px"
  7: "120px"
components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "#FFFFFF"
    rounded: "{rounded.md}"
    padding: "12px 24px"
    typography: "{typography.label}"
  button-primary-hover:
    backgroundColor: "{colors.accent-hover}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "12px 24px"
  button-ghost-hover:
    backgroundColor: "{colors.accent-dim}"
    textColor: "{colors.ink}"
  tag:
    backgroundColor: "{colors.accent-dim}"
    textColor: "{colors.accent}"
    rounded: "{rounded.pill}"
    padding: "5px 13px"
  tag-patina:
    backgroundColor: "{colors.patina-dim}"
    textColor: "{colors.patina}"
    rounded: "{rounded.pill}"
    padding: "5px 13px"
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.lg}"
    padding: "28px"
  card-hover:
    backgroundColor: "{colors.surface}"
  nav:
    backgroundColor: "{colors.warm-parchment}"
    textColor: "{colors.warm-stone}"
---

# Design System: CopperBuilds

## 1. Overview

**Creative North Star: "The Tradesman's Partner"**

CopperBuilds serves home service contractors who have been burned by agencies — overcharged, underdelivered, treated like an account number. The design system signals, at a glance, that this is different: a partner who knows the trades, speaks plainly, and delivers results. Warm, confident, clean — not the cold chrome of enterprise SaaS or the hollow polish of an AI-generated template.

The palette is drawn from the material every trade shares: copper. Fresh Copper (#B87333) is the primary accent — warm, tangible, immediately recognizable to any contractor. Aged Patina (#4E9F7D) is the secondary accent — the teal-green that copper develops over years of honest work. It signals permanence, trust earned over time. Together they tell a story no generic agency palette can: we know your world.

Light mode is mandatory. The background is Morning Parchment (#FAFAF7) — a workshop surface, not a corporate lobby. Calistoga headings carry editorial warmth. DM Sans body copy reads like someone who knows their field and speaks plainly.

This system explicitly rejects: dark mode defaults, cyan/purple SaaS palettes, gradient text on headings, glassmorphism, dot-grid textures, ambient glow radial blobs, identical-card feature grids, and the SaaS metric hero row. All are signals of "AI-generated template" — none belong here.

**Key Characteristics:**
- Light mode only. Warm parchment base. Cold white and dark backgrounds are prohibited.
- Two accent colors: Fresh Copper (#B87333) primary, Aged Patina (#4E9F7D) secondary. Each on ≤15% of any screen.
- Editorial serif headings (Calistoga) paired with a humanist sans body (DM Sans).
- Flat surfaces at rest. Shadows are earned by state change (hover, elevation, modal).
- At least one anti-grid layout moment per page — asymmetry, overlap, or diagonal flow.

## 2. Colors: The Copper Palette

Two accents drawn from a single material at two moments in time: fresh copper and aged patina. Warm neutrals form the foundation. No neon, no gradient fills, no cold blues.

### Primary Accent
- **Fresh Copper** (#B87333): The brand's primary signal. Primary CTAs, active nav states, tag foregrounds, focus rings. Never used as a large-surface background. Scarcity is the signal.
- **Fresh Copper — Hover** (#96602A): Darkened on hover. Applied via CSS transition on all copper-accented elements.

### Secondary Accent
- **Aged Patina** (#4E9F7D): Secondary actions, secondary tags, highlight callouts, links. The green-teal of oxidized copper — signals trust and permanence. Used more sparingly than Fresh Copper.
- **Aged Patina — Hover** (#3D8B6C): Darkened on hover for patina-accented elements.

### Neutral
- **Morning Parchment** (#FAFAF7): The page background. Warm off-white — not pure #FFFFFF and not cold gray.
- **Clean Canvas** (#FFFFFF): Card and surface backgrounds. Slightly elevated against Morning Parchment.
- **Warm Cream** (#F5F0EA): Hover states for inputs and subtly elevated surfaces.
- **Warm Ink** (#1C1917): Primary text. Warm near-black — not cold #000000.
- **River Stone** (#78716C): Secondary text, nav links at rest, supporting copy.
- **Soft Stone** (#A8A29E): Tertiary text, placeholders, disabled field labels.
- **Parchment Edge** (#E7E0D8): All borders and dividers. Warm.

### Named Rules
**The Two-Signal Rule.** Fresh Copper is the primary action signal. Aged Patina is the secondary trust signal. Neither exceeds 15% of any screen. If both appear at equal weight, hierarchy collapses — copper leads, patina supports.

**The No-Cold-Shadow Rule.** All shadow values use `rgba(28, 25, 23, ...)` — warm ink at low alpha. `rgba(0, 0, 0, ...)` is prohibited in all shadow declarations.

## 3. Typography: The Editorial Pairing

**Display Font:** Calistoga (Google Fonts), with Georgia and serif as stack fallback.
**Body Font:** DM Sans (Google Fonts, weights 300–700), with sans-serif as fallback.
**Label/Mono Font:** JetBrains Mono (Google Fonts, weights 400–500), with monospace as fallback.

**Character:** Calistoga carries the warmth of vintage editorial print — slightly retro, ink-quality, unmistakably crafted. DM Sans is clean and geometric without the coldness of Inter or the tech-startup flavor of Space Grotesk. Together they read as "professional and human" rather than "startup template."

### Hierarchy
- **Display** (Calistoga 400, clamp(2.2rem, 5vw, 3.75rem), line-height 1.08): Hero H1 only.
- **Headline** (Calistoga 400, clamp(1.75rem, 3vw, 2.5rem), line-height 1.12): Section H2 titles.
- **Title** (DM Sans 700, 1.25rem, line-height 1.3): H3 card headers, sidebar labels.
- **Body** (DM Sans 400, 1rem / 16px, line-height 1.72): All paragraph copy. Max 680px width.
- **Body Large** (DM Sans 400, 1.0625rem, line-height 1.7): Hero sub-headlines, lead paragraphs.
- **Label** (JetBrains Mono 500, 0.68rem, letter-spacing 0.10em, uppercase): Tags, stat labels, price callouts, section eyebrows.

### Named Rules
**The Calistoga-Only Rule.** Calistoga is the sole heading font. Inter, Space Grotesk, Unbounded, Poppins, Plus Jakarta Sans, and Roboto are prohibited as heading fonts.

**The No-Body-Tracking Rule.** `letter-spacing` on DM Sans body copy is forbidden. Tracking is permitted only on JetBrains Mono label elements.

**The Italic-as-Voice Rule.** Calistoga italic is the only emphasis voice permitted in headings. Body copy uses DM Sans 600 weight for inline emphasis — never italic.

## 4. Elevation: Flat by Default

Surfaces are flat at rest. A shadow appears only when an element is interactively elevated: hover, drag-active, modal open, popover visible. Shadow tints are always warm ink (`rgba(28, 25, 23, ...)`). Cold black is prohibited.

### Shadow Vocabulary
- **Definition** (`0 1px 3px rgba(28,25,23,0.08), 0 1px 2px rgba(28,25,23,0.06)`): Card resting state subtle edge.
- **Hover Lift** (`0 4px 16px rgba(28,25,23,0.10), 0 2px 6px rgba(28,25,23,0.06)`): Cards on hover.
- **Elevated** (`0 12px 40px rgba(28,25,23,0.12), 0 4px 12px rgba(28,25,23,0.06)`): Modals, dropdowns.
- **Accent Glow** (`0 8px 24px rgba(184, 115, 51, 0.22)`): Primary CTA button on hover only. Warm copper haze — used once per screen maximum.

### Named Rules
**The Flat-by-Default Rule.** No surface renders decorative shadow at rest.

**The Earned Glow Rule.** Accent Glow permitted on one element per screen: the primary CTA button hover state only.

## 5. Components

### Buttons
- **Primary:** Fresh Copper (#B87333) background, #FFFFFF text, DM Sans 700, padding 12px × 24px. Hover: `#96602A`, `translateY(-2px)`, Accent Glow box-shadow.
- **Ghost / Secondary:** Transparent background, Warm Ink text, 1.5px Parchment Edge border. Hover: border shifts to `#B8733338`, background to `#B8733314`.
- **Patina CTA:** Aged Patina (#4E9F7D) background for secondary emphasis. Hover: `#3D8B6C`.
- **Focus-visible:** 2px solid Fresh Copper, 3px offset. All interactive elements, no exceptions.

### Tags / Chips
- **Copper tag:** JetBrains Mono 500, 0.68rem, uppercase. Fresh Copper text on `#B8733314` background, `#B8733338` border. 100px pill radius.
- **Patina tag:** Aged Patina text on `#4E9F7D14` background, `#4E9F7D38` border. Same type rules.

### Cards
- **Corner Style:** 12px radius.
- **Background:** Clean Canvas (#FFFFFF) on Morning Parchment.
- **Shadow:** Flat at rest. Hover: Hover Lift + `translateY(-3px)` + border shifts to `#B8733338`.
- **Border:** 1.5px Parchment Edge at rest. Internal padding 28px minimum.
- **Prohibition:** No nested cards. No colored border stripes as emphasis.

### Inputs / Fields
- **Style:** 1.5px Parchment Edge border, Clean Canvas background, 6px radius.
- **Focus:** Border shifts to Fresh Copper (#B87333), background to `#B8733314`.

### Navigation
- **Style:** Morning Parchment at 90% opacity, 16px backdrop-filter blur. Sticky top.
- **States:** Default = River Stone. Hover = Warm Ink. Active = Fresh Copper (#B87333).

### Section Labels
- JetBrains Mono 500, 0.68rem, 0.10em tracking, uppercase. Fresh Copper for emphasis; River Stone for neutral labels. Patina permitted for secondary section eyebrows.

## 6. Do's and Don'ts

### Do:
- **Do** use `#FAFAF7` (Morning Parchment) as the page background.
- **Do** use Calistoga for all H1 and H2 headings.
- **Do** use Fresh Copper (`#B87333`) for primary CTAs, active nav states, tags, focus rings.
- **Do** use Aged Patina (`#4E9F7D`) as the secondary accent — links, secondary tags, trust signals.
- **Do** use warm shadows exclusively: `rgba(28, 25, 23, ...)` at maximum 0.12 alpha.
- **Do** keep surfaces flat at rest — shadows earned by hover state only.
- **Do** include at least one anti-grid layout moment per page.
- **Do** specify hover + focus-visible + active states on every interactive element.
- **Do** animate `transform` and `opacity` only.
- **Do** use `transition: [property] [duration] [easing]` — named properties always.
- **Do** cap body text containers at 680px max-width.
- **Do** use `prefers-reduced-motion` to disable non-essential transitions.

### Don't:
- **Don't** use dark mode as default. Light mode only.
- **Don't** use cyan (`#00E5FF`), purple (`#7C5CFC`), or the old orange (`#E8600A`) — eradicated.
- **Don't** use gradient text via `background-clip: text` on headings.
- **Don't** add dot-grid texture backgrounds.
- **Don't** add ambient glow radial gradients.
- **Don't** use glassmorphism.
- **Don't** use Inter, Roboto, Arial, Space Grotesk, Unbounded, Plus Jakarta Sans, or Poppins as a heading font.
- **Don't** use `transition-all`.
- **Don't** use bounce or elastic easing.
- **Don't** animate layout properties (width, height, padding, margin).
- **Don't** nest cards.
- **Don't** use identical-card feature grids.
- **Don't** use a colored border stripe as a card emphasis pattern.
- **Don't** build a SaaS metric hero row.
- **Don't** use cold black shadows (`rgba(0,0,0,...)`).
- **Don't** use pure white (`#FFFFFF`) as the page background.
