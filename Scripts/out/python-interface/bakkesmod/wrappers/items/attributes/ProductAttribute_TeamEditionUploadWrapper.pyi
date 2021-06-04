from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class ProductAttribute_TeamEditionUploadWrapper():
    # Public:
    # ProductAttribute_TeamEditionUploadWrapper::ProductAttribute_TeamEditionUploadWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ProductAttribute_TeamEditionUploadWrapper::ProductAttribute_TeamEditionUploadWrapper(ProductAttribute_TeamEditionUploadWrapper const & other) [constructor]

    # ProductAttribute_TeamEditionUploadWrapper & ProductAttribute_TeamEditionUploadWrapper::operator=(ProductAttribute_TeamEditionUploadWrapper rhs) [member operator]

    # ProductAttribute_TeamEditionUploadWrapper::~ProductAttribute_TeamEditionUploadWrapper() [destructor]
    def __del__(self) -> None: ...

    # ArrayWrapper<int> ProductAttribute_TeamEditionUploadWrapper::GetSupportedTeamEditions() [member function]
    def GetSupportedTeamEditions(self) -> ArrayWrapper_int: ...

    # Private:
    # ProductAttribute_TeamEditionUploadWrapper::Impl [class declaration]

    # ProductAttribute_TeamEditionUploadWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


