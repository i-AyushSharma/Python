import time
import asyncio

async def func1():
    # time.sleep(3)
    await asyncio.sleep(2)
    print("Func1")
    return "Ayush"
async def func2():
    # time.sleep(3)
    await asyncio.sleep(2)
    print("Func2")
async def func3():
    # time.sleep(3)
    await asyncio.sleep(4)
    print("Func3")

async def main():
    # task = asyncio.create_task(func1())
    # await func2()
    # await func3()
    L = await asyncio.gather(func1(), func2(), func3())
    print(L)
asyncio.run(main())
print("🥵🥶💩")