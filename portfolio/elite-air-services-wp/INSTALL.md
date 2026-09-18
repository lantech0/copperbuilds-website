# Installing the Elite Air Services WordPress Theme

This theme is built the "real WordPress" way: the templates (`front-page.php`, `page-about.php`, `page-services.php`, `page-contact.php`) just render `the_content()` — all the actual copy lives in the WordPress block editor, same as any normal WP site. That means after activating the theme, each page's content has to be pasted in once (step 3 below), and SEO (title/meta/schema) is handled by whatever SEO plugin you install (step 5), not hardcoded in the theme.

## 1. Upload the theme

**Option A — WP Admin (simplest):**
1. Zip the `elite-air-services-wp/` folder so the zip's top level is that single folder (i.e. `style.css` sits one level inside the zip, at `elite-air-services-wp/style.css` — not loose at the zip's root). A pre-built zip is at `copperbuilds/.tmp/elite-air-services-wp.zip`.
2. In wp-admin: Appearance → Themes → Add New → Upload Theme → choose the zip → Install → Activate.

**Option B — FTP/SFTP:**
1. Upload this whole folder to `wp-content/themes/elite-air-services-wp/` on the host.
2. In wp-admin: Appearance → Themes → activate "Elite Air Services".

## 2. Create the pages

Go to Pages → Add New and create exactly these 5 pages (slug must match — WordPress sets it from the title automatically, lowercased with dashes):

| Page title | Slug (auto from title) |
|---|---|
| Home | `home` (slug doesn't matter for this one — see step 4) |
| About | `about` |
| Services | `services` |
| Blog | `blog` (leave the content empty — see step 4, this becomes the Posts page, not a normal page you paste content into) |
| Contact | `contact` |

## 3. Paste in each page's content

For each page, open it in the block editor, click the three-dot menu (top right) → **Code editor**, delete anything there, and paste in the matching file from this theme's `content/` folder:

| Page | Paste from |
|---|---|
| Home | `content/front-page.html` |
| About | `content/about.html` |
| Services | `content/services.html` |
| Contact | `content/contact.html` |

Click the three-dot menu again → **Visual editor** to switch back, then **Update/Publish** the page. You should see real, distinct blocks (headings, paragraphs, images) you can click into and edit directly — that's the point of this rebuild.

**One thing you'll notice:** some blocks in the editor show as an empty-looking "Custom HTML" box with no preview, usually right before or after the blocks you can actually edit. Those are intentional structural markers (they open or close a styled wrapper `<div>` that the real content sits inside) — leave them alone. Don't delete one without deleting its matching pair, or the layout for that section will break. Everything you'd actually want to change — headlines, paragraphs, prices, team bios, FAQ answers, reviews — is a normal Heading/Paragraph/List block you can click straight into.

## 4. Set the homepage and permalinks

- Settings → Reading → "Your homepage displays" → Static Page → set Homepage to the "Home" page you created, and **Posts page to the "Blog" page you created**. This is what makes `/blog/` show the post archive instead of 404ing — the nav/footer "Blog" link depends on this being set, not just the page existing.
- Settings → Permalinks → select **"Post name"** → Save. Required — the theme's nav/footer links point to `/about/`, `/services/`, `/blog/`, `/contact/`, which 404 on the default "Plain" setting.
- Blog will show "No posts found" until an actual post is published — that's expected on a fresh install, not a bug.

## 5. Install an SEO plugin (RankMath or Yoast)

The theme no longer outputs its own title tag, meta description, canonical URL, Open Graph tags, or schema — that's now the SEO plugin's job, same as any real WordPress build.

1. Install RankMath (or Yoast SEO) from Plugins → Add New.
2. Run its setup wizard — enter the business as a Local Business, fill in NAP (name/address/phone), logo, and social profiles once; this drives the site-wide schema.
3. On each of the 4 pages, open the plugin's SEO box (bottom of the page editor, or a sidebar panel) and set the SEO title + meta description. Suggested titles/descriptions (from the original build) if you want a starting point:

| Page | Suggested SEO title | Suggested meta description |
|---|---|---|
| Home | AC Repair Tampa FL \| Elite Air Services Tampa \| HVAC Experts | Elite Air Services Tampa provides fast, reliable AC repair in Tampa FL. Licensed HVAC contractor serving Hillsborough County. Call (813) 555-0100 for same-day service. |
| About | About Elite Air Services Tampa \| Licensed HVAC Company Tampa FL | Elite Air Services Tampa is a licensed HVAC company serving Hillsborough County for 15+ years. Meet our team of certified technicians dedicated to honest, reliable AC service. |
| Services | Air Conditioning Installation Tampa FL \| HVAC Services \| Elite Air Services Tampa | Full HVAC services in Tampa FL — AC repair, air conditioning installation, heating, maintenance plans, and 24/7 emergency service. Licensed contractor. Free estimates. |
| Contact | Contact Elite Air Services Tampa \| Schedule HVAC Service Tampa FL | Contact Elite Air Services Tampa to schedule AC repair, HVAC installation, or maintenance. Call (813) 555-0100 or request a free estimate online. Serving Hillsborough County. |

4. For the FAQ schema (the accordion on Home, and the 4 FAQ cards on Services), use RankMath's FAQ block/schema block if you want that markup back — the original hardcoded JSON-LD for this was removed along with the rest of the custom SEO code.

## 6. Verify

- Visit the homepage — hero, stats bar, services grid, reviews, FAQ accordion, footer should all render, and the browser tab should show the real SEO title (not "My Blog" — if it still does, the SEO plugin isn't configured for that page yet).
- Click through Home → Services → About → Blog → Contact in the nav — confirm no 404s (Blog is allowed to show "No posts found").
- Click a service card on the homepage (e.g. "AC Repair") — should land on `/services/#ac-repair` and jump to that section.
- Check mobile width (375px) — sticky Call/Free Quote bar should appear at the bottom.
- Try editing a piece of text (a review, an FAQ answer, a price) directly in the block editor and confirm it updates on the live page.

## Known limitations (carried over from the original static mock, not new)

- The contact form and the homepage hero form (via the `[eas_hero_form]` / `[eas_contact_form]` shortcodes in `functions.php`) have no backend — they don't send email or store leads. If real lead capture is needed, install WPForms or Contact Form 7 and replace the shortcode in the page content with theirs.
- All content (phone number, address, reviews, pricing, team bios) is the placeholder demo content from the CopperBuilds portfolio mock — replace with the real business's actual details before this goes live for a real client.
- Google Fonts (Barlow, Barlow Condensed) load from Google's CDN — if the eventual host requires zero third-party requests, self-host them instead (see `functions.php` → `eas_enqueue_assets()`).
