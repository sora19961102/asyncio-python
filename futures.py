import asyncio

async def set_future_result(future, value):
    await asyncio.sleep(2)

    # Set the result of the future
    future.set_result(value)
    print(f"Future result is set to {value}")

async def main():
    # get_running_loop() is used to get the current running event loop
    loop = asyncio.get_running_loop()

    # create_future() is used to create a future object in the current event loop
    future = loop.create_future()

    # Schedule setting the future result
    asyncio.create_task(set_future_result(future, "Future result is ready"))

    # Wait for the future result
    result = await future
    print(f"Future result is {result}")

asyncio.run(main())
