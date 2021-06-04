void bind_mmrwrapper(pybind11::module& m)
{

	pybind11::class_<MMRWrapper, std::shared_ptr<MMRWrapper>, ObjectWrapper> cl_MMRWrapper(m, "MMRWrapper");
	cl_MMRWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_MMRWrapper.def(pybind11::init<MMRWrapper const &>(), pybind11::arg("other"));
	// cl_MMRWrapper.def(pybind11::del<>());
	cl_MMRWrapper.def("IsSyncing", [](MMRWrapper& cls_, UniqueIDWrapper playerID) { return cls_.IsSyncing(playerID); }, pybind11::arg("playerID"));
	cl_MMRWrapper.def("IsSyncing", [](MMRWrapper& cls_, SteamID playerID) { return cls_.IsSyncing(playerID); }, pybind11::arg("playerID"));
	cl_MMRWrapper.def("IsSynced", [](MMRWrapper& cls_, UniqueIDWrapper playerID, int playlistID) { return cls_.IsSynced(playerID, playlistID); }, pybind11::arg("playerID"), pybind11::arg("playlistID"));
	cl_MMRWrapper.def("IsSynced", [](MMRWrapper& cls_, SteamID playerID, int playlistID) { return cls_.IsSynced(playerID, playlistID); }, pybind11::arg("playerID"), pybind11::arg("playlistID"));
	cl_MMRWrapper.def("IsRanked", [](MMRWrapper& cls_, int playlistID) { return cls_.IsRanked(playlistID); }, pybind11::arg("playlistID"));
	cl_MMRWrapper.def("GetPlayerSkillRating", [](MMRWrapper& cls_, UniqueIDWrapper playerID, int playlistID) { return cls_.GetPlayerSkillRating(playerID, playlistID); }, pybind11::arg("playerID"), pybind11::arg("playlistID"));
	cl_MMRWrapper.def("GetPlayerRank", [](MMRWrapper& cls_, UniqueIDWrapper playerID, int playlistID) { return cls_.GetPlayerRank(playerID, playlistID); }, pybind11::arg("playerID"), pybind11::arg("playlistID"));
	cl_MMRWrapper.def("GetPlayerMMR", [](MMRWrapper& cls_, UniqueIDWrapper playerID, int playlistID) { return cls_.GetPlayerMMR(playerID, playlistID); }, pybind11::arg("playerID"), pybind11::arg("playlistID"));
	cl_MMRWrapper.def("GetPlayerSkillRating", [](MMRWrapper& cls_, SteamID playerID, int playlistID) { return cls_.GetPlayerSkillRating(playerID, playlistID); }, pybind11::arg("playerID"), pybind11::arg("playlistID"));
	cl_MMRWrapper.def("GetPlayerRank", [](MMRWrapper& cls_, SteamID playerID, int playlistID) { return cls_.GetPlayerRank(playerID, playlistID); }, pybind11::arg("playerID"), pybind11::arg("playlistID"));
	cl_MMRWrapper.def("GetPlayerMMR", [](MMRWrapper& cls_, SteamID playerID, int playlistID) { return cls_.GetPlayerMMR(playerID, playlistID); }, pybind11::arg("playerID"), pybind11::arg("playlistID"));
	cl_MMRWrapper.def("CalculateMMR", [](MMRWrapper& cls_, SkillRating sr, bool disregardPlacements) { return cls_.CalculateMMR(sr, disregardPlacements); }, pybind11::arg("sr"), pybind11::arg("disregardPlacements"));
	cl_MMRWrapper.def("GetCurrentPlaylist", [](MMRWrapper& cls_) { return cls_.GetCurrentPlaylist(); });
	cl_MMRWrapper.def("RegisterMMRNotifier", [](MMRWrapper& cls_, std::function<void (UniqueIDWrapper)> arg0) { return cls_.RegisterMMRNotifier(arg0); }, pybind11::arg("arg0"));

	pybind11::class_<MMRNotifierToken, std::shared_ptr<MMRNotifierToken>> cl_MMRNotifierToken(m, "MMRNotifierToken");
	// cl_MMRNotifierToken.def(pybind11::del<>());
}
