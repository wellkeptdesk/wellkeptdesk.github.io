# Widgets design system (wellkeptdesk.github.io)

Small embeddable widgets for Notion templates. Opt-in `?palette=graphite` (light/dark via `?theme`).

## Graphite palette
Graphite #4A4F53, Fog #B9BDBE, Chalk #E3E5E3, Paper #FBFBFA, ink #2A2D30, muted #686D70 (AA contrast on white). Single accent Signal #D8532B lives Notion-side.

## Rules
- System sans stack, tabular digits for time. Micro labels uppercase, 10-11px, muted.
- Flat surfaces, no gradients; soft tile shadow only on the clock.
- Local-storage only, no tracking.
- Transparent body so widgets read on Notion light and dark pages.
- Known gaps: quote photo still beige; no aria labels on clock/calendar.
