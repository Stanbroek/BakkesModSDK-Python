from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class ControllerWrapper():
    # Public:
    # ControllerWrapper::ControllerWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ControllerWrapper::ControllerWrapper(ControllerWrapper const & other) [constructor]

    # ControllerWrapper & ControllerWrapper::operator=(ControllerWrapper rhs) [member operator]

    # ControllerWrapper::~ControllerWrapper() [destructor]
    def __del__(self) -> None: ...

    # PlayerReplicationInfoWrapper ControllerWrapper::GetPlayerReplicationInfo() [member function]
    def GetPlayerReplicationInfo(self) -> PlayerReplicationInfoWrapper: ...

    # Private:
    # ControllerWrapper::Impl [class declaration]

    # ControllerWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


