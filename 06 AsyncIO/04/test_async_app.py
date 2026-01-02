import pytest  # type: ignore[import-not-found]
from async_app import fetch_data


@pytest.mark.asyncio
async def test_fetch_data():
    result = await fetch_data()
    assert result == {"data": 123}, "Expected result did not match!"
