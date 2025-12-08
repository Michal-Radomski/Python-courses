FastAPI is a modern, high-performance Python web framework for building APIs with minimal code, leveraging type hints for
automatic data validation, serialization, and interactive OpenAPI documentation. It supports asynchronous operations for
superior speed compared to frameworks like Flask, and includes features like dependency injection and built-in
security.[1][2][3]

## Running FastAPI on Ubuntu

Install Python 3.8+ (pre-installed on recent Ubuntu) and pip if needed:
`sudo apt update && sudo apt install python3 python3-pip python3-venv`.[1]

Create and activate a virtual environment, then install FastAPI and Uvicorn (ASGI server):

```
python3 -m venv fastapi-env
source fastapi-env/bin/activate
pip install fastapi uvicorn
```

Create `main.py` with a basic app:

```python
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root(): return {"Hello": "World"}
```

Run with `uvicorn main:app --reload --host 0.0.0.0 --port 8000`; access at `http://localhost:8000/docs` for interactive
docs.[4][7][1]

## Key Features

- Automatic Swagger UI and ReDoc at `/docs` and `/redoc`.[2][1]
- Pydantic-based validation using Python type hints.[3]
- Async support for high concurrency, on par with Node.js.[6][2]

[1](https://www.geeksforgeeks.org/python/fastapi-introduction/) [2](https://fastapi.tiangolo.com/features/)
[3](https://en.wikipedia.org/wiki/FastAPI) [4](https://realpython.com/fastapi-python-web-apis/)
[5](https://refine.dev/blog/introduction-to-fast-api/) [6](https://fastapi.tiangolo.com)
[7](https://realpython.com/get-started-with-fastapi/) [8](https://www.youtube.com/watch?v=rvFsGRvj9jo)
[9](https://kinsta.com/blog/fastapi/)
[10](https://datascientest.com/en/fastapi-everything-you-need-to-know-about-the-most-widely-used-python-web-framework-for-machine-learning)
