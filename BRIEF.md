# Lantech Website — Master Page Brief

Paste this entire document into Claude when asking it to build or redesign any page.
Fill in the [BRACKETED] fields before sending.

---

## Who This Is For

**Lantech** is a US-based web design agency founded by Luis Echarri. We build fast,
affordable websites and local SEO for small businesses across the United States.
Flat-rate packages: Starter $1,200 · Growth $1,699 · Pro $1,999.

---

## The Page I Need

- **Page name:** [e.g. Services, About, Pricing, Contact, Blog, Help, Landing Page]
- **File name:** [e.g. services.html]
- **URL:** https://lantech.co/[slug] [e.g. https://lantech.co/services]
- **Purpose:** [One sentence — what this page does for visitors]
- **Primary keyword:** [e.g. "web design for small businesses"]
- **Content to include:** [List the sections, copy, or reference any existing content]

---

## Brand & Design System

Use these EXACT values. Do not substitute Tailwind defaults or generic colors.

### Colors
```
Background:   #07070E
Surface:      #0D0D1A
Elevated:     #141428
Cyan accent:  #00E5FF
Purple:       #7C5CFC
Body text:    #EAEAF5
Muted text:   #8A8AAA
Border:       rgba(255,255,255,0.06)
```

### CSS Variables (copy into every page's `<style>` block)
```css
:root {
  --bg: #07070E;
  --surface: #0D0D1A;
  --elevated: #141428;
  --accent: #00E5FF;
  --accent2: #7C5CFC;
  --txt: #EAEAF5;
  --muted: #8A8AAA;
  --border: rgba(255,255,255,0.06);
  --accent-dim: rgba(0,229,255,0.06);
  --accent-border: rgba(0,229,255,0.18);
  --purple-dim: rgba(124,92,252,0.08);
  --purple-border: rgba(124,92,252,0.22);
}
```

