from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class FXActorWrapper():
    # Public:
    # FXActorWrapper::FXActorWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # FXActorWrapper::FXActorWrapper(FXActorWrapper const & other) [constructor]

    # FXActorWrapper & FXActorWrapper::operator=(FXActorWrapper rhs) [member operator]

    # FXActorWrapper::~FXActorWrapper() [destructor]
    def __del__(self) -> None: ...

    # long unsigned int FXActorWrapper::GetbDeactivateWhenOwnerDestroyed() [member function]
    def GetbDeactivateWhenOwnerDestroyed(self) -> bool: ...

    # void FXActorWrapper::SetbDeactivateWhenOwnerDestroyed(long unsigned int newbDeactivateWhenOwnerDestroyed) [member function]
    def SetbDeactivateWhenOwnerDestroyed(self, newbDeactivateWhenOwnerDestroyed: bool) -> None: ...

    # long unsigned int FXActorWrapper::GetbAllowShadowCasting() [member function]
    def GetbAllowShadowCasting(self) -> bool: ...

    # void FXActorWrapper::SetbAllowShadowCasting(long unsigned int newbAllowShadowCasting) [member function]
    def SetbAllowShadowCasting(self, newbAllowShadowCasting: bool) -> None: ...

    # long unsigned int FXActorWrapper::GetbAutoActivate() [member function]
    def GetbAutoActivate(self) -> bool: ...

    # void FXActorWrapper::SetbAutoActivate(long unsigned int newbAutoActivate) [member function]
    def SetbAutoActivate(self, newbAutoActivate: bool) -> None: ...

    # long unsigned int FXActorWrapper::GetbRenderInactive() [member function]
    def GetbRenderInactive(self) -> bool: ...

    # void FXActorWrapper::SetbRenderInactive(long unsigned int newbRenderInactive) [member function]
    def SetbRenderInactive(self, newbRenderInactive: bool) -> None: ...

    # long unsigned int FXActorWrapper::GetbActive() [member function]
    def GetbActive(self) -> bool: ...

    # void FXActorWrapper::SetbActive(long unsigned int newbActive) [member function]
    def SetbActive(self, newbActive: bool) -> None: ...

    # long unsigned int FXActorWrapper::GetbHadOwner() [member function]
    def GetbHadOwner(self) -> bool: ...

    # void FXActorWrapper::SetbHadOwner(long unsigned int newbHadOwner) [member function]
    def SetbHadOwner(self, newbHadOwner: bool) -> None: ...

    # FXActorWrapper FXActorWrapper::GetParent() [member function]
    def GetParent(self) -> FXActorWrapper: ...

    # void FXActorWrapper::SetParent(FXActorWrapper newParent) [member function]
    def SetParent(self, newParent: FXActorWrapper) -> None: ...

    # ActorWrapper FXActorWrapper::GetAttachmentActor() [member function]
    def GetAttachmentActor(self) -> ActorWrapper: ...

    # void FXActorWrapper::SetAttachmentActor(ActorWrapper newAttachmentActor) [member function]
    def SetAttachmentActor(self, newAttachmentActor: ActorWrapper) -> None: ...

    # float FXActorWrapper::GetDestroyWaitTime() [member function]
    def GetDestroyWaitTime(self) -> float: ...

    # void FXActorWrapper::SetDestroyWaitTime(float newDestroyWaitTime) [member function]
    def SetDestroyWaitTime(self, newDestroyWaitTime: float) -> None: ...

    # float FXActorWrapper::GetDestroyTime() [member function]
    def GetDestroyTime(self) -> float: ...

    # void FXActorWrapper::SetDestroyTime(float newDestroyTime) [member function]
    def SetDestroyTime(self, newDestroyTime: float) -> None: ...

    # int FXActorWrapper::GetEditID() [member function]
    def GetEditID(self) -> int: ...

    # void FXActorWrapper::SetEditID(int newEditID) [member function]
    def SetEditID(self, newEditID: int) -> None: ...

    # void FXActorWrapper::eventDumpDebugInfo() [member function]
    def eventDumpDebugInfo(self) -> None: ...

    # void FXActorWrapper::eventDestroyed() [member function]
    def eventDestroyed(self) -> None: ...

    # void FXActorWrapper::Inherit(FXActorWrapper Other) [member function]
    def Inherit(self, Other: FXActorWrapper) -> None: ...

    # void FXActorWrapper::ResetParticles() [member function]
    def ResetParticles(self) -> None: ...

    # void FXActorWrapper::StopAllEffects() [member function]
    def StopAllEffects(self) -> None: ...

    # void FXActorWrapper::eventDeactivateAndDestroy() [member function]
    def eventDeactivateAndDestroy(self) -> None: ...

    # void FXActorWrapper::UpdateFXStates() [member function]
    def UpdateFXStates(self) -> None: ...

    # bool FXActorWrapper::IsLocallyControlled() [member function]
    def IsLocallyControlled(self) -> bool: ...

    # void FXActorWrapper::Deactivate2() [member function]
    def Deactivate2(self) -> None: ...

    # void FXActorWrapper::Activate2() [member function]
    def Activate2(self) -> None: ...

    # void FXActorWrapper::BindTo(FXActorWrapper ParentFXActor) [member function]
    def BindTo(self, ParentFXActor: FXActorWrapper) -> None: ...

    # void FXActorWrapper::SetAttachmentActor2(ActorWrapper AttachToActor) [member function]
    def SetAttachmentActor2(self, AttachToActor: ActorWrapper) -> None: ...

    # void FXActorWrapper::PostBeginPlay() [member function]
    def PostBeginPlay(self) -> None: ...

    # Private:
    # FXActorWrapper::Impl [class declaration]

    # FXActorWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


