# Job Aid Session 1 — Agentic Research

This session demystifies agentic AI by building five manually-run LangChain agents that research a company, reconcile the outputs, and stream them through a LangGraph workflow.

## Scope

| Milestone | Focus | Items |
|-----------|-------|-------|
| **Milestone 1** | Build 4 research agents, run each manually. | 01 – 10 |
| **Milestone 2** | Validation + Cleaning + ETL + LangGraph orchestration. | 11 – 15 |

Only **10 core `staging_company` fields** are populated in the Researcher/Consolidator pipeline to keep API credits low. The full 163-field surface lives in `Milestone 1 - Researcher to Hiring/07 - Researcher Agent/schemas.py` with 153 fields intentionally commented out.

## Provider Wiring

| Agent | Providers |
|-------|-----------|
| Researcher | Groq, Google AI Studio, Cerebras (same prompt, 3 calls in parallel). |
| Consolidator | OpenRouter (cherry-picks best value per field). |
| Skill Set | Groq (single call). |
| Hiring Process | Groq (single call). |

Keys live in `Milestone 1 - Researcher to Hiring/05 - Setup Accounts and Env/.env.example`.

## Prompts

Canonical prompts live in the repo-root `Prompts/` folder:

- `Researcher Prompt.md`
- `Consolidator Prompt.md`
- `Skill Set Prompt.md`
- `Hiring Process Prompt.md`

Each agent loads its prompt file at runtime — no duplication.

## Run Order

1. Copy `.env.example` → `.env`, fill in the 4 provider keys.
2. `pip install -r "Milestone 1 - Researcher to Hiring/05 - Setup Accounts and Env/requirements.txt"`
3. `python "Milestone 1 - Researcher to Hiring/07 - Researcher Agent/run.py" --company "Fractal"`
4. `python "Milestone 1 - Researcher to Hiring/08 - Consolidator Agent/run.py" --company "Fractal"`
5. `python "Milestone 1 - Researcher to Hiring/09 - Skill Set Agent/run.py" --company "Fractal"`
6. `python "Milestone 1 - Researcher to Hiring/10 - Hiring Process Agent/run.py" --company "Fractal"`
7. Milestone 2 wires the validation → cleaning → ETL flow in LangGraph.
