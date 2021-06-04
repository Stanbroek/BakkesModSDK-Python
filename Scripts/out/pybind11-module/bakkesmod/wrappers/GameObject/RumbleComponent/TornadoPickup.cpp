void bind_TornadoPickup(pybind11::module& m)
{

	pybind11::class_<TornadoPickup, std::shared_ptr<TornadoPickup>, RumblePickupComponentWrapper> cl_TornadoPickup(m, "TornadoPickup");
	cl_TornadoPickup.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_TornadoPickup.def(pybind11::init<TornadoPickup const &>(), pybind11::arg("other"));
	// cl_TornadoPickup.def(pybind11::del<>());
	cl_TornadoPickup.def("GetHeight", [](TornadoPickup& cls_) { return cls_.GetHeight(); });
	cl_TornadoPickup.def("SetHeight", [](TornadoPickup& cls_, float newHeight) { return cls_.SetHeight(newHeight); }, pybind11::arg("newHeight"));
	cl_TornadoPickup.def("GetRadius", [](TornadoPickup& cls_) { return cls_.GetRadius(); });
	cl_TornadoPickup.def("SetRadius", [](TornadoPickup& cls_, float newRadius) { return cls_.SetRadius(newRadius); }, pybind11::arg("newRadius"));
	cl_TornadoPickup.def("GetOffset", [](TornadoPickup& cls_) { return cls_.GetOffset(); });
	cl_TornadoPickup.def("SetOffset", [](TornadoPickup& cls_, Vector newOffset) { return cls_.SetOffset(newOffset); }, pybind11::arg("newOffset"));
	cl_TornadoPickup.def("GetRotationalForce", [](TornadoPickup& cls_) { return cls_.GetRotationalForce(); });
	cl_TornadoPickup.def("SetRotationalForce", [](TornadoPickup& cls_, float newRotationalForce) { return cls_.SetRotationalForce(newRotationalForce); }, pybind11::arg("newRotationalForce"));
	cl_TornadoPickup.def("GetTorque", [](TornadoPickup& cls_) { return cls_.GetTorque(); });
	cl_TornadoPickup.def("SetTorque", [](TornadoPickup& cls_, float newTorque) { return cls_.SetTorque(newTorque); }, pybind11::arg("newTorque"));
	cl_TornadoPickup.def("GetFXScale", [](TornadoPickup& cls_) { return cls_.GetFXScale(); });
	cl_TornadoPickup.def("SetFXScale", [](TornadoPickup& cls_, Vector newFXScale) { return cls_.SetFXScale(newFXScale); }, pybind11::arg("newFXScale"));
	cl_TornadoPickup.def("GetFXOffset", [](TornadoPickup& cls_) { return cls_.GetFXOffset(); });
	cl_TornadoPickup.def("SetFXOffset", [](TornadoPickup& cls_, Vector newFXOffset) { return cls_.SetFXOffset(newFXOffset); }, pybind11::arg("newFXOffset"));
	cl_TornadoPickup.def("GetMeshOffset", [](TornadoPickup& cls_) { return cls_.GetMeshOffset(); });
	cl_TornadoPickup.def("SetMeshOffset", [](TornadoPickup& cls_, Vector newMeshOffset) { return cls_.SetMeshOffset(newMeshOffset); }, pybind11::arg("newMeshOffset"));
	cl_TornadoPickup.def("GetMeshScale", [](TornadoPickup& cls_) { return cls_.GetMeshScale(); });
	cl_TornadoPickup.def("SetMeshScale", [](TornadoPickup& cls_, Vector newMeshScale) { return cls_.SetMeshScale(newMeshScale); }, pybind11::arg("newMeshScale"));
	cl_TornadoPickup.def("GetMaxVelocityOffset", [](TornadoPickup& cls_) { return cls_.GetMaxVelocityOffset(); });
	cl_TornadoPickup.def("SetMaxVelocityOffset", [](TornadoPickup& cls_, float newMaxVelocityOffset) { return cls_.SetMaxVelocityOffset(newMaxVelocityOffset); }, pybind11::arg("newMaxVelocityOffset"));
	cl_TornadoPickup.def("GetBallMultiplier", [](TornadoPickup& cls_) { return cls_.GetBallMultiplier(); });
	cl_TornadoPickup.def("SetBallMultiplier", [](TornadoPickup& cls_, float newBallMultiplier) { return cls_.SetBallMultiplier(newBallMultiplier); }, pybind11::arg("newBallMultiplier"));
	cl_TornadoPickup.def("GetbDebugVis", [](TornadoPickup& cls_) { return cls_.GetbDebugVis(); });
	cl_TornadoPickup.def("SetbDebugVis", [](TornadoPickup& cls_, long unsigned int newbDebugVis) { return cls_.SetbDebugVis(newbDebugVis); }, pybind11::arg("newbDebugVis"));
	cl_TornadoPickup.def("GetVelocityEase", [](TornadoPickup& cls_) { return cls_.GetVelocityEase(); });
	cl_TornadoPickup.def("SetVelocityEase", [](TornadoPickup& cls_, float newVelocityEase) { return cls_.SetVelocityEase(newVelocityEase); }, pybind11::arg("newVelocityEase"));
	cl_TornadoPickup.def("GetVel", [](TornadoPickup& cls_) { return cls_.GetVel(); });
	cl_TornadoPickup.def("SetVel", [](TornadoPickup& cls_, Vector newVel) { return cls_.SetVel(newVel); }, pybind11::arg("newVel"));
	cl_TornadoPickup.def("GetAffecting", [](TornadoPickup& cls_) { return cls_.GetAffecting(); });
	cl_TornadoPickup.def("ApplyForces", [](TornadoPickup& cls_, float ActiveTime) { return cls_.ApplyForces(ActiveTime); }, pybind11::arg("ActiveTime"));
	cl_TornadoPickup.def("PlayCarSFX", [](TornadoPickup& cls_, RBActorWrapper InActor) { return cls_.PlayCarSFX(InActor); }, pybind11::arg("InActor"));
	cl_TornadoPickup.def("PlayBallSFX", [](TornadoPickup& cls_, RBActorWrapper InActor) { return cls_.PlayBallSFX(InActor); }, pybind11::arg("InActor"));
}
