from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class HitForcePickup():
    # Public:
    # HitForcePickup::HitForcePickup(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # HitForcePickup::HitForcePickup(HitForcePickup const & other) [constructor]

    # HitForcePickup & HitForcePickup::operator=(HitForcePickup rhs) [member operator]

    # HitForcePickup::~HitForcePickup() [destructor]
    def __del__(self) -> None: ...

    # long unsigned int HitForcePickup::GetbBallForce() [member function]
    def GetbBallForce(self) -> bool: ...

    # void HitForcePickup::SetbBallForce(long unsigned int newbBallForce) [member function]
    def SetbBallForce(self, newbBallForce: bool) -> None: ...

    # long unsigned int HitForcePickup::GetbCarForce() [member function]
    def GetbCarForce(self) -> bool: ...

    # void HitForcePickup::SetbCarForce(long unsigned int newbCarForce) [member function]
    def SetbCarForce(self, newbCarForce: bool) -> None: ...

    # long unsigned int HitForcePickup::GetbDemolishCars() [member function]
    def GetbDemolishCars(self) -> bool: ...

    # void HitForcePickup::SetbDemolishCars(long unsigned int newbDemolishCars) [member function]
    def SetbDemolishCars(self, newbDemolishCars: bool) -> None: ...

    # float HitForcePickup::GetBallHitForce() [member function]
    def GetBallHitForce(self) -> float: ...

    # void HitForcePickup::SetBallHitForce(float newBallHitForce) [member function]
    def SetBallHitForce(self, newBallHitForce: float) -> None: ...

    # float HitForcePickup::GetCarHitForce() [member function]
    def GetCarHitForce(self) -> float: ...

    # void HitForcePickup::SetCarHitForce(float newCarHitForce) [member function]
    def SetCarHitForce(self, newCarHitForce: float) -> None: ...

    # float HitForcePickup::GetMinFXTime() [member function]
    def GetMinFXTime(self) -> float: ...

    # void HitForcePickup::SetMinFXTime(float newMinFXTime) [member function]
    def SetMinFXTime(self, newMinFXTime: float) -> None: ...

    # float HitForcePickup::GetOrigBallHitForce() [member function]
    def GetOrigBallHitForce(self) -> float: ...

    # void HitForcePickup::SetOrigBallHitForce(float newOrigBallHitForce) [member function]
    def SetOrigBallHitForce(self, newOrigBallHitForce: float) -> None: ...

    # float HitForcePickup::GetOrigCarHitForce() [member function]
    def GetOrigCarHitForce(self) -> float: ...

    # void HitForcePickup::SetOrigCarHitForce(float newOrigCarHitForce) [member function]
    def SetOrigCarHitForce(self, newOrigCarHitForce: float) -> None: ...

    # float HitForcePickup::GetLastFXTime() [member function]
    def GetLastFXTime(self) -> float: ...

    # void HitForcePickup::SetLastFXTime(float newLastFXTime) [member function]
    def SetLastFXTime(self, newLastFXTime: float) -> None: ...

    # void HitForcePickup::PickupEnd() [member function]
    def PickupEnd(self) -> None: ...

    # void HitForcePickup::PickupStart() [member function]
    def PickupStart(self) -> None: ...

    # Private:
    # HitForcePickup::Impl [class declaration]

    # HitForcePickup::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


