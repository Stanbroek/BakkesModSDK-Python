from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class SaveDataWrapper():
    # Public:
    # SaveDataWrapper::SaveDataWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # SaveDataWrapper::SaveDataWrapper(SaveDataWrapper const & other) [constructor]

    # SaveDataWrapper & SaveDataWrapper::operator=(SaveDataWrapper rhs) [member operator]

    # SaveDataWrapper::~SaveDataWrapper() [destructor]
    def __del__(self) -> None: ...

    # bool SaveDataWrapper::IsNull() const [member function]
    def IsNull(self) -> bool: ...

    # bool SaveDataWrapper::operator bool() const [casting operator]

    # UnrealStringWrapper SaveDataWrapper::GetDirectoryPath() [member function]
    def GetDirectoryPath(self) -> UnrealStringWrapper: ...

    # UnrealStringWrapper SaveDataWrapper::GetSaveType() [member function]
    def GetSaveType(self) -> UnrealStringWrapper: ...

    # UnrealStringWrapper SaveDataWrapper::GetSaveExt() [member function]
    def GetSaveExt(self) -> UnrealStringWrapper: ...

    # long unsigned int SaveDataWrapper::GetbExactFileMatch() [member function]
    def GetbExactFileMatch(self) -> bool: ...

    # void SaveDataWrapper::SetbExactFileMatch(long unsigned int newbExactFileMatch) [member function]
    def SetbExactFileMatch(self, newbExactFileMatch: bool) -> None: ...

    # void SaveDataWrapper::Init() [member function]
    def Init(self) -> None: ...

    # Private:
    # SaveDataWrapper::Impl [class declaration]

    # SaveDataWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


