void bind_ClubDetailsWrapper(pybind11::module& m)
{

	pybind11::class_<ClubDetailsWrapper, std::shared_ptr<ClubDetailsWrapper>, ClubSettingsWrapper> cl_ClubDetailsWrapper(m, "ClubDetailsWrapper");
	cl_ClubDetailsWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ClubDetailsWrapper.def(pybind11::init<ClubDetailsWrapper const &>(), pybind11::arg("other"));
	// cl_ClubDetailsWrapper.def(pybind11::del<>());
	cl_ClubDetailsWrapper.def("GetClubID", [](ClubDetailsWrapper& cls_) { return cls_.GetClubID(); });
	// [deprecated] cl_ClubDetailsWrapper.def("GetOwnerPlayerID", [](ClubDetailsWrapper& cls_) { return cls_.GetOwnerPlayerID(); });
	cl_ClubDetailsWrapper.def("GetOwnerPlayerUniqueID", [](ClubDetailsWrapper& cls_) { return cls_.GetOwnerPlayerUniqueID(); });
	cl_ClubDetailsWrapper.def("GetMotD", [](ClubDetailsWrapper& cls_) { return cls_.GetMotD(); });
	cl_ClubDetailsWrapper.def("GetbVerified", [](ClubDetailsWrapper& cls_) { return cls_.GetbVerified(); });
	cl_ClubDetailsWrapper.def("GetLastUpdatedTime", [](ClubDetailsWrapper& cls_) { return cls_.GetLastUpdatedTime(); });
	cl_ClubDetailsWrapper.def("GetMembers", [](ClubDetailsWrapper& cls_) { return cls_.GetMembers(); });

	pybind11::class_<ClubMember, std::shared_ptr<ClubMember>> cl_ClubMember(m, "ClubMember");
	//cl_ClubMember.def_property("paddingForReasons", [](const ClubMember& cls_) { return cls_.paddingForReasons; }, [](ClubMember& cls_, unsigned char [72] const& prop_) { cls_.paddingForReasons = prop_; });
	// [deprecated] cl_ClubMember.def("GetSteamId", [](ClubMember& cls_) { return cls_.GetSteamId(); });
	cl_ClubMember.def("GetUniqueID", [](ClubMember& cls_) { return cls_.GetUniqueID(); });
	cl_ClubMember.def("GetName", [](ClubMember& cls_) { return cls_.GetName(); });
	cl_ClubMember.def(pybind11::init<>());
	cl_ClubMember.def(pybind11::init<ClubMember const &>(), pybind11::arg("arg0"));
	// cl_ClubMember.def(pybind11::del<>());
}
