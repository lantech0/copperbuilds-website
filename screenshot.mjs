import puppeteer from 'puppeteer';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const url = process.argv[2] || 'http://localhost:3000';
const args = process.argv.slice(3);
const mobileFlag = args.includes('--mobile');
const label = args.filter(a => !a.startsWith('--')).join('-') || '';

const screenshotsDir = path.join(__dirname, '.tmp');
if (!fs.existsSync(screenshotsDir)) fs.mkdirSync(screenshotsDir, { recursive: true });

const existing = fs.readdirSync(screenshotsDir).filter(f => f.endsWith('.png'));
const n = existing.length + 1;
const filename = label ? `screenshot-${n}-${label}.png` : `screenshot-${n}.png`;
const outputPath = path.join(screenshotsDir, filename);

const browser = await puppeteer.launch({
  headless: 'new',
  executablePath: undefined, // uses bundled chromium
});
const page = await browser.newPage();
await page.setViewport(mobileFlag
  ? { width: 375, height: 812, deviceScaleFactor: 3, isMobile: true }
  : { width: 1440, height: 900, deviceScaleFactor: 2 });
await page.goto(url, { waitUntil: 'networkidle2', timeout: 15000 });
// Skip CSS animations so all fade-in elements are fully visible in the screenshot
await page.addStyleTag({
  content: '*, *::before, *::after { animation-duration: 0s !important; animation-delay: 0s !important; transition-duration: 0s !important; transition-delay: 0s !important; }'
});
await new Promise(r => setTimeout(r, 400));
await page.screenshot({ path: outputPath, fullPage: true });
await browser.close();

console.log(`Screenshot saved: ${outputPath}`);
