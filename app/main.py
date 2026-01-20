from fastapi import FastAPI
from app.core.exception_handler import register_exception_handlers
from app.api.router import router as api_router
from app.core.middleware import response_middleware


def create_app() -> FastAPI:
    app = FastAPI(title="Puma FastAPI Template")
    app.include_router(api_router, prefix="/api")
    # register middleware-based response wrapper
    app.middleware("http")(response_middleware)
    register_exception_handlers(app)
    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
