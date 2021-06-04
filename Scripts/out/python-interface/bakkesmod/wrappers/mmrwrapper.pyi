from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class MMRWrapper():
    # Public:
    # MMRWrapper::MMRWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # MMRWrapper::MMRWrapper(MMRWrapper const & other) [constructor]

    # MMRWrapper & MMRWrapper::operator=(MMRWrapper rhs) [member operator]

    # MMRWrapper::~MMRWrapper() [destructor]
    def __del__(self) -> None: ...

    # bool MMRWrapper::IsSyncing(UniqueIDWrapper playerID) [member function]
    def IsSyncing(self, playerID: UniqueIDWrapper) -> bool: ...

    # bool MMRWrapper::IsSyncing(SteamID playerID) [member function]
    def IsSyncing(self, playerID: SteamID) -> bool: ...

    # bool MMRWrapper::IsSynced(UniqueIDWrapper playerID, int playlistID) [member function]
    def IsSynced(self, playerID: UniqueIDWrapper, playlistID: int) -> bool: ...

    # bool MMRWrapper::IsSynced(SteamID playerID, int playlistID) [member function]
    def IsSynced(self, playerID: SteamID, playlistID: int) -> bool: ...

    # bool MMRWrapper::IsRanked(int playlistID) [member function]
    def IsRanked(self, playlistID: int) -> bool: ...

    # SkillRating MMRWrapper::GetPlayerSkillRating(UniqueIDWrapper playerID, int playlistID) [member function]
    def GetPlayerSkillRating(self, playerID: UniqueIDWrapper, playlistID: int) -> SkillRating: ...

    # SkillRank MMRWrapper::GetPlayerRank(UniqueIDWrapper playerID, int playlistID) [member function]
    def GetPlayerRank(self, playerID: UniqueIDWrapper, playlistID: int) -> SkillRank: ...

    # float MMRWrapper::GetPlayerMMR(UniqueIDWrapper playerID, int playlistID) [member function]
    def GetPlayerMMR(self, playerID: UniqueIDWrapper, playlistID: int) -> float: ...

    # SkillRating MMRWrapper::GetPlayerSkillRating(SteamID playerID, int playlistID) [member function]
    def GetPlayerSkillRating(self, playerID: SteamID, playlistID: int) -> SkillRating: ...

    # SkillRank MMRWrapper::GetPlayerRank(SteamID playerID, int playlistID) [member function]
    def GetPlayerRank(self, playerID: SteamID, playlistID: int) -> SkillRank: ...

    # float MMRWrapper::GetPlayerMMR(SteamID playerID, int playlistID) [member function]
    def GetPlayerMMR(self, playerID: SteamID, playlistID: int) -> float: ...

    # float MMRWrapper::CalculateMMR(SkillRating sr, bool disregardPlacements) [member function]
    def CalculateMMR(self, sr: SkillRating, disregardPlacements: bool) -> float: ...

    # int MMRWrapper::GetCurrentPlaylist() [member function]
    def GetCurrentPlaylist(self) -> int: ...

    # std::unique_ptr<MMRNotifierToken, std::default_delete<MMRNotifierToken> > MMRWrapper::RegisterMMRNotifier(std::function<void (UniqueIDWrapper)> arg0) [member function]
    def RegisterMMRNotifier(self, arg0: Callable[[UniqueIDWrapper], None]) -> MMRNotifierToken: ...

    # Private:
    # MMRWrapper::Impl [class declaration]

    # MMRWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


class MMRNotifierToken():
    # Public:
    # MMRNotifierToken::~MMRNotifierToken() [destructor]
    def __del__(self) -> None: ...

    # Private:
    # MMRNotifierToken::MMRNotifierToken(long long unsigned int t) [constructor]
    def __init__(self, t: int) -> None: ...

    # MMRNotifierToken::token [variable]
    @property
    def token(self) -> int: ...


