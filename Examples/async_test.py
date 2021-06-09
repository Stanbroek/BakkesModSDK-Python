import asyncio
from bmasync import BMEventLoopPolicy

loop = None


async def main():
    print('blieb')
    await asyncio.sleep(5)
    print('bloeb')


def onLoad():
    asyncio.set_event_loop_policy(BMEventLoopPolicy())
    global loop
    loop = asyncio.new_event_loop()
    # loop.set_debug(True)
    asyncio.set_event_loop(loop)
    asyncio.ensure_future(main())
    loop.start()


def onUnload():
    global loop
    if loop:
        loop.stop()
        loop = None
