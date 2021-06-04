void bind_StatGraphWrapper(pybind11::module& m)
{

	pybind11::class_<StatGraphWrapper, std::shared_ptr<StatGraphWrapper>, ObjectWrapper> cl_StatGraphWrapper(m, "StatGraphWrapper");
	cl_StatGraphWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_StatGraphWrapper.def(pybind11::init<StatGraphWrapper const &>(), pybind11::arg("other"));
	// cl_StatGraphWrapper.def(pybind11::del<>());
	cl_StatGraphWrapper.def("IsNull", [](StatGraphWrapper& cls_) { return cls_.IsNull(); });
	cl_StatGraphWrapper.def("GetRecordSettings", [](StatGraphWrapper& cls_) { return cls_.GetRecordSettings(); });
	cl_StatGraphWrapper.def("SetRecordSettings", [](StatGraphWrapper& cls_, SampleRecordSettingsWrapper newRecordSettings) { return cls_.SetRecordSettings(newRecordSettings); }, pybind11::arg("newRecordSettings"));
	cl_StatGraphWrapper.def("GetLastTickTime", [](StatGraphWrapper& cls_) { return cls_.GetLastTickTime(); });
	cl_StatGraphWrapper.def("SetLastTickTime", [](StatGraphWrapper& cls_, double newLastTickTime) { return cls_.SetLastTickTime(newLastTickTime); }, pybind11::arg("newLastTickTime"));
	cl_StatGraphWrapper.def("GetSampleHistories", [](StatGraphWrapper& cls_) { return cls_.GetSampleHistories(); });
	cl_StatGraphWrapper.def("StopDrawing", [](StatGraphWrapper& cls_) { return cls_.StopDrawing(); });
	cl_StatGraphWrapper.def("CreateSampleHistory", [](StatGraphWrapper& cls_, std::string Title) { return cls_.CreateSampleHistory(Title); }, pybind11::arg("Title"));
	cl_StatGraphWrapper.def("AddSampleHistory", [](StatGraphWrapper& cls_, SampleHistoryWrapper History) { return cls_.AddSampleHistory(History); }, pybind11::arg("History"));
	cl_StatGraphWrapper.def("eventConstruct", [](StatGraphWrapper& cls_) { return cls_.eventConstruct(); });
}
