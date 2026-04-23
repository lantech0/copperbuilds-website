# Client Website Brief — [CLIENT BUSINESS NAME]
> Filled out by Luis Echarri from the completed onboarding questionnaire.
> Paste this entire document into Claude to build any page for this client.

---

## HOW TO USE THIS TEMPLATE

1. Complete the client's onboarding questionnaire (`02-onboarding-questionnaire.md`)
2. Copy this file and rename it: `[client-slug]-brief.md` (e.g. `mikes-plumbing-brief.md`)
3. Fill in every [BRACKETED] field below using the questionnaire answers
4. Paste the completed brief into Claude and say:
   *"Using the brief below, build the [page name] page as a complete, standalone HTML file."*

---

## THE CLIENT

| Field | Value |
|---|---|
| Business name | [EXACT business name] |
| Owner name | [Owner first + last name] |
| Industry | [e.g. Plumbing, Restaurant, Law Firm, Salon] |
| City / State | [City, State — e.g. Austin, TX] |
| Service area | [All cities/areas they serve] |
| Phone | [Real phone number] |
| Email | [Contact email] |
| Address | [Street, City, State, ZIP — or "service area business, no storefront"] |
| Business hours | [e.g. Mon–Fri 8am–6pm, Sat 9am–2pm] |
| Domain | [e.g. mikesplumbingaustin.com] |
| Google Business Profile | [URL or "not set up"] |
| Years in business | [e.g. 12 years] |
| Tagline / slogan | [If they have one] |

---

## BRAND

