# from fastapi import FastAPI  # type: ignore[import-not-found]
from fastapi import FastAPI
from routers.posts import router as posts_router

# app = FastAPI()
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


app = FastAPI()
# print("app:", app) # app: <fastapi.applications.FastAPI object at 0x757e51b34e60>
app.include_router(posts_router)
