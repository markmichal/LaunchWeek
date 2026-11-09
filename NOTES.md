# LaunchWeek: project notes

The website for Cru High School Launch Weeks: spring break mission trips where people share the gospel with high school students on or near campus. It lists the three trips (San Diego and Tampa, March 14 to 19; Orlando, March 21 to 26). Each location is a photo button that opens that trip's page on campus.cru.org to register.

Live at https://launchweek.crutastic.com (also https://markmichal.github.io/LaunchWeek/). GitHub repo: markmichal/LaunchWeek (public).

## Why Mark built this
From his Projects Hub card: "So students and leaders can find everything for the week without digging through emails." And what he learned: "That I can build a whole site from my phone. I took a picture of a flyer and Claude turned it into this."

It started as a phone-first web version of the Launch Weeks spring break flyer.

## How to use it
- `index.html` is the whole site. Open it in a browser to preview. Photos and icons are mostly baked into the file, which is why it's over 1 MB.
- Publishing: GitHub Pages from the `main` branch, root folder. A push goes live in 1 to 2 minutes (ask Mark before pushing).

## Files
- `index.html`: the page.
- `develop yourself.png`, `experience ministry.png`, `make a difference.png`: the three real Cru icons.
- `Cru_Brandmark_..._White_[RGB] (2).svg`: the official white Cru logo.
- `CNAME`: tells GitHub Pages the address is launchweek.crutastic.com.
- `README.md`: short public description on GitHub. `AGENTS.md`: rules for any AI helper (CLAUDE.md points to it).

## Decisions
- 2026-07-13: Built from Mark's phone as `launch-week.html` inside the cru-hs-60th repo, then moved to this repo as `index.html` with its own domain. The copy in cru-hs-60th was deleted so only one exists.
- 2026-07-13: The three locations are tappable photo buttons that link to each trip's page. The flyer's QR code and generic register button were dropped (the location buttons do that job on a phone).
- 2026-07-13: Real Cru icon files and the official white Cru SVG logo replaced the stand-ins. Mark chose the "bigger visual impact" look: full-width hero with the headline over the photo, scroll reveals, subtle motion.
- 2026-07-13: Display text in sentence case per Cru branding (kicker stays uppercase). Intro split into three short paragraphs, em dashes replaced with commas. Registration opens Sept 1, 2026.
- 2026-08-12: Orlando dates set to March 21 to 26.

## Ideas for later
None written down yet.

## History
- 2026-07-13: Built and published (first inside cru-hs-60th, then moved here the same day). Real icons, logo and new hero added.
- 2026-08-12: Orlando dates updated.
- 2026-11-09: Project kit added (AGENTS.md, NOTES.md, save points, backup to Drive).
