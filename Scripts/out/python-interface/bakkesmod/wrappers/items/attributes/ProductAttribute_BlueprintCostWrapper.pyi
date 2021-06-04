from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class ProductAttribute_BlueprintCostWrapper():
    # Public:
    # ProductAttribute_BlueprintCostWrapper::ProductAttribute_BlueprintCostWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ProductAttribute_BlueprintCostWrapper::ProductAttribute_BlueprintCostWrapper(ProductAttribute_BlueprintCostWrapper const & other) [constructor]

    # ProductAttribute_BlueprintCostWrapper & ProductAttribute_BlueprintCostWrapper::operator=(ProductAttribute_BlueprintCostWrapper rhs) [member operator]

    # ProductAttribute_BlueprintCostWrapper::~ProductAttribute_BlueprintCostWrapper() [destructor]
    def __del__(self) -> None: ...

    # int ProductAttribute_BlueprintCostWrapper::GetCost() [member function]
    def GetCost(self) -> int: ...

    # Private:
    # ProductAttribute_BlueprintCostWrapper::Impl [class declaration]

    # ProductAttribute_BlueprintCostWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


