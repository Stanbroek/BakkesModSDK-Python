from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class SpecialEditionDatabaseWrapper():
    # Public:
    # SpecialEditionDatabaseWrapper::SpecialEditionDatabaseWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # SpecialEditionDatabaseWrapper::SpecialEditionDatabaseWrapper(SpecialEditionDatabaseWrapper const & other) [constructor]

    # SpecialEditionDatabaseWrapper & SpecialEditionDatabaseWrapper::operator=(SpecialEditionDatabaseWrapper rhs) [member operator]

    # SpecialEditionDatabaseWrapper::~SpecialEditionDatabaseWrapper() [destructor]
    def __del__(self) -> None: ...

    # bool SpecialEditionDatabaseWrapper::IsNull() const [member function]
    def IsNull(self) -> bool: ...

    # bool SpecialEditionDatabaseWrapper::operator bool() const [casting operator]

    # std::string SpecialEditionDatabaseWrapper::GetSpecialEditionName(int EditionID) [member function]
    def GetSpecialEditionName(self, EditionID: int) -> str: ...

    # int SpecialEditionDatabaseWrapper::GetSpecialEditionId(std::string & EditionName) [member function]
    def GetSpecialEditionId(self, EditionName: str) -> int: ...

    # Private:
    # SpecialEditionDatabaseWrapper::Impl [class declaration]

    # SpecialEditionDatabaseWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


