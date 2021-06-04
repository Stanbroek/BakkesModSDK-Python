from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class TradeWrapper():
    # Public:
    # TradeWrapper::TradeWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # TradeWrapper::TradeWrapper(TradeWrapper const & other) [constructor]

    # TradeWrapper & TradeWrapper::operator=(TradeWrapper rhs) [member operator]

    # TradeWrapper::~TradeWrapper() [destructor]
    def __del__(self) -> None: ...

    class Currency():
        # Public:
        # TradeWrapper::Currency::currency_id [variable]
        @property
        def currency_id(self) -> int: ...

        # TradeWrapper::Currency::quantity [variable]
        @property
        def quantity(self) -> int: ...

        # TradeWrapper::Currency::Currency() [constructor]
        def __init__(self) -> None: ...

        # TradeWrapper::Currency::Currency(TradeWrapper::Currency const & arg0) [constructor]

        # TradeWrapper::Currency & TradeWrapper::Currency::operator=(TradeWrapper::Currency const & arg0) [member operator]

        # TradeWrapper::Currency::~Currency() [destructor]
        def __del__(self) -> None: ...


    # std::vector<TradeWrapper::Currency, std::allocator<TradeWrapper::Currency> > TradeWrapper::GetReceivingCurrency() const [member function]
    def GetReceivingCurrency(self) -> List[Currency]: ...

    # std::vector<TradeWrapper::Currency, std::allocator<TradeWrapper::Currency> > TradeWrapper::GetSendingCurrency() const [member function]
    def GetSendingCurrency(self) -> List[Currency]: ...

    # ArrayWrapper<OnlineProductWrapper> TradeWrapper::GetReceivingProducts() [member function]
    def GetReceivingProducts(self) -> ArrayWrapper_OnlineProductWrapper: ...

    # ArrayWrapper<OnlineProductWrapper> TradeWrapper::GetSendingProducts() [member function]
    def GetSendingProducts(self) -> ArrayWrapper_OnlineProductWrapper: ...

    # bool TradeWrapper::IsNull() [member function]
    def IsNull(self) -> bool: ...

    # bool TradeWrapper::operator bool() [casting operator]

    # Private:
    # TradeWrapper::Impl [class declaration]

    # TradeWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


