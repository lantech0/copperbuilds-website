# Lantech Website — Master Page Brief

Paste this entire document into Claude when asking it to build or redesign any page.
Fill in the [BRACKETED] fields before sending.

---

## Who This Is For

**Lantech** is a web design agency founded by Luis Echarri, serving small businesses
across the United States. We build fast, affordable websites and local SEO for home
service contractors and local businesses. Monthly retainer plans: Local Presence $997/mo · Lead Machine $1,997/mo · Market Leader $3,497/mo.

---

## The Page I Need

- **Page name:** [e.g. Services, About, Pricing, Contact, Blog, Help, Landing Page]
- **File name:** [e.g. services.html]
- **URL:** https://lantech-website.vercel.app/[slug] [e.g. https://lantech-website.vercel.app/services]
- **Purpose:** [One sentence — what this page does for visitors]
- **Primary keyword:** [e.g. "web design for small businesses"]
- **Content to include:** [List the sections, copy, or reference any existing content]

---

## Brand & Design System

Use these EXACT values. Do not substitute Tailwind defaults or generic colors.

### Colors
```
Background:   #FAFAF7  (warm off-white — NEVER dark, NEVER pure white)
Surface:      #FFFFFF  (cards)
Text:         #1C1917  (warm near-black)
Muted text:   #78716C  (warm stone gray)
Accent:       #E8600A  (warm orange — the Rebel signal)
Accent hover: #C2500A
Blue:         #1D4ED8  (supporting blue for links only)
Border:       #E7E0D8  (warm border)
```

### CSS Variables (copy into every page's `<style>` block)
```css
:root {
  --bg: #FAFAF7;
  --surface: #FFFFFF;
  --txt: #1C1917;
  --muted: #78716C;
  --accent: #E8600A;
  --accent-hover: #C2500A;
  --blue: #1D4ED8;
  --border: #E7E0D8;
  --ink: #1C1917;
}
```

### Fonts (load via Google Fonts)
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Calistoga&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```
- **Headings (H1, H2, H3):** Calistoga, weight 400 (it's a display serif — do NOT use bold)
- **Body text:** DM Sans, 400–600
- **Labels, tags, code, prices:** JetBrains Mono, 400–500

### Typography Rules
- Large headings: `line-height: 1.15`, no letter-spacing override needed
- Body text: `line-height: 1.72`, `font-size: 1rem`, max-width 680px (65–75 chars/line)
- Section labels (uppercase eyebrow tags): JetBrains Mono, 0.68–0.72rem, letter-spacing 0.12em, color var(--accent)
- Body text: NO letter-spacing. Labels only get tracking.

### Styling Rules
- **Shadows:** Warm-tinted — `0 2px 12px rgba(28,25,23,.07)` (card rest), `0 8px 40px rgba(28,25,23,.10)` (hover lift). Never cold black shadows.
- **Gradients:** NO gradient text (`background-clip: text` is banned). No cyan-to-purple gradients.
- **Animations:** Only animate `transform` and `opacity`. NEVER `transition-all`. NEVER animate width/height/padding.
- **Cards:** background `var(--surface)` (#FFFFFF), border `1px solid var(--border)`, border-radius 8–16px, shadow on hover only (not at rest).
- **Buttons:** Primary = `var(--accent)` (#E8600A) bg + white text. Ghost = transparent + `var(--border)` border + `var(--txt)` text.
- **Hover states:** Every clickable element needs hover + focus-visible + active states. Focus ring: 2px solid `var(--accent)`, 3px offset.
- **Background:** Always `var(--bg)` (#FAFAF7). NEVER dark backgrounds for page body. NO glassmorphism, dot-grid textures, or ambient glow blobs.
- **No default Tailwind colors** (no indigo-500, blue-600, etc.)

---

## MANDATORY: Navigation (Exact Structure)

Every page must have this sticky top navigation:

```
[Lantech logo/wordmark — left] ........... [Nav links — center/right] ........... [CTA button]

Nav links (in order):
- Home        → index.html
- Services    → services.html
- Pricing     → pricing.html
- Blog        → blog.html
- About       → about.html
- Contact     → contact.html

