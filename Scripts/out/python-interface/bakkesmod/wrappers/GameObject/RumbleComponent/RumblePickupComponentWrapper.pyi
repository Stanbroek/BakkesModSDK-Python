from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class RumblePickupComponentWrapper():
    # Public:
    # RumblePickupComponentWrapper::RumblePickupComponentWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # RumblePickupComponentWrapper::RumblePickupComponentWrapper(RumblePickupComponentWrapper const & other) [constructor]

    # RumblePickupComponentWrapper & RumblePickupComponentWrapper::operator=(RumblePickupComponentWrapper rhs) [member operator]

    # RumblePickupComponentWrapper::~RumblePickupComponentWrapper() [destructor]
    def __del__(self) -> None: ...

    # UnrealStringWrapper RumblePickupComponentWrapper::GetPickupName() [member function]
    def GetPickupName(self) -> UnrealStringWrapper: ...

    # long unsigned int RumblePickupComponentWrapper::GetbHudIgnoreUseTime() [member function]
    def GetbHudIgnoreUseTime(self) -> bool: ...

    # void RumblePickupComponentWrapper::SetbHudIgnoreUseTime(long unsigned int newbHudIgnoreUseTime) [member function]
    def SetbHudIgnoreUseTime(self, newbHudIgnoreUseTime: bool) -> None: ...

    # long unsigned int RumblePickupComponentWrapper::GetbHasActivated() [member function]
    def GetbHasActivated(self) -> bool: ...

    # void RumblePickupComponentWrapper::SetbHasActivated(long unsigned int newbHasActivated) [member function]
    def SetbHasActivated(self, newbHasActivated: bool) -> None: ...

    # long unsigned int RumblePickupComponentWrapper::GetbIsActive() [member function]
    def GetbIsActive(self) -> bool: ...

    # void RumblePickupComponentWrapper::SetbIsActive(long unsigned int newbIsActive) [member function]
    def SetbIsActive(self, newbIsActive: bool) -> None: ...

    # float RumblePickupComponentWrapper::GetActivationDuration() [member function]
    def GetActivationDuration(self) -> float: ...

    # void RumblePickupComponentWrapper::SetActivationDuration(float newActivationDuration) [member function]
    def SetActivationDuration(self, newActivationDuration: float) -> None: ...

    # FXActorWrapper RumblePickupComponentWrapper::GetPickupFXArchetype() [member function]
    def GetPickupFXArchetype(self) -> FXActorWrapper: ...

    # void RumblePickupComponentWrapper::SetPickupFXArchetype(FXActorWrapper newPickupFXArchetype) [member function]
    def SetPickupFXArchetype(self, newPickupFXArchetype: FXActorWrapper) -> None: ...

    # FXActorWrapper RumblePickupComponentWrapper::GetPickupFX() [member function]
    def GetPickupFX(self) -> FXActorWrapper: ...

    # void RumblePickupComponentWrapper::SetPickupFX(FXActorWrapper newPickupFX) [member function]
    def SetPickupFX(self, newPickupFX: FXActorWrapper) -> None: ...

    # bool RumblePickupComponentWrapper::HasActivated2() [member function]
    def HasActivated2(self) -> bool: ...

    # RBActorWrapper RumblePickupComponentWrapper::GetClientTarget() [member function]
    def GetClientTarget(self) -> RBActorWrapper: ...

    # void RumblePickupComponentWrapper::OnVehicleSetupComplete() [member function]
    def OnVehicleSetupComplete(self) -> None: ...

    # float RumblePickupComponentWrapper::GetActiveTimePercent() [member function]
    def GetActiveTimePercent(self) -> float: ...

    # void RumblePickupComponentWrapper::PickupEnd() [member function]
    def PickupEnd(self) -> None: ...

    # void RumblePickupComponentWrapper::PickupStart() [member function]
    def PickupStart(self) -> None: ...

    # BoostWrapper RumblePickupComponentWrapper::GetBoostComponent() [member function]
    def GetBoostComponent(self) -> BoostWrapper: ...

    # void RumblePickupComponentWrapper::DeactivatePickup() [member function]
    def DeactivatePickup(self) -> None: ...

    # bool RumblePickupComponentWrapper::TryActivate(RBActorWrapper TargetOverride) [member function]
    def TryActivate(self, TargetOverride: RBActorWrapper) -> bool: ...

    # void RumblePickupComponentWrapper::OnCreated() [member function]
    def OnCreated(self) -> None: ...

    # bool RumblePickupComponentWrapper::CanPickup(CarWrapper InCar) [member function]
    def CanPickup(self, InCar: CarWrapper) -> bool: ...

    # void RumblePickupComponentWrapper::ApplyPickup(CarWrapper InCar) [member function]
    def ApplyPickup(self, InCar: CarWrapper) -> None: ...

    # Private:
    # RumblePickupComponentWrapper::Impl [class declaration]

    # RumblePickupComponentWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


