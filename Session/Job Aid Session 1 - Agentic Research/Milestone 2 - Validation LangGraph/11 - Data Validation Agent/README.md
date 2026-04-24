# 11 — Data Validation Agent  *(Hands-On — 5 min)*

A **pure-Python function**, not an LLM call. Takes any of the Milestone 1 payloads and returns `(is_valid, errors)`.

It combines:

1. **Pydantic gate** — re-parses the payload with the matching schema.
2. **Semantic checks** — business rules the schema can't express (e.g. no "TBD" in `vision_statement`, `incorporation_year` within `1800..current_year`, skill levels don't all cluster on the same value).

If either fails, the caller (Cleaning agent / LangGraph) can retry with feedback.

## Files

| File | What it does |
|------|--------------|
| `validator_agent.py` | `validate_company_core`, `validate_skill_sets`, `validate_hiring_process`, `validate(kind, payload)`. |
| `run.py` | CLI smoke check: loads saved JSONs from M1 and prints validity. |

## Run it

```bash
cd "Job Aid Session 1 - Agentic Research/Milestone 2 - Validation LangGraph/11 - Data Validation Agent"
python run.py --kind company --payload "../../Milestone 1 - Researcher to Hiring/08 - Consolidator Agent/outputs/Fractal/golden.json"
```

## Why this is "one" agent per the spec

The user's brief: *"Data validation, data cleaning, ETL — these three can be one single agent."* Here we keep them as **three files** for pedagogy but they share a single module and can be collapsed into one class in production. The LangGraph in step 15 wires them as three nodes.
