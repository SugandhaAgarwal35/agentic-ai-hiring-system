"""End-to-end LangGraph runner."""

from __future__ import annotations

import argparse
import json

from graph import build_graph


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the full LangGraph flow.")
    parser.add_argument("--company", required=True)
    args = parser.parse_args()

    graph = build_graph()
    final_state = graph.invoke({"company": args.company.strip()})

    print("=== Final Golden Record ===")
    print(json.dumps(final_state["golden"], indent=2, ensure_ascii=False))
    print("\n=== Staged Rows ===")
    print(json.dumps(final_state["staged_rows"], indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
