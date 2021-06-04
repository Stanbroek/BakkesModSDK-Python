from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class UniqueIDWrapper():
    # Public:
    # UniqueIDWrapper::UniqueIDWrapper() [constructor]
    def __init__(self) -> None: ...

    # UniqueIDWrapper::UniqueIDWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # UniqueIDWrapper::UniqueIDWrapper(UniqueIDWrapper const & other) [constructor]

    # UniqueIDWrapper & UniqueIDWrapper::operator=(UniqueIDWrapper rhs) [member operator]

    # UniqueIDWrapper::~UniqueIDWrapper() [destructor]
    def __del__(self) -> None: ...

    # OnlinePlatform UniqueIDWrapper::GetPlatform() const [member function]
    def GetPlatform(self) -> OnlinePlatform: ...

    # std::string UniqueIDWrapper::GetEpicAccountID() const [member function]
    def GetEpicAccountID(self) -> str: ...

    # long long unsigned int UniqueIDWrapper::GetUID() const [member function]
    def GetUID(self) -> int: ...

    # unsigned char UniqueIDWrapper::GetSplitscreenID() const [member function]
    def GetSplitscreenID(self) -> int: ...

    # std::string UniqueIDWrapper::str() const [member function]
    def str(self) -> str: ...

    # std::string UniqueIDWrapper::GetIdString() const [member function]
    def GetIdString(self) -> str: ...

    # static UniqueIDWrapper UniqueIDWrapper::FromEpicAccountID(std::string epicAccountID, long long unsigned int uid, OnlinePlatform platform, unsigned char splitscreenID=0) [member function]
    def FromEpicAccountID(self, epicAccountID: str, uid: int, platform: OnlinePlatform, splitscreenID: int = 0) -> UniqueIDWrapper: ...

    # bool UniqueIDWrapper::operator<(UniqueIDWrapper const & rhs) const [member operator]
    def __lt__(self, other: UniqueIDWrapper) -> bool: ...

    # bool UniqueIDWrapper::operator==(UniqueIDWrapper const & rhs) const [member operator]
    def __eq__(self, other: UniqueIDWrapper) -> bool: ...

    # bool UniqueIDWrapper::operator!=(UniqueIDWrapper const & rhs) const [member operator]
    def __ne__(self, other: UniqueIDWrapper) -> bool: ...

    # Protected:
    # UniqueIDWrapper::Impl [class declaration]

    # UniqueIDWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


