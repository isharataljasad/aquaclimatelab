# Vercel Upload and Live Check Instructions — v44

## Upload method

Upload the contents of the unzipped v44 folder, not the parent folder itself.

At the Vercel project root, these files must be visible:

- `index.html`
- `life-operating-calendar.html`
- `year-operating-wheel.html`
- `career-os.html`
- `search.html`
- `vercel.json`
- `assets/`

Also confirm these fallback folders exist:

- `life-operating-calendar/index.html`
- `year-operating-wheel/index.html`
- `career-os/index.html`
- `search/index.html`

## After deployment

1. Open the newest Vercel deployment preview URL first.
2. Test these before assigning or checking the custom domain:
   - `/life-operating-calendar`
   - `/year-operating-wheel`
   - `/career-os`
   - `/wisdom-of-day`
   - `/water-without-fear`
   - `/search`
3. In DevTools → Network, enable `Disable cache`, reload, and confirm v44 assets load with 200.
4. Then test the custom domain.

## If the Vercel preview works but the custom domain still fails

This is not a code problem inside the ZIP. Check Vercel settings:

1. Confirm `aquaclimatelab.com` and `www.aquaclimatelab.com` point to the same Vercel project.
2. Confirm the custom domain is assigned to the latest deployment, not an older project.
3. In Vercel → Deployments, open the latest deployment and use “Visit” from that deployment.
4. If one domain works and the other fails, fix the domain redirect/canonical domain setting.
5. Purge browser cache or use a fresh incognito window.
6. If still stale, redeploy once with “Clear build cache” if the Vercel UI provides that option.

## Live route check

Both forms should work:

- `/life-operating-calendar`
- `/life-operating-calendar.html`
- `/year-operating-wheel`
- `/year-operating-wheel.html`

If `.html` works but clean URL fails, the issue is rewrites or deployment settings.

If Vercel preview works but production custom domain fails, the issue is custom-domain assignment or stale production deployment.
