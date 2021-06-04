void bind_ClubSettingsWrapper(pybind11::module& m)
{

	pybind11::class_<ClubSettingsWrapper, std::shared_ptr<ClubSettingsWrapper>, ObjectWrapper> cl_ClubSettingsWrapper(m, "ClubSettingsWrapper");
	cl_ClubSettingsWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ClubSettingsWrapper.def(pybind11::init<ClubSettingsWrapper const &>(), pybind11::arg("other"));
	// cl_ClubSettingsWrapper.def(pybind11::del<>());
	cl_ClubSettingsWrapper.def("IsNull", [](ClubSettingsWrapper& cls_) { return cls_.IsNull(); });
	cl_ClubSettingsWrapper.def("GetClubName", [](ClubSettingsWrapper& cls_) { return cls_.GetClubName(); });
	cl_ClubSettingsWrapper.def("GetClubTag", [](ClubSettingsWrapper& cls_) { return cls_.GetClubTag(); });
	cl_ClubSettingsWrapper.def("GetPrimaryColor", [](ClubSettingsWrapper& cls_) { return cls_.GetPrimaryColor(); });
	cl_ClubSettingsWrapper.def("GetAccentColor", [](ClubSettingsWrapper& cls_) { return cls_.GetAccentColor(); });
}
