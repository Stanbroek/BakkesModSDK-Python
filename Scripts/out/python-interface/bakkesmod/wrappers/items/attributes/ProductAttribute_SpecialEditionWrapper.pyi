from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class ProductAttribute_SpecialEditionWrapper():
    # Public:
    # ProductAttribute_SpecialEditionWrapper::ProductAttribute_SpecialEditionWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ProductAttribute_SpecialEditionWrapper::ProductAttribute_SpecialEditionWrapper(ProductAttribute_SpecialEditionWrapper const & other) [constructor]

    # ProductAttribute_SpecialEditionWrapper & ProductAttribute_SpecialEditionWrapper::operator=(ProductAttribute_SpecialEditionWrapper rhs) [member operator]

    # ProductAttribute_SpecialEditionWrapper::~ProductAttribute_SpecialEditionWrapper() [destructor]
    def __del__(self) -> None: ...

    # int ProductAttribute_SpecialEditionWrapper::GetEditionID() [member function]
    def GetEditionID(self) -> int: ...

    # UnrealStringWrapper ProductAttribute_SpecialEditionWrapper::GetSortLabel() [member function]
    def GetSortLabel(self) -> UnrealStringWrapper: ...

    # int ProductAttribute_SpecialEditionWrapper::GetOverrideProductID(int ProductID) [member function]
    def GetOverrideProductID(self, ProductID: int) -> int: ...

    # Private:
    # ProductAttribute_SpecialEditionWrapper::Impl [class declaration]

    # ProductAttribute_SpecialEditionWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


