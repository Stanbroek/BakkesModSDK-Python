from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class ClubDetailsWrapper():
    # Public:
    # ClubDetailsWrapper::ClubDetailsWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ClubDetailsWrapper::ClubDetailsWrapper(ClubDetailsWrapper const & other) [constructor]

    # ClubDetailsWrapper & ClubDetailsWrapper::operator=(ClubDetailsWrapper rhs) [member operator]

    # ClubDetailsWrapper::~ClubDetailsWrapper() [destructor]
    def __del__(self) -> None: ...

    # long long unsigned int ClubDetailsWrapper::GetClubID() [member function]
    def GetClubID(self) -> int: ...

    # SteamID ClubDetailsWrapper::GetOwnerPlayerID() [member function]
    def GetOwnerPlayerID(self) -> SteamID: ...

    # UniqueIDWrapper ClubDetailsWrapper::GetOwnerPlayerUniqueID() [member function]
    def GetOwnerPlayerUniqueID(self) -> UniqueIDWrapper: ...

    # UnrealStringWrapper ClubDetailsWrapper::GetMotD() [member function]
    def GetMotD(self) -> UnrealStringWrapper: ...

    # long unsigned int ClubDetailsWrapper::GetbVerified() [member function]
    def GetbVerified(self) -> bool: ...

    # long long unsigned int ClubDetailsWrapper::GetLastUpdatedTime() [member function]
    def GetLastUpdatedTime(self) -> int: ...

    # StructArrayWrapper<ClubMember> ClubDetailsWrapper::GetMembers() [member function]
    def GetMembers(self) -> StructArrayWrapper_ClubMember: ...

    # Private:
    # ClubDetailsWrapper::Impl [class declaration]

    # ClubDetailsWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


class ClubMember():
    # Public:
    # ClubMember::paddingForReasons [variable]
    @property
    def paddingForReasons(self) -> unsigned char [72]: ...

    # SteamID ClubMember::GetSteamId() [member function]
    def GetSteamId(self) -> SteamID: ...

    # UniqueIDWrapper ClubMember::GetUniqueID() [member function]
    def GetUniqueID(self) -> UniqueIDWrapper: ...

    # UnrealStringWrapper ClubMember::GetName() [member function]
    def GetName(self) -> UnrealStringWrapper: ...

    # ClubMember::ClubMember() [constructor]
    def __init__(self) -> None: ...

    # ClubMember::ClubMember(ClubMember const & arg0) [constructor]

    # ClubMember & ClubMember::operator=(ClubMember const & arg0) [member operator]

    # ClubMember::~ClubMember() [destructor]
    def __del__(self) -> None: ...


