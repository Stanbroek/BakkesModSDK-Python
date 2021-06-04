void bind_BoostModPickup(pybind11::module& m)
{

	pybind11::class_<BoostModPickup, std::shared_ptr<BoostModPickup>, RumblePickupComponentWrapper> cl_BoostModPickup(m, "BoostModPickup");
	cl_BoostModPickup.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_BoostModPickup.def(pybind11::init<BoostModPickup const &>(), pybind11::arg("other"));
	// cl_BoostModPickup.def(pybind11::del<>());
	cl_BoostModPickup.def("GetbUnlimitedBoost", [](BoostModPickup& cls_) { return cls_.GetbUnlimitedBoost(); });
	cl_BoostModPickup.def("SetbUnlimitedBoost", [](BoostModPickup& cls_, long unsigned int newbUnlimitedBoost) { return cls_.SetbUnlimitedBoost(newbUnlimitedBoost); }, pybind11::arg("newbUnlimitedBoost"));
	cl_BoostModPickup.def("GetBoostStrength", [](BoostModPickup& cls_) { return cls_.GetBoostStrength(); });
	cl_BoostModPickup.def("SetBoostStrength", [](BoostModPickup& cls_, float newBoostStrength) { return cls_.SetBoostStrength(newBoostStrength); }, pybind11::arg("newBoostStrength"));
	cl_BoostModPickup.def("GetOldBoostStrength", [](BoostModPickup& cls_) { return cls_.GetOldBoostStrength(); });
	cl_BoostModPickup.def("SetOldBoostStrength", [](BoostModPickup& cls_, float newOldBoostStrength) { return cls_.SetOldBoostStrength(newOldBoostStrength); }, pybind11::arg("newOldBoostStrength"));
	cl_BoostModPickup.def("PickupEnd", [](BoostModPickup& cls_) { return cls_.PickupEnd(); });
	cl_BoostModPickup.def("PickupStart", [](BoostModPickup& cls_) { return cls_.PickupStart(); });
}
