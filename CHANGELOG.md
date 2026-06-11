## v37 — Invite-only showcase reading gate

- Added a soft invitation pass gate for the private operating-system pages only: `career-os.html`, `wisdom-of-day.html`, `life-operating-calendar.html`, and `year-operating-wheel.html`.
- Kept the homepage public as a premium showcase and added visible invite labels on protected hub cards.
- Kept Water Wonder, the PDF download page, 404 page, and all public assets open.
- Added `assets/js/invite-pass.js` and `assets/css/invite-pass.css`. One shared invite pass unlocks all protected pages through localStorage, and “خروج من مساحة الدعوة” clears access.
- Passcode is changed in one place only inside `assets/js/invite-pass.js`: `SITE_INVITE_PASS = 'CHANGE_THIS_INVITE_PASS'`.
- This is a soft static reading gate only, not real security; no network calls, accounts, cookies, analytics, or backend were added.
- Preserved Book Tools 001–010, Wisdom of the Day, Life Operating Calendar, Year Operating Wheel, Water Wonder, PDFs, both contact emails, and static GitHub/Vercel compatibility.
- Verified local links and anchors, JS syntax, protected/public page split, preserved emails/PDFs, and absence of the blocked terms.

## v36 — Precision UX red-team review (audit-driven, six changes only)

Role: senior mobile UX red-team pass on v35. No rebuild, no redesign, no content rewrite. Every change below was driven by a measured finding from headless-Chromium audits at 390 / 430 / 768 / 1366px, and each is scoped to the smallest possible surface.

Changes (file · reason · risk):

1. assets/css/mobile-ux.css — Book Tools index stacked layout at ≤600px.
   Finding: at 390px the index table's action column ("افتح") sat off-screen (measured at left:-35px) — reachable only by discovering a horizontal swipe. The most important column was the hidden one.
   Fix: pure-CSS responsive-table pattern scoped to .bt-index only: each row becomes a mini-card (number + theme on line 1, artifact on line 2, full-width 44px "افتح" button on line 3). Table header kept for screen readers via the clip pattern. Desktop table unchanged.
   Risk: low (CSS-only, one component, one breakpoint).

2. assets/css/mobile-ux.css — restored a scrollable cap (460px) on the Wisdom 60-theme list at ≤640px.
   Finding: v35's removal of the height cap made the list 5,490px tall and doubled the mobile page to 10,049px — a scannability regression introduced by v35 itself. v36 honestly reverts that over-correction: internal scroll returns (with touch momentum + overscroll containment), and the v35 win (≥46px theme tap targets) is kept. Page is back to 5,020px.
   Risk: low (reinstates pre-v35 behaviour with better targets).

3. assets/js/mobile-ux.js — mobile-only collapse of the ten "READY TO USE" tables in Book Tools.
   Finding: all ten tool tables default to open, adding length and per-tool table noise at 390px.
   Fix: on load at ≤760px only, the open attribute is removed inside #book-derived-tools. Content is fully preserved — one tap re-opens (verified: 5 rows render). Desktop is untouched (verified: 10 still open at 1366px). Without JS they simply stay open — a safe fallback. Runs once on load only, so it never fights the user's own toggles on rotation.
   Risk: low (progressive enhancement, mobile-only, graceful degradation).

4. year-operating-wheel.html + life-operating-calendar.html — removed one dead element from each: <button class="back-to-top">↑</button>.
   Finding: this button has no CSS rule anywhere and no JS handler (main.js only wires the .floating-top it injects itself). It rendered as a stray, unstyled 23×21px "↑" in static flow at the page bottom that does nothing when tapped — a duplicate of the working floating button, which remains on both pages (verified present). This is defect debris, not content.
   Risk: low (removes a non-functional duplicate; the working control is unaffected).

5. assets/css/mobile-ux.css — visual style for .nav-menu a[aria-current="page"].
   Finding: v35's JS sets aria-current="page" on the current page's nav link, but no rule made it visible.
   Fix: reuses the nav's existing focus treatment (background:rgba(255,255,255,.12), white text) — no new colors, identity untouched. Verified rendering on year-operating-wheel. Pages whose navs reference themselves only via #section anchors correctly get no marker (semantically right).
   Risk: low (one selector, mirrors an existing style).

