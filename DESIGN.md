---
name: Lantech
description: Professional websites for small businesses. Not enterprise.
colors:
  accent: "#E8600A"
  accent-hover: "#C2500A"
  accent-dim: "#E8600A14"
  accent-border: "#E8600A38"
  accent-shadow: "#E8600A38"
  warm-parchment: "#FAFAF7"
  surface: "#FFFFFF"
  elevated: "#F5F0EA"
  ink: "#1C1917"
  warm-stone: "#78716C"
  subtle: "#A8A29E"
  confident-blue: "#1D4ED8"
  blue-dim: "#1D4ED814"
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

# Design System: Lantech

## 1. Overview

**Creative North Star: "The Trusted Craftsman"**

Lantech serves small businesses that have been burned by agencies — overcharged, underdelivered, treated like an account number. The design system's job is to signal, at a glance, that this is different: a skilled local expert with their act together. Warm, confident, clean — not the cold chrome of enterprise SaaS or the hollow polish of an AI-generated template.

Light mode is mandatory. The background is Morning Parchment (#FAFAF7) — not pure white, not dark. The accent is Advocate Orange (#E8600A): the Rebel signal. It says "we mean it" without aggression. Calistoga headings carry the editorial warmth of a craftsman's sign, not a startup's growth deck. DM Sans body copy reads like someone who knows their field and speaks plainly.

This system explicitly rejects: dark mode defaults, cyan/purple SaaS palettes (`#00E5FF`, `#7C5CFC`), gradient text on headings, glassmorphism, dot-grid textures, ambient glow radial blobs, identical-card feature grids, and the SaaS metric hero row. All are signals of "AI-generated template" — none belong here.

**Key Characteristics:**
- Light mode only. Warm parchment base. Cold white and dark backgrounds are prohibited.
- One accent color. Advocate Orange (#E8600A) on ≤15% of any given screen. Rarity is the signal.
- Editorial serif headings (Calistoga) paired with a humanist sans body (DM Sans). No interchangeable defaults.
- Flat surfaces at rest. Shadows are earned by state change (hover, elevation, modal).
- At least one anti-grid layout moment per page — asymmetry, overlap, or diagonal flow — to break template symmetry.

## 2. Colors: The Warmth-and-Ember Palette

A restrained palette: warm tinted neutrals form the foundation; one ember accent carries the emotional signal. No secondary accent, no tertiary color. The orange's scarcity is intentional — its presence means something.

### Primary
- **Advocate Orange** (#E8600A): The brand's Rebel signal. Primary CTAs, active nav states, tag foregrounds, focus rings. Never used as a large-surface background. Its scarcity across the page is the point.
- **Advocate Orange — Hover** (#C2500A): Darkened 15% on hover. Applied via CSS transition on all orange-accented elements.

### Neutral
- **Morning Parchment** (#FAFAF7): The page background. Warm off-white — not pure #FFFFFF and not cold gray. The subtle warmth accumulates across the page as a signal of intention.
- **Clean Canvas** (#FFFFFF): Card and surface backgrounds. Appears slightly elevated against Morning Parchment.
- **Warm Cream** (#F5F0EA): Hover states for inputs and subtly elevated surfaces. One step warmer than Canvas.
- **Warm Ink** (#1C1917): Primary text. A warm near-black — not cold #000000. All shadows use this hue family at low alpha.
- **River Stone** (#78716C): Secondary text, nav links at rest, supporting copy, meta information.
- **Soft Stone** (#A8A29E): Tertiary text, placeholders, disabled field labels.
- **Anchor Blue** (#1D4ED8): Hyperlinks and secondary actions. Confident, not generic corporate blue.
- **Parchment Edge** (#E7E0D8): All borders and dividers. Warm — reads as intentional, not a default gray.

### Named Rules
**The One Signal Rule.** Advocate Orange is used on ≤15% of any given screen. CTAs and active states only. If orange appears everywhere, it means nothing.

**The No-Cold-Shadow Rule.** All shadow values use `rgba(28, 25, 23, ...)` — warm ink at low alpha. `rgba(0, 0, 0, ...)` is prohibited in all shadow declarations. The cumulative warmth of the tinted shadow is a system-wide signal.

## 3. Typography: The Editorial Pairing

**Display Font:** Calistoga (Google Fonts), with Georgia and serif as stack fallback.
**Body Font:** DM Sans (Google Fonts, weights 300–700), with sans-serif as fallback.
**Label/Mono Font:** JetBrains Mono (Google Fonts, weights 400–500), with monospace as fallback.

**Character:** Calistoga carries the warmth of vintage editorial print — slightly retro, ink-quality, unmistakably crafted. DM Sans is clean and geometric without the coldness of Inter or the tech-startup flavor of Space Grotesk. Together they read as "professional and human" rather than "startup template."

### Hierarchy
- **Display** (Calistoga 400, clamp(2.2rem, 5vw, 3.75rem), line-height 1.08): Hero H1 only. Fluid between mobile and desktop via `clamp()`.
- **Headline** (Calistoga 400, clamp(1.75rem, 3vw, 2.5rem), line-height 1.12): Section H2 titles. Same font, smaller fluid range.
- **Title** (DM Sans 700, 1.25rem, line-height 1.3): H3 card headers, sidebar labels, strong section labels.
- **Body** (DM Sans 400, 1rem / 16px, line-height 1.72): All paragraph copy. Max line length 65–75ch enforced with `max-width: 680px` on prose containers.
- **Body Large** (DM Sans 400, 1.0625rem, line-height 1.7): Hero sub-headlines, lead paragraphs.
- **Label** (JetBrains Mono 500, 0.68rem, letter-spacing 0.10em, uppercase): Tags, stat labels, price callouts, section eyebrow labels. Letter-tracking on Mono labels only.

### Named Rules
**The Calistoga-Only Rule.** Calistoga is the sole heading font. Inter, Space Grotesk, Unbounded, Poppins, Plus Jakarta Sans, and Roboto are prohibited as heading fonts.

**The No-Body-Tracking Rule.** `letter-spacing` on DM Sans body copy is forbidden. Tracking (`0.10em`) is permitted only on JetBrains Mono label elements.

**The Italic-as-Voice Rule.** Calistoga italic is the only emphasis voice permitted in headings. Body copy uses DM Sans 600 weight for inline emphasis — never italic.

## 4. Elevation: Flat by Default

This system uses warm-tinted drop shadows for elevation — not glassmorphism, not tonal surface layering, not decorative glow blobs. Surfaces are flat at rest. A shadow appears only when an element is interactively elevated: hover, drag-active, modal open, popover visible.

Shadow tints are always warm ink (`rgba(28, 25, 23, ...)`). Cold black (`rgba(0, 0, 0, ...)`) is prohibited in all shadow values regardless of alpha.

### Shadow Vocabulary
- **Definition** (`0 1px 3px rgba(28,25,23,0.08), 0 1px 2px rgba(28,25,23,0.06)`): Card resting state when a subtle edge definition is needed. Functions as a border alternative, not as decorative depth.
- **Hover Lift** (`0 4px 16px rgba(28,25,23,0.10), 0 2px 6px rgba(28,25,23,0.06)`): Cards and interactive surfaces on hover. Lifts the element off the surface; signals interactivity.
- **Elevated** (`0 12px 40px rgba(28,25,23,0.12), 0 4px 12px rgba(28,25,23,0.06)`): Modals, dropdowns, popovers. Maximum depth in the system.
- **Accent Glow** (`0 8px 24px rgba(232, 96, 10, 0.22)`): Primary CTA button on hover only. Warm orange haze — used once per screen maximum. Never on cards or backgrounds.

### Named Rules
**The Flat-by-Default Rule.** No surface renders decorative shadow at rest. Definition shadow (0.08 alpha) is the only exception — it functions as a border alternative. Real elevation is earned by interaction state.

**The Earned Glow Rule.** Accent Glow is permitted on one element per screen: the primary CTA button hover state. It is not a decorative pattern for cards, sections, or secondary buttons.

## 5. Components

Components are direct and tactile. Buttons have presence without aggression. Cards are clean white surfaces that gently lift on interaction. Tags are the only element that uses the accent at surface opacity. Nothing nests, nothing glows at rest, nothing imitates a template.

### Buttons
- **Shape:** Gently rounded (6px radius — `rounded.md`). Not square (too cold), not pill (too informal).
- **Primary:** Advocate Orange (#E8600A) background, #FFFFFF text, DM Sans 700, padding 12px × 24px. Hover: `#C2500A` background, `translateY(-2px)`, Accent Glow box-shadow. Active: `translateY(0)`, shadow removed.
- **Hover / Focus:** Transitions on `background 0.15s ease`, `transform 0.2s cubic-bezier(0.16, 1, 0.3, 1)`, `box-shadow 0.15s ease`. Focus-visible: 2px solid Advocate Orange, 3px offset. Never `transition-all`.
- **Ghost / Secondary:** Transparent background, Warm Ink (#1C1917) text, 1.5px Parchment Edge border. Hover: border shifts to `#E8600A38`, background tints to `#E8600A14`, same lift animation.
- **Text Link:** No border, no background. River Stone at rest, Warm Ink on hover. Inline arrow (`→`) where directional context helps.

### Tags / Chips
- **Style:** JetBrains Mono 500, 0.68rem, 0.10em letter-spacing, uppercase. Advocate Orange (#E8600A) text on `#E8600A14` background with `#E8600A38` border. 100px pill radius.
- **State:** Static label by default. If an interactive filter chip is needed: selected state = full Advocate Orange background + #FFFFFF text.

### Cards
- **Corner Style:** Gently rounded (12px — `rounded.lg`).
- **Background:** Clean Canvas (#FFFFFF) on Morning Parchment page background.
- **Shadow Strategy:** Flat at rest (no visible shadow). On hover: Hover Lift shadow + `translateY(-3px)` + border shifts from Parchment Edge to `#E8600A38`.
- **Border:** 1.5px Parchment Edge (#E7E0D8) at rest.
- **Internal Padding:** 28px minimum. Never below 24px.
- **Prohibition:** No nested cards. No colored left-border or right-border stripe as an emphasis pattern. No card-inside-card.

### Inputs / Fields
- **Style:** 1.5px Parchment Edge border, Clean Canvas (#FFFFFF) background, 6px radius.
- **Focus:** Border shifts to Advocate Orange (`#E8600A`), background tints to `#E8600A14`. No glow. Transitions on `border-color 0.15s`, `background 0.15s`.
- **Error:** Border shifts to warm red. Error message below the field, River Stone color, 0.875rem, same line-height as body copy.
- **Disabled:** River Stone text, Warm Cream (#F5F0EA) background, 0.5 opacity border.

### Navigation
- **Style:** Morning Parchment background at 90% opacity (`rgba(250, 250, 247, 0.90)`), 16px `backdrop-filter: blur`. 1px Parchment Edge bottom border. `position: sticky; top: 0`.
- **Typography:** DM Sans 500, 0.875rem.
- **States:** Default = River Stone (#78716C). Hover = Warm Ink (#1C1917). Active = Advocate Orange (#E8600A).
- **Mobile:** Hamburger toggle. Menu expands below nav bar on same Morning Parchment background — no dark overlay, no fullscreen takeover.

### Section Labels (Mono eyebrows)
- JetBrains Mono 500, 0.68rem, 0.10em letter-spacing, uppercase. Used above H2 headings to name the section context. Advocate Orange color when emphasis is needed; River Stone for neutral section labels.

## 6. Do's and Don'ts

### Do:
- **Do** use `#FAFAF7` (Morning Parchment) as the page background — the warm off-white is the system's base signal.
- **Do** use Calistoga for all H1 and H2 headings — the editorial serif is the primary brand differentiator.
- **Do** use Advocate Orange (`#E8600A`) sparingly: primary CTAs, active nav states, tags, focus rings only.
- **Do** use warm shadows exclusively: `rgba(28, 25, 23, ...)` at maximum 0.12 alpha.
- **Do** keep surfaces flat at rest — shadows and lifts are earned by hover state only.
- **Do** include at least one anti-grid layout moment per page: asymmetric columns, overlap, diagonal flow, or a grid-breaking element.
- **Do** specify hover + focus-visible + active states on every interactive element.
- **Do** animate `transform` and `opacity` only — no layout property animations.
- **Do** use `transition: [property] [duration] [easing]` — named properties always, never `transition-all`.
- **Do** cap body text containers at 680px max-width (65–75 characters per line).
- **Do** use `prefers-reduced-motion` to disable all non-essential transitions.
- **Do** use the entrance easing `cubic-bezier(0.16, 1, 0.3, 1)` for hover lifts and element entrances.

### Don't:
- **Don't** use dark mode as default. The site is light mode. This is non-negotiable.
- **Don't** use cyan (`#00E5FF`) or purple (`#7C5CFC`) — these are the eradicated old brand colors.
- **Don't** use gradient text via `background-clip: text` on headings. Prohibited.
- **Don't** add dot-grid texture backgrounds. Prohibited.
- **Don't** add ambient glow radial gradients (the cyan/purple blob glows). Prohibited.
- **Don't** use glassmorphism — blurred translucent cards or glass-border effects. Prohibited.
- **Don't** use Inter, Roboto, Arial, Space Grotesk, Unbounded, Plus Jakarta Sans, or Poppins as a heading font.
- **Don't** use `transition-all` — always specify individual transition properties.
- **Don't** use bounce or elastic easing — `cubic-bezier(0.34, 1.56, ...)` is banned.
- **Don't** animate layout properties (width, height, padding, margin).
- **Don't** nest cards — no card inside a card.
- **Don't** use identical-card feature grids — vary card sizes, weights, or layout rhythm.
- **Don't** use a colored left-border or right-border stripe as a card emphasis pattern.
- **Don't** build a SaaS metric hero row ("50+ businesses · 48h · 100%") — use contextual social proof instead.
- **Don't** use cold black shadows (`rgba(0,0,0,...)`). Warm ink tints only.
- **Don't** use pure white (`#FFFFFF`) as the page background — Morning Parchment only.
