void bind_FXActorWrapper(pybind11::module& m)
{

	pybind11::class_<FXActorWrapper, std::shared_ptr<FXActorWrapper>, ActorWrapper> cl_FXActorWrapper(m, "FXActorWrapper");
	cl_FXActorWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_FXActorWrapper.def(pybind11::init<FXActorWrapper const &>(), pybind11::arg("other"));
	// cl_FXActorWrapper.def(pybind11::del<>());
	cl_FXActorWrapper.def("GetbDeactivateWhenOwnerDestroyed", [](FXActorWrapper& cls_) { return cls_.GetbDeactivateWhenOwnerDestroyed(); });
	cl_FXActorWrapper.def("SetbDeactivateWhenOwnerDestroyed", [](FXActorWrapper& cls_, long unsigned int newbDeactivateWhenOwnerDestroyed) { return cls_.SetbDeactivateWhenOwnerDestroyed(newbDeactivateWhenOwnerDestroyed); }, pybind11::arg("newbDeactivateWhenOwnerDestroyed"));
	cl_FXActorWrapper.def("GetbAllowShadowCasting", [](FXActorWrapper& cls_) { return cls_.GetbAllowShadowCasting(); });
	cl_FXActorWrapper.def("SetbAllowShadowCasting", [](FXActorWrapper& cls_, long unsigned int newbAllowShadowCasting) { return cls_.SetbAllowShadowCasting(newbAllowShadowCasting); }, pybind11::arg("newbAllowShadowCasting"));
	cl_FXActorWrapper.def("GetbAutoActivate", [](FXActorWrapper& cls_) { return cls_.GetbAutoActivate(); });
	cl_FXActorWrapper.def("SetbAutoActivate", [](FXActorWrapper& cls_, long unsigned int newbAutoActivate) { return cls_.SetbAutoActivate(newbAutoActivate); }, pybind11::arg("newbAutoActivate"));
	cl_FXActorWrapper.def("GetbRenderInactive", [](FXActorWrapper& cls_) { return cls_.GetbRenderInactive(); });
	cl_FXActorWrapper.def("SetbRenderInactive", [](FXActorWrapper& cls_, long unsigned int newbRenderInactive) { return cls_.SetbRenderInactive(newbRenderInactive); }, pybind11::arg("newbRenderInactive"));
	cl_FXActorWrapper.def("GetbActive", [](FXActorWrapper& cls_) { return cls_.GetbActive(); });
	cl_FXActorWrapper.def("SetbActive", [](FXActorWrapper& cls_, long unsigned int newbActive) { return cls_.SetbActive(newbActive); }, pybind11::arg("newbActive"));
	cl_FXActorWrapper.def("GetbHadOwner", [](FXActorWrapper& cls_) { return cls_.GetbHadOwner(); });
	cl_FXActorWrapper.def("SetbHadOwner", [](FXActorWrapper& cls_, long unsigned int newbHadOwner) { return cls_.SetbHadOwner(newbHadOwner); }, pybind11::arg("newbHadOwner"));
	cl_FXActorWrapper.def("GetParent", [](FXActorWrapper& cls_) { return cls_.GetParent(); });
	cl_FXActorWrapper.def("SetParent", [](FXActorWrapper& cls_, FXActorWrapper newParent) { return cls_.SetParent(newParent); }, pybind11::arg("newParent"));
	cl_FXActorWrapper.def("GetAttachmentActor", [](FXActorWrapper& cls_) { return cls_.GetAttachmentActor(); });
	cl_FXActorWrapper.def("SetAttachmentActor", [](FXActorWrapper& cls_, ActorWrapper newAttachmentActor) { return cls_.SetAttachmentActor(newAttachmentActor); }, pybind11::arg("newAttachmentActor"));
	cl_FXActorWrapper.def("GetDestroyWaitTime", [](FXActorWrapper& cls_) { return cls_.GetDestroyWaitTime(); });
	cl_FXActorWrapper.def("SetDestroyWaitTime", [](FXActorWrapper& cls_, float newDestroyWaitTime) { return cls_.SetDestroyWaitTime(newDestroyWaitTime); }, pybind11::arg("newDestroyWaitTime"));
	cl_FXActorWrapper.def("GetDestroyTime", [](FXActorWrapper& cls_) { return cls_.GetDestroyTime(); });
	cl_FXActorWrapper.def("SetDestroyTime", [](FXActorWrapper& cls_, float newDestroyTime) { return cls_.SetDestroyTime(newDestroyTime); }, pybind11::arg("newDestroyTime"));
	cl_FXActorWrapper.def("GetEditID", [](FXActorWrapper& cls_) { return cls_.GetEditID(); });
	cl_FXActorWrapper.def("SetEditID", [](FXActorWrapper& cls_, int newEditID) { return cls_.SetEditID(newEditID); }, pybind11::arg("newEditID"));
	cl_FXActorWrapper.def("eventDumpDebugInfo", [](FXActorWrapper& cls_) { return cls_.eventDumpDebugInfo(); });
	cl_FXActorWrapper.def("eventDestroyed", [](FXActorWrapper& cls_) { return cls_.eventDestroyed(); });
	cl_FXActorWrapper.def("Inherit", [](FXActorWrapper& cls_, FXActorWrapper Other) { return cls_.Inherit(Other); }, pybind11::arg("Other"));
	cl_FXActorWrapper.def("ResetParticles", [](FXActorWrapper& cls_) { return cls_.ResetParticles(); });
	cl_FXActorWrapper.def("StopAllEffects", [](FXActorWrapper& cls_) { return cls_.StopAllEffects(); });
	cl_FXActorWrapper.def("eventDeactivateAndDestroy", [](FXActorWrapper& cls_) { return cls_.eventDeactivateAndDestroy(); });
	cl_FXActorWrapper.def("UpdateFXStates", [](FXActorWrapper& cls_) { return cls_.UpdateFXStates(); });
	cl_FXActorWrapper.def("IsLocallyControlled", [](FXActorWrapper& cls_) { return cls_.IsLocallyControlled(); });
	cl_FXActorWrapper.def("Deactivate2", [](FXActorWrapper& cls_) { return cls_.Deactivate2(); });
	cl_FXActorWrapper.def("Activate2", [](FXActorWrapper& cls_) { return cls_.Activate2(); });
	cl_FXActorWrapper.def("BindTo", [](FXActorWrapper& cls_, FXActorWrapper ParentFXActor) { return cls_.BindTo(ParentFXActor); }, pybind11::arg("ParentFXActor"));
	cl_FXActorWrapper.def("SetAttachmentActor2", [](FXActorWrapper& cls_, ActorWrapper AttachToActor) { return cls_.SetAttachmentActor2(AttachToActor); }, pybind11::arg("AttachToActor"));
	cl_FXActorWrapper.def("PostBeginPlay", [](FXActorWrapper& cls_) { return cls_.PostBeginPlay(); });
}
