<?php
/**
 * Fallback template (required by WordPress for every theme).
 * This site's real pages are rendered by front-page.php, page-about.php,
 * page-services.php, and page-contact.php. This file only renders if a
 * URL doesn't match any of those (e.g. an unexpected archive or 404).
 */
get_header();
?>

<div class="page-hero">
	<h1><?php is_404() ? _e( 'Page Not Found' ) : the_title(); ?></h1>
</div>

<section>
	<div class="section-inner">
		<?php if ( have_posts() ) : ?>
			<?php while ( have_posts() ) : the_post(); ?>
				<h2 class="section-title"><?php the_title(); ?></h2>
				<div><?php the_content(); ?></div>
			<?php endwhile; ?>
		<?php else : ?>
			<p>Sorry, that page couldn't be found. <a href="<?php echo esc_url( home_url( '/' ) ); ?>">Return home</a>.</p>
		<?php endif; ?>
	</div>
</section>

<?php get_footer(); ?>
