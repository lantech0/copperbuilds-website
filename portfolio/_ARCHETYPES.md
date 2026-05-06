# Trade Website Style Catalog — Layout Archetypes

Reference for all mock portfolio builds. Before starting any new mock, pick an unused archetype
from this list. All 6 are currently used — see the Portfolio column for which site demonstrates
each one.

---

## 1. Urgency / Emergency

**Best-fit trades:** HVAC, plumbing, electrical, pest control, water damage — any service with
24/7 emergency demand where the customer is in crisis when they search.

**Core idea:** The phone number or response-time guarantee is the hero. Everything signals speed
and availability. Dark, high-contrast palette. No soft language.

**Key layout characteristics:**
- Emergency / alert bar pinned at top (phone number + "24/7" or "Same Day")
- Dark nav on dark hero — feels like the service is already on alert
- Hero shows phone number prominently OR a split layout with form card on the right
- Trust-proof bar immediately below hero: response time, license number, service area
- Service cards: dark background, accent-colored icon, no photos
- Footer repeats the emergency phone number

**Hero styles used:**
- *Split layout + form card* (Elite Air Services) — two-column hero, form on right, phone on left
- *Centered giant phone number* (Priority Plumbing) — phone number as the visual centerpiece,
  no form, Barlow Condensed at display scale

**Portfolio demos:**
- `elite-air-services/` — HVAC, Navy #1A7BC0 + Orange #F07820
- `priority-plumbing/` — Plumbing, Navy #1A3A6E + Orange #E85D04 (variant: centered phone)

---

## 2. Premium Credibility / Whitespace

**Best-fit trades:** Roofing, remodeling, custom homes, painting, flooring — trades where the
client is spending significant money and needs to trust the contractor before calling.

**Core idea:** The site earns trust through restraint. Generous whitespace, serif typography,
credentials treated as visual design elements, no shouting.

**Key layout characteristics:**
- Split hero: large photo left, text right — or cream/warm white background with editorial type
- Serif heading font (Cormorant Garamond, Playfair Display, or similar)
- License + insurance credentials displayed prominently as design elements (not hidden in footer)
- Photo-top service cards (photo above copy, not icon-based)
- Pull quote band or testimonial section with large typographic quotes
- No emergency bar — a trust bar instead (years in business, licensed, insured)
- CTA language is consultation-focused, not "call now"

**Portfolio demo:**
- `keiths-roofing/` — Roofing, Cream + Brick #C85422, Cormorant Garamond

---

## 3. Visual Portfolio / Transformation

**Best-fit trades:** Landscaping, fencing, hardscaping, painting, cleaning, pressure washing —
trades that sell with visual proof of their work.

**Core idea:** The work is the argument. The site prioritizes photos over copy. Before/after
transformations build emotional proof. The hero is full-bleed, photo-first.

**Key layout characteristics:**
- Full-bleed photo hero with transparent nav (nav overlays the photo)
- Gallery section appears early — often the first content section after the hero
- Before/after transformation feature (slider or side-by-side)
- Service cards are photo-top or photo-only with overlay label
- Minimal text in the hero — just a punchy line and CTA
- Color palette matches the natural environment of the trade (greens, earths, blues)

**Portfolio demo:**
- `seraphin-landscaping/` — Landscaping, Forest green #2A5218 + Earth gold

---

## 4. Bold Industrial

**Best-fit trades:** Concrete, steel, excavation, demolition, heavy equipment, commercial
construction — trades that sell strength and durability, not warmth.

**Core idea:** The site itself feels heavy and purposeful. Display typography at extreme scale.
Dark industrial palette. Numbered, systematic layouts signal precision and process.

**Key layout characteristics:**
- Yellow utility strip at top (high-visibility industrial yellow)
- Dark hero — near-black background, construction photo at low opacity
- Display font at extreme scale: Bebas Neue, Impact, or condensed grotesque at 90–120px
- Service grid uses numbered cards (01–06) to signal process and completeness
- Asymmetric project photo gallery — large lead image + smaller grid (2fr + 1fr + 1fr)
- Yellow CTA band at bottom
- Stats bar uses industrial-feel numbers (tons poured, years operating, projects completed)
- Body font: condensed grotesque (Roboto Condensed, Barlow Condensed)

