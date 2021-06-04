from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class BoostModPickup():
    # Public:
    # BoostModPickup::BoostModPickup(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # BoostModPickup::BoostModPickup(BoostModPickup const & other) [constructor]

    # BoostModPickup & BoostModPickup::operator=(BoostModPickup rhs) [member operator]

    # BoostModPickup::~BoostModPickup() [destructor]
    def __del__(self) -> None: ...

    # long unsigned int BoostModPickup::GetbUnlimitedBoost() [member function]
    def GetbUnlimitedBoost(self) -> bool: ...

    # void BoostModPickup::SetbUnlimitedBoost(long unsigned int newbUnlimitedBoost) [member function]
    def SetbUnlimitedBoost(self, newbUnlimitedBoost: bool) -> None: ...

    # float BoostModPickup::GetBoostStrength() [member function]
    def GetBoostStrength(self) -> float: ...

    # void BoostModPickup::SetBoostStrength(float newBoostStrength) [member function]
    def SetBoostStrength(self, newBoostStrength: float) -> None: ...

    # float BoostModPickup::GetOldBoostStrength() [member function]
    def GetOldBoostStrength(self) -> float: ...

    # void BoostModPickup::SetOldBoostStrength(float newOldBoostStrength) [member function]
    def SetOldBoostStrength(self, newOldBoostStrength: float) -> None: ...

    # void BoostModPickup::PickupEnd() [member function]
    def PickupEnd(self) -> None: ...

    # void BoostModPickup::PickupStart() [member function]
    def PickupStart(self) -> None: ...

    # Private:
    # BoostModPickup::Impl [class declaration]

    # BoostModPickup::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


