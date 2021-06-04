void bind_BoostOverridePickup(pybind11::module& m)
{

	pybind11::class_<BoostOverridePickup, std::shared_ptr<BoostOverridePickup>, TargetedPickup> cl_BoostOverridePickup(m, "BoostOverridePickup");
	cl_BoostOverridePickup.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_BoostOverridePickup.def(pybind11::init<BoostOverridePickup const &>(), pybind11::arg("other"));
	// cl_BoostOverridePickup.def(pybind11::del<>());
	cl_BoostOverridePickup.def("GetOtherCar", [](BoostOverridePickup& cls_) { return cls_.GetOtherCar(); });
	cl_BoostOverridePickup.def("SetOtherCar", [](BoostOverridePickup& cls_, CarWrapper newOtherCar) { return cls_.SetOtherCar(newOtherCar); }, pybind11::arg("newOtherCar"));
	cl_BoostOverridePickup.def("PickupEnd", [](BoostOverridePickup& cls_) { return cls_.PickupEnd(); });
	cl_BoostOverridePickup.def("OnTargetChanged", [](BoostOverridePickup& cls_) { return cls_.OnTargetChanged(); });
	cl_BoostOverridePickup.def("PickupStart", [](BoostOverridePickup& cls_) { return cls_.PickupStart(); });
}
