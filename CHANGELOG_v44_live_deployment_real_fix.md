# v44 — Live deployment real fix · no password

## Primary fix
This version targets the live-only failure on:

- `/life-operating-calendar`
- `/year-operating-wheel`

The fix is deployment-focused, not a local-preview styling pass.

## What changed

1. Added explicit Vercel rewrites for the clean routes:
   - `/life-operating-calendar`
   - `/year-operating-wheel`
   - `/career-os`
   - `/wisdom-of-day`
   - `/water-without-fear`
   - `/search`
   - `/download-water-wonder-pdf`

2. Added folder-index fallbacks:
   - `life-operating-calendar/index.html`
   - `year-operating-wheel/index.html`
   - `career-os/index.html`
   - `wisdom-of-day/index.html`
   - `water-without-fear/index.html`
   - `search/index.html`
   - `download-water-wonder-pdf/index.html`

3. Converted navigation and internal links to root-absolute clean URLs, so they work from:
   - `/page`
   - `/page/`
   - `/page.html`

4. Created versioned CSS/JS files to bypass stale live cache:
   - `/assets/css/styles.v44.css`
   - `/assets/css/mobile-ux.v44.css`
   - `/assets/js/main.v44.js`
   - `/assets/js/mobile-ux.v44.js`
   - `/assets/js/site-search.v44.js`

5. Updated all pages to load root-absolute `/assets/...` paths.

6. Added a small critical shell/navigation CSS fallback inside every HTML page. This prevents raw bullets, default menu buttons, and unstyled header if external CSS is delayed, stale, or blocked.

7. Updated `vercel.json`:
   - explicit rewrites
   - page no-cache headers
   - CSS/JS no-cache headers during this stabilization build
   - image/PDF cache preserved safely
   - CSP adjusted to match the current static architecture and avoid blocking the site’s own static scripts

8. Updated current-page nav highlighting so it works on clean URLs, `.html` URLs, and folder-index URLs.

9. Fixed Search canonical URL and made search result URLs root-absolute.

## Preserved

- No password
- No invite gate
- No frameworks
- No tracking
- No content removed
- No PDFs removed
- Search preserved
- Book Tools preserved
- Water Wonder preserved
- Life Calendar preserved
- Year Wheel preserved

## Why this is different from v41/v42

Earlier passes focused mainly on typography and mobile styling. v44 fixes live deployment failure modes: clean route resolution, root-absolute assets, stale cache, folder fallback routing, CSP compatibility, and deployment headers.
