import asyncio

# Define a coroutine that simulates a time-consuming task
async def fetch_data(delay, id):
    print(f"Fetching data after {delay} seconds for {id}")
    # Simulate an I/O operation with a sleep
    await asyncio.sleep(delay)
    print(f"Data fetched for {id}")

    return f"Data fetched after {delay} seconds for {id}"

# Define another coroutine that uses the first coroutine
async def main():
    print("Start of main coroutine")

    task = fetch_data(2, 1)
    task2 = fetch_data(2, 2)

    # Await the fetch_data coroutine, pausing execution of main until fetch_data completes
    result = await task
    print(f"Received result: {result}")

    result2 = await task2
    print(f"Received result: {result2}")

    print("End of main coroutine")

# Run the main coroutine
asyncio.run(main())
