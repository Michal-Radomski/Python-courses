# from fastapi import FastAPI  # type: ignore[import-not-found]
import logging
from contextlib import asynccontextmanager

from asgi_correlation_id import CorrelationIdMiddleware
from database import database
from fastapi import FastAPI, HTTPException
from fastapi.exception_handlers import http_exception_handler
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from logging_conf import configure_logging
from routers.posts import router as posts_router
from routers.upload import router as upload_router
from routers.user import router as user_router

# app = FastAPI()
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# * V1
# app = FastAPI()
# print("app:", app) # app: <fastapi.applications.FastAPI object at 0x757e51b34e60>

logger = logging.getLogger(__name__)


# + Test not working, code not working!
# * V2
@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)
app.add_middleware(CorrelationIdMiddleware)

app.include_router(posts_router)
app.include_router(upload_router)
app.include_router(user_router)


@app.exception_handler(HTTPException)
async def http_exception_handle_logging(request, exc):
    logger.error(f"HTTPException: {exc.status_code} {exc.detail}")
    return await http_exception_handler(request, exc)


# * Favicon
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.svg")
