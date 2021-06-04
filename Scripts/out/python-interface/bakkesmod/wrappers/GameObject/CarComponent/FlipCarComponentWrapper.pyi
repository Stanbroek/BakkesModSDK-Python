from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class FlipCarComponentWrapper():
    # Public:
    # FlipCarComponentWrapper::FlipCarComponentWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # FlipCarComponentWrapper::FlipCarComponentWrapper(FlipCarComponentWrapper const & other) [constructor]

    # FlipCarComponentWrapper & FlipCarComponentWrapper::operator=(FlipCarComponentWrapper rhs) [member operator]

    # FlipCarComponentWrapper::~FlipCarComponentWrapper() [destructor]
    def __del__(self) -> None: ...

    # float FlipCarComponentWrapper::GetFlipCarImpulse() [member function]
    def GetFlipCarImpulse(self) -> float: ...

    # void FlipCarComponentWrapper::SetFlipCarImpulse(float newFlipCarImpulse) [member function]
    def SetFlipCarImpulse(self, newFlipCarImpulse: float) -> None: ...

    # float FlipCarComponentWrapper::GetFlipCarTorque() [member function]
    def GetFlipCarTorque(self) -> float: ...

    # void FlipCarComponentWrapper::SetFlipCarTorque(float newFlipCarTorque) [member function]
    def SetFlipCarTorque(self, newFlipCarTorque: float) -> None: ...

    # float FlipCarComponentWrapper::GetFlipCarTime() [member function]
    def GetFlipCarTime(self) -> float: ...

    # void FlipCarComponentWrapper::SetFlipCarTime(float newFlipCarTime) [member function]
    def SetFlipCarTime(self, newFlipCarTime: float) -> None: ...

    # long unsigned int FlipCarComponentWrapper::GetbFlipRight() [member function]
    def GetbFlipRight(self) -> bool: ...

    # void FlipCarComponentWrapper::SetbFlipRight(long unsigned int newbFlipRight) [member function]
    def SetbFlipRight(self, newbFlipRight: bool) -> None: ...

    # void FlipCarComponentWrapper::InitFlip() [member function]
    def InitFlip(self) -> None: ...

    # void FlipCarComponentWrapper::ApplyForces(float ActiveTime) [member function]
    def ApplyForces(self, ActiveTime: float) -> None: ...

    # bool FlipCarComponentWrapper::CanActivate() [member function]
    def CanActivate(self) -> bool: ...

    # void FlipCarComponentWrapper::OnCreated() [member function]
    def OnCreated(self) -> None: ...

    # Private:
    # FlipCarComponentWrapper::Impl [class declaration]

    # FlipCarComponentWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


