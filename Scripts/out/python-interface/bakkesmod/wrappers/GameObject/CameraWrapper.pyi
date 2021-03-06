from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class CameraWrapper():
    # Public:
    # CameraWrapper::CameraWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # CameraWrapper::CameraWrapper(CameraWrapper const & other) [constructor]

    # CameraWrapper & CameraWrapper::operator=(CameraWrapper rhs) [member operator]

    # CameraWrapper::~CameraWrapper() [destructor]
    def __del__(self) -> None: ...

    # Vector CameraWrapper::GetLocation() [member function]
    def GetLocation(self) -> Vector: ...

    # void CameraWrapper::SetLocation(Vector location) [member function]
    def SetLocation(self, location: Vector) -> None: ...

    # Rotator CameraWrapper::GetRotation() [member function]
    def GetRotation(self) -> Rotator: ...

    # void CameraWrapper::SetRotation(Rotator rotation) [member function]
    def SetRotation(self, rotation: Rotator) -> None: ...

    # ProfileCameraSettings CameraWrapper::GetCameraSettings() [member function]
    def GetCameraSettings(self) -> ProfileCameraSettings: ...

    # void CameraWrapper::SetCameraSettings(ProfileCameraSettings settings) [member function]
    def SetCameraSettings(self, settings: ProfileCameraSettings) -> None: ...

    # bool CameraWrapper::IsCameraShakeOn() [member function]
    def IsCameraShakeOn(self) -> bool: ...

    # POV CameraWrapper::GetPOV() [member function]
    def GetPOV(self) -> POV: ...

    # void CameraWrapper::SetPOV(POV pov) [member function]
    def SetPOV(self, pov: POV) -> None: ...

    # void CameraWrapper::SetFOV(float fov) [member function]
    def SetFOV(self, fov: float) -> None: ...

    # float CameraWrapper::GetFOV() [member function]
    def GetFOV(self) -> float: ...

    # void CameraWrapper::SetLockedFOV(bool lock) [member function]
    def SetLockedFOV(self, lock: bool) -> None: ...

    # ActorWrapper CameraWrapper::GetCameraAsActor() [member function]
    def GetCameraAsActor(self) -> ActorWrapper: ...

    # std::string CameraWrapper::GetCameraState() [member function]
    def GetCameraState(self) -> str: ...

    # void CameraWrapper::SetCameraState(std::string stateName) [member function]
    def SetCameraState(self, stateName: str) -> None: ...

    # Vector CameraWrapper::linterp(Vector start, Vector end, float elapsed, float speed) [member function]
    def linterp(self, start: Vector, end: Vector, elapsed: float, speed: float) -> Vector: ...

    # std::string CameraWrapper::GetFocusActor() [member function]
    def GetFocusActor(self) -> str: ...

    # bool CameraWrapper::SetFocusActor(std::string actorName) [member function]
    def SetFocusActor(self, actorName: str) -> bool: ...

    # bool CameraWrapper::SetFlyCamBallTargetMode() [member function]
    def SetFlyCamBallTargetMode(self) -> bool: ...

    # float CameraWrapper::GetSwivelFastSpeed() [member function]
    def GetSwivelFastSpeed(self) -> float: ...

    # void CameraWrapper::SetSwivelFastSpeed(float newSwivelFastSpeed) [member function]
    def SetSwivelFastSpeed(self, newSwivelFastSpeed: float) -> None: ...

    # float CameraWrapper::GetSwivelDieRate() [member function]
    def GetSwivelDieRate(self) -> float: ...

    # void CameraWrapper::SetSwivelDieRate(float newSwivelDieRate) [member function]
    def SetSwivelDieRate(self, newSwivelDieRate: float) -> None: ...

    # StructArrayWrapper<ProfileCameraSettings> CameraWrapper::GetCameraPresetSettings() [member function]
    def GetCameraPresetSettings(self) -> StructArrayWrapper_ProfileCameraSettings: ...

    # float CameraWrapper::GetHorizontalSplitscreenHeightOffset() [member function]
    def GetHorizontalSplitscreenHeightOffset(self) -> float: ...

    # void CameraWrapper::SetHorizontalSplitscreenHeightOffset(float newHorizontalSplitscreenHeightOffset) [member function]
    def SetHorizontalSplitscreenHeightOffset(self, newHorizontalSplitscreenHeightOffset: float) -> None: ...

    # float CameraWrapper::GetHorizontalSplitscreenFOVOffset() [member function]
    def GetHorizontalSplitscreenFOVOffset(self) -> float: ...

    # void CameraWrapper::SetHorizontalSplitscreenFOVOffset(float newHorizontalSplitscreenFOVOffset) [member function]
    def SetHorizontalSplitscreenFOVOffset(self, newHorizontalSplitscreenFOVOffset: float) -> None: ...

    # float CameraWrapper::GetVerticalSplitscreenFOVOffset() [member function]
    def GetVerticalSplitscreenFOVOffset(self) -> float: ...

    # void CameraWrapper::SetVerticalSplitscreenFOVOffset(float newVerticalSplitscreenFOVOffset) [member function]
    def SetVerticalSplitscreenFOVOffset(self, newVerticalSplitscreenFOVOffset: float) -> None: ...

    # float CameraWrapper::GetClipRate() [member function]
    def GetClipRate(self) -> float: ...

    # void CameraWrapper::SetClipRate(float newClipRate) [member function]
    def SetClipRate(self, newClipRate: float) -> None: ...

    # Rotator CameraWrapper::GetCurrentSwivel() [member function]
    def GetCurrentSwivel(self) -> Rotator: ...

    # void CameraWrapper::SetCurrentSwivel(Rotator newCurrentSwivel) [member function]
    def SetCurrentSwivel(self, newCurrentSwivel: Rotator) -> None: ...

    # RBActorWrapper CameraWrapper::GetDemolisher() [member function]
    def GetDemolisher(self) -> RBActorWrapper: ...

    # void CameraWrapper::SetDemolisher(RBActorWrapper newDemolisher) [member function]
    def SetDemolisher(self, newDemolisher: RBActorWrapper) -> None: ...

    # long unsigned int CameraWrapper::GetbDemolished() [member function]
    def GetbDemolished(self) -> bool: ...

    # void CameraWrapper::SetbDemolished(long unsigned int newbDemolished) [member function]
    def SetbDemolished(self, newbDemolished: bool) -> None: ...

    # float CameraWrapper::ClipToField(float CameraLocationZ) [member function]
    def ClipToField(self, CameraLocationZ: float) -> float: ...

    # void CameraWrapper::Demolished2(RBActorWrapper InDemolisher) [member function]
    def Demolished2(self, InDemolisher: RBActorWrapper) -> None: ...

    # Rotator CameraWrapper::GetDesiredSwivel(float LookUp, float LookRight) [member function]
    def GetDesiredSwivel(self, LookUp: float, LookRight: float) -> Rotator: ...

    # void CameraWrapper::UpdateSwivel(float DeltaTime) [member function]
    def UpdateSwivel(self, DeltaTime: float) -> None: ...

    # float CameraWrapper::GetDefaultFOVOffset() [member function]
    def GetDefaultFOVOffset(self) -> float: ...

    # float CameraWrapper::GetDefaultViewHeightOffset() [member function]
    def GetDefaultViewHeightOffset(self) -> float: ...

    # void CameraWrapper::UpdateFOV() [member function]
    def UpdateFOV(self) -> None: ...

    # void CameraWrapper::EventCameraTargetChanged(CameraWrapper Camera, ActorWrapper Target) [member function]
    def EventCameraTargetChanged(self, Camera: CameraWrapper, Target: ActorWrapper) -> None: ...

    # Private:
    # CameraWrapper::Impl [class declaration]

    # CameraWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


