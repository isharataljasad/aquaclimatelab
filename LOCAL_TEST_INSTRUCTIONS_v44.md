# Local HTTP Test Instructions — v44

Do not test only by double-clicking HTML files. Test through a local HTTP server.

## Simple server test

From the unzipped folder:

```bash
python -m http.server 8080
```

Then open:

- `http://localhost:8080/`
- `http://localhost:8080/index.html`
- `http://localhost:8080/life-operating-calendar/`
- `http://localhost:8080/life-operating-calendar.html`
- `http://localhost:8080/year-operating-wheel/`
- `http://localhost:8080/year-operating-wheel.html`
- `http://localhost:8080/career-os/`
- `http://localhost:8080/search/`

Note: Python’s simple server serves folder routes with a trailing slash. v44 also includes root `.html` files and Vercel rewrites for clean no-slash routes.

## Vercel-like clean route test

For exact clean URLs without trailing slash, use Vercel preview after upload, because Vercel applies `vercel.json` rewrites.

Required Vercel preview routes:

- `/life-operating-calendar`
- `/year-operating-wheel`
- `/career-os`
- `/wisdom-of-day`
- `/water-without-fear`
- `/search`

## What to inspect locally

- CSS files load from `/assets/css/*.v44.css`.
- JS files load from `/assets/js/*.v44.js`.
- Top navigation is styled.
- Mobile menu opens and closes.
- Search returns results.
- Year Wheel month buttons appear.
- Life Calendar form fields appear.
