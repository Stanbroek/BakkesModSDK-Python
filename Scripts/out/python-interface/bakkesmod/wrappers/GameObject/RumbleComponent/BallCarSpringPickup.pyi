from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class BallCarSpringPickup():
    # Public:
    # BallCarSpringPickup::BallCarSpringPickup(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # BallCarSpringPickup::BallCarSpringPickup(BallCarSpringPickup const & other) [constructor]

    # BallCarSpringPickup & BallCarSpringPickup::operator=(BallCarSpringPickup rhs) [member operator]

    # BallCarSpringPickup::~BallCarSpringPickup() [destructor]
    def __del__(self) -> None: ...

    # void BallCarSpringPickup::ScaleSpringMeshToLocation(Vector & NewLocation, Vector & TargetLocation) [member function]
    def ScaleSpringMeshToLocation(self, NewLocation: Vector, TargetLocation: Vector) -> None: ...

    # Private:
    # BallCarSpringPickup::Impl [class declaration]

    # BallCarSpringPickup::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


