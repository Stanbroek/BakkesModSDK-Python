from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class SampleHistoryWrapper():
    # Public:
    # SampleHistoryWrapper::SampleHistoryWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # SampleHistoryWrapper::SampleHistoryWrapper(SampleHistoryWrapper const & other) [constructor]

    # SampleHistoryWrapper & SampleHistoryWrapper::operator=(SampleHistoryWrapper rhs) [member operator]

    # SampleHistoryWrapper::~SampleHistoryWrapper() [destructor]
    def __del__(self) -> None: ...

    # bool SampleHistoryWrapper::IsNull() const [member function]
    def IsNull(self) -> bool: ...

    # bool SampleHistoryWrapper::operator bool() const [casting operator]

    # SampleRecordSettingsWrapper SampleHistoryWrapper::GetRecordSettings() [member function]
    def GetRecordSettings(self) -> SampleRecordSettingsWrapper: ...

    # void SampleHistoryWrapper::SetRecordSettings(SampleRecordSettingsWrapper newRecordSettings) [member function]
    def SetRecordSettings(self, newRecordSettings: SampleRecordSettingsWrapper) -> None: ...

    # UnrealStringWrapper SampleHistoryWrapper::GetTitle() [member function]
    def GetTitle(self) -> UnrealStringWrapper: ...

    # float SampleHistoryWrapper::GetYMin() [member function]
    def GetYMin(self) -> float: ...

    # void SampleHistoryWrapper::SetYMin(float newYMin) [member function]
    def SetYMin(self, newYMin: float) -> None: ...

    # float SampleHistoryWrapper::GetYMax() [member function]
    def GetYMax(self) -> float: ...

    # void SampleHistoryWrapper::SetYMax(float newYMax) [member function]
    def SetYMax(self, newYMax: float) -> None: ...

    # float SampleHistoryWrapper::GetGoodValue() [member function]
    def GetGoodValue(self) -> float: ...

    # void SampleHistoryWrapper::SetGoodValue(float newGoodValue) [member function]
    def SetGoodValue(self, newGoodValue: float) -> None: ...

    # float SampleHistoryWrapper::GetBadValue() [member function]
    def GetBadValue(self) -> float: ...

    # void SampleHistoryWrapper::SetBadValue(float newBadValue) [member function]
    def SetBadValue(self, newBadValue: float) -> None: ...

    # float SampleHistoryWrapper::GetBaseValue() [member function]
    def GetBaseValue(self) -> float: ...

    # void SampleHistoryWrapper::SetBaseValue(float newBaseValue) [member function]
    def SetBaseValue(self, newBaseValue: float) -> None: ...

    # StructArrayWrapper<RecordedSample> SampleHistoryWrapper::GetSamples() [member function]
    def GetSamples(self) -> StructArrayWrapper_RecordedSample: ...

    # int SampleHistoryWrapper::GetSampleIndex() [member function]
    def GetSampleIndex(self) -> int: ...

    # void SampleHistoryWrapper::SetSampleIndex(int newSampleIndex) [member function]
    def SetSampleIndex(self, newSampleIndex: int) -> None: ...

    # float SampleHistoryWrapper::GetAccumTime() [member function]
    def GetAccumTime(self) -> float: ...

    # void SampleHistoryWrapper::SetAccumTime(float newAccumTime) [member function]
    def SetAccumTime(self, newAccumTime: float) -> None: ...

    # RecordedSample SampleHistoryWrapper::GetPendingSample() [member function]
    def GetPendingSample(self) -> RecordedSample: ...

    # void SampleHistoryWrapper::SetPendingSample(RecordedSample newPendingSample) [member function]
    def SetPendingSample(self, newPendingSample: RecordedSample) -> None: ...

    # long unsigned int SampleHistoryWrapper::GetbHasPendingSample() [member function]
    def GetbHasPendingSample(self) -> bool: ...

    # void SampleHistoryWrapper::SetbHasPendingSample(long unsigned int newbHasPendingSample) [member function]
    def SetbHasPendingSample(self, newbHasPendingSample: bool) -> None: ...

    # void SampleHistoryWrapper::Tick(float DeltaTime) [member function]
    def Tick(self, DeltaTime: float) -> None: ...

    # void SampleHistoryWrapper::AddSample(float NewValue) [member function]
    def AddSample(self, NewValue: float) -> None: ...

    # float SampleHistoryWrapper::GetSummaryValue(unsigned char Type, float MaxSampleAge, long unsigned int bAbsoluteValue) [member function]
    def GetSummaryValue(self, Type: int, MaxSampleAge: float, bAbsoluteValue: bool) -> float: ...

    # SampleHistoryWrapper SampleHistoryWrapper::SetBaseValue2(float InBaseValue) [member function]
    def SetBaseValue2(self, InBaseValue: float) -> SampleHistoryWrapper: ...

    # SampleHistoryWrapper SampleHistoryWrapper::SetGoodBadValues(float InGoodValue, float InBadValue) [member function]
    def SetGoodBadValues(self, InGoodValue: float, InBadValue: float) -> SampleHistoryWrapper: ...

    # SampleHistoryWrapper SampleHistoryWrapper::SetGraphMaxMin(float MaxValue, float MinValue) [member function]
    def SetGraphMaxMin(self, MaxValue: float, MinValue: float) -> SampleHistoryWrapper: ...

    # SampleHistoryWrapper SampleHistoryWrapper::SetTitle(std::string InTitle) [member function]
    def SetTitle(self, InTitle: str) -> SampleHistoryWrapper: ...

    # Private:
    # SampleHistoryWrapper::Impl [class declaration]

    # SampleHistoryWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


