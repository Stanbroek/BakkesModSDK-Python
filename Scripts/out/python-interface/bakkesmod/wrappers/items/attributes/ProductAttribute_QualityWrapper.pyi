from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class ProductAttribute_QualityWrapper():
    # Public:
    # ProductAttribute_QualityWrapper::ProductAttribute_QualityWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ProductAttribute_QualityWrapper::ProductAttribute_QualityWrapper(ProductAttribute_QualityWrapper const & other) [constructor]

    # ProductAttribute_QualityWrapper & ProductAttribute_QualityWrapper::operator=(ProductAttribute_QualityWrapper rhs) [member operator]

    # ProductAttribute_QualityWrapper::~ProductAttribute_QualityWrapper() [destructor]
    def __del__(self) -> None: ...

    # unsigned char ProductAttribute_QualityWrapper::GetQuality() [member function]
    def GetQuality(self) -> int: ...

    # UnrealStringWrapper ProductAttribute_QualityWrapper::ProductQualityToString(unsigned char InQuality) [member function]
    def ProductQualityToString(self, InQuality: int) -> UnrealStringWrapper: ...

    # Private:
    # ProductAttribute_QualityWrapper::Impl [class declaration]

    # ProductAttribute_QualityWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


