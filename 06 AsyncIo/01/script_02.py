import asyncio


# * Basic
async def say_after(delay, what):
    await asyncio.sleep(delay)  # seconds
    print(what)


async def main():
    print("Started at:", asyncio.get_running_loop().time())
    await say_after(1, "Hello AsyncIO")
    await say_after(2, "AsyncIO is powerful")

    print("Finished at:", asyncio.get_running_loop().time())


asyncio.run(main())
# Started at: 4603.88042025
# Hello AsyncIO
# AsyncIO is powerful
# Finished at: 4606.883207924


# * Custom
async def task(name, delay):
    print(f"Task {name} stating with delay of {delay}")
    await asyncio.sleep(delay)
    print(f"Task {name} finished!")
    return f"Task {name} result"


async def main():
    tasks = [task("A", 1), task("B", 2), task("C", 3)]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
# Task A stating with delay of 1
# Task B stating with delay of 2
# Task C stating with delay of 3
# Task A finished!
# Task B finished!
# Task C finished!
# Task A result
# Task B result
# Task C result
