from fastapi import FastAPI

from app.api.routes.chat import router as chat_router
from app.api.routes.documents import router as documents_router
from app.api.routes.health import router as health_router
from app.core.config import settings
from app.core.exception_handlers import register_exception_handlers
from app.core.logging import configure_logging


def create_application() -> FastAPI:
    """Create and configure the FastAPI application."""

    configure_logging()

    app = FastAPI(
        title=settings.app.name,
        debug=settings.app.debug,
    )

    register_exception_handlers(app)
    app.include_router(health_router)
    app.include_router(documents_router)
    app.include_router(chat_router)

    return app


app = create_application()
