from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class JumpComponentWrapper():
    # Public:
    # JumpComponentWrapper::JumpComponentWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # JumpComponentWrapper::JumpComponentWrapper(JumpComponentWrapper const & other) [constructor]

    # JumpComponentWrapper & JumpComponentWrapper::operator=(JumpComponentWrapper rhs) [member operator]

    # JumpComponentWrapper::~JumpComponentWrapper() [destructor]
    def __del__(self) -> None: ...

    # float JumpComponentWrapper::GetMinJumpTime() [member function]
    def GetMinJumpTime(self) -> float: ...

    # void JumpComponentWrapper::SetMinJumpTime(float newMinJumpTime) [member function]
    def SetMinJumpTime(self, newMinJumpTime: float) -> None: ...

    # float JumpComponentWrapper::GetJumpImpulse() [member function]
    def GetJumpImpulse(self) -> float: ...

    # void JumpComponentWrapper::SetJumpImpulse(float newJumpImpulse) [member function]
    def SetJumpImpulse(self, newJumpImpulse: float) -> None: ...

    # float JumpComponentWrapper::GetJumpForce() [member function]
    def GetJumpForce(self) -> float: ...

    # void JumpComponentWrapper::SetJumpForce(float newJumpForce) [member function]
    def SetJumpForce(self, newJumpForce: float) -> None: ...

    # float JumpComponentWrapper::GetJumpForceTime() [member function]
    def GetJumpForceTime(self) -> float: ...

    # void JumpComponentWrapper::SetJumpForceTime(float newJumpForceTime) [member function]
    def SetJumpForceTime(self, newJumpForceTime: float) -> None: ...

    # float JumpComponentWrapper::GetPodiumJumpForceTime() [member function]
    def GetPodiumJumpForceTime(self) -> float: ...

    # void JumpComponentWrapper::SetPodiumJumpForceTime(float newPodiumJumpForceTime) [member function]
    def SetPodiumJumpForceTime(self, newPodiumJumpForceTime: float) -> None: ...

    # float JumpComponentWrapper::GetJumpImpulseSpeed() [member function]
    def GetJumpImpulseSpeed(self) -> float: ...

    # void JumpComponentWrapper::SetJumpImpulseSpeed(float newJumpImpulseSpeed) [member function]
    def SetJumpImpulseSpeed(self, newJumpImpulseSpeed: float) -> None: ...

    # float JumpComponentWrapper::GetJumpAccel() [member function]
    def GetJumpAccel(self) -> float: ...

    # void JumpComponentWrapper::SetJumpAccel(float newJumpAccel) [member function]
    def SetJumpAccel(self, newJumpAccel: float) -> None: ...

    # float JumpComponentWrapper::GetMaxJumpHeight() [member function]
    def GetMaxJumpHeight(self) -> float: ...

    # void JumpComponentWrapper::SetMaxJumpHeight(float newMaxJumpHeight) [member function]
    def SetMaxJumpHeight(self, newMaxJumpHeight: float) -> None: ...

    # float JumpComponentWrapper::GetMaxJumpHeightTime() [member function]
    def GetMaxJumpHeightTime(self) -> float: ...

    # void JumpComponentWrapper::SetMaxJumpHeightTime(float newMaxJumpHeightTime) [member function]
    def SetMaxJumpHeightTime(self, newMaxJumpHeightTime: float) -> None: ...

    # long unsigned int JumpComponentWrapper::GetbDeactivate() [member function]
    def GetbDeactivate(self) -> bool: ...

    # void JumpComponentWrapper::SetbDeactivate(long unsigned int newbDeactivate) [member function]
    def SetbDeactivate(self, newbDeactivate: bool) -> None: ...

    # void JumpComponentWrapper::ApplyForces(float ActiveTime) [member function]
    def ApplyForces(self, ActiveTime: float) -> None: ...

    # void JumpComponentWrapper::CacheJumpData() [member function]
    def CacheJumpData(self) -> None: ...

    # void JumpComponentWrapper::OnCreated() [member function]
    def OnCreated(self) -> None: ...

    # Private:
    # JumpComponentWrapper::Impl [class declaration]

    # JumpComponentWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


