import bakkesmod
from bmutils import logger, decorators

logger.redirectStandardStreams()


@decorators.plugin("TestPlugin", decorators.PLUGINTYPE_NORMAL)
class Test(bakkesmod.BakkesModPlugin):
    def __init__(self):
        super().__init__()
        print("init class")

    def __del__(self):
        print("del class")

    @decorators.onLoad
    def onLoad(self):
        print("onLoad class")
        print(self.gameWrapper)
        print(self.cvarManager)

    @decorators.onUnload
    def onUnload(self):
        print("onUnload class")
