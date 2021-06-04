from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class StatGraphWrapper():
    # Public:
    # StatGraphWrapper::StatGraphWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # StatGraphWrapper::StatGraphWrapper(StatGraphWrapper const & other) [constructor]

    # StatGraphWrapper & StatGraphWrapper::operator=(StatGraphWrapper rhs) [member operator]

    # StatGraphWrapper::~StatGraphWrapper() [destructor]
    def __del__(self) -> None: ...

    # bool StatGraphWrapper::IsNull() const [member function]
    def IsNull(self) -> bool: ...

    # bool StatGraphWrapper::operator bool() const [casting operator]

    # SampleRecordSettingsWrapper StatGraphWrapper::GetRecordSettings() [member function]
    def GetRecordSettings(self) -> SampleRecordSettingsWrapper: ...

    # void StatGraphWrapper::SetRecordSettings(SampleRecordSettingsWrapper newRecordSettings) [member function]
    def SetRecordSettings(self, newRecordSettings: SampleRecordSettingsWrapper) -> None: ...

    # double StatGraphWrapper::GetLastTickTime() [member function]
    def GetLastTickTime(self) -> float: ...

    # void StatGraphWrapper::SetLastTickTime(double newLastTickTime) [member function]
    def SetLastTickTime(self, newLastTickTime: float) -> None: ...

    # ArrayWrapper<SampleHistoryWrapper> StatGraphWrapper::GetSampleHistories() [member function]
    def GetSampleHistories(self) -> ArrayWrapper_SampleHistoryWrapper: ...

    # void StatGraphWrapper::StopDrawing() [member function]
    def StopDrawing(self) -> None: ...

    # SampleHistoryWrapper StatGraphWrapper::CreateSampleHistory(std::string Title) [member function]
    def CreateSampleHistory(self, Title: str) -> SampleHistoryWrapper: ...

    # SampleHistoryWrapper StatGraphWrapper::AddSampleHistory(SampleHistoryWrapper History) [member function]
    def AddSampleHistory(self, History: SampleHistoryWrapper) -> SampleHistoryWrapper: ...

    # void StatGraphWrapper::eventConstruct() [member function]
    def eventConstruct(self) -> None: ...

    # Private:
    # StatGraphWrapper::Impl [class declaration]

    # StatGraphWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


