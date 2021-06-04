void bind_TargetedPickup(pybind11::module& m)
{

	pybind11::class_<TargetedPickup, std::shared_ptr<TargetedPickup>, RumblePickupComponentWrapper> cl_TargetedPickup(m, "TargetedPickup");
	cl_TargetedPickup.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_TargetedPickup.def(pybind11::init<TargetedPickup const &>(), pybind11::arg("other"));
	// cl_TargetedPickup.def(pybind11::del<>());
	cl_TargetedPickup.def("GetbCanTargetBall", [](TargetedPickup& cls_) { return cls_.GetbCanTargetBall(); });
	cl_TargetedPickup.def("SetbCanTargetBall", [](TargetedPickup& cls_, long unsigned int newbCanTargetBall) { return cls_.SetbCanTargetBall(newbCanTargetBall); }, pybind11::arg("newbCanTargetBall"));
	cl_TargetedPickup.def("GetbCanTargetCars", [](TargetedPickup& cls_) { return cls_.GetbCanTargetCars(); });
	cl_TargetedPickup.def("SetbCanTargetCars", [](TargetedPickup& cls_, long unsigned int newbCanTargetCars) { return cls_.SetbCanTargetCars(newbCanTargetCars); }, pybind11::arg("newbCanTargetCars"));
	cl_TargetedPickup.def("GetbCanTargetEnemyCars", [](TargetedPickup& cls_) { return cls_.GetbCanTargetEnemyCars(); });
	cl_TargetedPickup.def("SetbCanTargetEnemyCars", [](TargetedPickup& cls_, long unsigned int newbCanTargetEnemyCars) { return cls_.SetbCanTargetEnemyCars(newbCanTargetEnemyCars); }, pybind11::arg("newbCanTargetEnemyCars"));
	cl_TargetedPickup.def("GetbCanTargetTeamCars", [](TargetedPickup& cls_) { return cls_.GetbCanTargetTeamCars(); });
	cl_TargetedPickup.def("SetbCanTargetTeamCars", [](TargetedPickup& cls_, long unsigned int newbCanTargetTeamCars) { return cls_.SetbCanTargetTeamCars(newbCanTargetTeamCars); }, pybind11::arg("newbCanTargetTeamCars"));
	cl_TargetedPickup.def("GetbUseDirectionalTargeting", [](TargetedPickup& cls_) { return cls_.GetbUseDirectionalTargeting(); });
	cl_TargetedPickup.def("SetbUseDirectionalTargeting", [](TargetedPickup& cls_, long unsigned int newbUseDirectionalTargeting) { return cls_.SetbUseDirectionalTargeting(newbUseDirectionalTargeting); }, pybind11::arg("newbUseDirectionalTargeting"));
	cl_TargetedPickup.def("GetbRequireTrace", [](TargetedPickup& cls_) { return cls_.GetbRequireTrace(); });
	cl_TargetedPickup.def("SetbRequireTrace", [](TargetedPickup& cls_, long unsigned int newbRequireTrace) { return cls_.SetbRequireTrace(newbRequireTrace); }, pybind11::arg("newbRequireTrace"));
	cl_TargetedPickup.def("GetRange", [](TargetedPickup& cls_) { return cls_.GetRange(); });
	cl_TargetedPickup.def("SetRange", [](TargetedPickup& cls_, float newRange) { return cls_.SetRange(newRange); }, pybind11::arg("newRange"));
	cl_TargetedPickup.def("GetDirectionalTargetingAccuracy", [](TargetedPickup& cls_) { return cls_.GetDirectionalTargetingAccuracy(); });
	cl_TargetedPickup.def("SetDirectionalTargetingAccuracy", [](TargetedPickup& cls_, float newDirectionalTargetingAccuracy) { return cls_.SetDirectionalTargetingAccuracy(newDirectionalTargetingAccuracy); }, pybind11::arg("newDirectionalTargetingAccuracy"));
	cl_TargetedPickup.def("GetClientTarget", [](TargetedPickup& cls_) { return cls_.GetClientTarget(); });
	cl_TargetedPickup.def("SetClientTarget", [](TargetedPickup& cls_, RBActorWrapper newClientTarget) { return cls_.SetClientTarget(newClientTarget); }, pybind11::arg("newClientTarget"));
	cl_TargetedPickup.def("GetTargeted", [](TargetedPickup& cls_) { return cls_.GetTargeted(); });
	cl_TargetedPickup.def("SetTargeted", [](TargetedPickup& cls_, RBActorWrapper newTargeted) { return cls_.SetTargeted(newTargeted); }, pybind11::arg("newTargeted"));
	cl_TargetedPickup.def("GetClientTarget2", [](TargetedPickup& cls_) { return cls_.GetClientTarget2(); });
	cl_TargetedPickup.def("TargetChanged", [](TargetedPickup& cls_) { return cls_.TargetChanged(); });
	cl_TargetedPickup.def("OnTargetChanged", [](TargetedPickup& cls_) { return cls_.OnTargetChanged(); });
	cl_TargetedPickup.def("TryActivate", [](TargetedPickup& cls_, RBActorWrapper TargetOverride) { return cls_.TryActivate(TargetOverride); }, pybind11::arg("TargetOverride"));
	cl_TargetedPickup.def("ValidateTargetTrace", [](TargetedPickup& cls_, RBActorWrapper InTarget) { return cls_.ValidateTargetTrace(InTarget); }, pybind11::arg("InTarget"));
	cl_TargetedPickup.def("ValidateTarget2", [](TargetedPickup& cls_, RBActorWrapper InTarget) { return cls_.ValidateTarget2(InTarget); }, pybind11::arg("InTarget"));
	cl_TargetedPickup.def("GetTarget2", [](TargetedPickup& cls_) { return cls_.GetTarget2(); });
}
