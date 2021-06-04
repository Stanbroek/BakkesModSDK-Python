void bind_JumpComponentWrapper(pybind11::module& m)
{

	pybind11::class_<JumpComponentWrapper, std::shared_ptr<JumpComponentWrapper>, CarComponentWrapper> cl_JumpComponentWrapper(m, "JumpComponentWrapper");
	cl_JumpComponentWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_JumpComponentWrapper.def(pybind11::init<JumpComponentWrapper const &>(), pybind11::arg("other"));
	// cl_JumpComponentWrapper.def(pybind11::del<>());
	cl_JumpComponentWrapper.def("GetMinJumpTime", [](JumpComponentWrapper& cls_) { return cls_.GetMinJumpTime(); });
	cl_JumpComponentWrapper.def("SetMinJumpTime", [](JumpComponentWrapper& cls_, float newMinJumpTime) { return cls_.SetMinJumpTime(newMinJumpTime); }, pybind11::arg("newMinJumpTime"));
	cl_JumpComponentWrapper.def("GetJumpImpulse", [](JumpComponentWrapper& cls_) { return cls_.GetJumpImpulse(); });
	cl_JumpComponentWrapper.def("SetJumpImpulse", [](JumpComponentWrapper& cls_, float newJumpImpulse) { return cls_.SetJumpImpulse(newJumpImpulse); }, pybind11::arg("newJumpImpulse"));
	cl_JumpComponentWrapper.def("GetJumpForce", [](JumpComponentWrapper& cls_) { return cls_.GetJumpForce(); });
	cl_JumpComponentWrapper.def("SetJumpForce", [](JumpComponentWrapper& cls_, float newJumpForce) { return cls_.SetJumpForce(newJumpForce); }, pybind11::arg("newJumpForce"));
	cl_JumpComponentWrapper.def("GetJumpForceTime", [](JumpComponentWrapper& cls_) { return cls_.GetJumpForceTime(); });
	cl_JumpComponentWrapper.def("SetJumpForceTime", [](JumpComponentWrapper& cls_, float newJumpForceTime) { return cls_.SetJumpForceTime(newJumpForceTime); }, pybind11::arg("newJumpForceTime"));
	cl_JumpComponentWrapper.def("GetPodiumJumpForceTime", [](JumpComponentWrapper& cls_) { return cls_.GetPodiumJumpForceTime(); });
	cl_JumpComponentWrapper.def("SetPodiumJumpForceTime", [](JumpComponentWrapper& cls_, float newPodiumJumpForceTime) { return cls_.SetPodiumJumpForceTime(newPodiumJumpForceTime); }, pybind11::arg("newPodiumJumpForceTime"));
	cl_JumpComponentWrapper.def("GetJumpImpulseSpeed", [](JumpComponentWrapper& cls_) { return cls_.GetJumpImpulseSpeed(); });
	cl_JumpComponentWrapper.def("SetJumpImpulseSpeed", [](JumpComponentWrapper& cls_, float newJumpImpulseSpeed) { return cls_.SetJumpImpulseSpeed(newJumpImpulseSpeed); }, pybind11::arg("newJumpImpulseSpeed"));
	cl_JumpComponentWrapper.def("GetJumpAccel", [](JumpComponentWrapper& cls_) { return cls_.GetJumpAccel(); });
	cl_JumpComponentWrapper.def("SetJumpAccel", [](JumpComponentWrapper& cls_, float newJumpAccel) { return cls_.SetJumpAccel(newJumpAccel); }, pybind11::arg("newJumpAccel"));
	cl_JumpComponentWrapper.def("GetMaxJumpHeight", [](JumpComponentWrapper& cls_) { return cls_.GetMaxJumpHeight(); });
	cl_JumpComponentWrapper.def("SetMaxJumpHeight", [](JumpComponentWrapper& cls_, float newMaxJumpHeight) { return cls_.SetMaxJumpHeight(newMaxJumpHeight); }, pybind11::arg("newMaxJumpHeight"));
	cl_JumpComponentWrapper.def("GetMaxJumpHeightTime", [](JumpComponentWrapper& cls_) { return cls_.GetMaxJumpHeightTime(); });
	cl_JumpComponentWrapper.def("SetMaxJumpHeightTime", [](JumpComponentWrapper& cls_, float newMaxJumpHeightTime) { return cls_.SetMaxJumpHeightTime(newMaxJumpHeightTime); }, pybind11::arg("newMaxJumpHeightTime"));
	cl_JumpComponentWrapper.def("GetbDeactivate", [](JumpComponentWrapper& cls_) { return cls_.GetbDeactivate(); });
	cl_JumpComponentWrapper.def("SetbDeactivate", [](JumpComponentWrapper& cls_, long unsigned int newbDeactivate) { return cls_.SetbDeactivate(newbDeactivate); }, pybind11::arg("newbDeactivate"));
	cl_JumpComponentWrapper.def("ApplyForces", [](JumpComponentWrapper& cls_, float ActiveTime) { return cls_.ApplyForces(ActiveTime); }, pybind11::arg("ActiveTime"));
	cl_JumpComponentWrapper.def("CacheJumpData", [](JumpComponentWrapper& cls_) { return cls_.CacheJumpData(); });
	cl_JumpComponentWrapper.def("OnCreated", [](JumpComponentWrapper& cls_) { return cls_.OnCreated(); });
}
