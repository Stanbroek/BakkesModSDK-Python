void bind_SequenceWrapper(pybind11::module& m)
{

	pybind11::class_<SequenceWrapper, std::shared_ptr<SequenceWrapper>, SequenceOpWrapper> cl_SequenceWrapper(m, "SequenceWrapper");
	cl_SequenceWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_SequenceWrapper.def(pybind11::init<SequenceWrapper const &>(), pybind11::arg("other"));
	// cl_SequenceWrapper.def(pybind11::del<>());
	cl_SequenceWrapper.def("GetSequenceObjects", [](SequenceWrapper& cls_) { return cls_.GetSequenceObjects(); });
	cl_SequenceWrapper.def("GetNestedSequences", [](SequenceWrapper& cls_) { return cls_.GetNestedSequences(); });
	cl_SequenceWrapper.def("ActivateRemoteEvents", [](SequenceWrapper& cls_, std::string const & remote_event_name) { return cls_.ActivateRemoteEvents(remote_event_name); }, pybind11::arg("remote_event_name"));
	cl_SequenceWrapper.def("GetAllSequenceVariables", [](SequenceWrapper& cls_, bool reqursive) { return cls_.GetAllSequenceVariables(reqursive); }, pybind11::arg("reqursive"));
}
