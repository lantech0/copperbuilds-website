(function () {
  var footerHTML = '<footer style="background:var(--bg);border-top:1px solid var(--rule);padding:3.5rem 0 2rem" role="contentinfo">'
    + '<div class="container">'
      + '<div class="footer-grid" style="display:grid;grid-template-columns:1.6fr 1fr 1fr 1fr;gap:3rem;margin-bottom:3rem">'

        + '<div>'
          + '<a href="/" aria-label="CopperBuilds homepage" style="display:inline-block;margin-bottom:1rem">'
            + '<img src="/brand_assets/logo.svg" alt="CopperBuilds" height="36" style="display:block">'
          + '</a>'
          + '<p style="color:var(--warm-stone);font-size:0.875rem;line-height:1.72;max-width:260px;margin-bottom:1.25rem">Websites and local SEO for home services pros across the USA. Built for small businesses. Not enterprise.</p>'
          + '<div style="display:flex;gap:0.625rem">'
            + '<a href="https://www.facebook.com/CopperBuilds/" aria-label="CopperBuilds on Facebook" target="_blank" rel="noopener" style="display:flex;align-items:center;justify-content:center;width:36px;height:36px;border-radius:8px;border:1.5px solid var(--border);color:var(--warm-stone);text-decoration:none;transition:border-color 0.15s ease,background 0.15s ease,color 0.15s ease" onmouseover="this.style.borderColor=\'var(--accent-border)\';this.style.background=\'var(--accent-dim)\';this.style.color=\'var(--accent)\'" onmouseout="this.style.borderColor=\'var(--border)\';this.style.background=\'transparent\';this.style.color=\'var(--warm-stone)\'">'
              + '<svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"/></svg>'
            + '</a>'
            + '<a href="https://www.linkedin.com/in/luisecharri/" aria-label="CopperBuilds on LinkedIn" target="_blank" rel="noopener" style="display:flex;align-items:center;justify-content:center;width:36px;height:36px;border-radius:8px;border:1.5px solid var(--border);color:var(--warm-stone);text-decoration:none;transition:border-color 0.15s ease,background 0.15s ease,color 0.15s ease" onmouseover="this.style.borderColor=\'var(--accent-border)\';this.style.background=\'var(--accent-dim)\';this.style.color=\'var(--accent)\'" onmouseout="this.style.borderColor=\'var(--border)\';this.style.background=\'transparent\';this.style.color=\'var(--warm-stone)\'">'
              + '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="4"/><line x1="8" y1="11" x2="8" y2="16"/><circle cx="8" cy="8" r="1" fill="currentColor" stroke="none"/><path d="M12 11v5"/><path d="M12 11a3 3 0 016 0v5"/></svg>'
            + '</a>'
          + '</div>'
        + '</div>'

        + '<div>'
          + '<h3 style="font-size:0.8125rem;font-weight:700;color:var(--ink);margin-bottom:1rem;letter-spacing:0.04em;text-transform:uppercase">Services</h3>'
          + '<nav aria-label="Services footer links" style="display:flex;flex-direction:column;gap:0.625rem">'
            + footerLink('/services', 'Web Design')
            + footerLink('/services', 'Local SEO')
            + footerLink('/services', 'Google Business')
            + footerLink('/services', 'Social Media')
            + footerLink('/pricing', 'Pricing')
          + '</nav>'
        + '</div>'

        + '<div>'
          + '<h3 style="font-size:0.8125rem;font-weight:700;color:var(--ink);margin-bottom:1rem;letter-spacing:0.04em;text-transform:uppercase">Company</h3>'
          + '<nav aria-label="Company footer links" style="display:flex;flex-direction:column;gap:0.625rem">'
            + footerLink('/about', 'About')
            + footerLink('/how-we-work', 'How We Work')
            + footerLink('/portfolio', 'Portfolio')
            + footerLink('/blog', 'Blog')
            + footerLink('/reports/', 'Reports')
            + footerLink('/help', 'Help Center')
            + footerLink('/contact', 'Contact')
          + '</nav>'
        + '</div>'

        + '<div>'
          + '<h3 style="font-size:0.8125rem;font-weight:700;color:var(--ink);margin-bottom:1rem;letter-spacing:0.04em;text-transform:uppercase">Get Started</h3>'
          + '<p style="color:var(--warm-stone);font-size:0.875rem;line-height:1.65;margin-bottom:1rem">Ready to get your business online?</p>'
          + '<a href="/contact" class="btn btn-primary" style="font-size:0.875rem;padding:0.6875rem 1.25rem">Free Quote</a>'
          + '<p style="margin-top:0.875rem">' + footerLink('mailto:luis.copperbuilds@gmail.com', 'luis.copperbuilds@gmail.com', true) + '</p>'
          + '<p style="margin-top:0.375rem">' + footerLink('https://wa.me/639773293969', 'Message on WhatsApp', true) + '</p>'
        + '</div>'

      + '</div>'
      + '<hr class="rule">'
      + '<div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;padding-top:1.5rem">'
        + '<p style="color:var(--subtle);font-size:0.8125rem">&copy; 2026 CopperBuilds. All rights reserved.</p>'
        + '<div style="display:flex;gap:1.25rem;align-items:center;flex-wrap:wrap">'
          + '<p style="color:var(--subtle);font-size:0.8125rem;margin:0">Built for small businesses. Not enterprise.</p>'
          + footerLink('/privacy', 'Privacy Policy', true)
          + footerLink('/terms', 'Terms of Service', true)
        + '</div>'
      + '</div>'
    + '</div>'
  + '</footer>';

  function footerLink(href, label, subtle) {
    var color = subtle ? 'var(--subtle)' : 'var(--warm-stone)';
    var size = subtle ? '0.8125rem' : '0.875rem';
    return '<a href="' + href + '" style="color:' + color + ';font-size:' + size + ';text-decoration:none;transition:color 0.15s ease" onmouseover="this.style.color=\'var(--ink)\'" onmouseout="this.style.color=\'' + color + '\'">' + label + '</a>';
  }

  var s = document.currentScript;
  s.insertAdjacentHTML('afterend', footerHTML);
})();