6. assets/css/mobile-ux.css — footer links get ≥44px tap targets at ≤760px.
   Finding: footer link rows measured 20px tall on phones across inner pages.
   Risk: low (padding only).

Intentionally NOT changed (and why):
- career-os.html overall length (~100K px at 390px): that is the preserved content of ten full Book Tools; the mitigations are navigation (index jump links, summary cards, floating top, collapse), not deletion.
- Inline prose links (e.g., Catalyst Sources) below 44px: they are inline within running text; enlarging them would break paragraph flow. Accepted convention.
- "001–010" visual order in RTL context: the bidi rendering is correct for Arabic readers (reading right-to-left yields 001 first). Forcing dir="ltr" would be a typographic opinion, not a fix.
- Hub card order, month-card field order, desktop wheel, all wording, all colors/visual identity: audited, found correct, left alone.
- The two non-Book-Tools open details (Master Form, Daily Pack): only two elements; collapsing them was judged not worth touching another section.

Verification (headless Chromium): 0px horizontal overflow on all 8 pages at all 4 widths; zero real console/page errors; all inline + external JS pass node --check; year-wheel month select + clipboard copy verified; life-calendar red-flag alert verified; wisdom daily card renders and themes are clickable; all local links and anchors resolve; sitemap XML valid; both emails, 3 PDFs, Book Tools 001–010, and all pages preserved; the four blocked terms absent from every file.

Files changed: assets/css/mobile-ux.css, assets/js/mobile-ux.js, year-operating-wheel.html, life-operating-calendar.html (one dead element each). Files added: none. Files removed: none.


## v35 — Real mobile UX upgrade (hub, navigation, Book Tools browsing)

Scope: a genuine mobile user-experience upgrade on top of v34's CSS polish — not another CSS pass. No rebuild, no page or content removal, no frameworks, no external libraries, no tracking. Static HTML/CSS/JS only.

Bug fixes (page-breaking):
- wisdom-of-day.html: fixed a real JavaScript SyntaxError — the "copy card" string literal was split across five physical lines (raw newlines inside single quotes), which broke the entire inline script. In v34 this prevented the daily card and the 60-theme index from rendering. Rewritten as a valid single statement with `\n` escapes; verified with `node --check` and an end-to-end clipboard test.
- life-operating-calendar.html & year-operating-wheel.html: completed a malformed footer-logo SVG path (cubic-bezier `C` had 4 numbers instead of 6), removing a recurring console error.

New shared mobile-UX layer (additive, enhancement-only):
- assets/css/mobile-ux.css: visible keyboard focus rings, 44–52px touch targets, mobile table horizontal-scroll with an "اسحب أفقيًا" hint, mobile-only overflow guard (scoped to protect desktop `position:sticky`), and styles for the new hub / quick-nav / Book-Tools index & summary components. Loads after each page's embedded critical CSS, so base styling is never at risk.
- assets/js/mobile-ux.js: tiny, dependency-free — marks the current page in the top nav (`aria-current`) and flags genuinely-scrollable tables on resize.

1. Homepage as a mobile hub:
- index.html: added a self-contained "خريطة النظام" hub section (id="hub") right after the hero, with 6 large hub cards — حكمة اليوم, تقويم الحياة, العجلة السنوية, Career-OS, أدوات الكتب 001–010, الماء بلا خوف. Each card has a short Arabic title, a one-line purpose, a clear button, and a large tap area.
- Hero primary CTA now reads "ابدأ من هنا — خريطة النظام" and jumps to the hub; added an "ابدأ من هنا" entry to the nav.

2. Mobile navigation:
- Consistent current-page highlighting across pages (aria-current). Existing per-page navs and the floating back-to-top button preserved. Wisdom page gained explicit cross-links to تقويم الحياة and العجلة السنوية.

3. Career-OS / Book Tools browsing:
- career-os.html: added a collapsible compact Book Tools index (رقم الأداة · محور المهارة · الأداة الأساسية · افتح القسم) linking to tools 001–010.
- Added a scannable summary card above each of the 10 tools — CORE USE, TOOLS, 30-DAY, EVIDENCE, and "ما لا يُدّعى" — derived only from existing on-page content. No new book content invented; full original content preserved.

