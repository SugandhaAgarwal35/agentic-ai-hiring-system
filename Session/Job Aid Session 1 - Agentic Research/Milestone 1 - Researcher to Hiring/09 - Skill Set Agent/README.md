# 09 — Skill Set Agent  *(Hands-On — 5 min)*

A single-provider (Groq) agent that produces a 12-row skill-set table for a target company. Each row is `(skill_area, level 1–10, proficiency_code, rationale)`.

## Files

| File | What it does |
|------|--------------|
| `schemas.py` | `SkillSetsResponse` — company_name + exactly 12 `SkillSetEntry` rows. |
| `skill_set_agent.py` | `run(company)` → validated `SkillSetsResponse`. |
| `run.py` | CLI: writes `outputs/<company>/skills.json`. |

## Run it

```bash
cd "Job Aid Session 1 - Agentic Research/Milestone 1 - Researcher to Hiring/09 - Skill Set Agent"
python run.py --company "Fractal"
```

## What to demo

- Open `outputs/Fractal/skills.json` — note that **every** of the 12 skill areas is present, even ones the company rarely asks about (they get a low `level`, e.g. `operating_system: level=3, code=CU`).
- Change the company and re-run — see how `ai_native_engineering` bumps up for AI-first firms like OpenAI, drops for legacy service firms.

## Key concept

> One provider is enough here because the output space is **constrained**: 12 enum-keyed rows, level ∈ 1..10, code ∈ 5 enums. The schema does most of the validation work — the LLM just fills the numbers.
