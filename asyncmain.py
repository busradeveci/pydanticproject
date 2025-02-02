import asyncio

async def first_function():
    print(f"first function starts.")
    await asyncio.sleep(5)  #non blocking delay simülasyonu
    print(f"first function ends.")
    return 5

async def second_function():
    print(f"second function stars.")
    await asyncio.sleep(5)  #non blocking delay simülasyonu
    print(f"second function ends.")
    return 10

async def main():

    task1 = asyncio.create_task(first_function())
    task2 = asyncio.create_task((second_function()))

    x = await task1
    y = await task2

    print(x)
    print(y)

if __name__ =='__main__':
    asyncio.run(main())