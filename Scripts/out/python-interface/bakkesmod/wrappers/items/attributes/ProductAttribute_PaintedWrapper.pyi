from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class ProductAttribute_PaintedWrapper():
    # Public:
    # ProductAttribute_PaintedWrapper::ProductAttribute_PaintedWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ProductAttribute_PaintedWrapper::ProductAttribute_PaintedWrapper(ProductAttribute_PaintedWrapper const & other) [constructor]

    # ProductAttribute_PaintedWrapper & ProductAttribute_PaintedWrapper::operator=(ProductAttribute_PaintedWrapper rhs) [member operator]

    # ProductAttribute_PaintedWrapper::~ProductAttribute_PaintedWrapper() [destructor]
    def __del__(self) -> None: ...

    # int ProductAttribute_PaintedWrapper::GetPaintID() [member function]
    def GetPaintID(self) -> int: ...

    # UnrealStringWrapper ProductAttribute_PaintedWrapper::GetSortLabel() [member function]
    def GetSortLabel(self) -> UnrealStringWrapper: ...

    # Private:
    # ProductAttribute_PaintedWrapper::Impl [class declaration]

    # ProductAttribute_PaintedWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


