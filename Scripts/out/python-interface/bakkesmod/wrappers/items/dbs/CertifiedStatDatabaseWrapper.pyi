from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class CertifiedStatDatabaseWrapper():
    # Public:
    # CertifiedStatDatabaseWrapper::CertifiedStatDatabaseWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # CertifiedStatDatabaseWrapper::CertifiedStatDatabaseWrapper(CertifiedStatDatabaseWrapper const & other) [constructor]

    # CertifiedStatDatabaseWrapper & CertifiedStatDatabaseWrapper::operator=(CertifiedStatDatabaseWrapper rhs) [member operator]

    # CertifiedStatDatabaseWrapper::~CertifiedStatDatabaseWrapper() [destructor]
    def __del__(self) -> None: ...

    # bool CertifiedStatDatabaseWrapper::IsNull() const [member function]
    def IsNull(self) -> bool: ...

    # bool CertifiedStatDatabaseWrapper::operator bool() const [casting operator]

    # std::string CertifiedStatDatabaseWrapper::GetStatName(int StatId) [member function]
    def GetStatName(self, StatId: int) -> str: ...

    # int CertifiedStatDatabaseWrapper::GetStatId(std::string & StatName) [member function]
    def GetStatId(self, StatName: str) -> int: ...

    # Private:
    # CertifiedStatDatabaseWrapper::Impl [class declaration]

    # CertifiedStatDatabaseWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


