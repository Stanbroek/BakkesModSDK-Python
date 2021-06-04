void bind_SwapperPickup(pybind11::module& m)
{

	pybind11::class_<SwapperPickup, std::shared_ptr<SwapperPickup>, TargetedPickup> cl_SwapperPickup(m, "SwapperPickup");
	cl_SwapperPickup.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_SwapperPickup.def(pybind11::init<SwapperPickup const &>(), pybind11::arg("other"));
	// cl_SwapperPickup.def(pybind11::del<>());
	cl_SwapperPickup.def("GetOtherCar", [](SwapperPickup& cls_) { return cls_.GetOtherCar(); });
	cl_SwapperPickup.def("SetOtherCar", [](SwapperPickup& cls_, CarWrapper newOtherCar) { return cls_.SetOtherCar(newOtherCar); }, pybind11::arg("newOtherCar"));
	cl_SwapperPickup.def("PickupEnd", [](SwapperPickup& cls_) { return cls_.PickupEnd(); });
	cl_SwapperPickup.def("OnTargetChanged", [](SwapperPickup& cls_) { return cls_.OnTargetChanged(); });
	cl_SwapperPickup.def("PickupStart", [](SwapperPickup& cls_) { return cls_.PickupStart(); });
}
