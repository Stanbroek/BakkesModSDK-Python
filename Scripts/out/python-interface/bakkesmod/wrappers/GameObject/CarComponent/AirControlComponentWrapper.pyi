from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class AirControlComponentWrapper():
    # Public:
    # AirControlComponentWrapper::AirControlComponentWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # AirControlComponentWrapper::AirControlComponentWrapper(AirControlComponentWrapper const & other) [constructor]

    # AirControlComponentWrapper & AirControlComponentWrapper::operator=(AirControlComponentWrapper rhs) [member operator]

    # AirControlComponentWrapper::~AirControlComponentWrapper() [destructor]
    def __del__(self) -> None: ...

    # Rotator AirControlComponentWrapper::GetAirTorque() [member function]
    def GetAirTorque(self) -> Rotator: ...

    # void AirControlComponentWrapper::SetAirTorque(Rotator newAirTorque) [member function]
    def SetAirTorque(self, newAirTorque: Rotator) -> None: ...

    # Rotator AirControlComponentWrapper::GetAirDamping() [member function]
    def GetAirDamping(self) -> Rotator: ...

    # void AirControlComponentWrapper::SetAirDamping(Rotator newAirDamping) [member function]
    def SetAirDamping(self, newAirDamping: Rotator) -> None: ...

    # float AirControlComponentWrapper::GetThrottleForce() [member function]
    def GetThrottleForce(self) -> float: ...

    # void AirControlComponentWrapper::SetThrottleForce(float newThrottleForce) [member function]
    def SetThrottleForce(self, newThrottleForce: float) -> None: ...

    # float AirControlComponentWrapper::GetDodgeDisableTimeRemaining() [member function]
    def GetDodgeDisableTimeRemaining(self) -> float: ...

    # void AirControlComponentWrapper::SetDodgeDisableTimeRemaining(float newDodgeDisableTimeRemaining) [member function]
    def SetDodgeDisableTimeRemaining(self, newDodgeDisableTimeRemaining: float) -> None: ...

    # float AirControlComponentWrapper::GetControlScale() [member function]
    def GetControlScale(self) -> float: ...

    # void AirControlComponentWrapper::SetControlScale(float newControlScale) [member function]
    def SetControlScale(self, newControlScale: float) -> None: ...

    # float AirControlComponentWrapper::GetAirControlSensitivity() [member function]
    def GetAirControlSensitivity(self) -> float: ...

    # void AirControlComponentWrapper::SetAirControlSensitivity(float newAirControlSensitivity) [member function]
    def SetAirControlSensitivity(self, newAirControlSensitivity: float) -> None: ...

    # void AirControlComponentWrapper::ApplyForces(float ActiveTime) [member function]
    def ApplyForces(self, ActiveTime: float) -> None: ...

    # void AirControlComponentWrapper::OnCreated() [member function]
    def OnCreated(self) -> None: ...

    # Private:
    # AirControlComponentWrapper::Impl [class declaration]

    # AirControlComponentWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


