void bind_DemolishPickup(pybind11::module& m)
{

	pybind11::class_<DemolishPickup, std::shared_ptr<DemolishPickup>, RumblePickupComponentWrapper> cl_DemolishPickup(m, "DemolishPickup");
	cl_DemolishPickup.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_DemolishPickup.def(pybind11::init<DemolishPickup const &>(), pybind11::arg("other"));
	// cl_DemolishPickup.def(pybind11::del<>());
	cl_DemolishPickup.def("GetDemolishTarget", [](DemolishPickup& cls_) { return cls_.GetDemolishTarget(); });
	cl_DemolishPickup.def("SetDemolishTarget", [](DemolishPickup& cls_, unsigned char newDemolishTarget) { return cls_.SetDemolishTarget(newDemolishTarget); }, pybind11::arg("newDemolishTarget"));
	cl_DemolishPickup.def("GetDemolishSpeed", [](DemolishPickup& cls_) { return cls_.GetDemolishSpeed(); });
	cl_DemolishPickup.def("SetDemolishSpeed", [](DemolishPickup& cls_, unsigned char newDemolishSpeed) { return cls_.SetDemolishSpeed(newDemolishSpeed); }, pybind11::arg("newDemolishSpeed"));
	cl_DemolishPickup.def("GetOldTarget", [](DemolishPickup& cls_) { return cls_.GetOldTarget(); });
	cl_DemolishPickup.def("SetOldTarget", [](DemolishPickup& cls_, unsigned char newOldTarget) { return cls_.SetOldTarget(newOldTarget); }, pybind11::arg("newOldTarget"));
	cl_DemolishPickup.def("GetOldSpeed", [](DemolishPickup& cls_) { return cls_.GetOldSpeed(); });
	cl_DemolishPickup.def("SetOldSpeed", [](DemolishPickup& cls_, unsigned char newOldSpeed) { return cls_.SetOldSpeed(newOldSpeed); }, pybind11::arg("newOldSpeed"));
	cl_DemolishPickup.def("PickupEnd", [](DemolishPickup& cls_) { return cls_.PickupEnd(); });
	cl_DemolishPickup.def("PickupStart", [](DemolishPickup& cls_) { return cls_.PickupStart(); });
}
