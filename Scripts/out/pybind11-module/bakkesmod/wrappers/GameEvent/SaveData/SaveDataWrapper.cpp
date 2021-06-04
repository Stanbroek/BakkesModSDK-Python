void bind_SaveDataWrapper(pybind11::module& m)
{

	pybind11::class_<SaveDataWrapper, std::shared_ptr<SaveDataWrapper>, ObjectWrapper> cl_SaveDataWrapper(m, "SaveDataWrapper");
	cl_SaveDataWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_SaveDataWrapper.def(pybind11::init<SaveDataWrapper const &>(), pybind11::arg("other"));
	// cl_SaveDataWrapper.def(pybind11::del<>());
	cl_SaveDataWrapper.def("IsNull", [](SaveDataWrapper& cls_) { return cls_.IsNull(); });
	cl_SaveDataWrapper.def("GetDirectoryPath", [](SaveDataWrapper& cls_) { return cls_.GetDirectoryPath(); });
	cl_SaveDataWrapper.def("GetSaveType", [](SaveDataWrapper& cls_) { return cls_.GetSaveType(); });
	cl_SaveDataWrapper.def("GetSaveExt", [](SaveDataWrapper& cls_) { return cls_.GetSaveExt(); });
	cl_SaveDataWrapper.def("GetbExactFileMatch", [](SaveDataWrapper& cls_) { return cls_.GetbExactFileMatch(); });
	cl_SaveDataWrapper.def("SetbExactFileMatch", [](SaveDataWrapper& cls_, long unsigned int newbExactFileMatch) { return cls_.SetbExactFileMatch(newbExactFileMatch); }, pybind11::arg("newbExactFileMatch"));
	cl_SaveDataWrapper.def("Init", [](SaveDataWrapper& cls_) { return cls_.Init(); });
}
