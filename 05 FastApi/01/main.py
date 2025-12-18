# from fastapi import FastAPI  # type: ignore[import-not-found]
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from routers.posts import router as posts_router

# app = FastAPI()
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


app = FastAPI()
# print("app:", app) # app: <fastapi.applications.FastAPI object at 0x757e51b34e60>
app.include_router(posts_router)

# * Favicon
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.svg")
