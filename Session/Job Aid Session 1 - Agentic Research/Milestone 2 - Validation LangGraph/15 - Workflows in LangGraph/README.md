# 15 — Workflows in LangGraph  *(Hands-On — 15 min)*

Wires every Milestone 1 + Milestone 2 agent into one end-to-end LangGraph. Enter a company name, get a staged row.

## Files

| File | What it does |
|------|--------------|
| `graph.py` | Builds the graph. Nodes: `researcher`, `consolidator`, `validator`, `cleaner`, `etl`. |
| `tracing_guide.md` | How to enable LangSmith and what to look at. |
| `run.py` | CLI: `python run.py --company "Fractal"`. |

## Run it

```bash
cd "Job Aid Session 1 - Agentic Research/Milestone 2 - Validation LangGraph/15 - Workflows in LangGraph"
python run.py --company "Fractal"
```

## Expected flow

1. `researcher` node calls 3 providers → 3 CompanyCore candidates.
2. `consolidator` node calls OpenRouter → 1 Golden Record.
3. `validator` node runs Pydantic + semantic checks.
4. If invalid, `cleaner` node asks the LLM to fix specific errors → back to `validator` (bounded to 3 passes).
5. Once valid, `etl` node stages the row. Trigger migrates downstream.

## LangSmith

Set these 3 env vars (see `tracing_guide.md`) and every node appears on the LangSmith dashboard with timings + tokens.

## Skill-Set and Hiring flows

Kept as **commented branches** in `graph.py`. The same pattern (`researcher → validator → cleaner → etl`) applies, just swap the node functions. Left as an extension so the demo finishes within the 15-minute slot.
