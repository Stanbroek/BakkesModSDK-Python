import asyncio
import bakkesmod
from bmutils import logger, decorators

logger.redirectStandardStreams()


@decorators.plugin("AsyncTestPlugin", decorators.PLUGINTYPE_ASYNC)
class AsyncTest(bakkesmod.BakkesModPlugin):
    def __init__(self):
        super().__init__()
        print("init class")

    def __del__(self):
        print("del class")

    @decorators.onLoad
    async def onLoad(self):
        print("onLoad class 1")
        await asyncio.sleep(3)
        print("onLoad class 2")

    @decorators.onUnload
    def onUnload(self):
        print("onUnload class 3")
