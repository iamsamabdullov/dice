import asyncio

async def waiter():
    task1 = asyncio.create_task(cook("Pasta", 8))
    task2 = asyncio.create_task(cook("Salad Caesar", 5))
    task3 = asyncio.create_task(cook("Choop", 3))

    await task1
    await task2
    await task3


async def cook(order, time_to_prepare):
    print(f"New order: {order}")
    await asyncio.sleep(time_to_prepare)
    print(order, " is ready")

asyncio.run(waiter())