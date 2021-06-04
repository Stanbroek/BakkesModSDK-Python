from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class WorldInfoWrapper():
    # Public:
    # WorldInfoWrapper::WorldInfoWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # WorldInfoWrapper::WorldInfoWrapper(WorldInfoWrapper const & other) [constructor]

    # WorldInfoWrapper & WorldInfoWrapper::operator=(WorldInfoWrapper rhs) [member operator]

    # WorldInfoWrapper::~WorldInfoWrapper() [destructor]
    def __del__(self) -> None: ...

    # float WorldInfoWrapper::GetTimeDilation() [member function]
    def GetTimeDilation(self) -> float: ...

    # float WorldInfoWrapper::GetDemoPlayTimeDilation() [member function]
    def GetDemoPlayTimeDilation(self) -> float: ...

    # float WorldInfoWrapper::GetTimeSeconds() [member function]
    def GetTimeSeconds(self) -> float: ...

    # float WorldInfoWrapper::GetRealTimeSeconds() [member function]
    def GetRealTimeSeconds(self) -> float: ...

    # float WorldInfoWrapper::GetRealDeltaSeconds() [member function]
    def GetRealDeltaSeconds(self) -> float: ...

    # float WorldInfoWrapper::GetAudioTimeSeconds() [member function]
    def GetAudioTimeSeconds(self) -> float: ...

    # float WorldInfoWrapper::GetDeltaSeconds() [member function]
    def GetDeltaSeconds(self) -> float: ...

    # float WorldInfoWrapper::GetPauseDelay() [member function]
    def GetPauseDelay(self) -> float: ...

    # float WorldInfoWrapper::GetRealTimeToUnPause() [member function]
    def GetRealTimeToUnPause(self) -> float: ...

    # float WorldInfoWrapper::GetStallZ() [member function]
    def GetStallZ(self) -> float: ...

    # float WorldInfoWrapper::GetWorldGravityZ() [member function]
    def GetWorldGravityZ(self) -> float: ...

    # float WorldInfoWrapper::GetDefaultGravityZ() [member function]
    def GetDefaultGravityZ(self) -> float: ...

    # float WorldInfoWrapper::GetGlobalGravityZ() [member function]
    def GetGlobalGravityZ(self) -> float: ...

    # float WorldInfoWrapper::GetRBPhysicsGravityScaling() [member function]
    def GetRBPhysicsGravityScaling(self) -> float: ...

    # Private:
    # WorldInfoWrapper::Impl [class declaration]

    # WorldInfoWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


