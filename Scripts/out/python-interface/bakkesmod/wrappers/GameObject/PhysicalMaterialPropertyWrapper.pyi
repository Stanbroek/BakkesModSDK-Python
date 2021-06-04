from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class PhysicalMaterialPropertyWrapper():
    # Public:
    # PhysicalMaterialPropertyWrapper::PhysicalMaterialPropertyWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # PhysicalMaterialPropertyWrapper::PhysicalMaterialPropertyWrapper(PhysicalMaterialPropertyWrapper const & other) [constructor]

    # PhysicalMaterialPropertyWrapper & PhysicalMaterialPropertyWrapper::operator=(PhysicalMaterialPropertyWrapper rhs) [member operator]

    # PhysicalMaterialPropertyWrapper::~PhysicalMaterialPropertyWrapper() [destructor]
    def __del__(self) -> None: ...

    # bool PhysicalMaterialPropertyWrapper::IsNull() const [member function]
    def IsNull(self) -> bool: ...

    # bool PhysicalMaterialPropertyWrapper::operator bool() const [casting operator]

    # float PhysicalMaterialPropertyWrapper::GetTireFrictionScale() [member function]
    def GetTireFrictionScale(self) -> float: ...

    # void PhysicalMaterialPropertyWrapper::SetTireFrictionScale(float newTireFrictionScale) [member function]
    def SetTireFrictionScale(self, newTireFrictionScale: float) -> None: ...

    # long unsigned int PhysicalMaterialPropertyWrapper::GetbStickyWheels() [member function]
    def GetbStickyWheels(self) -> bool: ...

    # void PhysicalMaterialPropertyWrapper::SetbStickyWheels(long unsigned int newbStickyWheels) [member function]
    def SetbStickyWheels(self, newbStickyWheels: bool) -> None: ...

    # long unsigned int PhysicalMaterialPropertyWrapper::GetbConsiderForGround() [member function]
    def GetbConsiderForGround(self) -> bool: ...

    # void PhysicalMaterialPropertyWrapper::SetbConsiderForGround(long unsigned int newbConsiderForGround) [member function]
    def SetbConsiderForGround(self, newbConsiderForGround: bool) -> None: ...

    # Private:
    # PhysicalMaterialPropertyWrapper::Impl [class declaration]

    # PhysicalMaterialPropertyWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


