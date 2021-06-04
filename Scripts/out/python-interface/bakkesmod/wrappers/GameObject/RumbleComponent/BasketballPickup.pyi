from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class BasketballPickup():
    # Public:
    # BasketballPickup::BasketballPickup(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # BasketballPickup::BasketballPickup(BasketballPickup const & other) [constructor]

    # BasketballPickup & BasketballPickup::operator=(BasketballPickup rhs) [member operator]

    # BasketballPickup::~BasketballPickup() [destructor]
    def __del__(self) -> None: ...

    # Vector BasketballPickup::GetBallOffset() [member function]
    def GetBallOffset(self) -> Vector: ...

    # void BasketballPickup::SetBallOffset(Vector newBallOffset) [member function]
    def SetBallOffset(self, newBallOffset: Vector) -> None: ...

    # float BasketballPickup::GetAttachedBallMass() [member function]
    def GetAttachedBallMass(self) -> float: ...

    # void BasketballPickup::SetAttachedBallMass(float newAttachedBallMass) [member function]
    def SetAttachedBallMass(self, newAttachedBallMass: float) -> None: ...

    # Vector BasketballPickup::GetLaunchForce() [member function]
    def GetLaunchForce(self) -> Vector: ...

    # void BasketballPickup::SetLaunchForce(Vector newLaunchForce) [member function]
    def SetLaunchForce(self, newLaunchForce: Vector) -> None: ...

    # BallWrapper BasketballPickup::GetWeldedBall() [member function]
    def GetWeldedBall(self) -> BallWrapper: ...

    # void BasketballPickup::SetWeldedBall(BallWrapper newWeldedBall) [member function]
    def SetWeldedBall(self, newWeldedBall: BallWrapper) -> None: ...

    # float BasketballPickup::GetOldBallMass() [member function]
    def GetOldBallMass(self) -> float: ...

    # void BasketballPickup::SetOldBallMass(float newOldBallMass) [member function]
    def SetOldBallMass(self, newOldBallMass: float) -> None: ...

    # void BasketballPickup::HandleCarTouch(BallWrapper InBall, CarWrapper InCar, unsigned char HitType) [member function]
    def HandleCarTouch(self, InBall: BallWrapper, InCar: CarWrapper, HitType: int) -> None: ...

    # void BasketballPickup::PickupStart() [member function]
    def PickupStart(self) -> None: ...

    # void BasketballPickup::HandleHitBall(CarWrapper InCar, BallWrapper InBall) [member function]
    def HandleHitBall(self, InCar: CarWrapper, InBall: BallWrapper) -> None: ...

    # bool BasketballPickup::TryActivate(RBActorWrapper TargetOverride) [member function]
    def TryActivate(self, TargetOverride: RBActorWrapper) -> bool: ...

    # void BasketballPickup::OnCreated() [member function]
    def OnCreated(self) -> None: ...

    # Private:
    # BasketballPickup::Impl [class declaration]

    # BasketballPickup::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


