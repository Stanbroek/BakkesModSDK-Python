void bind_FlipCarComponentWrapper(pybind11::module& m)
{

	pybind11::class_<FlipCarComponentWrapper, std::shared_ptr<FlipCarComponentWrapper>, CarComponentWrapper> cl_FlipCarComponentWrapper(m, "FlipCarComponentWrapper");
	cl_FlipCarComponentWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_FlipCarComponentWrapper.def(pybind11::init<FlipCarComponentWrapper const &>(), pybind11::arg("other"));
	// cl_FlipCarComponentWrapper.def(pybind11::del<>());
	cl_FlipCarComponentWrapper.def("GetFlipCarImpulse", [](FlipCarComponentWrapper& cls_) { return cls_.GetFlipCarImpulse(); });
	cl_FlipCarComponentWrapper.def("SetFlipCarImpulse", [](FlipCarComponentWrapper& cls_, float newFlipCarImpulse) { return cls_.SetFlipCarImpulse(newFlipCarImpulse); }, pybind11::arg("newFlipCarImpulse"));
	cl_FlipCarComponentWrapper.def("GetFlipCarTorque", [](FlipCarComponentWrapper& cls_) { return cls_.GetFlipCarTorque(); });
	cl_FlipCarComponentWrapper.def("SetFlipCarTorque", [](FlipCarComponentWrapper& cls_, float newFlipCarTorque) { return cls_.SetFlipCarTorque(newFlipCarTorque); }, pybind11::arg("newFlipCarTorque"));
	cl_FlipCarComponentWrapper.def("GetFlipCarTime", [](FlipCarComponentWrapper& cls_) { return cls_.GetFlipCarTime(); });
	cl_FlipCarComponentWrapper.def("SetFlipCarTime", [](FlipCarComponentWrapper& cls_, float newFlipCarTime) { return cls_.SetFlipCarTime(newFlipCarTime); }, pybind11::arg("newFlipCarTime"));
	cl_FlipCarComponentWrapper.def("GetbFlipRight", [](FlipCarComponentWrapper& cls_) { return cls_.GetbFlipRight(); });
	cl_FlipCarComponentWrapper.def("SetbFlipRight", [](FlipCarComponentWrapper& cls_, long unsigned int newbFlipRight) { return cls_.SetbFlipRight(newbFlipRight); }, pybind11::arg("newbFlipRight"));
	cl_FlipCarComponentWrapper.def("InitFlip", [](FlipCarComponentWrapper& cls_) { return cls_.InitFlip(); });
	cl_FlipCarComponentWrapper.def("ApplyForces", [](FlipCarComponentWrapper& cls_, float ActiveTime) { return cls_.ApplyForces(ActiveTime); }, pybind11::arg("ActiveTime"));
	cl_FlipCarComponentWrapper.def("CanActivate", [](FlipCarComponentWrapper& cls_) { return cls_.CanActivate(); });
	cl_FlipCarComponentWrapper.def("OnCreated", [](FlipCarComponentWrapper& cls_) { return cls_.OnCreated(); });
}
