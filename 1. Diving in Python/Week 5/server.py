import asyncio


async def hello(name):
    while True:
        print(f'Hello, {name}!')
        await asyncio.sleep(1.0)


def _main():
    loop1 = asyncio.get_event_loop()
    loop1.run_until_complete(hello('first loop'))
    loop1.close()    

    loop2 = asyncio.get_event_loop()
    loop2.run_until_complete(hello('second loop'))
    loop2.close()

if __name__ == '__main__':
    _main()