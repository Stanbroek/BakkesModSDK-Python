from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class CarWrapper():
    # Public:
    # CarWrapper::CarWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # CarWrapper::CarWrapper(CarWrapper const & other) [constructor]

    # CarWrapper & CarWrapper::operator=(CarWrapper rhs) [member operator]

    # CarWrapper::~CarWrapper() [destructor]
    def __del__(self) -> None: ...

    # bool CarWrapper::IsBoostCheap() [member function]
    def IsBoostCheap(self) -> bool: ...

    # void CarWrapper::SetBoostCheap(bool b) [member function]
    def SetBoostCheap(self, b: bool) -> None: ...

    # void CarWrapper::SetCarRotation(Rotator rotation) [member function]
    def SetCarRotation(self, rotation: Rotator) -> None: ...

    # void CarWrapper::ForceBoost(bool force) [member function]
    def ForceBoost(self, force: bool) -> None: ...

    # std::string CarWrapper::GetOwnerName() [member function]
    def GetOwnerName(self) -> str: ...

    # void CarWrapper::Unfreeze() [member function]
    def Unfreeze(self) -> None: ...

    # ControllerInput CarWrapper::GetInput() [member function]
    def GetInput(self) -> ControllerInput: ...

    # void CarWrapper::SetInput(ControllerInput input) [member function]
    def SetInput(self, input: ControllerInput) -> None: ...

    # void CarWrapper::Destroy() [member function]
    def Destroy(self) -> None: ...

    # void CarWrapper::Demolish() [member function]
    def Demolish(self) -> None: ...

    # long unsigned int CarWrapper::HasFlip() [member function]
    def HasFlip(self) -> bool: ...

    # int CarWrapper::GetLoadoutBody() [member function]
    def GetLoadoutBody(self) -> int: ...

    # ArrayWrapper<CarComponentWrapper> CarWrapper::GetDefaultCarComponents() [member function]
    def GetDefaultCarComponents(self) -> ArrayWrapper_CarComponentWrapper: ...

    # FlipCarComponentWrapper CarWrapper::GetFlipComponent() [member function]
    def GetFlipComponent(self) -> FlipCarComponentWrapper: ...

    # unsigned char CarWrapper::GetDemolishTarget() [member function]
    def GetDemolishTarget(self) -> int: ...

    # void CarWrapper::SetDemolishTarget(unsigned char newDemolishTarget) [member function]
    def SetDemolishTarget(self, newDemolishTarget: int) -> None: ...

    # unsigned char CarWrapper::GetDemolishSpeed() [member function]
    def GetDemolishSpeed(self) -> int: ...

    # void CarWrapper::SetDemolishSpeed(unsigned char newDemolishSpeed) [member function]
    def SetDemolishSpeed(self, newDemolishSpeed: int) -> None: ...

    # long unsigned int CarWrapper::GetbLoadoutSet() [member function]
    def GetbLoadoutSet(self) -> bool: ...

    # void CarWrapper::SetbLoadoutSet(long unsigned int newbLoadoutSet) [member function]
    def SetbLoadoutSet(self, newbLoadoutSet: bool) -> None: ...

    # long unsigned int CarWrapper::GetbDemolishOnOpposingGround() [member function]
    def GetbDemolishOnOpposingGround(self) -> bool: ...

    # void CarWrapper::SetbDemolishOnOpposingGround(long unsigned int newbDemolishOnOpposingGround) [member function]
    def SetbDemolishOnOpposingGround(self, newbDemolishOnOpposingGround: bool) -> None: ...

    # long unsigned int CarWrapper::GetbWasOnOpposingGround() [member function]
    def GetbWasOnOpposingGround(self) -> bool: ...

    # void CarWrapper::SetbWasOnOpposingGround(long unsigned int newbWasOnOpposingGround) [member function]
    def SetbWasOnOpposingGround(self, newbWasOnOpposingGround: bool) -> None: ...

    # long unsigned int CarWrapper::GetbDemolishOnGoalZone() [member function]
    def GetbDemolishOnGoalZone(self) -> bool: ...

    # void CarWrapper::SetbDemolishOnGoalZone(long unsigned int newbDemolishOnGoalZone) [member function]
    def SetbDemolishOnGoalZone(self, newbDemolishOnGoalZone: bool) -> None: ...

    # long unsigned int CarWrapper::GetbWasInGoalZone() [member function]
    def GetbWasInGoalZone(self) -> bool: ...

    # void CarWrapper::SetbWasInGoalZone(long unsigned int newbWasInGoalZone) [member function]
    def SetbWasInGoalZone(self, newbWasInGoalZone: bool) -> None: ...

    # long unsigned int CarWrapper::GetbOverrideHandbrakeOn() [member function]
    def GetbOverrideHandbrakeOn(self) -> bool: ...

    # void CarWrapper::SetbOverrideHandbrakeOn(long unsigned int newbOverrideHandbrakeOn) [member function]
    def SetbOverrideHandbrakeOn(self, newbOverrideHandbrakeOn: bool) -> None: ...

    # long unsigned int CarWrapper::GetbCollidesWithVehicles() [member function]
    def GetbCollidesWithVehicles(self) -> bool: ...

    # void CarWrapper::SetbCollidesWithVehicles(long unsigned int newbCollidesWithVehicles) [member function]
    def SetbCollidesWithVehicles(self, newbCollidesWithVehicles: bool) -> None: ...

    # long unsigned int CarWrapper::GetbOverrideBoostOn() [member function]
    def GetbOverrideBoostOn(self) -> bool: ...

    # void CarWrapper::SetbOverrideBoostOn(long unsigned int newbOverrideBoostOn) [member function]
    def SetbOverrideBoostOn(self, newbOverrideBoostOn: bool) -> None: ...

    # FXActorWrapper CarWrapper::GetExitFXArchetype() [member function]
    def GetExitFXArchetype(self) -> FXActorWrapper: ...

    # void CarWrapper::SetExitFXArchetype(FXActorWrapper newExitFXArchetype) [member function]
    def SetExitFXArchetype(self, newExitFXArchetype: FXActorWrapper) -> None: ...

    # float CarWrapper::GetMaxTimeForDodge() [member function]
    def GetMaxTimeForDodge(self) -> float: ...

    # void CarWrapper::SetMaxTimeForDodge(float newMaxTimeForDodge) [member function]
    def SetMaxTimeForDodge(self, newMaxTimeForDodge: float) -> None: ...

    # float CarWrapper::GetLastWheelsHitBallTime() [member function]
    def GetLastWheelsHitBallTime(self) -> float: ...

    # void CarWrapper::SetLastWheelsHitBallTime(float newLastWheelsHitBallTime) [member function]
    def SetLastWheelsHitBallTime(self, newLastWheelsHitBallTime: float) -> None: ...

    # float CarWrapper::GetReplicatedCarScale() [member function]
    def GetReplicatedCarScale(self) -> float: ...

    # void CarWrapper::SetReplicatedCarScale(float newReplicatedCarScale) [member function]
    def SetReplicatedCarScale(self, newReplicatedCarScale: float) -> None: ...

    # FXActorWrapper CarWrapper::GetBodyFXActor() [member function]
    def GetBodyFXActor(self) -> FXActorWrapper: ...

    # void CarWrapper::SetBodyFXActor(FXActorWrapper newBodyFXActor) [member function]
    def SetBodyFXActor(self, newBodyFXActor: FXActorWrapper) -> None: ...

    # PriWrapper CarWrapper::GetAttackerPRI() [member function]
    def GetAttackerPRI(self) -> PriWrapper: ...

    # void CarWrapper::SetAttackerPRI(PriWrapper newAttackerPRI) [member function]
    def SetAttackerPRI(self, newAttackerPRI: PriWrapper) -> None: ...

    # Vector CarWrapper::GetMouseAccel() [member function]
    def GetMouseAccel(self) -> Vector: ...

    # void CarWrapper::SetMouseAccel(Vector newMouseAccel) [member function]
    def SetMouseAccel(self, newMouseAccel: Vector) -> None: ...

    # Vector CarWrapper::GetMouseAirAccel() [member function]
    def GetMouseAirAccel(self) -> Vector: ...

    # void CarWrapper::SetMouseAirAccel(Vector newMouseAirAccel) [member function]
    def SetMouseAirAccel(self, newMouseAirAccel: Vector) -> None: ...

    # RumblePickupComponentWrapper CarWrapper::GetAttachedPickup() [member function]
    def GetAttachedPickup(self) -> RumblePickupComponentWrapper: ...

    # void CarWrapper::SetAttachedPickup(RumblePickupComponentWrapper newAttachedPickup) [member function]
    def SetAttachedPickup(self, newAttachedPickup: RumblePickupComponentWrapper) -> None: ...

    # Vector CarWrapper::GetReplayFocusOffset() [member function]
    def GetReplayFocusOffset(self) -> Vector: ...

    # void CarWrapper::SetReplayFocusOffset(Vector newReplayFocusOffset) [member function]
    def SetReplayFocusOffset(self, newReplayFocusOffset: Vector) -> None: ...

    # float CarWrapper::GetAddedBallForceMultiplier() [member function]
    def GetAddedBallForceMultiplier(self) -> float: ...

    # void CarWrapper::SetAddedBallForceMultiplier(float newAddedBallForceMultiplier) [member function]
    def SetAddedBallForceMultiplier(self, newAddedBallForceMultiplier: float) -> None: ...

    # float CarWrapper::GetAddedCarForceMultiplier() [member function]
    def GetAddedCarForceMultiplier(self) -> float: ...

    # void CarWrapper::SetAddedCarForceMultiplier(float newAddedCarForceMultiplier) [member function]
    def SetAddedCarForceMultiplier(self, newAddedCarForceMultiplier: float) -> None: ...

    # GameEventWrapper CarWrapper::GetGameEvent() [member function]
    def GetGameEvent(self) -> GameEventWrapper: ...

    # void CarWrapper::SetGameEvent(GameEventWrapper newGameEvent) [member function]
    def SetGameEvent(self, newGameEvent: GameEventWrapper) -> None: ...

    # float CarWrapper::GetMaxDriveBackwardsSpeed() [member function]
    def GetMaxDriveBackwardsSpeed(self) -> float: ...

    # float CarWrapper::GetMaxDriveForwardSpeed() [member function]
    def GetMaxDriveForwardSpeed(self) -> float: ...

    # Vector CarWrapper::GetReplayFocusLocation() [member function]
    def GetReplayFocusLocation(self) -> Vector: ...

    # void CarWrapper::OnPickupChanged(RumblePickupComponentWrapper InPickup) [member function]
    def OnPickupChanged(self, InPickup: RumblePickupComponentWrapper) -> None: ...

    # void CarWrapper::SetAttachedPickup2(RumblePickupComponentWrapper InPickup) [member function]
    def SetAttachedPickup2(self, InPickup: RumblePickupComponentWrapper) -> None: ...

    # void CarWrapper::EnablePodiumMode() [member function]
    def EnablePodiumMode(self) -> None: ...

    # void CarWrapper::CopyPushFactorCurve() [member function]
    def CopyPushFactorCurve(self) -> None: ...

    # void CarWrapper::ClearAttacker() [member function]
    def ClearAttacker(self) -> None: ...

    # void CarWrapper::NotifyNewAttacker(PriWrapper Attacker) [member function]
    def NotifyNewAttacker(self, Attacker: PriWrapper) -> None: ...

    # void CarWrapper::UpdateBallIndicator() [member function]
    def UpdateBallIndicator(self) -> None: ...

    # void CarWrapper::eventOnSuperSonicChanged() [member function]
    def eventOnSuperSonicChanged(self) -> None: ...

    # void CarWrapper::eventOnGroundChanged() [member function]
    def eventOnGroundChanged(self) -> None: ...

    # void CarWrapper::FellOutOfWorld() [member function]
    def FellOutOfWorld(self) -> None: ...

    # void CarWrapper::DemolishDestroyTimer() [member function]
    def DemolishDestroyTimer(self) -> None: ...

    # void CarWrapper::Demolish2(RBActorWrapper Demolisher) [member function]
    def Demolish2(self, Demolisher: RBActorWrapper) -> None: ...

    # bool CarWrapper::Teleport(Vector & SpawnLocation, Rotator & SpawnRotation, long unsigned int bStopVelocity, long unsigned int bUpdateRotation, float ExtraForce) [member function]
    def Teleport(self, SpawnLocation: Vector, SpawnRotation: Rotator, bStopVelocity: bool, bUpdateRotation: bool, ExtraForce: float) -> bool: ...

    # void CarWrapper::OnJumpReleased() [member function]
    def OnJumpReleased(self) -> None: ...

    # void CarWrapper::OnJumpPressed() [member function]
    def OnJumpPressed(self) -> None: ...

    # void CarWrapper::eventSetVehicleInput(ControllerInput & NewInput) [member function]
    def eventSetVehicleInput(self, NewInput: ControllerInput) -> None: ...

    # bool CarWrapper::CanDemolish(CarWrapper HitCar) [member function]
    def CanDemolish(self, HitCar: CarWrapper) -> bool: ...

    # bool CarWrapper::ShouldDemolish(CarWrapper HitCar, Vector & HitLocation, Vector & HitNormal, unsigned char * Result) [member function]
    def ShouldDemolish(self, HitCar: CarWrapper, HitLocation: Vector, HitNormal: Vector, Result: str) -> bool: ...

    # unsigned char CarWrapper::ApplyCarImpactForces(CarWrapper OtherCar, Vector & HitLocation, Vector & HitNormal) [member function]
    def ApplyCarImpactForces(self, OtherCar: CarWrapper, HitLocation: Vector, HitNormal: Vector) -> int: ...

    # bool CarWrapper::IsBumperHit(CarWrapper OtherCar) [member function]
    def IsBumperHit(self, OtherCar: CarWrapper) -> bool: ...

    # void CarWrapper::ApplyBallImpactForces(BallWrapper Ball, Vector & HitLocation) [member function]
    def ApplyBallImpactForces(self, Ball: BallWrapper, HitLocation: Vector) -> None: ...

    # bool CarWrapper::IsDodging() [member function]
    def IsDodging(self) -> bool: ...

    # void CarWrapper::OnHitBall(BallWrapper Ball, Vector & HitLocation, Vector & HitNormal) [member function]
    def OnHitBall(self, Ball: BallWrapper, HitLocation: Vector, HitNormal: Vector) -> None: ...

    # bool CarWrapper::AnyWheelTouchingGround() [member function]
    def AnyWheelTouchingGround(self) -> bool: ...

    # CarComponentWrapper CarWrapper::GiveCarComponent(CarComponentWrapper ComponentArchetype, PriWrapper Activator) [member function]
    def GiveCarComponent(self, ComponentArchetype: CarComponentWrapper, Activator: PriWrapper) -> CarComponentWrapper: ...

    # void CarWrapper::AddDefaultCarComponents() [member function]
    def AddDefaultCarComponents(self) -> None: ...

    # void CarWrapper::DetachPrimitiveComponent(PrimitiveComponentWrapper Component) [member function]
    def DetachPrimitiveComponent(self, Component: PrimitiveComponentWrapper) -> None: ...

    # void CarWrapper::HandleWheelBallHit(WheelWrapper Wheel) [member function]
    def HandleWheelBallHit(self, Wheel: WheelWrapper) -> None: ...

    # void CarWrapper::RespawnInPlace() [member function]
    def RespawnInPlace(self) -> None: ...

    # void CarWrapper::SetCarScale(float NewScale) [member function]
    def SetCarScale(self, NewScale: float) -> None: ...

    # void CarWrapper::OnClubColorsChanged() [member function]
    def OnClubColorsChanged(self) -> None: ...

    # void CarWrapper::HandleTeamChanged(PriXWrapper MyPRI) [member function]
    def HandleTeamChanged(self, MyPRI: PriXWrapper) -> None: ...

    # bool CarWrapper::UpdateTeamLoadout() [member function]
    def UpdateTeamLoadout(self) -> bool: ...

    # void CarWrapper::InitTeamPaint() [member function]
    def InitTeamPaint(self) -> None: ...

    # int CarWrapper::GetLoadoutTeamIndex() [member function]
    def GetLoadoutTeamIndex(self) -> int: ...

    # int CarWrapper::GetPreviewTeamIndex() [member function]
    def GetPreviewTeamIndex(self) -> int: ...

    # bool CarWrapper::HasTeam() [member function]
    def HasTeam(self) -> bool: ...

    # void CarWrapper::HandleLoadoutSelected(PriWrapper MyPRI) [member function]
    def HandleLoadoutSelected(self, MyPRI: PriWrapper) -> None: ...

    # void CarWrapper::HandleGameEventChanged(PriWrapper MyPRI) [member function]
    def HandleGameEventChanged(self, MyPRI: PriWrapper) -> None: ...

    # void CarWrapper::OnPRIChanged() [member function]
    def OnPRIChanged(self) -> None: ...

    # void CarWrapper::OnControllerChanged() [member function]
    def OnControllerChanged(self) -> None: ...

    # Private:
    # CarWrapper::Impl [class declaration]

    # CarWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


