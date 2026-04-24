# Milestone 3 - Placement Analytics Service

This milestone covers backend API development using `FastAPI` and `SQLModel`.

Service folder:

`Milestone-3/placement-analytics-service`

Prerequisites:

- See [PREREQUISITES.md](../PREREQUISITES.md)

## Learning Objective

Students should learn how to:

- create a Python virtual environment
- install backend dependencies
- configure a PostgreSQL connection using Supabase
- run a FastAPI microservice with Uvicorn
- validate APIs using Swagger UI

## Tech Stack

- FastAPI
- SQLModel
- PostgreSQL
- Uvicorn
- Python

## Step 1 - Open the Backend Folder

```powershell
cd "C:\Users\DELL\Downloads\SRM\Job Aid Session 2 - FastAPI Microservice\Milestone-3\placement-analytics-service"
```

## Step 2 - Create and Activate Virtual Environment

Create:

```powershell
python -m venv .venv
```

Activate:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

## Step 3 - Install Dependencies

```powershell
pip install -r requirements.txt
```

## Step 4 - Get the Database URL from Supabase

Students must copy the PostgreSQL connection string from Supabase and place it in `.env`.

Official reference:

- Supabase connection strings: https://supabase.com/docs/reference/postgres/connection-strings

Steps:

1. Sign in to the Supabase Dashboard.
2. Open the required project.
3. Click the `Connect` button near the top of the project dashboard.
4. In the connection options, locate the PostgreSQL connection string.
5. If your environment does not support IPv6, use the `Session pooler` connection string.
6. Copy the URI format string.
7. Replace `[YOUR-PASSWORD]` with the actual database password.
8. Paste the value into `.env` as `DATABASE_URL`.

Example:

```env
DATABASE_URL=postgresql://postgres.fhcqtrrwbfdptnjaejjo:<your-password>@aws-1-ap-south-1.pooler.supabase.com:5432/postgres
```

## Step 5 - Update the `.env` File

File:

`Milestone-3/placement-analytics-service/.env`

Required key:

```env
DATABASE_URL=postgresql://postgres.<project-ref>:<your-password>@aws-1-ap-south-1.pooler.supabase.com:5432/postgres
```

## Step 6 - Run the Backend

```powershell
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Step 7 - Open Swagger and Validate APIs

Open:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

Recommended API checks:

- `GET /health`
- `GET /api/v1/companies`
- `GET /api/v1/companies/{company_id}`
- `GET /api/v1/companies/{company_id}/full-json`
- `GET /api/v1/company-details/{company_id}`
- `GET /api/v1/hiring-rounds/{company_id}`
- `GET /api/v1/skill-intelligence/{company_id}`

## Important Notes for Mentors

- Home page data is now designed to consume `short_json` only.
- Dashboard data is now designed to use a separate `full_json` API.
- Students should understand why smaller payloads reduce unnecessary backend load.
s