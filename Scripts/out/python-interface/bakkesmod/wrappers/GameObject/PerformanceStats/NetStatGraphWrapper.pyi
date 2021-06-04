from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class NetStatGraphWrapper():
    # Public:
    # NetStatGraphWrapper::NetStatGraphWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # NetStatGraphWrapper::NetStatGraphWrapper(NetStatGraphWrapper const & other) [constructor]

    # NetStatGraphWrapper & NetStatGraphWrapper::operator=(NetStatGraphWrapper rhs) [member operator]

    # NetStatGraphWrapper::~NetStatGraphWrapper() [destructor]
    def __del__(self) -> None: ...

    # SampleHistoryWrapper NetStatGraphWrapper::GetPacketsOut() [member function]
    def GetPacketsOut(self) -> SampleHistoryWrapper: ...

    # void NetStatGraphWrapper::SetPacketsOut(SampleHistoryWrapper newPacketsOut) [member function]
    def SetPacketsOut(self, newPacketsOut: SampleHistoryWrapper) -> None: ...

    # SampleHistoryWrapper NetStatGraphWrapper::GetPacketsIn() [member function]
    def GetPacketsIn(self) -> SampleHistoryWrapper: ...

    # void NetStatGraphWrapper::SetPacketsIn(SampleHistoryWrapper newPacketsIn) [member function]
    def SetPacketsIn(self, newPacketsIn: SampleHistoryWrapper) -> None: ...

    # SampleHistoryWrapper NetStatGraphWrapper::GetLostPacketsOut() [member function]
    def GetLostPacketsOut(self) -> SampleHistoryWrapper: ...

    # void NetStatGraphWrapper::SetLostPacketsOut(SampleHistoryWrapper newLostPacketsOut) [member function]
    def SetLostPacketsOut(self, newLostPacketsOut: SampleHistoryWrapper) -> None: ...

    # SampleHistoryWrapper NetStatGraphWrapper::GetLostPacketsIn() [member function]
    def GetLostPacketsIn(self) -> SampleHistoryWrapper: ...

    # void NetStatGraphWrapper::SetLostPacketsIn(SampleHistoryWrapper newLostPacketsIn) [member function]
    def SetLostPacketsIn(self, newLostPacketsIn: SampleHistoryWrapper) -> None: ...

    # SampleHistoryWrapper NetStatGraphWrapper::GetBytesOut() [member function]
    def GetBytesOut(self) -> SampleHistoryWrapper: ...

    # void NetStatGraphWrapper::SetBytesOut(SampleHistoryWrapper newBytesOut) [member function]
    def SetBytesOut(self, newBytesOut: SampleHistoryWrapper) -> None: ...

    # SampleHistoryWrapper NetStatGraphWrapper::GetBytesIn() [member function]
    def GetBytesIn(self) -> SampleHistoryWrapper: ...

    # void NetStatGraphWrapper::SetBytesIn(SampleHistoryWrapper newBytesIn) [member function]
    def SetBytesIn(self, newBytesIn: SampleHistoryWrapper) -> None: ...

    # SampleHistoryWrapper NetStatGraphWrapper::GetLatency() [member function]
    def GetLatency(self) -> SampleHistoryWrapper: ...

    # void NetStatGraphWrapper::SetLatency(SampleHistoryWrapper newLatency) [member function]
    def SetLatency(self, newLatency: SampleHistoryWrapper) -> None: ...

    # float NetStatGraphWrapper::GetExpectedOutPacketRate() [member function]
    def GetExpectedOutPacketRate(self) -> float: ...

    # void NetStatGraphWrapper::SetExpectedOutPacketRate(float newExpectedOutPacketRate) [member function]
    def SetExpectedOutPacketRate(self, newExpectedOutPacketRate: float) -> None: ...

    # float NetStatGraphWrapper::GetExpectedInPacketRate() [member function]
    def GetExpectedInPacketRate(self) -> float: ...

    # void NetStatGraphWrapper::SetExpectedInPacketRate(float newExpectedInPacketRate) [member function]
    def SetExpectedInPacketRate(self, newExpectedInPacketRate: float) -> None: ...

    # float NetStatGraphWrapper::GetMaxBytesRate() [member function]
    def GetMaxBytesRate(self) -> float: ...

    # void NetStatGraphWrapper::SetMaxBytesRate(float newMaxBytesRate) [member function]
    def SetMaxBytesRate(self, newMaxBytesRate: float) -> None: ...

    # void NetStatGraphWrapper::eventUpdateGraphRanges() [member function]
    def eventUpdateGraphRanges(self) -> None: ...

    # SampleHistoryWrapper NetStatGraphWrapper::CreateBytesSummary(std::string Title) [member function]
    def CreateBytesSummary(self, Title: str) -> SampleHistoryWrapper: ...

    # SampleHistoryWrapper NetStatGraphWrapper::CreateLossSummary(std::string Title) [member function]
    def CreateLossSummary(self, Title: str) -> SampleHistoryWrapper: ...

    # SampleHistoryWrapper NetStatGraphWrapper::CreatePktSummary(std::string Title) [member function]
    def CreatePktSummary(self, Title: str) -> SampleHistoryWrapper: ...

    # void NetStatGraphWrapper::eventConstruct() [member function]
    def eventConstruct(self) -> None: ...

    # Private:
    # NetStatGraphWrapper::Impl [class declaration]

    # NetStatGraphWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


