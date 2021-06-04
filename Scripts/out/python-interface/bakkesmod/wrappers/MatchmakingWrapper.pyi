from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class MatchmakingWrapper():
    # Public:
    # MatchmakingWrapper::MatchmakingWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # MatchmakingWrapper::MatchmakingWrapper(MatchmakingWrapper const & other) [constructor]

    # MatchmakingWrapper & MatchmakingWrapper::operator=(MatchmakingWrapper rhs) [member operator]

    # MatchmakingWrapper::~MatchmakingWrapper() [destructor]
    def __del__(self) -> None: ...

    # bool MatchmakingWrapper::IsNull() const [member function]
    def IsNull(self) -> bool: ...

    # bool MatchmakingWrapper::operator bool() const [casting operator]

    # bool MatchmakingWrapper::IsSearching() [member function]
    def IsSearching(self) -> bool: ...

    # int MatchmakingWrapper::GetActiveViewTab() [member function]
    def GetActiveViewTab(self) -> int: ...

    # void MatchmakingWrapper::SetRegionSelection(Region region, bool bSelected) [member function]
    def SetRegionSelection(self, region: Region, bSelected: bool) -> None: ...

    # void MatchmakingWrapper::SetPlaylistSelection(Playlist playlist, bool bSelected) [member function]
    def SetPlaylistSelection(self, playlist: Playlist, bSelected: bool) -> None: ...

    # void MatchmakingWrapper::StartMatchmaking(PlaylistCategory playlist_category) [member function]
    def StartMatchmaking(self, playlist_category: PlaylistCategory) -> None: ...

    # void MatchmakingWrapper::CancelMatchmaking() [member function]
    def CancelMatchmaking(self) -> None: ...

    # void MatchmakingWrapper::CreatePrivateMatch(Region region, CustomMatchSettings const & match_settings) [member function]
    def CreatePrivateMatch(self, region: Region, match_settings: CustomMatchSettings) -> None: ...

    # void MatchmakingWrapper::JoinPrivateMatch(std::string const & server_name, std::string const & server_password="") [member function]
    def JoinPrivateMatch(self, server_name: str, server_password: str = "") -> None: ...

    # int MatchmakingWrapper::SeasonEndDays() [member function]
    def SeasonEndDays(self) -> int: ...

    # int MatchmakingWrapper::SeasonEndHours() [member function]
    def SeasonEndHours(self) -> int: ...

    # int MatchmakingWrapper::SeasonEndMinutes() [member function]
    def SeasonEndMinutes(self) -> int: ...

    # int MatchmakingWrapper::GetSeasonTimeRemaining() [member function]
    def GetSeasonTimeRemaining(self) -> int: ...

    # int MatchmakingWrapper::GetSeasonEndTimeSeconds() [member function]
    def GetSeasonEndTimeSeconds(self) -> int: ...

    # bool MatchmakingWrapper::HasSeasonEnded() [member function]
    def HasSeasonEnded(self) -> bool: ...

    # int MatchmakingWrapper::GetTotalPopulation() [member function]
    def GetTotalPopulation(self) -> int: ...

    # static std::string MatchmakingWrapper::GetRegionID(Region region) [member function]
    def GetRegionID(self, region: Region) -> str: ...

    # static std::string MatchmakingWrapper::GetRegionLabel(Region region) [member function]
    def GetRegionLabel(self, region: Region) -> str: ...

    # Private:
    # MatchmakingWrapper::Impl [class declaration]

    # MatchmakingWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


# Region [enumeration]
class Region(Enum):
    USE = 0
    EU = 1
    USW = 2
    ASC = 3
    ASM = 4
    JPN = 5
    ME = 6
    OCE = 7
    SAF = 8
    SAM = 9

