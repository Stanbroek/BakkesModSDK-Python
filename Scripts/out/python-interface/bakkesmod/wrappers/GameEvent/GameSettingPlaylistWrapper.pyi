from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class GameSettingPlaylistWrapper():
    # Public:
    # GameSettingPlaylistWrapper::GameSettingPlaylistWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # GameSettingPlaylistWrapper::GameSettingPlaylistWrapper(GameSettingPlaylistWrapper const & other) [constructor]

    # GameSettingPlaylistWrapper & GameSettingPlaylistWrapper::operator=(GameSettingPlaylistWrapper rhs) [member operator]

    # GameSettingPlaylistWrapper::~GameSettingPlaylistWrapper() [destructor]
    def __del__(self) -> None: ...

    # bool GameSettingPlaylistWrapper::IsNull() const [member function]
    def IsNull(self) -> bool: ...

    # bool GameSettingPlaylistWrapper::operator bool() const [casting operator]

    # UnrealStringWrapper GameSettingPlaylistWrapper::GetTitle() [member function]
    def GetTitle(self) -> UnrealStringWrapper: ...

    # UnrealStringWrapper GameSettingPlaylistWrapper::GetDescription() [member function]
    def GetDescription(self) -> UnrealStringWrapper: ...

    # int GameSettingPlaylistWrapper::GetPlayerCount() [member function]
    def GetPlayerCount(self) -> int: ...

    # void GameSettingPlaylistWrapper::SetPlayerCount(int newPlayerCount) [member function]
    def SetPlayerCount(self, newPlayerCount: int) -> None: ...

    # long unsigned int GameSettingPlaylistWrapper::GetbStandard() [member function]
    def GetbStandard(self) -> bool: ...

    # void GameSettingPlaylistWrapper::SetbStandard(long unsigned int newbStandard) [member function]
    def SetbStandard(self, newbStandard: bool) -> None: ...

    # long unsigned int GameSettingPlaylistWrapper::GetbRanked() [member function]
    def GetbRanked(self) -> bool: ...

    # void GameSettingPlaylistWrapper::SetbRanked(long unsigned int newbRanked) [member function]
    def SetbRanked(self, newbRanked: bool) -> None: ...

    # long unsigned int GameSettingPlaylistWrapper::GetbSolo() [member function]
    def GetbSolo(self) -> bool: ...

    # void GameSettingPlaylistWrapper::SetbSolo(long unsigned int newbSolo) [member function]
    def SetbSolo(self, newbSolo: bool) -> None: ...

    # long unsigned int GameSettingPlaylistWrapper::GetbNew() [member function]
    def GetbNew(self) -> bool: ...

    # void GameSettingPlaylistWrapper::SetbNew(long unsigned int newbNew) [member function]
    def SetbNew(self, newbNew: bool) -> None: ...

    # long unsigned int GameSettingPlaylistWrapper::GetbApplyQuitPenalty() [member function]
    def GetbApplyQuitPenalty(self) -> bool: ...

    # void GameSettingPlaylistWrapper::SetbApplyQuitPenalty(long unsigned int newbApplyQuitPenalty) [member function]
    def SetbApplyQuitPenalty(self, newbApplyQuitPenalty: bool) -> None: ...

    # long unsigned int GameSettingPlaylistWrapper::GetbAllowForfeit() [member function]
    def GetbAllowForfeit(self) -> bool: ...

    # void GameSettingPlaylistWrapper::SetbAllowForfeit(long unsigned int newbAllowForfeit) [member function]
    def SetbAllowForfeit(self, newbAllowForfeit: bool) -> None: ...

    # long unsigned int GameSettingPlaylistWrapper::GetbDisableRankedReconnect() [member function]
    def GetbDisableRankedReconnect(self) -> bool: ...

    # void GameSettingPlaylistWrapper::SetbDisableRankedReconnect(long unsigned int newbDisableRankedReconnect) [member function]
    def SetbDisableRankedReconnect(self, newbDisableRankedReconnect: bool) -> None: ...

    # long unsigned int GameSettingPlaylistWrapper::GetbIgnoreAssignTeams() [member function]
    def GetbIgnoreAssignTeams(self) -> bool: ...

    # void GameSettingPlaylistWrapper::SetbIgnoreAssignTeams(long unsigned int newbIgnoreAssignTeams) [member function]
    def SetbIgnoreAssignTeams(self, newbIgnoreAssignTeams: bool) -> None: ...

    # long unsigned int GameSettingPlaylistWrapper::GetbKickOnMigrate() [member function]
    def GetbKickOnMigrate(self) -> bool: ...

    # void GameSettingPlaylistWrapper::SetbKickOnMigrate(long unsigned int newbKickOnMigrate) [member function]
    def SetbKickOnMigrate(self, newbKickOnMigrate: bool) -> None: ...

    # long unsigned int GameSettingPlaylistWrapper::GetbAllowClubs() [member function]
    def GetbAllowClubs(self) -> bool: ...

    # void GameSettingPlaylistWrapper::SetbAllowClubs(long unsigned int newbAllowClubs) [member function]
    def SetbAllowClubs(self, newbAllowClubs: bool) -> None: ...

    # long unsigned int GameSettingPlaylistWrapper::GetbPlayersVSBots() [member function]
    def GetbPlayersVSBots(self) -> bool: ...

    # void GameSettingPlaylistWrapper::SetbPlayersVSBots(long unsigned int newbPlayersVSBots) [member function]
    def SetbPlayersVSBots(self, newbPlayersVSBots: bool) -> None: ...

    # int GameSettingPlaylistWrapper::GetPlaylistId() [member function]
    def GetPlaylistId(self) -> int: ...

    # void GameSettingPlaylistWrapper::SetPlaylistId(int newPlaylistId) [member function]
    def SetPlaylistId(self, newPlaylistId: int) -> None: ...

    # UnrealStringWrapper GameSettingPlaylistWrapper::GetServerCommand() [member function]
    def GetServerCommand(self) -> UnrealStringWrapper: ...

    # bool GameSettingPlaylistWrapper::IsLanMatch() [member function]
    def IsLanMatch(self) -> bool: ...

    # bool GameSettingPlaylistWrapper::IsPrivateMatch() [member function]
    def IsPrivateMatch(self) -> bool: ...

    # bool GameSettingPlaylistWrapper::ShouldUpdateSkills() [member function]
    def ShouldUpdateSkills(self) -> bool: ...

    # bool GameSettingPlaylistWrapper::IsValidID(int InPlaylistID) [member function]
    def IsValidID(self, InPlaylistID: int) -> bool: ...

    # bool GameSettingPlaylistWrapper::IsValid2() [member function]
    def IsValid2(self) -> bool: ...

    # Private:
    # GameSettingPlaylistWrapper::Impl [class declaration]

    # GameSettingPlaylistWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


