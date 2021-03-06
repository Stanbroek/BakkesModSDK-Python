from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

# WrapperStructs [class declaration]

class TeamWrapper():
    # Public:
    # TeamWrapper::TeamWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # TeamWrapper::TeamWrapper(TeamWrapper const & other) [constructor]

    # TeamWrapper & TeamWrapper::operator=(TeamWrapper rhs) [member operator]

    # TeamWrapper::~TeamWrapper() [destructor]
    def __del__(self) -> None: ...

    # LinearColor TeamWrapper::GetPrimaryColor() [member function]
    def GetPrimaryColor(self) -> LinearColor: ...

    # LinearColor TeamWrapper::GetSecondaryColor() [member function]
    def GetSecondaryColor(self) -> LinearColor: ...

    # LinearColor TeamWrapper::GetFontColor() [member function]
    def GetFontColor(self) -> LinearColor: ...

    # void TeamWrapper::SetFontColor(LinearColor newFontColor) [member function]
    def SetFontColor(self, newFontColor: LinearColor) -> None: ...

    # LinearColor TeamWrapper::GetColorBlindFontColor() [member function]
    def GetColorBlindFontColor(self) -> LinearColor: ...

    # void TeamWrapper::SetColorBlindFontColor(LinearColor newColorBlindFontColor) [member function]
    def SetColorBlindFontColor(self, newColorBlindFontColor: LinearColor) -> None: ...

    # UnrealColor TeamWrapper::GetTeamControllerColor() [member function]
    def GetTeamControllerColor(self) -> UnrealColor: ...

    # void TeamWrapper::SetTeamControllerColor(UnrealColor newTeamControllerColor) [member function]
    def SetTeamControllerColor(self, newTeamControllerColor: UnrealColor) -> None: ...

    # UnrealColor TeamWrapper::GetTeamScoreStrobeColor() [member function]
    def GetTeamScoreStrobeColor(self) -> UnrealColor: ...

    # void TeamWrapper::SetTeamScoreStrobeColor(UnrealColor newTeamScoreStrobeColor) [member function]
    def SetTeamScoreStrobeColor(self, newTeamScoreStrobeColor: UnrealColor) -> None: ...

    # StructArrayWrapper<LinearColor> TeamWrapper::GetDefaultColorList() [member function]
    def GetDefaultColorList(self) -> StructArrayWrapper_LinearColor: ...

    # StructArrayWrapper<LinearColor> TeamWrapper::GetColorBlindColorList() [member function]
    def GetColorBlindColorList(self) -> StructArrayWrapper_LinearColor: ...

    # StructArrayWrapper<LinearColor> TeamWrapper::GetCurrentColorList() [member function]
    def GetCurrentColorList(self) -> StructArrayWrapper_LinearColor: ...

    # TeamGameEventWrapper TeamWrapper::GetGameEvent() [member function]
    def GetGameEvent(self) -> TeamGameEventWrapper: ...

    # void TeamWrapper::SetGameEvent(TeamGameEventWrapper newGameEvent) [member function]
    def SetGameEvent(self, newGameEvent: TeamGameEventWrapper) -> None: ...

    # ArrayWrapper<PriWrapper> TeamWrapper::GetMembers() [member function]
    def GetMembers(self) -> ArrayWrapper_PriWrapper: ...

    # UnrealStringWrapper TeamWrapper::GetCustomTeamName() [member function]
    def GetCustomTeamName(self) -> UnrealStringWrapper: ...

    # UnrealStringWrapper TeamWrapper::GetSanitizedTeamName() [member function]
    def GetSanitizedTeamName(self) -> UnrealStringWrapper: ...

    # long long unsigned int TeamWrapper::GetClubID() [member function]
    def GetClubID(self) -> int: ...

    # void TeamWrapper::SetClubID(long long unsigned int newClubID) [member function]
    def SetClubID(self, newClubID: int) -> None: ...

    # long unsigned int TeamWrapper::GetbForfeit() [member function]
    def GetbForfeit(self) -> bool: ...

    # void TeamWrapper::SetbForfeit(long unsigned int newbForfeit) [member function]
    def SetbForfeit(self, newbForfeit: bool) -> None: ...

    # bool TeamWrapper::__Team_TA__GetHumanPlayers(PriWrapper PRI) [member function]
    def __Team_TA__GetHumanPlayers(self, PRI: PriWrapper) -> bool: ...

    # bool TeamWrapper::__Team_TA__GetHumanPrimaryPlayers(PriWrapper PRI) [member function]
    def __Team_TA__GetHumanPrimaryPlayers(self, PRI: PriWrapper) -> bool: ...

    # bool TeamWrapper::__Team_TA__GetNumOfMembersThatCanStartForfeit(PriWrapper P) [member function]
    def __Team_TA__GetNumOfMembersThatCanStartForfeit(self, P: PriWrapper) -> bool: ...

    # void TeamWrapper::__Team_TA__EnableAllMembersStartVoteToForfeit(PriWrapper Member) [member function]
    def __Team_TA__EnableAllMembersStartVoteToForfeit(self, Member: PriWrapper) -> None: ...

    # void TeamWrapper::OnClubColorsChanged() [member function]
    def OnClubColorsChanged(self) -> None: ...

    # void TeamWrapper::Forfeit2() [member function]
    def Forfeit2(self) -> None: ...

    # void TeamWrapper::EnableAllMembersStartVoteToForfeit2() [member function]
    def EnableAllMembersStartVoteToForfeit2(self) -> None: ...

    # void TeamWrapper::EnableAllMembersStartVoteToForfeitIfNecessary() [member function]
    def EnableAllMembersStartVoteToForfeitIfNecessary(self) -> None: ...

    # void TeamWrapper::VoteToForfeit22(PriWrapper PRI) [member function]
    def VoteToForfeit22(self, PRI: PriWrapper) -> None: ...

    # void TeamWrapper::NotifyKismetTeamColorChanged() [member function]
    def NotifyKismetTeamColorChanged(self) -> None: ...

    # void TeamWrapper::UpdateColors() [member function]
    def UpdateColors(self) -> None: ...

    # void TeamWrapper::SetLogo(int LogoID, long unsigned int bSwapColors) [member function]
    def SetLogo(self, LogoID: int, bSwapColors: bool) -> None: ...

    # void TeamWrapper::HandleTeamNameSanitized(std::string Original, std::string Sanitized) [member function]
    def HandleTeamNameSanitized(self, Original: str, Sanitized: str) -> None: ...

    # void TeamWrapper::SetClubID2(long long unsigned int InClubID) [member function]
    def SetClubID2(self, InClubID: int) -> None: ...

    # void TeamWrapper::SetCustomTeamName(std::string NewName) [member function]
    def SetCustomTeamName(self, NewName: str) -> None: ...

    # void TeamWrapper::SetDefaultColors() [member function]
    def SetDefaultColors(self) -> None: ...

    # bool TeamWrapper::IsSingleParty() [member function]
    def IsSingleParty(self) -> bool: ...

    # PriWrapper TeamWrapper::GetTeamMemberNamed(std::string PlayerName) [member function]
    def GetTeamMemberNamed(self, PlayerName: str) -> PriWrapper: ...

    # int TeamWrapper::GetNumBots() [member function]
    def GetNumBots(self) -> int: ...

    # int TeamWrapper::GetNumHumans() [member function]
    def GetNumHumans(self) -> int: ...

    # void TeamWrapper::OnScoreUpdated() [member function]
    def OnScoreUpdated(self) -> None: ...

    # void TeamWrapper::ResetScore() [member function]
    def ResetScore(self) -> None: ...

    # void TeamWrapper::RemovePoints(int Points) [member function]
    def RemovePoints(self, Points: int) -> None: ...

    # void TeamWrapper::SetScore(int Points) [member function]
    def SetScore(self, Points: int) -> None: ...

    # void TeamWrapper::ScorePoint(int AdditionalScore) [member function]
    def ScorePoint(self, AdditionalScore: int) -> None: ...

    # void TeamWrapper::MuteOtherTeam(TeamWrapper OtherTeam, long unsigned int bMute) [member function]
    def MuteOtherTeam(self, OtherTeam: TeamWrapper, bMute: bool) -> None: ...

    # void TeamWrapper::ClearTemporarySpawnSpots() [member function]
    def ClearTemporarySpawnSpots(self) -> None: ...

    # void TeamWrapper::ExpireTemporarySpawnSpots() [member function]
    def ExpireTemporarySpawnSpots(self) -> None: ...

    # void TeamWrapper::AddTemporarySpawnSpot(ActorWrapper AtActor) [member function]
    def AddTemporarySpawnSpot(self, AtActor: ActorWrapper) -> None: ...

    # void TeamWrapper::OnGameEventSet() [member function]
    def OnGameEventSet(self) -> None: ...

    # void TeamWrapper::SetGameEvent2(TeamGameEventWrapper InGameEvent) [member function]
    def SetGameEvent2(self, InGameEvent: TeamGameEventWrapper) -> None: ...

    # Private:
    # TeamWrapper::Impl [class declaration]

    # TeamWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


