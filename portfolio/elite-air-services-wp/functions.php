<?php
/**
 * Elite Air Services theme functions.
 *
 * SEO (title tag, meta description, canonical, Open Graph, Twitter Card, schema)
 * is intentionally NOT handled here — install RankMath or Yoast SEO and configure
 * each page's SEO fields (and the plugin's Local Business schema settings) there.
 * An earlier version of this theme hardcoded that output itself; it was removed so
 * the SEO plugin can own it cleanly with no duplicate/competing tags.
 */

if ( ! defined( 'ABSPATH' ) ) exit;

function eas_theme_setup() {
	add_theme_support( 'title-tag' );
	add_theme_support( 'post-thumbnails' );
	add_theme_support( 'html5', array( 'search-form', 'gallery', 'caption' ) );
	add_theme_support( 'align-wide' );
}
add_action( 'after_setup_theme', 'eas_theme_setup' );

function eas_enqueue_assets() {
	wp_enqueue_style(
		'eas-google-fonts',
		'https://fonts.googleapis.com/css2?family=Barlow:wght@400;600;700;800&family=Barlow+Condensed:wght@800&display=swap',
		array(),
		null
	);
	wp_enqueue_style( 'eas-style', get_stylesheet_uri(), array(), '1.0.1' );
	wp_enqueue_script( 'eas-faq-accordion', get_template_directory_uri() . '/js/faq-accordion.js', array(), '1.0.0', true );
}
add_action( 'wp_enqueue_scripts', 'eas_enqueue_assets' );

/**
 * [eas_hero_form] — the homepage hero's quick-estimate form. Registered as a shortcode
 * (instead of being hardcoded in front-page.php) so it can be dropped anywhere in the
 * block editor via a Shortcode block, same as the contact form below.
 */
function eas_hero_form_shortcode() {
	ob_start();
	?>
	<div class="hero-card">
		<h3>Get a Free Estimate Today</h3>
		<form action="<?php echo esc_url( home_url( '/contact/' ) ); ?>" method="get">
			<input type="text" placeholder="Your Name" aria-label="Your name" required>
			<input type="tel" placeholder="Phone Number" aria-label="Phone number" required>
			<select aria-label="Service needed">
				<option value="">Service Needed...</option>
				<option>AC Repair</option>
				<option>AC Installation</option>
				<option>Heating Service</option>
				<option>Maintenance Plan</option>
				<option>Emergency Service</option>
			</select>
			<button type="submit" class="btn btn-primary">Request Free Estimate →</button>
		</form>
	</div>
	<?php
	return ob_get_clean();
}
add_shortcode( 'eas_hero_form', 'eas_hero_form_shortcode' );

/**
 * [eas_contact_form] — the Contact page's estimate request form.
 * No backend is wired up (matches the original static mock). To capture real leads,
 * install a forms plugin (WPForms / Contact Form 7) and swap this shortcode for theirs.
 */
function eas_contact_form_shortcode() {
	ob_start();
	?>
	<div class="contact-form">
		<h2>Request a Free Estimate</h2>
		<p class="sub">Fill out the form and we'll call or text you back within the hour (during business hours) to confirm your appointment.</p>
		<form>
			<div class="form-row two" style="margin-bottom: 16px;">
				<div class="form-group">
					<label for="fname">First Name</label>
					<input type="text" id="fname" placeholder="Maria" required>
				</div>
				<div class="form-group">
					<label for="lname">Last Name</label>
					<input type="text" id="lname" placeholder="Garcia" required>
				</div>
			</div>
			<div class="form-row two" style="margin-bottom: 16px;">
				<div class="form-group">
					<label for="phone">Phone</label>
					<input type="tel" id="phone" placeholder="(813) 555-xxxx" required>
				</div>
				<div class="form-group">
					<label for="email">Email</label>
					<input type="email" id="email" placeholder="maria@email.com">
				</div>
			</div>
			<div class="form-row" style="margin-bottom: 16px;">
				<div class="form-group">
					<label for="service">Service Needed</label>
					<select id="service" required>
						<option value="">Select a service...</option>
						<option>AC Repair</option>
						<option>AC Installation / Replacement</option>
						<option>Heating Service</option>
						<option>Maintenance Plan</option>
						<option>Indoor Air Quality</option>
						<option>Emergency Service</option>
						<option>Other / Not Sure</option>
					</select>
				</div>
			</div>
			<div class="form-row" style="margin-bottom: 16px;">
				<div class="form-group">
					<label for="address">Property Address</label>
					<input type="text" id="address" placeholder="Tampa, FL 33603">
				</div>
			</div>
			<div class="form-row" style="margin-bottom: 16px;">
				<div class="form-group">
					<label for="message">Tell Us More (optional)</label>
					<textarea id="message" placeholder="Describe what's going on with your AC or what you're looking to get done..."></textarea>
				</div>
			</div>
			<button type="submit" class="btn btn-primary">Send My Request →</button>
			<p class="form-note">We respond within 1 hour during business hours. For emergencies, call (813) 555-0100 directly.</p>
		</form>
	</div>
	<?php
	return ob_get_clean();
}
add_shortcode( 'eas_contact_form', 'eas_contact_form_shortcode' );
