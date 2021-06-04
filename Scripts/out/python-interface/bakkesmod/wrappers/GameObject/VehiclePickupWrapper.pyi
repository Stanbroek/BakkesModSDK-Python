from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class VehiclePickupWrapper():
    # Public:
    # VehiclePickupWrapper::VehiclePickupWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # VehiclePickupWrapper::VehiclePickupWrapper(VehiclePickupWrapper const & other) [constructor]

    # VehiclePickupWrapper & VehiclePickupWrapper::operator=(VehiclePickupWrapper rhs) [member operator]

    # VehiclePickupWrapper::~VehiclePickupWrapper() [destructor]
    def __del__(self) -> None: ...

    # float VehiclePickupWrapper::GetRespawnDelay() [member function]
    def GetRespawnDelay(self) -> float: ...

    # void VehiclePickupWrapper::SetRespawnDelay(float newRespawnDelay) [member function]
    def SetRespawnDelay(self, newRespawnDelay: float) -> None: ...

    # FXActorWrapper VehiclePickupWrapper::GetFXActorArchetype() [member function]
    def GetFXActorArchetype(self) -> FXActorWrapper: ...

    # void VehiclePickupWrapper::SetFXActorArchetype(FXActorWrapper newFXActorArchetype) [member function]
    def SetFXActorArchetype(self, newFXActorArchetype: FXActorWrapper) -> None: ...

    # FXActorWrapper VehiclePickupWrapper::GetFXActor() [member function]
    def GetFXActor(self) -> FXActorWrapper: ...

    # void VehiclePickupWrapper::SetFXActor(FXActorWrapper newFXActor) [member function]
    def SetFXActor(self, newFXActor: FXActorWrapper) -> None: ...

    # long unsigned int VehiclePickupWrapper::GetbPickedUp() [member function]
    def GetbPickedUp(self) -> bool: ...

    # void VehiclePickupWrapper::SetbPickedUp(long unsigned int newbPickedUp) [member function]
    def SetbPickedUp(self, newbPickedUp: bool) -> None: ...

    # long unsigned int VehiclePickupWrapper::GetbNetRelevant() [member function]
    def GetbNetRelevant(self) -> bool: ...

    # void VehiclePickupWrapper::SetbNetRelevant(long unsigned int newbNetRelevant) [member function]
    def SetbNetRelevant(self, newbNetRelevant: bool) -> None: ...

    # long unsigned int VehiclePickupWrapper::GetbNoPickup() [member function]
    def GetbNoPickup(self) -> bool: ...

    # void VehiclePickupWrapper::SetbNoPickup(long unsigned int newbNoPickup) [member function]
    def SetbNoPickup(self, newbNoPickup: bool) -> None: ...

    # void VehiclePickupWrapper::PlayPickedUpFX() [member function]
    def PlayPickedUpFX(self) -> None: ...

    # bool VehiclePickupWrapper::IsTouchingAVehicle() [member function]
    def IsTouchingAVehicle(self) -> bool: ...

    # void VehiclePickupWrapper::UpdateTickDisabled() [member function]
    def UpdateTickDisabled(self) -> None: ...

    # void VehiclePickupWrapper::SetNetRelevant(long unsigned int bRelevant) [member function]
    def SetNetRelevant(self, bRelevant: bool) -> None: ...

    # void VehiclePickupWrapper::Respawn2() [member function]
    def Respawn2(self) -> None: ...

    # void VehiclePickupWrapper::SetPickedUp(long unsigned int bNewPickedUp, CarWrapper InInstigator) [member function]
    def SetPickedUp(self, bNewPickedUp: bool, InInstigator: CarWrapper) -> None: ...

    # void VehiclePickupWrapper::Pickup2(CarWrapper Car) [member function]
    def Pickup2(self, Car: CarWrapper) -> None: ...

    # bool VehiclePickupWrapper::CanPickup(CarWrapper Car) [member function]
    def CanPickup(self, Car: CarWrapper) -> bool: ...

    # void VehiclePickupWrapper::OnTouch(CarWrapper Car) [member function]
    def OnTouch(self, Car: CarWrapper) -> None: ...

    # void VehiclePickupWrapper::eventTouch(ActorWrapper Other, PrimitiveComponentWrapper OtherComp, Vector & HitLocation, Vector & HitNormal) [member function]
    def eventTouch(self, Other: ActorWrapper, OtherComp: PrimitiveComponentWrapper, HitLocation: Vector, HitNormal: Vector) -> None: ...

    # void VehiclePickupWrapper::OnPickUp() [member function]
    def OnPickUp(self) -> None: ...

    # void VehiclePickupWrapper::OnSpawn() [member function]
    def OnSpawn(self) -> None: ...

    # void VehiclePickupWrapper::SetNoPickup() [member function]
    def SetNoPickup(self) -> None: ...

    # void VehiclePickupWrapper::SetupReplicateNoPickup() [member function]
    def SetupReplicateNoPickup(self) -> None: ...

    # void VehiclePickupWrapper::InitFX() [member function]
    def InitFX(self) -> None: ...

    # void VehiclePickupWrapper::eventPostBeginPlay() [member function]
    def eventPostBeginPlay(self) -> None: ...

    # void VehiclePickupWrapper::eventPreBeginPlay() [member function]
    def eventPreBeginPlay(self) -> None: ...

    # void VehiclePickupWrapper::EventPickedUp(VehiclePickupWrapper Pickup) [member function]
    def EventPickedUp(self, Pickup: VehiclePickupWrapper) -> None: ...

    # void VehiclePickupWrapper::EventSpawned(VehiclePickupWrapper Pickup) [member function]
    def EventSpawned(self, Pickup: VehiclePickupWrapper) -> None: ...

    # Private:
    # VehiclePickupWrapper::Impl [class declaration]

    # VehiclePickupWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


