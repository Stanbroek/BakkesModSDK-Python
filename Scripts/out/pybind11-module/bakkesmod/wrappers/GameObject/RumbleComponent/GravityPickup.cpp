void bind_GravityPickup(pybind11::module& m)
{

	pybind11::class_<GravityPickup, std::shared_ptr<GravityPickup>, RumblePickupComponentWrapper> cl_GravityPickup(m, "GravityPickup");
	cl_GravityPickup.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_GravityPickup.def(pybind11::init<GravityPickup const &>(), pybind11::arg("other"));
	// cl_GravityPickup.def(pybind11::del<>());
	cl_GravityPickup.def("GetBallGravity", [](GravityPickup& cls_) { return cls_.GetBallGravity(); });
	cl_GravityPickup.def("SetBallGravity", [](GravityPickup& cls_, float newBallGravity) { return cls_.SetBallGravity(newBallGravity); }, pybind11::arg("newBallGravity"));
	cl_GravityPickup.def("GetRange", [](GravityPickup& cls_) { return cls_.GetRange(); });
	cl_GravityPickup.def("SetRange", [](GravityPickup& cls_, float newRange) { return cls_.SetRange(newRange); }, pybind11::arg("newRange"));
	cl_GravityPickup.def("GetOffset", [](GravityPickup& cls_) { return cls_.GetOffset(); });
	cl_GravityPickup.def("SetOffset", [](GravityPickup& cls_, Vector newOffset) { return cls_.SetOffset(newOffset); }, pybind11::arg("newOffset"));
	cl_GravityPickup.def("GetbDeactivateOnTouch", [](GravityPickup& cls_) { return cls_.GetbDeactivateOnTouch(); });
	cl_GravityPickup.def("SetbDeactivateOnTouch", [](GravityPickup& cls_, long unsigned int newbDeactivateOnTouch) { return cls_.SetbDeactivateOnTouch(newbDeactivateOnTouch); }, pybind11::arg("newbDeactivateOnTouch"));
	cl_GravityPickup.def("GetRecordBallHitRate", [](GravityPickup& cls_) { return cls_.GetRecordBallHitRate(); });
	cl_GravityPickup.def("SetRecordBallHitRate", [](GravityPickup& cls_, float newRecordBallHitRate) { return cls_.SetRecordBallHitRate(newRecordBallHitRate); }, pybind11::arg("newRecordBallHitRate"));
	cl_GravityPickup.def("GetLastRecordedBallHitTime", [](GravityPickup& cls_) { return cls_.GetLastRecordedBallHitTime(); });
	cl_GravityPickup.def("SetLastRecordedBallHitTime", [](GravityPickup& cls_, float newLastRecordedBallHitTime) { return cls_.SetLastRecordedBallHitTime(newLastRecordedBallHitTime); }, pybind11::arg("newLastRecordedBallHitTime"));
	cl_GravityPickup.def("GetPrevBall", [](GravityPickup& cls_) { return cls_.GetPrevBall(); });
	cl_GravityPickup.def("SetPrevBall", [](GravityPickup& cls_, BallWrapper newPrevBall) { return cls_.SetPrevBall(newPrevBall); }, pybind11::arg("newPrevBall"));
	//cl_GravityPickup.def("HandleHitBall", [](GravityPickup& cls_, CarWrapper InCar, BallWrapper Ball) { return cls_.HandleHitBall(InCar, Ball); }, pybind11::arg("InCar"), pybind11::arg("Ball"));
	cl_GravityPickup.def("UpdateVisual", [](GravityPickup& cls_) { return cls_.UpdateVisual(); });
	cl_GravityPickup.def("ApplyForces", [](GravityPickup& cls_, float ActiveTime) { return cls_.ApplyForces(ActiveTime); }, pybind11::arg("ActiveTime"));
	cl_GravityPickup.def("PickupEnd", [](GravityPickup& cls_) { return cls_.PickupEnd(); });
	cl_GravityPickup.def("PickupStart", [](GravityPickup& cls_) { return cls_.PickupStart(); });
}
