from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class ReplaySoccarWrapper():
    # Public:
    # ReplaySoccarWrapper::ReplaySoccarWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ReplaySoccarWrapper::ReplaySoccarWrapper(ReplaySoccarWrapper const & other) [constructor]

    # ReplaySoccarWrapper & ReplaySoccarWrapper::operator=(ReplaySoccarWrapper rhs) [member operator]

    # ReplaySoccarWrapper::~ReplaySoccarWrapper() [destructor]
    def __del__(self) -> None: ...

    # int ReplaySoccarWrapper::GetTeamSize() [member function]
    def GetTeamSize(self) -> int: ...

    # void ReplaySoccarWrapper::SetTeamSize(int newTeamSize) [member function]
    def SetTeamSize(self, newTeamSize: int) -> None: ...

    # int ReplaySoccarWrapper::GetUnfairTeamSize() [member function]
    def GetUnfairTeamSize(self) -> int: ...

    # void ReplaySoccarWrapper::SetUnfairTeamSize(int newUnfairTeamSize) [member function]
    def SetUnfairTeamSize(self, newUnfairTeamSize: int) -> None: ...

    # long unsigned int ReplaySoccarWrapper::GetbUnfairBots() [member function]
    def GetbUnfairBots(self) -> bool: ...

    # void ReplaySoccarWrapper::SetbUnfairBots(long unsigned int newbUnfairBots) [member function]
    def SetbUnfairBots(self, newbUnfairBots: bool) -> None: ...

    # int ReplaySoccarWrapper::GetPrimaryPlayerTeam() [member function]
    def GetPrimaryPlayerTeam(self) -> int: ...

    # void ReplaySoccarWrapper::SetPrimaryPlayerTeam(int newPrimaryPlayerTeam) [member function]
    def SetPrimaryPlayerTeam(self, newPrimaryPlayerTeam: int) -> None: ...

    # int ReplaySoccarWrapper::GetTeam0Score() [member function]
    def GetTeam0Score(self) -> int: ...

    # void ReplaySoccarWrapper::SetTeam0Score(int newTeam0Score) [member function]
    def SetTeam0Score(self, newTeam0Score: int) -> None: ...

    # int ReplaySoccarWrapper::GetTeam1Score() [member function]
    def GetTeam1Score(self) -> int: ...

    # void ReplaySoccarWrapper::SetTeam1Score(int newTeam1Score) [member function]
    def SetTeam1Score(self, newTeam1Score: int) -> None: ...

    # void ReplaySoccarWrapper::eventPreExport() [member function]
    def eventPreExport(self) -> None: ...

    # void ReplaySoccarWrapper::RemoveTimelineKeyframe(int KeyframeIndex) [member function]
    def RemoveTimelineKeyframe(self, KeyframeIndex: int) -> None: ...

    # void ReplaySoccarWrapper::RecordUserEvent() [member function]
    def RecordUserEvent(self) -> None: ...

    # void ReplaySoccarWrapper::AddPlayer(PriWrapper PRI) [member function]
    def AddPlayer(self, PRI: PriWrapper) -> None: ...

    # Private:
    # ReplaySoccarWrapper::Impl [class declaration]

    # ReplaySoccarWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


