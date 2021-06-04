from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class LoadoutWrapper():
    # Public:
    # LoadoutWrapper::LoadoutWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # LoadoutWrapper::LoadoutWrapper(LoadoutWrapper const & other) [constructor]

    # LoadoutWrapper & LoadoutWrapper::operator=(LoadoutWrapper rhs) [member operator]

    # LoadoutWrapper::~LoadoutWrapper() [destructor]
    def __del__(self) -> None: ...

    # bool LoadoutWrapper::IsNull() const [member function]
    def IsNull(self) -> bool: ...

    # bool LoadoutWrapper::operator bool() const [casting operator]

    # ArrayWrapper<int> LoadoutWrapper::GetLoadout() [member function]
    def GetLoadout(self) -> ArrayWrapper_int: ...

    # ArrayWrapper<unsigned long long> LoadoutWrapper::GetOnlineLoadout() [member function]
    def GetOnlineLoadout(self) -> ArrayWrapper_unsigned_long_long: ...

    # unsigned char LoadoutWrapper::GetPrimaryPaintColorId() [member function]
    def GetPrimaryPaintColorId(self) -> int: ...

    # unsigned char LoadoutWrapper::GetAccentPaintColorId() [member function]
    def GetAccentPaintColorId(self) -> int: ...

    # int LoadoutWrapper::GetPrimaryFinishId() [member function]
    def GetPrimaryFinishId(self) -> int: ...

    # int LoadoutWrapper::GetAccentFinishId() [member function]
    def GetAccentFinishId(self) -> int: ...

    # Private:
    # LoadoutWrapper::Impl [class declaration]

    # LoadoutWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


