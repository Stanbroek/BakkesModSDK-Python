from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class GameEditorSaveDataWrapper():
    # Public:
    # GameEditorSaveDataWrapper::GameEditorSaveDataWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # GameEditorSaveDataWrapper::GameEditorSaveDataWrapper(GameEditorSaveDataWrapper const & other) [constructor]

    # GameEditorSaveDataWrapper & GameEditorSaveDataWrapper::operator=(GameEditorSaveDataWrapper rhs) [member operator]

    # GameEditorSaveDataWrapper::~GameEditorSaveDataWrapper() [destructor]
    def __del__(self) -> None: ...

    # UnrealStringWrapper GameEditorSaveDataWrapper::GetLoadedSaveName() [member function]
    def GetLoadedSaveName(self) -> UnrealStringWrapper: ...

    # TrainingEditorSaveDataWrapper GameEditorSaveDataWrapper::GetTrainingData() [member function]
    def GetTrainingData(self) -> TrainingEditorSaveDataWrapper: ...

    # void GameEditorSaveDataWrapper::SetTrainingData(TrainingEditorSaveDataWrapper newTrainingData) [member function]
    def SetTrainingData(self, newTrainingData: TrainingEditorSaveDataWrapper) -> None: ...

    # int GameEditorSaveDataWrapper::GetPlayerTeamNumber() [member function]
    def GetPlayerTeamNumber(self) -> int: ...

    # void GameEditorSaveDataWrapper::SetPlayerTeamNumber(int newPlayerTeamNumber) [member function]
    def SetPlayerTeamNumber(self, newPlayerTeamNumber: int) -> None: ...

    # long unsigned int GameEditorSaveDataWrapper::GetbUnowned() [member function]
    def GetbUnowned(self) -> bool: ...

    # void GameEditorSaveDataWrapper::SetbUnowned(long unsigned int newbUnowned) [member function]
    def SetbUnowned(self, newbUnowned: bool) -> None: ...

    # int GameEditorSaveDataWrapper::GetShotsCompleted() [member function]
    def GetShotsCompleted(self) -> int: ...

    # void GameEditorSaveDataWrapper::SetShotsCompleted(int newShotsCompleted) [member function]
    def SetShotsCompleted(self, newShotsCompleted: int) -> None: ...

    # UnrealStringWrapper GameEditorSaveDataWrapper::GetFavoritesFolderPath() [member function]
    def GetFavoritesFolderPath(self) -> UnrealStringWrapper: ...

    # UnrealStringWrapper GameEditorSaveDataWrapper::GetMyTrainingFolderPath() [member function]
    def GetMyTrainingFolderPath(self) -> UnrealStringWrapper: ...

    # UnrealStringWrapper GameEditorSaveDataWrapper::GetDownloadedFolderPath() [member function]
    def GetDownloadedFolderPath(self) -> UnrealStringWrapper: ...

    # unsigned char GameEditorSaveDataWrapper::GetTrainingSaveType(long unsigned int bOwned, long unsigned int bFavorited) [member function]
    def GetTrainingSaveType(self, bOwned: bool, bFavorited: bool) -> int: ...

    # void GameEditorSaveDataWrapper::Init() [member function]
    def Init(self) -> None: ...

    # Private:
    # GameEditorSaveDataWrapper::Impl [class declaration]

    # GameEditorSaveDataWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


