import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.core.config import get_settings
from app.core.logging import configure_logging
from app.db.mongo import MongoDB

configure_logging()
logger = logging.getLogger(__name__)
settings = get_settings()

app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in settings.cors_origins.split(",") if o.strip()],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    MongoDB.connect()
    logger.info("Connected to MongoDB")


@app.on_event("shutdown")
def shutdown_event():
    MongoDB.disconnect()
    logger.info("Disconnected from MongoDB")


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(router, prefix=settings.api_prefix)
