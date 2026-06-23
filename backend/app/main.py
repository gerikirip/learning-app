from contextlib import asynccontextmanager

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import CONTENT_TYPE_LATEST, Counter, generate_latest

from app.api import router
from app.core.config import settings
from app.db.session import Base, SessionLocal, engine
from app.models import Card, Deck, Review  # noqa: F401 - imported so metadata is registered
from app.services.seed_service import seed_devops_content

REQUESTS_TOTAL = Counter(
    "learning_app_http_requests_total",
    "Total HTTP requests handled by the learning app",
    ["method", "path"],
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as db:
        seed_devops_content(db)
    yield


app = FastAPI(title=settings.app_name, version="0.1.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.middleware("http")
async def metrics_middleware(request, call_next):
    response = await call_next(request)
    REQUESTS_TOTAL.labels(method=request.method, path=request.url.path).inc()
    return response


@app.get("/health", tags=["platform"])
def health() -> dict[str, str]:
    return {"status": "UP"}


@app.get("/metrics", tags=["platform"])
def metrics() -> Response:
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
