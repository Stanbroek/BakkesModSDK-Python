from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class PaintDatabaseWrapper():
    # Public:
    # PaintDatabaseWrapper::PaintDatabaseWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # PaintDatabaseWrapper::PaintDatabaseWrapper(PaintDatabaseWrapper const & other) [constructor]

    # PaintDatabaseWrapper & PaintDatabaseWrapper::operator=(PaintDatabaseWrapper rhs) [member operator]

    # PaintDatabaseWrapper::~PaintDatabaseWrapper() [destructor]
    def __del__(self) -> None: ...

    # bool PaintDatabaseWrapper::IsNull() const [member function]
    def IsNull(self) -> bool: ...

    # bool PaintDatabaseWrapper::operator bool() const [casting operator]

    # std::string PaintDatabaseWrapper::GetPaintName(int PaintID) [member function]
    def GetPaintName(self, PaintID: int) -> str: ...

    # int PaintDatabaseWrapper::GetPaintID(std::string & PaintName) [member function]
    def GetPaintID(self, PaintName: str) -> int: ...

    # Private:
    # PaintDatabaseWrapper::Impl [class declaration]

    # PaintDatabaseWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


