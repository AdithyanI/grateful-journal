#!/bin/bash
# Build the grateful journal PDF and clean up LaTeX artifacts

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_DIR"

echo "📝 Generating pages_2026.tex..."
python3 scripts/generate_pages_2026.py

echo "📄 Building PDF..."
latexmk -pdf grateful_journal.tex

echo "🧹 Cleaning up build artifacts..."
rm -f grateful_journal.aux grateful_journal.fdb_latexmk grateful_journal.fls grateful_journal.log
rm -f grateful_journal.synctex.gz grateful_journal.toc grateful_journal.out
rm -f grateful_journal.bbl grateful_journal.blg grateful_journal.run.xml

echo "✅ Done! Output: grateful_journal.pdf"
