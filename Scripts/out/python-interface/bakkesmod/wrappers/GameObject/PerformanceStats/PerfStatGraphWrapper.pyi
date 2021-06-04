from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class PerfStatGraphWrapper():
    # Public:
    # PerfStatGraphWrapper::PerfStatGraphWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # PerfStatGraphWrapper::PerfStatGraphWrapper(PerfStatGraphWrapper const & other) [constructor]

    # PerfStatGraphWrapper & PerfStatGraphWrapper::operator=(PerfStatGraphWrapper rhs) [member operator]

    # PerfStatGraphWrapper::~PerfStatGraphWrapper() [destructor]
    def __del__(self) -> None: ...

    # SampleHistoryWrapper PerfStatGraphWrapper::GetFPS() [member function]
    def GetFPS(self) -> SampleHistoryWrapper: ...

    # void PerfStatGraphWrapper::SetFPS(SampleHistoryWrapper newFPS) [member function]
    def SetFPS(self, newFPS: SampleHistoryWrapper) -> None: ...

    # SampleHistoryWrapper PerfStatGraphWrapper::GetFrameTime() [member function]
    def GetFrameTime(self) -> SampleHistoryWrapper: ...

    # void PerfStatGraphWrapper::SetFrameTime(SampleHistoryWrapper newFrameTime) [member function]
    def SetFrameTime(self, newFrameTime: SampleHistoryWrapper) -> None: ...

    # SampleHistoryWrapper PerfStatGraphWrapper::GetGameThreadTime() [member function]
    def GetGameThreadTime(self) -> SampleHistoryWrapper: ...

    # void PerfStatGraphWrapper::SetGameThreadTime(SampleHistoryWrapper newGameThreadTime) [member function]
    def SetGameThreadTime(self, newGameThreadTime: SampleHistoryWrapper) -> None: ...

    # SampleHistoryWrapper PerfStatGraphWrapper::GetRenderThreadTime() [member function]
    def GetRenderThreadTime(self) -> SampleHistoryWrapper: ...

    # void PerfStatGraphWrapper::SetRenderThreadTime(SampleHistoryWrapper newRenderThreadTime) [member function]
    def SetRenderThreadTime(self, newRenderThreadTime: SampleHistoryWrapper) -> None: ...

    # SampleHistoryWrapper PerfStatGraphWrapper::GetGPUFrameTime() [member function]
    def GetGPUFrameTime(self) -> SampleHistoryWrapper: ...

    # void PerfStatGraphWrapper::SetGPUFrameTime(SampleHistoryWrapper newGPUFrameTime) [member function]
    def SetGPUFrameTime(self, newGPUFrameTime: SampleHistoryWrapper) -> None: ...

    # ArrayWrapper<SampleHistoryWrapper> PerfStatGraphWrapper::GetFrameTimeHistories() [member function]
    def GetFrameTimeHistories(self) -> ArrayWrapper_SampleHistoryWrapper: ...

    # float PerfStatGraphWrapper::GetMaxFPS() [member function]
    def GetMaxFPS(self) -> float: ...

    # void PerfStatGraphWrapper::SetMaxFPS(float newMaxFPS) [member function]
    def SetMaxFPS(self, newMaxFPS: float) -> None: ...

    # float PerfStatGraphWrapper::GetTargetFPS() [member function]
    def GetTargetFPS(self) -> float: ...

    # void PerfStatGraphWrapper::SetTargetFPS(float newTargetFPS) [member function]
    def SetTargetFPS(self, newTargetFPS: float) -> None: ...

    # void PerfStatGraphWrapper::eventUpdateGraphRanges() [member function]
    def eventUpdateGraphRanges(self) -> None: ...

    # SampleHistoryWrapper PerfStatGraphWrapper::CreateFrameTimeHistory(std::string Title) [member function]
    def CreateFrameTimeHistory(self, Title: str) -> SampleHistoryWrapper: ...

    # SampleHistoryWrapper PerfStatGraphWrapper::CreateFpsHistory(std::string Title) [member function]
    def CreateFpsHistory(self, Title: str) -> SampleHistoryWrapper: ...

    # void PerfStatGraphWrapper::eventConstruct() [member function]
    def eventConstruct(self) -> None: ...

    # Private:
    # PerfStatGraphWrapper::Impl [class declaration]

    # PerfStatGraphWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