**Portfolio demo:**
- `steelman-concrete/` — Concrete, Coal #0F172A + Yellow #F59E0B, Bebas Neue

---

## 5. Local Trust / Community

**Best-fit trades:** Electricians, plumbers (non-emergency positioning), HVAC (maintenance focus),
pest control, cleaning — trades where the differentiator is being a reliable neighborhood fixture,
not the fastest responder.

**Core idea:** The site feels like it's from someone in your community, not a national franchise.
Light background, personal language, photos of real service situations, trust through connection
rather than authority.

**Key layout characteristics:**
- Light-background hero (white or warm white — NOT dark)
- Trust bar below hero: years in area, neighborhoods served, license badge
- Service grid uses icons, not photos — approachable, not glossy
- Neighborhood / service area section with a community-anchoring message or quote
- Testimonials feel personal — attribution includes suburb or neighborhood name
- Soft CTA language ("Schedule a visit", "Get a free estimate") — not urgency-based
- Footer includes local address and a community trust line

**Portfolio demo:**
- `rivera-electric/` — Electrical, Teal #134E4A + Amber #B45309, Lora serif

---

## 6. Cinematic / Parallax

**Best-fit trades:** Luxury remodelers, custom home builders, high-end interior designers,
architects — trades that sell to clients who think of their home as a creative project.

**Core idea:** The site feels like a magazine spread or a design film. Full-viewport hero,
editorial photography, CSS parallax photo breaks between content sections. Slow, confident pace.

**Key layout characteristics:**
- 100vh hero (full viewport height) — not a short banner
- Animated scroll indicator in hero (subtle pulse or arrow)
- NO utility strip — the opening is clean and cinematic
- Serif heading font (Playfair Display, Cormorant Garamond) — italic weight used deliberately
- Gold or warm metallic accent
- CSS parallax breaks: `background-attachment: fixed` photo sections between content areas
  (mobile fallback: `background-attachment: scroll`)
- Service cards are editorial photo cards with text overlay or caption
- Gallery uses asymmetric CSS grid
- Review section: large typographic quote marks, italic review text
- Body copy is editorial-length — not bulleted service lists
- CTA language is aspirational: "Start your project", "Request a consultation"
- Mobile: `@media (max-width: 767px) { .parallax-break { background-attachment: scroll; } }`

**Portfolio demo:**
- `hargrove-design-build/` — Renovation, Ink #0D0D0D + Warm Cream #F9F6F1 + Gold #B8965A

---

## Archetype Selection Rules

1. **Each new mock must use a demonstrably different archetype** from all existing portfolio
   sites. Check this table before building starts — picking the archetype is Step 0.5.

2. **All 6 archetypes are currently used.** To add more mocks, either:
   - Repeat an archetype with a demonstrably different structural execution (documented in the
     table above — e.g., Elite Air's split-form vs. Priority Plumbing's centered-phone for
     Urgency/Emergency)
   - Expand this catalog with a new archetype backed by research

3. **State the archetype by name** before writing any code. Document the structural difference
   if repeating.

4. **Palette and font must differ from existing sites** even when repeating an archetype.

---

## Archetype Assignment Table

| Site | Archetype | Palette | Key structural differentiator |
|---|---|---|---|
| `elite-air-services/` | Urgency/Emergency | Navy #1A7BC0 + Orange #F07820 | Split layout + form card on right |
| `keiths-roofing/` | Premium Credibility | Cream + Brick #C85422 | Cormorant Garamond, credential display |
| `seraphin-landscaping/` | Visual Portfolio | Forest green #2A5218 + Earth gold | Full-bleed hero, gallery-first |
| `priority-plumbing/` | Urgency/Emergency (variant) | Navy #1A3A6E + Orange #E85D04 | Centered hero — giant phone number |
| `rivera-electric/` | Local Trust / Community | Teal #134E4A + Amber #B45309 | Light hero, icon grid, neighborhood section |
| `steelman-concrete/` | Bold Industrial | Coal #0F172A + Yellow #F59E0B | Bebas Neue 110px, numbered grid, photo gallery |
| `hargrove-design-build/` | Cinematic / Parallax | Ink #0D0D0D + Cream #F9F6F1 + Gold #B8965A | 100vh hero, parallax breaks, no utility strip |