4. Year Operating Wheel:
- Larger, calmer mobile month navigator (≥52px buttons, 3 columns, 2 under 420px). Desktop wheel unchanged. Verified month selection, report build, and copy all work; no horizontal overflow; JS clean.

5. Life Operating Calendar:
- Bigger checklist tap rows and form targets on mobile; calmer red-flag list; verified the red-flag protection alert and local-save/copy behaviour still work. No medical claims added.

6. Wisdom of the Day:
- Page now actually works (see bug fix). Tidier 60-theme index and larger theme tap targets on mobile; copy and "أظهر حكمة أخرى" verified.

7–9. CSS / accessibility / SEO:
- Calmer section rhythm and breathing room on long pages, focus states, and table handling. Added a `.visually-hidden` utility (used for an index table caption). Normalized sitemap.xml (consistent lastmod 2026-06-11; includes index, career-os, wisdom-of-day, life-operating-calendar, year-operating-wheel, water-without-fear, and the Water Wonder PDF page). 404.html given the same overflow guard.

10. Testing (headless Chromium):
- Horizontal overflow = 0px on all pages at 390 / 768 / 1366px.
- No console/page errors (Google-Fonts 403s are sandbox-only and degrade gracefully via the font fallback stack).
- All inline + external JS pass `node --check`; copy buttons verified writing to the clipboard.
- The four blocked terms specified in the brief are absent across all text file types.
- Both contact emails and all 3 PDFs preserved; all local links/anchors resolve.

Files changed: index.html, career-os.html, wisdom-of-day.html, life-operating-calendar.html, year-operating-wheel.html, water-without-fear.html, 404.html, sitemap.xml. Files added: assets/css/mobile-ux.css, assets/js/mobile-ux.js.


## v23 — Book Tool 003: Interaction Styles Leadership Kit

- Added Book Tool 003 under Book-Derived Leadership Tools: `Interaction Styles Leadership Kit | التفاعل بأنماط القيادة: عدة التواصل والإسناد والضغط`.
- Converted the uploaded How to Get On with Anyone extraction into a practical leadership toolkit, not a book summary.
- Added 9 leadership clusters: impact gap, team reading map, communication planning, delegation decision, advocacy/inquiry balance, launch message, meeting stages, quiet authority, and pressure triage.
- Added 5 ready-to-use tools, a 30-day practice plan, a one-page report template, and safe CV/LinkedIn wording.
- Updated homepage Book Tools teaser.
- Added `CLAUDE_FABLE_V23_BOOK_TOOL_003_PROMPT.md` for final polish only.
- Preserved static HTML/CSS/JS structure, existing PDFs, Water Wonder pages, and contact emails.


## v22 — Book Tool 002: Clear-Mind Leadership Kit

- Added Book Tool 002 under Book-Derived Leadership Tools: `Clear-Mind Leadership Kit | حقيبة القيادة بالذهن الصافي`.
- Converted the uploaded Declutter Your Mind extraction into a practical leadership toolkit, not a book summary.
- Added 10 leadership clusters: mental load, meeting reframing, risk window, priority charter, capacity allocation, quarterly goals, weekly review, one-on-one listening, feedback balance, and task triage.
- Added 5 ready-to-use tools, a 30-day practice plan, a one-page report template, and safe CV/LinkedIn wording.
- Updated homepage Career-OS teaser and Book Tools card.
- Added `CLAUDE_FABLE_V22_BOOK_TOOL_002_PROMPT.md` for final polish only.
- Preserved static HTML/CSS/JS structure, existing PDFs, Water Wonder pages, and contact emails.

# Change log

## v20 — Cost Effectiveness & Operational Survival Engine

