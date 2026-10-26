# wellkeptdesk.github.io
Small widgets used in WellKeptDesk Notion templates.

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
