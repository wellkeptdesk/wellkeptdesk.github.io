# wellkeptdesk.github.io
Small widgets used in WellKeptDesk Notion templates.

## More v1 widgets

| Widget | URL | Parameters |
|---|---|---|
| Habit | `/v1/habit/` | `label`, `goal` (days per week, 1-7). Taps are saved in the browser on this device. |
| Water | `/v1/water/` | `goal` (default 8), `unit`. Resets each day, saved on this device. |
| Life in years | `/v1/life/` | `born=YYYY-MM-DD`, `years` (default 80). |
| Breathe | `/v1/breathe/` | `pattern=in-hold-out-hold` in seconds (default 4-4-4-4), `label`. |
| Chart | `/v1/chart/` | `d=1,2,3` (required), `type=bar\|line\|ring`, `labels=M,T,W`, `goal`, `unit`, `title`. |

All widgets accept `theme=light|dark`. Embeds cannot read Notion data, so the chart widget shows the numbers in its URL.

## Life OS widgets (v1)

Every widget takes `theme=light|dark` (default follows the system). Data a widget saves stays in the viewer's own browser (localStorage); nothing is sent anywhere.

| Widget | URL | Options |
| --- | --- | --- |
| Ritual checklist, resets daily | `/v1/ritual/` | `title`, `items` (comma separated, up to 8) |
| Mood check-in + last 7 days | `/v1/mood/` | none |
| Day timeline with a "now" line | `/v1/timeline/` | `blocks` like `7-9 Morning,9-12 Deep work,12:30-13 Lunch` |
| Savings jar | `/v1/jar/` | `label`, `goal`, `saved` (start value), `step`, `currency` |
| Sticky note | `/v1/note/` | `title`, `hint`, `daily=1` for a fresh note each day |

## Hosting on Cloudflare Pages

The repo is plain static files, so Cloudflare Pages serves it as is:
Workers & Pages > Create > Pages > Connect to Git > this repo, framework preset **None**, build command empty, output directory `/`.
`_headers` allows the widgets to be embedded (Notion uses iframes) and sets cache times.
Put a custom domain in front (for example `widgets.<your-domain>`) so the URLs inside sold templates never depend on the host.
