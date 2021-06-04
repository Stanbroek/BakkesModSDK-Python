void bind_SequenceObjectWrapper(pybind11::module& m)
{

	pybind11::class_<SequenceObjectWrapper, std::shared_ptr<SequenceObjectWrapper>, ObjectWrapper> cl_SequenceObjectWrapper(m, "SequenceObjectWrapper");
	cl_SequenceObjectWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_SequenceObjectWrapper.def(pybind11::init<SequenceObjectWrapper const &>(), pybind11::arg("other"));
	// cl_SequenceObjectWrapper.def(pybind11::del<>());
	cl_SequenceObjectWrapper.def("IsNull", [](SequenceObjectWrapper& cls_) { return cls_.IsNull(); });
	cl_SequenceObjectWrapper.def("GetParentSequence", [](SequenceObjectWrapper& cls_) { return cls_.GetParentSequence(); });
	cl_SequenceObjectWrapper.def("GetObjName", [](SequenceObjectWrapper& cls_) { return cls_.GetObjName(); });
	cl_SequenceObjectWrapper.def("GetObjCategory", [](SequenceObjectWrapper& cls_) { return cls_.GetObjCategory(); });
	cl_SequenceObjectWrapper.def("GetObjComment", [](SequenceObjectWrapper& cls_) { return cls_.GetObjComment(); });
}
