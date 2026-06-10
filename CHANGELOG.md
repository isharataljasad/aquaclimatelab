# Change log

## Revision — Career wording cleanup

- Replaced career-outcome wording with evidence-based professional readiness language.
- Removed direct career-outcome promise language from visible pages and prompts.
- Kept the focus on skills, measurable work artifacts, leadership readiness, and safe CV statements.

## v16 — Career-OS Skill Module engine + Module 001
- New #skill-modules section: reusable daily module structure (native <details> accordions, zero JS) covering best practice, 8-week training, artifact, readiness metrics, CV-safety, next-skill pointer.
- Module 001 shipped: ISO/IEC 17025 awareness & practice (chosen because the v15 decision table already names it as the chemistry-quality choice); includes verification flag and the standard's labs-not-individuals accreditation caveat.
- Accuracy fix: sources section mislabeled ISO/Aspen/PMI/NEBOSH links as 'Open source' — relabeled (USGS tools: المصدر الرسمي (مجاني); commercial/standards: الموقع الرسمي).
- Nav: added Modules link. CSS appended to page-embedded styles and assets/css/styles.css. No content removed.

## Revision — Career-OS decision-based update

- Replaced vague career examples with fixed selected paths.
- Hydrology path: MODFLOW 6 + QGIS + NASA ARSET.
- Chemistry path: Aspen Plus + Minitab + ISO/IEC 17025.
- Water chemistry bridge: PHREEQC after foundations.
- Team lead readiness: ISO 14001 + ISO/IEC 17025 + CAPM/PMP by eligibility + NEBOSH IGC.
- Added leadership readiness matrix and evidence-based CV language.
- Updated Claude prompt to require decisions, not generic examples.

## v14 — Career-OS completion
- Added missing CSS for .timeline, .mini-dashboard, .hero-visual/.hero-copy (the 12-month plan previously rendered as an unstyled browser list); appended to both the page-embedded CSS and assets/css/styles.css.
- Hydrology track: named QGIS/ArcGIS as supporting skill, added the Water-Source Mapping mini-project alongside the groundwater scenario.
- Chemistry track: added lab-quality (calibration/QC/documentation) as a supporting skill next to Minitab/JMP/Excel.
- Bridge: explicit rule that the dashboard organizes questions and never declares water safe/unsafe; added the verification-gate wording.
- Work skills expanded 6→8 cards: asking for feedback, pressure & professional disagreement, and a dedicated Career Evidence Portfolio card.
- Health expanded 4→6 cards: consistent sleep, hydration-without-fear (links the article, with medical-context caveat), digital boundaries inside Focus; stress workflow added; feminine-form Arabic normalized to the site's neutral voice.
- No frameworks, no removed pages/PDF links/emails; layout responsive at 980/900/620px.

## Revision — Career-OS starter section

- Added homepage Career-OS section for Hydrology × Chemistry career building.
- Added `career-os.html` as a full starter page.
- Added navigation links to Career-OS.
- Added CV-ready sample statements for MODFLOW 6, Aspen Plus, and water chemistry interpretation.
- Added work skills, business language, career evidence portfolio logic, and health/energy routines.
- Added `CLAUDE_CAREER_OS_PROMPT.md` so Claude can continue the remaining refinement safely.

