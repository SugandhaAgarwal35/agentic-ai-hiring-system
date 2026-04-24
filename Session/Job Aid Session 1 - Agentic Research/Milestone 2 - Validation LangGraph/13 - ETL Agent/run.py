"""CLI runner for the ETL agent."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from dotenv import load_dotenv

# Load DATABASE_URL / ETL_WRITE_MODE from the Milestone 1 env file.
_ENV_FILE = (
    Path(__file__).resolve().parent.parent.parent
    / "Milestone 1 - Researcher to Hiring"
    / "05 - Setup Accounts and Env"
    / ".env"
)
if _ENV_FILE.exists():
    load_dotenv(_ENV_FILE)
else:
    load_dotenv()

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "11 - Data Validation Agent"))

from validator_agent import validate  # noqa: E402

from etl_agent import stage  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Stage a validated M1 payload.")
    parser.add_argument("--kind", required=True, choices=("company", "skills", "hiring"))
    parser.add_argument("--payload", required=True, help="Path to the validated JSON.")
    args = parser.parse_args()

    data = json.loads(Path(args.payload).read_text(encoding="utf-8"))

    ok, errors = validate(args.kind, data)
    if not ok:
        raise SystemExit(
            "Refusing to stage an invalid payload:\n  " + "\n  ".join(errors)
        )

    stage(args.kind, data)


if __name__ == "__main__":
    main()
