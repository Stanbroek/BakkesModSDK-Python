// Python BakkesMod pybind11 bindings edits:
//  - removed ClubMember::paddingForReasons, padding array. (ClubDetailsWrapper.cpp)
//  - removed GameWrapper::GetGUIManager, ImGui not supported. (GameWrapper.cpp)
//  - removed GameWrapper::pimpl non copyable. (GameWrapper.cpp)
//  - removed Vector::init<FVector>, incomplete type. (WrapperStructs.cpp)
//  - removed Rotator::init<FRotator>, incomplete type. (WrapperStructs.cpp)
//  - removed first CVarManagerWrapper::registerNotifier function, typedefed arg. (CVarManagerWrapper.cpp)
//  - removed all CVarWrapper::bindTo functions, holder classes are only supported for custom types. (cvarwrapper.cpp)
//  - removed all mat4x4 functions, typedef stuff. (linmath.cpp)
//  - exposed export_values. (wrapperstructs.cpp)
//  - edited stuff. (bakkesmodplugin.cpp)
//  - added exception catchers to lambda functions. (CVarManagerWrapper.cpp and GameWrapper.cpp)

// Unresolved external symbols:
//  - ArrayWrapper<BoostPickupWrapper>::*;
//  - GameEventWrapper::GetGameMode(void);
//  - GameEventWrapper::SetGameMode(void);
//  - GameEventWrapper::GetIdleKickTime(void);
//  - GameEventWrapper::SetIdleKickTime(float);
//  - GameEventWrapper::GetIdleKickWarningTime(void);
//  - GameEventWrapper::SetIdleKickWarningTime(float);
//  - GameEventWrapper::KickSplitscreenIdlers(void);
//  - GameEventWrapper::KickIdlers(void);
//  - GameEventWrapper::StopIdleKickTimer(void);
//  - GameEventWrapper::StartIdleKickTimer(float);
//  - ServerWrapper::GetLastTrialTime(void);
//  - ServerWrapper::SetLastTrialTime(int);
//  - ServerWrapper::GetbKickOnTrialEnd(void);
//  - ServerWrapper::SetbKickOnTrialEnd(unsigned long);
//  - ServerWrapper::GetKickIdleReplayOffset(void);
//  - ServerWrapper::SetKickIdleReplayOffset(float);
//  - ServerWrapper::WaitForBallOnGround(void);
//  - ServerWrapper::BallHitGround(struct Vector&);
//  - ServerWrapper::HandleBallHitGround(class BallWrapper, struct Vector&, struct Vector&);
//  - ServerWrapper::HandleBallHitGroundTimeout(void);
//  - BoostWrapper::GetbUnlimitedBoost(void);
//  - BoostWrapper::SetbUnlimitedBoost(unsigned long);
//  - PriWrapper::GetbDeveloper(void);
//  - PriWrapper::SetbDeveloper(unsigned long);
//  - PriWrapper::GetbPlayedWithGamepad(void);
//  - PriWrapper::SetbPlayedWithGamepad(unsigned long);
//  - PriWrapper::GetTotalXP(void);
//  - PriWrapper::SetTotalXP(int);
//  - PriWrapper::GetXpLevel(void);
//  - PriWrapper::SetXpLevel(int);
//  - PriWrapper::SetXPInfo(int, int);
//  - PriWrapper::SetTotalXP2(int);
//  - BasketballPickup::*;
//  - GravityPickup::HandleHitBall(class CarWrapper, class BallWrapper);
//  - VelcroPickup::HandleHitBall(class CarWrapper, class BallWrapper);
//  - PlayerControllerWrapper::GetbPendingIdleKick(void);
//  - PlayerControllerWrapper::SetbPendingIdleKick(unsigned long);
//  - PlayerControllerWrapper::OnPendingIdleKickChanged(void);
//  - PlayerControllerWrapper::SetPendingIdleKick(unsigned long);
//  - PlayerControllerWrapper::KickTrialPlayer(void);
//  - PlayerControllerWrapper::RemoveChatBan(void);
//  - PlayerControllerWrapper::ApplyChatBan(unsigned __int64);
//  - PlayerControllerWrapper::EventPendingIdleKickChanged(class PlayerControllerWrapper);

#include "bindings.h"


PYBIND11_EMBEDDED_MODULE(bakkesmod, m) {
    bind_bakkesmod(m);

    // Globals
    m.attr("cvarManager") = pybind11::none();
    m.attr("gameWrapper") = pybind11::none();

    m.attr("__author__") = "Stanbroek";
    m.attr("__version__") = STRINGIZE(PLUGIN_VERSION);
}