# Playlist [enumeration]
class Playlist(Enum):
    CASUAL_STANDARD = 0
    CASUAL_DOUBLES = 1
    CASUAL_DUELS = 2
    CASUAL_CHAOS = 3
    RANKED_STANDARD = 4
    RANKED_DOUBLES = 5
    RANKED_DUELS = 6
    EXTRAS_RUMBLE = 12
    EXTRAS_DROPSHOT = 13
    EXTRAS_HOOPS = 14
    EXTRAS_SNOWDAY = 15

# PlaylistCategory [enumeration]
class PlaylistCategory(Enum):
    CASUAL = 0
    RANKED = 1
    EXTRAS = 2

class ClubColorSet():
    # Public:
    # ClubColorSet::TeamColorID [variable]
    @property
    def TeamColorID(self) -> int: ...

    # ClubColorSet::CustomColorID [variable]
    @property
    def CustomColorID(self) -> int: ...

    # ClubColorSet::bTeamColorSet [variable]
    @property
    def bTeamColorSet(self) -> bool: ...

    # ClubColorSet::bCustomColorSet [variable]
    @property
    def bCustomColorSet(self) -> bool: ...

    # ClubColorSet::ClubColorSet(ClubColorSet const & arg0) [constructor]

    # ClubColorSet::~ClubColorSet() [destructor]
    def __del__(self) -> None: ...

    # ClubColorSet & ClubColorSet::operator=(ClubColorSet const & arg0) [member operator]

    # ClubColorSet::ClubColorSet() [constructor]
    def __init__(self) -> None: ...


class CustomMatchTeamSettings():
    # Public:
    # CustomMatchTeamSettings::Name [variable]
    @property
    def Name(self) -> str: ...

    # CustomMatchTeamSettings::Colors [variable]
    @property
    def Colors(self) -> ClubColorSet: ...

    # CustomMatchTeamSettings::GameScore [variable]
    @property
    def GameScore(self) -> int: ...

    # CustomMatchTeamSettings::CustomMatchTeamSettings(CustomMatchTeamSettings const & arg0) [constructor]

    # CustomMatchTeamSettings::~CustomMatchTeamSettings() [destructor]
    def __del__(self) -> None: ...

    # CustomMatchTeamSettings & CustomMatchTeamSettings::operator=(CustomMatchTeamSettings const & arg0) [member operator]

    # CustomMatchTeamSettings::CustomMatchTeamSettings() [constructor]
    def __init__(self) -> None: ...


class CustomMatchSettings():
    # Public:
    # CustomMatchSettings::GameTags [variable]
    @property
    def GameTags(self) -> str: ...

    # CustomMatchSettings::MapName [variable]
    @property
    def MapName(self) -> str: ...

    # CustomMatchSettings::ServerName [variable]
    @property
    def ServerName(self) -> str: ...

    # CustomMatchSettings::Password [variable]
    @property
    def Password(self) -> str: ...

    # CustomMatchSettings::BlueTeamSettings [variable]
    @property
    def BlueTeamSettings(self) -> CustomMatchTeamSettings: ...

    # CustomMatchSettings::OrangeTeamSettings [variable]
    @property
    def OrangeTeamSettings(self) -> CustomMatchTeamSettings: ...

    # CustomMatchSettings::GameMode [variable]
    @property
    def GameMode(self) -> int: ...

    # CustomMatchSettings::MaxPlayerCount [variable]
    @property
    def MaxPlayerCount(self) -> int: ...

    # CustomMatchSettings::bPartyMembersOnly [variable]
    @property
    def bPartyMembersOnly(self) -> bool: ...

    # CustomMatchSettings::bClubServer [variable]
    @property
    def bClubServer(self) -> bool: ...

    # CustomMatchSettings::CustomMatchSettings(CustomMatchSettings const & arg0) [constructor]

    # CustomMatchSettings::~CustomMatchSettings() [destructor]
    def __del__(self) -> None: ...

    # CustomMatchSettings::CustomMatchSettings() [constructor]
    def __init__(self) -> None: ...

    # CustomMatchSettings & CustomMatchSettings::operator=(CustomMatchSettings const & arg0) [member operator]