Active link: highlight in var(--accent) (#E8600A orange)
CTA button: "Get a Free Quote" → contact.html (var(--accent) orange background, white text)
```

Mobile: hamburger menu that reveals the links as a vertical stack.

Logo: Use the Lantech wordmark. The real logo files are in `/brand_assets/`:
- Light backgrounds (page body): `lantech-logo-dark.png`
- Dark backgrounds (dark header/footer): `lantech-logo-white.png`
- Icon only: `lantech-icon-800.png`

---

## MANDATORY: Footer (Exact Structure)

Every page must have this footer:

```
[Lantech logo + tagline]    [Pages]           [Services]         [Contact]
                            Home              Web Design         lantech016@gmail.com
                            Services          SEO                +63 977 329 3969
                            Pricing           Google Business    
                            Blog              Social Media
                            About
                            Contact
                            Help

[Social icons: Facebook, Instagram, LinkedIn]

© 2026 Lantech. All rights reserved. | Privacy Policy | Terms of Service

Background: var(--ink) (#1C1917), top border: 1px solid rgba(255,255,255,0.06)
```

**IMPORTANT:** Use `lantech016@gmail.com` for email and `+63 977 329 3969` (tel:+639773293969) for phone.
Do NOT use lantech016@gmail.com on live pages — that is the internal/Gmail address only.

---

## MANDATORY: `<head>` SEO Block

Every page must include ALL of the following in `<head>`. Replace [BRACKETED] values
with the actual page data. Do not skip any tag.

```html
<!-- Core -->
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#FAFAF7">

<!-- Title & Description -->
<title>[Page Title — 50–60 characters, include primary keyword]</title>
<meta name="description" content="[150–160 characters. Include one specific stat or benefit. No generic copy.]">

<!-- Canonical -->
<link rel="canonical" href="https://lantech-website.vercel.app/[slug]">

<!-- Favicon -->
<link rel="icon" type="image/png" sizes="512x512" href="/brand_assets/lantech-icon-800.png">
<link rel="apple-touch-icon" sizes="180x180" href="/brand_assets/lantech-icon-800.png">

<!-- Open Graph (social sharing) -->
<meta property="og:type" content="website">
<meta property="og:site_name" content="Lantech">
<meta property="og:title" content="[Same as title tag]">
<meta property="og:description" content="[Same as meta description]">
<meta property="og:url" content="https://lantech-website.vercel.app/[slug]">
<meta property="og:image" content="https://lantech-website.vercel.app/brand_assets/lantech-fb-banner-820x312.png">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="[Same as title tag]">
<meta name="twitter:description" content="[Same as meta description]">
<meta name="twitter:image" content="https://lantech-website.vercel.app/brand_assets/lantech-fb-banner-820x312.png">
```

---

## MANDATORY: Schema JSON-LD by Page Type

Add the matching schema block before `</head>`. Pick the one that matches your page.

### Homepage (index.html)
```html
<script type="application/ld+json">
[
  {
    "@context": "https://schema.org",
    "@type": ["LocalBusiness", "ProfessionalService"],
    "name": "Lantech",
    "url": "https://lantech-website.vercel.app",
    "logo": "https://lantech-website.vercel.app/brand_assets/lantech-logo-dark.png",
    "image": "https://lantech-website.vercel.app/brand_assets/lantech-fb-banner-1640x624.png",
    "description": "Web design, SEO, and Google Business Profile optimization for home service contractors and local businesses across the United States.",
    "email": "lantech016@gmail.com",
    "telephone": "+639773293969",
    "priceRange": "$1,200 - $1,999",
    "openingHoursSpecification": {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
      "opens": "09:00", "closes": "18:00"
    },
    "areaServed": {"@type": "Country", "name": "United States"},
    "founder": {"@type": "Person", "name": "Luis Echarri"},
    "sameAs": ["https://facebook.com/lantechco", "https://instagram.com/lantechco"]
  },
  {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "Lantech",
    "url": "https://lantech-website.vercel.app"
  }
]
</script>
```

### Services page
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Lantech Services",
  "url": "https://lantech-website.vercel.app/services",
  "itemListElement": [
    {"@type":"ListItem","position":1,"item":{"@type":"Service","name":"Website Design & Development","provider":{"@type":"Organization","name":"Lantech"},"areaServed":{"@type":"Country","name":"United States"}}},
    {"@type":"ListItem","position":2,"item":{"@type":"Service","name":"Local SEO Optimization","provider":{"@type":"Organization","name":"Lantech"},"areaServed":{"@type":"Country","name":"United States"}}},
    {"@type":"ListItem","position":3,"item":{"@type":"Service","name":"Google Business Profile Optimization","provider":{"@type":"Organization","name":"Lantech"},"areaServed":{"@type":"Country","name":"United States"}}},
    {"@type":"ListItem","position":4,"item":{"@type":"Service","name":"Monthly SEO Retainer","provider":{"@type":"Organization","name":"Lantech"},"areaServed":{"@type":"Country","name":"United States"}}}
  ]
}
</script>
```

### Pricing page
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Lantech Pricing Plans",
  "url": "https://lantech-website.vercel.app/pricing",
  "itemListElement": [
    {"@type":"ListItem","position":1,"item":{"@type":"Offer","name":"Starter Package","price":"1200","priceCurrency":"USD","seller":{"@type":"Organization","name":"Lantech"}}},
    {"@type":"ListItem","position":2,"item":{"@type":"Offer","name":"Growth Package","price":"1699","priceCurrency":"USD","seller":{"@type":"Organization","name":"Lantech"}}},
    {"@type":"ListItem","position":3,"item":{"@type":"Offer","name":"Pro Package","price":"1999","priceCurrency":"USD","seller":{"@type":"Organization","name":"Lantech"}}}
  ]
}
</script>
```

### About page
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Lantech",
  "url": "https://lantech-website.vercel.app/about",
  "logo": "https://lantech-website.vercel.app/brand_assets/lantech-logo-white.png",
  "description": "A web design studio helping home service businesses rank on Google and turn local searches into booked jobs. Founded by Luis Echarri.",
  "founder": {"@type": "Person", "name": "Luis Echarri"},
  "email": "lantech016@gmail.com",
  "telephone": "+639773293969",
  "areaServed": {"@type": "Country", "name": "United States"}
}
</script>
```

### Contact page
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ContactPage",
  "name": "Contact Lantech",
  "url": "https://lantech-website.vercel.app/contact",
  "mainEntity": {
    "@type": "Organization",
    "name": "Lantech",
    "email": "lantech016@gmail.com",
    "telephone": "+639773293969",
    "contactPoint": {
      "@type": "ContactPoint",
      "contactType": "sales",
      "email": "lantech016@gmail.com",
      "availableLanguage": "English",
      "hoursAvailable": {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
        "opens": "09:00", "closes": "18:00"
      }
    }
  }
}
</script>
```

### Blog index page
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Blog",
  "name": "Lantech Blog",
  "url": "https://lantech-website.vercel.app/blog",
  "publisher": {"@type":"Organization","name":"Lantech","url":"https://lantech-website.vercel.app"},
  "inLanguage": "en-US"
}
</script>
```

