import asyncio
from bmutils import logger, decorators

logger.redirectStandardStreams()


@decorators.bmasync
async def onLoad():
    print("onLoad 1")
    await asyncio.sleep(3)
    print("onLoad 2")


def onUnload():
    print("onUnload 3")
