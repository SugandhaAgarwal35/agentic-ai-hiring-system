# LangSmith Tracing Guide

LangSmith automatically captures LangChain + LangGraph runs when three environment variables are set. Nothing to add to code.

## 1. Get a key

1. Sign in at <https://smith.langchain.com>.
2. Top-right → **Settings** → **API Keys** → **Create API Key**.
3. Copy the key (`lsv2_pt_...`).

## 2. Set the env vars

Paste these into `Milestone 1 - Researcher to Hiring/05 - Setup Accounts and Env/.env`:

```
LANGCHAIN_TRACING_V2=true
LANGSMITH_API_KEY=lsv2_pt_...
LANGSMITH_PROJECT=job-aid-session-1
```

The `_common.load_dotenv(...)` call in `_common.py` picks these up automatically.

## 3. Run the graph

```bash
cd "Milestone 2 - Validation LangGraph/15 - Workflows in LangGraph"
python run.py --company "Fractal"
```

## 4. What to look at in the LangSmith UI

- **Projects → job-aid-session-1** — one row per graph run.
- Click a row → see the **node timeline**: `researcher → consolidator → validator → (cleaner ↻)*  → etl`.
- Drill into any LLM call to see exact prompt, response, token count, latency, provider.
- Filter by **model** to compare Groq vs Google vs Cerebras on the same prompt.

## 5. Things to observe

- Does `cleaner` fire on the first run? If yes, which validator error triggered it?
- Which provider is the slowest? (Usually Google.)
- Which field most often needs cleaning? (Usually `incorporation_year`.)

## 6. Cost awareness

- Every trace counts toward your LangSmith quota (free tier = 5 k traces/month).
- Turn tracing off (`LANGCHAIN_TRACING_V2=false`) during large batch runs; turn on for the demo.
