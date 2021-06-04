void bind_ControllerWrapper(pybind11::module& m)
{

	pybind11::class_<ControllerWrapper, std::shared_ptr<ControllerWrapper>, ActorWrapper> cl_ControllerWrapper(m, "ControllerWrapper");
	cl_ControllerWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ControllerWrapper.def(pybind11::init<ControllerWrapper const &>(), pybind11::arg("other"));
	// cl_ControllerWrapper.def(pybind11::del<>());
	cl_ControllerWrapper.def("GetPlayerReplicationInfo", [](ControllerWrapper& cls_) { return cls_.GetPlayerReplicationInfo(); });
}
