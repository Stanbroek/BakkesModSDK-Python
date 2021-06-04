void bind_VehiclePickupWrapper(pybind11::module& m)
{

	pybind11::class_<VehiclePickupWrapper, std::shared_ptr<VehiclePickupWrapper>, ActorWrapper> cl_VehiclePickupWrapper(m, "VehiclePickupWrapper");
	cl_VehiclePickupWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_VehiclePickupWrapper.def(pybind11::init<VehiclePickupWrapper const &>(), pybind11::arg("other"));
	// cl_VehiclePickupWrapper.def(pybind11::del<>());
	cl_VehiclePickupWrapper.def("GetRespawnDelay", [](VehiclePickupWrapper& cls_) { return cls_.GetRespawnDelay(); });
	cl_VehiclePickupWrapper.def("SetRespawnDelay", [](VehiclePickupWrapper& cls_, float newRespawnDelay) { return cls_.SetRespawnDelay(newRespawnDelay); }, pybind11::arg("newRespawnDelay"));
	cl_VehiclePickupWrapper.def("GetFXActorArchetype", [](VehiclePickupWrapper& cls_) { return cls_.GetFXActorArchetype(); });
	cl_VehiclePickupWrapper.def("SetFXActorArchetype", [](VehiclePickupWrapper& cls_, FXActorWrapper newFXActorArchetype) { return cls_.SetFXActorArchetype(newFXActorArchetype); }, pybind11::arg("newFXActorArchetype"));
	cl_VehiclePickupWrapper.def("GetFXActor", [](VehiclePickupWrapper& cls_) { return cls_.GetFXActor(); });
	cl_VehiclePickupWrapper.def("SetFXActor", [](VehiclePickupWrapper& cls_, FXActorWrapper newFXActor) { return cls_.SetFXActor(newFXActor); }, pybind11::arg("newFXActor"));
	cl_VehiclePickupWrapper.def("GetbPickedUp", [](VehiclePickupWrapper& cls_) { return cls_.GetbPickedUp(); });
	cl_VehiclePickupWrapper.def("SetbPickedUp", [](VehiclePickupWrapper& cls_, long unsigned int newbPickedUp) { return cls_.SetbPickedUp(newbPickedUp); }, pybind11::arg("newbPickedUp"));
	cl_VehiclePickupWrapper.def("GetbNetRelevant", [](VehiclePickupWrapper& cls_) { return cls_.GetbNetRelevant(); });
	cl_VehiclePickupWrapper.def("SetbNetRelevant", [](VehiclePickupWrapper& cls_, long unsigned int newbNetRelevant) { return cls_.SetbNetRelevant(newbNetRelevant); }, pybind11::arg("newbNetRelevant"));
	cl_VehiclePickupWrapper.def("GetbNoPickup", [](VehiclePickupWrapper& cls_) { return cls_.GetbNoPickup(); });
	cl_VehiclePickupWrapper.def("SetbNoPickup", [](VehiclePickupWrapper& cls_, long unsigned int newbNoPickup) { return cls_.SetbNoPickup(newbNoPickup); }, pybind11::arg("newbNoPickup"));
	cl_VehiclePickupWrapper.def("PlayPickedUpFX", [](VehiclePickupWrapper& cls_) { return cls_.PlayPickedUpFX(); });
	cl_VehiclePickupWrapper.def("IsTouchingAVehicle", [](VehiclePickupWrapper& cls_) { return cls_.IsTouchingAVehicle(); });
	cl_VehiclePickupWrapper.def("UpdateTickDisabled", [](VehiclePickupWrapper& cls_) { return cls_.UpdateTickDisabled(); });
	cl_VehiclePickupWrapper.def("SetNetRelevant", [](VehiclePickupWrapper& cls_, long unsigned int bRelevant) { return cls_.SetNetRelevant(bRelevant); }, pybind11::arg("bRelevant"));
	cl_VehiclePickupWrapper.def("Respawn2", [](VehiclePickupWrapper& cls_) { return cls_.Respawn2(); });
	cl_VehiclePickupWrapper.def("SetPickedUp", [](VehiclePickupWrapper& cls_, long unsigned int bNewPickedUp, CarWrapper InInstigator) { return cls_.SetPickedUp(bNewPickedUp, InInstigator); }, pybind11::arg("bNewPickedUp"), pybind11::arg("InInstigator"));
	cl_VehiclePickupWrapper.def("Pickup2", [](VehiclePickupWrapper& cls_, CarWrapper Car) { return cls_.Pickup2(Car); }, pybind11::arg("Car"));
	cl_VehiclePickupWrapper.def("CanPickup", [](VehiclePickupWrapper& cls_, CarWrapper Car) { return cls_.CanPickup(Car); }, pybind11::arg("Car"));
	cl_VehiclePickupWrapper.def("OnTouch", [](VehiclePickupWrapper& cls_, CarWrapper Car) { return cls_.OnTouch(Car); }, pybind11::arg("Car"));
	cl_VehiclePickupWrapper.def("eventTouch", [](VehiclePickupWrapper& cls_, ActorWrapper Other, PrimitiveComponentWrapper OtherComp, Vector & HitLocation, Vector & HitNormal) { return cls_.eventTouch(Other, OtherComp, HitLocation, HitNormal); }, pybind11::arg("Other"), pybind11::arg("OtherComp"), pybind11::arg("HitLocation"), pybind11::arg("HitNormal"));
	cl_VehiclePickupWrapper.def("OnPickUp", [](VehiclePickupWrapper& cls_) { return cls_.OnPickUp(); });
	cl_VehiclePickupWrapper.def("OnSpawn", [](VehiclePickupWrapper& cls_) { return cls_.OnSpawn(); });
	cl_VehiclePickupWrapper.def("SetNoPickup", [](VehiclePickupWrapper& cls_) { return cls_.SetNoPickup(); });
	cl_VehiclePickupWrapper.def("SetupReplicateNoPickup", [](VehiclePickupWrapper& cls_) { return cls_.SetupReplicateNoPickup(); });
	cl_VehiclePickupWrapper.def("InitFX", [](VehiclePickupWrapper& cls_) { return cls_.InitFX(); });
	cl_VehiclePickupWrapper.def("eventPostBeginPlay", [](VehiclePickupWrapper& cls_) { return cls_.eventPostBeginPlay(); });
	cl_VehiclePickupWrapper.def("eventPreBeginPlay", [](VehiclePickupWrapper& cls_) { return cls_.eventPreBeginPlay(); });
	cl_VehiclePickupWrapper.def("EventPickedUp", [](VehiclePickupWrapper& cls_, VehiclePickupWrapper Pickup) { return cls_.EventPickedUp(Pickup); }, pybind11::arg("Pickup"));
	cl_VehiclePickupWrapper.def("EventSpawned", [](VehiclePickupWrapper& cls_, VehiclePickupWrapper Pickup) { return cls_.EventSpawned(Pickup); }, pybind11::arg("Pickup"));
}
