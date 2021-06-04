from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class ProductAttribute_TeamEditionWrapper():
    # Public:
    # ProductAttribute_TeamEditionWrapper::ProductAttribute_TeamEditionWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ProductAttribute_TeamEditionWrapper::ProductAttribute_TeamEditionWrapper(ProductAttribute_TeamEditionWrapper const & other) [constructor]

    # ProductAttribute_TeamEditionWrapper & ProductAttribute_TeamEditionWrapper::operator=(ProductAttribute_TeamEditionWrapper rhs) [member operator]

    # ProductAttribute_TeamEditionWrapper::~ProductAttribute_TeamEditionWrapper() [destructor]
    def __del__(self) -> None: ...

    # int ProductAttribute_TeamEditionWrapper::GetId() [member function]
    def GetId(self) -> int: ...

    # UnrealStringWrapper ProductAttribute_TeamEditionWrapper::GetSortLabel() [member function]
    def GetSortLabel(self) -> UnrealStringWrapper: ...

    # Private:
    # ProductAttribute_TeamEditionWrapper::Impl [class declaration]

    # ProductAttribute_TeamEditionWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


