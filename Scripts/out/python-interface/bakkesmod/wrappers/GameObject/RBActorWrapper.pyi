from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class RBActorWrapper():
    # Public:
    # RBActorWrapper::RBActorWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # RBActorWrapper::RBActorWrapper(RBActorWrapper const & other) [constructor]

    # RBActorWrapper & RBActorWrapper::operator=(RBActorWrapper rhs) [member operator]

    # RBActorWrapper::~RBActorWrapper() [destructor]
    def __del__(self) -> None: ...

    # float RBActorWrapper::GetMaxLinearSpeed() [member function]
    def GetMaxLinearSpeed(self) -> float: ...

    # void RBActorWrapper::SetMaxLinearSpeed(float newMaxLinearSpeed) [member function]
    def SetMaxLinearSpeed(self, newMaxLinearSpeed: float) -> None: ...

    # float RBActorWrapper::GetMaxAngularSpeed() [member function]
    def GetMaxAngularSpeed(self) -> float: ...

    # void RBActorWrapper::SetMaxAngularSpeed(float newMaxAngularSpeed) [member function]
    def SetMaxAngularSpeed(self, newMaxAngularSpeed: float) -> None: ...

    # long unsigned int RBActorWrapper::GetbDisableSleeping() [member function]
    def GetbDisableSleeping(self) -> bool: ...

    # void RBActorWrapper::SetbDisableSleeping(long unsigned int newbDisableSleeping) [member function]
    def SetbDisableSleeping(self, newbDisableSleeping: bool) -> None: ...

    # long unsigned int RBActorWrapper::GetbReplayActor() [member function]
    def GetbReplayActor(self) -> bool: ...

    # void RBActorWrapper::SetbReplayActor(long unsigned int newbReplayActor) [member function]
    def SetbReplayActor(self, newbReplayActor: bool) -> None: ...

    # long unsigned int RBActorWrapper::GetbFrozen() [member function]
    def GetbFrozen(self) -> bool: ...

    # void RBActorWrapper::SetbFrozen(long unsigned int newbFrozen) [member function]
    def SetbFrozen(self, newbFrozen: bool) -> None: ...

    # long unsigned int RBActorWrapper::GetbIgnoreSyncing() [member function]
    def GetbIgnoreSyncing(self) -> bool: ...

    # void RBActorWrapper::SetbIgnoreSyncing(long unsigned int newbIgnoreSyncing) [member function]
    def SetbIgnoreSyncing(self, newbIgnoreSyncing: bool) -> None: ...

    # long unsigned int RBActorWrapper::GetbPhysInitialized() [member function]
    def GetbPhysInitialized(self) -> bool: ...

    # RBState RBActorWrapper::GetOldRBState() [member function]
    def GetOldRBState(self) -> RBState: ...

    # void RBActorWrapper::SetOldRBState(RBState newOldRBState) [member function]
    def SetOldRBState(self, newOldRBState: RBState) -> None: ...

    # RBState RBActorWrapper::GetRBState() [member function]
    def GetRBState(self) -> RBState: ...

    # void RBActorWrapper::SetRBState(RBState newRBState) [member function]
    def SetRBState(self, newRBState: RBState) -> None: ...

    # RBState RBActorWrapper::GetReplicatedRBState() [member function]
    def GetReplicatedRBState(self) -> RBState: ...

    # void RBActorWrapper::SetReplicatedRBState(RBState newReplicatedRBState) [member function]
    def SetReplicatedRBState(self, newReplicatedRBState: RBState) -> None: ...

    # RBState RBActorWrapper::GetClientCorrectionRBState() [member function]
    def GetClientCorrectionRBState(self) -> RBState: ...

    # void RBActorWrapper::SetClientCorrectionRBState(RBState newClientCorrectionRBState) [member function]
    def SetClientCorrectionRBState(self, newClientCorrectionRBState: RBState) -> None: ...

    # WorldContactData RBActorWrapper::GetWorldContact() [member function]
    def GetWorldContact(self) -> WorldContactData: ...

    # void RBActorWrapper::SetWorldContact(WorldContactData newWorldContact) [member function]
    def SetWorldContact(self, newWorldContact: WorldContactData) -> None: ...

    # Vector RBActorWrapper::GetSyncErrorLocation() [member function]
    def GetSyncErrorLocation(self) -> Vector: ...

    # float RBActorWrapper::GetSyncErrorAngle() [member function]
    def GetSyncErrorAngle(self) -> float: ...

    # Vector RBActorWrapper::GetSyncErrorAxis() [member function]
    def GetSyncErrorAxis(self) -> Vector: ...

    # FXActorWrapper RBActorWrapper::GetFXActorArchetype() [member function]
    def GetFXActorArchetype(self) -> FXActorWrapper: ...

    # void RBActorWrapper::SetFXActorArchetype(FXActorWrapper newFXActorArchetype) [member function]
    def SetFXActorArchetype(self, newFXActorArchetype: FXActorWrapper) -> None: ...

    # FXActorWrapper RBActorWrapper::GetFXActor() [member function]
    def GetFXActor(self) -> FXActorWrapper: ...

    # void RBActorWrapper::SetFXActor(FXActorWrapper newFXActor) [member function]
    def SetFXActor(self, newFXActor: FXActorWrapper) -> None: ...

    # int RBActorWrapper::GetLastRBCollisionsFrame() [member function]
    def GetLastRBCollisionsFrame(self) -> int: ...

    # RBActorWrapper RBActorWrapper::GetWeldedActor() [member function]
    def GetWeldedActor(self) -> RBActorWrapper: ...

    # RBActorWrapper RBActorWrapper::GetWeldedTo() [member function]
    def GetWeldedTo(self) -> RBActorWrapper: ...

    # float RBActorWrapper::GetPreWeldMass() [member function]
    def GetPreWeldMass(self) -> float: ...

    # void RBActorWrapper::SetMass(float NewMass) [member function]
    def SetMass(self, NewMass: float) -> None: ...

    # void RBActorWrapper::SetConstrained3D(Vector & LinearLower, Vector & LinearUpper, Vector & AngularLower, Vector & AngularUpper) [member function]
    def SetConstrained3D(self, LinearLower: Vector, LinearUpper: Vector, AngularLower: Vector, AngularUpper: Vector) -> None: ...

    # void RBActorWrapper::SetConstrained2D(long unsigned int bConstrain2D) [member function]
    def SetConstrained2D(self, bConstrain2D: bool) -> None: ...

    # void RBActorWrapper::SetPhysicsState(RBState & NewState) [member function]
    def SetPhysicsState(self, NewState: RBState) -> None: ...

    # void RBActorWrapper::SetFrozen(long unsigned int bEnabled) [member function]
    def SetFrozen(self, bEnabled: bool) -> None: ...

    # void RBActorWrapper::SetMaxAngularSpeed2(float NewMaxSpeed) [member function]
    def SetMaxAngularSpeed2(self, NewMaxSpeed: float) -> None: ...

    # void RBActorWrapper::SetMaxLinearSpeed2(float NewMaxSpeed) [member function]
    def SetMaxLinearSpeed2(self, NewMaxSpeed: float) -> None: ...

    # void RBActorWrapper::AddTorque(Vector & Torque, unsigned char ForceMode) [member function]
    def AddTorque(self, Torque: Vector, ForceMode: int) -> None: ...

    # void RBActorWrapper::AddForce(Vector & Force, unsigned char ForceMode) [member function]
    def AddForce(self, Force: Vector, ForceMode: int) -> None: ...

    # void RBActorWrapper::UnWeldRBActor(RBActorWrapper Other) [member function]
    def UnWeldRBActor(self, Other: RBActorWrapper) -> None: ...

    # void RBActorWrapper::WeldRBActor2(RBActorWrapper Other, Vector & WeldOffset, Rotator & WeldRotation) [member function]
    def WeldRBActor2(self, Other: RBActorWrapper, WeldOffset: Vector, WeldRotation: Rotator) -> None: ...

    # void RBActorWrapper::ReInitRBPhys() [member function]
    def ReInitRBPhys(self) -> None: ...

    # void RBActorWrapper::TerminateRBPhys() [member function]
    def TerminateRBPhys(self) -> None: ...

    # Vector RBActorWrapper::GetCurrentRBLocation() [member function]
    def GetCurrentRBLocation(self) -> Vector: ...

    # RBState RBActorWrapper::GetCurrentRBState() [member function]
    def GetCurrentRBState(self) -> RBState: ...

    # int RBActorWrapper::GetPhysicsFrame() [member function]
    def GetPhysicsFrame(self) -> int: ...

    # float RBActorWrapper::GetPhysicsTime() [member function]
    def GetPhysicsTime(self) -> float: ...

    # void RBActorWrapper::InitAk() [member function]
    def InitAk(self) -> None: ...

    # void RBActorWrapper::eventPreBeginPlay() [member function]
    def eventPreBeginPlay(self) -> None: ...

    # Private:
    # RBActorWrapper::Impl [class declaration]

    # RBActorWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


