# COPY-STANDARDS.md — Universal Copy Quality Standards

Read this before drafting ANY copy — Lantech website pages AND all client builds.
These are the floor. Client-specific voice and tone comes from that client's `BRAND-VOICE.md`.

---

## Three-Layer Copy Framework

Every page and post — Lantech site and client builds — is built in this exact order. Never reverse it.

| Layer | Name | Purpose | When to execute |
|---|---|---|---|
| **1** | **SEO Seed** | Establish what the page ranks for — target keyword cluster, search intent, page focus | Before writing anything |
| **2** | **Marketing Copy** | Make the copy convert — buyer psychology, AIDA/PAS structure, trade vocabulary, first-person CTAs | During drafting |
| **3** | **Grammar & Structure** | Make the copy clean and consistent — Vale gate (3A) + manual checklist (3B) | After drafting, before building HTML |

**Why this order is non-negotiable:**
- Grammar-polishing copy that doesn't rank is wasted effort — clean sentences no one finds
- Marketing layering on a keyword-free draft produces copy that converts but never gets discovered
- SEO-seeded copy that skips the grammar gate ships with "We" openers, passive voice, and weak CTAs that erode trust

**For client builds:** The SEO seed uses the client's keyword data. The marketing copy uses the client's `BRAND-VOICE.md`. The grammar gates (`COPY-STANDARDS.md`) apply to every build without exception.

---

## Readability Targets

| Target | Standard |
|---|---|
| Flesch-Kincaid Grade Level | 6–8 (local business audiences) |
| Sentence length | 14–18 words average. Hard ceiling: 25 words. Split anything over 25. No exceptions. |
| Paragraph length | 3 sentences max for body copy. Single-sentence paragraphs are fine — preferred on mobile. |
| Jargon | Explain it or cut it. Never assume the reader knows industry terms. |

---

## Layer 3A — Mechanical Gate (Vale catches these automatically)

Vale runs after every copy draft. These are the errors it flags. Do not let any of these survive into HTML.

| Rule | What Vale flags |
|---|---|
| Passive voice | Any sentence where the subject receives the action — target < 10% of sentences per page |
| Oxford comma | Missing serial comma in lists of three or more items |
| Weak CTAs | "Click Here", "Learn More", "Contact Us", "Submit", "Buy Now", "Sign Up", "Read More", "Get Started", "Find Out More" — all flag as warnings |
| Corporate jargon | "synergy", "leverage", "innovative solutions", "cutting-edge", "world-class", "best-in-class", "seamlessly", "holistic", "paradigm", "transformative", "empower" |
| Hedging language | "might", "could possibly", "in some cases", "it seems" — hedges destroy authority in marketing copy |
| Needless words | "very", "really", "quite", "rather", "somewhat" — weak intensifiers that add no meaning |
| Banned phrases | See `styles/Lantech/BannedPhrases.yml` for full list |
| Terminology | See `styles/Lantech/Substitutions.yml` — "Google My Business" → "Google Business Profile", etc. |
| Clichés | Proselint flags overused phrases |
| Corporate speak | Proselint flags formal organizational voice |

---

## Layer 3B — Judgment Gate (run this checklist manually before building HTML)

Go through every item. Do not rely on gut feel — check each one explicitly.

- [ ] **No "We" sentence openers** — sentences that start with "We" shift focus to the agency. Restructure to lead with the client, the outcome, or the problem. ("We helped them..." → "A simple review system took them...")
- [ ] **No dangling modifiers** — a phrase at the start of a sentence must modify the grammatical subject. ("As a licensed plumber, your pipes will be safe" is wrong — the pipes are not a licensed plumber.)
- [ ] **No ambiguous pronoun antecedents** — every "he", "she", "it", "they" must clearly refer to one specific noun. If it could mean two different things, rewrite it.
- [ ] **No incomplete comparisons** — "better", "faster", "cheaper" must be followed by "than [something]". "We do it better" = incomplete. "We respond faster than most contractors in your area" = complete.
- [ ] **AIDA structure check** — does the page or section move the reader through: Attention (headline grabs) → Interest (problem/context) → Desire (benefits + proof) → Action (CTA)? If a section drops the reader before Action, fix it.
- [ ] **Headline test (Ogilvy)** — does the headline do at least ONE of: promise a benefit, state a problem, deliver news, tell a story, or quote a customer? A purely clever or label-style headline fails this test.
- [ ] **Hero passes the 5-second test** — can a first-time visitor answer these three questions without scrolling: Who is this? What do they do? Who is it for? If any answer requires scrolling or thinking, the hero fails.
- [ ] **CTA specificity** — every CTA button says what happens when clicked. "Get My Free Estimate" passes. "Contact Us" fails. "Submit" fails. Test by reading the button in isolation with no surrounding context.
- [ ] **No accidental fragments in body paragraphs** — intentional fragments in headlines and bullets are fine. A fragment mid-paragraph that leaves the thought incomplete is an error.
- [ ] **Subject-verb agreement** — check sentences where a prepositional phrase separates subject from verb. "The quality of our services [is/are]..." — the subject is "quality" (singular), so "is" is correct.
- [ ] **Apostrophe audit** — scan for: its/it's confusion, possessive plurals, and contractions. These are the most-noticed errors by readers.
- [ ] **Sentence length scan** — split any sentence over 25 words. No exceptions. Average target: 14–18 words.
- [ ] **Awareness stage match (Schwartz)** — is the copy written for where the reader actually is? Cold traffic (unaware/problem-aware) needs a different entry point than warm traffic (solution-aware). Don't write for a reader who already knows they want your service when most visitors are arriving cold.

