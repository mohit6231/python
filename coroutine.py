import aiohttp
import asyncio


async def my_coroutine():
    print("Coroutine started")
    await asyncio.sleep(1)
    print("Coroutine resumed after 1 second")

# Running the coroutine
asyncio.run(my_coroutine())


async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 completed after 2 seconds")


async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 completed after 1 second")


async def main():
    await asyncio.gather(task1(), task2())

# Run the main coroutine
asyncio.run(main())

# Making HTTP Requests Asynchronously


async def fetch_data(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch_data(session, 'https://www.google.com')
        print(html)

# Running the main coroutine
asyncio.run(main())


async def faulty_coroutine():
    try:
        print("Coroutine started")
        await asyncio.sleep(1)
        raise ValueError("An error occurred")
    except ValueError as e:
        print(f"Caught an error: {e}")

asyncio.run(faulty_coroutine())
