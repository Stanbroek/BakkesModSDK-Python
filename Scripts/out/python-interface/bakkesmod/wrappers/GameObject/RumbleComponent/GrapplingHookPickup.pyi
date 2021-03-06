from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class GrapplingHookPickup():
    # Public:
    # GrapplingHookPickup::GrapplingHookPickup(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # GrapplingHookPickup::GrapplingHookPickup(GrapplingHookPickup const & other) [constructor]

    # GrapplingHookPickup & GrapplingHookPickup::operator=(GrapplingHookPickup rhs) [member operator]

    # GrapplingHookPickup::~GrapplingHookPickup() [destructor]
    def __del__(self) -> None: ...

    # float GrapplingHookPickup::GetImpulse() [member function]
    def GetImpulse(self) -> float: ...

    # void GrapplingHookPickup::SetImpulse(float newImpulse) [member function]
    def SetImpulse(self, newImpulse: float) -> None: ...

    # float GrapplingHookPickup::GetForce() [member function]
    def GetForce(self) -> float: ...

    # void GrapplingHookPickup::SetForce(float newForce) [member function]
    def SetForce(self, newForce: float) -> None: ...

    # float GrapplingHookPickup::GetMaxRopeLength() [member function]
    def GetMaxRopeLength(self) -> float: ...

    # void GrapplingHookPickup::SetMaxRopeLength(float newMaxRopeLength) [member function]
    def SetMaxRopeLength(self, newMaxRopeLength: float) -> None: ...

    # float GrapplingHookPickup::GetPredictionSpeed() [member function]
    def GetPredictionSpeed(self) -> float: ...

    # void GrapplingHookPickup::SetPredictionSpeed(float newPredictionSpeed) [member function]
    def SetPredictionSpeed(self, newPredictionSpeed: float) -> None: ...

    # long unsigned int GrapplingHookPickup::GetbDeactivateOnTouch() [member function]
    def GetbDeactivateOnTouch(self) -> bool: ...

    # void GrapplingHookPickup::SetbDeactivateOnTouch(long unsigned int newbDeactivateOnTouch) [member function]
    def SetbDeactivateOnTouch(self, newbDeactivateOnTouch: bool) -> None: ...

    # long unsigned int GrapplingHookPickup::GetbInstant() [member function]
    def GetbInstant(self) -> bool: ...

    # void GrapplingHookPickup::SetbInstant(long unsigned int newbInstant) [member function]
    def SetbInstant(self, newbInstant: bool) -> None: ...

    # long unsigned int GrapplingHookPickup::GetbBlocked() [member function]
    def GetbBlocked(self) -> bool: ...

    # void GrapplingHookPickup::SetbBlocked(long unsigned int newbBlocked) [member function]
    def SetbBlocked(self, newbBlocked: bool) -> None: ...

    # long unsigned int GrapplingHookPickup::GetbAttachedToBall() [member function]
    def GetbAttachedToBall(self) -> bool: ...

    # void GrapplingHookPickup::SetbAttachedToBall(long unsigned int newbAttachedToBall) [member function]
    def SetbAttachedToBall(self, newbAttachedToBall: bool) -> None: ...

    # Vector GrapplingHookPickup::GetRopeMeshScale() [member function]
    def GetRopeMeshScale(self) -> Vector: ...

    # void GrapplingHookPickup::SetRopeMeshScale(Vector newRopeMeshScale) [member function]
    def SetRopeMeshScale(self, newRopeMeshScale: Vector) -> None: ...

    # float GrapplingHookPickup::GetRopeMeshInitialSize() [member function]
    def GetRopeMeshInitialSize(self) -> float: ...

    # void GrapplingHookPickup::SetRopeMeshInitialSize(float newRopeMeshInitialSize) [member function]
    def SetRopeMeshInitialSize(self, newRopeMeshInitialSize: float) -> None: ...

    # Rotator GrapplingHookPickup::GetRopeRotationOffset() [member function]
    def GetRopeRotationOffset(self) -> Rotator: ...

    # void GrapplingHookPickup::SetRopeRotationOffset(Rotator newRopeRotationOffset) [member function]
    def SetRopeRotationOffset(self, newRopeRotationOffset: Rotator) -> None: ...

    # Vector GrapplingHookPickup::GetHookMeshScale() [member function]
    def GetHookMeshScale(self) -> Vector: ...

    # void GrapplingHookPickup::SetHookMeshScale(Vector newHookMeshScale) [member function]
    def SetHookMeshScale(self, newHookMeshScale: Vector) -> None: ...

    # Vector GrapplingHookPickup::GetHookMeshOffset() [member function]
    def GetHookMeshOffset(self) -> Vector: ...

    # void GrapplingHookPickup::SetHookMeshOffset(Vector newHookMeshOffset) [member function]
    def SetHookMeshOffset(self, newHookMeshOffset: Vector) -> None: ...

    # Rotator GrapplingHookPickup::GetHookRotationOffset() [member function]
    def GetHookRotationOffset(self) -> Rotator: ...

    # void GrapplingHookPickup::SetHookRotationOffset(Rotator newHookRotationOffset) [member function]
    def SetHookRotationOffset(self, newHookRotationOffset: Rotator) -> None: ...

    # float GrapplingHookPickup::GetHitDistanceOffset() [member function]
    def GetHitDistanceOffset(self) -> float: ...

    # void GrapplingHookPickup::SetHitDistanceOffset(float newHitDistanceOffset) [member function]
    def SetHitDistanceOffset(self, newHitDistanceOffset: float) -> None: ...

    # float GrapplingHookPickup::GetAfterAttachDuration() [member function]
    def GetAfterAttachDuration(self) -> float: ...

    # void GrapplingHookPickup::SetAfterAttachDuration(float newAfterAttachDuration) [member function]
    def SetAfterAttachDuration(self, newAfterAttachDuration: float) -> None: ...

    # float GrapplingHookPickup::GetBlockedRequiredMoveDistance() [member function]
    def GetBlockedRequiredMoveDistance(self) -> float: ...

    # void GrapplingHookPickup::SetBlockedRequiredMoveDistance(float newBlockedRequiredMoveDistance) [member function]
    def SetBlockedRequiredMoveDistance(self, newBlockedRequiredMoveDistance: float) -> None: ...

    # float GrapplingHookPickup::GetBlockedRequiredMoveTime() [member function]
    def GetBlockedRequiredMoveTime(self) -> float: ...

    # void GrapplingHookPickup::SetBlockedRequiredMoveTime(float newBlockedRequiredMoveTime) [member function]
    def SetBlockedRequiredMoveTime(self, newBlockedRequiredMoveTime: float) -> None: ...

    # float GrapplingHookPickup::GetBlockedStartTime() [member function]
    def GetBlockedStartTime(self) -> float: ...

    # void GrapplingHookPickup::SetBlockedStartTime(float newBlockedStartTime) [member function]
    def SetBlockedStartTime(self, newBlockedStartTime: float) -> None: ...

    # Vector GrapplingHookPickup::GetBlockedStartPos() [member function]
    def GetBlockedStartPos(self) -> Vector: ...

    # void GrapplingHookPickup::SetBlockedStartPos(Vector newBlockedStartPos) [member function]
    def SetBlockedStartPos(self, newBlockedStartPos: Vector) -> None: ...

    # BallWrapper GrapplingHookPickup::GetBall() [member function]
    def GetBall(self) -> BallWrapper: ...

    # void GrapplingHookPickup::SetBall(BallWrapper newBall) [member function]
    def SetBall(self, newBall: BallWrapper) -> None: ...

    # Vector GrapplingHookPickup::GetRopeOrigin() [member function]
    def GetRopeOrigin(self) -> Vector: ...

    # void GrapplingHookPickup::SetRopeOrigin(Vector newRopeOrigin) [member function]
    def SetRopeOrigin(self, newRopeOrigin: Vector) -> None: ...

    # float GrapplingHookPickup::GetRopeToTime() [member function]
    def GetRopeToTime(self) -> float: ...

    # void GrapplingHookPickup::SetRopeToTime(float newRopeToTime) [member function]
    def SetRopeToTime(self, newRopeToTime: float) -> None: ...

    # float GrapplingHookPickup::GetCurrentRopeLength() [member function]
    def GetCurrentRopeLength(self) -> float: ...

    # void GrapplingHookPickup::SetCurrentRopeLength(float newCurrentRopeLength) [member function]
    def SetCurrentRopeLength(self, newCurrentRopeLength: float) -> None: ...

    # float GrapplingHookPickup::GetAttachTime() [member function]
    def GetAttachTime(self) -> float: ...

    # void GrapplingHookPickup::SetAttachTime(float newAttachTime) [member function]
    def SetAttachTime(self, newAttachTime: float) -> None: ...

    # void GrapplingHookPickup::HandleBallExploded(BallWrapper InBall) [member function]
    def HandleBallExploded(self, InBall: BallWrapper) -> None: ...

    # void GrapplingHookPickup::PickupEnd() [member function]
    def PickupEnd(self) -> None: ...

    # void GrapplingHookPickup::ScaleMeshToLocation(Vector & NewLocation, Vector & TargetLocation) [member function]
    def ScaleMeshToLocation(self, NewLocation: Vector, TargetLocation: Vector) -> None: ...

    # Vector GrapplingHookPickup::GetPredictedBallLocation(BallWrapper InBall) [member function]
    def GetPredictedBallLocation(self, InBall: BallWrapper) -> Vector: ...

    # Vector GrapplingHookPickup::GetTargetedLocation() [member function]
    def GetTargetedLocation(self) -> Vector: ...

    # void GrapplingHookPickup::UpdateVisual(float DeltaTime) [member function]
    def UpdateVisual(self, DeltaTime: float) -> None: ...

    # void GrapplingHookPickup::PickupTick(float DeltaTime) [member function]
    def PickupTick(self, DeltaTime: float) -> None: ...

    # void GrapplingHookPickup::ApplyForces(float ActiveTime) [member function]
    def ApplyForces(self, ActiveTime: float) -> None: ...

    # void GrapplingHookPickup::DoAttach() [member function]
    def DoAttach(self) -> None: ...

    # void GrapplingHookPickup::PickupStart() [member function]
    def PickupStart(self) -> None: ...

    # Private:
    # GrapplingHookPickup::Impl [class declaration]

    # GrapplingHookPickup::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


