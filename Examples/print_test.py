import sys
import bakkesmod
from bmutils import logger

logger.redirectStandardStreams()

print("global print")


def onLoad():
    print("onLoad print")
    print(bakkesmod)
    print(bakkesmod.cvarManager)
    print(bakkesmod.gameWrapper)

    print(sys.stdout)
    print("stdout test", file=sys.stdout)

    print(sys.stderr)
    print("stderr test", file=sys.stderr)


def onUnload():
    print("onUnload print")
