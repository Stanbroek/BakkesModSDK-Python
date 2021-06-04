from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class ProductAttributeWrapper():
    # Public:
    # ProductAttributeWrapper::ProductAttributeWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ProductAttributeWrapper::ProductAttributeWrapper(ProductAttributeWrapper const & other) [constructor]

    # ProductAttributeWrapper & ProductAttributeWrapper::operator=(ProductAttributeWrapper rhs) [member operator]

    # ProductAttributeWrapper::~ProductAttributeWrapper() [destructor]
    def __del__(self) -> None: ...

    # bool ProductAttributeWrapper::IsNull() const [member function]
    def IsNull(self) -> bool: ...

    # bool ProductAttributeWrapper::operator bool() const [casting operator]

    # std::string ProductAttributeWrapper::GetAttributeType() [member function]
    def GetAttributeType(self) -> str: ...

    # std::string ProductAttributeWrapper::GetTypename() [member function]
    def GetTypename(self) -> str: ...

    # UnrealStringWrapper ProductAttributeWrapper::GetLabel() [member function]
    def GetLabel(self) -> UnrealStringWrapper: ...

    # Private:
    # ProductAttributeWrapper::Impl [class declaration]

    # ProductAttributeWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


