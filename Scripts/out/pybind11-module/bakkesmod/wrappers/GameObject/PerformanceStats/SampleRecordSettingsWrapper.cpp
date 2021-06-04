void bind_SampleRecordSettingsWrapper(pybind11::module& m)
{

	pybind11::class_<SampleRecordSettingsWrapper, std::shared_ptr<SampleRecordSettingsWrapper>, ObjectWrapper> cl_SampleRecordSettingsWrapper(m, "SampleRecordSettingsWrapper");
	cl_SampleRecordSettingsWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_SampleRecordSettingsWrapper.def(pybind11::init<SampleRecordSettingsWrapper const &>(), pybind11::arg("other"));
	// cl_SampleRecordSettingsWrapper.def(pybind11::del<>());
	cl_SampleRecordSettingsWrapper.def("IsNull", [](SampleRecordSettingsWrapper& cls_) { return cls_.IsNull(); });
	cl_SampleRecordSettingsWrapper.def("GetMaxSampleAge", [](SampleRecordSettingsWrapper& cls_) { return cls_.GetMaxSampleAge(); });
	cl_SampleRecordSettingsWrapper.def("SetMaxSampleAge", [](SampleRecordSettingsWrapper& cls_, float newMaxSampleAge) { return cls_.SetMaxSampleAge(newMaxSampleAge); }, pybind11::arg("newMaxSampleAge"));
	cl_SampleRecordSettingsWrapper.def("GetRecordRate", [](SampleRecordSettingsWrapper& cls_) { return cls_.GetRecordRate(); });
	cl_SampleRecordSettingsWrapper.def("SetRecordRate", [](SampleRecordSettingsWrapper& cls_, float newRecordRate) { return cls_.SetRecordRate(newRecordRate); }, pybind11::arg("newRecordRate"));
}