- career-os.html: added Module 002 for manufacturing cost effectiveness and operational survival.
- career-os.html: added 12 saving idea clusters covering spend, suppliers, inventory, forecasting, yield, utilities, assets, quality, export, process mining, data/AI, and governance.
- career-os.html: added Saving Idea Master Form, 30-day practice task, safe CV/LinkedIn wording, and SAP-like catalyst source links.
- index.html: added homepage teaser and direct link to the new cost engine.
- Added CLAUDE_FABLE_V20_COST_ENGINE_PROMPT.md for final Fable polishing only.
- Static HTML/CSS/JS preserved; no PDF links removed.

## v19 — Final polish pass (RTL, mobile, accessibility)

- career-os.html: fixed hero fact-list showing default browser bullets/indent in RTL; styled previously unstyled tag pills in hero card and Catalyst Sources boxes.
- career-os.html: decision table now scrolls horizontally on mobile (min-width) instead of crushing columns; table alignment changed to logical `text-align:start`; added `scope="col"` to all table headers (decision + matrix tables) for screen readers.
- career-os.html: English-only Catalyst Sources lists now render LTR so punctuation flows correctly; escaped a bare `&`; added Evidence link to the page nav.
- All pages: nav menu now wraps instead of overflowing horizontally at desktop widths (fixed a 13px horizontal scroll on index at 1280px).
- All pages: added a floating, accessible back-to-top button (vanilla JS, aria-label, respects prefers-reduced-motion); existing inline "العودة للأعلى" buttons preserved.
- No content removed, no wording changes, no framework added. Verified: forbidden upgrade-related wording (Arabic and English) is fully absent; all PDF links, Water Wonder article, and both contact emails intact.

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


## v18 Career-OS Toolbox
- Reframed Career-OS as a practical Leadership Toolbox rather than skills/CV advice.
- Added Project Saving Leadership Toolkit: charter, baseline, stakeholders, consensus, risk, KPI, action tracker, meeting rhythm, and one-page management report.
- Added Soft Skills as Tools and Hard Skills as Tools sections.
- Added limited Catalyst Sources boxes.
- Enhanced Module 001 with daily publishing pack: training note, LinkedIn-safe sentence, 30-day task, and one-page report template.
- Preserved static HTML/CSS/JS structure and existing Water Wonder/PDF links.


## v21 — Book-Derived Leadership Tools
- Added Book-Derived Leadership Tools section to `career-os.html`.
- Added Book Tool 001: Confidence as Action System.
- Added 10 leadership clusters, 5 workplace tools, 30-day practice plan, one-page readiness report, and safe CV/LinkedIn wording.
- Updated homepage Career-OS section with Book Tool 001 card.
- Added `CLAUDE_FABLE_V21_BOOK_TOOLS_PROMPT.md` for final polish only.


## v24 — Book Tool 004: Negotiation Empathy Framework
- Added Book Tool 004 under Book-Derived Leadership Tools.
- Converted Never Split the Difference extraction into a workplace leadership toolkit: listening, mirroring, neutral labeling, calibrated questions, execution confirmation, communication style awareness, risk clarification, and unknowns discovery.
- Reorganized Book Tools 001–004 into one coherent section flow in career-os.html.
- Updated homepage Book Tools teaser to include negotiation-empathy tools.
- Added Claude Fable final-polish prompt for v24.
- Preserved static HTML/CSS/JS structure, Water Wonder links, PDFs, and contact emails.


## v25 — Book Tool 005: Operational Resilience
- Added Book Tool 005 under Book-Derived Leadership Tools.
- Converted Everyday Resilience extraction into operational leadership tools: incident reframing, purposeful pause, escalation decompression, daily intention tracking, feedback scorecard, and capacity boundaries.
- Updated homepage Book Tools teaser to include resilience.
- Added Claude final-polish prompt for v25.


## v26 — Book Tool 006: Performance Alignment OS
- Added Book Tool 006 under Book-Derived Leadership Tools.
- Converted High Performance Planner extraction into daily alignment and professional habit tools: priorities, risk anticipation, team connection, energy/focus, daily retrospective, weekly reframe, and scorecards.
- Updated homepage Book Tools teaser to include performance alignment.
- Added Claude final-polish prompt for v26.
## v27 — Book Tool 007 · Operational Time & Priority Architect

