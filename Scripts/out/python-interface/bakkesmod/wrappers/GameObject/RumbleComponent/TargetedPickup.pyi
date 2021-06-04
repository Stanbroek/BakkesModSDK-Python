from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class TargetedPickup():
    # Public:
    # TargetedPickup::TargetedPickup(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # TargetedPickup::TargetedPickup(TargetedPickup const & other) [constructor]

    # TargetedPickup & TargetedPickup::operator=(TargetedPickup rhs) [member operator]

    # TargetedPickup::~TargetedPickup() [destructor]
    def __del__(self) -> None: ...

    # long unsigned int TargetedPickup::GetbCanTargetBall() [member function]
    def GetbCanTargetBall(self) -> bool: ...

    # void TargetedPickup::SetbCanTargetBall(long unsigned int newbCanTargetBall) [member function]
    def SetbCanTargetBall(self, newbCanTargetBall: bool) -> None: ...

    # long unsigned int TargetedPickup::GetbCanTargetCars() [member function]
    def GetbCanTargetCars(self) -> bool: ...

    # void TargetedPickup::SetbCanTargetCars(long unsigned int newbCanTargetCars) [member function]
    def SetbCanTargetCars(self, newbCanTargetCars: bool) -> None: ...

    # long unsigned int TargetedPickup::GetbCanTargetEnemyCars() [member function]
    def GetbCanTargetEnemyCars(self) -> bool: ...

    # void TargetedPickup::SetbCanTargetEnemyCars(long unsigned int newbCanTargetEnemyCars) [member function]
    def SetbCanTargetEnemyCars(self, newbCanTargetEnemyCars: bool) -> None: ...

    # long unsigned int TargetedPickup::GetbCanTargetTeamCars() [member function]
    def GetbCanTargetTeamCars(self) -> bool: ...

    # void TargetedPickup::SetbCanTargetTeamCars(long unsigned int newbCanTargetTeamCars) [member function]
    def SetbCanTargetTeamCars(self, newbCanTargetTeamCars: bool) -> None: ...

    # long unsigned int TargetedPickup::GetbUseDirectionalTargeting() [member function]
    def GetbUseDirectionalTargeting(self) -> bool: ...

    # void TargetedPickup::SetbUseDirectionalTargeting(long unsigned int newbUseDirectionalTargeting) [member function]
    def SetbUseDirectionalTargeting(self, newbUseDirectionalTargeting: bool) -> None: ...

    # long unsigned int TargetedPickup::GetbRequireTrace() [member function]
    def GetbRequireTrace(self) -> bool: ...

    # void TargetedPickup::SetbRequireTrace(long unsigned int newbRequireTrace) [member function]
    def SetbRequireTrace(self, newbRequireTrace: bool) -> None: ...

    # float TargetedPickup::GetRange() [member function]
    def GetRange(self) -> float: ...

    # void TargetedPickup::SetRange(float newRange) [member function]
    def SetRange(self, newRange: float) -> None: ...

    # float TargetedPickup::GetDirectionalTargetingAccuracy() [member function]
    def GetDirectionalTargetingAccuracy(self) -> float: ...

    # void TargetedPickup::SetDirectionalTargetingAccuracy(float newDirectionalTargetingAccuracy) [member function]
    def SetDirectionalTargetingAccuracy(self, newDirectionalTargetingAccuracy: float) -> None: ...

    # RBActorWrapper TargetedPickup::GetClientTarget() [member function]
    def GetClientTarget(self) -> RBActorWrapper: ...

    # void TargetedPickup::SetClientTarget(RBActorWrapper newClientTarget) [member function]
    def SetClientTarget(self, newClientTarget: RBActorWrapper) -> None: ...

    # RBActorWrapper TargetedPickup::GetTargeted() [member function]
    def GetTargeted(self) -> RBActorWrapper: ...

    # void TargetedPickup::SetTargeted(RBActorWrapper newTargeted) [member function]
    def SetTargeted(self, newTargeted: RBActorWrapper) -> None: ...

    # RBActorWrapper TargetedPickup::GetClientTarget2() [member function]
    def GetClientTarget2(self) -> RBActorWrapper: ...

    # void TargetedPickup::TargetChanged() [member function]
    def TargetChanged(self) -> None: ...

    # void TargetedPickup::OnTargetChanged() [member function]
    def OnTargetChanged(self) -> None: ...

    # bool TargetedPickup::TryActivate(RBActorWrapper TargetOverride) [member function]
    def TryActivate(self, TargetOverride: RBActorWrapper) -> bool: ...

    # bool TargetedPickup::ValidateTargetTrace(RBActorWrapper InTarget) [member function]
    def ValidateTargetTrace(self, InTarget: RBActorWrapper) -> bool: ...

    # bool TargetedPickup::ValidateTarget2(RBActorWrapper InTarget) [member function]
    def ValidateTarget2(self, InTarget: RBActorWrapper) -> bool: ...

    # RBActorWrapper TargetedPickup::GetTarget2() [member function]
    def GetTarget2(self) -> RBActorWrapper: ...

    # Private:
    # TargetedPickup::Impl [class declaration]

    # TargetedPickup::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


