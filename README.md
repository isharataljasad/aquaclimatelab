# AquaClimate Lab

**Water × Weather × Chemistry × Data — for arid-region thinking.**

A fast, static, dependency-free knowledge prototype connecting three tracks under one theme:

- **Water & Climate** — hydrology, weather, climate, drought, groundwater, arid-region water systems.
- **Chemistry & Industry** — water quality, pH, TDS, salinity, hardness, treatment, materials.
- **Data Science & AI** — Python, SQL, GIS, dashboards, environmental data, machine learning, AI-assisted analysis.
- **Educational learning sections** — Water Data Explorer (8 indicators), Hydrology Signals (8 concepts), a Chemistry × Hydrology flow map, an interactive Mini Dataset Demo (5 fictional samples), and Water Wonder Questions.
- **Smart Fertigation** — controlled-release nutrients, precision fertigation, soil/EC/pH sensors, and AI decision support at the root zone. (Its feature image is embedded directly in `index.html` as a data URI, so it always renders — there is no separate image file to deploy.)

From Arizona to Saudi Arabia, the site explains how water, weather, chemistry, and data science connect in dry environments.

---

## Tech

Plain **HTML + CSS + JavaScript**. No React, no build step, no Node, no external fonts, no tracking, no third-party requests. It deploys as a static site anywhere.

```
aquaclimate-lab/
├── index.html              # single-page site
├── 404.html                # custom not-found page
├── robots.txt              # crawl rules + sitemap pointer
├── sitemap.xml             # single-URL sitemap
├── vercel.json             # clean URLs + security & cache headers
├── manifest.webmanifest    # PWA manifest
├── README.md
├── CHANGELOG.md
└── assets/
    ├── css/styles.css      # full dark "research console" theme
    ├── js/main.js          # nav, year, interactive demo
    └── img/
        ├── favicon.svg
        ├── og-image.svg    # editable source for the social card
        └── og-image.png    # 1200×630 Open Graph / Twitter image
```

---

## Deploy on Vercel

1. Create a GitHub repository and upload **the contents of this folder to the repo root** (so `index.html` is at the top level).
2. In Vercel: **Add New → Project → Import** the GitHub repo.
3. **Framework Preset:** `Other`.
4. **Build Command:** leave empty.
5. **Output Directory:** leave empty (or `.`).
6. **Deploy.**
7. Add the custom domain `aquaclimatelab.com` under **Project → Settings → Domains** and point DNS as Vercel instructs.

`cleanUrls` is enabled, so pages resolve without the `.html` extension. `404.html` is served automatically for unknown paths.

> Drag-and-drop also works: zip the folder contents and drop them into a new Vercel project, or use the Vercel CLI (`vercel --prod`).

---

## Before publishing — checklist

- [x] Public contact emails are set to `jumanajuh@gmail.com`, `renadsuf2002@gmail.com`, `yarasuf2001@gmail.com`, and `wejdanphy99@gmail.com`.
- [ ] Replace the three **profile placeholders** (Water & Climate / Chemistry & Industry / Data Science & AI) with real role descriptions, and swap the `Coming soon` LinkedIn labels for real URLs when ready.
- [ ] Confirm the domain is `aquaclimatelab.com` in `robots.txt`, `sitemap.xml`, and the metadata in `index.html` (already set).
- [ ] Optionally regenerate `assets/img/og-image.png` from `og-image.svg` after any branding change.

---

## Change log

See **[CHANGELOG.md](CHANGELOG.md)** for the full list of improvements made in this revision.

---

## Safety note

This site is an **independent educational and portfolio prototype**. It does **not** provide engineering, environmental, health, laboratory, or regulatory advice, and it does **not** represent any employer, university, or government entity. No company logos, internal data, or non-public projects are included. Mention professional backgrounds only in safe, general language.


### Water Wonder article
This build includes a practical Arabic article: `water-without-fear.html` — a consumer-facing guide on choosing water, bottles, filters, official warnings, water testing, and treated water without fear marketing or commercial endorsement.


## PDF attachment

The 12-slide Arabic PDF is included at `assets/docs/water-as-body-operating-system-12-slides.pdf` and linked from the homepage Water Wonder section and the article page.

## PDF deployment fix

The 12-slide PDF is now stored in two deployment-safe locations:

- `/water-as-body-operating-system-12-slides.pdf`  ← primary link used by buttons
- `/assets/docs/water-as-body-operating-system-12-slides.pdf` ← backup copy

A helper page is also included:

- `/download-water-wonder-pdf.html`

After uploading to GitHub/Vercel, test this direct URL first:

`https://www.aquaclimatelab.com/water-as-body-operating-system-12-slides.pdf`

If it returns 404, the PDF file was not committed/uploaded to the deployed repository.

## Career-OS update

This build adds a new career-development layer:

- Homepage section: `#career-os`
- New page: `career-os.html`
- Claude continuation prompt: `CLAUDE_CAREER_OS_PROMPT.md`

Career-OS focuses on hydrology and chemistry career growth through:
simulation practice, mini-projects, CV-ready statements, management reporting, career evidence portfolios, and work-health discipline.

## Career-OS v15 decision update

The Career-OS page has been changed from broad examples into selected career decisions:

- Hydrology: MODFLOW 6 + QGIS + NASA ARSET
- Chemistry: Aspen Plus + Minitab + ISO/IEC 17025
- Water chemistry bridge: PHREEQC after foundations
- Team lead readiness: ISO 14001 + ISO/IEC 17025 + CAPM/PMP by eligibility + NEBOSH IGC

The language avoids promising a specific career outcome. It focuses on leadership readiness evidence, measurable work outputs, and safe educational projects.
