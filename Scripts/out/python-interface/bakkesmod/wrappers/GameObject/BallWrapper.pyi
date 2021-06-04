from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class BallWrapper():
    # Public:
    # BallWrapper::BallWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # BallWrapper::BallWrapper(BallWrapper const & other) [constructor]

    # BallWrapper & BallWrapper::operator=(BallWrapper rhs) [member operator]

    # BallWrapper::~BallWrapper() [destructor]
    def __del__(self) -> None: ...

    # float BallWrapper::GetLastTouchTime() [member function]
    def GetLastTouchTime(self) -> float: ...

    # PredictionInfo BallWrapper::PredictPosition(float timeAhead) [member function]
    def PredictPosition(self, timeAhead: float) -> PredictionInfo: ...

    # FXActorWrapper BallWrapper::GetEndOfGameFXArchetype() [member function]
    def GetEndOfGameFXArchetype(self) -> FXActorWrapper: ...

    # void BallWrapper::SetEndOfGameFXArchetype(FXActorWrapper newEndOfGameFXArchetype) [member function]
    def SetEndOfGameFXArchetype(self, newEndOfGameFXArchetype: FXActorWrapper) -> None: ...

    # long unsigned int BallWrapper::GetbAllowPlayerExplosionOverride() [member function]
    def GetbAllowPlayerExplosionOverride(self) -> bool: ...

    # void BallWrapper::SetbAllowPlayerExplosionOverride(long unsigned int newbAllowPlayerExplosionOverride) [member function]
    def SetbAllowPlayerExplosionOverride(self, newbAllowPlayerExplosionOverride: bool) -> None: ...

    # long unsigned int BallWrapper::GetbNotifyGroundHit() [member function]
    def GetbNotifyGroundHit(self) -> bool: ...

    # void BallWrapper::SetbNotifyGroundHit(long unsigned int newbNotifyGroundHit) [member function]
    def SetbNotifyGroundHit(self, newbNotifyGroundHit: bool) -> None: ...

    # long unsigned int BallWrapper::GetbEndOfGameHidden() [member function]
    def GetbEndOfGameHidden(self) -> bool: ...

    # void BallWrapper::SetbEndOfGameHidden(long unsigned int newbEndOfGameHidden) [member function]
    def SetbEndOfGameHidden(self, newbEndOfGameHidden: bool) -> None: ...

    # long unsigned int BallWrapper::GetbFadeIn() [member function]
    def GetbFadeIn(self) -> bool: ...

    # void BallWrapper::SetbFadeIn(long unsigned int newbFadeIn) [member function]
    def SetbFadeIn(self, newbFadeIn: bool) -> None: ...

    # long unsigned int BallWrapper::GetbFadeOut() [member function]
    def GetbFadeOut(self) -> bool: ...

    # void BallWrapper::SetbFadeOut(long unsigned int newbFadeOut) [member function]
    def SetbFadeOut(self, newbFadeOut: bool) -> None: ...

    # long unsigned int BallWrapper::GetbPredictionOnGround() [member function]
    def GetbPredictionOnGround(self) -> bool: ...

    # void BallWrapper::SetbPredictionOnGround(long unsigned int newbPredictionOnGround) [member function]
    def SetbPredictionOnGround(self, newbPredictionOnGround: bool) -> None: ...

    # long unsigned int BallWrapper::GetbCanBeAttached() [member function]
    def GetbCanBeAttached(self) -> bool: ...

    # void BallWrapper::SetbCanBeAttached(long unsigned int newbCanBeAttached) [member function]
    def SetbCanBeAttached(self, newbCanBeAttached: bool) -> None: ...

    # long unsigned int BallWrapper::GetbItemFreeze() [member function]
    def GetbItemFreeze(self) -> bool: ...

    # void BallWrapper::SetbItemFreeze(long unsigned int newbItemFreeze) [member function]
    def SetbItemFreeze(self, newbItemFreeze: bool) -> None: ...

    # Vector BallWrapper::GetMagnusCoefficient() [member function]
    def GetMagnusCoefficient(self) -> Vector: ...

    # void BallWrapper::SetMagnusCoefficient(Vector newMagnusCoefficient) [member function]
    def SetMagnusCoefficient(self, newMagnusCoefficient: Vector) -> None: ...

    # float BallWrapper::GetRadius() [member function]
    def GetRadius(self) -> float: ...

    # void BallWrapper::SetRadius(float newRadius) [member function]
    def SetRadius(self, newRadius: float) -> None: ...

    # float BallWrapper::GetVisualRadius() [member function]
    def GetVisualRadius(self) -> float: ...

    # void BallWrapper::SetVisualRadius(float newVisualRadius) [member function]
    def SetVisualRadius(self, newVisualRadius: float) -> None: ...

    # float BallWrapper::GetLastCalculateCarHit() [member function]
    def GetLastCalculateCarHit(self) -> float: ...

    # Vector BallWrapper::GetInitialLocation() [member function]
    def GetInitialLocation(self) -> Vector: ...

    # void BallWrapper::SetInitialLocation(Vector newInitialLocation) [member function]
    def SetInitialLocation(self, newInitialLocation: Vector) -> None: ...

    # void BallWrapper::SetInitialRotation(Rotator newInitialRotation) [member function]
    def SetInitialRotation(self, newInitialRotation: Rotator) -> None: ...

    # float BallWrapper::GetLastHitWorldTime() [member function]
    def GetLastHitWorldTime(self) -> float: ...

    # float BallWrapper::GetReplicatedBallScale() [member function]
    def GetReplicatedBallScale(self) -> float: ...

    # void BallWrapper::SetReplicatedBallScale(float newReplicatedBallScale) [member function]
    def SetReplicatedBallScale(self, newReplicatedBallScale: float) -> None: ...

    # float BallWrapper::GetReplicatedWorldBounceScale() [member function]
    def GetReplicatedWorldBounceScale(self) -> float: ...

    # void BallWrapper::SetReplicatedWorldBounceScale(float newReplicatedWorldBounceScale) [member function]
    def SetReplicatedWorldBounceScale(self, newReplicatedWorldBounceScale: float) -> None: ...

    # float BallWrapper::GetReplicatedBallGravityScale() [member function]
    def GetReplicatedBallGravityScale(self) -> float: ...

    # void BallWrapper::SetReplicatedBallGravityScale(float newReplicatedBallGravityScale) [member function]
    def SetReplicatedBallGravityScale(self, newReplicatedBallGravityScale: float) -> None: ...

    # float BallWrapper::GetReplicatedBallMaxLinearSpeedScale() [member function]
    def GetReplicatedBallMaxLinearSpeedScale(self) -> float: ...

    # void BallWrapper::SetReplicatedBallMaxLinearSpeedScale(float newReplicatedBallMaxLinearSpeedScale) [member function]
    def SetReplicatedBallMaxLinearSpeedScale(self, newReplicatedBallMaxLinearSpeedScale: float) -> None: ...

    # float BallWrapper::GetReplicatedAddedCarBounceScale() [member function]
    def GetReplicatedAddedCarBounceScale(self) -> float: ...

    # void BallWrapper::SetReplicatedAddedCarBounceScale(float newReplicatedAddedCarBounceScale) [member function]
    def SetReplicatedAddedCarBounceScale(self, newReplicatedAddedCarBounceScale: float) -> None: ...

    # float BallWrapper::GetAdditionalCarGroundBounceScaleZ() [member function]
    def GetAdditionalCarGroundBounceScaleZ(self) -> float: ...

    # void BallWrapper::SetAdditionalCarGroundBounceScaleZ(float newAdditionalCarGroundBounceScaleZ) [member function]
    def SetAdditionalCarGroundBounceScaleZ(self, newAdditionalCarGroundBounceScaleZ: float) -> None: ...

    # float BallWrapper::GetAdditionalCarGroundBounceScaleXY() [member function]
    def GetAdditionalCarGroundBounceScaleXY(self) -> float: ...

    # void BallWrapper::SetAdditionalCarGroundBounceScaleXY(float newAdditionalCarGroundBounceScaleXY) [member function]
    def SetAdditionalCarGroundBounceScaleXY(self, newAdditionalCarGroundBounceScaleXY: float) -> None: ...

    # unsigned char BallWrapper::GetHitTeamNum() [member function]
    def GetHitTeamNum(self) -> int: ...

    # void BallWrapper::SetHitTeamNum(unsigned char newHitTeamNum) [member function]
    def SetHitTeamNum(self, newHitTeamNum: int) -> None: ...

    # ServerWrapper BallWrapper::GetGameEvent() [member function]
    def GetGameEvent(self) -> ServerWrapper: ...

    # float BallWrapper::GetExplosionTime() [member function]
    def GetExplosionTime(self) -> float: ...

    # void BallWrapper::SetExplosionTime(float newExplosionTime) [member function]
    def SetExplosionTime(self, newExplosionTime: float) -> None: ...

    # Vector BallWrapper::GetOldLocation() [member function]
    def GetOldLocation(self) -> Vector: ...

    # void BallWrapper::SetOldLocation(Vector newOldLocation) [member function]
    def SetOldLocation(self, newOldLocation: Vector) -> None: ...

    # float BallWrapper::GetPredictionTimestep() [member function]
    def GetPredictionTimestep(self) -> float: ...

    # void BallWrapper::SetPredictionTimestep(float newPredictionTimestep) [member function]
    def SetPredictionTimestep(self, newPredictionTimestep: float) -> None: ...

    # float BallWrapper::GetLastPredictionTime() [member function]
    def GetLastPredictionTime(self) -> float: ...

    # void BallWrapper::SetLastPredictionTime(float newLastPredictionTime) [member function]
    def SetLastPredictionTime(self, newLastPredictionTime: float) -> None: ...

    # float BallWrapper::GetGroundForce() [member function]
    def GetGroundForce(self) -> float: ...

    # void BallWrapper::SetGroundForce(float newGroundForce) [member function]
    def SetGroundForce(self, newGroundForce: float) -> None: ...

    # CarWrapper BallWrapper::GetCurrentAffector() [member function]
    def GetCurrentAffector(self) -> CarWrapper: ...

    # void BallWrapper::SetCurrentAffector(CarWrapper newCurrentAffector) [member function]
    def SetCurrentAffector(self, newCurrentAffector: CarWrapper) -> None: ...

    # Vector BallWrapper::GetTrajectoryStartVelocity() [member function]
    def GetTrajectoryStartVelocity(self) -> Vector: ...

    # Rotator BallWrapper::GetTrajectoryStartRotation() [member function]
    def GetTrajectoryStartRotation(self) -> Rotator: ...

    # Vector BallWrapper::GetTrajectoryStartLocation() [member function]
    def GetTrajectoryStartLocation(self) -> Vector: ...

    # bool BallWrapper::ShouldDrawTrajectory() [member function]
    def ShouldDrawTrajectory(self) -> bool: ...

    # float BallWrapper::GetAdditionalCarBounceScaleZ(CarWrapper Car) [member function]
    def GetAdditionalCarBounceScaleZ(self, Car: CarWrapper) -> float: ...

    # void BallWrapper::SetEndOfGameHidden() [member function]
    def SetEndOfGameHidden(self) -> None: ...

    # void BallWrapper::Explode(GoalWrapper ExplosionGoal, Vector & ExplodeLocation, PriWrapper Scorer) [member function]
    def Explode(self, ExplosionGoal: GoalWrapper, ExplodeLocation: Vector, Scorer: PriWrapper) -> None: ...

    # void BallWrapper::DoDestroy() [member function]
    def DoDestroy(self) -> None: ...

    # void BallWrapper::DoExplode() [member function]
    def DoExplode(self) -> None: ...

    # void BallWrapper::Launch(Vector & LaunchPosition, Vector & LaunchDirection) [member function]
    def Launch(self, LaunchPosition: Vector, LaunchDirection: Vector) -> None: ...

    # void BallWrapper::OnCarTouch(CarWrapper HitCar, unsigned char HitType) [member function]
    def OnCarTouch(self, HitCar: CarWrapper, HitType: int) -> None: ...

    # void BallWrapper::RecordCarHit(CarWrapper HitCar, Vector & HitLocation, Vector & HitNormal, unsigned char HitType) [member function]
    def RecordCarHit(self, HitCar: CarWrapper, HitLocation: Vector, HitNormal: Vector, HitType: int) -> None: ...

    # bool BallWrapper::IsGroundHit(Vector & HitNormal) [member function]
    def IsGroundHit(self, HitNormal: Vector) -> bool: ...

    # void BallWrapper::FellOutOfWorld() [member function]
    def FellOutOfWorld(self) -> None: ...

    # bool BallWrapper::IsRoundActive() [member function]
    def IsRoundActive(self) -> bool: ...

    # void BallWrapper::eventOnHitGoal(GoalWrapper Goal, Vector & HitLoc) [member function]
    def eventOnHitGoal(self, Goal: GoalWrapper, HitLoc: Vector) -> None: ...

    # void BallWrapper::TurnOff() [member function]
    def TurnOff(self) -> None: ...

    # void BallWrapper::InitAk() [member function]
    def InitAk(self) -> None: ...

    # void BallWrapper::SetWorldBounceScale(float NewScale) [member function]
    def SetWorldBounceScale(self, NewScale: float) -> None: ...

    # void BallWrapper::SetCarBounceScale(float NewScale) [member function]
    def SetCarBounceScale(self, NewScale: float) -> None: ...

    # void BallWrapper::SetBallMaxLinearSpeedScale(float InMaxLinearSpeedScale) [member function]
    def SetBallMaxLinearSpeedScale(self, InMaxLinearSpeedScale: float) -> None: ...

    # void BallWrapper::SetBallGravityScale(float InBallGravityScale) [member function]
    def SetBallGravityScale(self, InBallGravityScale: float) -> None: ...

    # void BallWrapper::SetBallScale(float NewScale) [member function]
    def SetBallScale(self, NewScale: float) -> None: ...

    # void BallWrapper::EventHitGoal(BallWrapper Ball, GoalWrapper Goal) [member function]
    def EventHitGoal(self, Ball: BallWrapper, Goal: GoalWrapper) -> None: ...

    # Private:
    # BallWrapper::Impl [class declaration]

    # BallWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...

