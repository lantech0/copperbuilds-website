# Site Structure — Website Development for Small Business (USA)
> Generated: 2026-04-17

---

## URL Hierarchy

```
/  (Home)
│   Target: "website design for small business"
│
├── /services/
│   ├── /services/web-design/
│   │   Target: "professional website design for small business"
│   ├── /services/ecommerce-websites/
│   │   Target: "ecommerce website design for small business"
│   ├── /services/wordpress-websites/
│   │   Target: "WordPress website design for small business"
│   ├── /services/landing-pages/
│   │   Target: "landing page design for small business"
│   └── /services/website-redesign/
│       Target: "website redesign for small business"
│
├── /pricing/
│   Target: "small business website design packages", "website design pricing"
│
├── /industries/
│   ├── /industries/restaurants/          → "restaurant website design"
│   ├── /industries/plumbers/             → "plumber website design"
│   ├── /industries/electricians/         → "electrician website design"
│   ├── /industries/salons/               → "salon website design"
│   ├── /industries/law-firms/            → "law firm website design small business"
│   ├── /industries/real-estate/          → "real estate website design"
│   ├── /industries/contractors/          → "contractor website design"
│   ├── /industries/dentists/             → "dental website design"
│   ├── /industries/gyms/                 → "gym website design small business"
│   └── /industries/retail/               → "retail store website design"
│
├── /locations/
│   ├── /locations/new-york/              → "web design for small business New York"
│   ├── /locations/los-angeles/           → "web design for small business Los Angeles"
│   ├── /locations/chicago/               → "web design for small business Chicago"
│   ├── /locations/houston/               → "web design for small business Houston"
│   ├── /locations/phoenix/               → "web design for small business Phoenix"
│   ├── /locations/philadelphia/          → "web design for small business Philadelphia"
│   ├── /locations/san-antonio/           → "web design for small business San Antonio"
│   ├── /locations/dallas/                → "web design for small business Dallas"
│   ├── /locations/miami/                 → "web design for small business Miami"
│   └── /locations/atlanta/              → "web design for small business Atlanta"
│
├── /work/  (Portfolio / Case Studies)
│   ├── /work/[client-1]/
│   ├── /work/[client-2]/
│   └── /work/[client-3]/
│
├── /about/
│   └── /about/team/
│       └── /about/team/[member-name]/
│
├── /blog/
│   ├── /blog/how-much-does-a-website-cost-small-business/
│   ├── /blog/why-small-businesses-need-a-website/
│   ├── /blog/small-business-website-checklist/
│   └── (20+ articles — see Content Calendar)
│
├── /faq/
├── /process/
└── /contact/
```

---

## Page Priority (Build Order)

| Priority | Page | Reason |
|---|---|---|
| P0 | Home | Brand + primary keyword |
| P0 | /services/web-design/ | Main commercial page |
| P0 | /pricing/ | Conversion + keyword |
| P0 | /contact/ | Lead capture |
| P1 | /about/ + /about/team/ | E-E-A-T signals |
| P1 | /work/ + 3 case studies | Trust + E-E-A-T |
| P1 | /faq/ | Schema + informational |
| P2 | /services/* (sub-pages) | Service keyword coverage |
| P2 | /industries/* (top 5) | Vertical keyword capture |
| P2 | Blog (first 5 posts) | Informational traffic |
| P3 | /locations/* (top 10 cities) | Local keyword capture |
| P3 | /industries/* (remaining 5) | More verticals |
| P4 | Blog (ongoing) | Authority building |

---

## Internal Linking Strategy

- Home → /services/web-design/ (primary CTA)
- Home → /pricing/ (secondary CTA)
- Every service page → /pricing/ + /contact/
- Every industry page → relevant service page + /work/ case study
- Every blog post → 2–3 service or industry pages
- /work/ case studies → relevant industry page
- /pricing/ → /contact/ + /faq/

---

## Schema Plan by Page Type

| Page Type | Schema |
|---|---|
| Home | Organization, ProfessionalService |
| Service Pages | Service, ProfessionalService |
| Pricing | Service (with Offer/price) |
| Industry Pages | Service, FAQPage |
| Location Pages | LocalBusiness, Service |
| Case Studies | Article |
| Team Member | Person, ProfilePage |
| Blog Posts | Article, BlogPosting, FAQPage |
| FAQ Page | FAQPage |
