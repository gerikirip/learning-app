# DevOps Learning App

A Docker-first Quizlet-style application for learning DevOps job skills through
flashcards, commands, interview questions, troubleshooting scenarios, and labs.

## Stack

- Frontend: React + Vite + TypeScript
- Backend: FastAPI + SQLAlchemy + Pydantic
- Database: PostgreSQL
- Runtime: Docker Compose
- Later deployment: Kubernetes + Helm

## Run Locally With Docker

You do not need Node, Python, or PostgreSQL installed locally.

```bash
docker compose up --build
```

Open:

- Frontend: `http://localhost:5173`
- Backend: `http://localhost:8000`
- API docs: `http://localhost:8000/docs`
- Health: `http://localhost:8000/health`
- Metrics: `http://localhost:8000/metrics`

## What The App Teaches

Seeded decks include:

- Docker foundations
- Kubernetes core objects
- Helm charts and values
- CI/CD with GitHub Actions
- Terraform basics
- Monitoring with Prometheus and Grafana
- DevOps security hardening

## Main Features

- List DevOps learning decks
- Create custom decks
- Add cards to a deck
- Study one card at a time
- Reveal the answer
- Rate the card as `again`, `good`, or `easy`
- Persist progress in PostgreSQL

## API Examples

```bash
curl http://localhost:8000/health
curl http://localhost:8000/metrics
curl http://localhost:8000/api/decks
```

Create a deck:

```bash
curl -X POST http://localhost:8000/api/decks \
  -H "Content-Type: application/json" \
  -d "{\"title\":\"Linux Basics\",\"description\":\"Commands and processes\",\"topic\":\"linux\",\"level\":\"beginner\"}"
```

## Deploy to Railway

Railway needs **3 services** from this repo (plus a PostgreSQL database).

### 1. PostgreSQL

1. In your Railway project, click **+ New** → **Database** → **PostgreSQL**
2. Copy the `DATABASE_URL` variable from the Postgres service

### 2. Backend

1. **+ New** → **GitHub Repo** → select `learning-app`
2. Set **Root Directory** to `backend` (or use repo root — it has a root `Dockerfile` for backend)
3. Railway will detect `railway.toml` and build with Docker (not Railpack)
4. Add variables:
   - `DATABASE_URL` = `${{Postgres.DATABASE_URL}}` (required — without this the app starts but decks API will fail)
   - `CORS_ORIGINS` = your frontend URL (set after frontend deploys), e.g. `https://your-frontend.up.railway.app`

### 3. Frontend

1. **+ New** → **GitHub Repo** → same `learning-app` repo
2. Set **Root Directory** to `frontend`
3. Add variable (must be available at **build** time):
   - `VITE_API_BASE_URL` = `https://${{backend.RAILWAY_PUBLIC_DOMAIN}}` (replace `backend` with your backend service name)
4. Generate a public domain under **Settings → Networking**

### Troubleshooting

| Error | Fix |
|-------|-----|
| `Script start.sh not found` / Railpack failed | Ensure `railway.toml` exists and **Builder** is set to **Dockerfile** in service settings |
| Backend can't connect to DB | Link `DATABASE_URL` from the Postgres plugin |
| Frontend shows network errors | Set `VITE_API_BASE_URL` to the backend public URL and **redeploy** frontend (Vite bakes it in at build time) |
| CORS errors | Set `CORS_ORIGINS` on backend to the frontend public URL |

## Kubernetes

Build local images:

```bash
docker build -t devops-learning-backend:0.1.0 backend
docker build --target prod --build-arg VITE_API_BASE_URL=http://localhost:8001 -t devops-learning-frontend:0.1.0 frontend
```

Apply manifests:

```bash
kubectl apply -f k8s/
kubectl get all -n devops-learning
kubectl port-forward svc/learning-frontend 8088:80 -n devops-learning
kubectl port-forward svc/learning-backend 8001:8000 -n devops-learning
```

## Helm

Render the chart:

```bash
helm template devops-learning ./helm/devops-learning-app
```

Install locally:

```bash
helm upgrade --install devops-learning ./helm/devops-learning-app
```

## DevOps Learning Path

This app will itself become a DevOps portfolio project:

1. Docker Compose local development
2. CI pipeline
3. Kubernetes manifests
4. Helm chart
5. Monitoring and logging
6. Security hardening
7. Cloud deployment later

## Interview Practice Ideas

- Explain the difference between frontend, backend, and database containers.
- Explain why PostgreSQL data survives container recreation.
- Debug a failing backend DB connection.
- Convert raw Kubernetes YAML into a Helm chart.
- Add monitoring and alerts for backend errors.
