from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class VehicleSimWrapper():
    # Public:
    # VehicleSimWrapper::VehicleSimWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # VehicleSimWrapper::VehicleSimWrapper(VehicleSimWrapper const & other) [constructor]

    # VehicleSimWrapper & VehicleSimWrapper::operator=(VehicleSimWrapper rhs) [member operator]

    # VehicleSimWrapper::~VehicleSimWrapper() [destructor]
    def __del__(self) -> None: ...

    # bool VehicleSimWrapper::IsNull() const [member function]
    def IsNull(self) -> bool: ...

    # bool VehicleSimWrapper::operator bool() const [casting operator]

    # ArrayWrapper<WheelWrapper> VehicleSimWrapper::GetWheels() [member function]
    def GetWheels(self) -> ArrayWrapper_WheelWrapper: ...

    # float VehicleSimWrapper::GetDriveTorque() [member function]
    def GetDriveTorque(self) -> float: ...

    # void VehicleSimWrapper::SetDriveTorque(float newDriveTorque) [member function]
    def SetDriveTorque(self, newDriveTorque: float) -> None: ...

    # float VehicleSimWrapper::GetBrakeTorque() [member function]
    def GetBrakeTorque(self) -> float: ...

    # void VehicleSimWrapper::SetBrakeTorque(float newBrakeTorque) [member function]
    def SetBrakeTorque(self, newBrakeTorque: float) -> None: ...

    # float VehicleSimWrapper::GetStopThreshold() [member function]
    def GetStopThreshold(self) -> float: ...

    # void VehicleSimWrapper::SetStopThreshold(float newStopThreshold) [member function]
    def SetStopThreshold(self, newStopThreshold: float) -> None: ...

    # float VehicleSimWrapper::GetIdleBrakeFactor() [member function]
    def GetIdleBrakeFactor(self) -> float: ...

    # void VehicleSimWrapper::SetIdleBrakeFactor(float newIdleBrakeFactor) [member function]
    def SetIdleBrakeFactor(self, newIdleBrakeFactor: float) -> None: ...

    # float VehicleSimWrapper::GetOppositeBrakeFactor() [member function]
    def GetOppositeBrakeFactor(self) -> float: ...

    # void VehicleSimWrapper::SetOppositeBrakeFactor(float newOppositeBrakeFactor) [member function]
    def SetOppositeBrakeFactor(self, newOppositeBrakeFactor: float) -> None: ...

    # long unsigned int VehicleSimWrapper::GetbUseAckermannSteering() [member function]
    def GetbUseAckermannSteering(self) -> bool: ...

    # void VehicleSimWrapper::SetbUseAckermannSteering(long unsigned int newbUseAckermannSteering) [member function]
    def SetbUseAckermannSteering(self, newbUseAckermannSteering: bool) -> None: ...

    # long unsigned int VehicleSimWrapper::GetbWasAttached() [member function]
    def GetbWasAttached(self) -> bool: ...

    # void VehicleSimWrapper::SetbWasAttached(long unsigned int newbWasAttached) [member function]
    def SetbWasAttached(self, newbWasAttached: bool) -> None: ...

    # float VehicleSimWrapper::GetOutputThrottle() [member function]
    def GetOutputThrottle(self) -> float: ...

    # void VehicleSimWrapper::SetOutputThrottle(float newOutputThrottle) [member function]
    def SetOutputThrottle(self, newOutputThrottle: float) -> None: ...

    # float VehicleSimWrapper::GetOutputSteer() [member function]
    def GetOutputSteer(self) -> float: ...

    # void VehicleSimWrapper::SetOutputSteer(float newOutputSteer) [member function]
    def SetOutputSteer(self, newOutputSteer: float) -> None: ...

    # float VehicleSimWrapper::GetOutputBrake() [member function]
    def GetOutputBrake(self) -> float: ...

    # void VehicleSimWrapper::SetOutputBrake(float newOutputBrake) [member function]
    def SetOutputBrake(self, newOutputBrake: float) -> None: ...

    # float VehicleSimWrapper::GetOutputHandbrake() [member function]
    def GetOutputHandbrake(self) -> float: ...

    # void VehicleSimWrapper::SetOutputHandbrake(float newOutputHandbrake) [member function]
    def SetOutputHandbrake(self, newOutputHandbrake: float) -> None: ...

    # VehicleWrapper VehicleSimWrapper::GetVehicle() [member function]
    def GetVehicle(self) -> VehicleWrapper: ...

    # void VehicleSimWrapper::SetVehicle(VehicleWrapper newVehicle) [member function]
    def SetVehicle(self, newVehicle: VehicleWrapper) -> None: ...

    # CarWrapper VehicleSimWrapper::GetCar() [member function]
    def GetCar(self) -> CarWrapper: ...

    # void VehicleSimWrapper::SetCar(CarWrapper newCar) [member function]
    def SetCar(self, newCar: CarWrapper) -> None: ...

    # float VehicleSimWrapper::GetSteeringSensitivity() [member function]
    def GetSteeringSensitivity(self) -> float: ...

    # void VehicleSimWrapper::SetSteeringSensitivity(float newSteeringSensitivity) [member function]
    def SetSteeringSensitivity(self, newSteeringSensitivity: float) -> None: ...

    # Private:
    # VehicleSimWrapper::Impl [class declaration]

    # VehicleSimWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


