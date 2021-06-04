from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class ReplayServerWrapper():
    # Public:
    # ReplayServerWrapper::ReplayServerWrapper(uintptr_t server, uintptr_t gameinfo, uintptr_t replaydirector) [constructor]
    def __init__(self, server: int, gameinfo: int, replaydirector: int) -> None: ...

    # ReplayServerWrapper::ReplayServerWrapper(ReplayServerWrapper const & other) [constructor]

    # ReplayServerWrapper & ReplayServerWrapper::operator=(ReplayServerWrapper rhs) [member operator]

    # ReplayServerWrapper::~ReplayServerWrapper() [destructor]
    def __del__(self) -> None: ...

    # ActorWrapper ReplayServerWrapper::GetViewTarget() [member function]
    def GetViewTarget(self) -> ActorWrapper: ...

    # ReplayWrapper ReplayServerWrapper::GetReplay() [member function]
    def GetReplay(self) -> ReplayWrapper: ...

    # float ReplayServerWrapper::GetReplayTimeElapsed() [member function]
    def GetReplayTimeElapsed(self) -> float: ...

    # int ReplayServerWrapper::GetReplayFPS() [member function]
    def GetReplayFPS(self) -> int: ...

    # int ReplayServerWrapper::GetCurrentReplayFrame() [member function]
    def GetCurrentReplayFrame(self) -> int: ...

    # void ReplayServerWrapper::AddKeyFrame(int frame, std::string name) [member function]
    def AddKeyFrame(self, frame: int, name: str) -> None: ...

    # void ReplayServerWrapper::RemoveKeyFrame(int frame) [member function]
    def RemoveKeyFrame(self, frame: int) -> None: ...

    # void ReplayServerWrapper::SkipToFrame(int frame) [member function]
    def SkipToFrame(self, frame: int) -> None: ...

    # void ReplayServerWrapper::SkipToTime(float time) [member function]
    def SkipToTime(self, time: float) -> None: ...

    # void ReplayServerWrapper::StartPlaybackAtFrame(int frame) [member function]
    def StartPlaybackAtFrame(self, frame: int) -> None: ...

    # void ReplayServerWrapper::StartPlaybackAtTime(float time) [member function]
    def StartPlaybackAtTime(self, time: float) -> None: ...

    # Private:
    # ReplayServerWrapper::Impl [class declaration]

    # ReplayServerWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


