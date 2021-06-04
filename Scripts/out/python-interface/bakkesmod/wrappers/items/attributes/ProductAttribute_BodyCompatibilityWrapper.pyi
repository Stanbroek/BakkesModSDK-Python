from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class ProductAttribute_BodyCompatibilityWrapper():
    # Public:
    # ProductAttribute_BodyCompatibilityWrapper::ProductAttribute_BodyCompatibilityWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ProductAttribute_BodyCompatibilityWrapper::ProductAttribute_BodyCompatibilityWrapper(ProductAttribute_BodyCompatibilityWrapper const & other) [constructor]

    # ProductAttribute_BodyCompatibilityWrapper & ProductAttribute_BodyCompatibilityWrapper::operator=(ProductAttribute_BodyCompatibilityWrapper rhs) [member operator]

    # ProductAttribute_BodyCompatibilityWrapper::~ProductAttribute_BodyCompatibilityWrapper() [destructor]
    def __del__(self) -> None: ...

    # ArrayWrapper<ProductWrapper> ProductAttribute_BodyCompatibilityWrapper::GetCompatibleBodies() [member function]
    def GetCompatibleBodies(self) -> ArrayWrapper_ProductWrapper: ...

    # Private:
    # ProductAttribute_BodyCompatibilityWrapper::Impl [class declaration]

    # ProductAttribute_BodyCompatibilityWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


