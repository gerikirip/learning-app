import logging
import time
from contextlib import asynccontextmanager

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import CONTENT_TYPE_LATEST, Counter, generate_latest

from app.api import router
from app.core.config import settings
from app.db.session import Base, SessionLocal, engine
from app.models import Card, Deck, Review  # noqa: F401 - imported so metadata is registered
from app.services.seed_service import seed_devops_content

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

REQUESTS_TOTAL = Counter(
    "learning_app_http_requests_total",
    "Total HTTP requests handled by the learning app",
    ["method", "path"],
)

DB_INIT_RETRIES = 10
DB_INIT_RETRY_DELAY_SECONDS = 3


def initialize_database() -> dict[str, int | bool]:
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as db:
        return seed_devops_content(db)


@asynccontextmanager
async def lifespan(app: FastAPI):
    last_error: Exception | None = None
    for attempt in range(1, DB_INIT_RETRIES + 1):
        try:
            stats = initialize_database()
            logger.info("Database initialized: %s", stats)
            last_error = None
            break
        except Exception as exc:
            last_error = exc
            if attempt < DB_INIT_RETRIES:
                logger.warning(
                    "Database init attempt %s/%s failed, retrying in %ss",
                    attempt,
                    DB_INIT_RETRIES,
                    DB_INIT_RETRY_DELAY_SECONDS,
                )
                time.sleep(DB_INIT_RETRY_DELAY_SECONDS)
            else:
                logger.exception(
                    "Database initialization failed after %s attempts. "
                    "Check DATABASE_URL and call POST /api/admin/seed after fixing it.",
                    DB_INIT_RETRIES,
                )
    if last_error is not None:
        logger.error("App started without database: %s", last_error)
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


@app.post("/api/admin/seed", tags=["platform"])
def run_seed() -> dict[str, int | bool]:
    """Create tables and seed DevOps decks if the database is empty."""
    return initialize_database()


@app.get("/metrics", tags=["platform"])
def metrics() -> Response:
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
