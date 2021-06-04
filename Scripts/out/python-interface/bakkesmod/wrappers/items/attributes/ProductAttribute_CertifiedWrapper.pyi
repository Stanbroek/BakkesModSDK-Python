from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class ProductAttribute_CertifiedWrapper():
    # Public:
    # ProductAttribute_CertifiedWrapper::ProductAttribute_CertifiedWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ProductAttribute_CertifiedWrapper::ProductAttribute_CertifiedWrapper(ProductAttribute_CertifiedWrapper const & other) [constructor]

    # ProductAttribute_CertifiedWrapper & ProductAttribute_CertifiedWrapper::operator=(ProductAttribute_CertifiedWrapper rhs) [member operator]

    # ProductAttribute_CertifiedWrapper::~ProductAttribute_CertifiedWrapper() [destructor]
    def __del__(self) -> None: ...

    # std::string ProductAttribute_CertifiedWrapper::GetValueKeyName() [member function]
    def GetValueKeyName(self) -> str: ...

    # int ProductAttribute_CertifiedWrapper::GetStatId() [member function]
    def GetStatId(self) -> int: ...

    # int ProductAttribute_CertifiedWrapper::GetStatValue() [member function]
    def GetStatValue(self) -> int: ...

    # UnrealStringWrapper ProductAttribute_CertifiedWrapper::GetSortLabel() [member function]
    def GetSortLabel(self) -> UnrealStringWrapper: ...

    # UnrealStringWrapper ProductAttribute_CertifiedWrapper::GetDescription() [member function]
    def GetDescription(self) -> UnrealStringWrapper: ...

    # UnrealStringWrapper ProductAttribute_CertifiedWrapper::GetRankLabel() [member function]
    def GetRankLabel(self) -> UnrealStringWrapper: ...

    # int ProductAttribute_CertifiedWrapper::GetRank() [member function]
    def GetRank(self) -> int: ...

    # Private:
    # ProductAttribute_CertifiedWrapper::Impl [class declaration]

    # ProductAttribute_CertifiedWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


