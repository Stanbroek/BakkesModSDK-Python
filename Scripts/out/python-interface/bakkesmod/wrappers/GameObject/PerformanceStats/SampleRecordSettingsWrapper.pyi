from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class SampleRecordSettingsWrapper():
    # Public:
    # SampleRecordSettingsWrapper::SampleRecordSettingsWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # SampleRecordSettingsWrapper::SampleRecordSettingsWrapper(SampleRecordSettingsWrapper const & other) [constructor]

    # SampleRecordSettingsWrapper & SampleRecordSettingsWrapper::operator=(SampleRecordSettingsWrapper rhs) [member operator]

    # SampleRecordSettingsWrapper::~SampleRecordSettingsWrapper() [destructor]
    def __del__(self) -> None: ...

    # bool SampleRecordSettingsWrapper::IsNull() const [member function]
    def IsNull(self) -> bool: ...

    # bool SampleRecordSettingsWrapper::operator bool() const [casting operator]

    # float SampleRecordSettingsWrapper::GetMaxSampleAge() [member function]
    def GetMaxSampleAge(self) -> float: ...

    # void SampleRecordSettingsWrapper::SetMaxSampleAge(float newMaxSampleAge) [member function]
    def SetMaxSampleAge(self, newMaxSampleAge: float) -> None: ...

    # float SampleRecordSettingsWrapper::GetRecordRate() [member function]
    def GetRecordRate(self) -> float: ...

    # void SampleRecordSettingsWrapper::SetRecordRate(float newRecordRate) [member function]
    def SetRecordRate(self, newRecordRate: float) -> None: ...

    # Private:
    # SampleRecordSettingsWrapper::Impl [class declaration]

    # SampleRecordSettingsWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


