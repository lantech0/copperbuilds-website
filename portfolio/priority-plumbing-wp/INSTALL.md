# Installing the Priority Plumbing & Drain WordPress Theme

This theme is built the "real WordPress" way: the templates (`front-page.php`, `page-about.php`, `page-services.php`, `page-contact.php`) just render `the_content()` — all the actual copy lives in the WordPress block editor, same as any normal WP site. That means after activating the theme, each page's content has to be pasted in once (step 3 below), and SEO (title/meta/schema) is handled by whatever SEO plugin you install (step 5), not hardcoded in the theme.

## 1. Upload the theme

**Option A — WP Admin (simplest):**
1. Zip the `priority-plumbing-wp/` folder so the zip's top level is that single folder (i.e. `style.css` sits one level inside the zip, at `priority-plumbing-wp/style.css` — not loose at the zip's root).
2. In wp-admin: Appearance → Themes → Add New → Upload Theme → choose the zip → Install → Activate.

**Option B — FTP/SFTP:**
1. Upload this whole folder to `wp-content/themes/priority-plumbing-wp/` on the host.
2. In wp-admin: Appearance → Themes → activate "Priority Plumbing & Drain".

## 2. Create the pages

Go to Pages → Add New and create exactly these 4 pages (slug must match — WordPress sets it from the title automatically, lowercased with dashes):

| Page title | Slug (auto from title) |
|---|---|
| Home | `home` (slug doesn't matter for this one — see step 4) |
| About | `about` |
| Services | `services` |
| Contact | `contact` |

## 3. Paste in each page's content

For each page, open it in the block editor, click the three-dot menu (top right) → **Code editor**, delete anything there, and paste in the matching file from this theme's `content/` folder:

| Page | Paste from |
|---|---|
| Home | `content/front-page.html` |
| About | `content/about.html` |
| Services | `content/services.html` |
| Contact | `content/contact.html` |

Click the three-dot menu again → **Visual editor** to switch back, then **Update/Publish** the page. You should see real, distinct blocks (headings, paragraphs, lists, images) you can click into and edit directly — that's the point of this rebuild.

**One thing you'll notice:** some blocks in the editor show as an empty-looking "Custom HTML" box with no preview, usually right before or after the blocks you can actually edit. Those are intentional structural markers (they open or close a styled wrapper `<div>` that the real content sits inside) — leave them alone. Don't delete one without deleting its matching pair, or the layout for that section will break. Everything you'd actually want to change — headlines, paragraphs, prices, service checklists, FAQ answers, reviews, team/credential copy — is a normal Heading/Paragraph/List block you can click straight into.

## 4. Set the homepage and permalinks

- Settings → Reading → "Your homepage displays" → Static Page → set Homepage to the "Home" page you created.
- Settings → Permalinks → select **"Post name"** → Save. Required — the theme's nav/footer links point to `/about/`, `/services/`, `/contact/`, which 404 on the default "Plain" setting.

## 5. Install an SEO plugin (RankMath or Yoast)

The theme does not output its own title tag, meta description, canonical URL, Open Graph tags, or schema — that's the SEO plugin's job.

1. Install RankMath (or Yoast SEO) from Plugins → Add New.
2. Run its setup wizard — enter the business as a Local Business / Plumber type, fill in NAP (name/address/phone), logo, and social profiles once; this drives the site-wide schema.
3. On each of the 4 pages, open the plugin's SEO box and set the SEO title + meta description. Suggested titles/descriptions (from the original build) if you want a starting point:

| Page | Suggested SEO title | Suggested meta description |
|---|---|---|
| Home | Plumbing Services Tampa FL \| Priority Plumbing & Drain \| 24/7 Emergency | Priority Plumbing & Drain — licensed plumber in Tampa FL available 24/7. Emergency plumbing, drain cleaning, water heater repair & replacement. Same-day service. Call (813) 555-0194. |
| About | Licensed Plumber Tampa FL \| About Priority Plumbing & Drain | Priority Plumbing & Drain — licensed plumbing company in Tampa FL since 2009. Family-owned, Lic. # CFC1431872. Meet the team behind Tampa's most-trusted plumber. |
| Services | Emergency Plumber Tampa FL \| Services \| Priority Plumbing & Drain | Emergency plumbing, drain cleaning, water heater repair, leak detection & sewer service in Tampa FL. Licensed plumber available 24/7. Call (813) 555-0194. |
| Contact | Plumber Tampa FL Free Estimate \| Contact Priority Plumbing & Drain | Contact Priority Plumbing & Drain for a free estimate in Tampa FL. Available 24/7 for emergency plumbing. Call (813) 555-0194 or fill out the form — we respond within 15 minutes. |

4. For the FAQ schema (the accordion on Home, the plain list on About, and the 4 FAQ cards on Services), use RankMath's FAQ block/schema block if you want that markup back — the original static mock's hardcoded JSON-LD for this was intentionally not carried over.

## 6. Verify

- Visit the homepage — hero, social proof bar, response strip, services grid, financing band, process steps, why-us, service areas, reviews, FAQ accordion, guarantee band, and footer should all render, and the browser tab should show the real SEO title (not "My Blog" — if it still does, the SEO plugin isn't configured for that page yet).
- Click through Home → Services → About → Contact in the nav — confirm no 404s.
- Click a service card on the homepage (e.g. "Emergency Plumbing") — should land on `/services/#emergency` and jump to that section.
- Click the FAQ accordion questions on the homepage — each should expand/collapse independently, only one open at a time.
- Check mobile width (375px) — sticky Call/Get Estimate bar should appear at the bottom on every page.
- Try editing a piece of text (a review, an FAQ answer, a checklist item) directly in the block editor and confirm it updates on the live page.

## Deviations from a pure copy (disclosed, not silent)

- **Mobile sticky CTA bar is now on every page.** The original static mock only included it on `index.html` — About, Services, and Contact never had it. Since header/footer are shared PHP templates across all 4 WordPress pages, the bar now appears everywhere. This is an improvement (consistent contact access), not a bug.
- **Footer unified to the richer 4-column version.** The static mock's About/Services/Contact pages used a 3-column footer with no Google rating badge; Home used a 4-column footer with a "Service Areas" column and a star-rating badge. The WordPress theme uses Home's richer version site-wide, same approach used for the CopperBuilds/Elite Air Services conversion.
- **Homepage FAQ section renamed internally from `.faq-bg` to `.faq-section`.** The original static mock reused the class `.faq-bg` for two visually different things — the homepage's interactive accordion-with-sidebar FAQ, and the Services page's static two-column FAQ cards. Reusing the same class name for both would have caused a CSS collision once merged into one stylesheet, so the homepage's version was renamed to `.faq-section` (matching the class-collision fix already used on the Elite Air Services HVAC theme). Purely an internal class-naming change — nothing a site editor will ever see or need to touch.
- Google Fonts (Open Sans, Barlow Condensed) load from Google's CDN — if the eventual host requires zero third-party requests, self-host them instead (see `functions.php` → `pp_enqueue_assets()`).

## Known limitations (carried over from the original static mock, not new)

- The contact form (via the `[pp_contact_form]` shortcode in `functions.php`) has no backend — it doesn't send email or store leads. If real lead capture is needed, install WPForms or Contact Form 7 and replace the shortcode in the Contact page's content with theirs.
- All content (phone number, address, reviews, pricing, license number) is placeholder demo content from the CopperBuilds portfolio mock — replace with the real business's actual details before this goes live for a real client.
- The Google Maps embed on the Contact page uses a placeholder `iframe` URL — replace with a real embed URL for the actual business address before going live.
