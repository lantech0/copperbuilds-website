const fs = require('fs');

const aboutSVG = `<svg viewBox="0 0 480 360" fill="none" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:480px">
<rect width="480" height="360" rx="20" fill="#FAFAF7"/>
<rect x="24" y="24" width="204" height="148" rx="14" fill="#FFFFFF" stroke="#E7E0D8" stroke-width="1.5"/>
<text x="44" y="56" font-family="JetBrains Mono,monospace" font-size="9" fill="#E8600A" letter-spacing="1.2">BUSINESSES SERVED</text>
<text x="44" y="116" font-family="JetBrains Mono,monospace" font-size="52" font-weight="700" fill="#1C1917">50+</text>
<text x="44" y="148" font-family="JetBrains Mono,monospace" font-size="9" fill="#78716C" letter-spacing="0.8">Across the United States</text>
<rect x="252" y="24" width="204" height="68" rx="14" fill="#E8600A"/>
<text x="272" y="52" font-family="JetBrains Mono,monospace" font-size="9" fill="rgba(255,255,255,0.7)" letter-spacing="1.2">AVG DELIVERY TIME</text>
<text x="272" y="80" font-family="JetBrains Mono,monospace" font-size="36" font-weight="700" fill="#FFFFFF">48h</text>
<rect x="252" y="104" width="204" height="68" rx="14" fill="#FFFFFF" stroke="#E7E0D8" stroke-width="1.5"/>
<text x="272" y="130" font-family="JetBrains Mono,monospace" font-size="9" fill="#E8600A" letter-spacing="1.2">CLIENT SATISFACTION</text>
<text x="272" y="158" font-family="JetBrains Mono,monospace" font-size="36" font-weight="700" fill="#1C1917">100%</text>
<rect x="24" y="188" width="432" height="148" rx="14" fill="#FFFFFF" stroke="#E7E0D8" stroke-width="1.5"/>
<text x="44" y="216" font-family="JetBrains Mono,monospace" font-size="9" fill="#E8600A" letter-spacing="1.2">CORE SERVICES</text>
<rect x="44" y="228" width="88" height="76" rx="10" fill="#FAFAF7" stroke="#E7E0D8" stroke-width="1"/>
<text x="88" y="264" font-family="JetBrains Mono,monospace" font-size="8" fill="#78716C" text-anchor="middle">Web Design</text>
<rect x="44" y="282" width="88" height="4" rx="2" fill="#E8600A"/>
<rect x="148" y="228" width="88" height="76" rx="10" fill="#FAFAF7" stroke="#E7E0D8" stroke-width="1"/>
<text x="192" y="264" font-family="JetBrains Mono,monospace" font-size="8" fill="#78716C" text-anchor="middle">Local SEO</text>
<rect x="252" y="228" width="88" height="76" rx="10" fill="#FAFAF7" stroke="#E7E0D8" stroke-width="1"/>
<text x="296" y="264" font-family="JetBrains Mono,monospace" font-size="8" fill="#78716C" text-anchor="middle">Google Maps</text>
<rect x="356" y="228" width="88" height="76" rx="10" fill="#FAFAF7" stroke="#E7E0D8" stroke-width="1"/>
<text x="400" y="264" font-family="JetBrains Mono,monospace" font-size="8" fill="#78716C" text-anchor="middle">Social Media</text>
</svg>`;

