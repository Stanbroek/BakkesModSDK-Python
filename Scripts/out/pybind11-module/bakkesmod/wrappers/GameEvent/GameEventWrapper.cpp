void bind_GameEventWrapper(pybind11::module& m)
{

	pybind11::class_<GameEventWrapper, std::shared_ptr<GameEventWrapper>, ActorWrapper> cl_GameEventWrapper(m, "GameEventWrapper");
	cl_GameEventWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_GameEventWrapper.def(pybind11::init<GameEventWrapper const &>(), pybind11::arg("other"));
	// cl_GameEventWrapper.def(pybind11::del<>());
	//cl_GameEventWrapper.def("GetGameMode", [](GameEventWrapper& cls_) { return cls_.GetGameMode(); });
	//cl_GameEventWrapper.def("SetGameMode", [](GameEventWrapper& cls_, unsigned char newGameMode) { return cls_.SetGameMode(newGameMode); }, pybind11::arg("newGameMode"));
	cl_GameEventWrapper.def("GetReplicatedStateIndex", [](GameEventWrapper& cls_) { return cls_.GetReplicatedStateIndex(); });
	cl_GameEventWrapper.def("SetReplicatedStateIndex", [](GameEventWrapper& cls_, unsigned char newReplicatedStateIndex) { return cls_.SetReplicatedStateIndex(newReplicatedStateIndex); }, pybind11::arg("newReplicatedStateIndex"));
	cl_GameEventWrapper.def("GetCarArchetype", [](GameEventWrapper& cls_) { return cls_.GetCarArchetype(); });
	cl_GameEventWrapper.def("SetCarArchetype", [](GameEventWrapper& cls_, CarWrapper newCarArchetype) { return cls_.SetCarArchetype(newCarArchetype); }, pybind11::arg("newCarArchetype"));
	cl_GameEventWrapper.def("GetCountdownTime", [](GameEventWrapper& cls_) { return cls_.GetCountdownTime(); });
	cl_GameEventWrapper.def("SetCountdownTime", [](GameEventWrapper& cls_, int newCountdownTime) { return cls_.SetCountdownTime(newCountdownTime); }, pybind11::arg("newCountdownTime"));
	cl_GameEventWrapper.def("GetFinishTime", [](GameEventWrapper& cls_) { return cls_.GetFinishTime(); });
	cl_GameEventWrapper.def("SetFinishTime", [](GameEventWrapper& cls_, int newFinishTime) { return cls_.SetFinishTime(newFinishTime); }, pybind11::arg("newFinishTime"));
	cl_GameEventWrapper.def("GetbMultiplayer", [](GameEventWrapper& cls_) { return cls_.GetbMultiplayer(); });
	cl_GameEventWrapper.def("SetbMultiplayer", [](GameEventWrapper& cls_, long unsigned int newbMultiplayer) { return cls_.SetbMultiplayer(newbMultiplayer); }, pybind11::arg("newbMultiplayer"));
	cl_GameEventWrapper.def("GetbCountdownMessagesDisabled", [](GameEventWrapper& cls_) { return cls_.GetbCountdownMessagesDisabled(); });
	cl_GameEventWrapper.def("SetbCountdownMessagesDisabled", [](GameEventWrapper& cls_, long unsigned int newbCountdownMessagesDisabled) { return cls_.SetbCountdownMessagesDisabled(newbCountdownMessagesDisabled); }, pybind11::arg("newbCountdownMessagesDisabled"));
	cl_GameEventWrapper.def("GetbFillWithAI", [](GameEventWrapper& cls_) { return cls_.GetbFillWithAI(); });
	cl_GameEventWrapper.def("SetbFillWithAI", [](GameEventWrapper& cls_, long unsigned int newbFillWithAI) { return cls_.SetbFillWithAI(newbFillWithAI); }, pybind11::arg("newbFillWithAI"));
	cl_GameEventWrapper.def("GetbAllowQueueSaveReplay", [](GameEventWrapper& cls_) { return cls_.GetbAllowQueueSaveReplay(); });
	cl_GameEventWrapper.def("SetbAllowQueueSaveReplay", [](GameEventWrapper& cls_, long unsigned int newbAllowQueueSaveReplay) { return cls_.SetbAllowQueueSaveReplay(newbAllowQueueSaveReplay); }, pybind11::arg("newbAllowQueueSaveReplay"));
	cl_GameEventWrapper.def("GetbAllowReadyUp", [](GameEventWrapper& cls_) { return cls_.GetbAllowReadyUp(); });
	cl_GameEventWrapper.def("SetbAllowReadyUp", [](GameEventWrapper& cls_, long unsigned int newbAllowReadyUp) { return cls_.SetbAllowReadyUp(newbAllowReadyUp); }, pybind11::arg("newbAllowReadyUp"));
	cl_GameEventWrapper.def("GetbRestartingMatch", [](GameEventWrapper& cls_) { return cls_.GetbRestartingMatch(); });
	cl_GameEventWrapper.def("SetbRestartingMatch", [](GameEventWrapper& cls_, long unsigned int newbRestartingMatch) { return cls_.SetbRestartingMatch(newbRestartingMatch); }, pybind11::arg("newbRestartingMatch"));
	cl_GameEventWrapper.def("GetbRandomizedBotLoadouts", [](GameEventWrapper& cls_) { return cls_.GetbRandomizedBotLoadouts(); });
	cl_GameEventWrapper.def("SetbRandomizedBotLoadouts", [](GameEventWrapper& cls_, long unsigned int newbRandomizedBotLoadouts) { return cls_.SetbRandomizedBotLoadouts(newbRandomizedBotLoadouts); }, pybind11::arg("newbRandomizedBotLoadouts"));
	cl_GameEventWrapper.def("GetbHasLeaveMatchPenalty", [](GameEventWrapper& cls_) { return cls_.GetbHasLeaveMatchPenalty(); });
	cl_GameEventWrapper.def("SetbHasLeaveMatchPenalty", [](GameEventWrapper& cls_, long unsigned int newbHasLeaveMatchPenalty) { return cls_.SetbHasLeaveMatchPenalty(newbHasLeaveMatchPenalty); }, pybind11::arg("newbHasLeaveMatchPenalty"));
	cl_GameEventWrapper.def("GetbCanVoteToForfeit", [](GameEventWrapper& cls_) { return cls_.GetbCanVoteToForfeit(); });
	cl_GameEventWrapper.def("SetbCanVoteToForfeit", [](GameEventWrapper& cls_, long unsigned int newbCanVoteToForfeit) { return cls_.SetbCanVoteToForfeit(newbCanVoteToForfeit); }, pybind11::arg("newbCanVoteToForfeit"));
	cl_GameEventWrapper.def("GetbDisableAimAssist", [](GameEventWrapper& cls_) { return cls_.GetbDisableAimAssist(); });
	cl_GameEventWrapper.def("SetbDisableAimAssist", [](GameEventWrapper& cls_, long unsigned int newbDisableAimAssist) { return cls_.SetbDisableAimAssist(newbDisableAimAssist); }, pybind11::arg("newbDisableAimAssist"));
	cl_GameEventWrapper.def("GetbAwardAchievements", [](GameEventWrapper& cls_) { return cls_.GetbAwardAchievements(); });
	cl_GameEventWrapper.def("SetbAwardAchievements", [](GameEventWrapper& cls_, long unsigned int newbAwardAchievements) { return cls_.SetbAwardAchievements(newbAwardAchievements); }, pybind11::arg("newbAwardAchievements"));
	cl_GameEventWrapper.def("GetMinPlayers", [](GameEventWrapper& cls_) { return cls_.GetMinPlayers(); });
	cl_GameEventWrapper.def("SetMinPlayers", [](GameEventWrapper& cls_, int newMinPlayers) { return cls_.SetMinPlayers(newMinPlayers); }, pybind11::arg("newMinPlayers"));
	cl_GameEventWrapper.def("GetMaxPlayers", [](GameEventWrapper& cls_) { return cls_.GetMaxPlayers(); });
	cl_GameEventWrapper.def("SetMaxPlayers", [](GameEventWrapper& cls_, int newMaxPlayers) { return cls_.SetMaxPlayers(newMaxPlayers); }, pybind11::arg("newMaxPlayers"));
	cl_GameEventWrapper.def("GetSpawnPoints", [](GameEventWrapper& cls_) { return cls_.GetSpawnPoints(); });
	cl_GameEventWrapper.def("GetBotSkill", [](GameEventWrapper& cls_) { return cls_.GetBotSkill(); });
	cl_GameEventWrapper.def("SetBotSkill", [](GameEventWrapper& cls_, float newBotSkill) { return cls_.SetBotSkill(newBotSkill); }, pybind11::arg("newBotSkill"));
	cl_GameEventWrapper.def("GetRespawnTime", [](GameEventWrapper& cls_) { return cls_.GetRespawnTime(); });
	cl_GameEventWrapper.def("SetRespawnTime", [](GameEventWrapper& cls_, int newRespawnTime) { return cls_.SetRespawnTime(newRespawnTime); }, pybind11::arg("newRespawnTime"));
	cl_GameEventWrapper.def("GetMatchTimeDilation", [](GameEventWrapper& cls_) { return cls_.GetMatchTimeDilation(); });
	cl_GameEventWrapper.def("SetMatchTimeDilation", [](GameEventWrapper& cls_, float newMatchTimeDilation) { return cls_.SetMatchTimeDilation(newMatchTimeDilation); }, pybind11::arg("newMatchTimeDilation"));
	cl_GameEventWrapper.def("GetActivator", [](GameEventWrapper& cls_) { return cls_.GetActivator(); });
	cl_GameEventWrapper.def("SetActivator", [](GameEventWrapper& cls_, PlayerControllerWrapper newActivator) { return cls_.SetActivator(newActivator); }, pybind11::arg("newActivator"));
	cl_GameEventWrapper.def("GetActivatorCar", [](GameEventWrapper& cls_) { return cls_.GetActivatorCar(); });
	cl_GameEventWrapper.def("SetActivatorCar", [](GameEventWrapper& cls_, CarWrapper newActivatorCar) { return cls_.SetActivatorCar(newActivatorCar); }, pybind11::arg("newActivatorCar"));
	cl_GameEventWrapper.def("GetPlayers", [](GameEventWrapper& cls_) { return cls_.GetPlayers(); });
	cl_GameEventWrapper.def("GetPRIs", [](GameEventWrapper& cls_) { return cls_.GetPRIs(); });
	cl_GameEventWrapper.def("GetCars", [](GameEventWrapper& cls_) { return cls_.GetCars(); });
	cl_GameEventWrapper.def("GetLocalPlayers", [](GameEventWrapper& cls_) { return cls_.GetLocalPlayers(); });
	cl_GameEventWrapper.def("GetStartPointIndex", [](GameEventWrapper& cls_) { return cls_.GetStartPointIndex(); });
	cl_GameEventWrapper.def("SetStartPointIndex", [](GameEventWrapper& cls_, int newStartPointIndex) { return cls_.SetStartPointIndex(newStartPointIndex); }, pybind11::arg("newStartPointIndex"));
	cl_GameEventWrapper.def("GetGameStateTimeRemaining", [](GameEventWrapper& cls_) { return cls_.GetGameStateTimeRemaining(); });
	cl_GameEventWrapper.def("SetGameStateTimeRemaining", [](GameEventWrapper& cls_, int newGameStateTimeRemaining) { return cls_.SetGameStateTimeRemaining(newGameStateTimeRemaining); }, pybind11::arg("newGameStateTimeRemaining"));
	cl_GameEventWrapper.def("GetReplicatedGameStateTimeRemaining", [](GameEventWrapper& cls_) { return cls_.GetReplicatedGameStateTimeRemaining(); });
	cl_GameEventWrapper.def("SetReplicatedGameStateTimeRemaining", [](GameEventWrapper& cls_, int newReplicatedGameStateTimeRemaining) { return cls_.SetReplicatedGameStateTimeRemaining(newReplicatedGameStateTimeRemaining); }, pybind11::arg("newReplicatedGameStateTimeRemaining"));
	//cl_GameEventWrapper.def("GetIdleKickTime", [](GameEventWrapper& cls_) { return cls_.GetIdleKickTime(); });
	//cl_GameEventWrapper.def("SetIdleKickTime", [](GameEventWrapper& cls_, float newIdleKickTime) { return cls_.SetIdleKickTime(newIdleKickTime); }, pybind11::arg("newIdleKickTime"));
	//cl_GameEventWrapper.def("GetIdleKickWarningTime", [](GameEventWrapper& cls_) { return cls_.GetIdleKickWarningTime(); });
	//cl_GameEventWrapper.def("SetIdleKickWarningTime", [](GameEventWrapper& cls_, float newIdleKickWarningTime) { return cls_.SetIdleKickWarningTime(newIdleKickWarningTime); }, pybind11::arg("newIdleKickWarningTime"));
	cl_GameEventWrapper.def("GetBotBoostThreshold_vsAI", [](GameEventWrapper& cls_) { return cls_.GetBotBoostThreshold_vsAI(); });
	cl_GameEventWrapper.def("SetBotBoostThreshold_vsAI", [](GameEventWrapper& cls_, float newBotBoostThreshold_vsAI) { return cls_.SetBotBoostThreshold_vsAI(newBotBoostThreshold_vsAI); }, pybind11::arg("newBotBoostThreshold_vsAI"));
	cl_GameEventWrapper.def("GetForfeitInitiatorIDs", [](GameEventWrapper& cls_) { return cls_.GetForfeitInitiatorIDs(); });
	cl_GameEventWrapper.def("GetBannedPlayers", [](GameEventWrapper& cls_) { return cls_.GetBannedPlayers(); });
	cl_GameEventWrapper.def("GetGameOwner", [](GameEventWrapper& cls_) { return cls_.GetGameOwner(); });
	cl_GameEventWrapper.def("SetGameOwner", [](GameEventWrapper& cls_, PriWrapper newGameOwner) { return cls_.SetGameOwner(newGameOwner); }, pybind11::arg("newGameOwner"));
	cl_GameEventWrapper.def("GetRichPresenceString", [](GameEventWrapper& cls_) { return cls_.GetRichPresenceString(); });
	cl_GameEventWrapper.def("GetReplicatedRoundCountDownNumber", [](GameEventWrapper& cls_) { return cls_.GetReplicatedRoundCountDownNumber(); });
	cl_GameEventWrapper.def("SetReplicatedRoundCountDownNumber", [](GameEventWrapper& cls_, int newReplicatedRoundCountDownNumber) { return cls_.SetReplicatedRoundCountDownNumber(newReplicatedRoundCountDownNumber); }, pybind11::arg("newReplicatedRoundCountDownNumber"));
	cl_GameEventWrapper.def("InitCountDown", [](GameEventWrapper& cls_) { return cls_.InitCountDown(); });
	cl_GameEventWrapper.def("StartCountdownTimer", [](GameEventWrapper& cls_) { return cls_.StartCountdownTimer(); });
	cl_GameEventWrapper.def("AllowReadyUp2", [](GameEventWrapper& cls_) { return cls_.AllowReadyUp2(); });
	cl_GameEventWrapper.def("FindPlayerPRI", [](GameEventWrapper& cls_, SteamID & UniqueId) { return cls_.FindPlayerPRI(UniqueId); }, pybind11::arg("UniqueId"));
	cl_GameEventWrapper.def("HandlePlayerRemoved", [](GameEventWrapper& cls_, GameEventWrapper GameEvent, PriWrapper PRI) { return cls_.HandlePlayerRemoved(GameEvent, PRI); }, pybind11::arg("GameEvent"), pybind11::arg("PRI"));
	cl_GameEventWrapper.def("UpdateGameOwner", [](GameEventWrapper& cls_) { return cls_.UpdateGameOwner(); });
	cl_GameEventWrapper.def("SetGameOwner2", [](GameEventWrapper& cls_, PriWrapper NewOwner) { return cls_.SetGameOwner2(NewOwner); }, pybind11::arg("NewOwner"));
	cl_GameEventWrapper.def("__GameEvent_TA__SetAllowReadyUp", [](GameEventWrapper& cls_, PriWrapper P) { return cls_.__GameEvent_TA__SetAllowReadyUp(P); }, pybind11::arg("P"));
	cl_GameEventWrapper.def("__GameEvent_TA__CheckPlayersReady", [](GameEventWrapper& cls_, PriWrapper P) { return cls_.__GameEvent_TA__CheckPlayersReady(P); }, pybind11::arg("P"));
	cl_GameEventWrapper.def("__GameEvent_TA__CheckForBannedPlayers", [](GameEventWrapper& cls_, PriWrapper PRI) { return cls_.__GameEvent_TA__CheckForBannedPlayers(PRI); }, pybind11::arg("PRI"));
	cl_GameEventWrapper.def("__Pylon__ChangeNotifyFunc", [](GameEventWrapper& cls_) { return cls_.__Pylon__ChangeNotifyFunc(); });
	cl_GameEventWrapper.def("PlayerResetTraining", [](GameEventWrapper& cls_) { return cls_.PlayerResetTraining(); });
	cl_GameEventWrapper.def("SuppressModalDialogs", [](GameEventWrapper& cls_) { return cls_.SuppressModalDialogs(); });
	cl_GameEventWrapper.def("ShouldShowBallIndicator", [](GameEventWrapper& cls_) { return cls_.ShouldShowBallIndicator(); });
	cl_GameEventWrapper.def("CheckInitiatedForfeit", [](GameEventWrapper& cls_, PriWrapper PRI) { return cls_.CheckInitiatedForfeit(PRI); }, pybind11::arg("PRI"));
	cl_GameEventWrapper.def("CheckChatBanned", [](GameEventWrapper& cls_, PlayerControllerWrapper PC) { return cls_.CheckChatBanned(PC); }, pybind11::arg("PC"));
	cl_GameEventWrapper.def("FindPCForUniqueID", [](GameEventWrapper& cls_, SteamID & PlayerID) { return cls_.FindPCForUniqueID(PlayerID); }, pybind11::arg("PlayerID"));
	cl_GameEventWrapper.def("AllowSplitScreenPlayer", [](GameEventWrapper& cls_) { return cls_.AllowSplitScreenPlayer(); });
	cl_GameEventWrapper.def("AddPlayerChatMessage", [](GameEventWrapper& cls_, SteamID & PlayerID, unsigned char ChatChannel, TeamInfoWrapper Team, std::string Message) { return cls_.AddPlayerChatMessage(PlayerID, ChatChannel, Team, Message); }, pybind11::arg("PlayerID"), pybind11::arg("ChatChannel"), pybind11::arg("Team"), pybind11::arg("Message"));
	cl_GameEventWrapper.def("ConditionalStartSpectatorMatch", [](GameEventWrapper& cls_) { return cls_.ConditionalStartSpectatorMatch(); });
	cl_GameEventWrapper.def("IsPlayingTraining", [](GameEventWrapper& cls_) { return cls_.IsPlayingTraining(); });
	cl_GameEventWrapper.def("IsPlayingLan", [](GameEventWrapper& cls_) { return cls_.IsPlayingLan(); });
	cl_GameEventWrapper.def("IsPlayingOffline", [](GameEventWrapper& cls_) { return cls_.IsPlayingOffline(); });
	cl_GameEventWrapper.def("IsPlayingPrivate", [](GameEventWrapper& cls_) { return cls_.IsPlayingPrivate(); });
	cl_GameEventWrapper.def("IsPlayingPublic", [](GameEventWrapper& cls_) { return cls_.IsPlayingPublic(); });
	cl_GameEventWrapper.def("IsOnlineMultiplayer", [](GameEventWrapper& cls_) { return cls_.IsOnlineMultiplayer(); });
	cl_GameEventWrapper.def("CreateMatchType", [](GameEventWrapper& cls_, std::string Options) { return cls_.CreateMatchType(Options); }, pybind11::arg("Options"));
	cl_GameEventWrapper.def("AllPlayersSelectedTeam", [](GameEventWrapper& cls_) { return cls_.AllPlayersSelectedTeam(); });
	cl_GameEventWrapper.def("CanQueSaveReplay", [](GameEventWrapper& cls_) { return cls_.CanQueSaveReplay(); });
	cl_GameEventWrapper.def("ForceMatchStart", [](GameEventWrapper& cls_) { return cls_.ForceMatchStart(); });
	cl_GameEventWrapper.def("ConditionalStartMatch", [](GameEventWrapper& cls_) { return cls_.ConditionalStartMatch(); });
	cl_GameEventWrapper.def("SaveLocalPlayerStats", [](GameEventWrapper& cls_) { return cls_.SaveLocalPlayerStats(); });
	cl_GameEventWrapper.def("CanUseBallCam", [](GameEventWrapper& cls_) { return cls_.CanUseBallCam(); });
	cl_GameEventWrapper.def("HandleNextGame", [](GameEventWrapper& cls_) { return cls_.HandleNextGame(); });
	cl_GameEventWrapper.def("SetMaxPlayers2", [](GameEventWrapper& cls_, int InMaxPlayers) { return cls_.SetMaxPlayers2(InMaxPlayers); }, pybind11::arg("InMaxPlayers"));
	cl_GameEventWrapper.def("SetRestartingMatch", [](GameEventWrapper& cls_, long unsigned int bRestart) { return cls_.SetRestartingMatch(bRestart); }, pybind11::arg("bRestart"));
	cl_GameEventWrapper.def("ShouldBeFullScreen", [](GameEventWrapper& cls_) { return cls_.ShouldBeFullScreen(); });
	cl_GameEventWrapper.def("IsFinished", [](GameEventWrapper& cls_) { return cls_.IsFinished(); });
	cl_GameEventWrapper.def("OnAllPlayersReady", [](GameEventWrapper& cls_) { return cls_.OnAllPlayersReady(); });
	cl_GameEventWrapper.def("CheckPlayersReady2", [](GameEventWrapper& cls_) { return cls_.CheckPlayersReady2(); });
	cl_GameEventWrapper.def("SetAllowReadyUp2", [](GameEventWrapper& cls_, long unsigned int bAllow) { return cls_.SetAllowReadyUp2(bAllow); }, pybind11::arg("bAllow"));
	cl_GameEventWrapper.def("AutoReadyPlayers", [](GameEventWrapper& cls_) { return cls_.AutoReadyPlayers(); });
	cl_GameEventWrapper.def("ShouldAutoReadyUp", [](GameEventWrapper& cls_, PriWrapper PRI) { return cls_.ShouldAutoReadyUp(PRI); }, pybind11::arg("PRI"));
	//cl_GameEventWrapper.def("KickSplitscreenIdlers", [](GameEventWrapper& cls_) { return cls_.KickSplitscreenIdlers(); });
	//cl_GameEventWrapper.def("KickIdlers", [](GameEventWrapper& cls_) { return cls_.KickIdlers(); });
	//cl_GameEventWrapper.def("StopIdleKickTimer", [](GameEventWrapper& cls_) { return cls_.StopIdleKickTimer(); });
	//cl_GameEventWrapper.def("StartIdleKickTimer", [](GameEventWrapper& cls_, float OffsetTime) { return cls_.StartIdleKickTimer(OffsetTime); }, pybind11::arg("OffsetTime"));
	cl_GameEventWrapper.def("SendGoMessage", [](GameEventWrapper& cls_, PlayerControllerWrapper Player) { return cls_.SendGoMessage(Player); }, pybind11::arg("Player"));
	cl_GameEventWrapper.def("SendCountdownMessage", [](GameEventWrapper& cls_, int Seconds, PlayerControllerWrapper Player) { return cls_.SendCountdownMessage(Seconds, Player); }, pybind11::arg("Seconds"), pybind11::arg("Player"));
	cl_GameEventWrapper.def("BroadcastCountdownMessage", [](GameEventWrapper& cls_, int Seconds) { return cls_.BroadcastCountdownMessage(Seconds); }, pybind11::arg("Seconds"));
	cl_GameEventWrapper.def("BroadcastGoMessage", [](GameEventWrapper& cls_) { return cls_.BroadcastGoMessage(); });
	cl_GameEventWrapper.def("AllowShutdown", [](GameEventWrapper& cls_) { return cls_.AllowShutdown(); });
	cl_GameEventWrapper.def("GetRealDeltaTime", [](GameEventWrapper& cls_, float ElapsedTime) { return cls_.GetRealDeltaTime(ElapsedTime); }, pybind11::arg("ElapsedTime"));
	cl_GameEventWrapper.def("SetTimeDilation", [](GameEventWrapper& cls_, float NewTimeDilation) { return cls_.SetTimeDilation(NewTimeDilation); }, pybind11::arg("NewTimeDilation"));
	cl_GameEventWrapper.def("ClearRespawnList", [](GameEventWrapper& cls_) { return cls_.ClearRespawnList(); });
	cl_GameEventWrapper.def("ReplaceBotsWithAwaitingPlayers", [](GameEventWrapper& cls_) { return cls_.ReplaceBotsWithAwaitingPlayers(); });
	cl_GameEventWrapper.def("GetRespawnTime2", [](GameEventWrapper& cls_) { return cls_.GetRespawnTime2(); });
	cl_GameEventWrapper.def("RemoveCar", [](GameEventWrapper& cls_, CarWrapper Car) { return cls_.RemoveCar(Car); }, pybind11::arg("Car"));
	cl_GameEventWrapper.def("AddCar", [](GameEventWrapper& cls_, CarWrapper Car) { return cls_.AddCar(Car); }, pybind11::arg("Car"));
	cl_GameEventWrapper.def("TickRespawnTime", [](GameEventWrapper& cls_, float DeltaTime) { return cls_.TickRespawnTime(DeltaTime); }, pybind11::arg("DeltaTime"));
	cl_GameEventWrapper.def("SetBotSkill2", [](GameEventWrapper& cls_, float NewSkill) { return cls_.SetBotSkill2(NewSkill); }, pybind11::arg("NewSkill"));
	cl_GameEventWrapper.def("GetLocalPrimaryPlayer", [](GameEventWrapper& cls_) { return cls_.GetLocalPrimaryPlayer(); });
	cl_GameEventWrapper.def("HasPlayerNamed", [](GameEventWrapper& cls_, std::string PlayerName) { return cls_.HasPlayerNamed(PlayerName); }, pybind11::arg("PlayerName"));
	cl_GameEventWrapper.def("RandomizeBots", [](GameEventWrapper& cls_) { return cls_.RandomizeBots(); });
	cl_GameEventWrapper.def("MoveToGround", [](GameEventWrapper& cls_, ActorWrapper Mover, float HeightCheck) { return cls_.MoveToGround(Mover, HeightCheck); }, pybind11::arg("Mover"), pybind11::arg("HeightCheck"));
	cl_GameEventWrapper.def("SetAllDriving", [](GameEventWrapper& cls_, long unsigned int bDriving) { return cls_.SetAllDriving(bDriving); }, pybind11::arg("bDriving"));
	cl_GameEventWrapper.def("OnFinished", [](GameEventWrapper& cls_) { return cls_.OnFinished(); });
	cl_GameEventWrapper.def("StartCountDown", [](GameEventWrapper& cls_) { return cls_.StartCountDown(); });
	cl_GameEventWrapper.def("StartInitialCountDown", [](GameEventWrapper& cls_) { return cls_.StartInitialCountDown(); });
	cl_GameEventWrapper.def("OnGameStateTimeLapsed", [](GameEventWrapper& cls_) { return cls_.OnGameStateTimeLapsed(); });
	cl_GameEventWrapper.def("OnGameStateTimeUpdated", [](GameEventWrapper& cls_) { return cls_.OnGameStateTimeUpdated(); });
	cl_GameEventWrapper.def("UpdateGameStateTime", [](GameEventWrapper& cls_) { return cls_.UpdateGameStateTime(); });
	cl_GameEventWrapper.def("SetGameStateTimeRemaining2", [](GameEventWrapper& cls_, int StateTime, long unsigned int bFromReplication) { return cls_.SetGameStateTimeRemaining2(StateTime, bFromReplication); }, pybind11::arg("StateTime"), pybind11::arg("bFromReplication"));
	cl_GameEventWrapper.def("SetGameStateTime2", [](GameEventWrapper& cls_, int StateTime) { return cls_.SetGameStateTime2(StateTime); }, pybind11::arg("StateTime"));
	cl_GameEventWrapper.def("OnPlayerRestarted", [](GameEventWrapper& cls_, CarWrapper PlayerCar) { return cls_.OnPlayerRestarted(PlayerCar); }, pybind11::arg("PlayerCar"));
	cl_GameEventWrapper.def("TeleportCar", [](GameEventWrapper& cls_, CarWrapper PlayerCar) { return cls_.TeleportCar(PlayerCar); }, pybind11::arg("PlayerCar"));
	cl_GameEventWrapper.def("OnCarSpawned", [](GameEventWrapper& cls_, CarWrapper NewCar) { return cls_.OnCarSpawned(NewCar); }, pybind11::arg("NewCar"));
	cl_GameEventWrapper.def("SpotIsEncroached", [](GameEventWrapper& cls_, Vector & Spot) { return cls_.SpotIsEncroached(Spot); }, pybind11::arg("Spot"));
	cl_GameEventWrapper.def("RandomizeSpawnPoints", [](GameEventWrapper& cls_) { return cls_.RandomizeSpawnPoints(); });
	cl_GameEventWrapper.def("RestartPlayers", [](GameEventWrapper& cls_) { return cls_.RestartPlayers(); });
	cl_GameEventWrapper.def("RemoveLocalPlayer", [](GameEventWrapper& cls_, PlayerControllerWrapper Player) { return cls_.RemoveLocalPlayer(Player); }, pybind11::arg("Player"));
	cl_GameEventWrapper.def("AddLocalPlayer", [](GameEventWrapper& cls_, PlayerControllerWrapper Player) { return cls_.AddLocalPlayer(Player); }, pybind11::arg("Player"));
	cl_GameEventWrapper.def("RemovePRI", [](GameEventWrapper& cls_, PriWrapper PRI) { return cls_.RemovePRI(PRI); }, pybind11::arg("PRI"));
	cl_GameEventWrapper.def("AddPRI", [](GameEventWrapper& cls_, PriWrapper PRI) { return cls_.AddPRI(PRI); }, pybind11::arg("PRI"));
	cl_GameEventWrapper.def("AddForfeitInitiator", [](GameEventWrapper& cls_, SteamID & PlayerID) { return cls_.AddForfeitInitiator(PlayerID); }, pybind11::arg("PlayerID"));
	cl_GameEventWrapper.def("BanPlayerID", [](GameEventWrapper& cls_, SteamID & PlayerID) { return cls_.BanPlayerID(PlayerID); }, pybind11::arg("PlayerID"));
	cl_GameEventWrapper.def("GetMaxHumans", [](GameEventWrapper& cls_) { return cls_.GetMaxHumans(); });
	cl_GameEventWrapper.def("GetNumHumans", [](GameEventWrapper& cls_) { return cls_.GetNumHumans(); });
	cl_GameEventWrapper.def("FindBotReplacement", [](GameEventWrapper& cls_, PriWrapper PRI) { return cls_.FindBotReplacement(PRI); }, pybind11::arg("PRI"));
	cl_GameEventWrapper.def("UpdateBotCount", [](GameEventWrapper& cls_) { return cls_.UpdateBotCount(); });
	cl_GameEventWrapper.def("TimerUpdateBotCount", [](GameEventWrapper& cls_) { return cls_.TimerUpdateBotCount(); });
	cl_GameEventWrapper.def("InitBotSkill", [](GameEventWrapper& cls_) { return cls_.InitBotSkill(); });
	cl_GameEventWrapper.def("InitMutators", [](GameEventWrapper& cls_) { return cls_.InitMutators(); });
	cl_GameEventWrapper.def("HandleFinished", [](GameEventWrapper& cls_, GameEventWrapper GameEvent) { return cls_.HandleFinished(GameEvent); }, pybind11::arg("GameEvent"));
	cl_GameEventWrapper.def("Init2", [](GameEventWrapper& cls_, PlayerControllerWrapper InActivator) { return cls_.Init2(InActivator); }, pybind11::arg("InActivator"));
	cl_GameEventWrapper.def("eventInitGame", [](GameEventWrapper& cls_, std::string Options) { return cls_.eventInitGame(Options); }, pybind11::arg("Options"));
	cl_GameEventWrapper.def("OnGameStateChanged", [](GameEventWrapper& cls_) { return cls_.OnGameStateChanged(); });
	cl_GameEventWrapper.def("OnCanVoteForfeitChanged", [](GameEventWrapper& cls_) { return cls_.OnCanVoteForfeitChanged(); });
	cl_GameEventWrapper.def("UpdateCanVoteToForfeit", [](GameEventWrapper& cls_) { return cls_.UpdateCanVoteToForfeit(); });
	cl_GameEventWrapper.def("ShouldAllowVoteToForfeit", [](GameEventWrapper& cls_) { return cls_.ShouldAllowVoteToForfeit(); });
	cl_GameEventWrapper.def("OnPenaltyChanged", [](GameEventWrapper& cls_) { return cls_.OnPenaltyChanged(); });
	cl_GameEventWrapper.def("UpdateLeaveMatchPenalty", [](GameEventWrapper& cls_) { return cls_.UpdateLeaveMatchPenalty(); });
	cl_GameEventWrapper.def("GetPlaylist", [](GameEventWrapper& cls_) { return cls_.GetPlaylist(); });
	cl_GameEventWrapper.def("ShouldHaveLeaveMatchPenalty", [](GameEventWrapper& cls_) { return cls_.ShouldHaveLeaveMatchPenalty(); });
	cl_GameEventWrapper.def("OnMatchSettingsChanged", [](GameEventWrapper& cls_) { return cls_.OnMatchSettingsChanged(); });
	cl_GameEventWrapper.def("ClearGameScoreFromCustomSettings", [](GameEventWrapper& cls_) { return cls_.ClearGameScoreFromCustomSettings(); });
	cl_GameEventWrapper.def("EventPlayerResetTraining", [](GameEventWrapper& cls_, GameEventWrapper GameEvent) { return cls_.EventPlayerResetTraining(GameEvent); }, pybind11::arg("GameEvent"));
}