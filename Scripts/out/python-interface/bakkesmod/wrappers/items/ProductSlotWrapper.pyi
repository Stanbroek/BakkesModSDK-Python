from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class ProductSlotWrapper():
    # Public:
    # ProductSlotWrapper::ProductSlotWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ProductSlotWrapper::ProductSlotWrapper(ProductSlotWrapper const & other) [constructor]

    # ProductSlotWrapper & ProductSlotWrapper::operator=(ProductSlotWrapper rhs) [member operator]

    # ProductSlotWrapper::~ProductSlotWrapper() [destructor]
    def __del__(self) -> None: ...

    # bool ProductSlotWrapper::IsNull() const [member function]
    def IsNull(self) -> bool: ...

    # bool ProductSlotWrapper::operator bool() const [casting operator]

    # UnrealStringWrapper ProductSlotWrapper::GetLabel() [member function]
    def GetLabel(self) -> UnrealStringWrapper: ...

    # UnrealStringWrapper ProductSlotWrapper::GetPluralLabel() [member function]
    def GetPluralLabel(self) -> UnrealStringWrapper: ...

    # UnrealStringWrapper ProductSlotWrapper::GetDescription() [member function]
    def GetDescription(self) -> UnrealStringWrapper: ...

    # UnrealStringWrapper ProductSlotWrapper::GetOnlineLabel() [member function]
    def GetOnlineLabel(self) -> UnrealStringWrapper: ...

    # int ProductSlotWrapper::GetSlotIndex() [member function]
    def GetSlotIndex(self) -> int: ...

    # Private:
    # ProductSlotWrapper::Impl [class declaration]

    # ProductSlotWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


