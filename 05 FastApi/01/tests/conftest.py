import os
from typing import AsyncGenerator, Generator

import pytest  # type: ignore[import-not-found]
from fastapi.testclient import TestClient  # type: ignore[import-not-found]
from httpx import ASGITransport, AsyncClient  # type: ignore[import-not-found]

os.environ["ENV_STATE"] = "test"


from main import app
from routers.posts import comments_table, post_table


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture()
def client() -> Generator:
    yield TestClient(app)


@pytest.fixture(autouse=True)
async def db() -> AsyncGenerator:
    post_table.clear()
    comments_table.clear()
    yield


@pytest.fixture()
async def async_client(client) -> AsyncGenerator:
    async with AsyncClient(
        transport=ASGITransport(app),
        base_url=client.base_url,
    ) as ac:
        yield ac
