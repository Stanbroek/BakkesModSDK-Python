from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class UnrealStringWrapper():
    # Public:
    # UnrealStringWrapper::UnrealStringWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # UnrealStringWrapper::UnrealStringWrapper(UnrealStringWrapper const & other) [constructor]

    # UnrealStringWrapper & UnrealStringWrapper::operator=(UnrealStringWrapper rhs) [member operator]

    # UnrealStringWrapper::~UnrealStringWrapper() [destructor]
    def __del__(self) -> None: ...

    # std::string UnrealStringWrapper::ToString() [member function]
    def ToString(self) -> str: ...

    # std::wstring UnrealStringWrapper::ToWideString() [member function]
    def ToWideString(self) -> str: ...

    # bool UnrealStringWrapper::IsNull() [member function]
    def IsNull(self) -> bool: ...

    # bool UnrealStringWrapper::operator bool() [casting operator]

    # Private:
    # UnrealStringWrapper::Impl [class declaration]

    # UnrealStringWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


