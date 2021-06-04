from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class ItemsWrapper():
    # Public:
    # ItemsWrapper::ItemsWrapper(uintptr_t gamedata, uintptr_t savedata) [constructor]
    def __init__(self, gamedata: int, savedata: int) -> None: ...

    # ItemsWrapper::ItemsWrapper(ItemsWrapper const & other) [constructor]

    # ItemsWrapper & ItemsWrapper::operator=(ItemsWrapper rhs) [member operator]

    # ItemsWrapper::~ItemsWrapper() [destructor]
    def __del__(self) -> None: ...

    # bool ItemsWrapper::IsNull() [member function]
    def IsNull(self) -> bool: ...

    # bool ItemsWrapper::operator bool() [casting operator]

    # ArrayWrapper<ProductWrapper> ItemsWrapper::GetAllProducts() [member function]
    def GetAllProducts(self) -> ArrayWrapper_ProductWrapper: ...

    # ProductWrapper ItemsWrapper::GetProduct(int productId) [member function]
    def GetProduct(self, productId: int) -> ProductWrapper: ...

    # OnlineProductWrapper ItemsWrapper::GetOnlineProduct(long long unsigned int instanceID) [member function]
    def GetOnlineProduct(self, instanceID: int) -> OnlineProductWrapper: ...

    # ArrayWrapper<OnlineProductWrapper> ItemsWrapper::GetUnlockedProducts() [member function]
    def GetUnlockedProducts(self) -> ArrayWrapper_OnlineProductWrapper: ...

    # ArrayWrapper<ProductWrapper> ItemsWrapper::GetCachedUnlockedProducts() [member function]
    def GetCachedUnlockedProducts(self) -> ArrayWrapper_ProductWrapper: ...

    # ArrayWrapper<OnlineProductWrapper> ItemsWrapper::GetOwnedProducts() [member function]
    def GetOwnedProducts(self) -> ArrayWrapper_OnlineProductWrapper: ...

    # CertifiedStatDatabaseWrapper ItemsWrapper::GetCertifiedStatDB() [member function]
    def GetCertifiedStatDB(self) -> CertifiedStatDatabaseWrapper: ...

    # DataAssetDatabase_ESportsTeamWrapper ItemsWrapper::GetEsportTeamDB() [member function]
    def GetEsportTeamDB(self) -> DataAssetDatabase_ESportsTeamWrapper: ...

    # PaintDatabaseWrapper ItemsWrapper::GetPaintDB() [member function]
    def GetPaintDB(self) -> PaintDatabaseWrapper: ...

    # SpecialEditionDatabaseWrapper ItemsWrapper::GetSpecialEditionDB() [member function]
    def GetSpecialEditionDB(self) -> SpecialEditionDatabaseWrapper: ...

    # UnrealStringWrapper ItemsWrapper::GetCurrentLoadoutName() [member function]
    def GetCurrentLoadoutName(self) -> UnrealStringWrapper: ...

    # LoadoutWrapper ItemsWrapper::GetCurrentLoadout(int teamIndex) [member function]
    def GetCurrentLoadout(self, teamIndex: int) -> LoadoutWrapper: ...

    # TradeWrapper ItemsWrapper::GetTradeWrapper() [member function]
    def GetTradeWrapper(self) -> TradeWrapper: ...

    # ProductTradeInWrapper ItemsWrapper::GetProductTradeInWrapper() [member function]
    def GetProductTradeInWrapper(self) -> ProductTradeInWrapper: ...

    # Private:
    # ItemsWrapper::Impl [class declaration]

    # ItemsWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