const pricingSVG = `<svg viewBox="0 0 480 360" fill="none" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:480px">
<rect width="480" height="360" rx="20" fill="#FAFAF7"/>
<rect x="16" y="48" width="136" height="272" rx="14" fill="#FFFFFF" stroke="#E7E0D8" stroke-width="1.5"/>
<text x="84" y="82" font-family="JetBrains Mono,monospace" font-size="8" fill="#78716C" text-anchor="middle" letter-spacing="1">STARTER</text>
<text x="84" y="122" font-family="JetBrains Mono,monospace" font-size="28" font-weight="700" fill="#1C1917" text-anchor="middle">$1,200</text>
<text x="84" y="140" font-family="JetBrains Mono,monospace" font-size="7.5" fill="#78716C" text-anchor="middle">flat rate</text>
<line x1="32" y1="158" x2="136" y2="158" stroke="#E7E0D8" stroke-width="1"/>
<rect x="32" y="172" width="8" height="8" rx="2" fill="rgba(232,96,10,0.2)"/>
<rect x="48" y="173" width="76" height="6" rx="3" fill="#E7E0D8"/>
<rect x="32" y="190" width="8" height="8" rx="2" fill="rgba(232,96,10,0.2)"/>
<rect x="48" y="191" width="60" height="6" rx="3" fill="#E7E0D8"/>
<rect x="32" y="208" width="8" height="8" rx="2" fill="rgba(232,96,10,0.2)"/>
<rect x="48" y="209" width="68" height="6" rx="3" fill="#E7E0D8"/>
<rect x="32" y="226" width="8" height="8" rx="2" fill="rgba(232,96,10,0.2)"/>
<rect x="48" y="227" width="54" height="6" rx="3" fill="#E7E0D8"/>
<rect x="28" y="286" width="104" height="20" rx="10" fill="#FAFAF7" stroke="#E7E0D8" stroke-width="1.5"/>
<text x="80" y="300" font-family="JetBrains Mono,monospace" font-size="8" fill="#1C1917" text-anchor="middle">Get Started</text>
<rect x="172" y="24" width="136" height="308" rx="14" fill="#1C1917"/>
<rect x="180" y="52" width="120" height="22" rx="11" fill="#E8600A"/>
<text x="240" y="66" font-family="JetBrains Mono,monospace" font-size="8" fill="#FFFFFF" text-anchor="middle" letter-spacing="0.8">MOST POPULAR</text>
<text x="240" y="104" font-family="JetBrains Mono,monospace" font-size="8" fill="rgba(255,255,255,0.55)" text-anchor="middle" letter-spacing="1">GROWTH</text>
<text x="240" y="148" font-family="JetBrains Mono,monospace" font-size="32" font-weight="700" fill="#FFFFFF" text-anchor="middle">$1,699</text>
<text x="240" y="166" font-family="JetBrains Mono,monospace" font-size="7.5" fill="rgba(255,255,255,0.45)" text-anchor="middle">flat rate</text>
<line x1="188" y1="184" x2="292" y2="184" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>
<rect x="188" y="198" width="8" height="8" rx="2" fill="rgba(232,96,10,0.5)"/>
<rect x="204" y="199" width="76" height="6" rx="3" fill="rgba(255,255,255,0.12)"/>
<rect x="188" y="216" width="8" height="8" rx="2" fill="rgba(232,96,10,0.5)"/>
<rect x="204" y="217" width="60" height="6" rx="3" fill="rgba(255,255,255,0.12)"/>
<rect x="188" y="234" width="8" height="8" rx="2" fill="rgba(232,96,10,0.5)"/>
<rect x="204" y="235" width="68" height="6" rx="3" fill="rgba(255,255,255,0.12)"/>
<rect x="188" y="252" width="8" height="8" rx="2" fill="rgba(232,96,10,0.5)"/>
<rect x="204" y="253" width="54" height="6" rx="3" fill="rgba(255,255,255,0.12)"/>
<rect x="188" y="270" width="8" height="8" rx="2" fill="rgba(232,96,10,0.5)"/>
<rect x="204" y="271" width="72" height="6" rx="3" fill="rgba(255,255,255,0.12)"/>
<rect x="184" y="298" width="112" height="22" rx="11" fill="#E8600A"/>
<text x="240" y="312" font-family="JetBrains Mono,monospace" font-size="8.5" fill="#FFFFFF" text-anchor="middle">Get Started</text>
<rect x="328" y="48" width="136" height="272" rx="14" fill="#FFFFFF" stroke="#E7E0D8" stroke-width="1.5"/>
<text x="396" y="82" font-family="JetBrains Mono,monospace" font-size="8" fill="#78716C" text-anchor="middle" letter-spacing="1">PRO</text>
<text x="396" y="122" font-family="JetBrains Mono,monospace" font-size="28" font-weight="700" fill="#1C1917" text-anchor="middle">$1,999</text>
<text x="396" y="140" font-family="JetBrains Mono,monospace" font-size="7.5" fill="#78716C" text-anchor="middle">flat rate</text>
<line x1="344" y1="158" x2="448" y2="158" stroke="#E7E0D8" stroke-width="1"/>
<rect x="344" y="172" width="8" height="8" rx="2" fill="rgba(232,96,10,0.2)"/>
<rect x="360" y="173" width="76" height="6" rx="3" fill="#E7E0D8"/>
<rect x="344" y="190" width="8" height="8" rx="2" fill="rgba(232,96,10,0.2)"/>
<rect x="360" y="191" width="60" height="6" rx="3" fill="#E7E0D8"/>
<rect x="344" y="208" width="8" height="8" rx="2" fill="rgba(232,96,10,0.2)"/>
<rect x="360" y="209" width="68" height="6" rx="3" fill="#E7E0D8"/>
<rect x="344" y="226" width="8" height="8" rx="2" fill="rgba(232,96,10,0.2)"/>
<rect x="360" y="227" width="54" height="6" rx="3" fill="#E7E0D8"/>
<rect x="344" y="244" width="8" height="8" rx="2" fill="rgba(232,96,10,0.2)"/>
<rect x="360" y="245" width="72" height="6" rx="3" fill="#E7E0D8"/>
<rect x="340" y="286" width="104" height="20" rx="10" fill="#FAFAF7" stroke="#E7E0D8" stroke-width="1.5"/>
<text x="392" y="300" font-family="JetBrains Mono,monospace" font-size="8" fill="#1C1917" text-anchor="middle">Get Started</text>
</svg>`;

