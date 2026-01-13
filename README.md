# Grateful Journal (Kindle Scribe)

Minimal daily journal template for Kindle Scribe, sized to 6.2in × 8.2667in (300 ppi) and prefilled with 2026 dates.

## Contents
- `grateful_journal.pdf` — ready to load on Kindle Scribe
- `grateful_journal.tex` — source layout
- `pages_2026.tex` — auto-generated dated pages
- `scripts/generate_pages_2026.py` — date page generator

## Build

```bash
python3 scripts/generate_pages_2026.py
latexmk -pdf grateful_journal.tex
```

Output: `grateful_journal.pdf`
