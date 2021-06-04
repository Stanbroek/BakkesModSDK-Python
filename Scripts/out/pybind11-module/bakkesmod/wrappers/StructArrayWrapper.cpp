void bind_StructArrayWrapper(pybind11::module& m)
{

	pybind11::class_<StructArrayWrapper<LinearColor>, std::shared_ptr<StructArrayWrapper<LinearColor>>> cl_StructArrayWrapper_LinearColor(m, "StructArrayWrapper<LinearColor>");
	cl_StructArrayWrapper_LinearColor.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_StructArrayWrapper_LinearColor.def(pybind11::init<StructArrayWrapper<LinearColor> const &>(), pybind11::arg("other"));
	// cl_StructArrayWrapper_LinearColor.def(pybind11::del<>());
	cl_StructArrayWrapper_LinearColor.def("Count", [](StructArrayWrapper<LinearColor>& cls_) { return cls_.Count(); });
	cl_StructArrayWrapper_LinearColor.def("Get", [](StructArrayWrapper<LinearColor>& cls_, int index) { return cls_.Get(index); }, pybind11::arg("index"));

	pybind11::class_<StructArrayWrapper<SteamID>, std::shared_ptr<StructArrayWrapper<SteamID>>> cl_StructArrayWrapper_SteamID(m, "StructArrayWrapper<SteamID>");
	cl_StructArrayWrapper_SteamID.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_StructArrayWrapper_SteamID.def(pybind11::init<StructArrayWrapper<SteamID> const &>(), pybind11::arg("other"));
	// cl_StructArrayWrapper_SteamID.def(pybind11::del<>());
	cl_StructArrayWrapper_SteamID.def("Count", [](StructArrayWrapper<SteamID>& cls_) { return cls_.Count(); });
	cl_StructArrayWrapper_SteamID.def("Get", [](StructArrayWrapper<SteamID>& cls_, int index) { return cls_.Get(index); }, pybind11::arg("index"));

	pybind11::class_<StructArrayWrapper<ProfileCameraSettings>, std::shared_ptr<StructArrayWrapper<ProfileCameraSettings>>> cl_StructArrayWrapper_ProfileCameraSettings(m, "StructArrayWrapper<ProfileCameraSettings>");
	cl_StructArrayWrapper_ProfileCameraSettings.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_StructArrayWrapper_ProfileCameraSettings.def(pybind11::init<StructArrayWrapper<ProfileCameraSettings> const &>(), pybind11::arg("other"));
	// cl_StructArrayWrapper_ProfileCameraSettings.def(pybind11::del<>());
	cl_StructArrayWrapper_ProfileCameraSettings.def("Count", [](StructArrayWrapper<ProfileCameraSettings>& cls_) { return cls_.Count(); });
	cl_StructArrayWrapper_ProfileCameraSettings.def("Get", [](StructArrayWrapper<ProfileCameraSettings>& cls_, int index) { return cls_.Get(index); }, pybind11::arg("index"));

	pybind11::class_<StructArrayWrapper<RecordedSample>, std::shared_ptr<StructArrayWrapper<RecordedSample>>> cl_StructArrayWrapper_RecordedSample(m, "StructArrayWrapper<RecordedSample>");
	cl_StructArrayWrapper_RecordedSample.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_StructArrayWrapper_RecordedSample.def(pybind11::init<StructArrayWrapper<RecordedSample> const &>(), pybind11::arg("other"));
	// cl_StructArrayWrapper_RecordedSample.def(pybind11::del<>());
	cl_StructArrayWrapper_RecordedSample.def("Count", [](StructArrayWrapper<RecordedSample>& cls_) { return cls_.Count(); });
	cl_StructArrayWrapper_RecordedSample.def("Get", [](StructArrayWrapper<RecordedSample>& cls_, int index) { return cls_.Get(index); }, pybind11::arg("index"));

	pybind11::class_<StructArrayWrapper<ClubMember>, std::shared_ptr<StructArrayWrapper<ClubMember>>> cl_StructArrayWrapper_ClubMember(m, "StructArrayWrapper<ClubMember>");
	cl_StructArrayWrapper_ClubMember.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_StructArrayWrapper_ClubMember.def(pybind11::init<StructArrayWrapper<ClubMember> const &>(), pybind11::arg("other"));
	// cl_StructArrayWrapper_ClubMember.def(pybind11::del<>());
	cl_StructArrayWrapper_ClubMember.def("Count", [](StructArrayWrapper<ClubMember>& cls_) { return cls_.Count(); });
	cl_StructArrayWrapper_ClubMember.def("Get", [](StructArrayWrapper<ClubMember>& cls_, int index) { return cls_.Get(index); }, pybind11::arg("index"));
}