## v12 — Back-to-top button fix
- Cause: id="top" lived on the position:sticky header; anchoring to a stuck sticky element resolves to its current pinned position, so clicking "العودة للأعلى" scrolled nowhere.
- Fix: moved id="top" to <body> on all pages (index, water-without-fear, 404, download page). No visual, content, or layout changes; smooth scrolling, skip-link (#main), PDF links, and both contact emails untouched.

## Revision — PDF 404 deployment fix

- Added root-level PDF: `water-as-body-operating-system-12-slides.pdf`.
- Kept backup PDF copy at `assets/docs/water-as-body-operating-system-12-slides.pdf`.
- Updated site buttons to use the safer root-level PDF path.
- Added `download-water-wonder-pdf.html` as a fallback download page.
- Added logo PNG asset: `assets/img/aquaclimate-lab-logo-horizontal.png`.
- Added explicit Vercel PDF headers.

## Revision — PDF attachment and logo asset

- Added the 12-slide PDF to `assets/docs/water-as-body-operating-system-12-slides.pdf`.
- Added a download button on the homepage Water Wonder section.
- Added a download button and sidebar link on `water-without-fear.html`.
- Added standalone logo asset `assets/img/aquaclimatelab-logo.svg`.

## v9 — Article page styling fix (water-without-fear)
- Root cause: the article and 404 pages depended solely on the external assets/css/styles.css; when the static pipeline fails to serve it, the page renders unstyled (purple skip link, giant droplet SVG, raw browser layout). The homepage was immune because its CSS is embedded.
- Fix: embedded the same critical CSS inline into water-without-fear.html and 404.html (homepage pattern); inlined main.js into the article page so nav toggle/footer year work without assets/.
- Hardened: width=24 height=24 attributes on all brand droplet SVGs (can never render huge, even unstyled); ./ relative favicon paths.
- No design, content, or routing changes. assets/css/styles.css kept in repo for future pages.

## v8 — Light "bright lab" redesign
- Inverted theme from dark research console to ice-white (#F2FAFD) premium light mode; deep navy retained for header, footer, contact, and the hero instrument console (signature element).
- Arabic typography upgraded to Tajawal (with IBM Plex Sans Arabic / Noto Kufi / Cairo fallbacks); larger base size, line-height 1.95 for comfortable long-form Arabic reading.
- Accents deepened (aqua #0E84A8, cyan #0E7C9E, amber #B9781E) for AA-level contrast on white; softer shadows, reduced glow.
- Completed the external stylesheet (added homepage-only blocks: data table, hydrology, flow map, edu/question cards) so it now matches the inline homepage CSS exactly.
- Updated theme-color and web manifest to the new palette. No content, structure, JS logic, or disclaimers changed.

## Revision — Contact email update

- Added the second public contact email: **yarasuf2001@gmail.com**.
- Preserved the existing contact email: **renadsuf2002@gmail.com**.

## Revision — Educational value expansion

- Added five new educational sections that turn the site from a landing page into a learning resource:
  - **Water Data Explorer** — 8 indicator cards (pH, EC, TDS, Salinity, Hardness, Nitrate, Temperature, Turbidity) with meaning + educational interpretation, plus a clear "screening concepts only" note.
  - **Hydrology Signals** — 8 concept cards (Rainfall, Infiltration, Recharge, Runoff, Evaporation, Soil Moisture, Water Table, Watershed) with why-it-matters.
  - **Chemistry × Hydrology Map** — a responsive flow diagram (Rainfall → Infiltration → Soil interaction → Dissolved ions → Groundwater/runoff → Water-quality signal) with an explanatory panel.
  - **Mini Dataset Demo** — an interactive, keyboard-accessible table of 5 fictional water samples (Sample ID, Source Type, pH, EC, TDS, Hardness, Nitrate, Salinity, Turbidity, Temperature). Selecting a row shows educational signal tags computed by static JS. Clearly labelled "Sample data for education only" with no diagnosis/safe-unsafe claims.
  - **Water Wonder Questions** — 6 bilingual prompts.
- Navigation updated to: Tracks · Smart Fertigation · Water Data · Hydrology Signals · Projects · Interactive Demo · Team · Contact.
- Renamed the team role "Data Science & AI Track Builder" → **"Digital Tools & Data Track"** with a softer, broader description.
- Public contact emails set to **renadsuf2002@gmail.com** and **yarasuf2001@gmail.com**.
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


## v6 — Water Wonder practical article
- Added a new Water Wonder section to the homepage.
- Added `water-without-fear.html`: practical Arabic article on bottled water, plastics, filters, official warnings, testing, and treated water.
- Updated sitemap and metadata for the new article.
- Preserved educational/non-diagnostic/non-commercial positioning.
