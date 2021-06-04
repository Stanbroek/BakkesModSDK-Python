void bind_AirControlComponentWrapper(pybind11::module& m)
{

	pybind11::class_<AirControlComponentWrapper, std::shared_ptr<AirControlComponentWrapper>, CarComponentWrapper> cl_AirControlComponentWrapper(m, "AirControlComponentWrapper");
	cl_AirControlComponentWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_AirControlComponentWrapper.def(pybind11::init<AirControlComponentWrapper const &>(), pybind11::arg("other"));
	// cl_AirControlComponentWrapper.def(pybind11::del<>());
	cl_AirControlComponentWrapper.def("GetAirTorque", [](AirControlComponentWrapper& cls_) { return cls_.GetAirTorque(); });
	cl_AirControlComponentWrapper.def("SetAirTorque", [](AirControlComponentWrapper& cls_, Rotator newAirTorque) { return cls_.SetAirTorque(newAirTorque); }, pybind11::arg("newAirTorque"));
	cl_AirControlComponentWrapper.def("GetAirDamping", [](AirControlComponentWrapper& cls_) { return cls_.GetAirDamping(); });
	cl_AirControlComponentWrapper.def("SetAirDamping", [](AirControlComponentWrapper& cls_, Rotator newAirDamping) { return cls_.SetAirDamping(newAirDamping); }, pybind11::arg("newAirDamping"));
	cl_AirControlComponentWrapper.def("GetThrottleForce", [](AirControlComponentWrapper& cls_) { return cls_.GetThrottleForce(); });
	cl_AirControlComponentWrapper.def("SetThrottleForce", [](AirControlComponentWrapper& cls_, float newThrottleForce) { return cls_.SetThrottleForce(newThrottleForce); }, pybind11::arg("newThrottleForce"));
	cl_AirControlComponentWrapper.def("GetDodgeDisableTimeRemaining", [](AirControlComponentWrapper& cls_) { return cls_.GetDodgeDisableTimeRemaining(); });
	cl_AirControlComponentWrapper.def("SetDodgeDisableTimeRemaining", [](AirControlComponentWrapper& cls_, float newDodgeDisableTimeRemaining) { return cls_.SetDodgeDisableTimeRemaining(newDodgeDisableTimeRemaining); }, pybind11::arg("newDodgeDisableTimeRemaining"));
	cl_AirControlComponentWrapper.def("GetControlScale", [](AirControlComponentWrapper& cls_) { return cls_.GetControlScale(); });
	cl_AirControlComponentWrapper.def("SetControlScale", [](AirControlComponentWrapper& cls_, float newControlScale) { return cls_.SetControlScale(newControlScale); }, pybind11::arg("newControlScale"));
	cl_AirControlComponentWrapper.def("GetAirControlSensitivity", [](AirControlComponentWrapper& cls_) { return cls_.GetAirControlSensitivity(); });
	cl_AirControlComponentWrapper.def("SetAirControlSensitivity", [](AirControlComponentWrapper& cls_, float newAirControlSensitivity) { return cls_.SetAirControlSensitivity(newAirControlSensitivity); }, pybind11::arg("newAirControlSensitivity"));
	cl_AirControlComponentWrapper.def("ApplyForces", [](AirControlComponentWrapper& cls_, float ActiveTime) { return cls_.ApplyForces(ActiveTime); }, pybind11::arg("ActiveTime"));
	cl_AirControlComponentWrapper.def("OnCreated", [](AirControlComponentWrapper& cls_) { return cls_.OnCreated(); });
}
