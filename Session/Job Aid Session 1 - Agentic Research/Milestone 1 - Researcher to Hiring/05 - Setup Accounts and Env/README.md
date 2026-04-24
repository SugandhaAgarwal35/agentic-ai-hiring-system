# 05 — Setting Up Accounts with LLM API Providers + Env  *(Hands-On — 10 min)*

This step is **one-time setup**. You need 4 free API keys and one Python virtualenv.

## 1. Groq

1. Open <https://console.groq.com/> and sign in with Google or GitHub.
2. Left sidebar → **API Keys** → **Create API Key** → name it `job-aid`.
3. Copy the key (starts with `gsk_...`) — **this is the only time it's shown**.
4. Paste into `.env` as `GROQ_API_KEY=...`.
5. Free tier: ~30 requests/min, plenty for this session.

## 2. Google AI Studio  *(a.k.a. Gemini API)*

1. Open <https://aistudio.google.com/app/apikey> and sign in with a personal Google account.
2. Click **Create API key** → pick **Create API key in new project** (or reuse an existing GCP project).
3. Copy the key (starts with `AIza...`).
4. Paste into `.env` as `GOOGLE_API_KEY=...`.
5. Free tier: 15 req/min for `gemini-2.5-flash-lite`. Do not share the key publicly — it's billing-linked.

## 3. Cerebras

1. Open <https://cloud.cerebras.ai/> → **Sign Up** (email / Google).
2. Verify email, then left sidebar → **API Keys** → **Create Key**.
3. Copy the key (starts with `csk-...`).
4. Paste into `.env` as `CEREBRAS_API_KEY=...`.
5. Free tier: 30 req/min on `llama3.1-8b`.

## 4. OpenRouter

1. Open <https://openrouter.ai/> → **Sign In** (Google/GitHub/email).
2. Top-right avatar → **Keys** → **Create Key** → name it `job-aid`.
3. Copy the key (starts with `sk-or-v1-...`).
4. Paste into `.env` as `OPENROUTER_API_KEY=...`.
5. You get a small free credit on signup; model `meta-llama/llama-3.2-3b-instruct:free` is zero-cost.

## 5. Python environment

```bash
cd "Job Aid Session 1 - Agentic Research/Milestone 1 - Researcher to Hiring/05 - Setup Accounts and Env"
cp .env.example .env     # then paste your 4 keys
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # macOS / Linux
pip install -r requirements.txt
```

## 6. Verify

```bash
python -c "from dotenv import load_dotenv; load_dotenv(); import os; print({k: bool(os.environ.get(k)) for k in ['GROQ_API_KEY','GOOGLE_API_KEY','CEREBRAS_API_KEY','OPENROUTER_API_KEY']})"
```

All four should print `True`. If any is `False`, re-check the `.env` file and restart the shell.

## Security

- Never commit `.env`. It is already in the repo-root `.gitignore`.
- Rotate keys if you accidentally paste one into Slack/screen-share.
- For the classroom demo, we only need read-level calls — no key escalation or service-account work.
