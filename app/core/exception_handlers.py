import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.exceptions import ChatPDFException

logger = logging.getLogger(__name__)


def register_exception_handlers(app: FastAPI) -> None:
    """Register global exception handlers."""

    @app.exception_handler(ChatPDFException)
    async def chatpdf_exception_handler(
        request: Request,
        exc: ChatPDFException,
    ) -> JSONResponse:
        return JSONResponse(
            status_code=400,
            content={
                "success": False,
                "error": {
                    "type": exc.__class__.__name__,
                    "message": exc.message,
                },
            },
        )

    @app.exception_handler(Exception)
    async def global_exception_handler(
        request: Request,
        exc: Exception,
    ) -> JSONResponse:
        logger.exception("Unhandled exception occurred.")

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "error": {
                    "type": "InternalServerError",
                    "message": "An unexpected error occurred.",
                },
            },
        )
