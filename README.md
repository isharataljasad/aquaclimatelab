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

- [x] Public contact email is set to `renadsuf2002@gmail.com`.
- [ ] Replace the three **profile placeholders** (Water & Climate / Chemistry & Industry / Data Science & AI) with real role descriptions, and swap the `Coming soon` LinkedIn labels for real URLs when ready.
- [ ] Confirm the domain is `aquaclimatelab.com` in `robots.txt`, `sitemap.xml`, and the metadata in `index.html` (already set).
- [ ] Optionally regenerate `assets/img/og-image.png` from `og-image.svg` after any branding change.

---

## Change log

See **[CHANGELOG.md](CHANGELOG.md)** for the full list of improvements made in this revision.

---

## Safety note

This site is an **independent educational and portfolio prototype**. It does **not** provide engineering, environmental, health, laboratory, or regulatory advice, and it does **not** represent any employer, university, or government entity. No company logos, internal data, or non-public projects are included. Mention professional backgrounds only in safe, general language.
