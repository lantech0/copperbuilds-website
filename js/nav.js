(function () {
  var path = window.location.pathname;
  var page = path.split('/').pop() || '';

  function isActive(href) {
    if (href === '/') return page === '' || page === 'index.html';
    if (href === '/blog') return page === 'blog' || path.includes('/blog/');
    if (href === '/reports/') return path.includes('/reports/');
    return page === href.replace(/^\//, '');
  }

  function link(href, label) {
    var active = isActive(href);
    var style = active
      ? 'color:var(--accent);font-weight:600;text-decoration:none;font-size:.9375rem;letter-spacing:-.01em;'
      : 'color:var(--ink);text-decoration:none;font-size:.9375rem;letter-spacing:-.01em;transition:color .15s;';
    var aria = active ? ' aria-current="page"' : '';
    return '<a href="' + href + '" style="' + style + '"' + aria + '>' + label + '</a>';
  }

  var navHTML = '<nav id="main-nav" aria-label="Main navigation" style="position:sticky;top:0;z-index:50;height:64px;background:rgba(250,250,247,.92);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border-bottom:1px solid var(--rule);">'
    + '<div class="container" style="display:flex;align-items:center;justify-content:space-between;height:100%;">'
      + '<a href="/" aria-label="CopperBuilds — go to homepage" style="display:flex;align-items:center;text-decoration:none;flex-shrink:0;">'
        + '<img src="/brand_assets/logo.svg" alt="CopperBuilds" height="36" style="display:block;">'
      + '</a>'
      + '<div id="nav-links" style="display:flex;align-items:center;gap:2rem;">'
        + link('/services', 'Services')
        + link('/portfolio', 'Portfolio')
        + link('/pricing', 'Pricing')
        + link('/about', 'About')
        + link('/blog', 'Blog')
        + link('/reports/', 'Reports')
      + '</div>'
      + '<div style="display:flex;align-items:center;gap:.625rem;">'
        + '<a href="https://wa.me/639773293969" target="_blank" rel="noopener" aria-label="Message CopperBuilds on WhatsApp" style="display:flex;align-items:center;justify-content:center;width:40px;height:40px;border-radius:8px;border:1.5px solid var(--border);color:var(--warm-stone);text-decoration:none;transition:border-color .15s ease,background .15s ease,color .15s ease;flex-shrink:0;" onmouseover="this.style.borderColor=\'var(--accent-border)\';this.style.background=\'var(--accent-dim)\';this.style.color=\'var(--accent)\'" onmouseout="this.style.borderColor=\'var(--border)\';this.style.background=\'transparent\';this.style.color=\'var(--warm-stone)\'">'
          + '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 11.5a8.38 8.38 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.38 8.38 0 01-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.38 8.38 0 013.8-.9h.5a8.48 8.48 0 018 8v.5z"/></svg>'
        + '</a>'
        + '<a href="/contact" class="btn btn-primary" id="nav-cta" style="white-space:nowrap;">Get a Free Quote</a>'
        + '<button id="nav-toggle" aria-label="Open navigation menu" aria-expanded="false" aria-controls="mobile-menu" style="display:none;flex-direction:column;justify-content:center;align-items:center;gap:5px;width:40px;height:40px;background:none;border:none;cursor:pointer;padding:0;">'
          + '<span class="hb" style="display:block;width:22px;height:2px;background:var(--ink);border-radius:2px;transition:transform .25s,opacity .25s;"></span>'
          + '<span class="hb" style="display:block;width:22px;height:2px;background:var(--ink);border-radius:2px;transition:transform .25s,opacity .25s;"></span>'
          + '<span class="hb" style="display:block;width:22px;height:2px;background:var(--ink);border-radius:2px;transition:transform .25s,opacity .25s;"></span>'
        + '</button>'
      + '</div>'
    + '</div>'
    + '<div id="mobile-menu" style="display:none;flex-direction:column;gap:0;background:var(--bg);border-top:1px solid var(--rule);padding:1rem 0;">'
      + '<a href="/services" style="display:block;padding:.75rem 1.5rem;font-size:1rem;color:var(--ink);text-decoration:none;letter-spacing:-.01em;">Services</a>'
      + '<a href="/portfolio" style="display:block;padding:.75rem 1.5rem;font-size:1rem;color:var(--ink);text-decoration:none;letter-spacing:-.01em;">Portfolio</a>'
      + '<a href="/pricing" style="display:block;padding:.75rem 1.5rem;font-size:1rem;color:var(--ink);text-decoration:none;letter-spacing:-.01em;">Pricing</a>'
      + '<a href="/about" style="display:block;padding:.75rem 1.5rem;font-size:1rem;color:var(--ink);text-decoration:none;letter-spacing:-.01em;">About</a>'
      + '<a href="/blog" style="display:block;padding:.75rem 1.5rem;font-size:1rem;color:var(--ink);text-decoration:none;letter-spacing:-.01em;">Blog</a>'
      + '<a href="/reports/" style="display:block;padding:.75rem 1.5rem;font-size:1rem;color:var(--ink);text-decoration:none;letter-spacing:-.01em;">Reports</a>'
      + '<hr style="margin:.75rem 1.5rem;border:none;border-top:1px solid var(--rule);">'
      + '<a href="/contact" class="btn btn-primary" style="margin:.5rem 1.5rem 1rem;display:block;text-align:center;">Get a Free Quote</a>'
      + '<a href="https://wa.me/639773293969" target="_blank" rel="noopener" class="btn btn-ghost" style="margin:0 1.5rem 1rem;display:block;text-align:center;">Message Me on WhatsApp</a>'
    + '</div>'
  + '</nav>';

  var s = document.currentScript;
  s.insertAdjacentHTML('afterend', navHTML);

  // Hover states for non-active desktop links
  var nav = document.getElementById('main-nav');
  if (nav) {
    var links = nav.querySelectorAll('#nav-links a:not([aria-current])');
    links.forEach(function (a) {
      a.addEventListener('mouseenter', function () { a.style.color = 'var(--accent)'; });
      a.addEventListener('mouseleave', function () { a.style.color = 'var(--ink)'; });
    });
  }

  // Mobile toggle
  var toggle = document.getElementById('nav-toggle');
  var menu = document.getElementById('mobile-menu');
  if (toggle && menu) {
    var hbs = toggle.querySelectorAll('.hb');

    function openMenu() {
      menu.style.display = 'flex';
      toggle.setAttribute('aria-expanded', 'true');
      if (hbs[0]) hbs[0].style.transform = 'translateY(7px) rotate(45deg)';
      if (hbs[1]) hbs[1].style.opacity = '0';
      if (hbs[2]) hbs[2].style.transform = 'translateY(-7px) rotate(-45deg)';
    }

    function closeMenu() {
      menu.style.display = 'none';
      toggle.setAttribute('aria-expanded', 'false');
      if (hbs[0]) hbs[0].style.transform = '';
      if (hbs[1]) hbs[1].style.opacity = '';
      if (hbs[2]) hbs[2].style.transform = '';
    }

    toggle.addEventListener('click', function () {
      if (menu.style.display === 'flex') {
        closeMenu();
      } else {
        openMenu();
      }
    });

    menu.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', closeMenu);
    });
  }
})();
