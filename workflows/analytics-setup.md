# Workflow: Analytics & Search Console Setup

**Triggered by:** `workflows/deploy.md` Step 4 — run immediately after the live site smoke test passes
**Reference for:** `workflows/monthly-report.md` — all reporting depends on data collected here

---

## Objective

Set up Google Analytics 4 and Google Search Console for the client's live site, install tracking, configure conversions, link both tools together, and grant the right access to both CopperBuilds and the client.

---

## Trigger

Run this workflow once per client, immediately after the live site smoke test passes in `deploy.md`. Do not defer it — every day without tracking is data lost forever.

---

## Required Inputs

- Client's live domain (e.g., `https://joesplumbing.com`)
- Client's Google account email (collected in `02-onboarding-questionnaire.md`)
- CopperBuilds' agency Google account: `luis.copperbuilds@gmail.com`
- Access to the live site files (to add tracking code)
- Hostinger FTP/File Manager access (to re-upload files after adding the tag)

---

## Part A — Google Analytics 4

### Step A1 — Create the GA4 Property

1. Go to [analytics.google.com](https://analytics.google.com) — sign in with `luis.copperbuilds@gmail.com`
2. Click **Admin** (bottom-left gear icon)
3. In the Account column: click **Create Account** if this is the first client, or select the existing CopperBuilds account
   - Account name: `Lantech Agency`
4. In the Property column: click **Create Property**
   - Property name: `[Business Name]`
   - Reporting time zone: match the client's city (e.g., `United States — Eastern Time`)
   - Currency: `US Dollar (USD)`
   - Click **Next** → select business category → click **Create**
5. In the platform prompt: click **Web**
   - Website URL: `https://[clientdomain].com`
   - Stream name: `[Business Name] Website`
   - Click **Create stream**
6. Copy the **Measurement ID** — format: `G-XXXXXXXXXX`
   - Save it to `clients/active/[slug]/LAUNCH-SUMMARY.md` under `GA4 ID:`

---

### Step A2 — Install the GA4 Tag on the Site

Add this snippet to the `<head>` of **every HTML page** on the site, immediately after the opening `<head>` tag:

```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

Replace `G-XXXXXXXXXX` with the actual Measurement ID from Step A1.

For a CopperBuilds-built site with 4–6 pages: add the snippet manually to each HTML file. It takes 2 minutes per page.

After adding: re-upload the updated files to Hostinger via File Manager or FTP.

**Verify installation:**
- Open the live site in Chrome
- Open DevTools (F12) → Network tab → reload the page
- Filter by `gtag` — you should see a request to `googletagmanager.com`
- OR: in GA4 → Reports → Realtime → open your own browser to the live site — you should appear as an active user within 30 seconds

---

### Step A3 — Set Up Contact Form Conversion

The most valuable conversion for a local service business is a contact form submission or a phone call. Set up at least one.

**Option A — Thank-You Page (recommended for Formspree or native forms):**
1. Create a simple `thank-you.html` page on the site (just a "Thanks, we'll be in touch!" message)
2. Configure the contact form to redirect to `/thank-you.html` after submission
3. In GA4 → Admin → Events → **Create event**
   - Event name: `generate_lead`
   - Matching condition: `page_location` contains `thank-you`
4. Mark it as a conversion: Admin → Conversions → toggle `generate_lead` ON

**Option B — GA4 Enhanced Measurement (basic, no code):**
GA4 automatically tracks outbound clicks, scrolls, and file downloads. For phone number clicks:
- Admin → Data Streams → select the web stream → Enhanced measurement → toggle ON
- Outbound clicks to `tel:` links will be tracked automatically as `click` events

---

### Step A4 — Grant GA4 Access

Give the client viewer access so they can check their own data:

1. GA4 → Admin → Account → **Account Access Management**
2. Click **+** → Add users
3. Enter client's Google email from the questionnaire
4. Role: **Viewer**
5. Click **Add**

CopperBuilds (`luis.copperbuilds@gmail.com`) should already be Admin as the property creator. Confirm this is the case.

---

## Part B — Google Search Console

### Step B1 — Create the GSC Property

1. Go to [search.google.com/search-console](https://search.google.com/search-console) — sign in with `luis.copperbuilds@gmail.com`
2. Click **Add property**
3. Choose **URL prefix** (not Domain — URL prefix is simpler for static sites)
4. Enter: `https://[clientdomain].com` (include the https://, no trailing slash)
5. Click **Continue** — you'll be taken to the verification screen

---

### Step B2 — Verify Ownership

Use the **HTML tag method** — it's the fastest for sites you control:

1. GSC will show you a `<meta>` tag like this:
   ```html
   <meta name="google-site-verification" content="XXXXXXXXXXXXXXXXXXX" />
   ```
2. Add this tag to the `<head>` of `index.html` only (verification only needs the homepage)
3. Re-upload `index.html` to Hostinger
4. Back in GSC, click **Verify**
5. Confirmation: "Ownership verified" — GSC is now active

**Alternative — DNS TXT record (if HTML tag method fails):**
1. Copy the TXT record value from GSC (format: `google-site-verification=XXXXXXX`)
2. Log in to Hostinger hPanel → **Domains** → **DNS / Nameservers**
3. Add a new TXT record:
   - Type: `TXT`
   - Name: `@`
   - Value: paste the verification string
   - TTL: 3600
4. Wait 5–15 minutes → return to GSC → click Verify

---

### Step B3 — Submit the Sitemap

1. In GSC left sidebar: **Sitemaps**
2. In the "Add a new sitemap" field: enter `sitemap.xml`
3. Click **Submit**
4. Status should show "Success" within a few minutes
   - If it shows "Couldn't fetch": verify `https://[domain]/sitemap.xml` loads in the browser first

---

### Step B4 — Request Indexing for Key Pages

Don't wait for Google to crawl — request indexing manually for the most important pages:

1. GSC → **URL Inspection** (top search bar)
2. Enter the homepage URL → press Enter → click **Request indexing**
3. Repeat for: Services page, Contact page, and any location-specific landing page
4. Limit: ~10 requests per day — prioritize the pages most likely to drive conversions

---

### Step B5 — Link GSC to GA4

Linking lets you see organic search queries directly inside GA4 reports:

1. In GA4 → Admin → Property column → **Search Console Linking**
2. Click **Link** → **Choose accounts** → select the GSC property you just created
3. Select the GA4 web data stream → click **Next** → **Submit**
4. Confirm: in GA4 → Reports → Acquisition → Search Console → Organic Search queries tab should appear (data populates within 24–48 hours)

---

### Step B6 — Grant GSC Access

Give the client access to their own Search Console data:

1. GSC → **Settings** (bottom-left) → **Users and permissions**
2. Click **Add user**
3. Enter client's Google email
4. Permission level: **Full** (lets them see all data but not remove the property)
5. Click **Add**

---

## Part C — Save & Handover

### Step C1 — Log Everything

Add to `clients/active/[slug]/LAUNCH-SUMMARY.md`:

```
GA4 Property: [Property name]
GA4 Measurement ID: G-XXXXXXXXXX
GA4 Conversion: generate_lead (thank-you page) / outbound clicks (enhanced)
GSC Property: https://[domain]/
GSC Verification method: HTML tag / DNS TXT
Sitemap submitted: https://[domain]/sitemap.xml
GSC linked to GA4: yes
Client access granted: GA4 Viewer + GSC Full — [client email]
```

### Step C2 — Update the Handover Package

In `clients/templates/05-handover-package.md`, confirm these fields are filled:
- GA4 Measurement ID
- GSC property URL
- Note that both tools need ~48–72 hours before data appears

---

## Part D — GBP Instant Verification via GSC

**When to run:** Immediately after GSC ownership is verified (Part B, Step B2). If the same Google Account owns both the GSC property and the GBP listing, Google can verify the GBP in seconds — no postcard, no phone call, no DNS record.

### Why This Works

Google trusts the GSC ownership signal. If `luis.copperbuilds@gmail.com` is a verified GSC owner for `https://[clientdomain].com` and the same account manages the GBP listing, Google confirms the business controls the domain and approves GBP verification instantly.

**Prerequisite:** The GBP listing must be claimed and managed under the same Google Account used for GSC (`luis.copperbuilds@gmail.com` for CopperBuilds-managed clients). If the client manages their own GBP under a different account, this method doesn't apply — use postcard or phone verification instead.

### Steps

1. **Verify the domain in GSC first** (Part B, Steps B1–B2) — GSC ownership must be confirmed before GBP will accept it as a verification signal
2. **Open GBP** — go to [business.google.com](https://business.google.com), sign in with `luis.copperbuilds@gmail.com`
3. **Start the verification flow** for the listing → when prompted for a verification method, look for **"Google Search Console"** or **"Instant Verification"** as an option
   - This option only appears if: (a) you're signed in with the same Google Account that owns the GSC property, and (b) the website URL on the GBP listing matches the verified GSC property exactly
4. **Select it** — Google cross-checks the GSC ownership record and approves verification immediately (no waiting period)
5. **Confirm** — the GBP listing status changes to "Verified" within seconds. Screenshot the verified state and note it in `LAUNCH-SUMMARY.md`

### If the Instant Verification Option Doesn't Appear

Check these in order:
- GBP listing URL and GSC property URL must match exactly (both `https://`, consistent trailing slash)
- Both must be the same Google Account — not two accounts associated with the same business
- The GSC property must be a URL-prefix property, not a Domain property — Domain-type properties don't trigger the instant verification signal in GBP
- If all checks pass and the option still doesn't appear: fall back to phone or postcard verification

### Log It

Add to `LAUNCH-SUMMARY.md`:
```
GBP verification method: GSC instant verification (same Google Account)
GBP verified: yes — [date]
```

---

## Required Outputs Before Considering Analytics Setup Done

- [ ] GA4 property created — Measurement ID saved to `LAUNCH-SUMMARY.md`
- [ ] GA4 tag installed on every page — verified via Realtime report or DevTools
- [ ] At least one conversion configured (thank-you page or enhanced measurement)
- [ ] Client granted GA4 Viewer access
- [ ] GSC property created — ownership verified
- [ ] Sitemap submitted — status shows "Success"
- [ ] Indexing requested for homepage + key pages
- [ ] GSC linked to GA4
- [ ] Client granted GSC Full access
- [ ] `LAUNCH-SUMMARY.md` updated with all IDs and access details
- [ ] Handover package updated

---

## Edge Cases

**Client doesn't have a Google account:**
Ask them to create one before launch: *"You'll need a Google account (Gmail works) so I can give you access to your analytics and search console. Takes 2 minutes at accounts.google.com — just send me the email when it's ready."* Do not skip access setup — they paid for this transparency.

**Client already has an existing GA4 / GSC property:**
Ask for admin access to their existing account. Add CopperBuilds as an Editor. Do not create a new property that duplicates their old data. Preserve history.

**Sitemap submission shows "Couldn't fetch":**
- Confirm `https://[domain]/sitemap.xml` loads in the browser
- Check that the file is in `public_html/` root, not a subfolder
- Check `robots.txt` isn't blocking the sitemap path
- Wait 24 hours and retry if everything looks correct

**GA4 Realtime shows no data after installing tag:**
- Double-check the Measurement ID in the code matches the property (copy-paste error is common)
- Confirm the tag is in `<head>` of the live version, not just local
- Disable any ad-blockers or browser extensions for the test
- Try Chrome Incognito mode

**GSC ownership verification fails with HTML tag method:**
Use the DNS TXT record method (Step B2 alternative). If that also fails, check that the domain's DNS is pointing to Hostinger correctly — a mis-pointed domain means the live site isn't actually at that domain yet.
