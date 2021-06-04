void bind_BallFreezePickup(pybind11::module& m)
{

	pybind11::class_<BallFreezePickup, std::shared_ptr<BallFreezePickup>, TargetedPickup> cl_BallFreezePickup(m, "BallFreezePickup");
	cl_BallFreezePickup.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_BallFreezePickup.def(pybind11::init<BallFreezePickup const &>(), pybind11::arg("other"));
	// cl_BallFreezePickup.def(pybind11::del<>());
	cl_BallFreezePickup.def("GetFreezeBreakFXArchetype", [](BallFreezePickup& cls_) { return cls_.GetFreezeBreakFXArchetype(); });
	cl_BallFreezePickup.def("SetFreezeBreakFXArchetype", [](BallFreezePickup& cls_, FXActorWrapper newFreezeBreakFXArchetype) { return cls_.SetFreezeBreakFXArchetype(newFreezeBreakFXArchetype); }, pybind11::arg("newFreezeBreakFXArchetype"));
	cl_BallFreezePickup.def("GetFreezeFXArchetype", [](BallFreezePickup& cls_) { return cls_.GetFreezeFXArchetype(); });
	cl_BallFreezePickup.def("SetFreezeFXArchetype", [](BallFreezePickup& cls_, FXActorWrapper newFreezeFXArchetype) { return cls_.SetFreezeFXArchetype(newFreezeFXArchetype); }, pybind11::arg("newFreezeFXArchetype"));
	cl_BallFreezePickup.def("GetbMaintainMomentum", [](BallFreezePickup& cls_) { return cls_.GetbMaintainMomentum(); });
	cl_BallFreezePickup.def("SetbMaintainMomentum", [](BallFreezePickup& cls_, long unsigned int newbMaintainMomentum) { return cls_.SetbMaintainMomentum(newbMaintainMomentum); }, pybind11::arg("newbMaintainMomentum"));
	cl_BallFreezePickup.def("GetbTouched", [](BallFreezePickup& cls_) { return cls_.GetbTouched(); });
	cl_BallFreezePickup.def("SetbTouched", [](BallFreezePickup& cls_, long unsigned int newbTouched) { return cls_.SetbTouched(newbTouched); }, pybind11::arg("newbTouched"));
	cl_BallFreezePickup.def("GetTimeToStop", [](BallFreezePickup& cls_) { return cls_.GetTimeToStop(); });
	cl_BallFreezePickup.def("SetTimeToStop", [](BallFreezePickup& cls_, float newTimeToStop) { return cls_.SetTimeToStop(newTimeToStop); }, pybind11::arg("newTimeToStop"));
	cl_BallFreezePickup.def("GetStopMomentumPercentage", [](BallFreezePickup& cls_) { return cls_.GetStopMomentumPercentage(); });
	cl_BallFreezePickup.def("SetStopMomentumPercentage", [](BallFreezePickup& cls_, float newStopMomentumPercentage) { return cls_.SetStopMomentumPercentage(newStopMomentumPercentage); }, pybind11::arg("newStopMomentumPercentage"));
	cl_BallFreezePickup.def("GetBall", [](BallFreezePickup& cls_) { return cls_.GetBall(); });
	cl_BallFreezePickup.def("SetBall", [](BallFreezePickup& cls_, BallWrapper newBall) { return cls_.SetBall(newBall); }, pybind11::arg("newBall"));
	cl_BallFreezePickup.def("GetOrigLinearVelocity", [](BallFreezePickup& cls_) { return cls_.GetOrigLinearVelocity(); });
	cl_BallFreezePickup.def("SetOrigLinearVelocity", [](BallFreezePickup& cls_, Vector newOrigLinearVelocity) { return cls_.SetOrigLinearVelocity(newOrigLinearVelocity); }, pybind11::arg("newOrigLinearVelocity"));
	cl_BallFreezePickup.def("GetOrigAngularVelocity", [](BallFreezePickup& cls_) { return cls_.GetOrigAngularVelocity(); });
	cl_BallFreezePickup.def("SetOrigAngularVelocity", [](BallFreezePickup& cls_, Vector newOrigAngularVelocity) { return cls_.SetOrigAngularVelocity(newOrigAngularVelocity); }, pybind11::arg("newOrigAngularVelocity"));
	cl_BallFreezePickup.def("GetOrigSpeed", [](BallFreezePickup& cls_) { return cls_.GetOrigSpeed(); });
	cl_BallFreezePickup.def("SetOrigSpeed", [](BallFreezePickup& cls_, float newOrigSpeed) { return cls_.SetOrigSpeed(newOrigSpeed); }, pybind11::arg("newOrigSpeed"));
	cl_BallFreezePickup.def("GetRepOrigSpeed", [](BallFreezePickup& cls_) { return cls_.GetRepOrigSpeed(); });
	cl_BallFreezePickup.def("SetRepOrigSpeed", [](BallFreezePickup& cls_, float newRepOrigSpeed) { return cls_.SetRepOrigSpeed(newRepOrigSpeed); }, pybind11::arg("newRepOrigSpeed"));
	cl_BallFreezePickup.def("GetFreezeFX", [](BallFreezePickup& cls_) { return cls_.GetFreezeFX(); });
	cl_BallFreezePickup.def("SetFreezeFX", [](BallFreezePickup& cls_, FXActorWrapper newFreezeFX) { return cls_.SetFreezeFX(newFreezeFX); }, pybind11::arg("newFreezeFX"));
	cl_BallFreezePickup.def("PickupEnd", [](BallFreezePickup& cls_) { return cls_.PickupEnd(); });
	cl_BallFreezePickup.def("HandleBallExploded", [](BallFreezePickup& cls_, BallWrapper InBall) { return cls_.HandleBallExploded(InBall); }, pybind11::arg("InBall"));
	cl_BallFreezePickup.def("HandleBallHit", [](BallFreezePickup& cls_, BallWrapper InBall, CarWrapper InCar, unsigned char HitType) { return cls_.HandleBallHit(InBall, InCar, HitType); }, pybind11::arg("InBall"), pybind11::arg("InCar"), pybind11::arg("HitType"));
	cl_BallFreezePickup.def("ApplyForces", [](BallFreezePickup& cls_, float ActiveTime) { return cls_.ApplyForces(ActiveTime); }, pybind11::arg("ActiveTime"));
	cl_BallFreezePickup.def("OnTargetChanged", [](BallFreezePickup& cls_) { return cls_.OnTargetChanged(); });
	cl_BallFreezePickup.def("PickupStart", [](BallFreezePickup& cls_) { return cls_.PickupStart(); });
}
