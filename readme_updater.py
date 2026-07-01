#!/usr/bin/env python3
"""Update README progress counters from the markdown progress table."""

from __future__ import annotations

import argparse
import re
from collections import Counter, defaultdict
from pathlib import Path


PROBLEM_COUNTER_RE = re.compile(r"^Problem counter:\s*\d+\s+Problems\s*$", re.MULTILINE)

DIFFICULTY_BLOCK_RE = re.compile(
    r"```mermaid\n"
    r"pie title Problems by Difficulty\n"
    r"(?:.*\n)*?"
    r"```",
    re.MULTILINE,
)

PER_DAY_BLOCK_RE = re.compile(
    r"```mermaid\n"
    r"pie title Problems Solved in a Day\n"
    r"(?:.*\n)*?"
    r"```",
    re.MULTILINE,
)


def parse_progress_table(readme_text: str) -> tuple[int, Counter[str], dict[int, int]]:
    lines = readme_text.splitlines()

    data_rows: list[list[str]] = []
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        if set(stripped.replace("|", "").strip()) <= {"-", ":", " "}:
            continue

        cols = [col.strip() for col in stripped.strip("|").split("|")]
        if len(cols) < 4:
            continue

        # Skip header row if present.
        if cols[0].lower() == "sr no" and cols[1].lower() == "day":
            continue

        data_rows.append(cols)

    difficulty_counts: Counter[str] = Counter()
    day_counts: dict[int, int] = defaultdict(int)

    total_problems = 0
    current_day: int | None = None

    for cols in data_rows:
        day_text = cols[1].strip()
        difficulty = cols[3].strip().lower()

        if day_text:
            digits = re.search(r"\d+", day_text)
            if digits:
                current_day = int(digits.group())

        total_problems += 1
        if difficulty in {"easy", "medium", "hard"}:
            difficulty_counts[difficulty] += 1

        if current_day is not None:
            day_counts[current_day] += 1

    return total_problems, difficulty_counts, dict(day_counts)


def build_difficulty_block(counts: Counter[str]) -> str:
    return (
        "```mermaid\n"
        "pie title Problems by Difficulty\n"
        f'    "Easy" : {counts.get("easy", 0)}\n'
        f'    "Medium" : {counts.get("medium", 0)}\n'
        f'    "Hard" : {counts.get("hard", 0)}\n'
        "```"
    )


def build_per_day_block(day_counts: dict[int, int]) -> str:
    one = sum(1 for c in day_counts.values() if c == 1)
    two = sum(1 for c in day_counts.values() if c == 2)
    three_plus = sum(1 for c in day_counts.values() if c >= 3)

    return (
        "```mermaid\n"
        "pie title Problems Solved in a Day\n"
        f'    "One" : {one}\n'
        f'    "Two" : {two}\n'
        f'    "Three+" : {three_plus}\n'
        "```"
    )


def update_readme(path: Path) -> None:
    original = path.read_text(encoding="utf-8")

    total, difficulty_counts, day_counts = parse_progress_table(original)

    updated = PROBLEM_COUNTER_RE.sub(f"Problem counter: {total} Problems", original, count=1)

    difficulty_block = build_difficulty_block(difficulty_counts)
    updated = DIFFICULTY_BLOCK_RE.sub(difficulty_block, updated, count=1)

    per_day_block = build_per_day_block(day_counts)
    updated = PER_DAY_BLOCK_RE.sub(per_day_block, updated, count=1)

    if updated == original:
        print("No changes made. Counters already match parsed table data.")
        return

    path.write_text(updated, encoding="utf-8")

    one = sum(1 for c in day_counts.values() if c == 1)
    two = sum(1 for c in day_counts.values() if c == 2)
    three_plus = sum(1 for c in day_counts.values() if c >= 3)

    print(f"Updated {path}")
    print(f"Problem counter: {total}")
    print(
        "Difficulty counts: "
        f"Easy={difficulty_counts.get('easy', 0)}, "
        f"Medium={difficulty_counts.get('medium', 0)}, "
        f"Hard={difficulty_counts.get('hard', 0)}"
    )
    print(f"Problems solved/day: One={one}, Two={two}, Three+={three_plus}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Update README counters from the existing progress table."
    )
    parser.add_argument(
        "--readme",
        type=Path,
        default=Path("readme.md"),
        help="Path to the README file (default: readme.md)",
    )
    args = parser.parse_args()

    if not args.readme.exists():
        raise FileNotFoundError(f"README file not found: {args.readme}")

    update_readme(args.readme)


if __name__ == "__main__":
    main()
