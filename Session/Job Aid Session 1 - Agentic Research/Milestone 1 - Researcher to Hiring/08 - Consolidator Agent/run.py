"""CLI runner for the Consolidator agent.

Reads `07 - Researcher Agent/outputs/<company>/{provider}.json`, runs the
Consolidator (OpenRouter), writes `outputs/<company>/golden.json`.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_MILESTONE = Path(__file__).resolve().parent.parent
_RESEARCHER = _MILESTONE / "07 - Researcher Agent"
sys.path.insert(0, str(_RESEARCHER))

from schemas import CompanyCore  # noqa: E402

from consolidator_agent import run  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the Consolidator agent.")
    parser.add_argument("--company", required=True, help="Target company name.")
    args = parser.parse_args()

    company = args.company.strip()
    candidate_dir = _RESEARCHER / "outputs" / company

    if not candidate_dir.exists():
        raise SystemExit(
            f"Researcher outputs not found at {candidate_dir}. "
            "Run `07 - Researcher Agent/run.py` first."
        )

    candidates: dict[str, CompanyCore] = {}
    for path in sorted(candidate_dir.glob("*.json")):
        provider = path.stem
        candidates[provider] = CompanyCore.model_validate_json(
            path.read_text(encoding="utf-8")
        )

    print(f"Loaded {len(candidates)} candidates from {candidate_dir}")
    if not candidates:
        raise SystemExit("No candidate JSONs found — did the Researcher run succeed?")

    golden = run(company, candidates)

    out_dir = Path(__file__).resolve().parent / "outputs" / company
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "golden.json"
    target.write_text(
        json.dumps(golden.model_dump(), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"OK → {target.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
