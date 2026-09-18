<?php
/**
 * Priority Plumbing & Drain theme functions.
 *
 * SEO (title tag, meta description, canonical, Open Graph, Twitter Card, schema)
 * is intentionally NOT handled here — install RankMath or Yoast SEO and configure
 * each page's SEO fields (and the plugin's Local Business / Plumber schema settings)
 * there instead, same as any real WordPress build.
 */

if ( ! defined( 'ABSPATH' ) ) exit;

function pp_theme_setup() {
	add_theme_support( 'title-tag' );
	add_theme_support( 'post-thumbnails' );
	add_theme_support( 'html5', array( 'search-form', 'gallery', 'caption' ) );
	add_theme_support( 'align-wide' );
}
add_action( 'after_setup_theme', 'pp_theme_setup' );

function pp_enqueue_assets() {
	wp_enqueue_style(
		'pp-google-fonts',
		'https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&family=Barlow+Condensed:wght@700;800&display=swap',
		array(),
		null
	);
	wp_enqueue_style( 'pp-style', get_stylesheet_uri(), array(), '1.0.0' );
	wp_enqueue_script( 'pp-faq-accordion', get_template_directory_uri() . '/js/faq-accordion.js', array(), '1.0.0', true );
}
add_action( 'wp_enqueue_scripts', 'pp_enqueue_assets' );

/**
 * [pp_contact_form] — the Contact page's free-estimate request form.
 * No backend is wired up (matches the original static mock). To capture real leads,
 * install a forms plugin (WPForms / Contact Form 7) and swap this shortcode for theirs.
 */
function pp_contact_form_shortcode() {
	ob_start();
	?>
	<div class="form-emergency-note">
		<strong>Have a plumbing emergency?</strong> Don't fill out the form — call us now at <a href="tel:8135550194">(813) 555-0194</a>. We answer 24/7 and dispatch within 60 minutes.
	</div>
	<form action="#" method="POST" novalidate aria-label="Request a free estimate">
		<div class="form-row">
			<div class="form-group">
				<label class="form-label" for="first-name">First Name *</label>
				<input class="form-input" type="text" id="first-name" name="first_name" required autocomplete="given-name" placeholder="Ray">
			</div>
			<div class="form-group">
				<label class="form-label" for="last-name">Last Name *</label>
				<input class="form-input" type="text" id="last-name" name="last_name" required autocomplete="family-name" placeholder="Vasquez">
			</div>
		</div>
		<div class="form-row">
			<div class="form-group">
				<label class="form-label" for="phone">Phone Number *</label>
				<input class="form-input" type="tel" id="phone" name="phone" required autocomplete="tel" placeholder="(813) 555-0000">
			</div>
			<div class="form-group">
				<label class="form-label" for="email">Email Address</label>
				<input class="form-input" type="email" id="email" name="email" autocomplete="email" placeholder="you@email.com">
			</div>
		</div>
		<div class="form-group">
			<label class="form-label" for="address">Service Address *</label>
			<input class="form-input" type="text" id="address" name="address" required autocomplete="street-address" placeholder="4218 N Nebraska Ave, Tampa, FL 33603">
		</div>
		<div class="form-group">
			<label class="form-label" for="service-type">Service Needed *</label>
			<select class="form-select" id="service-type" name="service_type" required>
				<option value="" disabled selected>Select a service...</option>
				<option value="emergency">Emergency Plumbing (call us instead)</option>
				<option value="drain-cleaning">Drain Cleaning</option>
				<option value="water-heater">Water Heater Repair / Replacement</option>
				<option value="pipe-repair">Pipe Repair / Repiping</option>
				<option value="leak-detection">Leak Detection</option>
				<option value="sewer">Sewer Line Service</option>
				<option value="other">Other / Not Sure</option>
			</select>
		</div>
		<div class="form-group">
			<label class="form-label" for="message">Describe the Problem</label>
			<textarea class="form-textarea" id="message" name="message" placeholder="Tell us what's happening — when did it start, any visible damage, what you've tried so far. The more detail you give, the faster we can quote it."></textarea>
		</div>
		<button type="submit" class="btn-submit">Send My Request — We'll Call You Within 15 Minutes</button>
		<p class="form-disclaimer">No spam. We use your contact info only to respond to this request. By submitting, you agree to be contacted by Priority Plumbing &amp; Drain by phone or email.</p>
	</form>
	<?php
	return ob_get_clean();
}
add_shortcode( 'pp_contact_form', 'pp_contact_form_shortcode' );
