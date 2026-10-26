# wellkeptdesk.github.io
Small widgets used in WellKeptDesk Notion templates.

## v1 widgets added in this branch

| Widget | URL | Parameters |
|---|---|---|
| Habit | `/v1/habit/` | `label`, `goal` (days per week, 1-7). Taps are saved in the browser on this device. |
| Water | `/v1/water/` | `goal` (default 8), `unit`. Resets each day, saved on this device. |
| Life in years | `/v1/life/` | `born=YYYY-MM-DD`, `years` (default 80). |
| Breathe | `/v1/breathe/` | `pattern=in-hold-out-hold` in seconds (default 4-4-4-4), `label`. |
| Chart | `/v1/chart/` | `d=1,2,3` (required), `type=bar\|line\|ring`, `labels=M,T,W`, `goal`, `unit`, `title`. |

All widgets accept `theme=light|dark`. Embeds cannot read Notion data, so the chart widget shows the numbers in its URL.
