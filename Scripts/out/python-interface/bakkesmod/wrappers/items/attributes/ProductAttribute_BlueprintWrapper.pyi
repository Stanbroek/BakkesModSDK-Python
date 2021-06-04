from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class ProductAttribute_BlueprintWrapper():
    # Public:
    # ProductAttribute_BlueprintWrapper::ProductAttribute_BlueprintWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ProductAttribute_BlueprintWrapper::ProductAttribute_BlueprintWrapper(ProductAttribute_BlueprintWrapper const & other) [constructor]

    # ProductAttribute_BlueprintWrapper & ProductAttribute_BlueprintWrapper::operator=(ProductAttribute_BlueprintWrapper rhs) [member operator]

    # ProductAttribute_BlueprintWrapper::~ProductAttribute_BlueprintWrapper() [destructor]
    def __del__(self) -> None: ...

    # int ProductAttribute_BlueprintWrapper::GetProductID() [member function]
    def GetProductID(self) -> int: ...

    # int ProductAttribute_BlueprintWrapper::GetCachedBlueprintSeriesID() [member function]
    def GetCachedBlueprintSeriesID(self) -> int: ...

    # UnrealStringWrapper ProductAttribute_BlueprintWrapper::GetSortLabel() [member function]
    def GetSortLabel(self) -> UnrealStringWrapper: ...

    # Private:
    # ProductAttribute_BlueprintWrapper::Impl [class declaration]

    # ProductAttribute_BlueprintWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


