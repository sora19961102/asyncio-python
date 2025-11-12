import asyncio

# Define a coroutine that simulates a time-consuming task
async def fetch_data(id, sleep_time):
    print(f"Continue {id} starting to fetch data")
    # if id == 2:
    #     raise Exception(f"id: {id} is not valid")
    await asyncio.sleep(sleep_time)
    return {"id": id, "data": f"Sample data from coroutine {id}"}

async def main():
    # Run coroutines concurrently and gather their return values
    results = await asyncio.gather(
        fetch_data(1, 2),
        fetch_data(2, 3),
        fetch_data(3, 1)
    )

    for result in results:
        print(result)

# Run the main coroutine
asyncio.run(main())
