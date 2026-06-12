# v44 Verification Checklist

## Must pass before saying the live bug is closed

Open each route in a fresh incognito/private browser window:

- `https://aquaclimatelab.com/life-operating-calendar`
- `https://aquaclimatelab.com/life-operating-calendar.html`
- `https://aquaclimatelab.com/year-operating-wheel`
- `https://aquaclimatelab.com/year-operating-wheel.html`
- `https://aquaclimatelab.com/career-os`
- `https://aquaclimatelab.com/wisdom-of-day`
- `https://aquaclimatelab.com/water-without-fear`
- `https://aquaclimatelab.com/search`
- `https://aquaclimatelab.com/`
- `https://aquaclimatelab.com/index.html`

## Visual checks

- Life Calendar is not blank.
- Year Wheel is not raw HTML.
- No default browser bullets in the top navigation.
- Menu button is styled, not default gray browser style.
- Header appears dark/premium.
- Cards and sections are styled.
- No horizontal overflow on mobile.
- Arabic RTL text is readable.

## Mobile menu checks

On phone width:

1. Tap `Menu`.
2. Menu opens.
3. Tap `Menu` again.
4. Menu closes.
5. Tap a link inside the menu.
6. Menu closes and navigation works.

## DevTools Network checks

In Chrome DevTools → Network, reload with `Disable cache` enabled.

The following must return 200:

- `/assets/css/styles.v44.css`
- `/assets/css/mobile-ux.v44.css`
- `/assets/js/main.v44.js`
- `/assets/js/mobile-ux.v44.js`
- `/assets/js/site-search.v44.js` on `/search`

The HTML route must return 200 for both clean and `.html` URLs.

## Console checks

Console should not show:

- blocked CSS
- blocked JS
- CSP script blocking for site scripts
- 404 for `/assets/...`
- MIME type errors for CSS or JS

## Local validation performed

A local HTTP server test was run against clean URLs, trailing-slash folder fallbacks, and `.html` URLs. All tested page routes returned 200, all referenced local CSS/JS/PDF assets returned 200, and internal link validation passed.
