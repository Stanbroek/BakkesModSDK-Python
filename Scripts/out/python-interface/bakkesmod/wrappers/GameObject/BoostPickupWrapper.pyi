from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class BoostPickupWrapper():
    # Public:
    # BoostPickupWrapper::BoostPickupWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # BoostPickupWrapper::BoostPickupWrapper(BoostPickupWrapper const & other) [constructor]

    # BoostPickupWrapper & BoostPickupWrapper::operator=(BoostPickupWrapper rhs) [member operator]

    # BoostPickupWrapper::~BoostPickupWrapper() [destructor]
    def __del__(self) -> None: ...

    # float BoostPickupWrapper::GetBoostAmount() [member function]
    def GetBoostAmount(self) -> float: ...

    # void BoostPickupWrapper::SetBoostAmount(float newBoostAmount) [member function]
    def SetBoostAmount(self, newBoostAmount: float) -> None: ...

    # unsigned char BoostPickupWrapper::GetBoostType() [member function]
    def GetBoostType(self) -> int: ...

    # void BoostPickupWrapper::SetBoostType(unsigned char newBoostType) [member function]
    def SetBoostType(self, newBoostType: int) -> None: ...

    # void BoostPickupWrapper::PlayPickedUpFX() [member function]
    def PlayPickedUpFX(self) -> None: ...

    # void BoostPickupWrapper::Pickup2(CarWrapper Car) [member function]
    def Pickup2(self, Car: CarWrapper) -> None: ...

    # bool BoostPickupWrapper::CanPickup(CarWrapper Car) [member function]
    def CanPickup(self, Car: CarWrapper) -> bool: ...

    # Private:
    # BoostPickupWrapper::Impl [class declaration]

    # BoostPickupWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


