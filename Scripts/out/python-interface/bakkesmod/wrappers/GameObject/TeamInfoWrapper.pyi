from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class TeamInfoWrapper():
    # Public:
    # TeamInfoWrapper::TeamInfoWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # TeamInfoWrapper::TeamInfoWrapper(TeamInfoWrapper const & other) [constructor]

    # TeamInfoWrapper & TeamInfoWrapper::operator=(TeamInfoWrapper rhs) [member operator]

    # TeamInfoWrapper::~TeamInfoWrapper() [destructor]
    def __del__(self) -> None: ...

    # UnrealStringWrapper TeamInfoWrapper::GetTeamName() [member function]
    def GetTeamName(self) -> UnrealStringWrapper: ...

    # int TeamInfoWrapper::GetSize() [member function]
    def GetSize(self) -> int: ...

    # void TeamInfoWrapper::SetSize(int newSize) [member function]
    def SetSize(self, newSize: int) -> None: ...

    # int TeamInfoWrapper::GetScore() [member function]
    def GetScore(self) -> int: ...

    # void TeamInfoWrapper::SetScore(int newScore) [member function]
    def SetScore(self, newScore: int) -> None: ...

    # int TeamInfoWrapper::GetTeamIndex() [member function]
    def GetTeamIndex(self) -> int: ...

    # void TeamInfoWrapper::SetTeamIndex(int newTeamIndex) [member function]
    def SetTeamIndex(self, newTeamIndex: int) -> None: ...

    # UnrealColor TeamInfoWrapper::GetTeamColor() [member function]
    def GetTeamColor(self) -> UnrealColor: ...

    # void TeamInfoWrapper::SetTeamColor(UnrealColor newTeamColor) [member function]
    def SetTeamColor(self, newTeamColor: UnrealColor) -> None: ...

    # unsigned char TeamInfoWrapper::GetTeamNum() [member function]
    def GetTeamNum(self) -> int: ...

    # void TeamInfoWrapper::eventDestroyed() [member function]
    def eventDestroyed(self) -> None: ...

    # Private:
    # TeamInfoWrapper::Impl [class declaration]

    # TeamInfoWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


