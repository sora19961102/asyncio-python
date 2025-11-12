import asyncio

async def fetch_data(delay):
    print(f"Fetching data after {delay} seconds")
    await asyncio.sleep(delay)
    print("Data fetched")
    return f"Data fetched after {delay} seconds"

# coroutine function
async def main():
    print("Start of main coroutine")
    task = fetch_data(2)
    result = await task
    print(f"Received result: {result}")
    print("End of main coroutine")

asyncio.run(main())
