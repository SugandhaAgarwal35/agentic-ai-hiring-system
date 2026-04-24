# 08 — Consolidator Agent  *(Hands-On — 5 min)*

Reads the 3 JSONs the Researcher wrote in step 07 and asks a **4th provider** (OpenRouter) to cherry-pick the best value per field. Returns **one** validated `CompanyCore` — the "Golden Record".

## Files

| File | What it does |
|------|--------------|
| `consolidator_agent.py` | `run(company, candidates_by_provider)` → `CompanyCore`. |
| `run.py` | CLI: loads `07 - Researcher Agent/outputs/<company>/*.json`, runs consolidation, writes `outputs/<company>/golden.json`. |

The Pydantic `CompanyCore` is re-used from step 07 via `sys.path` insert — no duplication.

## Run it

```bash
# Make sure step 07 has produced the 3 input JSONs first:
cd "../07 - Researcher Agent" && python run.py --company "Fractal"

cd "../08 - Consolidator Agent"
python run.py --company "Fractal"
```

Expected console output:

```
Loaded 3 candidates from ../07 - Researcher Agent/outputs/Fractal
OK → outputs/Fractal/golden.json
```

## What to demo

1. Open `07/outputs/Fractal/groq.json`, `google.json`, `cerebras.json`, and the new `08/outputs/Fractal/golden.json` side-by-side.
2. Ask the class "whose `overview_text` won?" The model usually picks the most detailed of the three.
3. Force a failure: blank one candidate's `overview_text` field to `"Not Found"`. Re-run — the Consolidator skips that candidate for that field (per the zero-fabrication selection rules).

## Key concept

> The Consolidator uses a **different provider family** than the three Researchers. That independence is the whole point — if we let Groq consolidate Groq's own answer, we'd bias toward Groq.
