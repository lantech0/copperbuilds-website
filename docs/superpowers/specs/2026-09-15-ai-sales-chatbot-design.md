# Design Spec — AI Sales-Qualifier Chatbot
**Date:** 2026-09-15
**Status:** Approved — build deferred (see Trigger to Resume)

---

## Goal

Embed an AI chat widget on copperbuilds.com that qualifies inbound visitors as sales leads and, for conversations that clear a qualification bar, books a discovery call directly — engineered from day one so the same engine can later be reskinned and resold to home-services trades clients as a customer-facing lead-gen chatbot on their own websites.

## Scope

CopperBuilds-exclusive for this build. Explicitly **not** integrated with or overlapping the separate LuisGHL trades-automation product line — that relationship was flagged during brainstorming and deliberately left out of scope for this design.

## Architecture / Data Flow

1. **Widget** — a small vanilla JS chat bubble embedded via `<script>` tag on copperbuilds.com, loaded async.
2. **Backend** — a new Cloudflare Worker (e.g. `/api/chat`). No separate server; this is the only backend component. Does not currently exist in the repo (confirmed — no `wrangler.toml` or Worker present as of this design).
3. **Conversation state** — Workers KV or D1, keyed by a session UUID generated client-side, so the bot has memory mid-conversation.
4. **Model routing** — the Worker calls Claude **through Cloudflare AI Gateway**, not the Anthropic API directly. The Gateway provides edge caching of the static system prompt, sliding-window rate limiting, and a hard monthly spend cap, at no added cost.
5. **Conversation design** — qualifies in order **Need → Timeline → Budget → Authority**; prefers quick-reply buttons over open text wherever possible; avoids sending 3+ unprompted bot messages before the visitor's first reply.
6. **Outcome (tiered, not binary):**
   - **Qualified** (real need, plausible timeline, right business type) → bot offers a **Calendly inline embed** widget directly in the chat; visitor books without leaving the conversation.
   - **Lower intent** → **capture-and-notify** fallback — same job the current Web3Forms contact form already does (email/Slack notification to the user), not a replacement for it.
7. **Lead visibility** — no dashboard for v1. Notification-only. All conversation/lead data is still stored in D1 regardless, so a dashboard can be added later as a small bounded task without any rework or data loss.

## Sales Behavior / Guardrails

**Active seller within guardrails** (explicit choice over "FAQ-only" and "fully autonomous closer"):
- Can quote official pricing/packages, grounded in `PRODUCT.md`, `pricing.html`, `services.html`, `POSITIONING-BRIEF.md`, `BRAND-VOICE.md`.
- Uses the existing objection-handling/value-framing talk track in `clients/templates/07-discovery-call-script.md` for persuasion.
- Pushes qualified conversations toward booking.
- **Cannot** negotiate discounts, promise custom terms, or state anything not backed by these source documents.

## Reusability for Trades-Client Resale

The Worker, system-prompt template, and KV/D1 schema are designed as **tenant-configuration-driven** from day one — business name, industry, tone, qualifying-question set, and notification target are data (a config record), not hardcoded Worker logic — even though only CopperBuilds' own configuration is populated in this build. This is what makes adding a future trades client a config change instead of a code fork/rewrite.

## Build vs. Buy

Custom build on infrastructure CopperBuilds already owns (Cloudflare + Anthropic), rejected in favor of third-party platforms (Chatbase, Intercom Fin, etc.) specifically because of the resale intent — renting a third-party platform would make the eventual resale product dependent on that vendor's pricing, branding limits, and continued existence.

## Cost & Abuse Control

Layered defense: input sanitization, sliding-window rate limiting (AI Gateway), a zero-trust system prompt (treats all conversation content as untrusted data, never as instructions), output length caps, and a hard monthly spend cap (AI Gateway). At expected traffic (dozens of sessions/month), Cloudflare components (Workers, KV/D1, AI Gateway) stay within free tiers; total cost is expected to land in the **tens of dollars/month**, driven almost entirely by Anthropic API usage, with prompt-caching the static system prompt cutting input cost roughly 10x.

## Research Basis

Full evidence-backed research report (23 sources, 82 claims, validated): `C:\Users\User\Documents\CopperBuilds_AI_Chatbot_Research_20260915\report.md`

## Open Items for a Future Session

- Whether/when to add a leads dashboard (deferred, not rejected — D1 data supports adding it later).
- Whether to revisit Calendly inline embed vs. a lighter link-drop once real usage patterns are known.
- Whether/how this later relates to the LuisGHL trades-automation line (explicitly out of scope here).

## Trigger to Resume

Do not start implementation until the user explicitly reopens this. Stated condition: build after copperbuilds.com is fully optimized and already seeing organic visitor traffic — this design is approved but intentionally not being executed now.
