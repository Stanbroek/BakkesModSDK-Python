from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class DoubleJumpComponentWrapper():
    # Public:
    # DoubleJumpComponentWrapper::DoubleJumpComponentWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # DoubleJumpComponentWrapper::DoubleJumpComponentWrapper(DoubleJumpComponentWrapper const & other) [constructor]

    # DoubleJumpComponentWrapper & DoubleJumpComponentWrapper::operator=(DoubleJumpComponentWrapper rhs) [member operator]

    # DoubleJumpComponentWrapper::~DoubleJumpComponentWrapper() [destructor]
    def __del__(self) -> None: ...

    # void DoubleJumpComponentWrapper::SetJumpImpulse(float newJumpImpulse) [member function]
    def SetJumpImpulse(self, newJumpImpulse: float) -> None: ...

    # float DoubleJumpComponentWrapper::GetImpulseScale() [member function]
    def GetImpulseScale(self) -> float: ...

    # void DoubleJumpComponentWrapper::SetImpulseScale(float newImpulseScale) [member function]
    def SetImpulseScale(self, newImpulseScale: float) -> None: ...

    # void DoubleJumpComponentWrapper::ApplyForces(float ActiveTime) [member function]
    def ApplyForces(self, ActiveTime: float) -> None: ...

    # void DoubleJumpComponentWrapper::OnCreated() [member function]
    def OnCreated(self) -> None: ...

    # Private:
    # DoubleJumpComponentWrapper::Impl [class declaration]

    # DoubleJumpComponentWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


