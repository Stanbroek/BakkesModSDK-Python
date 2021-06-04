void bind_WorldInfoWrapper(pybind11::module& m)
{

	pybind11::class_<WorldInfoWrapper, std::shared_ptr<WorldInfoWrapper>, ActorWrapper> cl_WorldInfoWrapper(m, "WorldInfoWrapper");
	cl_WorldInfoWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_WorldInfoWrapper.def(pybind11::init<WorldInfoWrapper const &>(), pybind11::arg("other"));
	// cl_WorldInfoWrapper.def(pybind11::del<>());
	cl_WorldInfoWrapper.def("GetTimeDilation", [](WorldInfoWrapper& cls_) { return cls_.GetTimeDilation(); });
	cl_WorldInfoWrapper.def("GetDemoPlayTimeDilation", [](WorldInfoWrapper& cls_) { return cls_.GetDemoPlayTimeDilation(); });
	cl_WorldInfoWrapper.def("GetTimeSeconds", [](WorldInfoWrapper& cls_) { return cls_.GetTimeSeconds(); });
	cl_WorldInfoWrapper.def("GetRealTimeSeconds", [](WorldInfoWrapper& cls_) { return cls_.GetRealTimeSeconds(); });
	cl_WorldInfoWrapper.def("GetRealDeltaSeconds", [](WorldInfoWrapper& cls_) { return cls_.GetRealDeltaSeconds(); });
	cl_WorldInfoWrapper.def("GetAudioTimeSeconds", [](WorldInfoWrapper& cls_) { return cls_.GetAudioTimeSeconds(); });
	cl_WorldInfoWrapper.def("GetDeltaSeconds", [](WorldInfoWrapper& cls_) { return cls_.GetDeltaSeconds(); });
	cl_WorldInfoWrapper.def("GetPauseDelay", [](WorldInfoWrapper& cls_) { return cls_.GetPauseDelay(); });
	cl_WorldInfoWrapper.def("GetRealTimeToUnPause", [](WorldInfoWrapper& cls_) { return cls_.GetRealTimeToUnPause(); });
	cl_WorldInfoWrapper.def("GetStallZ", [](WorldInfoWrapper& cls_) { return cls_.GetStallZ(); });
	cl_WorldInfoWrapper.def("GetWorldGravityZ", [](WorldInfoWrapper& cls_) { return cls_.GetWorldGravityZ(); });
	cl_WorldInfoWrapper.def("GetDefaultGravityZ", [](WorldInfoWrapper& cls_) { return cls_.GetDefaultGravityZ(); });
	cl_WorldInfoWrapper.def("GetGlobalGravityZ", [](WorldInfoWrapper& cls_) { return cls_.GetGlobalGravityZ(); });
	cl_WorldInfoWrapper.def("GetRBPhysicsGravityScaling", [](WorldInfoWrapper& cls_) { return cls_.GetRBPhysicsGravityScaling(); });
}
