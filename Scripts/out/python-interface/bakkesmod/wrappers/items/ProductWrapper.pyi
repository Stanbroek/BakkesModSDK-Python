from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class ProductWrapper():
    # Public:
    # ProductWrapper::ProductWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ProductWrapper::ProductWrapper(ProductWrapper const & other) [constructor]

    # ProductWrapper & ProductWrapper::operator=(ProductWrapper rhs) [member operator]

    # ProductWrapper::~ProductWrapper() [destructor]
    def __del__(self) -> None: ...

    # bool ProductWrapper::IsNull() [member function]
    def IsNull(self) -> bool: ...

    # std::string ProductWrapper::GetAssetPackageName() [member function]
    def GetAssetPackageName(self) -> str: ...

    # UnrealStringWrapper ProductWrapper::GetAssetPath() [member function]
    def GetAssetPath(self) -> UnrealStringWrapper: ...

    # UnrealStringWrapper ProductWrapper::GetLabel() [member function]
    def GetLabel(self) -> UnrealStringWrapper: ...

    # UnrealStringWrapper ProductWrapper::GetAsciiLabel() [member function]
    def GetAsciiLabel(self) -> UnrealStringWrapper: ...

    # UnrealStringWrapper ProductWrapper::GetLongLabel() [member function]
    def GetLongLabel(self) -> UnrealStringWrapper: ...

    # bool ProductWrapper::IsPaintable() [member function]
    def IsPaintable(self) -> bool: ...

    # UnrealStringWrapper ProductWrapper::GetDisplayLabelSlot() [member function]
    def GetDisplayLabelSlot(self) -> UnrealStringWrapper: ...

    # unsigned char ProductWrapper::GetQuality() [member function]
    def GetQuality(self) -> int: ...

    # bool ProductWrapper::IsContainerKey() [member function]
    def IsContainerKey(self) -> bool: ...

    # bool ProductWrapper::IsCurrency() [member function]
    def IsCurrency(self) -> bool: ...

    # bool ProductWrapper::IsBlueprint() [member function]
    def IsBlueprint(self) -> bool: ...

    # bool ProductWrapper::IsContainerUnlocked() [member function]
    def IsContainerUnlocked(self) -> bool: ...

    # bool ProductWrapper::IsContainer() [member function]
    def IsContainer(self) -> bool: ...

    # bool ProductWrapper::IsSchematic() [member function]
    def IsSchematic(self) -> bool: ...

    # bool ProductWrapper::IsPlatformExclusive() [member function]
    def IsPlatformExclusive(self) -> bool: ...

    # bool ProductWrapper::IsLicensed() [member function]
    def IsLicensed(self) -> bool: ...

    # ArrayWrapper<ProductAttributeWrapper> ProductWrapper::GetAttributes() [member function]
    def GetAttributes(self) -> ArrayWrapper_ProductAttributeWrapper: ...

    # UnrealStringWrapper ProductWrapper::GetSortLabel() [member function]
    def GetSortLabel(self) -> UnrealStringWrapper: ...

    # UnrealStringWrapper ProductWrapper::GetThumbnailAssetPath() [member function]
    def GetThumbnailAssetPath(self) -> UnrealStringWrapper: ...

    # UnrealStringWrapper ProductWrapper::GetThumbnailPackageNameForLoad() [member function]
    def GetThumbnailPackageNameForLoad(self) -> UnrealStringWrapper: ...

    # std::string ProductWrapper::GetThumbnailPackageName() [member function]
    def GetThumbnailPackageName(self) -> str: ...

    # std::string ProductWrapper::GetThumbnailAssetName() [member function]
    def GetThumbnailAssetName(self) -> str: ...

    # UnrealStringWrapper ProductWrapper::GetTrademarkLabel() [member function]
    def GetTrademarkLabel(self) -> UnrealStringWrapper: ...

    # int ProductWrapper::GetID() [member function]
    def GetID(self) -> int: ...

    # Private:
    # ProductWrapper::Impl [class declaration]

    # ProductWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


