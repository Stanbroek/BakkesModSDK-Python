from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class OnlineProductWrapper():
    # Public:
    # OnlineProductWrapper::OnlineProductWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # OnlineProductWrapper::OnlineProductWrapper(OnlineProductWrapper const & other) [constructor]

    # OnlineProductWrapper & OnlineProductWrapper::operator=(OnlineProductWrapper rhs) [member operator]

    # OnlineProductWrapper::~OnlineProductWrapper() [destructor]
    def __del__(self) -> None: ...

    # bool OnlineProductWrapper::IsNull() const [member function]
    def IsNull(self) -> bool: ...

    # bool OnlineProductWrapper::operator bool() const [casting operator]

    # std::string OnlineProductWrapper::SeriesIdToSeriesName(int seriesID) [member function]
    def SeriesIdToSeriesName(self, seriesID: int) -> str: ...

    # int OnlineProductWrapper::GetProductID() [member function]
    def GetProductID(self) -> int: ...

    # int OnlineProductWrapper::GetSeriesID() [member function]
    def GetSeriesID(self) -> int: ...

    # int OnlineProductWrapper::GetTradeHold() [member function]
    def GetTradeHold(self) -> int: ...

    # std::string OnlineProductWrapper::GetProductSeries() [member function]
    def GetProductSeries(self) -> str: ...

    # unsigned char OnlineProductWrapper::GetQuality() [member function]
    def GetQuality(self) -> int: ...

    # ArrayWrapper<ProductAttributeWrapper> OnlineProductWrapper::GetAttributes() [member function]
    def GetAttributes(self) -> ArrayWrapper_ProductAttributeWrapper: ...

    # UnrealStringWrapper OnlineProductWrapper::GetLongLabel() [member function]
    def GetLongLabel(self) -> UnrealStringWrapper: ...

    # int OnlineProductWrapper::GetBlueprintSeriesID() [member function]
    def GetBlueprintSeriesID(self) -> int: ...

    # unsigned char OnlineProductWrapper::GetBlueprintType() [member function]
    def GetBlueprintType(self) -> int: ...

    # bool OnlineProductWrapper::IsBlueprint() [member function]
    def IsBlueprint(self) -> bool: ...

    # ProductWrapper OnlineProductWrapper::GetProduct() [member function]
    def GetProduct(self) -> ProductWrapper: ...

    # bool OnlineProductWrapper::GetIsUntradable() [member function]
    def GetIsUntradable(self) -> bool: ...

    # long long unsigned int OnlineProductWrapper::GetInstanceID() [member function]
    def GetInstanceID(self) -> int: ...

    # Private:
    # OnlineProductWrapper::Impl [class declaration]

    # OnlineProductWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


