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
- `media/launch-week.mp4` and `media/launch-week-poster.jpg`: the Launch Week 2026 video and its cover image.
- `develop yourself.png`, `experience ministry.png`, `make a difference.png`: the three real Cru icons.
- `Cru_Brandmark_..._White_[RGB] (2).svg`: the official white Cru logo.
- `print-flyer/`: the printable flyer (two half-page flyers on one landscape 8.5x11 sheet, cut in half). Edit `flyer.html`, then make the PDF with `~/.venvs/playwright/bin/python print-flyer/render.py "$PWD/print-flyer/flyer.html" preview.png flyer.pdf`. The finished PDF is in Drive: CRU > EVENTS & PROJECTS > 2026-2027 > Launch Week.
- `CNAME`: tells GitHub Pages the address is launchweek.crutastic.com.
- `README.md`: short public description on GitHub. `AGENTS.md`: rules for any AI helper (CLAUDE.md points to it).

## Decisions
- 2026-07-13: Built from Mark's phone as `launch-week.html` inside the cru-hs-60th repo, then moved to this repo as `index.html` with its own domain. The copy in cru-hs-60th was deleted so only one exists.
- 2026-07-13: The three locations are tappable photo buttons that link to each trip's page. The flyer's QR code and generic register button were dropped (the location buttons do that job on a phone).
- 2026-07-13: Real Cru icon files and the official white Cru SVG logo replaced the stand-ins. Mark chose the "bigger visual impact" look: full-width hero with the headline over the photo, scroll reveals, subtle motion.
- 2026-07-13: Display text in sentence case per Cru branding (kicker stays uppercase). Intro split into three short paragraphs, em dashes replaced with commas. Registration opens Sept 1, 2026.
- 2026-08-12: Orlando dates set to March 21 to 26.
- 2026-11-18: Kirk Freeman asked for the Launch Week 2026 video (the same one on campus.cru.org/high-school/launchweek). Added a dark "See it for yourself" video section right under the hero, with a big play button, a beach group shot as the cover, and a stats row (57 decisions for Christ, 3 cities, $0). The hero got "Watch the video" and "Choose your trip" buttons. The video was shrunk from 275 MB to 25 MB (720p) and lives in `media/`; it only downloads when someone presses play. `.gitignore` has an exception so this one video can be saved. Built on branch `add-kirk-video`.
- 2026-11-18: Mark OK'd a visual refresh to match the Cru High School Launch Week page (campus.cru.org/high-school/launchweek). New look: black header and footer with the white Cru logo; a yellow box with a teal block behind it over the hero photo; pink "FREE!" tag; pink uppercase section labels; square black buttons; colored offset blocks behind the video and trip photos; pink square icons (the three round blue Cru icon PNGs are no longer used on the page but stay in the folder); a yellow "Cost: Free" band. Sora is now one variable font file (weights 300 to 800) so the light "Launch Weeks" type works. The mockup is Mark's private Claude design canvas "Launch Week site refresh". Built on branch `cru-look-refresh`.

- 2026-11-18: Mark needed the Launch Weeks flyer "2 to a page" for a friend to print and cut. First try was the old Canva flyer shrunk two-up, but it left big white gaps. Mark then asked for a new flyer in the website's style instead: yellow card over the hero photo, the three city photos, the three experience points, a yellow "Cost: Free" band with a QR code to launchweek.crutastic.com, black footer. It uses the website's Orlando dates (March 21 to 26), not the old Canva flyer's (21 to 28). A half-size Canva copy ("LAUNCH WEEKS", 5.5x8.5) was also made along the way and is unused. Mark sent the finished PDF to Kirk.

## Ideas for later
None written down yet.

## History
- 2026-07-13: Built and published (first inside cru-hs-60th, then moved here the same day). Real icons, logo and new hero added.
- 2026-08-12: Orlando dates updated.
- 2026-11-18: Launch Week 2026 video added with a new video section.
- 2026-11-18: Visual refresh to match the Cru High School Launch Week page.
- 2026-11-09: Project kit added (AGENTS.md, NOTES.md, save points, backup to Drive).
