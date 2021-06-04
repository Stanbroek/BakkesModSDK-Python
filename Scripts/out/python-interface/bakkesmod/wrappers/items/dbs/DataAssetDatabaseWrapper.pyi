from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class DataAssetDatabaseWrapper():
    # Public:
    # DataAssetDatabaseWrapper::DataAssetDatabaseWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # DataAssetDatabaseWrapper::DataAssetDatabaseWrapper(DataAssetDatabaseWrapper const & other) [constructor]

    # DataAssetDatabaseWrapper & DataAssetDatabaseWrapper::operator=(DataAssetDatabaseWrapper rhs) [member operator]

    # DataAssetDatabaseWrapper::~DataAssetDatabaseWrapper() [destructor]
    def __del__(self) -> None: ...

    # bool DataAssetDatabaseWrapper::IsNull() const [member function]
    def IsNull(self) -> bool: ...

    # bool DataAssetDatabaseWrapper::operator bool() const [casting operator]

    # std::string DataAssetDatabaseWrapper::GetName(int DataAssetID) [member function]
    def GetName(self, DataAssetID: int) -> str: ...

    # int DataAssetDatabaseWrapper::GetID(std::string & DataAssetName) [member function]
    def GetID(self, DataAssetName: str) -> int: ...

    # Private:
    # DataAssetDatabaseWrapper::Impl [class declaration]

    # DataAssetDatabaseWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


