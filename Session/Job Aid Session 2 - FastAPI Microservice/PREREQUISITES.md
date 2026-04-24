# Project Prerequisites

This document lists the tools students should install before starting milestone 3, milestone 4, and milestone 5.

## Required Software

### 1. Python

Used for:

- milestone 3 backend
- virtual environment creation
- running FastAPI with Uvicorn

Install from the official Python website:

- Python downloads: https://www.python.org/downloads/?lang=python
- Python on Windows guide: https://docs.python.org/3.10/using/windows.html

Recommended version:

- Python 3.11 or later

Important:

- During installation on Windows, enable `Add python.exe to PATH`.

### 2. Node.js and npm

Used for:

- milestone 4 frontend
- Vite development server
- installing frontend dependencies

Install from the official Node.js website:

- Node.js downloads: https://nodejs.org/en/download

Recommended version:

- Node.js 18 or later

### 3. Visual Studio Code

Used for:

- editing backend and frontend files
- reading README instructions
- terminal usage inside the IDE

Install from the official website:

- VS Code download: https://code.visualstudio.com/download

### 4. Docker Desktop

Used for:

- milestone 5 Docker deployment
- Docker Compose based multi-service execution

Install from the official Docker documentation:

- Docker Desktop for Windows: https://docs.docker.com/desktop/setup/install/windows-install/
- Docker Compose installation overview: https://docs.docker.com/compose/install/

Important:

- Docker Desktop should be running before using `docker compose up --build`.

### 5. Supabase Account

Used for:

- project database access
- project URL
- publishable key
- PostgreSQL connection string

Create or sign in:

- Supabase docs: https://supabase.com/docs
- Supabase API keys guide: https://supabase.com/docs/guides/api/api-keys
- Supabase connection strings guide: https://supabase.com/docs/reference/postgres/connection-strings
- Supabase API routes guide: https://supabase.com/docs/guides/api/creating-routes

## Minimum Knowledge Students Should Have

- basic terminal usage
- creating files and folders
- running Python commands
- running npm commands
- opening URLs in browser
- editing `.env` files carefully

## Installation Verification Commands

After installing the tools, students can verify them from PowerShell:

```powershell
python --version
pip --version
node --version
npm --version
docker --version
docker compose version
```

## Recommended Setup Order

1. Install Python
2. Install Node.js
3. Install VS Code
4. Install Docker Desktop
5. Sign in to Supabase and locate project credentials

## Notes

- Milestone 3 depends mainly on Python and Supabase.
- Milestone 4 depends on Node.js, npm, and the milestone 3 backend.
- Milestone 5 depends on Docker Desktop and the previous milestone environment files.
