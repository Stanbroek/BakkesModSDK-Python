from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class ProductTemplateWrapper():
    # Public:
    # ProductTemplateWrapper::ProductTemplateWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ProductTemplateWrapper::ProductTemplateWrapper(ProductTemplateWrapper const & other) [constructor]

    # ProductTemplateWrapper & ProductTemplateWrapper::operator=(ProductTemplateWrapper rhs) [member operator]

    # ProductTemplateWrapper::~ProductTemplateWrapper() [destructor]
    def __del__(self) -> None: ...

    # bool ProductTemplateWrapper::IsNull() const [member function]
    def IsNull(self) -> bool: ...

    # bool ProductTemplateWrapper::operator bool() const [casting operator]

    # ProductSlotWrapper ProductTemplateWrapper::GetSlot() [member function]
    def GetSlot(self) -> ProductSlotWrapper: ...

    # unsigned char ProductTemplateWrapper::GetUnlockMethod() [member function]
    def GetUnlockMethod(self) -> int: ...

    # unsigned char ProductTemplateWrapper::GetQuality() [member function]
    def GetQuality(self) -> int: ...

    # ProductWrapper ProductTemplateWrapper::GetRequiredProduct() [member function]
    def GetRequiredProduct(self) -> ProductWrapper: ...

    # long unsigned int ProductTemplateWrapper::GetbLicensed() [member function]
    def GetbLicensed(self) -> bool: ...

    # Private:
    # ProductTemplateWrapper::Impl [class declaration]

    # ProductTemplateWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


