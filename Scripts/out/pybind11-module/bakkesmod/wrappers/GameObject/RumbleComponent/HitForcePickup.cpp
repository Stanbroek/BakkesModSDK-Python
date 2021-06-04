void bind_HitForcePickup(pybind11::module& m)
{

	pybind11::class_<HitForcePickup, std::shared_ptr<HitForcePickup>, RumblePickupComponentWrapper> cl_HitForcePickup(m, "HitForcePickup");
	cl_HitForcePickup.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_HitForcePickup.def(pybind11::init<HitForcePickup const &>(), pybind11::arg("other"));
	// cl_HitForcePickup.def(pybind11::del<>());
	cl_HitForcePickup.def("GetbBallForce", [](HitForcePickup& cls_) { return cls_.GetbBallForce(); });
	cl_HitForcePickup.def("SetbBallForce", [](HitForcePickup& cls_, long unsigned int newbBallForce) { return cls_.SetbBallForce(newbBallForce); }, pybind11::arg("newbBallForce"));
	cl_HitForcePickup.def("GetbCarForce", [](HitForcePickup& cls_) { return cls_.GetbCarForce(); });
	cl_HitForcePickup.def("SetbCarForce", [](HitForcePickup& cls_, long unsigned int newbCarForce) { return cls_.SetbCarForce(newbCarForce); }, pybind11::arg("newbCarForce"));
	cl_HitForcePickup.def("GetbDemolishCars", [](HitForcePickup& cls_) { return cls_.GetbDemolishCars(); });
	cl_HitForcePickup.def("SetbDemolishCars", [](HitForcePickup& cls_, long unsigned int newbDemolishCars) { return cls_.SetbDemolishCars(newbDemolishCars); }, pybind11::arg("newbDemolishCars"));
	cl_HitForcePickup.def("GetBallHitForce", [](HitForcePickup& cls_) { return cls_.GetBallHitForce(); });
	cl_HitForcePickup.def("SetBallHitForce", [](HitForcePickup& cls_, float newBallHitForce) { return cls_.SetBallHitForce(newBallHitForce); }, pybind11::arg("newBallHitForce"));
	cl_HitForcePickup.def("GetCarHitForce", [](HitForcePickup& cls_) { return cls_.GetCarHitForce(); });
	cl_HitForcePickup.def("SetCarHitForce", [](HitForcePickup& cls_, float newCarHitForce) { return cls_.SetCarHitForce(newCarHitForce); }, pybind11::arg("newCarHitForce"));
	cl_HitForcePickup.def("GetMinFXTime", [](HitForcePickup& cls_) { return cls_.GetMinFXTime(); });
	cl_HitForcePickup.def("SetMinFXTime", [](HitForcePickup& cls_, float newMinFXTime) { return cls_.SetMinFXTime(newMinFXTime); }, pybind11::arg("newMinFXTime"));
	cl_HitForcePickup.def("GetOrigBallHitForce", [](HitForcePickup& cls_) { return cls_.GetOrigBallHitForce(); });
	cl_HitForcePickup.def("SetOrigBallHitForce", [](HitForcePickup& cls_, float newOrigBallHitForce) { return cls_.SetOrigBallHitForce(newOrigBallHitForce); }, pybind11::arg("newOrigBallHitForce"));
	cl_HitForcePickup.def("GetOrigCarHitForce", [](HitForcePickup& cls_) { return cls_.GetOrigCarHitForce(); });
	cl_HitForcePickup.def("SetOrigCarHitForce", [](HitForcePickup& cls_, float newOrigCarHitForce) { return cls_.SetOrigCarHitForce(newOrigCarHitForce); }, pybind11::arg("newOrigCarHitForce"));
	cl_HitForcePickup.def("GetLastFXTime", [](HitForcePickup& cls_) { return cls_.GetLastFXTime(); });
	cl_HitForcePickup.def("SetLastFXTime", [](HitForcePickup& cls_, float newLastFXTime) { return cls_.SetLastFXTime(newLastFXTime); }, pybind11::arg("newLastFXTime"));
	cl_HitForcePickup.def("PickupEnd", [](HitForcePickup& cls_) { return cls_.PickupEnd(); });
	cl_HitForcePickup.def("PickupStart", [](HitForcePickup& cls_) { return cls_.PickupStart(); });
}
