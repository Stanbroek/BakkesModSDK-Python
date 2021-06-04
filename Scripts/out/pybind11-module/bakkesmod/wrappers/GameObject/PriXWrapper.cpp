void bind_PriXWrapper(pybind11::module& m)
{

	pybind11::class_<PriXWrapper, std::shared_ptr<PriXWrapper>, PlayerReplicationInfoWrapper> cl_PriXWrapper(m, "PriXWrapper");
	cl_PriXWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_PriXWrapper.def(pybind11::init<PriXWrapper const &>(), pybind11::arg("other"));
	// cl_PriXWrapper.def(pybind11::del<>());
	cl_PriXWrapper.def("eventDestroyed", [](PriXWrapper& cls_) { return cls_.eventDestroyed(); });
	cl_PriXWrapper.def("OnUniqueIdChanged", [](PriXWrapper& cls_) { return cls_.OnUniqueIdChanged(); });
	// [deprecated] cl_PriXWrapper.def("SetUniqueId", [](PriXWrapper& cls_, SteamID & PlayerUniqueId) { return cls_.SetUniqueId(PlayerUniqueId); }, pybind11::arg("PlayerUniqueId"));
	cl_PriXWrapper.def("UnregisterPlayerFromSession", [](PriXWrapper& cls_) { return cls_.UnregisterPlayerFromSession(); });
	cl_PriXWrapper.def("RegisterPlayerWithSession", [](PriXWrapper& cls_) { return cls_.RegisterPlayerWithSession(); });
	cl_PriXWrapper.def("OnTeamChanged", [](PriXWrapper& cls_) { return cls_.OnTeamChanged(); });
	cl_PriXWrapper.def("SetPlayerTeam", [](PriXWrapper& cls_, TeamInfoWrapper NewTeam) { return cls_.SetPlayerTeam(NewTeam); }, pybind11::arg("NewTeam"));
	cl_PriXWrapper.def("eventOnOwnerChanged", [](PriXWrapper& cls_) { return cls_.eventOnOwnerChanged(); });
	cl_PriXWrapper.def("eventSetPlayerName", [](PriXWrapper& cls_, std::string S) { return cls_.eventSetPlayerName(S); }, pybind11::arg("S"));
	cl_PriXWrapper.def("EventDestroyed", [](PriXWrapper& cls_, PriXWrapper PRI) { return cls_.EventDestroyed(PRI); }, pybind11::arg("PRI"));
	cl_PriXWrapper.def("EventTeamChanged", [](PriXWrapper& cls_, PriXWrapper PRI) { return cls_.EventTeamChanged(PRI); }, pybind11::arg("PRI"));
	cl_PriXWrapper.def("EventUniqueIdChanged", [](PriXWrapper& cls_, PriXWrapper PRI) { return cls_.EventUniqueIdChanged(PRI); }, pybind11::arg("PRI"));
	cl_PriXWrapper.def("EventPlayerNameChanged", [](PriXWrapper& cls_, PriXWrapper PRI) { return cls_.EventPlayerNameChanged(PRI); }, pybind11::arg("PRI"));
}
