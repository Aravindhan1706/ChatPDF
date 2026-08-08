import logging
import time

from fastapi import FastAPI, Request

logger = logging.getLogger(__name__)


def register_middleware(app: FastAPI) -> None:
    """Register application middleware."""

    @app.middleware("http")
    async def log_requests(
        request: Request,
        call_next,
    ):
        start_time = time.perf_counter()

        logger.info(
            "Started %s %s",
            request.method,
            request.url.path,
        )

        response = await call_next(request)

        elapsed = (time.perf_counter() - start_time) * 1000

        logger.info(
            "Completed %s %s (%d) in %.2f ms",
            request.method,
            request.url.path,
            response.status_code,
            elapsed,
        )

        return response
