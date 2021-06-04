from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class ProductTradeInWrapper():
    # Public:
    # ProductTradeInWrapper::ProductTradeInWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ProductTradeInWrapper::ProductTradeInWrapper(ProductTradeInWrapper const & other) [constructor]

    # ProductTradeInWrapper & ProductTradeInWrapper::operator=(ProductTradeInWrapper rhs) [member operator]

    # ProductTradeInWrapper::~ProductTradeInWrapper() [destructor]
    def __del__(self) -> None: ...

    # ArrayWrapper<OnlineProductWrapper> ProductTradeInWrapper::GetProducts() const [member function]
    def GetProducts(self) -> ArrayWrapper_OnlineProductWrapper: ...

    # bool ProductTradeInWrapper::IsNull() const [member function]
    def IsNull(self) -> bool: ...

    # bool ProductTradeInWrapper::operator bool() const [casting operator]

    # Private:
    # ProductTradeInWrapper::Impl [class declaration]

    # ProductTradeInWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