const contactSVG = `<svg viewBox="0 0 480 360" fill="none" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:480px">
<rect width="480" height="360" rx="20" fill="#FAFAF7"/>
<rect x="24" y="24" width="288" height="312" rx="14" fill="#FFFFFF" stroke="#E7E0D8" stroke-width="1.5"/>
<text x="44" y="56" font-family="JetBrains Mono,monospace" font-size="9" fill="#E8600A" letter-spacing="1.2">GET IN TOUCH</text>
<text x="44" y="80" font-family="JetBrains Mono,monospace" font-size="11" font-weight="700" fill="#1C1917">Start your project</text>
<rect x="44" y="96" width="248" height="36" rx="8" fill="#FAFAF7" stroke="#E7E0D8" stroke-width="1.5"/>
<text x="60" y="119" font-family="JetBrains Mono,monospace" font-size="8.5" fill="#A8A29E">Your name</text>
<rect x="44" y="144" width="248" height="36" rx="8" fill="#FAFAF7" stroke="#E7E0D8" stroke-width="1.5"/>
<text x="60" y="167" font-family="JetBrains Mono,monospace" font-size="8.5" fill="#A8A29E">Email address</text>
<rect x="44" y="192" width="248" height="36" rx="8" fill="#FAFAF7" stroke="#E7E0D8" stroke-width="1.5"/>
<text x="60" y="215" font-family="JetBrains Mono,monospace" font-size="8.5" fill="#A8A29E">Business type</text>
<rect x="44" y="240" width="248" height="60" rx="8" fill="#FAFAF7" stroke="#E7E0D8" stroke-width="1.5"/>
<text x="60" y="263" font-family="JetBrains Mono,monospace" font-size="8.5" fill="#A8A29E">Tell us about your project...</text>
<rect x="44" y="314" width="248" height="8" rx="4" fill="#E8600A"/>
<rect x="332" y="24" width="124" height="64" rx="12" fill="#1C1917"/>
<text x="394" y="48" font-family="JetBrains Mono,monospace" font-size="8" fill="rgba(255,255,255,0.55)" text-anchor="middle" letter-spacing="1">RESPONSE</text>
<text x="394" y="72" font-family="JetBrains Mono,monospace" font-size="22" font-weight="700" fill="#FFFFFF" text-anchor="middle">&lt; 24h</text>
<rect x="332" y="100" width="124" height="64" rx="12" fill="#E8600A"/>
<text x="394" y="124" font-family="JetBrains Mono,monospace" font-size="8" fill="rgba(255,255,255,0.7)" text-anchor="middle" letter-spacing="1">QUOTE</text>
<text x="394" y="152" font-family="JetBrains Mono,monospace" font-size="22" font-weight="700" fill="#FFFFFF" text-anchor="middle">Free</text>
<rect x="332" y="176" width="124" height="160" rx="12" fill="#FFFFFF" stroke="#E7E0D8" stroke-width="1.5"/>
<text x="352" y="204" font-family="JetBrains Mono,monospace" font-size="8" fill="#E8600A" letter-spacing="1">WHAT WE NEED</text>
<rect x="352" y="214" width="8" height="8" rx="2" fill="rgba(232,96,10,0.2)"/>
<rect x="368" y="215" width="72" height="6" rx="3" fill="#E7E0D8"/>
<rect x="352" y="230" width="8" height="8" rx="2" fill="rgba(232,96,10,0.2)"/>
<rect x="368" y="231" width="56" height="6" rx="3" fill="#E7E0D8"/>
<rect x="352" y="246" width="8" height="8" rx="2" fill="rgba(232,96,10,0.2)"/>
<rect x="368" y="247" width="64" height="6" rx="3" fill="#E7E0D8"/>
<rect x="352" y="262" width="8" height="8" rx="2" fill="rgba(232,96,10,0.2)"/>
<rect x="368" y="263" width="48" height="6" rx="3" fill="#E7E0D8"/>
<rect x="352" y="290" width="84" height="24" rx="12" fill="#E8600A"/>
<text x="394" y="306" font-family="JetBrains Mono,monospace" font-size="8" fill="#FFFFFF" text-anchor="middle">Send Message</text>
</svg>`;

const apply = (file, oldSrc, newSVG) => {
  const path = 'C:/Users/User/LantechAI/copperbuilds/' + file;
  let c = fs.readFileSync(path, 'utf8');
  const escaped = oldSrc.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const updated = c.replace(new RegExp('<img src="' + escaped + '"[^>]*/?>'), newSVG);
  if (updated !== c) { fs.writeFileSync(path, updated); console.log('Updated:', file); return true; }
  console.log('No match in:', file);
  return false;
};

apply('about.html',   'brand_assets/illus-about-main.png',   aboutSVG);
apply('pricing.html', 'brand_assets/illus-pricing-main.png', pricingSVG);
apply('contact.html', 'brand_assets/illus-contact-main.png', contactSVG);
