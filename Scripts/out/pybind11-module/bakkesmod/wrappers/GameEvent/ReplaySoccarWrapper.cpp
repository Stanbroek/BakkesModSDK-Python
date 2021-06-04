void bind_ReplaySoccarWrapper(pybind11::module& m)
{

	pybind11::class_<ReplaySoccarWrapper, std::shared_ptr<ReplaySoccarWrapper>, ReplayWrapper> cl_ReplaySoccarWrapper(m, "ReplaySoccarWrapper");
	cl_ReplaySoccarWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ReplaySoccarWrapper.def(pybind11::init<ReplaySoccarWrapper const &>(), pybind11::arg("other"));
	// cl_ReplaySoccarWrapper.def(pybind11::del<>());
	cl_ReplaySoccarWrapper.def("GetTeamSize", [](ReplaySoccarWrapper& cls_) { return cls_.GetTeamSize(); });
	cl_ReplaySoccarWrapper.def("SetTeamSize", [](ReplaySoccarWrapper& cls_, int newTeamSize) { return cls_.SetTeamSize(newTeamSize); }, pybind11::arg("newTeamSize"));
	cl_ReplaySoccarWrapper.def("GetUnfairTeamSize", [](ReplaySoccarWrapper& cls_) { return cls_.GetUnfairTeamSize(); });
	cl_ReplaySoccarWrapper.def("SetUnfairTeamSize", [](ReplaySoccarWrapper& cls_, int newUnfairTeamSize) { return cls_.SetUnfairTeamSize(newUnfairTeamSize); }, pybind11::arg("newUnfairTeamSize"));
	cl_ReplaySoccarWrapper.def("GetbUnfairBots", [](ReplaySoccarWrapper& cls_) { return cls_.GetbUnfairBots(); });
	cl_ReplaySoccarWrapper.def("SetbUnfairBots", [](ReplaySoccarWrapper& cls_, long unsigned int newbUnfairBots) { return cls_.SetbUnfairBots(newbUnfairBots); }, pybind11::arg("newbUnfairBots"));
	cl_ReplaySoccarWrapper.def("GetPrimaryPlayerTeam", [](ReplaySoccarWrapper& cls_) { return cls_.GetPrimaryPlayerTeam(); });
	cl_ReplaySoccarWrapper.def("SetPrimaryPlayerTeam", [](ReplaySoccarWrapper& cls_, int newPrimaryPlayerTeam) { return cls_.SetPrimaryPlayerTeam(newPrimaryPlayerTeam); }, pybind11::arg("newPrimaryPlayerTeam"));
	cl_ReplaySoccarWrapper.def("GetTeam0Score", [](ReplaySoccarWrapper& cls_) { return cls_.GetTeam0Score(); });
	cl_ReplaySoccarWrapper.def("SetTeam0Score", [](ReplaySoccarWrapper& cls_, int newTeam0Score) { return cls_.SetTeam0Score(newTeam0Score); }, pybind11::arg("newTeam0Score"));
	cl_ReplaySoccarWrapper.def("GetTeam1Score", [](ReplaySoccarWrapper& cls_) { return cls_.GetTeam1Score(); });
	cl_ReplaySoccarWrapper.def("SetTeam1Score", [](ReplaySoccarWrapper& cls_, int newTeam1Score) { return cls_.SetTeam1Score(newTeam1Score); }, pybind11::arg("newTeam1Score"));
	cl_ReplaySoccarWrapper.def("eventPreExport", [](ReplaySoccarWrapper& cls_) { return cls_.eventPreExport(); });
	cl_ReplaySoccarWrapper.def("RemoveTimelineKeyframe", [](ReplaySoccarWrapper& cls_, int KeyframeIndex) { return cls_.RemoveTimelineKeyframe(KeyframeIndex); }, pybind11::arg("KeyframeIndex"));
	cl_ReplaySoccarWrapper.def("RecordUserEvent", [](ReplaySoccarWrapper& cls_) { return cls_.RecordUserEvent(); });
	cl_ReplaySoccarWrapper.def("AddPlayer", [](ReplaySoccarWrapper& cls_, PriWrapper PRI) { return cls_.AddPlayer(PRI); }, pybind11::arg("PRI"));
}
