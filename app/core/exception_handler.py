from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from .response import ResponseModel
from .exceptions import AppException


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(AppException)
    async def app_exception_handler(request: Request, exc: AppException):
        content = {"code": exc.code, "message": exc.message, "data": exc.data}
        return JSONResponse(status_code=exc.status_code, content=content)

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        content = {"code": str(getattr(exc, "status_code", exc.status_code)), "message": exc.detail or "HTTP error", "data": None}
        return JSONResponse(status_code=exc.status_code, content=content)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        content = {"code": "422", "message": "Validation Error", "data": exc.errors()}
        return JSONResponse(status_code=422, content=content)

    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception):
        content = {"code": "500", "message": "Internal Server Error", "data": str(exc)}
        return JSONResponse(status_code=500, content=content)
