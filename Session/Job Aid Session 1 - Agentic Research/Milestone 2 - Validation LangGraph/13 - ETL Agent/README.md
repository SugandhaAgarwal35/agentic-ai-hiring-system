# 13 — ETL Agent  *(Hands-On — 5 min)*

Writes a **validated payload** to the appropriate staging table. Once the row is in staging, the existing DB **trigger** from `Database Setup/Step 4` migrates it into the normalized tables — the ETL agent never touches normalized tables directly.

## Files

| File | What it does |
|------|--------------|
| `models.py` | SQLModel mirrors of `staging_company`, `staging_skills_topics`, `job_role_details_json`. |
| `etl_agent.py` | `stage(kind, payload)` → dict of the row that was/would be inserted. Defaults to dry-run. |
| `run.py` | CLI: reads a JSON, validates, stages. |

## Environment knobs

- `DATABASE_URL` — e.g. `postgresql+psycopg://user:pass@host:5432/campus`.
- `ETL_WRITE_MODE=db` — actually insert (default is `dry` — just print the row).

## Run it (dry mode by default)

```bash
cd "Job Aid Session 1 - Agentic Research/Milestone 2 - Validation LangGraph/13 - ETL Agent"
python run.py --kind company --payload "../../Milestone 1 - Researcher to Hiring/08 - Consolidator Agent/outputs/Fractal/golden.json"
```

You'll see the row the agent **would** write. Flip `ETL_WRITE_MODE=db` + set `DATABASE_URL` to perform the real insert.

## Why staging-only

The SP/trigger chain in `Database Setup/Step 4` owns all cross-table migration: updating normalized tables directly from an LLM agent would require duplicating that SP in Python and keeping the two copies in sync forever. Staging + trigger is the cheapest path to a reliable pipeline.
