from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class VelcroPickup():
    # Public:
    # VelcroPickup::VelcroPickup(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # VelcroPickup::VelcroPickup(VelcroPickup const & other) [constructor]

    # VelcroPickup & VelcroPickup::operator=(VelcroPickup rhs) [member operator]

    # VelcroPickup::~VelcroPickup() [destructor]
    def __del__(self) -> None: ...

    # Vector VelcroPickup::GetBallOffset() [member function]
    def GetBallOffset(self) -> Vector: ...

    # void VelcroPickup::SetBallOffset(Vector newBallOffset) [member function]
    def SetBallOffset(self, newBallOffset: Vector) -> None: ...

    # long unsigned int VelcroPickup::GetbUseRealOffset() [member function]
    def GetbUseRealOffset(self) -> bool: ...

    # void VelcroPickup::SetbUseRealOffset(long unsigned int newbUseRealOffset) [member function]
    def SetbUseRealOffset(self, newbUseRealOffset: bool) -> None: ...

    # long unsigned int VelcroPickup::GetbHit() [member function]
    def GetbHit(self) -> bool: ...

    # void VelcroPickup::SetbHit(long unsigned int newbHit) [member function]
    def SetbHit(self, newbHit: bool) -> None: ...

    # long unsigned int VelcroPickup::GetbBroken() [member function]
    def GetbBroken(self) -> bool: ...

    # void VelcroPickup::SetbBroken(long unsigned int newbBroken) [member function]
    def SetbBroken(self, newbBroken: bool) -> None: ...

    # float VelcroPickup::GetAfterHitDuration() [member function]
    def GetAfterHitDuration(self) -> float: ...

    # void VelcroPickup::SetAfterHitDuration(float newAfterHitDuration) [member function]
    def SetAfterHitDuration(self, newAfterHitDuration: float) -> None: ...

    # float VelcroPickup::GetPostBreakDuration() [member function]
    def GetPostBreakDuration(self) -> float: ...

    # void VelcroPickup::SetPostBreakDuration(float newPostBreakDuration) [member function]
    def SetPostBreakDuration(self, newPostBreakDuration: float) -> None: ...

    # float VelcroPickup::GetMinBreakForce() [member function]
    def GetMinBreakForce(self) -> float: ...

    # void VelcroPickup::SetMinBreakForce(float newMinBreakForce) [member function]
    def SetMinBreakForce(self, newMinBreakForce: float) -> None: ...

    # float VelcroPickup::GetMinBreakTime() [member function]
    def GetMinBreakTime(self) -> float: ...

    # void VelcroPickup::SetMinBreakTime(float newMinBreakTime) [member function]
    def SetMinBreakTime(self, newMinBreakTime: float) -> None: ...

    # float VelcroPickup::GetCheckLastTouchRate() [member function]
    def GetCheckLastTouchRate(self) -> float: ...

    # void VelcroPickup::SetCheckLastTouchRate(float newCheckLastTouchRate) [member function]
    def SetCheckLastTouchRate(self, newCheckLastTouchRate: float) -> None: ...

    # BallWrapper VelcroPickup::GetWeldedBall() [member function]
    def GetWeldedBall(self) -> BallWrapper: ...

    # void VelcroPickup::SetWeldedBall(BallWrapper newWeldedBall) [member function]
    def SetWeldedBall(self, newWeldedBall: BallWrapper) -> None: ...

    # float VelcroPickup::GetOldBallMass() [member function]
    def GetOldBallMass(self) -> float: ...

    # void VelcroPickup::SetOldBallMass(float newOldBallMass) [member function]
    def SetOldBallMass(self, newOldBallMass: float) -> None: ...

    # float VelcroPickup::GetAttachTime() [member function]
    def GetAttachTime(self) -> float: ...

    # void VelcroPickup::SetAttachTime(float newAttachTime) [member function]
    def SetAttachTime(self, newAttachTime: float) -> None: ...

    # float VelcroPickup::GetLastTouchCheckTime() [member function]
    def GetLastTouchCheckTime(self) -> float: ...

    # void VelcroPickup::SetLastTouchCheckTime(float newLastTouchCheckTime) [member function]
    def SetLastTouchCheckTime(self, newLastTouchCheckTime: float) -> None: ...

    # float VelcroPickup::GetBreakTime() [member function]
    def GetBreakTime(self) -> float: ...

    # void VelcroPickup::SetBreakTime(float newBreakTime) [member function]
    def SetBreakTime(self, newBreakTime: float) -> None: ...

    # void VelcroPickup::DoBreak() [member function]
    def DoBreak(self) -> None: ...

    # void VelcroPickup::HandleCarTouch(BallWrapper InBall, CarWrapper InCar, unsigned char HitType) [member function]
    def HandleCarTouch(self, InBall: BallWrapper, InCar: CarWrapper, HitType: int) -> None: ...

    # void VelcroPickup::PickupEnd() [member function]
    def PickupEnd(self) -> None: ...

    # void VelcroPickup::OnBallHit() [member function]
    def OnBallHit(self) -> None: ...

    # void VelcroPickup::HandleHitBall(CarWrapper InCar, BallWrapper InBall) [member function]
    def HandleHitBall(self, InCar: CarWrapper, InBall: BallWrapper) -> None: ...

    # void VelcroPickup::PickupStart() [member function]
    def PickupStart(self) -> None: ...

    # Private:
    # VelcroPickup::Impl [class declaration]

    # VelcroPickup::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


