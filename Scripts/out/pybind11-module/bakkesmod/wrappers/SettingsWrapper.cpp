void bind_SettingsWrapper(pybind11::module& m)
{

	pybind11::class_<SettingsWrapper, std::shared_ptr<SettingsWrapper>> cl_SettingsWrapper(m, "SettingsWrapper");
	cl_SettingsWrapper.def(pybind11::init<>());
	// cl_SettingsWrapper.def(pybind11::del<>());
	cl_SettingsWrapper.def("GetCameraSettings", [](SettingsWrapper& cls_) { return cls_.GetCameraSettings(); });
	cl_SettingsWrapper.def("GetCameraSaveSettings", [](SettingsWrapper& cls_) { return cls_.GetCameraSaveSettings(); });
	// [deprecated] cl_SettingsWrapper.def("GetPCBindings", [](SettingsWrapper& cls_) { return cls_.GetPCBindings(); });
	// [deprecated] cl_SettingsWrapper.def("GetGamepadBindings", [](SettingsWrapper& cls_) { return cls_.GetGamepadBindings(); });
	cl_SettingsWrapper.def("GetAllPCBindings", [](SettingsWrapper& cls_) { return cls_.GetAllPCBindings(); });
	cl_SettingsWrapper.def("GetAllGamepadBindings", [](SettingsWrapper& cls_) { return cls_.GetAllGamepadBindings(); });
	cl_SettingsWrapper.def("GetGamepadSettings", [](SettingsWrapper& cls_) { return cls_.GetGamepadSettings(); });
	cl_SettingsWrapper.def("GetVideoSettings", [](SettingsWrapper& cls_) { return cls_.GetVideoSettings(); });
	cl_SettingsWrapper.def(pybind11::init<SettingsWrapper const &>(), pybind11::arg("arg0"));
}
