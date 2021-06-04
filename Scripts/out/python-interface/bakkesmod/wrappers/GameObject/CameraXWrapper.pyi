from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class CameraXWrapper():
    # Public:
    # CameraXWrapper::CameraXWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # CameraXWrapper::CameraXWrapper(CameraXWrapper const & other) [constructor]

    # CameraXWrapper & CameraXWrapper::operator=(CameraXWrapper rhs) [member operator]

    # CameraXWrapper::~CameraXWrapper() [destructor]
    def __del__(self) -> None: ...

    # Rotator CameraXWrapper::GetPCDeltaRotation() [member function]
    def GetPCDeltaRotation(self) -> Rotator: ...

    # void CameraXWrapper::SetPCDeltaRotation(Rotator newPCDeltaRotation) [member function]
    def SetPCDeltaRotation(self, newPCDeltaRotation: Rotator) -> None: ...

    # Rotator CameraXWrapper::GetOldControllerRotation() [member function]
    def GetOldControllerRotation(self) -> Rotator: ...

    # void CameraXWrapper::SetOldControllerRotation(Rotator newOldControllerRotation) [member function]
    def SetOldControllerRotation(self, newOldControllerRotation: Rotator) -> None: ...

    # Vector CameraXWrapper::GetPCDeltaLocation() [member function]
    def GetPCDeltaLocation(self) -> Vector: ...

    # void CameraXWrapper::SetPCDeltaLocation(Vector newPCDeltaLocation) [member function]
    def SetPCDeltaLocation(self, newPCDeltaLocation: Vector) -> None: ...

    # Vector CameraXWrapper::GetOldControllerLocation() [member function]
    def GetOldControllerLocation(self) -> Vector: ...

    # void CameraXWrapper::SetOldControllerLocation(Vector newOldControllerLocation) [member function]
    def SetOldControllerLocation(self, newOldControllerLocation: Vector) -> None: ...

    # Vector CameraXWrapper::GetShakeLocationOffset() [member function]
    def GetShakeLocationOffset(self) -> Vector: ...

    # void CameraXWrapper::SetShakeLocationOffset(Vector newShakeLocationOffset) [member function]
    def SetShakeLocationOffset(self, newShakeLocationOffset: Vector) -> None: ...

    # Rotator CameraXWrapper::GetShakeRotationOffset() [member function]
    def GetShakeRotationOffset(self) -> Rotator: ...

    # void CameraXWrapper::SetShakeRotationOffset(Rotator newShakeRotationOffset) [member function]
    def SetShakeRotationOffset(self, newShakeRotationOffset: Rotator) -> None: ...

    # float CameraXWrapper::GetShakeFOVOffset() [member function]
    def GetShakeFOVOffset(self) -> float: ...

    # void CameraXWrapper::SetShakeFOVOffset(float newShakeFOVOffset) [member function]
    def SetShakeFOVOffset(self, newShakeFOVOffset: float) -> None: ...

    # UnrealColor CameraXWrapper::GetStartFadeColor() [member function]
    def GetStartFadeColor(self) -> UnrealColor: ...

    # void CameraXWrapper::SetStartFadeColor(UnrealColor newStartFadeColor) [member function]
    def SetStartFadeColor(self, newStartFadeColor: UnrealColor) -> None: ...

    # UnrealColor CameraXWrapper::GetEndFadeColor() [member function]
    def GetEndFadeColor(self) -> UnrealColor: ...

    # void CameraXWrapper::SetEndFadeColor(UnrealColor newEndFadeColor) [member function]
    def SetEndFadeColor(self, newEndFadeColor: UnrealColor) -> None: ...

    # Vector CameraXWrapper::GetClipOffset() [member function]
    def GetClipOffset(self) -> Vector: ...

    # void CameraXWrapper::SetClipOffset(Vector newClipOffset) [member function]
    def SetClipOffset(self, newClipOffset: Vector) -> None: ...

    # long unsigned int CameraXWrapper::GetbDisableCameraShake() [member function]
    def GetbDisableCameraShake(self) -> bool: ...

    # void CameraXWrapper::SetbDisableCameraShake(long unsigned int newbDisableCameraShake) [member function]
    def SetbDisableCameraShake(self, newbDisableCameraShake: bool) -> None: ...

    # long unsigned int CameraXWrapper::GetbSnapNextTransition() [member function]
    def GetbSnapNextTransition(self) -> bool: ...

    # void CameraXWrapper::SetbSnapNextTransition(long unsigned int newbSnapNextTransition) [member function]
    def SetbSnapNextTransition(self, newbSnapNextTransition: bool) -> None: ...

    # void CameraXWrapper::eventOnViewTargetChanged() [member function]
    def eventOnViewTargetChanged(self) -> None: ...

    # bool CameraXWrapper::IsTransitioning() [member function]
    def IsTransitioning(self) -> bool: ...

    # void CameraXWrapper::SnapTransition() [member function]
    def SnapTransition(self) -> None: ...

    # void CameraXWrapper::CopyFade(CameraXWrapper Other) [member function]
    def CopyFade(self, Other: CameraXWrapper) -> None: ...

    # void CameraXWrapper::UpdateFade(float DeltaTime) [member function]
    def UpdateFade(self, DeltaTime: float) -> None: ...

    # void CameraXWrapper::eventUpdateCamera(float DeltaTime) [member function]
    def eventUpdateCamera(self, DeltaTime: float) -> None: ...

    # Rotator CameraXWrapper::RemoveRoll(Rotator & InRot) [member function]
    def RemoveRoll(self, InRot: Rotator) -> Rotator: ...

    # void CameraXWrapper::UpdateCameraState() [member function]
    def UpdateCameraState(self) -> None: ...

    # void CameraXWrapper::InstanceCameraStates() [member function]
    def InstanceCameraStates(self) -> None: ...

    # void CameraXWrapper::OnLoadingMovieClosesd() [member function]
    def OnLoadingMovieClosesd(self) -> None: ...

    # void CameraXWrapper::eventPostBeginPlay() [member function]
    def eventPostBeginPlay(self) -> None: ...

    # Private:
    # CameraXWrapper::Impl [class declaration]

    # CameraXWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


