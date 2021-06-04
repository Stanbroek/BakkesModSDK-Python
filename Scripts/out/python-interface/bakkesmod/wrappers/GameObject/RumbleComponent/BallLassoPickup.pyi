from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class BallLassoPickup():
    # Public:
    # BallLassoPickup::BallLassoPickup(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # BallLassoPickup::BallLassoPickup(BallLassoPickup const & other) [constructor]

    # BallLassoPickup & BallLassoPickup::operator=(BallLassoPickup rhs) [member operator]

    # BallLassoPickup::~BallLassoPickup() [destructor]
    def __del__(self) -> None: ...

    # void BallLassoPickup::ScaleSpringMeshToLocation(Vector & NewLocation, Vector & TargetLocation) [member function]
    def ScaleSpringMeshToLocation(self, NewLocation: Vector, TargetLocation: Vector) -> None: ...

    # void BallLassoPickup::DoSpring(long unsigned int bFirstHit) [member function]
    def DoSpring(self, bFirstHit: bool) -> None: ...

    # Private:
    # BallLassoPickup::Impl [class declaration]

    # BallLassoPickup::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


