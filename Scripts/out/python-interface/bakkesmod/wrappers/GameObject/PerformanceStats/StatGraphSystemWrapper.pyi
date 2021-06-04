from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class StatGraphSystemWrapper():
    # Public:
    # StatGraphSystemWrapper::StatGraphSystemWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # StatGraphSystemWrapper::StatGraphSystemWrapper(StatGraphSystemWrapper const & other) [constructor]

    # StatGraphSystemWrapper & StatGraphSystemWrapper::operator=(StatGraphSystemWrapper rhs) [member operator]

    # StatGraphSystemWrapper::~StatGraphSystemWrapper() [destructor]
    def __del__(self) -> None: ...

    # bool StatGraphSystemWrapper::IsNull() const [member function]
    def IsNull(self) -> bool: ...

    # bool StatGraphSystemWrapper::operator bool() const [casting operator]

    # float StatGraphSystemWrapper::GetGraphSampleTime() [member function]
    def GetGraphSampleTime(self) -> float: ...

    # void StatGraphSystemWrapper::SetGraphSampleTime(float newGraphSampleTime) [member function]
    def SetGraphSampleTime(self, newGraphSampleTime: float) -> None: ...

    # unsigned char StatGraphSystemWrapper::GetGraphLevel() [member function]
    def GetGraphLevel(self) -> int: ...

    # void StatGraphSystemWrapper::SetGraphLevel(unsigned char newGraphLevel) [member function]
    def SetGraphLevel(self, newGraphLevel: int) -> None: ...

    # PerfStatGraphWrapper StatGraphSystemWrapper::GetPerfStatGraph() [member function]
    def GetPerfStatGraph(self) -> PerfStatGraphWrapper: ...

    # void StatGraphSystemWrapper::SetPerfStatGraph(PerfStatGraphWrapper newPerfStatGraph) [member function]
    def SetPerfStatGraph(self, newPerfStatGraph: PerfStatGraphWrapper) -> None: ...

    # NetStatGraphWrapper StatGraphSystemWrapper::GetNetStatGraph() [member function]
    def GetNetStatGraph(self) -> NetStatGraphWrapper: ...

    # void StatGraphSystemWrapper::SetNetStatGraph(NetStatGraphWrapper newNetStatGraph) [member function]
    def SetNetStatGraph(self, newNetStatGraph: NetStatGraphWrapper) -> None: ...

    # InputBufferGraphWrapper StatGraphSystemWrapper::GetInputBufferGraph() [member function]
    def GetInputBufferGraph(self) -> InputBufferGraphWrapper: ...

    # void StatGraphSystemWrapper::SetInputBufferGraph(InputBufferGraphWrapper newInputBufferGraph) [member function]
    def SetInputBufferGraph(self, newInputBufferGraph: InputBufferGraphWrapper) -> None: ...

    # ArrayWrapper<StatGraphWrapper> StatGraphSystemWrapper::GetStatGraphs() [member function]
    def GetStatGraphs(self) -> ArrayWrapper_StatGraphWrapper: ...

    # ArrayWrapper<StatGraphWrapper> StatGraphSystemWrapper::GetVisibleStatGraphs() [member function]
    def GetVisibleStatGraphs(self) -> ArrayWrapper_StatGraphWrapper: ...

    # int StatGraphSystemWrapper::GetPreallocGraphLines() [member function]
    def GetPreallocGraphLines(self) -> int: ...

    # void StatGraphSystemWrapper::SetPreallocGraphLines(int newPreallocGraphLines) [member function]
    def SetPreallocGraphLines(self, newPreallocGraphLines: int) -> None: ...

    # void StatGraphSystemWrapper::__StatGraphSystem_TA__SetGraphLevel(StatGraphWrapper G) [member function]
    def __StatGraphSystem_TA__SetGraphLevel(self, G: StatGraphWrapper) -> None: ...

    # void StatGraphSystemWrapper::PacketReceived(float Latency) [member function]
    def PacketReceived(self, Latency: float) -> None: ...

    # void StatGraphSystemWrapper::Graphtime(float Seconds) [member function]
    def Graphtime(self, Seconds: float) -> None: ...

    # void StatGraphSystemWrapper::StatGraphNext() [member function]
    def StatGraphNext(self) -> None: ...

    # float StatGraphSystemWrapper::GetGraphSampleTime2(unsigned char Level) [member function]
    def GetGraphSampleTime2(self, Level: int) -> float: ...

    # void StatGraphSystemWrapper::SetGraphLevel2(unsigned char Level) [member function]
    def SetGraphLevel2(self, Level: int) -> None: ...

    # Private:
    # StatGraphSystemWrapper::Impl [class declaration]

    # StatGraphSystemWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


