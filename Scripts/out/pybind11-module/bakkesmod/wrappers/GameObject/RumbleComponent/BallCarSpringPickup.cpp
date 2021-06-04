void bind_BallCarSpringPickup(pybind11::module& m)
{

	pybind11::class_<BallCarSpringPickup, std::shared_ptr<BallCarSpringPickup>, SpringPickup> cl_BallCarSpringPickup(m, "BallCarSpringPickup");
	cl_BallCarSpringPickup.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_BallCarSpringPickup.def(pybind11::init<BallCarSpringPickup const &>(), pybind11::arg("other"));
	// cl_BallCarSpringPickup.def(pybind11::del<>());
	cl_BallCarSpringPickup.def("ScaleSpringMeshToLocation", [](BallCarSpringPickup& cls_, Vector & NewLocation, Vector & TargetLocation) { return cls_.ScaleSpringMeshToLocation(NewLocation, TargetLocation); }, pybind11::arg("NewLocation"), pybind11::arg("TargetLocation"));
}
