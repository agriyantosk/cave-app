from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from utils.response import error_response
import logging
import traceback


def register_exception_handlers(app: FastAPI):
    # Global HTTP exception handler (like 404, 401, etc)
    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        return error_response(
            message=exc.detail,
            status_code=exc.status_code,
        )

    # Request validation errors (e.g., FastAPI can't parse int from string)
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        return error_response(
            message="Validation error",
            status_code=422
        )

    # Catch-all fallback for uncaught Python exceptions (500 errors)
    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception):
        logging.error(f"Unhandled error: {exc}", exc_info=True)
        logging.error(traceback.format_exc())
        return error_response(
            message="Internal Server Error",
            status_code=500
        )
