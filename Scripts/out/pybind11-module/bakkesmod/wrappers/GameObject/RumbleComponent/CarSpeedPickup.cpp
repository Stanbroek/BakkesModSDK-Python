void bind_CarSpeedPickup(pybind11::module& m)
{

	pybind11::class_<CarSpeedPickup, std::shared_ptr<CarSpeedPickup>, RumblePickupComponentWrapper> cl_CarSpeedPickup(m, "CarSpeedPickup");
	cl_CarSpeedPickup.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_CarSpeedPickup.def(pybind11::init<CarSpeedPickup const &>(), pybind11::arg("other"));
	// cl_CarSpeedPickup.def(pybind11::del<>());
	cl_CarSpeedPickup.def("GetGravityScale", [](CarSpeedPickup& cls_) { return cls_.GetGravityScale(); });
	cl_CarSpeedPickup.def("SetGravityScale", [](CarSpeedPickup& cls_, float newGravityScale) { return cls_.SetGravityScale(newGravityScale); }, pybind11::arg("newGravityScale"));
	cl_CarSpeedPickup.def("GetAddedForce", [](CarSpeedPickup& cls_) { return cls_.GetAddedForce(); });
	cl_CarSpeedPickup.def("SetAddedForce", [](CarSpeedPickup& cls_, Vector newAddedForce) { return cls_.SetAddedForce(newAddedForce); }, pybind11::arg("newAddedForce"));
	cl_CarSpeedPickup.def("GetOrigGravityScale", [](CarSpeedPickup& cls_) { return cls_.GetOrigGravityScale(); });
	cl_CarSpeedPickup.def("SetOrigGravityScale", [](CarSpeedPickup& cls_, float newOrigGravityScale) { return cls_.SetOrigGravityScale(newOrigGravityScale); }, pybind11::arg("newOrigGravityScale"));
	cl_CarSpeedPickup.def("PickupEnd", [](CarSpeedPickup& cls_) { return cls_.PickupEnd(); });
	cl_CarSpeedPickup.def("PickupStart", [](CarSpeedPickup& cls_) { return cls_.PickupStart(); });
}
