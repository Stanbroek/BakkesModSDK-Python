void bind_GameSettingPlaylistWrapper(pybind11::module& m)
{

	pybind11::class_<GameSettingPlaylistWrapper, std::shared_ptr<GameSettingPlaylistWrapper>, ObjectWrapper> cl_GameSettingPlaylistWrapper(m, "GameSettingPlaylistWrapper");
	cl_GameSettingPlaylistWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_GameSettingPlaylistWrapper.def(pybind11::init<GameSettingPlaylistWrapper const &>(), pybind11::arg("other"));
	// cl_GameSettingPlaylistWrapper.def(pybind11::del<>());
	cl_GameSettingPlaylistWrapper.def("IsNull", [](GameSettingPlaylistWrapper& cls_) { return cls_.IsNull(); });
	cl_GameSettingPlaylistWrapper.def("GetTitle", [](GameSettingPlaylistWrapper& cls_) { return cls_.GetTitle(); });
	cl_GameSettingPlaylistWrapper.def("GetDescription", [](GameSettingPlaylistWrapper& cls_) { return cls_.GetDescription(); });
	cl_GameSettingPlaylistWrapper.def("GetPlayerCount", [](GameSettingPlaylistWrapper& cls_) { return cls_.GetPlayerCount(); });
	cl_GameSettingPlaylistWrapper.def("SetPlayerCount", [](GameSettingPlaylistWrapper& cls_, int newPlayerCount) { return cls_.SetPlayerCount(newPlayerCount); }, pybind11::arg("newPlayerCount"));
	cl_GameSettingPlaylistWrapper.def("GetbStandard", [](GameSettingPlaylistWrapper& cls_) { return cls_.GetbStandard(); });
	cl_GameSettingPlaylistWrapper.def("SetbStandard", [](GameSettingPlaylistWrapper& cls_, long unsigned int newbStandard) { return cls_.SetbStandard(newbStandard); }, pybind11::arg("newbStandard"));
	cl_GameSettingPlaylistWrapper.def("GetbRanked", [](GameSettingPlaylistWrapper& cls_) { return cls_.GetbRanked(); });
	cl_GameSettingPlaylistWrapper.def("SetbRanked", [](GameSettingPlaylistWrapper& cls_, long unsigned int newbRanked) { return cls_.SetbRanked(newbRanked); }, pybind11::arg("newbRanked"));
	cl_GameSettingPlaylistWrapper.def("GetbSolo", [](GameSettingPlaylistWrapper& cls_) { return cls_.GetbSolo(); });
	cl_GameSettingPlaylistWrapper.def("SetbSolo", [](GameSettingPlaylistWrapper& cls_, long unsigned int newbSolo) { return cls_.SetbSolo(newbSolo); }, pybind11::arg("newbSolo"));
	cl_GameSettingPlaylistWrapper.def("GetbNew", [](GameSettingPlaylistWrapper& cls_) { return cls_.GetbNew(); });
	cl_GameSettingPlaylistWrapper.def("SetbNew", [](GameSettingPlaylistWrapper& cls_, long unsigned int newbNew) { return cls_.SetbNew(newbNew); }, pybind11::arg("newbNew"));
	cl_GameSettingPlaylistWrapper.def("GetbApplyQuitPenalty", [](GameSettingPlaylistWrapper& cls_) { return cls_.GetbApplyQuitPenalty(); });
	cl_GameSettingPlaylistWrapper.def("SetbApplyQuitPenalty", [](GameSettingPlaylistWrapper& cls_, long unsigned int newbApplyQuitPenalty) { return cls_.SetbApplyQuitPenalty(newbApplyQuitPenalty); }, pybind11::arg("newbApplyQuitPenalty"));
	cl_GameSettingPlaylistWrapper.def("GetbAllowForfeit", [](GameSettingPlaylistWrapper& cls_) { return cls_.GetbAllowForfeit(); });
	cl_GameSettingPlaylistWrapper.def("SetbAllowForfeit", [](GameSettingPlaylistWrapper& cls_, long unsigned int newbAllowForfeit) { return cls_.SetbAllowForfeit(newbAllowForfeit); }, pybind11::arg("newbAllowForfeit"));
	cl_GameSettingPlaylistWrapper.def("GetbDisableRankedReconnect", [](GameSettingPlaylistWrapper& cls_) { return cls_.GetbDisableRankedReconnect(); });
	cl_GameSettingPlaylistWrapper.def("SetbDisableRankedReconnect", [](GameSettingPlaylistWrapper& cls_, long unsigned int newbDisableRankedReconnect) { return cls_.SetbDisableRankedReconnect(newbDisableRankedReconnect); }, pybind11::arg("newbDisableRankedReconnect"));
	cl_GameSettingPlaylistWrapper.def("GetbIgnoreAssignTeams", [](GameSettingPlaylistWrapper& cls_) { return cls_.GetbIgnoreAssignTeams(); });
	cl_GameSettingPlaylistWrapper.def("SetbIgnoreAssignTeams", [](GameSettingPlaylistWrapper& cls_, long unsigned int newbIgnoreAssignTeams) { return cls_.SetbIgnoreAssignTeams(newbIgnoreAssignTeams); }, pybind11::arg("newbIgnoreAssignTeams"));
	cl_GameSettingPlaylistWrapper.def("GetbKickOnMigrate", [](GameSettingPlaylistWrapper& cls_) { return cls_.GetbKickOnMigrate(); });
	cl_GameSettingPlaylistWrapper.def("SetbKickOnMigrate", [](GameSettingPlaylistWrapper& cls_, long unsigned int newbKickOnMigrate) { return cls_.SetbKickOnMigrate(newbKickOnMigrate); }, pybind11::arg("newbKickOnMigrate"));
	cl_GameSettingPlaylistWrapper.def("GetbAllowClubs", [](GameSettingPlaylistWrapper& cls_) { return cls_.GetbAllowClubs(); });
	cl_GameSettingPlaylistWrapper.def("SetbAllowClubs", [](GameSettingPlaylistWrapper& cls_, long unsigned int newbAllowClubs) { return cls_.SetbAllowClubs(newbAllowClubs); }, pybind11::arg("newbAllowClubs"));
	cl_GameSettingPlaylistWrapper.def("GetbPlayersVSBots", [](GameSettingPlaylistWrapper& cls_) { return cls_.GetbPlayersVSBots(); });
	cl_GameSettingPlaylistWrapper.def("SetbPlayersVSBots", [](GameSettingPlaylistWrapper& cls_, long unsigned int newbPlayersVSBots) { return cls_.SetbPlayersVSBots(newbPlayersVSBots); }, pybind11::arg("newbPlayersVSBots"));
	cl_GameSettingPlaylistWrapper.def("GetPlaylistId", [](GameSettingPlaylistWrapper& cls_) { return cls_.GetPlaylistId(); });
	cl_GameSettingPlaylistWrapper.def("SetPlaylistId", [](GameSettingPlaylistWrapper& cls_, int newPlaylistId) { return cls_.SetPlaylistId(newPlaylistId); }, pybind11::arg("newPlaylistId"));
	cl_GameSettingPlaylistWrapper.def("GetServerCommand", [](GameSettingPlaylistWrapper& cls_) { return cls_.GetServerCommand(); });
	cl_GameSettingPlaylistWrapper.def("IsLanMatch", [](GameSettingPlaylistWrapper& cls_) { return cls_.IsLanMatch(); });
	cl_GameSettingPlaylistWrapper.def("IsPrivateMatch", [](GameSettingPlaylistWrapper& cls_) { return cls_.IsPrivateMatch(); });
	cl_GameSettingPlaylistWrapper.def("ShouldUpdateSkills", [](GameSettingPlaylistWrapper& cls_) { return cls_.ShouldUpdateSkills(); });
	cl_GameSettingPlaylistWrapper.def("IsValidID", [](GameSettingPlaylistWrapper& cls_, int InPlaylistID) { return cls_.IsValidID(InPlaylistID); }, pybind11::arg("InPlaylistID"));
	cl_GameSettingPlaylistWrapper.def("IsValid2", [](GameSettingPlaylistWrapper& cls_) { return cls_.IsValid2(); });
}
