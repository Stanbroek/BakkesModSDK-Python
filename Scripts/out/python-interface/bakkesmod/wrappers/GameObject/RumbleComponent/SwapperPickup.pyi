from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class SwapperPickup():
    # Public:
    # SwapperPickup::SwapperPickup(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # SwapperPickup::SwapperPickup(SwapperPickup const & other) [constructor]

    # SwapperPickup & SwapperPickup::operator=(SwapperPickup rhs) [member operator]

    # SwapperPickup::~SwapperPickup() [destructor]
    def __del__(self) -> None: ...

    # CarWrapper SwapperPickup::GetOtherCar() [member function]
    def GetOtherCar(self) -> CarWrapper: ...

    # void SwapperPickup::SetOtherCar(CarWrapper newOtherCar) [member function]
    def SetOtherCar(self, newOtherCar: CarWrapper) -> None: ...

    # void SwapperPickup::PickupEnd() [member function]
    def PickupEnd(self) -> None: ...

    # void SwapperPickup::OnTargetChanged() [member function]
    def OnTargetChanged(self) -> None: ...

    # void SwapperPickup::PickupStart() [member function]
    def PickupStart(self) -> None: ...

    # Private:
    # SwapperPickup::Impl [class declaration]

    # SwapperPickup::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


