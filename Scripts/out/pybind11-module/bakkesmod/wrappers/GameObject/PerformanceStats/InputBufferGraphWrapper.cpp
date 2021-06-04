void bind_InputBufferGraphWrapper(pybind11::module& m)
{

	pybind11::class_<InputBufferGraphWrapper, std::shared_ptr<InputBufferGraphWrapper>, StatGraphWrapper> cl_InputBufferGraphWrapper(m, "InputBufferGraphWrapper");
	cl_InputBufferGraphWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_InputBufferGraphWrapper.def(pybind11::init<InputBufferGraphWrapper const &>(), pybind11::arg("other"));
	// cl_InputBufferGraphWrapper.def(pybind11::del<>());
	cl_InputBufferGraphWrapper.def("GetBuffer", [](InputBufferGraphWrapper& cls_) { return cls_.GetBuffer(); });
	cl_InputBufferGraphWrapper.def("SetBuffer", [](InputBufferGraphWrapper& cls_, SampleHistoryWrapper newBuffer) { return cls_.SetBuffer(newBuffer); }, pybind11::arg("newBuffer"));
	cl_InputBufferGraphWrapper.def("GetBufferTarget", [](InputBufferGraphWrapper& cls_) { return cls_.GetBufferTarget(); });
	cl_InputBufferGraphWrapper.def("SetBufferTarget", [](InputBufferGraphWrapper& cls_, SampleHistoryWrapper newBufferTarget) { return cls_.SetBufferTarget(newBufferTarget); }, pybind11::arg("newBufferTarget"));
	cl_InputBufferGraphWrapper.def("GetOverUnderFrames", [](InputBufferGraphWrapper& cls_) { return cls_.GetOverUnderFrames(); });
	cl_InputBufferGraphWrapper.def("SetOverUnderFrames", [](InputBufferGraphWrapper& cls_, SampleHistoryWrapper newOverUnderFrames) { return cls_.SetOverUnderFrames(newOverUnderFrames); }, pybind11::arg("newOverUnderFrames"));
	cl_InputBufferGraphWrapper.def("GetPhysicsRate", [](InputBufferGraphWrapper& cls_) { return cls_.GetPhysicsRate(); });
	cl_InputBufferGraphWrapper.def("SetPhysicsRate", [](InputBufferGraphWrapper& cls_, SampleHistoryWrapper newPhysicsRate) { return cls_.SetPhysicsRate(newPhysicsRate); }, pybind11::arg("newPhysicsRate"));
	cl_InputBufferGraphWrapper.def("GetMaxPhysicsRate", [](InputBufferGraphWrapper& cls_) { return cls_.GetMaxPhysicsRate(); });
	cl_InputBufferGraphWrapper.def("SetMaxPhysicsRate", [](InputBufferGraphWrapper& cls_, float newMaxPhysicsRate) { return cls_.SetMaxPhysicsRate(newMaxPhysicsRate); }, pybind11::arg("newMaxPhysicsRate"));
	cl_InputBufferGraphWrapper.def("GetMinPhysicsRate", [](InputBufferGraphWrapper& cls_) { return cls_.GetMinPhysicsRate(); });
	cl_InputBufferGraphWrapper.def("SetMinPhysicsRate", [](InputBufferGraphWrapper& cls_, float newMinPhysicsRate) { return cls_.SetMinPhysicsRate(newMinPhysicsRate); }, pybind11::arg("newMinPhysicsRate"));
	cl_InputBufferGraphWrapper.def("CreateBufferHistory", [](InputBufferGraphWrapper& cls_, std::string Title) { return cls_.CreateBufferHistory(Title); }, pybind11::arg("Title"));
	cl_InputBufferGraphWrapper.def("eventConstruct", [](InputBufferGraphWrapper& cls_) { return cls_.eventConstruct(); });
}
