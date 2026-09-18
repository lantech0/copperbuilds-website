<!DOCTYPE html>
<html lang="en" <?php language_attributes(); ?>>
<head>
<meta charset="<?php bloginfo( 'charset' ); ?>">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>

<!-- EMERGENCY BAR -->
<div class="emergency-bar" role="banner">
  Pipe burst? Flooding? We respond in 60 minutes or less.
  <a href="tel:8135550194">Call (813) 555-0194 now</a>
</div>

<!-- NAV -->
<nav aria-label="Main navigation">
  <div class="nav-inner">
    <a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="logo" aria-label="Priority Plumbing &amp; Drain — home">
      <div class="logo-icon" aria-hidden="true">
        <svg viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M8 4.5C8 3.12 9.12 2 10.5 2C11.88 2 13 3.12 13 4.5V5H15V7H13V9H15.5C16.33 9 17 9.67 17 10.5V16C17 17.1 16.1 18 15 18H7C5.9 18 5 17.1 5 16V10.5C5 9.67 5.67 9 6.5 9H9V7H8V4.5Z" fill="white" opacity="0.9"/>
          <rect x="9" y="11" width="4" height="5" rx="1" fill="rgba(255,255,255,0.4)"/>
        </svg>
      </div>
      <div class="logo-text">
        <div class="name">Priority Plumbing</div>
        <div class="sub">&amp; Drain &middot; Tampa, FL</div>
      </div>
    </a>
    <button class="nav-toggle" aria-label="Open navigation" aria-expanded="false" onclick="const ul=this.nextElementSibling;const open=ul.style.display==='flex';ul.style.display=open?'none':'flex';ul.style.flexDirection='column';ul.style.position='absolute';ul.style.top='68px';ul.style.left='0';ul.style.right='0';ul.style.background='var(--navy)';ul.style.padding='12px 20px 20px';this.setAttribute('aria-expanded',!open)">&#9776;</button>
    <ul class="nav-links">
      <li><a href="<?php echo esc_url( home_url( '/' ) ); ?>"<?php echo is_front_page() ? ' aria-current="page"' : ''; ?>>Home</a></li>
      <li><a href="<?php echo esc_url( home_url( '/services/' ) ); ?>"<?php echo is_page( 'services' ) ? ' aria-current="page"' : ''; ?>>Services</a></li>
      <li><a href="<?php echo esc_url( home_url( '/about/' ) ); ?>"<?php echo is_page( 'about' ) ? ' aria-current="page"' : ''; ?>>About</a></li>
      <li><a href="<?php echo esc_url( home_url( '/blog/' ) ); ?>"<?php echo is_page( 'blog' ) ? ' aria-current="page"' : ''; ?>>Blog</a></li>
      <li><a href="<?php echo esc_url( home_url( '/contact/' ) ); ?>"<?php echo is_page( 'contact' ) ? ' aria-current="page"' : ''; ?>>Contact</a></li>
    </ul>
    <a href="tel:8135550194" class="nav-phone" aria-label="Call Priority Plumbing">
      <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true"><path d="M3.65 2h2.5l1 3-1.5 1.5c.7 1.4 1.85 2.55 3.25 3.25L10.4 8.3l3 1v2.5C13.4 13 12.3 14 11 14 5.95 14 2 10.05 2 5 2 3.7 3 2.6 3.65 2Z" stroke="white" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
      (813) 555-0194
    </a>
  </div>
</nav>
