"""CLI runner for the Skill Set agent."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from skill_set_agent import run


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the Skill Set agent.")
    parser.add_argument("--company", required=True, help="Target company name.")
    args = parser.parse_args()

    company = args.company.strip()
    response = run(company)

    out_dir = Path(__file__).resolve().parent / "outputs" / company
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "skills.json"
    target.write_text(
        json.dumps(response.model_dump(), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"OK → {target.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
