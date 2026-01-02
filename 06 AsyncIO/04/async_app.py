# pip install pytest
# pip install pytest-asyncio

import asyncio


async def fetch_data():
    await asyncio.sleep(1)
    return {"data": 123}
