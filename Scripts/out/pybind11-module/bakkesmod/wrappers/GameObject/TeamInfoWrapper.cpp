void bind_TeamInfoWrapper(pybind11::module& m)
{

	pybind11::class_<TeamInfoWrapper, std::shared_ptr<TeamInfoWrapper>, ActorWrapper> cl_TeamInfoWrapper(m, "TeamInfoWrapper");
	cl_TeamInfoWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_TeamInfoWrapper.def(pybind11::init<TeamInfoWrapper const &>(), pybind11::arg("other"));
	// cl_TeamInfoWrapper.def(pybind11::del<>());
	cl_TeamInfoWrapper.def("GetTeamName", [](TeamInfoWrapper& cls_) { return cls_.GetTeamName(); });
	cl_TeamInfoWrapper.def("GetSize", [](TeamInfoWrapper& cls_) { return cls_.GetSize(); });
	cl_TeamInfoWrapper.def("SetSize", [](TeamInfoWrapper& cls_, int newSize) { return cls_.SetSize(newSize); }, pybind11::arg("newSize"));
	cl_TeamInfoWrapper.def("GetScore", [](TeamInfoWrapper& cls_) { return cls_.GetScore(); });
	cl_TeamInfoWrapper.def("SetScore", [](TeamInfoWrapper& cls_, int newScore) { return cls_.SetScore(newScore); }, pybind11::arg("newScore"));
	cl_TeamInfoWrapper.def("GetTeamIndex", [](TeamInfoWrapper& cls_) { return cls_.GetTeamIndex(); });
	cl_TeamInfoWrapper.def("SetTeamIndex", [](TeamInfoWrapper& cls_, int newTeamIndex) { return cls_.SetTeamIndex(newTeamIndex); }, pybind11::arg("newTeamIndex"));
	cl_TeamInfoWrapper.def("GetTeamColor", [](TeamInfoWrapper& cls_) { return cls_.GetTeamColor(); });
	cl_TeamInfoWrapper.def("SetTeamColor", [](TeamInfoWrapper& cls_, UnrealColor newTeamColor) { return cls_.SetTeamColor(newTeamColor); }, pybind11::arg("newTeamColor"));
	cl_TeamInfoWrapper.def("GetTeamNum", [](TeamInfoWrapper& cls_) { return cls_.GetTeamNum(); });
	cl_TeamInfoWrapper.def("eventDestroyed", [](TeamInfoWrapper& cls_) { return cls_.eventDestroyed(); });
}
