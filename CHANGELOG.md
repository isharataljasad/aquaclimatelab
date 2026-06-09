# Change log

## Revision — Educational value expansion

- Added five new educational sections that turn the site from a landing page into a learning resource:
  - **Water Data Explorer** — 8 indicator cards (pH, EC, TDS, Salinity, Hardness, Nitrate, Temperature, Turbidity) with meaning + educational interpretation, plus a clear "screening concepts only" note.
  - **Hydrology Signals** — 8 concept cards (Rainfall, Infiltration, Recharge, Runoff, Evaporation, Soil Moisture, Water Table, Watershed) with why-it-matters.
  - **Chemistry × Hydrology Map** — a responsive flow diagram (Rainfall → Infiltration → Soil interaction → Dissolved ions → Groundwater/runoff → Water-quality signal) with an explanatory panel.
  - **Mini Dataset Demo** — an interactive, keyboard-accessible table of 5 fictional water samples (Sample ID, Source Type, pH, EC, TDS, Hardness, Nitrate, Salinity, Turbidity, Temperature). Selecting a row shows educational signal tags computed by static JS. Clearly labelled "Sample data for education only" with no diagnosis/safe-unsafe claims.
  - **Water Wonder Questions** — 6 bilingual prompts.
- Navigation updated to: Tracks · Smart Fertigation · Water Data · Hydrology Signals · Projects · Interactive Demo · Team · Contact.
- Renamed the team role "Data Science & AI Track Builder" → **"Digital Tools & Data Track"** with a softer, broader description.
- Public contact email set to **renadsuf2002@gmail.com** (only contact detail added).
- Meta description / keywords extended: water data, hydrology, water chemistry, arid regions, smart fertigation, data dashboards, educational water-quality indicators.
- Premium dark theme preserved; data table scrolls horizontally on mobile; no overcrowding. No personal/family/employer references; no company names.

---

## Revision — Smart Fertigation image reliability fix

- The Smart Fertigation feature image is now **embedded directly inside `index.html` as a data URI** (optimized JPEG). It makes zero network requests, so it can no longer 404 or show alt text on any host or build pipeline.
- Corrected earlier absolute (`/assets/...`) paths to relative for the favicon and manifest icon.
- Improved the section: defined 3:2 image frame with `object-fit: cover` (no stretching), cyan border, and soft glow; balanced two-column desktop layout that stacks cleanly on mobile.
- Refined Arabic/English copy, the subtitle, and the eight technology tags; refreshed the three cards.
- Removed the now-unused standalone `assets/smart-fertigation.png` (the image lives inline).
- No personal, family, employer, company, university, or government references.

---

## Revision — Smart Fertigation section

- Added a new premium section, **Smart Fertilizer & Precision Fertigation**, placed directly after Three Tracks to complete the lab triangle: Water/Climate → Chemistry/Nutrients → Data/AI.
- Section includes the supplied root-zone visual (`assets/smart-fertigation.png`, optimized for web with descriptive alt text), a concise intro, a chip row of the nine enabling technologies, and three cards: Controlled-Release Nutrients, Precision Fertigation, and AI & Sensor Feedback.
- Image styled to match the dark theme: rounded corners, hairline border, and a soft cyan inner glow; fully responsive and lazy-loaded.
- Added **Smart Fertigation** to the navigation menu.
- Gently extended metadata (description, Open Graph, Twitter, JSON-LD, keywords) to include precision fertigation and smart fertilizer.
- Expanded the disclaimer to explicitly exclude agricultural and commercial advice.
- Updated `sitemap.xml` `lastmod`, README file tree, and track list.
- No personal, family, employer, company, university, or government references anywhere; remains an independent educational and portfolio prototype.

---

## Revision — AquaClimate Lab (initial release)

### Rebrand
- Renamed the project from *Desert Water & Climate Lab* to **AquaClimate Lab** across every file.
- Switched all metadata, sitemap, robots, and canonical URLs to **aquaclimatelab.com** (was `example.com`).
- New brand mark (water-drop SVG), `favicon.svg`, and a 1200×630 social image (`og-image.png` + editable `og-image.svg`).

### Design
- Rebuilt the theme as a premium dark **"research console"** look: near-black navy base, faint data-grid texture, water-blue / soft-cyan / climate-amber accents, white text, muted-gray secondary text.
- New hero **signature element**: a "Convergence Readout" instrument panel (Water / Climate / Chemistry / Data channels) replacing the previous orbit graphic.
- System-font pairing (sans for display/body, mono for data labels and field codes) — no external fonts, so loading stays instant.
- Clean line-style SVG icons throughout (no childish or crowded infographics); elegant cards, soft gradients, and disciplined spacing.

### Structure & content
- Added the requested sections that were missing or merged: a dedicated **Why Arizona?**, a separate **Saudi relevance** section, and an **About / Profiles** section.
- Profiles use safe role placeholders — *Water & Climate Track Lead*, *Chemistry & Industry Track Lead*, *Data Science & AI Track Builder* — with `Coming soon` LinkedIn labels.
- Reworked **Mini Projects** to the five requested cards: Water Quality Dashboard, Rain to Groundwater Map, Desert Climate Notes, Chemistry of Water Treatment, Arid Region Data Explorer.
- Process model numbered only where order is real (Observe → Explain → Model → Communicate).
- Removed personal framing and product call-outs from the tracks; backgrounds are now described in safe, general language.

### Interactive demo
- Expanded the water-quality demo from 3 to **4 inputs**: pH, TDS, hardness, **and salinity**.
- Clear, priority-ordered educational interpretation with a live status readout; explicit "educational only — not a lab or health test" disclaimer.

### Safety
- Generalized the disclaimer to "any employer, university, or government entity" — no company or university is named anywhere.
- Added a clear standalone **Disclaimer** section plus footer link.

### SEO
- Improved `<title>` and meta description; added full **Open Graph** and **Twitter card** tags, canonical URL, and **JSON-LD** (`WebSite`).
- Structured semantic headings (`h1`/`h2`/`h3`), labelled landmarks, and an updated `sitemap.xml` with `lastmod`.

### Accessibility
- Strong contrast on the dark palette; visible keyboard focus rings (`:focus-visible`).
- Skip-to-content link, ARIA labels on nav and the demo, `aria-live` status for the demo result, Escape-to-close mobile menu.
- `prefers-reduced-motion` respected (animations disabled); the only motion is a subtle hero pulse.
- Alt text / `aria-label` on all meaningful graphics; decorative SVGs marked `aria-hidden`.

### Infrastructure
- `vercel.json`: kept clean URLs, added security headers (CSP, X-Content-Type-Options, X-Frame-Options, Referrer-Policy, Permissions-Policy) and long-lived caching for `/assets`.
- Updated `manifest.webmanifest` (name, colors, SVG icon) and a rebranded `404.html` that matches the new theme.
