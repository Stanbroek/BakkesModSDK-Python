from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class InputBufferGraphWrapper():
    # Public:
    # InputBufferGraphWrapper::InputBufferGraphWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # InputBufferGraphWrapper::InputBufferGraphWrapper(InputBufferGraphWrapper const & other) [constructor]

    # InputBufferGraphWrapper & InputBufferGraphWrapper::operator=(InputBufferGraphWrapper rhs) [member operator]

    # InputBufferGraphWrapper::~InputBufferGraphWrapper() [destructor]
    def __del__(self) -> None: ...

    # SampleHistoryWrapper InputBufferGraphWrapper::GetBuffer() [member function]
    def GetBuffer(self) -> SampleHistoryWrapper: ...

    # void InputBufferGraphWrapper::SetBuffer(SampleHistoryWrapper newBuffer) [member function]
    def SetBuffer(self, newBuffer: SampleHistoryWrapper) -> None: ...

    # SampleHistoryWrapper InputBufferGraphWrapper::GetBufferTarget() [member function]
    def GetBufferTarget(self) -> SampleHistoryWrapper: ...

    # void InputBufferGraphWrapper::SetBufferTarget(SampleHistoryWrapper newBufferTarget) [member function]
    def SetBufferTarget(self, newBufferTarget: SampleHistoryWrapper) -> None: ...

    # SampleHistoryWrapper InputBufferGraphWrapper::GetOverUnderFrames() [member function]
    def GetOverUnderFrames(self) -> SampleHistoryWrapper: ...

    # void InputBufferGraphWrapper::SetOverUnderFrames(SampleHistoryWrapper newOverUnderFrames) [member function]
    def SetOverUnderFrames(self, newOverUnderFrames: SampleHistoryWrapper) -> None: ...

    # SampleHistoryWrapper InputBufferGraphWrapper::GetPhysicsRate() [member function]
    def GetPhysicsRate(self) -> SampleHistoryWrapper: ...

    # void InputBufferGraphWrapper::SetPhysicsRate(SampleHistoryWrapper newPhysicsRate) [member function]
    def SetPhysicsRate(self, newPhysicsRate: SampleHistoryWrapper) -> None: ...

    # float InputBufferGraphWrapper::GetMaxPhysicsRate() [member function]
    def GetMaxPhysicsRate(self) -> float: ...

    # void InputBufferGraphWrapper::SetMaxPhysicsRate(float newMaxPhysicsRate) [member function]
    def SetMaxPhysicsRate(self, newMaxPhysicsRate: float) -> None: ...

    # float InputBufferGraphWrapper::GetMinPhysicsRate() [member function]
    def GetMinPhysicsRate(self) -> float: ...

    # void InputBufferGraphWrapper::SetMinPhysicsRate(float newMinPhysicsRate) [member function]
    def SetMinPhysicsRate(self, newMinPhysicsRate: float) -> None: ...

    # SampleHistoryWrapper InputBufferGraphWrapper::CreateBufferHistory(std::string Title) [member function]
    def CreateBufferHistory(self, Title: str) -> SampleHistoryWrapper: ...

    # void InputBufferGraphWrapper::eventConstruct() [member function]
    def eventConstruct(self) -> None: ...

    # Private:
    # InputBufferGraphWrapper::Impl [class declaration]

    # InputBufferGraphWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


