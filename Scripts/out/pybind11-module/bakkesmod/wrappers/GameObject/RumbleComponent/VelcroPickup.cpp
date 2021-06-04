void bind_VelcroPickup(pybind11::module& m)
{

	pybind11::class_<VelcroPickup, std::shared_ptr<VelcroPickup>, RumblePickupComponentWrapper> cl_VelcroPickup(m, "VelcroPickup");
	cl_VelcroPickup.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_VelcroPickup.def(pybind11::init<VelcroPickup const &>(), pybind11::arg("other"));
	// cl_VelcroPickup.def(pybind11::del<>());
	cl_VelcroPickup.def("GetBallOffset", [](VelcroPickup& cls_) { return cls_.GetBallOffset(); });
	cl_VelcroPickup.def("SetBallOffset", [](VelcroPickup& cls_, Vector newBallOffset) { return cls_.SetBallOffset(newBallOffset); }, pybind11::arg("newBallOffset"));
	cl_VelcroPickup.def("GetbUseRealOffset", [](VelcroPickup& cls_) { return cls_.GetbUseRealOffset(); });
	cl_VelcroPickup.def("SetbUseRealOffset", [](VelcroPickup& cls_, long unsigned int newbUseRealOffset) { return cls_.SetbUseRealOffset(newbUseRealOffset); }, pybind11::arg("newbUseRealOffset"));
	cl_VelcroPickup.def("GetbHit", [](VelcroPickup& cls_) { return cls_.GetbHit(); });
	cl_VelcroPickup.def("SetbHit", [](VelcroPickup& cls_, long unsigned int newbHit) { return cls_.SetbHit(newbHit); }, pybind11::arg("newbHit"));
	cl_VelcroPickup.def("GetbBroken", [](VelcroPickup& cls_) { return cls_.GetbBroken(); });
	cl_VelcroPickup.def("SetbBroken", [](VelcroPickup& cls_, long unsigned int newbBroken) { return cls_.SetbBroken(newbBroken); }, pybind11::arg("newbBroken"));
	cl_VelcroPickup.def("GetAfterHitDuration", [](VelcroPickup& cls_) { return cls_.GetAfterHitDuration(); });
	cl_VelcroPickup.def("SetAfterHitDuration", [](VelcroPickup& cls_, float newAfterHitDuration) { return cls_.SetAfterHitDuration(newAfterHitDuration); }, pybind11::arg("newAfterHitDuration"));
	cl_VelcroPickup.def("GetPostBreakDuration", [](VelcroPickup& cls_) { return cls_.GetPostBreakDuration(); });
	cl_VelcroPickup.def("SetPostBreakDuration", [](VelcroPickup& cls_, float newPostBreakDuration) { return cls_.SetPostBreakDuration(newPostBreakDuration); }, pybind11::arg("newPostBreakDuration"));
	cl_VelcroPickup.def("GetMinBreakForce", [](VelcroPickup& cls_) { return cls_.GetMinBreakForce(); });
	cl_VelcroPickup.def("SetMinBreakForce", [](VelcroPickup& cls_, float newMinBreakForce) { return cls_.SetMinBreakForce(newMinBreakForce); }, pybind11::arg("newMinBreakForce"));
	cl_VelcroPickup.def("GetMinBreakTime", [](VelcroPickup& cls_) { return cls_.GetMinBreakTime(); });
	cl_VelcroPickup.def("SetMinBreakTime", [](VelcroPickup& cls_, float newMinBreakTime) { return cls_.SetMinBreakTime(newMinBreakTime); }, pybind11::arg("newMinBreakTime"));
	cl_VelcroPickup.def("GetCheckLastTouchRate", [](VelcroPickup& cls_) { return cls_.GetCheckLastTouchRate(); });
	cl_VelcroPickup.def("SetCheckLastTouchRate", [](VelcroPickup& cls_, float newCheckLastTouchRate) { return cls_.SetCheckLastTouchRate(newCheckLastTouchRate); }, pybind11::arg("newCheckLastTouchRate"));
	cl_VelcroPickup.def("GetWeldedBall", [](VelcroPickup& cls_) { return cls_.GetWeldedBall(); });
	cl_VelcroPickup.def("SetWeldedBall", [](VelcroPickup& cls_, BallWrapper newWeldedBall) { return cls_.SetWeldedBall(newWeldedBall); }, pybind11::arg("newWeldedBall"));
	cl_VelcroPickup.def("GetOldBallMass", [](VelcroPickup& cls_) { return cls_.GetOldBallMass(); });
	cl_VelcroPickup.def("SetOldBallMass", [](VelcroPickup& cls_, float newOldBallMass) { return cls_.SetOldBallMass(newOldBallMass); }, pybind11::arg("newOldBallMass"));
	cl_VelcroPickup.def("GetAttachTime", [](VelcroPickup& cls_) { return cls_.GetAttachTime(); });
	cl_VelcroPickup.def("SetAttachTime", [](VelcroPickup& cls_, float newAttachTime) { return cls_.SetAttachTime(newAttachTime); }, pybind11::arg("newAttachTime"));
	cl_VelcroPickup.def("GetLastTouchCheckTime", [](VelcroPickup& cls_) { return cls_.GetLastTouchCheckTime(); });
	cl_VelcroPickup.def("SetLastTouchCheckTime", [](VelcroPickup& cls_, float newLastTouchCheckTime) { return cls_.SetLastTouchCheckTime(newLastTouchCheckTime); }, pybind11::arg("newLastTouchCheckTime"));
	cl_VelcroPickup.def("GetBreakTime", [](VelcroPickup& cls_) { return cls_.GetBreakTime(); });
	cl_VelcroPickup.def("SetBreakTime", [](VelcroPickup& cls_, float newBreakTime) { return cls_.SetBreakTime(newBreakTime); }, pybind11::arg("newBreakTime"));
	cl_VelcroPickup.def("DoBreak", [](VelcroPickup& cls_) { return cls_.DoBreak(); });
	cl_VelcroPickup.def("HandleCarTouch", [](VelcroPickup& cls_, BallWrapper InBall, CarWrapper InCar, unsigned char HitType) { return cls_.HandleCarTouch(InBall, InCar, HitType); }, pybind11::arg("InBall"), pybind11::arg("InCar"), pybind11::arg("HitType"));
	cl_VelcroPickup.def("PickupEnd", [](VelcroPickup& cls_) { return cls_.PickupEnd(); });
	cl_VelcroPickup.def("OnBallHit", [](VelcroPickup& cls_) { return cls_.OnBallHit(); });
	//cl_VelcroPickup.def("HandleHitBall", [](VelcroPickup& cls_, CarWrapper InCar, BallWrapper InBall) { return cls_.HandleHitBall(InCar, InBall); }, pybind11::arg("InCar"), pybind11::arg("InBall"));
	cl_VelcroPickup.def("PickupStart", [](VelcroPickup& cls_) { return cls_.PickupStart(); });
}
