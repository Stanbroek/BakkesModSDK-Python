void bind_CameraXWrapper(pybind11::module& m)
{

	pybind11::class_<CameraXWrapper, std::shared_ptr<CameraXWrapper>, BaseCameraWrapper> cl_CameraXWrapper(m, "CameraXWrapper");
	cl_CameraXWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_CameraXWrapper.def(pybind11::init<CameraXWrapper const &>(), pybind11::arg("other"));
	// cl_CameraXWrapper.def(pybind11::del<>());
	cl_CameraXWrapper.def("GetPCDeltaRotation", [](CameraXWrapper& cls_) { return cls_.GetPCDeltaRotation(); });
	cl_CameraXWrapper.def("SetPCDeltaRotation", [](CameraXWrapper& cls_, Rotator newPCDeltaRotation) { return cls_.SetPCDeltaRotation(newPCDeltaRotation); }, pybind11::arg("newPCDeltaRotation"));
	cl_CameraXWrapper.def("GetOldControllerRotation", [](CameraXWrapper& cls_) { return cls_.GetOldControllerRotation(); });
	cl_CameraXWrapper.def("SetOldControllerRotation", [](CameraXWrapper& cls_, Rotator newOldControllerRotation) { return cls_.SetOldControllerRotation(newOldControllerRotation); }, pybind11::arg("newOldControllerRotation"));
	cl_CameraXWrapper.def("GetPCDeltaLocation", [](CameraXWrapper& cls_) { return cls_.GetPCDeltaLocation(); });
	cl_CameraXWrapper.def("SetPCDeltaLocation", [](CameraXWrapper& cls_, Vector newPCDeltaLocation) { return cls_.SetPCDeltaLocation(newPCDeltaLocation); }, pybind11::arg("newPCDeltaLocation"));
	cl_CameraXWrapper.def("GetOldControllerLocation", [](CameraXWrapper& cls_) { return cls_.GetOldControllerLocation(); });
	cl_CameraXWrapper.def("SetOldControllerLocation", [](CameraXWrapper& cls_, Vector newOldControllerLocation) { return cls_.SetOldControllerLocation(newOldControllerLocation); }, pybind11::arg("newOldControllerLocation"));
	cl_CameraXWrapper.def("GetShakeLocationOffset", [](CameraXWrapper& cls_) { return cls_.GetShakeLocationOffset(); });
	cl_CameraXWrapper.def("SetShakeLocationOffset", [](CameraXWrapper& cls_, Vector newShakeLocationOffset) { return cls_.SetShakeLocationOffset(newShakeLocationOffset); }, pybind11::arg("newShakeLocationOffset"));
	cl_CameraXWrapper.def("GetShakeRotationOffset", [](CameraXWrapper& cls_) { return cls_.GetShakeRotationOffset(); });
	cl_CameraXWrapper.def("SetShakeRotationOffset", [](CameraXWrapper& cls_, Rotator newShakeRotationOffset) { return cls_.SetShakeRotationOffset(newShakeRotationOffset); }, pybind11::arg("newShakeRotationOffset"));
	cl_CameraXWrapper.def("GetShakeFOVOffset", [](CameraXWrapper& cls_) { return cls_.GetShakeFOVOffset(); });
	cl_CameraXWrapper.def("SetShakeFOVOffset", [](CameraXWrapper& cls_, float newShakeFOVOffset) { return cls_.SetShakeFOVOffset(newShakeFOVOffset); }, pybind11::arg("newShakeFOVOffset"));
	cl_CameraXWrapper.def("GetStartFadeColor", [](CameraXWrapper& cls_) { return cls_.GetStartFadeColor(); });
	cl_CameraXWrapper.def("SetStartFadeColor", [](CameraXWrapper& cls_, UnrealColor newStartFadeColor) { return cls_.SetStartFadeColor(newStartFadeColor); }, pybind11::arg("newStartFadeColor"));
	cl_CameraXWrapper.def("GetEndFadeColor", [](CameraXWrapper& cls_) { return cls_.GetEndFadeColor(); });
	cl_CameraXWrapper.def("SetEndFadeColor", [](CameraXWrapper& cls_, UnrealColor newEndFadeColor) { return cls_.SetEndFadeColor(newEndFadeColor); }, pybind11::arg("newEndFadeColor"));
	cl_CameraXWrapper.def("GetClipOffset", [](CameraXWrapper& cls_) { return cls_.GetClipOffset(); });
	cl_CameraXWrapper.def("SetClipOffset", [](CameraXWrapper& cls_, Vector newClipOffset) { return cls_.SetClipOffset(newClipOffset); }, pybind11::arg("newClipOffset"));
	cl_CameraXWrapper.def("GetbDisableCameraShake", [](CameraXWrapper& cls_) { return cls_.GetbDisableCameraShake(); });
	cl_CameraXWrapper.def("SetbDisableCameraShake", [](CameraXWrapper& cls_, long unsigned int newbDisableCameraShake) { return cls_.SetbDisableCameraShake(newbDisableCameraShake); }, pybind11::arg("newbDisableCameraShake"));
	cl_CameraXWrapper.def("GetbSnapNextTransition", [](CameraXWrapper& cls_) { return cls_.GetbSnapNextTransition(); });
	cl_CameraXWrapper.def("SetbSnapNextTransition", [](CameraXWrapper& cls_, long unsigned int newbSnapNextTransition) { return cls_.SetbSnapNextTransition(newbSnapNextTransition); }, pybind11::arg("newbSnapNextTransition"));
	cl_CameraXWrapper.def("eventOnViewTargetChanged", [](CameraXWrapper& cls_) { return cls_.eventOnViewTargetChanged(); });
	cl_CameraXWrapper.def("IsTransitioning", [](CameraXWrapper& cls_) { return cls_.IsTransitioning(); });
	cl_CameraXWrapper.def("SnapTransition", [](CameraXWrapper& cls_) { return cls_.SnapTransition(); });
	cl_CameraXWrapper.def("CopyFade", [](CameraXWrapper& cls_, CameraXWrapper Other) { return cls_.CopyFade(Other); }, pybind11::arg("Other"));
	cl_CameraXWrapper.def("UpdateFade", [](CameraXWrapper& cls_, float DeltaTime) { return cls_.UpdateFade(DeltaTime); }, pybind11::arg("DeltaTime"));
	cl_CameraXWrapper.def("eventUpdateCamera", [](CameraXWrapper& cls_, float DeltaTime) { return cls_.eventUpdateCamera(DeltaTime); }, pybind11::arg("DeltaTime"));
	cl_CameraXWrapper.def("RemoveRoll", [](CameraXWrapper& cls_, Rotator & InRot) { return cls_.RemoveRoll(InRot); }, pybind11::arg("InRot"));
	cl_CameraXWrapper.def("UpdateCameraState", [](CameraXWrapper& cls_) { return cls_.UpdateCameraState(); });
	cl_CameraXWrapper.def("InstanceCameraStates", [](CameraXWrapper& cls_) { return cls_.InstanceCameraStates(); });
	cl_CameraXWrapper.def("OnLoadingMovieClosesd", [](CameraXWrapper& cls_) { return cls_.OnLoadingMovieClosesd(); });
	cl_CameraXWrapper.def("eventPostBeginPlay", [](CameraXWrapper& cls_) { return cls_.eventPostBeginPlay(); });
}
