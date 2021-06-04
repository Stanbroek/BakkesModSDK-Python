from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class SpecialEdition():
    # Public:
    # SpecialEdition::productId [variable]
    @property
    def productId(self) -> int: ...

    # SpecialEdition::editionId [variable]
    @property
    def editionId(self) -> int: ...

    # SpecialEdition::label [variable]
    @property
    def label(self) -> str: ...

    # SpecialEdition::SpecialEdition(SpecialEdition const & arg0) [constructor]

    # SpecialEdition::~SpecialEdition() [destructor]
    def __del__(self) -> None: ...

    # SpecialEdition::SpecialEdition() [constructor]
    def __init__(self) -> None: ...

    # SpecialEdition & SpecialEdition::operator=(SpecialEdition const & arg0) [member operator]


class ProductAttribute_SpecialEditionSettingsWrapper():
    # Public:
    # ProductAttribute_SpecialEditionSettingsWrapper::ProductAttribute_SpecialEditionSettingsWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ProductAttribute_SpecialEditionSettingsWrapper::ProductAttribute_SpecialEditionSettingsWrapper(ProductAttribute_SpecialEditionSettingsWrapper const & other) [constructor]

    # ProductAttribute_SpecialEditionSettingsWrapper & ProductAttribute_SpecialEditionSettingsWrapper::operator=(ProductAttribute_SpecialEditionSettingsWrapper rhs) [member operator]

    # ProductAttribute_SpecialEditionSettingsWrapper::~ProductAttribute_SpecialEditionSettingsWrapper() [destructor]
    def __del__(self) -> None: ...

    # std::vector<SpecialEdition, std::allocator<SpecialEdition> > ProductAttribute_SpecialEditionSettingsWrapper::GetEditions() [member function]
    def GetEditions(self) -> List[SpecialEdition]: ...

    # Private:
    # ProductAttribute_SpecialEditionSettingsWrapper::Impl [class declaration]

    # ProductAttribute_SpecialEditionSettingsWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


