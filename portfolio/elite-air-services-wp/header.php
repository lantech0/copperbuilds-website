<!DOCTYPE html>
<html lang="en" <?php language_attributes(); ?>>
<head>
<meta charset="<?php bloginfo( 'charset' ); ?>">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>

<!-- TOP BAR -->
<div class="topbar">
  <a href="tel:8135550100">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 12 19.79 19.79 0 0 1 1.62 3.52a2 2 0 0 1 1.995-2.18h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 8.96a16 16 0 0 0 6.13 6.13l.98-.98a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
    (813) 555-0100
  </a>
  <a href="mailto:service@eliteairservicestampa.com">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
    service@eliteairservicestampa.com
  </a>
</div>

<!-- NAV -->
<nav>
  <div class="nav-inner">
    <a href="<?php echo esc_url( home_url( '/' ) ); ?>" class="logo">
      <div class="logo-icon">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#F07820" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12h20M12 2v20M4.93 4.93l14.14 14.14M19.07 4.93 4.93 19.07"/><circle cx="12" cy="12" r="2" fill="#F07820" stroke="none"/></svg>
      </div>
      <div class="logo-text">
        <div class="logo-name">Elite Air Services</div>
        <div class="logo-sub">Tampa, FL</div>
      </div>
    </a>
    <ul class="nav-links">
      <li><a href="<?php echo esc_url( home_url( '/' ) ); ?>"<?php echo is_front_page() ? ' aria-current="page"' : ''; ?>>Home</a></li>
      <li><a href="<?php echo esc_url( home_url( '/services/' ) ); ?>"<?php echo is_page( 'services' ) ? ' aria-current="page"' : ''; ?>>Services</a></li>
      <li><a href="<?php echo esc_url( home_url( '/about/' ) ); ?>"<?php echo is_page( 'about' ) ? ' aria-current="page"' : ''; ?>>About</a></li>
      <li><a href="<?php echo esc_url( home_url( '/contact/' ) ); ?>" class="nav-cta">Get a Free Quote</a></li>
    </ul>
  </div>
</nav>
