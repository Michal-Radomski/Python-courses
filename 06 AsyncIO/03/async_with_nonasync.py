import asyncio
import time


def sync_blocking_operations():
    time.sleep(2)
    return "Operation completed"


async def run_sync_in_thread_pool():
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, sync_blocking_operations)
    print(result)


async def main():
    await run_sync_in_thread_pool()


asyncio.run(main())
