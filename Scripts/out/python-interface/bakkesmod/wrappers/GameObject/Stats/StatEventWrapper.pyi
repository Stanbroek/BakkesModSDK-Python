from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class StatEventWrapper():
    # Public:
    # StatEventWrapper::StatEventWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # StatEventWrapper::StatEventWrapper(StatEventWrapper const & other) [constructor]

    # StatEventWrapper & StatEventWrapper::operator=(StatEventWrapper rhs) [member operator]

    # StatEventWrapper::~StatEventWrapper() [destructor]
    def __del__(self) -> None: ...

    # bool StatEventWrapper::IsNull() const [member function]
    def IsNull(self) -> bool: ...

    # bool StatEventWrapper::operator bool() const [casting operator]

    # int StatEventWrapper::GetPoints() [member function]
    def GetPoints(self) -> int: ...

    # float StatEventWrapper::GetCooldownSeconds() [member function]
    def GetCooldownSeconds(self) -> float: ...

    # long unsigned int StatEventWrapper::GetbAddToScore() [member function]
    def GetbAddToScore(self) -> bool: ...

    # long unsigned int StatEventWrapper::GetbIsLeaderboardStat() [member function]
    def GetbIsLeaderboardStat(self) -> bool: ...

    # long unsigned int StatEventWrapper::GetbNotifyTicker() [member function]
    def GetbNotifyTicker(self) -> bool: ...

    # long unsigned int StatEventWrapper::GetbShowOnHUD() [member function]
    def GetbShowOnHUD(self) -> bool: ...

    # long unsigned int StatEventWrapper::GetbPrimaryStat() [member function]
    def GetbPrimaryStat(self) -> bool: ...

    # long unsigned int StatEventWrapper::GetbSkipReplication() [member function]
    def GetbSkipReplication(self) -> bool: ...

    # long unsigned int StatEventWrapper::GetbCanMute() [member function]
    def GetbCanMute(self) -> bool: ...

    # long unsigned int StatEventWrapper::GetbCountMultiplied() [member function]
    def GetbCountMultiplied(self) -> bool: ...

    # UnrealStringWrapper StatEventWrapper::GetLabel() [member function]
    def GetLabel(self) -> UnrealStringWrapper: ...

    # UnrealStringWrapper StatEventWrapper::GetPluralLabel() [member function]
    def GetPluralLabel(self) -> UnrealStringWrapper: ...

    # UnrealStringWrapper StatEventWrapper::GetDescription() [member function]
    def GetDescription(self) -> UnrealStringWrapper: ...

    # float StatEventWrapper::GetNextCooldownTime() [member function]
    def GetNextCooldownTime(self) -> float: ...

    # std::string StatEventWrapper::GetGroupName() [member function]
    def GetGroupName(self) -> str: ...

    # std::string StatEventWrapper::GetEventName() [member function]
    def GetEventName(self) -> str: ...

    # Private:
    # StatEventWrapper::Impl [class declaration]

    # StatEventWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


