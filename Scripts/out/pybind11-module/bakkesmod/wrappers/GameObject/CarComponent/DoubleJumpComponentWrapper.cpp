void bind_DoubleJumpComponentWrapper(pybind11::module& m)
{

	pybind11::class_<DoubleJumpComponentWrapper, std::shared_ptr<DoubleJumpComponentWrapper>, CarComponentWrapper> cl_DoubleJumpComponentWrapper(m, "DoubleJumpComponentWrapper");
	cl_DoubleJumpComponentWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_DoubleJumpComponentWrapper.def(pybind11::init<DoubleJumpComponentWrapper const &>(), pybind11::arg("other"));
	// cl_DoubleJumpComponentWrapper.def(pybind11::del<>());
	cl_DoubleJumpComponentWrapper.def("SetJumpImpulse", [](DoubleJumpComponentWrapper& cls_, float newJumpImpulse) { return cls_.SetJumpImpulse(newJumpImpulse); }, pybind11::arg("newJumpImpulse"));
	cl_DoubleJumpComponentWrapper.def("GetImpulseScale", [](DoubleJumpComponentWrapper& cls_) { return cls_.GetImpulseScale(); });
	cl_DoubleJumpComponentWrapper.def("SetImpulseScale", [](DoubleJumpComponentWrapper& cls_, float newImpulseScale) { return cls_.SetImpulseScale(newImpulseScale); }, pybind11::arg("newImpulseScale"));
	cl_DoubleJumpComponentWrapper.def("ApplyForces", [](DoubleJumpComponentWrapper& cls_, float ActiveTime) { return cls_.ApplyForces(ActiveTime); }, pybind11::arg("ActiveTime"));
	cl_DoubleJumpComponentWrapper.def("OnCreated", [](DoubleJumpComponentWrapper& cls_) { return cls_.OnCreated(); });
}
