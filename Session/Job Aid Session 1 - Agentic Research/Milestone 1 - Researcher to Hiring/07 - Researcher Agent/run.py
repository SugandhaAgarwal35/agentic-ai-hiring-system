"""CLI runner for the Researcher agent.

Writes one JSON file per provider under:
    outputs/<company>/groq.json
    outputs/<company>/google.json
    outputs/<company>/cerebras.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from researcher_agent import run


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the Researcher agent.")
    parser.add_argument("--company", required=True, help="Target company name.")
    args = parser.parse_args()

    company = args.company.strip()
    print(f"Researching: {company!r}")
    print("Providers: groq, google, cerebras (same prompt, 3 calls)\n")

    out_root = Path(__file__).resolve().parent / "outputs" / company
    out_root.mkdir(parents=True, exist_ok=True)

    results = run(company)

    for provider, model in results.items():
        target = out_root / f"{provider}.json"
        target.write_text(
            json.dumps(model.model_dump(), indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        print(f"[{provider:<8}] OK → {target.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
