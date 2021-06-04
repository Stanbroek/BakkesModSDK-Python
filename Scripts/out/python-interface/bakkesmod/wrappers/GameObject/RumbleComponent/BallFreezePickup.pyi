from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class BallFreezePickup():
    # Public:
    # BallFreezePickup::BallFreezePickup(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # BallFreezePickup::BallFreezePickup(BallFreezePickup const & other) [constructor]

    # BallFreezePickup & BallFreezePickup::operator=(BallFreezePickup rhs) [member operator]

    # BallFreezePickup::~BallFreezePickup() [destructor]
    def __del__(self) -> None: ...

    # FXActorWrapper BallFreezePickup::GetFreezeBreakFXArchetype() [member function]
    def GetFreezeBreakFXArchetype(self) -> FXActorWrapper: ...

    # void BallFreezePickup::SetFreezeBreakFXArchetype(FXActorWrapper newFreezeBreakFXArchetype) [member function]
    def SetFreezeBreakFXArchetype(self, newFreezeBreakFXArchetype: FXActorWrapper) -> None: ...

    # FXActorWrapper BallFreezePickup::GetFreezeFXArchetype() [member function]
    def GetFreezeFXArchetype(self) -> FXActorWrapper: ...

    # void BallFreezePickup::SetFreezeFXArchetype(FXActorWrapper newFreezeFXArchetype) [member function]
    def SetFreezeFXArchetype(self, newFreezeFXArchetype: FXActorWrapper) -> None: ...

    # long unsigned int BallFreezePickup::GetbMaintainMomentum() [member function]
    def GetbMaintainMomentum(self) -> bool: ...

    # void BallFreezePickup::SetbMaintainMomentum(long unsigned int newbMaintainMomentum) [member function]
    def SetbMaintainMomentum(self, newbMaintainMomentum: bool) -> None: ...

    # long unsigned int BallFreezePickup::GetbTouched() [member function]
    def GetbTouched(self) -> bool: ...

    # void BallFreezePickup::SetbTouched(long unsigned int newbTouched) [member function]
    def SetbTouched(self, newbTouched: bool) -> None: ...

    # float BallFreezePickup::GetTimeToStop() [member function]
    def GetTimeToStop(self) -> float: ...

    # void BallFreezePickup::SetTimeToStop(float newTimeToStop) [member function]
    def SetTimeToStop(self, newTimeToStop: float) -> None: ...

    # float BallFreezePickup::GetStopMomentumPercentage() [member function]
    def GetStopMomentumPercentage(self) -> float: ...

    # void BallFreezePickup::SetStopMomentumPercentage(float newStopMomentumPercentage) [member function]
    def SetStopMomentumPercentage(self, newStopMomentumPercentage: float) -> None: ...

    # BallWrapper BallFreezePickup::GetBall() [member function]
    def GetBall(self) -> BallWrapper: ...

    # void BallFreezePickup::SetBall(BallWrapper newBall) [member function]
    def SetBall(self, newBall: BallWrapper) -> None: ...

    # Vector BallFreezePickup::GetOrigLinearVelocity() [member function]
    def GetOrigLinearVelocity(self) -> Vector: ...

    # void BallFreezePickup::SetOrigLinearVelocity(Vector newOrigLinearVelocity) [member function]
    def SetOrigLinearVelocity(self, newOrigLinearVelocity: Vector) -> None: ...

    # Vector BallFreezePickup::GetOrigAngularVelocity() [member function]
    def GetOrigAngularVelocity(self) -> Vector: ...

    # void BallFreezePickup::SetOrigAngularVelocity(Vector newOrigAngularVelocity) [member function]
    def SetOrigAngularVelocity(self, newOrigAngularVelocity: Vector) -> None: ...

    # float BallFreezePickup::GetOrigSpeed() [member function]
    def GetOrigSpeed(self) -> float: ...

    # void BallFreezePickup::SetOrigSpeed(float newOrigSpeed) [member function]
    def SetOrigSpeed(self, newOrigSpeed: float) -> None: ...

    # float BallFreezePickup::GetRepOrigSpeed() [member function]
    def GetRepOrigSpeed(self) -> float: ...

    # void BallFreezePickup::SetRepOrigSpeed(float newRepOrigSpeed) [member function]
    def SetRepOrigSpeed(self, newRepOrigSpeed: float) -> None: ...

    # FXActorWrapper BallFreezePickup::GetFreezeFX() [member function]
    def GetFreezeFX(self) -> FXActorWrapper: ...

    # void BallFreezePickup::SetFreezeFX(FXActorWrapper newFreezeFX) [member function]
    def SetFreezeFX(self, newFreezeFX: FXActorWrapper) -> None: ...

    # void BallFreezePickup::PickupEnd() [member function]
    def PickupEnd(self) -> None: ...

    # void BallFreezePickup::HandleBallExploded(BallWrapper InBall) [member function]
    def HandleBallExploded(self, InBall: BallWrapper) -> None: ...

    # void BallFreezePickup::HandleBallHit(BallWrapper InBall, CarWrapper InCar, unsigned char HitType) [member function]
    def HandleBallHit(self, InBall: BallWrapper, InCar: CarWrapper, HitType: int) -> None: ...

    # void BallFreezePickup::ApplyForces(float ActiveTime) [member function]
    def ApplyForces(self, ActiveTime: float) -> None: ...

    # void BallFreezePickup::OnTargetChanged() [member function]
    def OnTargetChanged(self) -> None: ...

    # void BallFreezePickup::PickupStart() [member function]
    def PickupStart(self) -> None: ...

    # Private:
    # BallFreezePickup::Impl [class declaration]

    # BallFreezePickup::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