---

## Copywriting Frameworks

Use these to structure page sections and hero copy. Pick the framework that fits the reader's state.

### AIDA — for pages where the reader needs to be moved from cold to ready-to-call
- **A**ttention — headline that stops the scroll (problem, outcome, or bold claim)
- **I**nterest — context that makes the problem real and specific
- **D**esire — proof + benefits that make the solution feel inevitable
- **A**ction — one clear CTA with no competing options

### PAS — for service pages and email where the pain is high-stakes
- **P**roblem — name the specific pain the reader already feels
- **A**gitate — make the stakes real (what happens if this isn't fixed?)
- **S**olve — present the service as the resolution

### BAB — for before/after sections, testimonials, and case studies
- **B**efore — where the reader is now (uncomfortable, costly, uncertain)
- **A**fter — where they want to be (resolved, saved money, confident)
- **B**ridge — how the service gets them from Before to After

---

## Headline Rules (Ogilvy)

- 5× more people read headlines than body copy. The headline earns the next line — nothing else.
- **Optimal length:** 6–10 words. Hard ceiling: 15 words.
- **Must do at least one of:**
  - Promise a specific benefit ("Get More Calls From Google Maps")
  - State a problem the reader recognizes ("Your Website Is Losing You Calls")
  - Deliver news ("Google Maps Rankings Changed in 2026")
  - Ask a question the reader is already asking ("Why Is My Competitor Ranking Above Me?")
  - Make a bold, specific claim ("47 Reviews in 90 Days — Here's How")
- **Never:** purely clever wordplay with no substance, label-style headings ("Our Services"), vague superlatives ("The Best Website Agency")
- **Specificity wins:** "Rank in the Local 3-Pack in 90 Days" beats "Improve Your Local SEO"

---

## CTA Rules

- **First-person possessive outperforms generic:** "Get My Free Quote" > "Get a Free Quote"
- **Action + outcome:** the button must name what happens. "Book a Same-Day Visit" names the action AND the outcome. "Contact Us" names neither.
- **One primary CTA per page.** Two competing CTAs above the fold = no action taken.
- **CTA must stand alone:** read the button text with no surrounding page copy. Does it still make sense? If not, rewrite it.
- **Never use:** Submit, Click Here, Learn More (unmodified), Contact Us, Buy Now, Get Started (unmodified), Read More, Find Out More
- **Strong CTA formula:** [Verb] + [My/Your] + [Specific Outcome] — "Start My Free Estimate", "Get My Free Roof Inspection", "Book My Same-Day Visit"

---

## Power Words by Category

Use one to two per sentence maximum — more than that and they lose all force.

| Category | Words |
|---|---|
| **Trust** | Guaranteed, Proven, Certified, Licensed, Verified, Accredited |
| **Speed** | Same-day, Instant, Fast, 90-minute, Today, Now |
| **Safety** | Protected, Secure, Worry-free, Safe, Peace of mind |
| **Ease** | Simple, Hassle-free, Done-for-you, Straightforward |
| **Urgency** | Today, Limited, Before, Expires, Now |
| **Value** | Free, Save, No obligation, Included, At no cost |

---

## What Not to Do

- **Never write vague comparative claims.** "We do it better" violates FTC guidelines and erodes trust. Prove it or cut it.
- **Never use jargon without explaining it.** Core Web Vitals, schema markup, CTR — either explain in plain English or cut.
- **Never stack adjectives.** "Professional, affordable, fast website design" means nothing. Pick one and prove it.
- **Never open with the company name.** The reader doesn't care about the company yet. Open with the reader's problem or outcome.
- **Never use passive voice in CTAs.** "A Quote Can Be Requested" → "Get My Free Quote."
- **Never write for yourself.** Every sentence should pass this test: "Does this serve the reader, or does it make us feel good about ourselves?" If the latter, cut it.
