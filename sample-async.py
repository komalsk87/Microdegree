import asyncio
import time

# async def greet():
#     print("Hello!")

#     await asyncio.sleep(3)
#     print("How are you?")

# asyncio.run(greet())

async def task1():
    print("Task 1: Starting")
    await asyncio.sleep(2)
    print("Task 1: Finished")

async def task2():
    print("Task 2: Starting")
    await asyncio.sleep(1)
    print("Task 2: Finished")

async def task3():
    print("Task 3: Starting")
    await asyncio.sleep(3)
    print("Task 3: Finished")

async def main():
    await asyncio.gather(task1(), task2(), task3())

asyncio.run(main())
