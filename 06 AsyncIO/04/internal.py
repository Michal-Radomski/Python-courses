import asyncio
import heapq
import time


class SimpleTaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, coro, delay):
        exec_time = time.time() + delay
        heapq.heappush(self.tasks, (exec_time, coro))

    async def run(self):
        while self.tasks:
            exec_time, coro = heapq.heappop(self.tasks)
            now = time.time()
            if now < exec_time:
                await asyncio.sleep(exec_time - now)
            try:
                print(f"Executing {coro.__name__} at {time.time()}")
                await coro()
            except Exception as e:
                print(f"Task {coro.__name__} raised {e}")


async def sample_task():
    print(f"Task executed at {time.time()}")


async def main():
    scheduler = SimpleTaskScheduler()
    scheduler.add_task(sample_task, 3)
    scheduler.add_task(sample_task, 1)

    await scheduler.run()


asyncio.run(main())