| Field | Value |
|---|---|
| Primary color | [Hex code — e.g. #1A3C6B] |
| Secondary color | [Hex code] |
| Accent color | [Hex code if any] |
| Font — headings | [Font name or "choose appropriate"] |
| Font — body | [Font name or "choose appropriate"] |
| Brand personality | [e.g. Trustworthy, professional, local, friendly] |
| Logo file | [Path or "attached" or "no logo"] |
| Style direction | [e.g. "Clean and professional", "Bold and modern", "Warm and local"] |
| Design references | [URLs of sites they like, or "none provided"] |
| What to avoid | [Any styles, colors, or elements they don't want] |

---

## THE PAGE I NEED BUILT

| Field | Value |
|---|---|
| Page name | [e.g. Homepage, Services, About, Contact] |
| File name | [e.g. index.html, services.html] |
| Canonical URL | https://[domain]/[slug] |
| Page purpose | [One sentence — what this page does] |
| Primary keyword | [e.g. "plumber in Austin TX"] |
| Secondary keywords | [2–3 related terms] |
| Primary CTA | [e.g. "Call now", "Get a free quote", "Book an appointment"] |
| CTA destination | [Phone number / contact form / booking link] |

---

## SERVICES TO HIGHLIGHT

List the top 3 services in order of priority:

1. **[Service name]** — [1–2 sentence description]
2. **[Service name]** — [1–2 sentence description]
3. **[Service name]** — [1–2 sentence description]

---

## UNIQUE SELLING POINTS

What makes this business different from competitors:
- [USP 1 — e.g. "Same-day service guaranteed"]
- [USP 2 — e.g. "Family-owned since 1998"]
- [USP 3 — e.g. "Licensed and insured, free estimates"]

---

## TESTIMONIALS

*(Paste real testimonials from questionnaire or Google reviews. Include name + business/location.)*

> "[Quote]"
> — [Customer name], [City or business]

> "[Quote]"
> — [Customer name], [City or business]

> "[Quote]"
> — [Customer name], [City or business]

---

## CONTENT NOTES

- Copy provided by client: [Yes / No / Partial — list which pages]
- Photos provided: [Yes / No / Partial]
- Existing content to reference: [Links or "none"]
- Tone of voice: [e.g. "Conversational and friendly", "Professional and direct"]

---

## MANDATORY SEO HEAD BLOCK
*(Pre-filled for Claude — update per page)*

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="[PRIMARY COLOR HEX]">
<title>[Page title — 50–60 chars, include primary keyword and city]</title>
<meta name="description" content="[150–160 chars — specific benefit + city + CTA]">
<link rel="canonical" href="https://[domain]/[slug]">
<link rel="icon" type="image/png" href="/favicon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="[Business name]">
<meta property="og:title" content="[Page title]">
<meta property="og:description" content="[Meta description]">
<meta property="og:url" content="https://[domain]/[slug]">
<meta property="og:image" content="https://[domain]/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="[Page title]">
<meta name="twitter:description" content="[Meta description]">
<meta name="twitter:image" content="https://[domain]/og-image.jpg">
```

---

## MANDATORY SCHEMA — LocalBusiness
*(Required on homepage and contact page for every client)*

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": ["LocalBusiness", "[SCHEMA TYPE — see list below]"],
  "name": "[Business name]",
  "url": "https://[domain]",
  "telephone": "[Phone number]",
  "email": "[Email]",
  "description": "[2-sentence business description]",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[Street]",
    "addressLocality": "[City]",
    "addressRegion": "[State]",
    "postalCode": "[ZIP]",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": [LAT],
    "longitude": [LNG]
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
      "opens": "[09:00]",
      "closes": "[17:00]"
    }
  ],
  "areaServed": [
    {"@type": "City", "name": "[City]"},
    {"@type": "State", "name": "[State]"}
  ],
  "priceRange": "[$ / $$ / $$$ or price range]",
  "image": "https://[domain]/og-image.jpg",
  "sameAs": [
    "[Facebook URL]",
    "[Instagram URL]",
    "[Yelp URL]"
  ]
}
</script>
```

### Schema @type by industry

| Industry | @type to use |
|---|---|
| Plumber, electrician, HVAC, landscaper | `Plumber` / `Electrician` / `HVACBusiness` / `LandscapingBusiness` |
| Restaurant, café, bar | `Restaurant` / `FoodEstablishment` / `CafeOrCoffeeShop` |
| Law firm, attorney | `LegalService` / `Attorney` |
| Medical, dentist, doctor | `MedicalBusiness` / `Dentist` / `Physician` |
| Salon, spa, barber | `BeautySalon` / `HairSalon` / `NailSalon` |
| Auto repair, car dealership | `AutoRepair` / `CarDealer` |
| Real estate agent | `RealEstateAgent` |
| Gym, fitness studio | `HealthAndBeautyBusiness` / `SportsActivityLocation` |
| General contractor | `GeneralContractor` |
| Retail store | `Store` |
| Generic service business | `ProfessionalService` or `LocalBusiness` |

---

## NAVIGATION STRUCTURE

Build a sticky top nav with:
- Logo (left) — use provided logo file, or styled business name text
- Nav links: [List the pages for this client's site]
- CTA button (right): "[Primary CTA text]" → [CTA destination]
- Mobile: hamburger menu

---

## FOOTER STRUCTURE

Include in footer:
- Logo + 1-line tagline
- Links: [list pages]
- Contact column: [Phone], [Email], [Address if applicable]
- Social icons: [list platforms with URLs]
- Hours: [Business hours]
- Copyright: © 2026 [Business name]. All rights reserved.
- Links: Privacy Policy | Terms of Service

---

## CONTENT RULES FOR THIS CLIENT

### Always include
- Business name, city, and primary keyword in the H1
- Physical address and phone number visible on every page (above the fold on contact page)
- Google Maps embed on contact page
- Real testimonials — do not fabricate reviews
- Real photos where provided — do not use placeholder images on live pages

### Never do
- Invent phone numbers, addresses, or statistics not provided by the client
- Use generic copy ("We are a leading provider of...") — write specific, local copy
- Use `href="#"` for any link that should go somewhere real
- Duplicate the title tag text in a visible H1 on the same page (reword one of them)
- Make guarantees or claims the client didn't confirm (e.g. "24/7 service" unless confirmed)

---

## SITE MAP FOR THIS PROJECT

| Page | File | URL | Priority |
|---|---|---|---|
| Homepage | index.html | https://[domain]/ | Must have |
| Services | services.html | https://[domain]/services | Must have |
| About | about.html | https://[domain]/about | Must have |
| Contact | contact.html | https://[domain]/contact | Must have |
| [Additional page] | [file] | https://[domain]/[slug] | [if in package] |

---

## DELIVERY CHECKLIST
*(Verify before sending preview to client)*

- [ ] Every page has a unique title tag (50–60 chars)
- [ ] Every page has a unique meta description (150–160 chars)
- [ ] Every page has canonical tag
- [ ] Every page has OG + Twitter Card tags
- [ ] Homepage has LocalBusiness JSON-LD schema with real address + phone
- [ ] Any FAQ section has FAQPage schema
- [ ] robots.txt created
- [ ] sitemap.xml created with all page URLs
- [ ] Contact form tested and submitting correctly
- [ ] All internal links work (no broken links)
- [ ] Mobile layout tested at 375px width
- [ ] All images have descriptive alt text
- [ ] No placeholder content visible (no lorem ipsum, no fake phone numbers)
- [ ] Google Analytics tag installed (if client provided GA4 ID)