### Blog article page
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "[Article title]",
  "description": "[Article meta description]",
  "url": "https://lantech-website.vercel.app/blog/[slug]",
  "datePublished": "[YYYY-MM-DD]",
  "dateModified": "[YYYY-MM-DD]",
  "author": {"@type":"Person","name":"Luis Echarri"},
  "publisher": {
    "@type": "Organization",
    "name": "Lantech",
    "url": "https://lantech-website.vercel.app",
    "logo": "https://lantech-website.vercel.app/brand_assets/lantech-logo-white.png"
  },
  "image": "[Cover image URL]",
  "inLanguage": "en-US"
}
</script>
```

### Help page
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "Help Center — Lantech",
  "url": "https://lantech-website.vercel.app/help",
  "isPartOf": {"@type":"WebSite","name":"Lantech","url":"https://lantech-website.vercel.app"},
  "breadcrumb": {
    "@type": "BreadcrumbList",
    "itemListElement": [
      {"@type":"ListItem","position":1,"name":"Home","item":"https://lantech-website.vercel.app"},
      {"@type":"ListItem","position":2,"name":"Help Center","item":"https://lantech-website.vercel.app/help"}
    ]
  }
}
</script>
```

### Any page with an FAQ section — add this ALSO
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[Question text]",
      "acceptedAnswer": {"@type":"Answer","text":"[Answer text]"}
    }
  ]
}
</script>
```

---

## MANDATORY: Content Rules

### What to ALWAYS include
- **One H1 per page** — contains the primary keyword
- **H2s for all major sections** — 60% phrased as questions
- **Internal links** — every page must link to at least 2 other Lantech pages naturally in the copy
- **One clear CTA** — every page ends with a call-to-action section (usually "Get a Free Quote → contact.html")
- **Real copy** — write actual content for the page. No lorem ipsum. No placeholder text.
- **Author credit** on blog posts — "By Luis Echarri · Founder of Lantech"

### What to NEVER do
- NEVER invent a phone number. If no phone is provided, leave it out.
- NEVER invent an address. If no address is provided, leave it out.
- NEVER use `href="#"` for links that should go somewhere real.
- NEVER use placeholder images via placehold.co on live pages.
- NEVER put duplicate text in heading and sub-label on the same element.
- NEVER use the default Tailwind color palette (blue-600, indigo-500, etc.).
- NEVER use `transition-all`.
- NEVER claim stats or numbers that aren't provided (e.g., "24+ articles" when only 6 exist).
- NEVER use AI-detectable filler phrases: "dive into", "game-changer", "leverage", "seamlessly", "crucial", "in today's landscape", "delve", "robust", "tapestry".

### Consistency across all pages
These values must match exactly everywhere they appear:

| Field | Value |
|---|---|
| Business name | Lantech (not "LanTech", not "LANTECH") |
| Founder | Luis Echarri |
| Public email | lantech016@gmail.com |
| Internal email | lantech016@gmail.com (never show on live pages) |
| Phone | +63 977 329 3969 |
| Starter price | $1,200 |
| Growth price | $1,699 |
| Pro price | $1,999 |
| Delivery time | Live within a week (not "48 hours" — that claim was removed) |
| Business hours | Mon–Fri, 9am–6pm |
| Website URL | https://lantech-website.vercel.app |

---

## MANDATORY: Technical Requirements

### Page must include
- [ ] `<!DOCTYPE html>` and `<html lang="en">`
- [ ] `<meta charset="UTF-8">` as first tag in `<head>`
- [ ] `<meta name="viewport">` as second tag
- [ ] Title tag (50–60 chars)
- [ ] Meta description (150–160 chars)
- [ ] Canonical link tag
- [ ] Favicon link tags
- [ ] OG meta tags (all 6)
- [ ] Twitter Card meta tags (all 4)
- [ ] theme-color meta
- [ ] JSON-LD schema block (correct type for page)
- [ ] Google Fonts loaded via `<link>`
- [ ] Mobile responsive (works on 375px width)
- [ ] All interactive elements have hover + focus + active states

### For new HTML pages in /blog subfolder
- Use `../` prefix for all links back to main pages (e.g., `../services.html`, `../contact.html`)
- Use `../brand_assets/` for logo and favicon paths

### File should NOT include
- Tailwind CDN script (for blog articles — write CSS directly)
- Inline `onclick` or `onmouseover` event handlers (use CSS :hover instead)
- Any reference to a test/localhost URL

---

## Asset Paths

All brand assets live in `/brand_assets/`:

| File | Use |
|---|---|
| `lantech-logo-white.png` | Logo on dark backgrounds |
| `lantech-logo-dark.png` | Logo on light backgrounds |
| `lantech-icon-800.png` | Favicon, app icon, small logo |
| `lantech-fb-banner-820x312.png` | OG/social share image |

---

## Site Map (All Pages)

| Page | File | Canonical URL |
|---|---|---|
| Homepage | index.html | https://lantech-website.vercel.app/ |
| Services | services.html | https://lantech-website.vercel.app/services |
| Pricing | pricing.html | https://lantech-website.vercel.app/pricing |
| About | about.html | https://lantech-website.vercel.app/about |
| Contact | contact.html | https://lantech-website.vercel.app/contact |
| Blog index | blog.html | https://lantech-website.vercel.app/blog |
| Help | help.html | https://lantech-website.vercel.app/help |
| Blog articles | blog/[slug].html | https://lantech-website.vercel.app/blog/[slug] |

---

## How to Use This Brief

1. **Copy this entire document**
2. **Fill in the [BRACKETED] fields** at the top (page name, URL, purpose, keyword, content)
3. **Paste into Claude** (web or Code) and say:
   *"Using the brief below, build the [page name] page as a complete, standalone HTML file."*
4. **Claude will generate** a fully designed, SEO-optimized page with no missing tags

This eliminates post-build SEO fixes entirely.
