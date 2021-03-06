from typing import Callable, List, Tuple, Dict, Any
from enum import Enum

class ServerWrapper():
    # Public:
    # ServerWrapper::ServerWrapper(uintptr_t mem) [constructor]
    def __init__(self, mem: int) -> None: ...

    # ServerWrapper::ServerWrapper(ServerWrapper const & other) [constructor]

    # ServerWrapper & ServerWrapper::operator=(ServerWrapper rhs) [member operator]

    # ServerWrapper::~ServerWrapper() [destructor]
    def __del__(self) -> None: ...

    # BallWrapper ServerWrapper::GetBall() [member function]
    def GetBall(self) -> BallWrapper: ...

    # void ServerWrapper::SpawnCar(int carBody, std::string name) [member function]
    def SpawnCar(self, carBody: int, name: str) -> None: ...

    # void ServerWrapper::SpawnBot(int carBody, std::string name) [member function]
    def SpawnBot(self, carBody: int, name: str) -> None: ...

    # BallWrapper ServerWrapper::SpawnBall(Vector const position, bool wake, bool spawnCannon) [member function]
    def SpawnBall(self, position: Vector, wake: bool, spawnCannon: bool) -> BallWrapper: ...

    # bool ServerWrapper::HasAuthority() [member function]
    def HasAuthority(self) -> bool: ...

    # void ServerWrapper::SetGameSpeed(float GameSpeed) [member function]
    def SetGameSpeed(self, GameSpeed: float) -> None: ...

    # float ServerWrapper::GetGameSpeed() [member function]
    def GetGameSpeed(self) -> float: ...

    # void ServerWrapper::SetSecondsElapsed(float SecondsElapsed) [member function]
    def SetSecondsElapsed(self, SecondsElapsed: float) -> None: ...

    # float ServerWrapper::GetSecondsElapsed() [member function]
    def GetSecondsElapsed(self) -> float: ...

    # CarWrapper ServerWrapper::GetGameCar() [member function]
    def GetGameCar(self) -> CarWrapper: ...

    # bool ServerWrapper::IsBallMovingTowardsGoal(int goalNo, BallWrapper bw) [member function]
    def IsBallMovingTowardsGoal(self, goalNo: int, bw: BallWrapper) -> bool: ...

    # bool ServerWrapper::IsInGoal(Vector vec) [member function]
    def IsInGoal(self, vec: Vector) -> bool: ...

    # void ServerWrapper::DisableGoalReset() [member function]
    def DisableGoalReset(self) -> None: ...

    # void ServerWrapper::EnableGoalReset() [member function]
    def EnableGoalReset(self) -> None: ...

    # Vector ServerWrapper::GenerateShot(Vector startPos, Vector destination, float speed) [member function]
    def GenerateShot(self, startPos: Vector, destination: Vector, speed: float) -> Vector: ...

    # Vector ServerWrapper::GenerateGoalAimLocation(int goalNumber, Vector currentBallLocation) [member function]
    def GenerateGoalAimLocation(self, goalNumber: int, currentBallLocation: Vector) -> Vector: ...

    # Vector ServerWrapper::GetGoalExtent(int goalNumber=0) [member function]
    def GetGoalExtent(self, goalNumber: int = 0) -> Vector: ...

    # Vector ServerWrapper::GetGoalLocation(int goalNumber=0) [member function]
    def GetGoalLocation(self, goalNumber: int = 0) -> Vector: ...

    # CarWrapper ServerWrapper::GetTestCarArchetype() [member function]
    def GetTestCarArchetype(self) -> CarWrapper: ...

    # void ServerWrapper::SetTestCarArchetype(CarWrapper newTestCarArchetype) [member function]
    def SetTestCarArchetype(self, newTestCarArchetype: CarWrapper) -> None: ...

    # BallWrapper ServerWrapper::GetBallArchetype() [member function]
    def GetBallArchetype(self) -> BallWrapper: ...

    # void ServerWrapper::SetBallArchetype(BallWrapper newBallArchetype) [member function]
    def SetBallArchetype(self, newBallArchetype: BallWrapper) -> None: ...

    # ActorWrapper ServerWrapper::GetBallSpawnPoint() [member function]
    def GetBallSpawnPoint(self) -> ActorWrapper: ...

    # void ServerWrapper::SetBallSpawnPoint(ActorWrapper newBallSpawnPoint) [member function]
    def SetBallSpawnPoint(self, newBallSpawnPoint: ActorWrapper) -> None: ...

    # int ServerWrapper::GetSeriesLength() [member function]
    def GetSeriesLength(self) -> int: ...

    # void ServerWrapper::SetSeriesLength(int newSeriesLength) [member function]
    def SetSeriesLength(self, newSeriesLength: int) -> None: ...

    # int ServerWrapper::GetGameTime() [member function]
    def GetGameTime(self) -> int: ...

    # void ServerWrapper::SetGameTime(int newGameTime) [member function]
    def SetGameTime(self, newGameTime: int) -> None: ...

    # int ServerWrapper::GetWarmupTime() [member function]
    def GetWarmupTime(self) -> int: ...

    # void ServerWrapper::SetWarmupTime(int newWarmupTime) [member function]
    def SetWarmupTime(self, newWarmupTime: int) -> None: ...

    # int ServerWrapper::GetMaxScore() [member function]
    def GetMaxScore(self) -> int: ...

    # void ServerWrapper::SetMaxScore(int newMaxScore) [member function]
    def SetMaxScore(self, newMaxScore: int) -> None: ...

    # int ServerWrapper::GetAutoBalanceDifference() [member function]
    def GetAutoBalanceDifference(self) -> int: ...

    # void ServerWrapper::SetAutoBalanceDifference(int newAutoBalanceDifference) [member function]
    def SetAutoBalanceDifference(self, newAutoBalanceDifference: int) -> None: ...

    # int ServerWrapper::GetLastTrialTime() [member function]
    def GetLastTrialTime(self) -> int: ...

    # void ServerWrapper::SetLastTrialTime(int newLastTrialTime) [member function]
    def SetLastTrialTime(self, newLastTrialTime: int) -> None: ...

    # float ServerWrapper::GetScoreSlomoTime() [member function]
    def GetScoreSlomoTime(self) -> float: ...

    # void ServerWrapper::SetScoreSlomoTime(float newScoreSlomoTime) [member function]
    def SetScoreSlomoTime(self, newScoreSlomoTime: float) -> None: ...

    # float ServerWrapper::GetGameTimeRemaining() [member function]
    def GetGameTimeRemaining(self) -> float: ...

    # void ServerWrapper::SetGameTimeRemaining(float newGameTimeRemaining) [member function]
    def SetGameTimeRemaining(self, newGameTimeRemaining: float) -> None: ...

    # int ServerWrapper::GetSecondsRemaining() [member function]
    def GetSecondsRemaining(self) -> int: ...

    # void ServerWrapper::SetSecondsRemaining(int newSecondsRemaining) [member function]
    def SetSecondsRemaining(self, newSecondsRemaining: int) -> None: ...

    # int ServerWrapper::GetWaitTimeRemaining() [member function]
    def GetWaitTimeRemaining(self) -> int: ...

    # void ServerWrapper::SetWaitTimeRemaining(int newWaitTimeRemaining) [member function]
    def SetWaitTimeRemaining(self, newWaitTimeRemaining: int) -> None: ...

    # float ServerWrapper::GetTotalGameTimePlayed() [member function]
    def GetTotalGameTimePlayed(self) -> float: ...

    # void ServerWrapper::SetTotalGameTimePlayed(float newTotalGameTimePlayed) [member function]
    def SetTotalGameTimePlayed(self, newTotalGameTimePlayed: float) -> None: ...

    # float ServerWrapper::GetOvertimeTimePlayed() [member function]
    def GetOvertimeTimePlayed(self) -> float: ...

    # void ServerWrapper::SetOvertimeTimePlayed(float newOvertimeTimePlayed) [member function]
    def SetOvertimeTimePlayed(self, newOvertimeTimePlayed: float) -> None: ...

    # long unsigned int ServerWrapper::GetbRoundActive() [member function]
    def GetbRoundActive(self) -> bool: ...

    # void ServerWrapper::SetbRoundActive(long unsigned int newbRoundActive) [member function]
    def SetbRoundActive(self, newbRoundActive: bool) -> None: ...

    # long unsigned int ServerWrapper::GetbPlayReplays() [member function]
    def GetbPlayReplays(self) -> bool: ...

    # void ServerWrapper::SetbPlayReplays(long unsigned int newbPlayReplays) [member function]
    def SetbPlayReplays(self, newbPlayReplays: bool) -> None: ...

    # long unsigned int ServerWrapper::GetbBallHasBeenHit() [member function]
    def GetbBallHasBeenHit(self) -> bool: ...

    # void ServerWrapper::SetbBallHasBeenHit(long unsigned int newbBallHasBeenHit) [member function]
    def SetbBallHasBeenHit(self, newbBallHasBeenHit: bool) -> None: ...

    # long unsigned int ServerWrapper::GetbOverTime() [member function]
    def GetbOverTime(self) -> bool: ...

    # void ServerWrapper::SetbOverTime(long unsigned int newbOverTime) [member function]
    def SetbOverTime(self, newbOverTime: bool) -> None: ...

    # long unsigned int ServerWrapper::GetbUnlimitedTime() [member function]
    def GetbUnlimitedTime(self) -> bool: ...

    # void ServerWrapper::SetbUnlimitedTime(long unsigned int newbUnlimitedTime) [member function]
    def SetbUnlimitedTime(self, newbUnlimitedTime: bool) -> None: ...

    # long unsigned int ServerWrapper::GetbKickOnTrialEnd() [member function]
    def GetbKickOnTrialEnd(self) -> bool: ...

    # void ServerWrapper::SetbKickOnTrialEnd(long unsigned int newbKickOnTrialEnd) [member function]
    def SetbKickOnTrialEnd(self, newbKickOnTrialEnd: bool) -> None: ...

    # long unsigned int ServerWrapper::GetbNoContest() [member function]
    def GetbNoContest(self) -> bool: ...

    # void ServerWrapper::SetbNoContest(long unsigned int newbNoContest) [member function]
    def SetbNoContest(self, newbNoContest: bool) -> None: ...

    # long unsigned int ServerWrapper::GetbDisableGoalDelay() [member function]
    def GetbDisableGoalDelay(self) -> bool: ...

    # void ServerWrapper::SetbDisableGoalDelay(long unsigned int newbDisableGoalDelay) [member function]
    def SetbDisableGoalDelay(self, newbDisableGoalDelay: bool) -> None: ...

    # long unsigned int ServerWrapper::GetbShowNoScorerGoalMessage() [member function]
    def GetbShowNoScorerGoalMessage(self) -> bool: ...

    # void ServerWrapper::SetbShowNoScorerGoalMessage(long unsigned int newbShowNoScorerGoalMessage) [member function]
    def SetbShowNoScorerGoalMessage(self, newbShowNoScorerGoalMessage: bool) -> None: ...

    # long unsigned int ServerWrapper::GetbMatchEnded() [member function]
    def GetbMatchEnded(self) -> bool: ...

    # void ServerWrapper::SetbMatchEnded(long unsigned int newbMatchEnded) [member function]
    def SetbMatchEnded(self, newbMatchEnded: bool) -> None: ...

    # long unsigned int ServerWrapper::GetbShowIntroScene() [member function]
    def GetbShowIntroScene(self) -> bool: ...

    # void ServerWrapper::SetbShowIntroScene(long unsigned int newbShowIntroScene) [member function]
    def SetbShowIntroScene(self, newbShowIntroScene: bool) -> None: ...

    # long unsigned int ServerWrapper::GetbClubMatch() [member function]
    def GetbClubMatch(self) -> bool: ...

    # void ServerWrapper::SetbClubMatch(long unsigned int newbClubMatch) [member function]
    def SetbClubMatch(self, newbClubMatch: bool) -> None: ...

    # int ServerWrapper::GetNextSpawnIndex() [member function]
    def GetNextSpawnIndex(self) -> int: ...

    # void ServerWrapper::SetNextSpawnIndex(int newNextSpawnIndex) [member function]
    def SetNextSpawnIndex(self, newNextSpawnIndex: int) -> None: ...

    # ReplayDirectorWrapper ServerWrapper::GetReplayDirectorArchetype() [member function]
    def GetReplayDirectorArchetype(self) -> ReplayDirectorWrapper: ...

    # void ServerWrapper::SetReplayDirectorArchetype(ReplayDirectorWrapper newReplayDirectorArchetype) [member function]
    def SetReplayDirectorArchetype(self, newReplayDirectorArchetype: ReplayDirectorWrapper) -> None: ...

    # ReplayDirectorWrapper ServerWrapper::GetReplayDirector() [member function]
    def GetReplayDirector(self) -> ReplayDirectorWrapper: ...

    # void ServerWrapper::SetReplayDirector(ReplayDirectorWrapper newReplayDirector) [member function]
    def SetReplayDirector(self, newReplayDirector: ReplayDirectorWrapper) -> None: ...

    # ArrayWrapper<BallWrapper> ServerWrapper::GetGameBalls() [member function]
    def GetGameBalls(self) -> ArrayWrapper_BallWrapper: ...

    # int ServerWrapper::GetTotalGameBalls() [member function]
    def GetTotalGameBalls(self) -> int: ...

    # void ServerWrapper::SetTotalGameBalls(int newTotalGameBalls) [member function]
    def SetTotalGameBalls(self, newTotalGameBalls: int) -> None: ...

    # float ServerWrapper::GetPostGoalTime() [member function]
    def GetPostGoalTime(self) -> float: ...

    # void ServerWrapper::SetPostGoalTime(float newPostGoalTime) [member function]
    def SetPostGoalTime(self, newPostGoalTime: float) -> None: ...

    # ArrayWrapper<GoalWrapper> ServerWrapper::GetGoals() [member function]
    def GetGoals(self) -> ArrayWrapper_GoalWrapper: ...

    # int ServerWrapper::GetSecondsRemainingCountdown() [member function]
    def GetSecondsRemainingCountdown(self) -> int: ...

    # void ServerWrapper::SetSecondsRemainingCountdown(int newSecondsRemainingCountdown) [member function]
    def SetSecondsRemainingCountdown(self, newSecondsRemainingCountdown: int) -> None: ...

    # Vector ServerWrapper::GetFieldCenter() [member function]
    def GetFieldCenter(self) -> Vector: ...

    # void ServerWrapper::SetFieldCenter(Vector newFieldCenter) [member function]
    def SetFieldCenter(self, newFieldCenter: Vector) -> None: ...

    # TeamWrapper ServerWrapper::GetGameWinner() [member function]
    def GetGameWinner(self) -> TeamWrapper: ...

    # void ServerWrapper::SetGameWinner(TeamWrapper newGameWinner) [member function]
    def SetGameWinner(self, newGameWinner: TeamWrapper) -> None: ...

    # TeamWrapper ServerWrapper::GetMatchWinner() [member function]
    def GetMatchWinner(self) -> TeamWrapper: ...

    # void ServerWrapper::SetMatchWinner(TeamWrapper newMatchWinner) [member function]
    def SetMatchWinner(self, newMatchWinner: TeamWrapper) -> None: ...

    # PriWrapper ServerWrapper::GetMVP() [member function]
    def GetMVP(self) -> PriWrapper: ...

    # void ServerWrapper::SetMVP(PriWrapper newMVP) [member function]
    def SetMVP(self, newMVP: PriWrapper) -> None: ...

    # PriWrapper ServerWrapper::GetFastestGoalPlayer() [member function]
    def GetFastestGoalPlayer(self) -> PriWrapper: ...

    # void ServerWrapper::SetFastestGoalPlayer(PriWrapper newFastestGoalPlayer) [member function]
    def SetFastestGoalPlayer(self, newFastestGoalPlayer: PriWrapper) -> None: ...

    # PriWrapper ServerWrapper::GetSlowestGoalPlayer() [member function]
    def GetSlowestGoalPlayer(self) -> PriWrapper: ...

    # void ServerWrapper::SetSlowestGoalPlayer(PriWrapper newSlowestGoalPlayer) [member function]
    def SetSlowestGoalPlayer(self, newSlowestGoalPlayer: PriWrapper) -> None: ...

    # PriWrapper ServerWrapper::GetFurthestGoalPlayer() [member function]
    def GetFurthestGoalPlayer(self) -> PriWrapper: ...

    # void ServerWrapper::SetFurthestGoalPlayer(PriWrapper newFurthestGoalPlayer) [member function]
    def SetFurthestGoalPlayer(self, newFurthestGoalPlayer: PriWrapper) -> None: ...

    # float ServerWrapper::GetFastestGoalSpeed() [member function]
    def GetFastestGoalSpeed(self) -> float: ...

    # void ServerWrapper::SetFastestGoalSpeed(float newFastestGoalSpeed) [member function]
    def SetFastestGoalSpeed(self, newFastestGoalSpeed: float) -> None: ...

    # float ServerWrapper::GetSlowestGoalSpeed() [member function]
    def GetSlowestGoalSpeed(self) -> float: ...

    # void ServerWrapper::SetSlowestGoalSpeed(float newSlowestGoalSpeed) [member function]
    def SetSlowestGoalSpeed(self, newSlowestGoalSpeed: float) -> None: ...

    # float ServerWrapper::GetFurthestGoal() [member function]
    def GetFurthestGoal(self) -> float: ...

    # void ServerWrapper::SetFurthestGoal(float newFurthestGoal) [member function]
    def SetFurthestGoal(self, newFurthestGoal: float) -> None: ...

    # unsigned char ServerWrapper::GetReplicatedScoredOnTeam() [member function]
    def GetReplicatedScoredOnTeam(self) -> int: ...

    # void ServerWrapper::SetReplicatedScoredOnTeam(unsigned char newReplicatedScoredOnTeam) [member function]
    def SetReplicatedScoredOnTeam(self, newReplicatedScoredOnTeam: int) -> None: ...

    # unsigned char ServerWrapper::GetReplicatedServerPerformanceState() [member function]
    def GetReplicatedServerPerformanceState(self) -> int: ...

    # void ServerWrapper::SetReplicatedServerPerformanceState(unsigned char newReplicatedServerPerformanceState) [member function]
    def SetReplicatedServerPerformanceState(self, newReplicatedServerPerformanceState: int) -> None: ...

    # int ServerWrapper::GetRoundNum() [member function]
    def GetRoundNum(self) -> int: ...

    # void ServerWrapper::SetRoundNum(int newRoundNum) [member function]
    def SetRoundNum(self, newRoundNum: int) -> None: ...

    # float ServerWrapper::GetKickIdleReplayOffset() [member function]
    def GetKickIdleReplayOffset(self) -> float: ...

    # void ServerWrapper::SetKickIdleReplayOffset(float newKickIdleReplayOffset) [member function]
    def SetKickIdleReplayOffset(self, newKickIdleReplayOffset: float) -> None: ...

    # float ServerWrapper::GetAssistMaxTime() [member function]
    def GetAssistMaxTime(self) -> float: ...

    # void ServerWrapper::SetAssistMaxTime(float newAssistMaxTime) [member function]
    def SetAssistMaxTime(self, newAssistMaxTime: float) -> None: ...

    # float ServerWrapper::GetBallHasBeenHitStartDelay() [member function]
    def GetBallHasBeenHitStartDelay(self) -> float: ...

    # void ServerWrapper::SetBallHasBeenHitStartDelay(float newBallHasBeenHitStartDelay) [member function]
    def SetBallHasBeenHitStartDelay(self, newBallHasBeenHitStartDelay: float) -> None: ...

    # float ServerWrapper::GetPodiumDelay() [member function]
    def GetPodiumDelay(self) -> float: ...

    # void ServerWrapper::SetPodiumDelay(float newPodiumDelay) [member function]
    def SetPodiumDelay(self, newPodiumDelay: float) -> None: ...

    # float ServerWrapper::GetPodiumTime() [member function]
    def GetPodiumTime(self) -> float: ...

    # void ServerWrapper::SetPodiumTime(float newPodiumTime) [member function]
    def SetPodiumTime(self, newPodiumTime: float) -> None: ...

    # int ServerWrapper::GetLobbyEndCountdown() [member function]
    def GetLobbyEndCountdown(self) -> int: ...

    # void ServerWrapper::SetLobbyEndCountdown(int newLobbyEndCountdown) [member function]
    def SetLobbyEndCountdown(self, newLobbyEndCountdown: int) -> None: ...

    # int ServerWrapper::GetLobbyCountdown() [member function]
    def GetLobbyCountdown(self) -> int: ...

    # void ServerWrapper::SetLobbyCountdown(int newLobbyCountdown) [member function]
    def SetLobbyCountdown(self, newLobbyCountdown: int) -> None: ...

    # float ServerWrapper::GetLobbyTime() [member function]
    def GetLobbyTime(self) -> float: ...

    # void ServerWrapper::SetLobbyTime(float newLobbyTime) [member function]
    def SetLobbyTime(self, newLobbyTime: float) -> None: ...

    # int ServerWrapper::GetLobbySpawnRestartTime() [member function]
    def GetLobbySpawnRestartTime(self) -> int: ...

    # void ServerWrapper::SetLobbySpawnRestartTime(int newLobbySpawnRestartTime) [member function]
    def SetLobbySpawnRestartTime(self, newLobbySpawnRestartTime: int) -> None: ...

    # PlayerControllerWrapper ServerWrapper::GetPauser() [member function]
    def GetPauser(self) -> PlayerControllerWrapper: ...

    # void ServerWrapper::SetPauser(PlayerControllerWrapper newPauser) [member function]
    def SetPauser(self, newPauser: PlayerControllerWrapper) -> None: ...

    # int ServerWrapper::GetPlayerCarCount() [member function]
    def GetPlayerCarCount(self) -> int: ...

    # void ServerWrapper::ReplicateSkillTiers() [member function]
    def ReplicateSkillTiers(self) -> None: ...

    # void ServerWrapper::RemoveTeamSelection() [member function]
    def RemoveTeamSelection(self) -> None: ...

    # void ServerWrapper::CheckStart() [member function]
    def CheckStart(self) -> None: ...

    # void ServerWrapper::StartLobbyTimer() [member function]
    def StartLobbyTimer(self) -> None: ...

    # void ServerWrapper::HandleCountdownTick() [member function]
    def HandleCountdownTick(self) -> None: ...

    # void ServerWrapper::CheckForCountdownAction() [member function]
    def CheckForCountdownAction(self) -> None: ...

    # void ServerWrapper::LobbyCountdownTick() [member function]
    def LobbyCountdownTick(self) -> None: ...

    # bool ServerWrapper::CanSpawnBots() [member function]
    def CanSpawnBots(self) -> bool: ...

    # void ServerWrapper::StartRound() [member function]
    def StartRound(self) -> None: ...

    # void ServerWrapper::EndRound() [member function]
    def EndRound(self) -> None: ...

    # void ServerWrapper::SetBallEventListeners(BallWrapper Ball, long unsigned int bListen) [member function]
    def SetBallEventListeners(self, Ball: BallWrapper, bListen: bool) -> None: ...

    # bool ServerWrapper::CanAwardPoints() [member function]
    def CanAwardPoints(self) -> bool: ...

    # void ServerWrapper::HandleCarTouch(BallWrapper Ball, CarWrapper HitCar, unsigned char HitType) [member function]
    def HandleCarTouch(self, Ball: BallWrapper, HitCar: CarWrapper, HitType: int) -> None: ...

    # void ServerWrapper::SetBallHasBeenHit2() [member function]
    def SetBallHasBeenHit2(self) -> None: ...

    # int ServerWrapper::DetermineScoreTouchIndex(BallWrapper Ball, GoalWrapper Goal) [member function]
    def DetermineScoreTouchIndex(self, Ball: BallWrapper, Goal: GoalWrapper) -> int: ...

    # int ServerWrapper::DetermineAssistTouchIndex(BallWrapper Ball, int ScoreIdx) [member function]
    def DetermineAssistTouchIndex(self, Ball: BallWrapper, ScoreIdx: int) -> int: ...

    # void ServerWrapper::UpdateTotalGameTimePlayed(float DeltaTime) [member function]
    def UpdateTotalGameTimePlayed(self, DeltaTime: float) -> None: ...

    # void ServerWrapper::UpdateGameTime(float DeltaTime) [member function]
    def UpdateGameTime(self, DeltaTime: float) -> None: ...

    # bool ServerWrapper::CanUpdateGameTime() [member function]
    def CanUpdateGameTime(self) -> bool: ...

    # void ServerWrapper::WaitForBallOnGround() [member function]
    def WaitForBallOnGround(self) -> None: ...

    # bool ServerWrapper::BallHitGround(Vector & HitNorm) [member function]
    def BallHitGround(self, HitNorm: Vector) -> bool: ...

    # void ServerWrapper::HandleBallHitGround(BallWrapper Ball, Vector & HitLoc, Vector & HitNorm) [member function]
    def HandleBallHitGround(self, Ball: BallWrapper, HitLoc: Vector, HitNorm: Vector) -> None: ...

    # void ServerWrapper::HandleBallHitGroundTimeout() [member function]
    def HandleBallHitGroundTimeout(self) -> None: ...

    # void ServerWrapper::StartReplay() [member function]
    def StartReplay(self) -> None: ...

    # void ServerWrapper::HandleReplayFinished(ReplayDirectorWrapper InReplay) [member function]
    def HandleReplayFinished(self, InReplay: ReplayDirectorWrapper) -> None: ...

    # void ServerWrapper::GotoPodiumSpotlight() [member function]
    def GotoPodiumSpotlight(self) -> None: ...

    # void ServerWrapper::UpdateSpotlight() [member function]
    def UpdateSpotlight(self) -> None: ...

    # void ServerWrapper::SpawnPodiumCars() [member function]
    def SpawnPodiumCars(self) -> None: ...

    # bool ServerWrapper::CanEnableCarPodiumMovement() [member function]
    def CanEnableCarPodiumMovement(self) -> bool: ...

    # void ServerWrapper::FinishEvent() [member function]
    def FinishEvent(self) -> None: ...

    # bool ServerWrapper::__GameEvent_Soccar_TA__UpdateTeamScores(TeamWrapper T) [member function]
    def __GameEvent_Soccar_TA__UpdateTeamScores(self, T: TeamWrapper) -> bool: ...

    # void ServerWrapper::__GameEvent_Soccar_TA__SubmitMatchComplete(PriWrapper PRI) [member function]
    def __GameEvent_Soccar_TA__SubmitMatchComplete(self, PRI: PriWrapper) -> None: ...

    # void ServerWrapper::__GameEvent_Soccar_TA__CheckStart(TeamWrapper T) [member function]
    def __GameEvent_Soccar_TA__CheckStart(self, T: TeamWrapper) -> None: ...

    # void ServerWrapper::__GameEvent_Soccar_TA__EndState(TeamWrapper T) [member function]
    def __GameEvent_Soccar_TA__EndState(self, T: TeamWrapper) -> None: ...

    # void ServerWrapper::__ReplicatedServerPerformanceState__ChangeNotifyFunc() [member function]
    def __ReplicatedServerPerformanceState__ChangeNotifyFunc(self) -> None: ...

    # void ServerWrapper::__bClubMatch__ChangeNotifyFunc() [member function]
    def __bClubMatch__ChangeNotifyFunc(self) -> None: ...

    # void ServerWrapper::__bShowIntroScene__ChangeNotifyFunc() [member function]
    def __bShowIntroScene__ChangeNotifyFunc(self) -> None: ...

    # void ServerWrapper::__WaitTimeRemaining__ChangeNotifyFunc() [member function]
    def __WaitTimeRemaining__ChangeNotifyFunc(self) -> None: ...

    # void ServerWrapper::CheckJoinInProgress(PriWrapper PRI) [member function]
    def CheckJoinInProgress(self, PRI: PriWrapper) -> None: ...

    # bool ServerWrapper::AllowDynamicCrowd() [member function]
    def AllowDynamicCrowd(self) -> bool: ...

    # void ServerWrapper::AddBallTrajectory(BallWrapper InBall) [member function]
    def AddBallTrajectory(self, InBall: BallWrapper) -> None: ...

    # bool ServerWrapper::ShowScorerGoalMessage() [member function]
    def ShowScorerGoalMessage(self) -> bool: ...

    # bool ServerWrapper::CanUseBallCam() [member function]
    def CanUseBallCam(self) -> bool: ...

    # bool ServerWrapper::DisableStatXP() [member function]
    def DisableStatXP(self) -> bool: ...

    # void ServerWrapper::SetDisableGoalDelay(long unsigned int bInDisableGoalDelay) [member function]
    def SetDisableGoalDelay(self, bInDisableGoalDelay: bool) -> None: ...

    # void ServerWrapper::ForceMatchStart() [member function]
    def ForceMatchStart(self) -> None: ...

    # void ServerWrapper::RemoveLocalPlayer(PlayerControllerWrapper Player) [member function]
    def RemoveLocalPlayer(self, Player: PlayerControllerWrapper) -> None: ...

    # void ServerWrapper::AddLocalPlayer(PlayerControllerWrapper Player) [member function]
    def AddLocalPlayer(self, Player: PlayerControllerWrapper) -> None: ...

    # void ServerWrapper::DestroyGoalIndicators(PlayerControllerWrapper Player) [member function]
    def DestroyGoalIndicators(self, Player: PlayerControllerWrapper) -> None: ...

    # void ServerWrapper::CreateGoalIndicators(PlayerControllerWrapper Player) [member function]
    def CreateGoalIndicators(self, Player: PlayerControllerWrapper) -> None: ...

    # void ServerWrapper::BeginHighlightsReplay() [member function]
    def BeginHighlightsReplay(self) -> None: ...

    # bool ServerWrapper::ShouldCountUp() [member function]
    def ShouldCountUp(self) -> bool: ...

    # bool ServerWrapper::ShouldAllowVoteToForfeit() [member function]
    def ShouldAllowVoteToForfeit(self) -> bool: ...

    # bool ServerWrapper::ShouldHaveLeaveMatchPenalty() [member function]
    def ShouldHaveLeaveMatchPenalty(self) -> bool: ...

    # void ServerWrapper::SetPaused(PlayerControllerWrapper InPauser, long unsigned int bInPaused) [member function]
    def SetPaused(self, InPauser: PlayerControllerWrapper, bInPaused: bool) -> None: ...

    # bool ServerWrapper::ShouldCountdownResumeFromPause() [member function]
    def ShouldCountdownResumeFromPause(self) -> bool: ...

    # void ServerWrapper::SetScoreAndTime(PlayerControllerWrapper PC, int NewScoreTeam0, int NewScoreTeam1, int InGameTimeRemaining, long unsigned int bInOvertime, long unsigned int bRestartRound) [member function]
    def SetScoreAndTime(self, PC: PlayerControllerWrapper, NewScoreTeam0: int, NewScoreTeam1: int, InGameTimeRemaining: int, bInOvertime: bool, bRestartRound: bool) -> None: ...

    # void ServerWrapper::SaveLocalPlayerStats() [member function]
    def SaveLocalPlayerStats(self) -> None: ...

    # bool ServerWrapper::ShouldPlayReplay() [member function]
    def ShouldPlayReplay(self) -> bool: ...

    # bool ServerWrapper::ShouldRecordReplay() [member function]
    def ShouldRecordReplay(self) -> bool: ...

    # void ServerWrapper::OnBallHasBeenHit() [member function]
    def OnBallHasBeenHit(self) -> None: ...

    # BallWrapper ServerWrapper::SpawnBall2(Vector & SpawnLoc, long unsigned int bWake, long unsigned int bSpawnCannon, std::string BallArch) [member function]
    def SpawnBall2(self, SpawnLoc: Vector, bWake: bool, bSpawnCannon: bool, BallArch: str) -> BallWrapper: ...

    # int ServerWrapper::GetTotalScore() [member function]
    def GetTotalScore(self) -> int: ...

    # void ServerWrapper::HandleCarSet(PriWrapper InPRI) [member function]
    def HandleCarSet(self, InPRI: PriWrapper) -> None: ...

    # void ServerWrapper::RemovePlayer(ControllerWrapper Player) [member function]
    def RemovePlayer(self, Player: ControllerWrapper) -> None: ...

    # void ServerWrapper::RemovePRI(PriWrapper PRI) [member function]
    def RemovePRI(self, PRI: PriWrapper) -> None: ...

    # void ServerWrapper::AddPRI(PriWrapper PRI) [member function]
    def AddPRI(self, PRI: PriWrapper) -> None: ...

    # void ServerWrapper::OnMatchWinnerSet() [member function]
    def OnMatchWinnerSet(self) -> None: ...

    # void ServerWrapper::OnGameWinnerSet() [member function]
    def OnGameWinnerSet(self) -> None: ...

    # int ServerWrapper::MVPSort(PriWrapper A, PriWrapper B) [member function]
    def MVPSort(self, A: PriWrapper, B: PriWrapper) -> int: ...

    # void ServerWrapper::HandleHitGoal(BallWrapper Ball, GoalWrapper Goal) [member function]
    def HandleHitGoal(self, Ball: BallWrapper, Goal: GoalWrapper) -> None: ...

    # void ServerWrapper::ClearReplicatedScoredOnTeam() [member function]
    def ClearReplicatedScoredOnTeam(self) -> None: ...

    # void ServerWrapper::TriggerScoreChangedEvent() [member function]
    def TriggerScoreChangedEvent(self) -> None: ...

    # void ServerWrapper::HandleScoreUpdated(TeamWrapper Team) [member function]
    def HandleScoreUpdated(self, Team: TeamWrapper) -> None: ...

    # void ServerWrapper::OnAllTeamsCreated() [member function]
    def OnAllTeamsCreated(self) -> None: ...

    # void ServerWrapper::TriggerGoalScoreEvent(int TeamScoredOn, CarWrapper Scorer) [member function]
    def TriggerGoalScoreEvent(self, TeamScoredOn: int, Scorer: CarWrapper) -> None: ...

    # void ServerWrapper::SetTotalGameBalls2(int TotalBalls) [member function]
    def SetTotalGameBalls2(self, TotalBalls: int) -> None: ...

    # void ServerWrapper::RecordRecentPlayers() [member function]
    def RecordRecentPlayers(self) -> None: ...

    # void ServerWrapper::UpdateStats() [member function]
    def UpdateStats(self) -> None: ...

    # void ServerWrapper::NotifyKismetOfCurrentTime() [member function]
    def NotifyKismetOfCurrentTime(self) -> None: ...

    # bool ServerWrapper::EnoughTimePassedToForfeit() [member function]
    def EnoughTimePassedToForfeit(self) -> bool: ...

    # void ServerWrapper::OnGameTimeUpdated() [member function]
    def OnGameTimeUpdated(self) -> None: ...

    # void ServerWrapper::OnOvertimeUpdated() [member function]
    def OnOvertimeUpdated(self) -> None: ...

    # void ServerWrapper::ForceOvertime() [member function]
    def ForceOvertime(self) -> None: ...

    # void ServerWrapper::StartOvertime() [member function]
    def StartOvertime(self) -> None: ...

    # bool ServerWrapper::OnMyHalf(Vector & TestLocation, unsigned char TeamNum) [member function]
    def OnMyHalf(self, TestLocation: Vector, TeamNum: int) -> bool: ...

    # TeamWrapper ServerWrapper::GetWinningTeam() [member function]
    def GetWinningTeam(self) -> TeamWrapper: ...

    # void ServerWrapper::ResetPickups() [member function]
    def ResetPickups(self) -> None: ...

    # void ServerWrapper::ResetPlayers() [member function]
    def ResetPlayers(self) -> None: ...

    # void ServerWrapper::OnBallSpawned(BallWrapper NewBall) [member function]
    def OnBallSpawned(self, NewBall: BallWrapper) -> None: ...

    # void ServerWrapper::ResetBalls() [member function]
    def ResetBalls(self) -> None: ...

    # void ServerWrapper::DestroyCars() [member function]
    def DestroyCars(self) -> None: ...

    # void ServerWrapper::FreezePawns() [member function]
    def FreezePawns(self) -> None: ...

    # void ServerWrapper::DestroyBalls() [member function]
    def DestroyBalls(self) -> None: ...

    # void ServerWrapper::RemoveGameBall(BallWrapper Ball) [member function]
    def RemoveGameBall(self, Ball: BallWrapper) -> None: ...

    # void ServerWrapper::AddGameBall(BallWrapper Ball) [member function]
    def AddGameBall(self, Ball: BallWrapper) -> None: ...

    # void ServerWrapper::StartNewRound() [member function]
    def StartNewRound(self) -> None: ...

    # void ServerWrapper::CheckForAutoBalance() [member function]
    def CheckForAutoBalance(self) -> None: ...

    # bool ServerWrapper::HasWinner() [member function]
    def HasWinner(self) -> bool: ...

    # void ServerWrapper::SubmitMatch2() [member function]
    def SubmitMatch2(self) -> None: ...

    # void ServerWrapper::SubmitMatchComplete2() [member function]
    def SubmitMatchComplete2(self) -> None: ...

    # void ServerWrapper::OnMatchEnded() [member function]
    def OnMatchEnded(self) -> None: ...

    # bool ServerWrapper::ShouldDoPodiumSpotlight() [member function]
    def ShouldDoPodiumSpotlight(self) -> bool: ...

    # void ServerWrapper::EndGame() [member function]
    def EndGame(self) -> None: ...

    # void ServerWrapper::UpdateTeamScores2() [member function]
    def UpdateTeamScores2(self) -> None: ...

    # void ServerWrapper::StartNewGame() [member function]
    def StartNewGame(self) -> None: ...

    # void ServerWrapper::ResetGame() [member function]
    def ResetGame(self) -> None: ...

    # void ServerWrapper::ClearReplicatedStatEvent() [member function]
    def ClearReplicatedStatEvent(self) -> None: ...

    # void ServerWrapper::eventDestroyed() [member function]
    def eventDestroyed(self) -> None: ...

    # void ServerWrapper::InitBotDetection() [member function]
    def InitBotDetection(self) -> None: ...

    # void ServerWrapper::InitCrowdManager() [member function]
    def InitCrowdManager(self) -> None: ...

    # void ServerWrapper::InitField() [member function]
    def InitField(self) -> None: ...

    # void ServerWrapper::InitGameObserver() [member function]
    def InitGameObserver(self) -> None: ...

    # void ServerWrapper::OnInit() [member function]
    def OnInit(self) -> None: ...

    # void ServerWrapper::InitMutators() [member function]
    def InitMutators(self) -> None: ...

    # void ServerWrapper::OnClubMatch() [member function]
    def OnClubMatch(self) -> None: ...

    # bool ServerWrapper::CanInitClubMatch() [member function]
    def CanInitClubMatch(self) -> bool: ...

    # void ServerWrapper::AssignCustomTeamSettings() [member function]
    def AssignCustomTeamSettings(self) -> None: ...

    # void ServerWrapper::InitGame2(std::string Options) [member function]
    def InitGame2(self, Options: str) -> None: ...

    # std::string ServerWrapper::GetMatchGUID() [member function]
    def GetMatchGUID(self) -> str: ...

    # void ServerWrapper::SetMatchGUID(std::string s) [member function]
    def SetMatchGUID(self, s: str) -> None: ...

    # void ServerWrapper::EventGameWinnerSet(ServerWrapper GameEvent) [member function]
    def EventGameWinnerSet(self, GameEvent: ServerWrapper) -> None: ...

    # void ServerWrapper::EventGoalScored(ServerWrapper GameEvent, BallWrapper Ball, GoalWrapper Goal, int ScoreIndex, int AssistIdx) [member function]
    def EventGoalScored(self, GameEvent: ServerWrapper, Ball: BallWrapper, Goal: GoalWrapper, ScoreIndex: int, AssistIdx: int) -> None: ...

    # Private:
    # ServerWrapper::Impl [class declaration]

    # ServerWrapper::pimpl [variable]
    @property
    def pimpl(self) -> Any: ...


