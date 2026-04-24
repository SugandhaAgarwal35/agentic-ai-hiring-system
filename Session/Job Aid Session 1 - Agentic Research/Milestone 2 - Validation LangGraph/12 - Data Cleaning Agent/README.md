# 12 — Data Cleaning Agent  *(Hands-On — 5 min)*

Takes a **broken payload** plus the list of errors the Validation agent produced, and asks the LLM to return a **fixed payload** — only the broken fields touched.

This is the **retry-with-feedback** step. Plain `run_with_retry` just re-invokes the same prompt; the Cleaning agent steers the LLM with the specific errors.

## Files

| File | What it does |
|------|--------------|
| `cleaner_agent.py` | `clean(kind, payload, errors)` → dict (possibly still invalid; caller re-validates). |
| `run.py` | CLI smoke: loads a JSON, validates, if invalid calls the cleaner, prints the result. |

## Run it

```bash
cd "Job Aid Session 1 - Agentic Research/Milestone 2 - Validation LangGraph/12 - Data Cleaning Agent"
python run.py --kind company --payload "../../Milestone 1 - Researcher to Hiring/08 - Consolidator Agent/outputs/Fractal/golden.json"
```

A sample `fixtures/bad_golden.json` can be any golden record with `incorporation_year: "1500"` or `vision_statement: "TBD"` to trigger the validator.

## Key concept

> The Validator tells the Cleaner **what** is broken. The Cleaner tells the LLM **how** to fix it. The LLM stays focused on broken fields instead of hallucinating new ones.
