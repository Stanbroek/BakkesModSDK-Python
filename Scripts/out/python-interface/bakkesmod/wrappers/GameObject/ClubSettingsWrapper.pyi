from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class ClubSettingsWrapper():
    # Public:
    # ClubSettingsWrapper::ClubSettingsWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ClubSettingsWrapper::ClubSettingsWrapper(ClubSettingsWrapper const & other) [constructor]

    # ClubSettingsWrapper & ClubSettingsWrapper::operator=(ClubSettingsWrapper rhs) [member operator]

    # ClubSettingsWrapper::~ClubSettingsWrapper() [destructor]
    def __del__(self) -> None: ...

    # bool ClubSettingsWrapper::IsNull() const [member function]
    def IsNull(self) -> bool: ...

    # bool ClubSettingsWrapper::operator bool() const [casting operator]

    # UnrealStringWrapper ClubSettingsWrapper::GetClubName() [member function]
    def GetClubName(self) -> UnrealStringWrapper: ...

    # UnrealStringWrapper ClubSettingsWrapper::GetClubTag() [member function]
    def GetClubTag(self) -> UnrealStringWrapper: ...

    # int ClubSettingsWrapper::GetPrimaryColor() [member function]
    def GetPrimaryColor(self) -> int: ...

    # int ClubSettingsWrapper::GetAccentColor() [member function]
    def GetAccentColor(self) -> int: ...

    # Private:
    # ClubSettingsWrapper::Impl [class declaration]

    # ClubSettingsWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


