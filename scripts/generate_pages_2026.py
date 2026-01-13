#!/usr/bin/env python3
from __future__ import annotations

from datetime import date, timedelta
from pathlib import Path

YEAR = 2026
WEEK_START = 0  # 0=Monday, 6=Sunday

OUTPUT = Path(__file__).resolve().parents[1] / "pages_2026.tex"


def format_date(d: date) -> str:
    return f"{d.strftime('%a')}, {d.strftime('%b')} {d.day}, {d.year}"


def iter_dates(start: date, end: date):
    current = start
    while current <= end:
        yield current
        current += timedelta(days=1)


def iter_week_starts(start: date, year: int):
    current = start
    while current.weekday() != WEEK_START:
        current += timedelta(days=1)
    while current.year == year:
        yield current
        current += timedelta(days=7)


def main() -> None:
    start = date(YEAR, 1, 1)
    end = date(YEAR, 12, 31)

    lines = []
    dates = list(iter_dates(start, end))
    for idx, d in enumerate(dates):
        label = format_date(d)
        lines.append(f"\\MorningPage{{{label}}}")
        lines.append("\\newpage")
        lines.append(f"\\EveningPage{{{label}}}")
        if idx < len(dates) - 1:
            lines.append("\\newpage")

    weeks = list(iter_week_starts(start, YEAR))
    if weeks:
        lines.append("\\newpage")
    for idx, d in enumerate(weeks):
        label = format_date(d)
        lines.append(f"\\WeeklyPage{{{label}}}")
        if idx < len(weeks) - 1:
            lines.append("\\newpage")

    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
