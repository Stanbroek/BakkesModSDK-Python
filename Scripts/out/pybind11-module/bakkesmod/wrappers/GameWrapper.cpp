void bind_GameWrapper(pybind11::module& m)
{

	pybind11::class_<GameWrapper, std::shared_ptr<GameWrapper>> cl_GameWrapper(m, "GameWrapper");
	cl_GameWrapper.def(pybind11::init<uintptr_t, long int, std::type_index>(), pybind11::arg("mem"), pybind11::arg("pluginType"), pybind11::arg("idx"));
	cl_GameWrapper.def(pybind11::init<GameWrapper const &>(), pybind11::arg("other"));
	// cl_GameWrapper.def(pybind11::del<>());
	cl_GameWrapper.def("IsInGame", [](GameWrapper& cls_) { return cls_.IsInGame(); });
	cl_GameWrapper.def("IsInOnlineGame", [](GameWrapper& cls_) { return cls_.IsInOnlineGame(); });
	cl_GameWrapper.def("IsInFreeplay", [](GameWrapper& cls_) { return cls_.IsInFreeplay(); });
	cl_GameWrapper.def("IsInReplay", [](GameWrapper& cls_) { return cls_.IsInReplay(); });
	cl_GameWrapper.def("IsInCustomTraining", [](GameWrapper& cls_) { return cls_.IsInCustomTraining(); });
	cl_GameWrapper.def("IsSpectatingInOnlineGame", [](GameWrapper& cls_) { return cls_.IsSpectatingInOnlineGame(); });
	cl_GameWrapper.def("IsPaused", [](GameWrapper& cls_) { return cls_.IsPaused(); });
	cl_GameWrapper.def("IsUsingEpicVersion", [](GameWrapper& cls_) { return cls_.IsUsingEpicVersion(); });
	cl_GameWrapper.def("IsUsingSteamVersion", [](GameWrapper& cls_) { return cls_.IsUsingSteamVersion(); });
	cl_GameWrapper.def("GetSteamVersion", [](GameWrapper& cls_) { return cls_.GetSteamVersion(); });
	cl_GameWrapper.def("GetPsyBuildID", [](GameWrapper& cls_) { return cls_.GetPsyBuildID(); });
	cl_GameWrapper.def("GetCurrentGameState", [](GameWrapper& cls_) { return cls_.GetCurrentGameState(); });
	cl_GameWrapper.def("GetOnlineGame", [](GameWrapper& cls_) { return cls_.GetOnlineGame(); });
	cl_GameWrapper.def("GetGameEventAsServer", [](GameWrapper& cls_) { return cls_.GetGameEventAsServer(); });
	cl_GameWrapper.def("GetGameEventAsReplay", [](GameWrapper& cls_) { return cls_.GetGameEventAsReplay(); });
	cl_GameWrapper.def("GetMMRWrapper", [](GameWrapper& cls_) { return cls_.GetMMRWrapper(); });
	cl_GameWrapper.def("GetLocalCar", [](GameWrapper& cls_) { return cls_.GetLocalCar(); });
	cl_GameWrapper.def("GetCamera", [](GameWrapper& cls_) { return cls_.GetCamera(); });
	cl_GameWrapper.def("GetEngine", [](GameWrapper& cls_) { return cls_.GetEngine(); });
	cl_GameWrapper.def("GetPluginManager", [](GameWrapper& cls_) { return cls_.GetPluginManager(); });
	//cl_GameWrapper.def("GetGUIManager", [](GameWrapper& cls_) { return cls_.GetGUIManager(); });
	cl_GameWrapper.def("GetPlayerController", [](GameWrapper& cls_) { return cls_.GetPlayerController(); });
	cl_GameWrapper.def("GetItemsWrapper", [](GameWrapper& cls_) { return cls_.GetItemsWrapper(); });
	cl_GameWrapper.def("GetMatchmakingWrapper", [](GameWrapper& cls_) { return cls_.GetMatchmakingWrapper(); });
	cl_GameWrapper.def("GetSettings", [](GameWrapper& cls_) { return cls_.GetSettings(); });
	cl_GameWrapper.def("CreateModal", [](GameWrapper& cls_, std::string const & title) { return cls_.CreateModal(title); }, pybind11::arg("title"));
	cl_GameWrapper.def("CreateTextInputModal", [](GameWrapper& cls_, std::string const & title) { return cls_.CreateTextInputModal(title); }, pybind11::arg("title"));
	cl_GameWrapper.def("OverrideParams", [](GameWrapper& cls_, void * src, size_t memsize) { return cls_.OverrideParams(src, memsize); }, pybind11::arg("src"), pybind11::arg("memsize"));
	//cl_GameWrapper.def("SetTimeout", [](GameWrapper& cls_, std::function<void (GameWrapper *)> theLambda, float time) { return cls_.SetTimeout(theLambda, time); }, pybind11::arg("theLambda"), pybind11::arg("time"));
	
	cl_GameWrapper.def("SetTimeout",
		[](GameWrapper& cls_, std::function<void (GameWrapper *)> theLambda, float time) {
			return cls_.SetTimeout([=](GameWrapper* gw) { CATCH_PYTHON_EXCEPTIONS(theLambda(gw);) }, time);
		}, pybind11::arg("theLambda"), pybind11::arg("time"));

	//cl_GameWrapper.def("Execute", [](GameWrapper& cls_, std::function<void (GameWrapper *)> theLambda) { return cls_.Execute(theLambda); }, pybind11::arg("theLambda"));
	
	cl_GameWrapper.def("Execute",
		[](GameWrapper& cls_, std::function<void (GameWrapper *)> theLambda) {
			return cls_.Execute([=](GameWrapper* gw) { CATCH_PYTHON_EXCEPTIONS(theLambda(gw);) });
		}, pybind11::arg("theLambda"));

	//cl_GameWrapper.def("RegisterDrawable", [](GameWrapper& cls_, std::function<void (CanvasWrapper)> callback) { return cls_.RegisterDrawable(callback); }, pybind11::arg("callback"));
	
	cl_GameWrapper.def("RegisterDrawable",
		[](GameWrapper& cls_, std::function<void (CanvasWrapper)> callback) {
			return cls_.RegisterDrawable([=](CanvasWrapper cw) { CATCH_PYTHON_EXCEPTIONS(callback(cw);) });
		}, pybind11::arg("callback"));

	cl_GameWrapper.def("UnregisterDrawables", [](GameWrapper& cls_) { return cls_.UnregisterDrawables(); });
	cl_GameWrapper.def("GetFNameByIndex", [](GameWrapper& cls_, int index) { return cls_.GetFNameByIndex(index); }, pybind11::arg("index"));
	cl_GameWrapper.def("GetFNameIndexByString", [](GameWrapper& cls_, std::string name) { return cls_.GetFNameIndexByString(name); }, pybind11::arg("name"));
	//cl_GameWrapper.def("HookEvent", [](GameWrapper& cls_, std::string eventName, std::function<void (std::basic_string<char>)> callback) { return cls_.HookEvent(eventName, callback); }, pybind11::arg("eventName"), pybind11::arg("callback"));
	
	cl_GameWrapper.def("HookEvent",
		[](GameWrapper& cls_, std::string eventName, std::function<void (std::basic_string<char>)> callback) {
			return cls_.HookEvent(eventName, [=](std::basic_string<char> str) { CATCH_PYTHON_EXCEPTIONS(callback(str);) });
		}, pybind11::arg("eventName"), pybind11::arg("callback"));

	cl_GameWrapper.def("UnhookEvent", [](GameWrapper& cls_, std::string eventName) { return cls_.UnhookEvent(eventName); }, pybind11::arg("eventName"));
	//cl_GameWrapper.def("HookEventPost", [](GameWrapper& cls_, std::string eventName, std::function<void (std::basic_string<char>)> callback) { return cls_.HookEventPost(eventName, callback); }, pybind11::arg("eventName"), pybind11::arg("callback"));

	cl_GameWrapper.def("HookEventPost",
		[](GameWrapper& cls_, std::string eventName, std::function<void(std::basic_string<char>)> callback) {
			return cls_.HookEventPost(eventName, [=](std::basic_string<char> str) { CATCH_PYTHON_EXCEPTIONS(callback(str);) });
		}, pybind11::arg("eventName"), pybind11::arg("callback"));

	cl_GameWrapper.def("UnhookEventPost", [](GameWrapper& cls_, std::string eventName) { return cls_.UnhookEventPost(eventName); }, pybind11::arg("eventName"));
	cl_GameWrapper.def("LogToChatbox", [](GameWrapper& cls_, std::string text, std::string sender="BAKKESMOD") { return cls_.LogToChatbox(text, sender); }, pybind11::arg("text"), pybind11::arg("sender"));
	cl_GameWrapper.def("LoadToastTexture", [](GameWrapper& cls_, std::string name, std::string path) { return cls_.LoadToastTexture(name, path); }, pybind11::arg("name"), pybind11::arg("path"));
	cl_GameWrapper.def("LoadToastTexture", [](GameWrapper& cls_, std::string name, std::wstring path) { return cls_.LoadToastTexture(name, path); }, pybind11::arg("name"), pybind11::arg("path"));
	cl_GameWrapper.def("Toast", [](GameWrapper& cls_, std::string title, std::string text, std::string texture="default", float timeout=3.5F, uint8_t toastType=0, float width=290.F, float height=60.F) { return cls_.Toast(title, text, texture, timeout, toastType, width, height); }, pybind11::arg("title"), pybind11::arg("text"), pybind11::arg("texture"), pybind11::arg("timeout"), pybind11::arg("toastType"), pybind11::arg("width"), pybind11::arg("height"));
	cl_GameWrapper.def("IsKeyPressed", [](GameWrapper& cls_, int keyName) { return cls_.IsKeyPressed(keyName); }, pybind11::arg("keyName"));
	cl_GameWrapper.def("IsCursorVisible", [](GameWrapper& cls_) { return cls_.IsCursorVisible(); });
	cl_GameWrapper.def("ExecuteUnrealCommand", [](GameWrapper& cls_, std::string command) { return cls_.ExecuteUnrealCommand(command); }, pybind11::arg("command"));
	cl_GameWrapper.def("GetRandomMap", [](GameWrapper& cls_) { return cls_.GetRandomMap(); });
	cl_GameWrapper.def("GetCurrentMap", [](GameWrapper& cls_) { return cls_.GetCurrentMap(); });
	cl_GameWrapper.def("GetSteamID", [](GameWrapper& cls_) { return cls_.GetSteamID(); });
	cl_GameWrapper.def("GetEpicID", [](GameWrapper& cls_) { return cls_.GetEpicID(); });
	cl_GameWrapper.def("GetUniqueID", [](GameWrapper& cls_) { return cls_.GetUniqueID(); });
	cl_GameWrapper.def("GetPlayerName", [](GameWrapper& cls_) { return cls_.GetPlayerName(); });
	cl_GameWrapper.def("GetLocalClub", [](GameWrapper& cls_) { return cls_.GetLocalClub(); });
	cl_GameWrapper.def("GetMainSequence", [](GameWrapper& cls_) { return cls_.GetMainSequence(); });
	// [deprecated] cl_GameWrapper.def("SetBotLoadout", [](GameWrapper& cls_, PriWrapper & bot_pri, BotLoadoutData const & loadout_data) { return cls_.SetBotLoadout(bot_pri, loadout_data); }, pybind11::arg("bot_pri"), pybind11::arg("loadout_data"));
	cl_GameWrapper.def("GetScreenSize", [](GameWrapper& cls_) { return cls_.GetScreenSize(); });
	cl_GameWrapper.def("GetSafeZoneRatio", [](GameWrapper& cls_) { return cls_.GetSafeZoneRatio(); });
	cl_GameWrapper.def("GetUIScale", [](GameWrapper& cls_) { return cls_.GetUIScale(); });
	cl_GameWrapper.def("GetbMetric", [](GameWrapper& cls_) { return cls_.GetbMetric(); });
	cl_GameWrapper.def("GetUILanguage", [](GameWrapper& cls_) { return cls_.GetUILanguage(); });
	cl_GameWrapper.def("GetbColorBlind", [](GameWrapper& cls_) { return cls_.GetbColorBlind(); });
	cl_GameWrapper.def("GetBakkesModPathW", [](GameWrapper& cls_) { return cls_.GetBakkesModPathW(); });
	cl_GameWrapper.def("GetDataFolderW", [](GameWrapper& cls_) { return cls_.GetDataFolderW(); });
	cl_GameWrapper.def("GetBakkesModVersion", [](GameWrapper& cls_) { return cls_.GetBakkesModVersion(); });
	cl_GameWrapper.def("PlayReplay", [](GameWrapper& cls_, std::wstring const & path) { return cls_.PlayReplay(path); }, pybind11::arg("path"));
	cl_GameWrapper.def("HookEventWithCaller", [](GameWrapper& cls_, std::string eventName, std::function<void (ServerWrapper, void *, std::basic_string<char>)> callback) { return cls_.HookEventWithCaller(eventName, callback); }, pybind11::arg("eventName"), pybind11::arg("callback"));
	cl_GameWrapper.def("HookEventWithCaller", [](GameWrapper& cls_, std::string eventName, std::function<void (ActorWrapper, void *, std::basic_string<char>)> callback) { return cls_.HookEventWithCaller(eventName, callback); }, pybind11::arg("eventName"), pybind11::arg("callback"));
	cl_GameWrapper.def("HookEventWithCaller", [](GameWrapper& cls_, std::string eventName, std::function<void (CarWrapper, void *, std::basic_string<char>)> callback) { return cls_.HookEventWithCaller(eventName, callback); }, pybind11::arg("eventName"), pybind11::arg("callback"));
	cl_GameWrapper.def("HookEventWithCaller", [](GameWrapper& cls_, std::string eventName, std::function<void (CarComponentWrapper, void *, std::basic_string<char>)> callback) { return cls_.HookEventWithCaller(eventName, callback); }, pybind11::arg("eventName"), pybind11::arg("callback"));
	cl_GameWrapper.def("HookEventWithCaller", [](GameWrapper& cls_, std::string eventName, std::function<void (PlayerControllerWrapper, void *, std::basic_string<char>)> callback) { return cls_.HookEventWithCaller(eventName, callback); }, pybind11::arg("eventName"), pybind11::arg("callback"));
	cl_GameWrapper.def("HookEventWithCaller", [](GameWrapper& cls_, std::string eventName, std::function<void (BallWrapper, void *, std::basic_string<char>)> callback) { return cls_.HookEventWithCaller(eventName, callback); }, pybind11::arg("eventName"), pybind11::arg("callback"));
	cl_GameWrapper.def("HookEventWithCallerPost", [](GameWrapper& cls_, std::string eventName, std::function<void (ActorWrapper, void *, std::basic_string<char>)> callback) { return cls_.HookEventWithCallerPost(eventName, callback); }, pybind11::arg("eventName"), pybind11::arg("callback"));
	cl_GameWrapper.def("HookEventWithCallerPost", [](GameWrapper& cls_, std::string eventName, std::function<void (ServerWrapper, void *, std::basic_string<char>)> callback) { return cls_.HookEventWithCallerPost(eventName, callback); }, pybind11::arg("eventName"), pybind11::arg("callback"));
	cl_GameWrapper.def("HookEventWithCallerPost", [](GameWrapper& cls_, std::string eventName, std::function<void (CarWrapper, void *, std::basic_string<char>)> callback) { return cls_.HookEventWithCallerPost(eventName, callback); }, pybind11::arg("eventName"), pybind11::arg("callback"));
	cl_GameWrapper.def("HookEventWithCallerPost", [](GameWrapper& cls_, std::string eventName, std::function<void (CarComponentWrapper, void *, std::basic_string<char>)> callback) { return cls_.HookEventWithCallerPost(eventName, callback); }, pybind11::arg("eventName"), pybind11::arg("callback"));
	cl_GameWrapper.def("HookEventWithCallerPost", [](GameWrapper& cls_, std::string eventName, std::function<void (PlayerControllerWrapper, void *, std::basic_string<char>)> callback) { return cls_.HookEventWithCallerPost(eventName, callback); }, pybind11::arg("eventName"), pybind11::arg("callback"));
	cl_GameWrapper.def("HookEventWithCallerPost", [](GameWrapper& cls_, std::string eventName, std::function<void (BallWrapper, void *, std::basic_string<char>)> callback) { return cls_.HookEventWithCallerPost(eventName, callback); }, pybind11::arg("eventName"), pybind11::arg("callback"));
	//cl_GameWrapper.def_property("pimpl", [](const GameWrapper& cls_) { return cls_.pimpl; }, [](GameWrapper& cls_, std::unique_ptr<GameWrapper::Impl, std::default_delete<GameWrapper::Impl> > const& prop_) { cls_.pimpl = prop_; });
}
