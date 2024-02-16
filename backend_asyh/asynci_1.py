import asyncio

async def print1():
    print(1)
    

async def print2():
    await asyncio.sleep(10)
    print(2)
    # Your coroutine code here
    


async def print3():
    print(3)
    

async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(print1())
        tg.create_task(print2())
        tg.create_task(print3())
    # Other code here

if __name__ == "__main__":
    asyncio.run(main())