from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class BoostOverridePickup():
    # Public:
    # BoostOverridePickup::BoostOverridePickup(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # BoostOverridePickup::BoostOverridePickup(BoostOverridePickup const & other) [constructor]

    # BoostOverridePickup & BoostOverridePickup::operator=(BoostOverridePickup rhs) [member operator]

    # BoostOverridePickup::~BoostOverridePickup() [destructor]
    def __del__(self) -> None: ...

    # CarWrapper BoostOverridePickup::GetOtherCar() [member function]
    def GetOtherCar(self) -> CarWrapper: ...

    # void BoostOverridePickup::SetOtherCar(CarWrapper newOtherCar) [member function]
    def SetOtherCar(self, newOtherCar: CarWrapper) -> None: ...

    # void BoostOverridePickup::PickupEnd() [member function]
    def PickupEnd(self) -> None: ...

    # void BoostOverridePickup::OnTargetChanged() [member function]
    def OnTargetChanged(self) -> None: ...

    # void BoostOverridePickup::PickupStart() [member function]
    def PickupStart(self) -> None: ...

    # Private:
    # BoostOverridePickup::Impl [class declaration]

    # BoostOverridePickup::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


