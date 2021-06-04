void bind_BallLassoPickup(pybind11::module& m)
{

	pybind11::class_<BallLassoPickup, std::shared_ptr<BallLassoPickup>, SpringPickup> cl_BallLassoPickup(m, "BallLassoPickup");
	cl_BallLassoPickup.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_BallLassoPickup.def(pybind11::init<BallLassoPickup const &>(), pybind11::arg("other"));
	// cl_BallLassoPickup.def(pybind11::del<>());
	cl_BallLassoPickup.def("ScaleSpringMeshToLocation", [](BallLassoPickup& cls_, Vector & NewLocation, Vector & TargetLocation) { return cls_.ScaleSpringMeshToLocation(NewLocation, TargetLocation); }, pybind11::arg("NewLocation"), pybind11::arg("TargetLocation"));
	cl_BallLassoPickup.def("DoSpring", [](BallLassoPickup& cls_, long unsigned int bFirstHit) { return cls_.DoSpring(bFirstHit); }, pybind11::arg("bFirstHit"));
}
