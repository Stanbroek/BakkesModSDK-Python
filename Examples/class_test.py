import bakkesmod
import decorators


@decorators.plugin("TestPlugin", 0)
class Test(bakkesmod.BakkesModPlugin):
    def __init__(self):
        super().__init__()
        print("init")

    def __del__(self):
        print("del")

    @decorators.onLoad
    def onLoad(self):
        print("onLoad")
        print(self.gameWrapper)
        print(self.cvarManager)

    @decorators.onUnload
    def onUnload(self):
        print("onUnload")
