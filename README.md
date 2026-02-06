# Labour Monorepo

Production-ready monorepo with a Next.js frontend and Django + DRF backend.

## Repository Structure

```
/
├── frontend/                 # Next.js App Router
├── backend/                  # Django + DRF
├── docker-compose.yml        # Postgres + Redis
├── README.md
└── .gitignore
```

## Frontend (Next.js App Router)

### Local setup

```bash
cd frontend
npm install
npm run dev
```

### Testing

```bash
npm run lint
npm run build
npm run test:unit
npm run test:e2e
```

> `npm run test:e2e` will **always exit 0**. If Playwright is not installed, it prints `Playwright not installed, skipping e2e` and exits successfully.

## Backend (Django + DRF)

### Local setup

Start Postgres + Redis:

```bash
docker compose up -d
```

Configure environment:

```bash
cp backend/.env.example backend/.env
```

Run server:

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Testing

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
python manage.py check
pytest -q
```

## API Endpoints

- `GET /healthz`
- `POST /auth/request-otp`
- `POST /auth/verify-otp`
- `GET /api/me`

Set `DEV_OTP_BYPASS=True` in `backend/.env` to return OTPs in responses for local development/testing.

## Vercel Deployment Requirements

Vercel must be configured with:

- **Root Directory**: `frontend`
- **Framework**: Next.js
- **Build Command**: `npm run build`

Common causes of a Vercel 404:

- Missing `app/page.tsx`
- Incorrect root directory

This repository prevents 404s by shipping a mandatory `app/page.tsx` (homepage) and `app/not-found.tsx`, and by documenting the correct Vercel root.

## CI Workflow

GitHub Actions runs:

- Frontend: `npm install`, `npm run lint`, `npm run build`, `npm run test:unit`, `npm run test:e2e`
- Backend: `pip install -r requirements-dev.txt`, `python manage.py check`, `pytest`

Playwright is optional and never required for installs or CI success.
