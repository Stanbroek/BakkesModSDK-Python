void bind_HandbrakeOverridePickup(pybind11::module& m)
{

	pybind11::class_<HandbrakeOverridePickup, std::shared_ptr<HandbrakeOverridePickup>, TargetedPickup> cl_HandbrakeOverridePickup(m, "HandbrakeOverridePickup");
	cl_HandbrakeOverridePickup.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_HandbrakeOverridePickup.def(pybind11::init<HandbrakeOverridePickup const &>(), pybind11::arg("other"));
	// cl_HandbrakeOverridePickup.def(pybind11::del<>());
	cl_HandbrakeOverridePickup.def("GetOtherCar", [](HandbrakeOverridePickup& cls_) { return cls_.GetOtherCar(); });
	cl_HandbrakeOverridePickup.def("SetOtherCar", [](HandbrakeOverridePickup& cls_, CarWrapper newOtherCar) { return cls_.SetOtherCar(newOtherCar); }, pybind11::arg("newOtherCar"));
	cl_HandbrakeOverridePickup.def("PickupEnd", [](HandbrakeOverridePickup& cls_) { return cls_.PickupEnd(); });
	cl_HandbrakeOverridePickup.def("PickupStart", [](HandbrakeOverridePickup& cls_) { return cls_.PickupStart(); });
}
