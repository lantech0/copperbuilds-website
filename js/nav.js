(function () {
  var path = window.location.pathname;
  var page = path.split('/').pop() || 'index.html';

  function isActive(href) {
    if (href === '/index.html') return page === 'index.html' || page === '';
    if (href === '/blog.html') return page === 'blog.html' || path.includes('/blog/');
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
      + '<a href="/index.html" aria-label="CopperBuilds — go to homepage" style="display:flex;align-items:center;text-decoration:none;flex-shrink:0;">'
        + '<img src="/brand_assets/logo.svg" alt="CopperBuilds" height="36" style="display:block;">'
      + '</a>'
      + '<div id="nav-links" style="display:flex;align-items:center;gap:2rem;">'
        + link('/services.html', 'Services')
        + link('/portfolio.html', 'Portfolio')
        + link('/pricing.html', 'Pricing')
        + link('/about.html', 'About')
        + link('/blog.html', 'Blog')
      + '</div>'
      + '<div style="display:flex;align-items:center;gap:1rem;">'
        + '<a href="/contact.html" class="btn btn-primary" id="nav-cta" style="white-space:nowrap;">Get a Free Quote</a>'
        + '<button id="nav-toggle" aria-label="Open navigation menu" aria-expanded="false" aria-controls="mobile-menu" style="display:none;flex-direction:column;justify-content:center;align-items:center;gap:5px;width:40px;height:40px;background:none;border:none;cursor:pointer;padding:0;">'
          + '<span class="hb" style="display:block;width:22px;height:2px;background:var(--ink);border-radius:2px;transition:transform .25s,opacity .25s;"></span>'
          + '<span class="hb" style="display:block;width:22px;height:2px;background:var(--ink);border-radius:2px;transition:transform .25s,opacity .25s;"></span>'
          + '<span class="hb" style="display:block;width:22px;height:2px;background:var(--ink);border-radius:2px;transition:transform .25s,opacity .25s;"></span>'
        + '</button>'
      + '</div>'
    + '</div>'
    + '<div id="mobile-menu" style="display:none;flex-direction:column;gap:0;background:var(--bg);border-top:1px solid var(--rule);padding:1rem 0;">'
      + '<a href="/services.html" style="display:block;padding:.75rem 1.5rem;font-size:1rem;color:var(--ink);text-decoration:none;letter-spacing:-.01em;">Services</a>'
      + '<a href="/portfolio.html" style="display:block;padding:.75rem 1.5rem;font-size:1rem;color:var(--ink);text-decoration:none;letter-spacing:-.01em;">Portfolio</a>'
      + '<a href="/pricing.html" style="display:block;padding:.75rem 1.5rem;font-size:1rem;color:var(--ink);text-decoration:none;letter-spacing:-.01em;">Pricing</a>'
      + '<a href="/about.html" style="display:block;padding:.75rem 1.5rem;font-size:1rem;color:var(--ink);text-decoration:none;letter-spacing:-.01em;">About</a>'
      + '<a href="/blog.html" style="display:block;padding:.75rem 1.5rem;font-size:1rem;color:var(--ink);text-decoration:none;letter-spacing:-.01em;">Blog</a>'
      + '<hr style="margin:.75rem 1.5rem;border:none;border-top:1px solid var(--rule);">'
      + '<a href="/contact.html" class="btn btn-primary" style="margin:.5rem 1.5rem 1rem;display:block;text-align:center;">Get a Free Quote</a>'
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
