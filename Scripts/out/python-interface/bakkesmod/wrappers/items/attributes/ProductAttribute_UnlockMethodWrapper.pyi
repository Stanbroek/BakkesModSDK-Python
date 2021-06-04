from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class ProductAttribute_UnlockMethodWrapper():
    # Public:
    # ProductAttribute_UnlockMethodWrapper::ProductAttribute_UnlockMethodWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ProductAttribute_UnlockMethodWrapper::ProductAttribute_UnlockMethodWrapper(ProductAttribute_UnlockMethodWrapper const & other) [constructor]

    # ProductAttribute_UnlockMethodWrapper & ProductAttribute_UnlockMethodWrapper::operator=(ProductAttribute_UnlockMethodWrapper rhs) [member operator]

    # ProductAttribute_UnlockMethodWrapper::~ProductAttribute_UnlockMethodWrapper() [destructor]
    def __del__(self) -> None: ...

    # unsigned char ProductAttribute_UnlockMethodWrapper::GetUnlockMethod() [member function]
    def GetUnlockMethod(self) -> int: ...

    # Private:
    # ProductAttribute_UnlockMethodWrapper::Impl [class declaration]

    # ProductAttribute_UnlockMethodWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