### Fonts (load via Google Fonts)
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@700;800&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
```
- **Headings (H1, H2):** Unbounded, 700–800
- **Body text:** Plus Jakarta Sans, 400–700
- **Labels, tags, code:** IBM Plex Mono, 400–500

### Typography Rules
- Large headings: `letter-spacing: -0.025em`, `line-height: 1.1`
- Body text: `line-height: 1.7`, `font-size: 0.9375rem`
- Section labels (uppercase tags): IBM Plex Mono, 0.68rem, letter-spacing 0.12em

### Styling Rules
- **Shadows:** Layered with color tint — `0 16px 48px rgba(0,0,0,.35), 0 0 0 1px var(--accent-border)`
- **Gradients:** `linear-gradient(135deg, #00E5FF 0%, #7C5CFC 100%)` for gradient text
- **Animations:** Only animate `transform` and `opacity`. NEVER use `transition-all`
- **Cards:** background `var(--surface)`, border `1px solid var(--border)`, border-radius 14px
- **Buttons:** Primary = cyan bg `#00E5FF` + dark text. Ghost = transparent + white border
- **Hover states:** Every clickable element needs hover + focus-visible + active states
- **Background depth:** Use radial gradient glows (cyan and purple) + dot-grid texture
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

Active link: highlight in var(--accent) cyan
CTA button: "Get a Free Quote" → contact.html (cyan background, dark text)
```

Mobile: hamburger menu that reveals the links as a vertical stack.

Logo: Use the Lantech wordmark in Unbounded font. The real logo files are in `/brand_assets/`:
- Light backgrounds: `lantech-logo-dark.png`
- Dark backgrounds: `lantech-logo-white.png`
- Icon only: `lantech-icon-800.png`

---

## MANDATORY: Footer (Exact Structure)

Every page must have this footer:

```
[Lantech logo + tagline]    [Pages]           [Services]         [Contact]
                            Home              Web Design         hello@lantech.co
                            Services          SEO                [Phone — TBD]
                            Pricing           Google Business    [City, State — TBD]
                            Blog              Social Media
                            About
                            Contact
                            Help

[Social icons: Facebook, Instagram, LinkedIn]

© 2026 Lantech. All rights reserved. | Privacy Policy | Terms of Service

Background: #07070E, top border: 1px solid var(--border)
```

**IMPORTANT:** Do NOT invent a phone number or address. If those are not provided, omit them.
Use `hello@lantech.co` for email.

---

## MANDATORY: `<head>` SEO Block

Every page must include ALL of the following in `<head>`. Replace [BRACKETED] values
with the actual page data. Do not skip any tag.

```html
<!-- Core -->
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#07070E">

<!-- Title & Description -->
<title>[Page Title — 50–60 characters, include primary keyword]</title>
<meta name="description" content="[150–160 characters. Include one specific stat or benefit. No generic copy.]">

<!-- Canonical -->
<link rel="canonical" href="https://lantech.co/[slug]">

<!-- Favicon -->
<link rel="icon" type="image/png" sizes="512x512" href="/brand_assets/lantech-icon-800.png">
<link rel="apple-touch-icon" sizes="180x180" href="/brand_assets/lantech-icon-800.png">

<!-- Open Graph (social sharing) -->
<meta property="og:type" content="website">
<meta property="og:site_name" content="Lantech">
<meta property="og:title" content="[Same as title tag]">
<meta property="og:description" content="[Same as meta description]">
<meta property="og:url" content="https://lantech.co/[slug]">
<meta property="og:image" content="https://lantech.co/brand_assets/lantech-fb-banner-820x312.png">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="[Same as title tag]">
<meta name="twitter:description" content="[Same as meta description]">
<meta name="twitter:image" content="https://lantech.co/brand_assets/lantech-fb-banner-820x312.png">
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
    "url": "https://lantech.co",
    "logo": "https://lantech.co/brand_assets/lantech-logo-white.png",
    "image": "https://lantech.co/brand_assets/lantech-fb-banner-820x312.png",
    "description": "Web design, SEO, Google Business Profile optimization, and social media services for small businesses across the United States.",
    "email": "hello@lantech.co",
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
    "url": "https://lantech.co"
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
  "url": "https://lantech.co/services",
  "itemListElement": [
    {"@type":"ListItem","position":1,"item":{"@type":"Service","name":"Web Design & Development","provider":{"@type":"Organization","name":"Lantech"},"areaServed":{"@type":"Country","name":"United States"}}},
    {"@type":"ListItem","position":2,"item":{"@type":"Service","name":"SEO Optimization","provider":{"@type":"Organization","name":"Lantech"},"areaServed":{"@type":"Country","name":"United States"}}},
    {"@type":"ListItem","position":3,"item":{"@type":"Service","name":"Google Business Profile Optimization","provider":{"@type":"Organization","name":"Lantech"},"areaServed":{"@type":"Country","name":"United States"}}},
    {"@type":"ListItem","position":4,"item":{"@type":"Service","name":"Social Media Optimization","provider":{"@type":"Organization","name":"Lantech"},"areaServed":{"@type":"Country","name":"United States"}}}
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
  "url": "https://lantech.co/pricing",
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
  "url": "https://lantech.co/about",
  "logo": "https://lantech.co/brand_assets/lantech-logo-white.png",
  "description": "A dedicated web design studio helping US small businesses grow online with fast, affordable websites and SEO. Founded by Luis Echarri.",
  "founder": {"@type": "Person", "name": "Luis Echarri"},
  "email": "hello@lantech.co",
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
  "url": "https://lantech.co/contact",
  "mainEntity": {
    "@type": "Organization",
    "name": "Lantech",
    "email": "hello@lantech.co",
    "contactPoint": {
      "@type": "ContactPoint",
      "contactType": "sales",
      "email": "hello@lantech.co",
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
  "url": "https://lantech.co/blog",
  "publisher": {"@type":"Organization","name":"Lantech","url":"https://lantech.co"},
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
  "url": "https://lantech.co/blog/[slug]",
  "datePublished": "[YYYY-MM-DD]",
  "dateModified": "[YYYY-MM-DD]",
  "author": {"@type":"Person","name":"Luis Echarri"},
  "publisher": {
    "@type": "Organization",
    "name": "Lantech",
    "url": "https://lantech.co",
    "logo": "https://lantech.co/brand_assets/lantech-logo-white.png"
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
  "url": "https://lantech.co/help",
  "isPartOf": {"@type":"WebSite","name":"Lantech","url":"https://lantech.co"},
  "breadcrumb": {
    "@type": "BreadcrumbList",
    "itemListElement": [
      {"@type":"ListItem","position":1,"name":"Home","item":"https://lantech.co"},
      {"@type":"ListItem","position":2,"name":"Help Center","item":"https://lantech.co/help"}
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
| Email | hello@lantech.co |
| Starter price | $1,200 |
| Growth price | $1,699 |
| Pro price | $1,999 |
| Delivery time | 48 hours (not "48h", not "2 days", not "5 days") |
| Business hours | Mon–Fri, 9am–6pm EST |
| Website URL | https://lantech.co |

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
| Homepage | index.html | https://lantech.co/ |
| Services | services.html | https://lantech.co/services |
| Pricing | pricing.html | https://lantech.co/pricing |
| About | about.html | https://lantech.co/about |
| Contact | contact.html | https://lantech.co/contact |
| Blog index | blog.html | https://lantech.co/blog |
| Help | help.html | https://lantech.co/help |
| Blog articles | blog/[slug].html | https://lantech.co/blog/[slug] |

---

## How to Use This Brief

1. **Copy this entire document**
2. **Fill in the [BRACKETED] fields** at the top (page name, URL, purpose, keyword, content)
3. **Paste into Claude** (web or Code) and say:
   *"Using the brief below, build the [page name] page as a complete, standalone HTML file."*
4. **Claude will generate** a fully designed, SEO-optimized page with no missing tags

This eliminates post-build SEO fixes entirely.
