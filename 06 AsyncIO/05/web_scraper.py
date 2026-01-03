# pip install aiohttp
import asyncio

import aiohttp  # type: ignore[import-not-found]


async def fetch_page(session, url):
    async with session.get(url) as response:
        print(f"Status for {url}: {response.status}")
        return await response.text()


async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_page(session, url) for url in urls]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    urls = [
        "http://python.org",
        "https://asyncio.readthedocs.io",
        "https://aiohttp.readthedocs.io",
    ]
    asyncio.run(main(urls))
