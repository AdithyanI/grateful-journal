# Grateful Journal (Kindle Scribe)

A clean, calm, minimalist gratefulness journal built for Kindle Scribe. It is sized to the Scribe’s native 6.2in × 8.2667in (300 ppi) canvas and prefilled with every date in 2026. Each day has a **Morning** page and an **Evening** page, plus weekly reflection pages. The layout is intentionally light, with subtle guides and gentle separators so the writing stays the focus.

## What this includes

Daily structure is consistent and simple:

**Morning page**
- Date header + Sleep / Energy / Mood ratings
- Grateful for (3 items)
- Today will be a win if (2 lines)
- One priority (2 lines)
- How I’ll show up today (2 lines)

**Evening page**
- Date header + Mood / Energy ratings
- 3 good things that happened (3 items)
- Why they happened / what I did right (2 lines)
- One adjustment for tomorrow (2 lines)

**Weekly page**
- Week of
- 3 highlights
- What worked
- One improvement
- Intention for next week

## Files
- `grateful_journal.pdf` — ready to load on Kindle Scribe
- `grateful_journal.tex` — LaTeX source
- `pages_2026.tex` — auto-generated dated pages
- `scripts/generate_pages_2026.py` — date page generator
- `scripts/build.sh` — one-command build (recommended)

## Build (recommended)

```bash
./scripts/build.sh
```

Output: `grateful_journal.pdf`

## Customize

You can change the year, weekly start day, spacing, and even page size.

**Dates**
- Edit `scripts/generate_pages_2026.py` to change `YEAR` and `WEEK_START`
- Then run `./scripts/build.sh` again

**Layout + spacing**
- Open `grateful_journal.tex`
- Adjust line spacing with `\WriteLines` and `\WriteNumberedLines`
- Adjust margins in the `geometry` block

**Device size**
- Change `paperwidth` and `paperheight` in `grateful_journal.tex`
- Rebuild with `./scripts/build.sh`

This template is meant to be a starting point. Make it yours and keep it simple.
