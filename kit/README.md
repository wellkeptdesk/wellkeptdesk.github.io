# WellKeptDesk widgets

Quiet, self-hosted widgets for Notion pages: clock, desk (clock + date + payday), greeting, almanac (week, day of the year, moon), month calendar, week strip, countdown, year/month/week/day progress, progress rings, analog clock, moon phase, quote of the day and a focus timer.

- Preview and copy links: open `index.html` on this site.
- Settings go after `#` in the link (`palette`, `theme`, `style` and each widget's own options), so they never reach a server.
- No tracking, no cookies, no external requests. Fonts are served from this repository.

## Embed in Notion
1. Copy a widget link, e.g. `https://<this-site>/clock.html#palette=olive&theme=auto`.
2. In Notion, paste it and choose **Create embed**.
3. Set the embed height (see `index.html`; the clock needs about 90 px).
4. Use `theme=auto` to follow Notion's light or dark theme (tested in Chrome and the Notion desktop app). If a browser shows a solid box behind the widget, set `theme=dark` or `theme=light` to match Notion.

## Editorial layouts
- `greeting.html#layout=masthead&note=...`: a small kicker with the greeting and date, a hairline and one italic line.
- `clock.html#layout=corner&align=right`: a serif clock with the week and day of the year.
- `almanac.html`: this week's days, week number, day of the year, moon phase and a year line.
- `pomodoro.html#layout=session&label=Session`: a quiet reading or focus session timer.
- `quote.html#set=shelf&size=large`: a pull quote from public-domain classics.
- Palettes `ink`, `fern` and `oxblood` keep secondary text neutral and use one accent.

## Licence
- Widget code and design: © WellKeptDesk. All rights reserved. Free to embed in WellKeptDesk templates; not licensed for redistribution or resale.
- Fonts (Inter, Source Serif 4, Cormorant Garamond, IBM Plex Mono): SIL Open Font License 1.1. Licence texts are in `fonts/`.
