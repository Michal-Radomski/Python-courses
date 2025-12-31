import asyncio


async def greet(name, delay):
    await asyncio.sleep(delay)
    print(f"hello {name}, after {delay} seconds!")


async def main():
    task1 = asyncio.create_task(greet("Alice", 1))
    task2 = asyncio.create_task(greet("Bob", 2))
    # print(task1, task2)

    await task1
    await task2


asyncio.run(main())
# hello Alice, after 1 seconds!
# hello Bob, after 2 seconds!


async def download_file(file_name):
    print(f"starting download {file_name}")
    await asyncio.sleep(2)
    print(f"Finished downloading {file_name}")
    return f"{file_name} downloaded"


async def main():
    files_lst = ["file1.txt", "file2.txt", "file3.txt"]
    # download_coroutines = [download_file(file) for file in files_lst]
    download_tasks = [asyncio.create_task(download_file(file)) for file in files_lst]

    completed, pending = await asyncio.wait(
        download_tasks,
        return_when=asyncio.ALL_COMPLETED,  # Now passes Tasks
    )
    print(pending)

    for download_task in completed:
        print(download_task.result())


asyncio.run(main())
# starting download file1.txt
# starting download file2.txt
# starting download file3.txt
# Finished downloading file1.txt
# Finished downloading file2.txt
# Finished downloading file3.txt
# set()
# file2.txt downloaded
# file1.txt downloaded
# file3.txt downloaded


async def compute_square(number):
    await asyncio.sleep(1)
    print(f"Square of {number} is {number * number}")
    return number * number


async def main():
    numbers = [1, 2, 3, 4, 5]
    tasks = [asyncio.create_task(compute_square(number)) for number in numbers]

    squares = await asyncio.gather(*tasks)
    print(f"Squares: {squares}")


asyncio.run(main())
# Square of 1 is 1
# Square of 2 is 4
# Square of 3 is 9
# Square of 4 is 16
# Square of 5 is 25
# Squares: [1, 4, 9, 16, 25]
