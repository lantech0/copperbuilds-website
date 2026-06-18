import puppeteer from 'puppeteer';
import path from 'path';
import { fileURLToPath, pathToFileURL } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const src = pathToFileURL(path.join(__dirname, 'render-logo.html')).href;

const browser = await puppeteer.launch({ headless: 'new' });

async function exportLogo(variant, outFile, bgColor) {
  const page = await browser.newPage();
  await page.setViewport({ width: 600, height: 200, deviceScaleFactor: 3 });
  await page.goto(src, { waitUntil: 'networkidle2' });

  if (variant === 'white') {
    await page.evaluate(() => document.body.classList.add('white'));
  }
  if (bgColor) {
    await page.evaluate((c) => document.body.style.background = c, bgColor);
  }

  // Wait for font
  await new Promise(r => setTimeout(r, 600));

  const el = await page.$('#logo');
  await el.screenshot({
    path: path.join(__dirname, outFile),
    omitBackground: !bgColor,
  });
  await page.close();
  console.log('Saved:', outFile);
}

// Light variant — dark text, transparent bg
await exportLogo('light', 'lantech-logo-new-light.png', null);

// White variant — white text, transparent bg (for dark surfaces)
await exportLogo('white', 'lantech-logo-new-white.png', null);

// On-surface preview — dark text on parchment bg
await exportLogo('light', 'lantech-logo-new-dark.png', '#FAFAF7');

await browser.close();
console.log('All logos exported.');
