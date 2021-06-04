from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class HandbrakeOverridePickup():
    # Public:
    # HandbrakeOverridePickup::HandbrakeOverridePickup(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # HandbrakeOverridePickup::HandbrakeOverridePickup(HandbrakeOverridePickup const & other) [constructor]

    # HandbrakeOverridePickup & HandbrakeOverridePickup::operator=(HandbrakeOverridePickup rhs) [member operator]

    # HandbrakeOverridePickup::~HandbrakeOverridePickup() [destructor]
    def __del__(self) -> None: ...

    # CarWrapper HandbrakeOverridePickup::GetOtherCar() [member function]
    def GetOtherCar(self) -> CarWrapper: ...

    # void HandbrakeOverridePickup::SetOtherCar(CarWrapper newOtherCar) [member function]
    def SetOtherCar(self, newOtherCar: CarWrapper) -> None: ...

    # void HandbrakeOverridePickup::PickupEnd() [member function]
    def PickupEnd(self) -> None: ...

    # void HandbrakeOverridePickup::PickupStart() [member function]
    def PickupStart(self) -> None: ...

    # Private:
    # HandbrakeOverridePickup::Impl [class declaration]

    # HandbrakeOverridePickup::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


