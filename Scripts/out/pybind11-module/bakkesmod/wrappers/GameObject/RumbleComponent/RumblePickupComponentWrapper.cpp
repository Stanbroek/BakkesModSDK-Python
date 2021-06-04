void bind_RumblePickupComponentWrapper(pybind11::module& m)
{

	pybind11::class_<RumblePickupComponentWrapper, std::shared_ptr<RumblePickupComponentWrapper>, CarComponentWrapper> cl_RumblePickupComponentWrapper(m, "RumblePickupComponentWrapper");
	cl_RumblePickupComponentWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_RumblePickupComponentWrapper.def(pybind11::init<RumblePickupComponentWrapper const &>(), pybind11::arg("other"));
	// cl_RumblePickupComponentWrapper.def(pybind11::del<>());
	cl_RumblePickupComponentWrapper.def("GetPickupName", [](RumblePickupComponentWrapper& cls_) { return cls_.GetPickupName(); });
	cl_RumblePickupComponentWrapper.def("GetbHudIgnoreUseTime", [](RumblePickupComponentWrapper& cls_) { return cls_.GetbHudIgnoreUseTime(); });
	cl_RumblePickupComponentWrapper.def("SetbHudIgnoreUseTime", [](RumblePickupComponentWrapper& cls_, long unsigned int newbHudIgnoreUseTime) { return cls_.SetbHudIgnoreUseTime(newbHudIgnoreUseTime); }, pybind11::arg("newbHudIgnoreUseTime"));
	cl_RumblePickupComponentWrapper.def("GetbHasActivated", [](RumblePickupComponentWrapper& cls_) { return cls_.GetbHasActivated(); });
	cl_RumblePickupComponentWrapper.def("SetbHasActivated", [](RumblePickupComponentWrapper& cls_, long unsigned int newbHasActivated) { return cls_.SetbHasActivated(newbHasActivated); }, pybind11::arg("newbHasActivated"));
	cl_RumblePickupComponentWrapper.def("GetbIsActive", [](RumblePickupComponentWrapper& cls_) { return cls_.GetbIsActive(); });
	cl_RumblePickupComponentWrapper.def("SetbIsActive", [](RumblePickupComponentWrapper& cls_, long unsigned int newbIsActive) { return cls_.SetbIsActive(newbIsActive); }, pybind11::arg("newbIsActive"));
	cl_RumblePickupComponentWrapper.def("GetActivationDuration", [](RumblePickupComponentWrapper& cls_) { return cls_.GetActivationDuration(); });
	cl_RumblePickupComponentWrapper.def("SetActivationDuration", [](RumblePickupComponentWrapper& cls_, float newActivationDuration) { return cls_.SetActivationDuration(newActivationDuration); }, pybind11::arg("newActivationDuration"));
	cl_RumblePickupComponentWrapper.def("GetPickupFXArchetype", [](RumblePickupComponentWrapper& cls_) { return cls_.GetPickupFXArchetype(); });
	cl_RumblePickupComponentWrapper.def("SetPickupFXArchetype", [](RumblePickupComponentWrapper& cls_, FXActorWrapper newPickupFXArchetype) { return cls_.SetPickupFXArchetype(newPickupFXArchetype); }, pybind11::arg("newPickupFXArchetype"));
	cl_RumblePickupComponentWrapper.def("GetPickupFX", [](RumblePickupComponentWrapper& cls_) { return cls_.GetPickupFX(); });
	cl_RumblePickupComponentWrapper.def("SetPickupFX", [](RumblePickupComponentWrapper& cls_, FXActorWrapper newPickupFX) { return cls_.SetPickupFX(newPickupFX); }, pybind11::arg("newPickupFX"));
	cl_RumblePickupComponentWrapper.def("HasActivated2", [](RumblePickupComponentWrapper& cls_) { return cls_.HasActivated2(); });
	cl_RumblePickupComponentWrapper.def("GetClientTarget", [](RumblePickupComponentWrapper& cls_) { return cls_.GetClientTarget(); });
	cl_RumblePickupComponentWrapper.def("OnVehicleSetupComplete", [](RumblePickupComponentWrapper& cls_) { return cls_.OnVehicleSetupComplete(); });
	cl_RumblePickupComponentWrapper.def("GetActiveTimePercent", [](RumblePickupComponentWrapper& cls_) { return cls_.GetActiveTimePercent(); });
	cl_RumblePickupComponentWrapper.def("PickupEnd", [](RumblePickupComponentWrapper& cls_) { return cls_.PickupEnd(); });
	cl_RumblePickupComponentWrapper.def("PickupStart", [](RumblePickupComponentWrapper& cls_) { return cls_.PickupStart(); });
	cl_RumblePickupComponentWrapper.def("GetBoostComponent", [](RumblePickupComponentWrapper& cls_) { return cls_.GetBoostComponent(); });
	cl_RumblePickupComponentWrapper.def("DeactivatePickup", [](RumblePickupComponentWrapper& cls_) { return cls_.DeactivatePickup(); });
	cl_RumblePickupComponentWrapper.def("TryActivate", [](RumblePickupComponentWrapper& cls_, RBActorWrapper TargetOverride) { return cls_.TryActivate(TargetOverride); }, pybind11::arg("TargetOverride"));
	cl_RumblePickupComponentWrapper.def("OnCreated", [](RumblePickupComponentWrapper& cls_) { return cls_.OnCreated(); });
	cl_RumblePickupComponentWrapper.def("CanPickup", [](RumblePickupComponentWrapper& cls_, CarWrapper InCar) { return cls_.CanPickup(InCar); }, pybind11::arg("InCar"));
	cl_RumblePickupComponentWrapper.def("ApplyPickup", [](RumblePickupComponentWrapper& cls_, CarWrapper InCar) { return cls_.ApplyPickup(InCar); }, pybind11::arg("InCar"));
}
