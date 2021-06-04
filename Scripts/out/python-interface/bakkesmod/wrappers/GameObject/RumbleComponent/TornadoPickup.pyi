from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class TornadoPickup():
    # Public:
    # TornadoPickup::TornadoPickup(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # TornadoPickup::TornadoPickup(TornadoPickup const & other) [constructor]

    # TornadoPickup & TornadoPickup::operator=(TornadoPickup rhs) [member operator]

    # TornadoPickup::~TornadoPickup() [destructor]
    def __del__(self) -> None: ...

    # float TornadoPickup::GetHeight() [member function]
    def GetHeight(self) -> float: ...

    # void TornadoPickup::SetHeight(float newHeight) [member function]
    def SetHeight(self, newHeight: float) -> None: ...

    # float TornadoPickup::GetRadius() [member function]
    def GetRadius(self) -> float: ...

    # void TornadoPickup::SetRadius(float newRadius) [member function]
    def SetRadius(self, newRadius: float) -> None: ...

    # Vector TornadoPickup::GetOffset() [member function]
    def GetOffset(self) -> Vector: ...

    # void TornadoPickup::SetOffset(Vector newOffset) [member function]
    def SetOffset(self, newOffset: Vector) -> None: ...

    # float TornadoPickup::GetRotationalForce() [member function]
    def GetRotationalForce(self) -> float: ...

    # void TornadoPickup::SetRotationalForce(float newRotationalForce) [member function]
    def SetRotationalForce(self, newRotationalForce: float) -> None: ...

    # float TornadoPickup::GetTorque() [member function]
    def GetTorque(self) -> float: ...

    # void TornadoPickup::SetTorque(float newTorque) [member function]
    def SetTorque(self, newTorque: float) -> None: ...

    # Vector TornadoPickup::GetFXScale() [member function]
    def GetFXScale(self) -> Vector: ...

    # void TornadoPickup::SetFXScale(Vector newFXScale) [member function]
    def SetFXScale(self, newFXScale: Vector) -> None: ...

    # Vector TornadoPickup::GetFXOffset() [member function]
    def GetFXOffset(self) -> Vector: ...

    # void TornadoPickup::SetFXOffset(Vector newFXOffset) [member function]
    def SetFXOffset(self, newFXOffset: Vector) -> None: ...

    # Vector TornadoPickup::GetMeshOffset() [member function]
    def GetMeshOffset(self) -> Vector: ...

    # void TornadoPickup::SetMeshOffset(Vector newMeshOffset) [member function]
    def SetMeshOffset(self, newMeshOffset: Vector) -> None: ...

    # Vector TornadoPickup::GetMeshScale() [member function]
    def GetMeshScale(self) -> Vector: ...

    # void TornadoPickup::SetMeshScale(Vector newMeshScale) [member function]
    def SetMeshScale(self, newMeshScale: Vector) -> None: ...

    # float TornadoPickup::GetMaxVelocityOffset() [member function]
    def GetMaxVelocityOffset(self) -> float: ...

    # void TornadoPickup::SetMaxVelocityOffset(float newMaxVelocityOffset) [member function]
    def SetMaxVelocityOffset(self, newMaxVelocityOffset: float) -> None: ...

    # float TornadoPickup::GetBallMultiplier() [member function]
    def GetBallMultiplier(self) -> float: ...

    # void TornadoPickup::SetBallMultiplier(float newBallMultiplier) [member function]
    def SetBallMultiplier(self, newBallMultiplier: float) -> None: ...

    # long unsigned int TornadoPickup::GetbDebugVis() [member function]
    def GetbDebugVis(self) -> bool: ...

    # void TornadoPickup::SetbDebugVis(long unsigned int newbDebugVis) [member function]
    def SetbDebugVis(self, newbDebugVis: bool) -> None: ...

    # float TornadoPickup::GetVelocityEase() [member function]
    def GetVelocityEase(self) -> float: ...

    # void TornadoPickup::SetVelocityEase(float newVelocityEase) [member function]
    def SetVelocityEase(self, newVelocityEase: float) -> None: ...

    # Vector TornadoPickup::GetVel() [member function]
    def GetVel(self) -> Vector: ...

    # void TornadoPickup::SetVel(Vector newVel) [member function]
    def SetVel(self, newVel: Vector) -> None: ...

    # ArrayWrapper<RBActorWrapper> TornadoPickup::GetAffecting() [member function]
    def GetAffecting(self) -> ArrayWrapper_RBActorWrapper: ...

    # void TornadoPickup::ApplyForces(float ActiveTime) [member function]
    def ApplyForces(self, ActiveTime: float) -> None: ...

    # void TornadoPickup::PlayCarSFX(RBActorWrapper InActor) [member function]
    def PlayCarSFX(self, InActor: RBActorWrapper) -> None: ...

    # void TornadoPickup::PlayBallSFX(RBActorWrapper InActor) [member function]
    def PlayBallSFX(self, InActor: RBActorWrapper) -> None: ...

    # Private:
    # TornadoPickup::Impl [class declaration]

    # TornadoPickup::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


