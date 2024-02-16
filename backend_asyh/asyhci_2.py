import asyncio
from time import time


async def do_something(sec):
    await asyncio.sleep(sec)
    print("results", sec)

async def print1(sec):
    await asyncio.sleep(sec)
    print(sec)
    await do_something(sec)
async def main():

    test = [print1(i) for i in range(1,16)]
    await asyncio.gather(*test)
        
    # Other code here

if __name__ == "__main__":
    asyncio.run(main())