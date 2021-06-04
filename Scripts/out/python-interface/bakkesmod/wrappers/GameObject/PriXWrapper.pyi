from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class PriXWrapper():
    # Public:
    # PriXWrapper::PriXWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # PriXWrapper::PriXWrapper(PriXWrapper const & other) [constructor]

    # PriXWrapper & PriXWrapper::operator=(PriXWrapper rhs) [member operator]

    # PriXWrapper::~PriXWrapper() [destructor]
    def __del__(self) -> None: ...

    # void PriXWrapper::eventDestroyed() [member function]
    def eventDestroyed(self) -> None: ...

    # void PriXWrapper::OnUniqueIdChanged() [member function]
    def OnUniqueIdChanged(self) -> None: ...

    # void PriXWrapper::SetUniqueId(SteamID & PlayerUniqueId) [member function]
    def SetUniqueId(self, PlayerUniqueId: SteamID) -> None: ...

    # void PriXWrapper::UnregisterPlayerFromSession() [member function]
    def UnregisterPlayerFromSession(self) -> None: ...

    # void PriXWrapper::RegisterPlayerWithSession() [member function]
    def RegisterPlayerWithSession(self) -> None: ...

    # void PriXWrapper::OnTeamChanged() [member function]
    def OnTeamChanged(self) -> None: ...

    # void PriXWrapper::SetPlayerTeam(TeamInfoWrapper NewTeam) [member function]
    def SetPlayerTeam(self, NewTeam: TeamInfoWrapper) -> None: ...

    # void PriXWrapper::eventOnOwnerChanged() [member function]
    def eventOnOwnerChanged(self) -> None: ...

    # void PriXWrapper::eventSetPlayerName(std::string S) [member function]
    def eventSetPlayerName(self, S: str) -> None: ...

    # void PriXWrapper::EventDestroyed(PriXWrapper PRI) [member function]
    def EventDestroyed(self, PRI: PriXWrapper) -> None: ...

    # void PriXWrapper::EventTeamChanged(PriXWrapper PRI) [member function]
    def EventTeamChanged(self, PRI: PriXWrapper) -> None: ...

    # void PriXWrapper::EventUniqueIdChanged(PriXWrapper PRI) [member function]
    def EventUniqueIdChanged(self, PRI: PriXWrapper) -> None: ...

    # void PriXWrapper::EventPlayerNameChanged(PriXWrapper PRI) [member function]
    def EventPlayerNameChanged(self, PRI: PriXWrapper) -> None: ...

    # Private:
    # PriXWrapper::Impl [class declaration]

    # PriXWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


