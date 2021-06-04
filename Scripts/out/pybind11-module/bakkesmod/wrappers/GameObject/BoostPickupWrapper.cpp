void bind_BoostPickupWrapper(pybind11::module& m)
{

	pybind11::class_<BoostPickupWrapper, std::shared_ptr<BoostPickupWrapper>, VehiclePickupWrapper> cl_BoostPickupWrapper(m, "BoostPickupWrapper");
	cl_BoostPickupWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_BoostPickupWrapper.def(pybind11::init<BoostPickupWrapper const &>(), pybind11::arg("other"));
	// cl_BoostPickupWrapper.def(pybind11::del<>());
	cl_BoostPickupWrapper.def("GetBoostAmount", [](BoostPickupWrapper& cls_) { return cls_.GetBoostAmount(); });
	cl_BoostPickupWrapper.def("SetBoostAmount", [](BoostPickupWrapper& cls_, float newBoostAmount) { return cls_.SetBoostAmount(newBoostAmount); }, pybind11::arg("newBoostAmount"));
	cl_BoostPickupWrapper.def("GetBoostType", [](BoostPickupWrapper& cls_) { return cls_.GetBoostType(); });
	cl_BoostPickupWrapper.def("SetBoostType", [](BoostPickupWrapper& cls_, unsigned char newBoostType) { return cls_.SetBoostType(newBoostType); }, pybind11::arg("newBoostType"));
	cl_BoostPickupWrapper.def("PlayPickedUpFX", [](BoostPickupWrapper& cls_) { return cls_.PlayPickedUpFX(); });
	cl_BoostPickupWrapper.def("Pickup2", [](BoostPickupWrapper& cls_, CarWrapper Car) { return cls_.Pickup2(Car); }, pybind11::arg("Car"));
	cl_BoostPickupWrapper.def("CanPickup", [](BoostPickupWrapper& cls_, CarWrapper Car) { return cls_.CanPickup(Car); }, pybind11::arg("Car"));
}
