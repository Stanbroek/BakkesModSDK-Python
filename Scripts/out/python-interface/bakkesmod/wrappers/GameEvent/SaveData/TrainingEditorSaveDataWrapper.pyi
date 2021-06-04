from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class TrainingEditorSaveDataWrapper():
    # Public:
    # TrainingEditorSaveDataWrapper::TrainingEditorSaveDataWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # TrainingEditorSaveDataWrapper::TrainingEditorSaveDataWrapper(TrainingEditorSaveDataWrapper const & other) [constructor]

    # TrainingEditorSaveDataWrapper & TrainingEditorSaveDataWrapper::operator=(TrainingEditorSaveDataWrapper rhs) [member operator]

    # TrainingEditorSaveDataWrapper::~TrainingEditorSaveDataWrapper() [destructor]
    def __del__(self) -> None: ...

    # bool TrainingEditorSaveDataWrapper::IsNull() const [member function]
    def IsNull(self) -> bool: ...

    # bool TrainingEditorSaveDataWrapper::operator bool() const [casting operator]

    # UnrealStringWrapper TrainingEditorSaveDataWrapper::GetCode() [member function]
    def GetCode(self) -> UnrealStringWrapper: ...

    # UnrealStringWrapper TrainingEditorSaveDataWrapper::GetTM_Name() [member function]
    def GetTM_Name(self) -> UnrealStringWrapper: ...

    # unsigned char TrainingEditorSaveDataWrapper::GetType() [member function]
    def GetType(self) -> int: ...

    # void TrainingEditorSaveDataWrapper::SetType(unsigned char newType) [member function]
    def SetType(self, newType: int) -> None: ...

    # unsigned char TrainingEditorSaveDataWrapper::GetDifficulty() [member function]
    def GetDifficulty(self) -> int: ...

    # void TrainingEditorSaveDataWrapper::SetDifficulty(unsigned char newDifficulty) [member function]
    def SetDifficulty(self, newDifficulty: int) -> None: ...

    # UnrealStringWrapper TrainingEditorSaveDataWrapper::GetCreatorName() [member function]
    def GetCreatorName(self) -> UnrealStringWrapper: ...

    # UnrealStringWrapper TrainingEditorSaveDataWrapper::GetDescription() [member function]
    def GetDescription(self) -> UnrealStringWrapper: ...

    # int TrainingEditorSaveDataWrapper::GetNumRounds() [member function]
    def GetNumRounds(self) -> int: ...

    # void TrainingEditorSaveDataWrapper::SetNumRounds(int newNumRounds) [member function]
    def SetNumRounds(self, newNumRounds: int) -> None: ...

    # long long unsigned int TrainingEditorSaveDataWrapper::GetCreatedAt() [member function]
    def GetCreatedAt(self) -> int: ...

    # void TrainingEditorSaveDataWrapper::SetCreatedAt(long long unsigned int newCreatedAt) [member function]
    def SetCreatedAt(self, newCreatedAt: int) -> None: ...

    # long long unsigned int TrainingEditorSaveDataWrapper::GetUpdatedAt() [member function]
    def GetUpdatedAt(self) -> int: ...

    # void TrainingEditorSaveDataWrapper::SetUpdatedAt(long long unsigned int newUpdatedAt) [member function]
    def SetUpdatedAt(self, newUpdatedAt: int) -> None: ...

    # SteamID TrainingEditorSaveDataWrapper::GetCreatorPlayerID() [member function]
    def GetCreatorPlayerID(self) -> SteamID: ...

    # void TrainingEditorSaveDataWrapper::SetCreatorPlayerID(SteamID newCreatorPlayerID) [member function]
    def SetCreatorPlayerID(self, newCreatorPlayerID: SteamID) -> None: ...

    # void TrainingEditorSaveDataWrapper::Init() [member function]
    def Init(self) -> None: ...

    # UniqueIDWrapper TrainingEditorSaveDataWrapper::GetCreatorPlayerUniqueID() [member function]
    def GetCreatorPlayerUniqueID(self) -> UniqueIDWrapper: ...

    # Private:
    # TrainingEditorSaveDataWrapper::Impl [class declaration]

    # TrainingEditorSaveDataWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


