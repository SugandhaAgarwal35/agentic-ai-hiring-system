# 07 — Researcher Agent  *(Hands-On — 5 min)*

Runs the **same Researcher prompt** through **3 different providers** and returns 3 validated `CompanyCore` JSONs. The 3 JSONs are saved under `outputs/` so the next step (Consolidator) can read them.

## Files

| File | What it does |
|------|--------------|
| `schemas.py` | Pydantic `CompanyCore` — all 163 `staging_company` fields (10 strict core + 153 optional extended). |
| `researcher_agent.py` | `run(company)` → dict keyed by `"groq" / "google" / "cerebras"`. |
| `run.py` | CLI wrapper: writes `outputs/<company>/{provider}.json`. |

## Run it

```bash
cd "Job Aid Session 1 - Agentic Research/Milestone 1 - Researcher to Hiring/07 - Researcher Agent"
python run.py --company "Fractal"
```

Expected console output:

```
[groq]     OK → outputs/Fractal/groq.json
[google]   OK → outputs/Fractal/google.json
[cerebras] OK → outputs/Fractal/cerebras.json
```

## What to demo

- Open the 3 saved JSONs side-by-side. Compare the `vision_statement` and `overview_text` — the wording differs but the schema is identical.
- Force a failure: in `.env`, temporarily blank `GROQ_API_KEY`. Re-run. The Groq call fails, `run_with_retry` burns through 3 attempts, the whole call raises `AgentRetryExhausted`. Restore the key and re-run — green again.

## Key concept

> **Same prompt × multiple providers = free triangulation.** One provider might say Fractal was founded in 2000, another 2001. The Consolidator (step 08) breaks the tie.
