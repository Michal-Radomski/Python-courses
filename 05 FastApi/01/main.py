from fastapi import FastAPI  # type: ignore[import-not-found]

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
