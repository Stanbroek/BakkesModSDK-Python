from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class GravityPickup():
    # Public:
    # GravityPickup::GravityPickup(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # GravityPickup::GravityPickup(GravityPickup const & other) [constructor]

    # GravityPickup & GravityPickup::operator=(GravityPickup rhs) [member operator]

    # GravityPickup::~GravityPickup() [destructor]
    def __del__(self) -> None: ...

    # float GravityPickup::GetBallGravity() [member function]
    def GetBallGravity(self) -> float: ...

    # void GravityPickup::SetBallGravity(float newBallGravity) [member function]
    def SetBallGravity(self, newBallGravity: float) -> None: ...

    # float GravityPickup::GetRange() [member function]
    def GetRange(self) -> float: ...

    # void GravityPickup::SetRange(float newRange) [member function]
    def SetRange(self, newRange: float) -> None: ...

    # Vector GravityPickup::GetOffset() [member function]
    def GetOffset(self) -> Vector: ...

    # void GravityPickup::SetOffset(Vector newOffset) [member function]
    def SetOffset(self, newOffset: Vector) -> None: ...

    # long unsigned int GravityPickup::GetbDeactivateOnTouch() [member function]
    def GetbDeactivateOnTouch(self) -> bool: ...

    # void GravityPickup::SetbDeactivateOnTouch(long unsigned int newbDeactivateOnTouch) [member function]
    def SetbDeactivateOnTouch(self, newbDeactivateOnTouch: bool) -> None: ...

    # float GravityPickup::GetRecordBallHitRate() [member function]
    def GetRecordBallHitRate(self) -> float: ...

    # void GravityPickup::SetRecordBallHitRate(float newRecordBallHitRate) [member function]
    def SetRecordBallHitRate(self, newRecordBallHitRate: float) -> None: ...

    # float GravityPickup::GetLastRecordedBallHitTime() [member function]
    def GetLastRecordedBallHitTime(self) -> float: ...

    # void GravityPickup::SetLastRecordedBallHitTime(float newLastRecordedBallHitTime) [member function]
    def SetLastRecordedBallHitTime(self, newLastRecordedBallHitTime: float) -> None: ...

    # BallWrapper GravityPickup::GetPrevBall() [member function]
    def GetPrevBall(self) -> BallWrapper: ...

    # void GravityPickup::SetPrevBall(BallWrapper newPrevBall) [member function]
    def SetPrevBall(self, newPrevBall: BallWrapper) -> None: ...

    # void GravityPickup::HandleHitBall(CarWrapper InCar, BallWrapper Ball) [member function]
    def HandleHitBall(self, InCar: CarWrapper, Ball: BallWrapper) -> None: ...

    # void GravityPickup::UpdateVisual() [member function]
    def UpdateVisual(self) -> None: ...

    # void GravityPickup::ApplyForces(float ActiveTime) [member function]
    def ApplyForces(self, ActiveTime: float) -> None: ...

    # void GravityPickup::PickupEnd() [member function]
    def PickupEnd(self) -> None: ...

    # void GravityPickup::PickupStart() [member function]
    def PickupStart(self) -> None: ...

    # Private:
    # GravityPickup::Impl [class declaration]

    # GravityPickup::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


