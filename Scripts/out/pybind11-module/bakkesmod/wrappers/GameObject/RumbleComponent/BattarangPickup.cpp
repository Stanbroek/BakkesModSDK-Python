void bind_BattarangPickup(pybind11::module& m)
{

	pybind11::class_<BattarangPickup, std::shared_ptr<BattarangPickup>, BallLassoPickup> cl_BattarangPickup(m, "BattarangPickup");
	cl_BattarangPickup.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_BattarangPickup.def(pybind11::init<BattarangPickup const &>(), pybind11::arg("other"));
	// cl_BattarangPickup.def(pybind11::del<>());
	cl_BattarangPickup.def("GetSpinSpeed", [](BattarangPickup& cls_) { return cls_.GetSpinSpeed(); });
	cl_BattarangPickup.def("SetSpinSpeed", [](BattarangPickup& cls_, float newSpinSpeed) { return cls_.SetSpinSpeed(newSpinSpeed); }, pybind11::arg("newSpinSpeed"));
	cl_BattarangPickup.def("GetCurRotation", [](BattarangPickup& cls_) { return cls_.GetCurRotation(); });
	cl_BattarangPickup.def("SetCurRotation", [](BattarangPickup& cls_, float newCurRotation) { return cls_.SetCurRotation(newCurRotation); }, pybind11::arg("newCurRotation"));
}
