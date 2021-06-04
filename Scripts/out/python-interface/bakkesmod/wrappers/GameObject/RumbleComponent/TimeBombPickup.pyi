from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class TimeBombPickup():
    # Public:
    # TimeBombPickup::TimeBombPickup(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # TimeBombPickup::TimeBombPickup(TimeBombPickup const & other) [constructor]

    # TimeBombPickup & TimeBombPickup::operator=(TimeBombPickup rhs) [member operator]

    # TimeBombPickup::~TimeBombPickup() [destructor]
    def __del__(self) -> None: ...

    # float TimeBombPickup::GetRadius() [member function]
    def GetRadius(self) -> float: ...

    # void TimeBombPickup::SetRadius(float newRadius) [member function]
    def SetRadius(self, newRadius: float) -> None: ...

    # float TimeBombPickup::GetAlmostReadyDuration() [member function]
    def GetAlmostReadyDuration(self) -> float: ...

    # void TimeBombPickup::SetAlmostReadyDuration(float newAlmostReadyDuration) [member function]
    def SetAlmostReadyDuration(self, newAlmostReadyDuration: float) -> None: ...

    # float TimeBombPickup::GetStartMatSpeed() [member function]
    def GetStartMatSpeed(self) -> float: ...

    # void TimeBombPickup::SetStartMatSpeed(float newStartMatSpeed) [member function]
    def SetStartMatSpeed(self, newStartMatSpeed: float) -> None: ...

    # float TimeBombPickup::GetAlmostReadyMatSpeed() [member function]
    def GetAlmostReadyMatSpeed(self) -> float: ...

    # void TimeBombPickup::SetAlmostReadyMatSpeed(float newAlmostReadyMatSpeed) [member function]
    def SetAlmostReadyMatSpeed(self, newAlmostReadyMatSpeed: float) -> None: ...

    # float TimeBombPickup::GetImpulseForce() [member function]
    def GetImpulseForce(self) -> float: ...

    # void TimeBombPickup::SetImpulseForce(float newImpulseForce) [member function]
    def SetImpulseForce(self, newImpulseForce: float) -> None: ...

    # float TimeBombPickup::GetCarVerticalForce() [member function]
    def GetCarVerticalForce(self) -> float: ...

    # void TimeBombPickup::SetCarVerticalForce(float newCarVerticalForce) [member function]
    def SetCarVerticalForce(self, newCarVerticalForce: float) -> None: ...

    # float TimeBombPickup::GetCarTorque() [member function]
    def GetCarTorque(self) -> float: ...

    # void TimeBombPickup::SetCarTorque(float newCarTorque) [member function]
    def SetCarTorque(self, newCarTorque: float) -> None: ...

    # long unsigned int TimeBombPickup::GetbDemolish() [member function]
    def GetbDemolish(self) -> bool: ...

    # void TimeBombPickup::SetbDemolish(long unsigned int newbDemolish) [member function]
    def SetbDemolish(self, newbDemolish: bool) -> None: ...

    # long unsigned int TimeBombPickup::GetbImpulse() [member function]
    def GetbImpulse(self) -> bool: ...

    # void TimeBombPickup::SetbImpulse(long unsigned int newbImpulse) [member function]
    def SetbImpulse(self, newbImpulse: bool) -> None: ...

    # void TimeBombPickup::PickupEnd() [member function]
    def PickupEnd(self) -> None: ...

    # void TimeBombPickup::AlmostReady2() [member function]
    def AlmostReady2(self) -> None: ...

    # void TimeBombPickup::PickupStart() [member function]
    def PickupStart(self) -> None: ...

    # Private:
    # TimeBombPickup::Impl [class declaration]

    # TimeBombPickup::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


