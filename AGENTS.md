# LaunchWeek: notes for any AI helper

This file is for whatever AI is helping Mark (Claude today, maybe something else later). Read NOTES.md next: it has why this exists, how it works, the decisions and the history. README.md is the short public front page on GitHub; leave it as it is. Copies of past conversations go in `chats/` (kept on this Mac only, never pushed).

One-page website for Cru High School Launch Weeks (spring break mission trips to reach high school students), live at https://launchweek.crutastic.com. Mark is not a coder: plain words, no em dashes, clickable links.

## Rules
- This repo is public on GitHub, and pushing to `main` publishes the live site. Never push without Mark's OK.
- Anything committed here can end up online, so keep private details (personal info, keys, chat copies) out of every file.
- Follow Cru branding: sentence case for display text (the small kicker label stays uppercase), commas instead of em dashes.

## At the end of every work session
1. Write new decisions into NOTES.md (with the date).
2. Save a copy of the chat: `python3 ~/Projects/project-kit/save-chat.py ~/Projects/LaunchWeek` (`chats/` is in .gitignore, so it stays on this Mac).
3. Make a save point: `git add -A && git commit -m "<what changed and why>"`. Don't push unless Mark says so.
4. Back up: `~/Projects/project-kit/backup-projects.sh ~/Projects/LaunchWeek` (copies only what the save point tracks).
