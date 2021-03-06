from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class WheelWrapper():
    # Public:
    # WheelWrapper::WheelWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # WheelWrapper::WheelWrapper(WheelWrapper const & other) [constructor]

    # WheelWrapper & WheelWrapper::operator=(WheelWrapper rhs) [member operator]

    # WheelWrapper::~WheelWrapper() [destructor]
    def __del__(self) -> None: ...

    # bool WheelWrapper::IsNull() const [member function]
    def IsNull(self) -> bool: ...

    # bool WheelWrapper::operator bool() const [casting operator]

    # float WheelWrapper::GetSteerFactor() [member function]
    def GetSteerFactor(self) -> float: ...

    # void WheelWrapper::SetSteerFactor(float newSteerFactor) [member function]
    def SetSteerFactor(self, newSteerFactor: float) -> None: ...

    # float WheelWrapper::GetWheelRadius() [member function]
    def GetWheelRadius(self) -> float: ...

    # void WheelWrapper::SetWheelRadius(float newWheelRadius) [member function]
    def SetWheelRadius(self, newWheelRadius: float) -> None: ...

    # float WheelWrapper::GetSuspensionStiffness() [member function]
    def GetSuspensionStiffness(self) -> float: ...

    # void WheelWrapper::SetSuspensionStiffness(float newSuspensionStiffness) [member function]
    def SetSuspensionStiffness(self, newSuspensionStiffness: float) -> None: ...

    # float WheelWrapper::GetSuspensionDampingCompression() [member function]
    def GetSuspensionDampingCompression(self) -> float: ...

    # void WheelWrapper::SetSuspensionDampingCompression(float newSuspensionDampingCompression) [member function]
    def SetSuspensionDampingCompression(self, newSuspensionDampingCompression: float) -> None: ...

    # float WheelWrapper::GetSuspensionDampingRelaxation() [member function]
    def GetSuspensionDampingRelaxation(self) -> float: ...

    # void WheelWrapper::SetSuspensionDampingRelaxation(float newSuspensionDampingRelaxation) [member function]
    def SetSuspensionDampingRelaxation(self, newSuspensionDampingRelaxation: float) -> None: ...

    # float WheelWrapper::GetSuspensionTravel() [member function]
    def GetSuspensionTravel(self) -> float: ...

    # void WheelWrapper::SetSuspensionTravel(float newSuspensionTravel) [member function]
    def SetSuspensionTravel(self, newSuspensionTravel: float) -> None: ...

    # float WheelWrapper::GetSuspensionMaxRaise() [member function]
    def GetSuspensionMaxRaise(self) -> float: ...

    # void WheelWrapper::SetSuspensionMaxRaise(float newSuspensionMaxRaise) [member function]
    def SetSuspensionMaxRaise(self, newSuspensionMaxRaise: float) -> None: ...

    # float WheelWrapper::GetContactForceDistance() [member function]
    def GetContactForceDistance(self) -> float: ...

    # void WheelWrapper::SetContactForceDistance(float newContactForceDistance) [member function]
    def SetContactForceDistance(self, newContactForceDistance: float) -> None: ...

    # float WheelWrapper::GetSpinSpeedDecayRate() [member function]
    def GetSpinSpeedDecayRate(self) -> float: ...

    # void WheelWrapper::SetSpinSpeedDecayRate(float newSpinSpeedDecayRate) [member function]
    def SetSpinSpeedDecayRate(self, newSpinSpeedDecayRate: float) -> None: ...

    # Vector WheelWrapper::GetBoneOffset() [member function]
    def GetBoneOffset(self) -> Vector: ...

    # void WheelWrapper::SetBoneOffset(Vector newBoneOffset) [member function]
    def SetBoneOffset(self, newBoneOffset: Vector) -> None: ...

    # Vector WheelWrapper::GetPresetRestPosition() [member function]
    def GetPresetRestPosition(self) -> Vector: ...

    # void WheelWrapper::SetPresetRestPosition(Vector newPresetRestPosition) [member function]
    def SetPresetRestPosition(self, newPresetRestPosition: Vector) -> None: ...

    # Vector WheelWrapper::GetLocalSuspensionRayStart() [member function]
    def GetLocalSuspensionRayStart(self) -> Vector: ...

    # void WheelWrapper::SetLocalSuspensionRayStart(Vector newLocalSuspensionRayStart) [member function]
    def SetLocalSuspensionRayStart(self, newLocalSuspensionRayStart: Vector) -> None: ...

    # Vector WheelWrapper::GetLocalRestPosition() [member function]
    def GetLocalRestPosition(self) -> Vector: ...

    # void WheelWrapper::SetLocalRestPosition(Vector newLocalRestPosition) [member function]
    def SetLocalRestPosition(self, newLocalRestPosition: Vector) -> None: ...

    # VehicleSimWrapper WheelWrapper::GetVehicleSim() [member function]
    def GetVehicleSim(self) -> VehicleSimWrapper: ...

    # void WheelWrapper::SetVehicleSim(VehicleSimWrapper newVehicleSim) [member function]
    def SetVehicleSim(self, newVehicleSim: VehicleSimWrapper) -> None: ...

    # int WheelWrapper::GetWheelIndex() [member function]
    def GetWheelIndex(self) -> int: ...

    # void WheelWrapper::SetWheelIndex(int newWheelIndex) [member function]
    def SetWheelIndex(self, newWheelIndex: int) -> None: ...

    # WheelContactData WheelWrapper::GetContact() [member function]
    def GetContact(self) -> WheelContactData: ...

    # void WheelWrapper::SetContact(WheelContactData newContact) [member function]
    def SetContact(self, newContact: WheelContactData) -> None: ...

    # long unsigned int WheelWrapper::GetbDrawDebug() [member function]
    def GetbDrawDebug(self) -> bool: ...

    # void WheelWrapper::SetbDrawDebug(long unsigned int newbDrawDebug) [member function]
    def SetbDrawDebug(self, newbDrawDebug: bool) -> None: ...

    # long unsigned int WheelWrapper::GetbHadContact() [member function]
    def GetbHadContact(self) -> bool: ...

    # void WheelWrapper::SetbHadContact(long unsigned int newbHadContact) [member function]
    def SetbHadContact(self, newbHadContact: bool) -> None: ...

    # float WheelWrapper::GetFrictionCurveInput() [member function]
    def GetFrictionCurveInput(self) -> float: ...

    # void WheelWrapper::SetFrictionCurveInput(float newFrictionCurveInput) [member function]
    def SetFrictionCurveInput(self, newFrictionCurveInput: float) -> None: ...

    # float WheelWrapper::GetAerialThrottleToVelocityFactor() [member function]
    def GetAerialThrottleToVelocityFactor(self) -> float: ...

    # void WheelWrapper::SetAerialThrottleToVelocityFactor(float newAerialThrottleToVelocityFactor) [member function]
    def SetAerialThrottleToVelocityFactor(self, newAerialThrottleToVelocityFactor: float) -> None: ...

    # float WheelWrapper::GetAerialAccelerationFactor() [member function]
    def GetAerialAccelerationFactor(self) -> float: ...

    # void WheelWrapper::SetAerialAccelerationFactor(float newAerialAccelerationFactor) [member function]
    def SetAerialAccelerationFactor(self, newAerialAccelerationFactor: float) -> None: ...

    # float WheelWrapper::GetSpinSpeed() [member function]
    def GetSpinSpeed(self) -> float: ...

    # void WheelWrapper::SetSpinSpeed(float newSpinSpeed) [member function]
    def SetSpinSpeed(self, newSpinSpeed: float) -> None: ...

    # Vector WheelWrapper::GetRefWheelLocation() [member function]
    def GetRefWheelLocation(self) -> Vector: ...

    # float WheelWrapper::GetSuspensionDistance() [member function]
    def GetSuspensionDistance(self) -> float: ...

    # float WheelWrapper::GetSteer2() [member function]
    def GetSteer2(self) -> float: ...

    # Vector WheelWrapper::GetLinearVelocity() [member function]
    def GetLinearVelocity(self) -> Vector: ...

    # void WheelWrapper::EventContactChanged(WheelWrapper Wheel) [member function]
    def EventContactChanged(self, Wheel: WheelWrapper) -> None: ...

    # Private:
    # WheelWrapper::Impl [class declaration]

    # WheelWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


