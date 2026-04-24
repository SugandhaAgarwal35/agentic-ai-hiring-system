# Placement Analytics Service

This is the milestone 3 backend microservice built using `FastAPI` and `SQLModel`.

## Key Files

- `main.py`
- `database.py`
- `models.py`
- `requirements.txt`
- `.env`

## Setup

### 1. Open the folder

```powershell
cd "C:\Users\DELL\Downloads\SRM\Job Aid Session 2 - FastAPI Microservice\Milestone-3\placement-analytics-service"
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

## How to Get `DATABASE_URL` from Supabase

Official docs:

- API keys guide: https://supabase.com/docs/guides/api/api-keys
- Connection strings guide: https://supabase.com/docs/reference/postgres/connection-strings

Detailed steps:

1. Log in to Supabase.
2. Open your project.
3. Click `Connect`.
4. Find the PostgreSQL connection string section.
5. Select the connection string format recommended for your environment.
6. For most Windows student setups using IPv4, prefer the `Session pooler` string.
7. Copy the URI.
8. Replace `[YOUR-PASSWORD]` with the database password.
9. Paste it into `.env` as `DATABASE_URL`.

Example:

```env
DATABASE_URL=postgresql://postgres.<project-ref>:<your-password>@aws-1-ap-south-1.pooler.supabase.com:5432/postgres
```

## Run the Service

```powershell
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Swagger

- `http://localhost:8000/docs`
- `http://localhost:8000/redoc`

## Endpoints

- `GET /health`
- `GET /api/v1/companies`
- `GET /api/v1/companies/{company_id}`
- `GET /api/v1/companies/{company_id}/full-json`
- `GET /api/v1/company-details`
- `GET /api/v1/company-details/{company_id}`
- `GET /api/v1/hiring-rounds/{company_id}`
- `GET /api/v1/innovx/{company_id}`
- `GET /api/v1/skill-intelligence/{company_id}`
