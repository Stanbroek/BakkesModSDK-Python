void bind_SequenceVariableWrapper(pybind11::module& m)
{

	pybind11::class_<SequenceVariableWrapper, std::shared_ptr<SequenceVariableWrapper>, SequenceObjectWrapper> cl_SequenceVariableWrapper(m, "SequenceVariableWrapper");
	cl_SequenceVariableWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_SequenceVariableWrapper.def(pybind11::init<SequenceVariableWrapper const &>(), pybind11::arg("other"));
	// cl_SequenceVariableWrapper.def(pybind11::del<>());
	cl_SequenceVariableWrapper.def("GetVarName", [](SequenceVariableWrapper& cls_) { return cls_.GetVarName(); });
	cl_SequenceVariableWrapper.def("IsInt", [](SequenceVariableWrapper& cls_) { return cls_.IsInt(); });
	cl_SequenceVariableWrapper.def("IsFloat", [](SequenceVariableWrapper& cls_) { return cls_.IsFloat(); });
	cl_SequenceVariableWrapper.def("IsString", [](SequenceVariableWrapper& cls_) { return cls_.IsString(); });
	cl_SequenceVariableWrapper.def("IsVector", [](SequenceVariableWrapper& cls_) { return cls_.IsVector(); });
	cl_SequenceVariableWrapper.def("IsBool", [](SequenceVariableWrapper& cls_) { return cls_.IsBool(); });
	cl_SequenceVariableWrapper.def("IsObjectList", [](SequenceVariableWrapper& cls_) { return cls_.IsObjectList(); });
	cl_SequenceVariableWrapper.def("IsActor", [](SequenceVariableWrapper& cls_) { return cls_.IsActor(); });
	cl_SequenceVariableWrapper.def("GetFloat", [](SequenceVariableWrapper& cls_) { return cls_.GetFloat(); });
	cl_SequenceVariableWrapper.def("GetInt", [](SequenceVariableWrapper& cls_) { return cls_.GetInt(); });
	cl_SequenceVariableWrapper.def("GetString", [](SequenceVariableWrapper& cls_) { return cls_.GetString(); });
	cl_SequenceVariableWrapper.def("GetVector", [](SequenceVariableWrapper& cls_) { return cls_.GetVector(); });
	cl_SequenceVariableWrapper.def("GetBool", [](SequenceVariableWrapper& cls_) { return cls_.GetBool(); });
	cl_SequenceVariableWrapper.def("GetObjectList", [](SequenceVariableWrapper& cls_) { return cls_.GetObjectList(); });
	cl_SequenceVariableWrapper.def("SetFloat", [](SequenceVariableWrapper& cls_, float value) { return cls_.SetFloat(value); }, pybind11::arg("value"));
	cl_SequenceVariableWrapper.def("SetInt", [](SequenceVariableWrapper& cls_, int value) { return cls_.SetInt(value); }, pybind11::arg("value"));
	cl_SequenceVariableWrapper.def("SetString", [](SequenceVariableWrapper& cls_, std::string const & value) { return cls_.SetString(value); }, pybind11::arg("value"));
	cl_SequenceVariableWrapper.def("SetVector", [](SequenceVariableWrapper& cls_, Vector value) { return cls_.SetVector(value); }, pybind11::arg("value"));
	cl_SequenceVariableWrapper.def("SetBool", [](SequenceVariableWrapper& cls_, bool value) { return cls_.SetBool(value); }, pybind11::arg("value"));
	cl_SequenceVariableWrapper.def("GetActor", [](SequenceVariableWrapper& cls_) { return cls_.GetActor(); });
}
