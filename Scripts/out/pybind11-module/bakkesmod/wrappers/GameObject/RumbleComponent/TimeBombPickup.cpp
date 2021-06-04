void bind_TimeBombPickup(pybind11::module& m)
{

	pybind11::class_<TimeBombPickup, std::shared_ptr<TimeBombPickup>, RumblePickupComponentWrapper> cl_TimeBombPickup(m, "TimeBombPickup");
	cl_TimeBombPickup.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_TimeBombPickup.def(pybind11::init<TimeBombPickup const &>(), pybind11::arg("other"));
	// cl_TimeBombPickup.def(pybind11::del<>());
	cl_TimeBombPickup.def("GetRadius", [](TimeBombPickup& cls_) { return cls_.GetRadius(); });
	cl_TimeBombPickup.def("SetRadius", [](TimeBombPickup& cls_, float newRadius) { return cls_.SetRadius(newRadius); }, pybind11::arg("newRadius"));
	cl_TimeBombPickup.def("GetAlmostReadyDuration", [](TimeBombPickup& cls_) { return cls_.GetAlmostReadyDuration(); });
	cl_TimeBombPickup.def("SetAlmostReadyDuration", [](TimeBombPickup& cls_, float newAlmostReadyDuration) { return cls_.SetAlmostReadyDuration(newAlmostReadyDuration); }, pybind11::arg("newAlmostReadyDuration"));
	cl_TimeBombPickup.def("GetStartMatSpeed", [](TimeBombPickup& cls_) { return cls_.GetStartMatSpeed(); });
	cl_TimeBombPickup.def("SetStartMatSpeed", [](TimeBombPickup& cls_, float newStartMatSpeed) { return cls_.SetStartMatSpeed(newStartMatSpeed); }, pybind11::arg("newStartMatSpeed"));
	cl_TimeBombPickup.def("GetAlmostReadyMatSpeed", [](TimeBombPickup& cls_) { return cls_.GetAlmostReadyMatSpeed(); });
	cl_TimeBombPickup.def("SetAlmostReadyMatSpeed", [](TimeBombPickup& cls_, float newAlmostReadyMatSpeed) { return cls_.SetAlmostReadyMatSpeed(newAlmostReadyMatSpeed); }, pybind11::arg("newAlmostReadyMatSpeed"));
	cl_TimeBombPickup.def("GetImpulseForce", [](TimeBombPickup& cls_) { return cls_.GetImpulseForce(); });
	cl_TimeBombPickup.def("SetImpulseForce", [](TimeBombPickup& cls_, float newImpulseForce) { return cls_.SetImpulseForce(newImpulseForce); }, pybind11::arg("newImpulseForce"));
	cl_TimeBombPickup.def("GetCarVerticalForce", [](TimeBombPickup& cls_) { return cls_.GetCarVerticalForce(); });
	cl_TimeBombPickup.def("SetCarVerticalForce", [](TimeBombPickup& cls_, float newCarVerticalForce) { return cls_.SetCarVerticalForce(newCarVerticalForce); }, pybind11::arg("newCarVerticalForce"));
	cl_TimeBombPickup.def("GetCarTorque", [](TimeBombPickup& cls_) { return cls_.GetCarTorque(); });
	cl_TimeBombPickup.def("SetCarTorque", [](TimeBombPickup& cls_, float newCarTorque) { return cls_.SetCarTorque(newCarTorque); }, pybind11::arg("newCarTorque"));
	cl_TimeBombPickup.def("GetbDemolish", [](TimeBombPickup& cls_) { return cls_.GetbDemolish(); });
	cl_TimeBombPickup.def("SetbDemolish", [](TimeBombPickup& cls_, long unsigned int newbDemolish) { return cls_.SetbDemolish(newbDemolish); }, pybind11::arg("newbDemolish"));
	cl_TimeBombPickup.def("GetbImpulse", [](TimeBombPickup& cls_) { return cls_.GetbImpulse(); });
	cl_TimeBombPickup.def("SetbImpulse", [](TimeBombPickup& cls_, long unsigned int newbImpulse) { return cls_.SetbImpulse(newbImpulse); }, pybind11::arg("newbImpulse"));
	cl_TimeBombPickup.def("PickupEnd", [](TimeBombPickup& cls_) { return cls_.PickupEnd(); });
	cl_TimeBombPickup.def("AlmostReady2", [](TimeBombPickup& cls_) { return cls_.AlmostReady2(); });
	cl_TimeBombPickup.def("PickupStart", [](TimeBombPickup& cls_) { return cls_.PickupStart(); });
}
