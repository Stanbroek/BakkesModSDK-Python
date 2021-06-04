from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class DemolishPickup():
    # Public:
    # DemolishPickup::DemolishPickup(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # DemolishPickup::DemolishPickup(DemolishPickup const & other) [constructor]

    # DemolishPickup & DemolishPickup::operator=(DemolishPickup rhs) [member operator]

    # DemolishPickup::~DemolishPickup() [destructor]
    def __del__(self) -> None: ...

    # unsigned char DemolishPickup::GetDemolishTarget() [member function]
    def GetDemolishTarget(self) -> int: ...

    # void DemolishPickup::SetDemolishTarget(unsigned char newDemolishTarget) [member function]
    def SetDemolishTarget(self, newDemolishTarget: int) -> None: ...

    # unsigned char DemolishPickup::GetDemolishSpeed() [member function]
    def GetDemolishSpeed(self) -> int: ...

    # void DemolishPickup::SetDemolishSpeed(unsigned char newDemolishSpeed) [member function]
    def SetDemolishSpeed(self, newDemolishSpeed: int) -> None: ...

    # unsigned char DemolishPickup::GetOldTarget() [member function]
    def GetOldTarget(self) -> int: ...

    # void DemolishPickup::SetOldTarget(unsigned char newOldTarget) [member function]
    def SetOldTarget(self, newOldTarget: int) -> None: ...

    # unsigned char DemolishPickup::GetOldSpeed() [member function]
    def GetOldSpeed(self) -> int: ...

    # void DemolishPickup::SetOldSpeed(unsigned char newOldSpeed) [member function]
    def SetOldSpeed(self, newOldSpeed: int) -> None: ...

    # void DemolishPickup::PickupEnd() [member function]
    def PickupEnd(self) -> None: ...

    # void DemolishPickup::PickupStart() [member function]
    def PickupStart(self) -> None: ...

    # Private:
    # DemolishPickup::Impl [class declaration]

    # DemolishPickup::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


