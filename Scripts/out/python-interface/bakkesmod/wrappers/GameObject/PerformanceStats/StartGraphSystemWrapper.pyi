from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class StartGraphSystemWrapper():
    # Public:
    # StartGraphSystemWrapper::StartGraphSystemWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # StartGraphSystemWrapper::StartGraphSystemWrapper(StartGraphSystemWrapper const & other) [constructor]

    # StartGraphSystemWrapper & StartGraphSystemWrapper::operator=(StartGraphSystemWrapper rhs) [member operator]

    # StartGraphSystemWrapper::~StartGraphSystemWrapper() [destructor]
    def __del__(self) -> None: ...

    # bool StartGraphSystemWrapper::IsNull() const [member function]
    def IsNull(self) -> bool: ...

    # bool StartGraphSystemWrapper::operator bool() const [casting operator]

    # float StartGraphSystemWrapper::GetGraphSampleTime() [member function]
    def GetGraphSampleTime(self) -> float: ...

    # void StartGraphSystemWrapper::SetGraphSampleTime(float newGraphSampleTime) [member function]
    def SetGraphSampleTime(self, newGraphSampleTime: float) -> None: ...

    # unsigned char StartGraphSystemWrapper::GetGraphLevel() [member function]
    def GetGraphLevel(self) -> int: ...

    # void StartGraphSystemWrapper::SetGraphLevel(unsigned char newGraphLevel) [member function]
    def SetGraphLevel(self, newGraphLevel: int) -> None: ...

    # PerfStatGraphWrapper StartGraphSystemWrapper::GetPerfStatGraph() [member function]
    def GetPerfStatGraph(self) -> PerfStatGraphWrapper: ...

    # void StartGraphSystemWrapper::SetPerfStatGraph(PerfStatGraphWrapper newPerfStatGraph) [member function]
    def SetPerfStatGraph(self, newPerfStatGraph: PerfStatGraphWrapper) -> None: ...

    # NetStatGraphWrapper StartGraphSystemWrapper::GetNetStatGraph() [member function]
    def GetNetStatGraph(self) -> NetStatGraphWrapper: ...

    # void StartGraphSystemWrapper::SetNetStatGraph(NetStatGraphWrapper newNetStatGraph) [member function]
    def SetNetStatGraph(self, newNetStatGraph: NetStatGraphWrapper) -> None: ...

    # InputBufferGraphWrapper StartGraphSystemWrapper::GetInputBufferGraph() [member function]
    def GetInputBufferGraph(self) -> InputBufferGraphWrapper: ...

    # void StartGraphSystemWrapper::SetInputBufferGraph(InputBufferGraphWrapper newInputBufferGraph) [member function]
    def SetInputBufferGraph(self, newInputBufferGraph: InputBufferGraphWrapper) -> None: ...

    # ArrayWrapper<StatGraphWrapper> StartGraphSystemWrapper::GetStatGraphs() [member function]
    def GetStatGraphs(self) -> ArrayWrapper_StatGraphWrapper: ...

    # ArrayWrapper<StatGraphWrapper> StartGraphSystemWrapper::GetVisibleStatGraphs() [member function]
    def GetVisibleStatGraphs(self) -> ArrayWrapper_StatGraphWrapper: ...

    # void StartGraphSystemWrapper::Graphtime(float Seconds) [member function]
    def Graphtime(self, Seconds: float) -> None: ...

    # void StartGraphSystemWrapper::StatGraphNext() [member function]
    def StatGraphNext(self) -> None: ...

    # float StartGraphSystemWrapper::GetGraphSampleTime2(unsigned char Level) [member function]
    def GetGraphSampleTime2(self, Level: int) -> float: ...

    # void StartGraphSystemWrapper::SetGraphLevel2(unsigned char Level) [member function]
    def SetGraphLevel2(self, Level: int) -> None: ...

    # Private:
    # StartGraphSystemWrapper::Impl [class declaration]

    # StartGraphSystemWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


