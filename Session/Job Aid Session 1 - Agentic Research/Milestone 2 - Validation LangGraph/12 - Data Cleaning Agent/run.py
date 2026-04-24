"""CLI smoke runner for the Cleaning agent."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "11 - Data Validation Agent"))

from validator_agent import validate  # noqa: E402

from cleaner_agent import clean  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Clean an invalid M1 JSON payload.")
    parser.add_argument("--kind", required=True, choices=("company", "skills", "hiring"))
    parser.add_argument("--payload", required=True, help="Path to JSON file.")
    args = parser.parse_args()

    data = json.loads(Path(args.payload).read_text(encoding="utf-8"))
    ok, errors = validate(args.kind, data)
    if ok:
        print("Payload is already valid — nothing to clean.")
        return

    print("Errors detected — invoking Cleaner:")
    for err in errors:
        print(f"  • {err}")

    cleaned = clean(args.kind, data, errors)
    ok_again, errors_again = validate(args.kind, cleaned)
    print("\nCleaned payload:")
    print(json.dumps(cleaned, indent=2, ensure_ascii=False))
    print("\nRe-validation:", "VALID" if ok_again else f"STILL INVALID: {errors_again}")


if __name__ == "__main__":
    main()