- Added Book Tool 007 under Book-Derived Leadership Tools.
- Source extraction: The Full Life Planner 2021 / Lifehack.
- Added tools for operational opportunity transformation, critical scope filtering, weekly time-budget allocation, daily five focus, and weekly operational review.
- Updated homepage Book Tools summary from 001–006 to 001–007.
- Added Claude final-polish prompt for v27.
- Preserved static HTML/CSS/JS structure and existing PDFs/Water Wonder content.



## v28 — Book Tool 008: Full Focus Planner Leadership Tools
- Added Book Tool 008 to `career-os.html`: Full Focus Planner Leadership Tools.
- Added SMARTER goal card, Daily Big 3, Leader Weekly Review, Ideal Week, Workday Rituals, AAR, and Quarterly Review logic.
- Updated homepage Book Tools count from 001–007 to 001–008.
- Added Claude final-polish prompt: `CLAUDE_FABLE_V28_BOOK_TOOL_008_PROMPT.md`.
- Preserved static HTML/CSS/JS structure and existing Water Wonder assets.


## v29 — Book Tool 009 Intentional Leadership Routine
- Added Book Tool 009 derived from Live Intentionally: quarterly mission card, junk task audit, first 30 minutes, weekly pattern log, reframe sheet, direct feedback protocol, daily review, book-to-tool extraction, and values clarity.
- Updated index and Career-OS copy to show Book Tools 001–009.
- Added CLAUDE_FABLE_V29_BOOK_TOOL_009_PROMPT.md for final polish.


## v30 — Book Tool 010 Cognitive Reserve & Technical Memory OS
- Added Book Tool 010 derived from The Neuroscience of Memory: attention management, WOPR technical onboarding, cognitive reserve matrix, crisis decision sheet, retrieval testing, and peer review.
- Updated index and Career-OS copy to show Book Tools 001–010.
- Added CLAUDE_FABLE_V30_BOOK_TOOL_010_PROMPT.md for final polish.


## v31 — Wisdom of the Day

- Added `wisdom-of-day.html` as a static Daily Wisdom Agent.
- Added 60 original daily practice cards organized into Right Attitude, Right Practice, and Right Understanding.
- Added homepage and Career-OS links to Wisdom of the Day.
- Added a Career-OS bridge card near Book-Derived Leadership Tools.
- Updated sitemap with the new page.
- Preserved Water Wonder, PDFs, Book Tools 001-010, and contact emails.
- No copied book passages, no personal context, no confidential data, and no career-outcome guarantees.


## v34 — Mobile Experience Polish

- Enhanced mobile-first responsiveness across all pages: increased line-height to 2.0 for Arabic readability, adjusted section paddings, larger buttons/touch targets, improved card spacing in Book Tools and long modules.
- Refined navigation menu on mobile for easier tapping; better responsive grid fallbacks for Year Wheel month cards and Life Calendar forms.
- Improved typography scaling, focus states, and breathing room in Career-OS, Wisdom, Calendar, Wheel pages.
- Verified no horizontal overflow, preserved all content/JS functionality, static only.
- Updated styles.css and verified deployment readiness.

## v32 — Life Operating Calendar & Early Protection Radar
- Added `life-operating-calendar.html` as a static daily/weekly operating calendar.
- Added Daily Operating Card: mission, Big 3 outputs, importance matrix, life requirements.
- Added Early Protection Radar: sleep, food, stress, movement/pain, symptoms, medications/supplements, labs, red flags.
- Added copy/save/clear local browser tools; no external data transfer.
- Added navigation links from homepage, Career-OS, and Wisdom of the Day.
- Updated sitemap and added Claude final-polish prompt.
- Preserved Water Wonder, Book Tools 001-010, Wisdom of the Day, PDFs, and contact emails.


## v33 — Year Operating Wheel
- Added `year-operating-wheel.html` as a circular annual operating calendar.
- Connected year → quarter → month → week → day with monthly review cards, daily input axes, and early-protection red flags.
- Added navigation links from homepage, Career-OS, Life Operating Calendar, Wisdom page, and sitemap.
- Preserved Water Wonder, Book Tools 001–010, Wisdom of the Day, PDF assets, and contact emails.
- Static HTML/CSS/JS only; no external libraries for the wheel module.
