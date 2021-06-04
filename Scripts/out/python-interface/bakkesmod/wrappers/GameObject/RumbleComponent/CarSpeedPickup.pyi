from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class CarSpeedPickup():
    # Public:
    # CarSpeedPickup::CarSpeedPickup(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # CarSpeedPickup::CarSpeedPickup(CarSpeedPickup const & other) [constructor]

    # CarSpeedPickup & CarSpeedPickup::operator=(CarSpeedPickup rhs) [member operator]

    # CarSpeedPickup::~CarSpeedPickup() [destructor]
    def __del__(self) -> None: ...

    # float CarSpeedPickup::GetGravityScale() [member function]
    def GetGravityScale(self) -> float: ...

    # void CarSpeedPickup::SetGravityScale(float newGravityScale) [member function]
    def SetGravityScale(self, newGravityScale: float) -> None: ...

    # Vector CarSpeedPickup::GetAddedForce() [member function]
    def GetAddedForce(self) -> Vector: ...

    # void CarSpeedPickup::SetAddedForce(Vector newAddedForce) [member function]
    def SetAddedForce(self, newAddedForce: Vector) -> None: ...

    # float CarSpeedPickup::GetOrigGravityScale() [member function]
    def GetOrigGravityScale(self) -> float: ...

    # void CarSpeedPickup::SetOrigGravityScale(float newOrigGravityScale) [member function]
    def SetOrigGravityScale(self, newOrigGravityScale: float) -> None: ...

    # void CarSpeedPickup::PickupEnd() [member function]
    def PickupEnd(self) -> None: ...

    # void CarSpeedPickup::PickupStart() [member function]
    def PickupStart(self) -> None: ...

    # Private:
    # CarSpeedPickup::Impl [class declaration]

    # CarSpeedPickup::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


