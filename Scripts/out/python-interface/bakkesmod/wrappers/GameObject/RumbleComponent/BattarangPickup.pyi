from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class BattarangPickup():
    # Public:
    # BattarangPickup::BattarangPickup(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # BattarangPickup::BattarangPickup(BattarangPickup const & other) [constructor]

    # BattarangPickup & BattarangPickup::operator=(BattarangPickup rhs) [member operator]

    # BattarangPickup::~BattarangPickup() [destructor]
    def __del__(self) -> None: ...

    # float BattarangPickup::GetSpinSpeed() [member function]
    def GetSpinSpeed(self) -> float: ...

    # void BattarangPickup::SetSpinSpeed(float newSpinSpeed) [member function]
    def SetSpinSpeed(self, newSpinSpeed: float) -> None: ...

    # float BattarangPickup::GetCurRotation() [member function]
    def GetCurRotation(self) -> float: ...

    # void BattarangPickup::SetCurRotation(float newCurRotation) [member function]
    def SetCurRotation(self, newCurRotation: float) -> None: ...

    # Private:
    # BattarangPickup::Impl [class declaration]

    # BattarangPickup::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


