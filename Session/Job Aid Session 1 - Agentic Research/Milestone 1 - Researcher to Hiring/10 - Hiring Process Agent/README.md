# 10 — Hiring Process Agent  *(Hands-On — 5 min)*

A single-provider (Groq) agent that produces a realistic campus-hiring JSON for a target company: 1–3 roles × N rounds × M skill sets with typical interview questions.

## Files

| File | What it does |
|------|--------------|
| `schemas.py` | Nested Pydantic models: `HiringResponse → JobRoleDetails → HiringRound → RoundSkillSet`. |
| `hiring_process_agent.py` | `run(company)` → validated `HiringResponse`. |
| `run.py` | CLI: writes `outputs/<company>/hiring.json`. |

## Run it

```bash
cd "Job Aid Session 1 - Agentic Research/Milestone 1 - Researcher to Hiring/10 - Hiring Process Agent"
python run.py --company "Fractal"
```

## What to demo

- Open `outputs/Fractal/hiring.json`. Follow the nesting: `job_role_details[0].hiring_rounds[1].skill_sets[*].typical_questions` — note the semicolon-separated question list that matches the DB's storage format.
- Change the company to a non-tech name (say `"Maruti Suzuki"`). The `role_category`, round count, and `ctc_or_stipend` numbers shift realistically.

## Key concept

> Deep nesting in the schema catches LLM slop early. If the model forgets `skill_sets` or returns fewer than 3 entries per round, `Field(min_length=3)` triggers a Pydantic error and the retry loop fires.
