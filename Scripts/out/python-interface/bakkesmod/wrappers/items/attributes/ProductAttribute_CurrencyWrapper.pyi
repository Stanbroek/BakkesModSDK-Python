from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class ProductAttribute_CurrencyWrapper():
    # Public:
    # ProductAttribute_CurrencyWrapper::ProductAttribute_CurrencyWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ProductAttribute_CurrencyWrapper::ProductAttribute_CurrencyWrapper(ProductAttribute_CurrencyWrapper const & other) [constructor]

    # ProductAttribute_CurrencyWrapper & ProductAttribute_CurrencyWrapper::operator=(ProductAttribute_CurrencyWrapper rhs) [member operator]

    # ProductAttribute_CurrencyWrapper::~ProductAttribute_CurrencyWrapper() [destructor]
    def __del__(self) -> None: ...

    # int ProductAttribute_CurrencyWrapper::GetCurrencyID() [member function]
    def GetCurrencyID(self) -> int: ...

    # UnrealStringWrapper ProductAttribute_CurrencyWrapper::GetSortLabel() [member function]
    def GetSortLabel(self) -> UnrealStringWrapper: ...

    # Private:
    # ProductAttribute_CurrencyWrapper::Impl [class declaration]

    # ProductAttribute_CurrencyWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


