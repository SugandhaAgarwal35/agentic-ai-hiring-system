"""CLI smoke check for the Validation agent."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from validator_agent import validate


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate an M1 JSON payload.")
    parser.add_argument("--kind", required=True, choices=("company", "skills", "hiring"))
    parser.add_argument("--payload", required=True, help="Path to the JSON file to validate.")
    args = parser.parse_args()

    data = json.loads(Path(args.payload).read_text(encoding="utf-8"))
    ok, errors = validate(args.kind, data)

    if ok:
        print(f"[{args.kind}] VALID — {args.payload}")
    else:
        print(f"[{args.kind}] INVALID — {args.payload}")
        for err in errors:
            print(f"  • {err}")


if __name__ == "__main__":
    main()
