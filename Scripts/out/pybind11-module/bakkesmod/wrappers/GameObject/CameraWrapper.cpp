void bind_CameraWrapper(pybind11::module& m)
{

	pybind11::class_<CameraWrapper, std::shared_ptr<CameraWrapper>, CameraXWrapper> cl_CameraWrapper(m, "CameraWrapper");
	cl_CameraWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_CameraWrapper.def(pybind11::init<CameraWrapper const &>(), pybind11::arg("other"));
	// cl_CameraWrapper.def(pybind11::del<>());
	cl_CameraWrapper.def("GetLocation", [](CameraWrapper& cls_) { return cls_.GetLocation(); });
	cl_CameraWrapper.def("SetLocation", [](CameraWrapper& cls_, Vector location) { return cls_.SetLocation(location); }, pybind11::arg("location"));
	cl_CameraWrapper.def("GetRotation", [](CameraWrapper& cls_) { return cls_.GetRotation(); });
	cl_CameraWrapper.def("SetRotation", [](CameraWrapper& cls_, Rotator rotation) { return cls_.SetRotation(rotation); }, pybind11::arg("rotation"));
	cl_CameraWrapper.def("GetCameraSettings", [](CameraWrapper& cls_) { return cls_.GetCameraSettings(); });
	cl_CameraWrapper.def("SetCameraSettings", [](CameraWrapper& cls_, ProfileCameraSettings settings) { return cls_.SetCameraSettings(settings); }, pybind11::arg("settings"));
	cl_CameraWrapper.def("IsCameraShakeOn", [](CameraWrapper& cls_) { return cls_.IsCameraShakeOn(); });
	cl_CameraWrapper.def("GetPOV", [](CameraWrapper& cls_) { return cls_.GetPOV(); });
	cl_CameraWrapper.def("SetPOV", [](CameraWrapper& cls_, POV pov) { return cls_.SetPOV(pov); }, pybind11::arg("pov"));
	cl_CameraWrapper.def("SetFOV", [](CameraWrapper& cls_, float fov) { return cls_.SetFOV(fov); }, pybind11::arg("fov"));
	cl_CameraWrapper.def("GetFOV", [](CameraWrapper& cls_) { return cls_.GetFOV(); });
	cl_CameraWrapper.def("SetLockedFOV", [](CameraWrapper& cls_, bool lock) { return cls_.SetLockedFOV(lock); }, pybind11::arg("lock"));
	cl_CameraWrapper.def("GetCameraAsActor", [](CameraWrapper& cls_) { return cls_.GetCameraAsActor(); });
	cl_CameraWrapper.def("GetCameraState", [](CameraWrapper& cls_) { return cls_.GetCameraState(); });
	cl_CameraWrapper.def("SetCameraState", [](CameraWrapper& cls_, std::string stateName) { return cls_.SetCameraState(stateName); }, pybind11::arg("stateName"));
	cl_CameraWrapper.def("linterp", [](CameraWrapper& cls_, Vector start, Vector end, float elapsed, float speed) { return cls_.linterp(start, end, elapsed, speed); }, pybind11::arg("start"), pybind11::arg("end"), pybind11::arg("elapsed"), pybind11::arg("speed"));
	cl_CameraWrapper.def("GetFocusActor", [](CameraWrapper& cls_) { return cls_.GetFocusActor(); });
	cl_CameraWrapper.def("SetFocusActor", [](CameraWrapper& cls_, std::string actorName) { return cls_.SetFocusActor(actorName); }, pybind11::arg("actorName"));
	cl_CameraWrapper.def("SetFlyCamBallTargetMode", [](CameraWrapper& cls_) { return cls_.SetFlyCamBallTargetMode(); });
	cl_CameraWrapper.def("GetSwivelFastSpeed", [](CameraWrapper& cls_) { return cls_.GetSwivelFastSpeed(); });
	cl_CameraWrapper.def("SetSwivelFastSpeed", [](CameraWrapper& cls_, float newSwivelFastSpeed) { return cls_.SetSwivelFastSpeed(newSwivelFastSpeed); }, pybind11::arg("newSwivelFastSpeed"));
	cl_CameraWrapper.def("GetSwivelDieRate", [](CameraWrapper& cls_) { return cls_.GetSwivelDieRate(); });
	cl_CameraWrapper.def("SetSwivelDieRate", [](CameraWrapper& cls_, float newSwivelDieRate) { return cls_.SetSwivelDieRate(newSwivelDieRate); }, pybind11::arg("newSwivelDieRate"));
	cl_CameraWrapper.def("GetCameraPresetSettings", [](CameraWrapper& cls_) { return cls_.GetCameraPresetSettings(); });
	cl_CameraWrapper.def("GetHorizontalSplitscreenHeightOffset", [](CameraWrapper& cls_) { return cls_.GetHorizontalSplitscreenHeightOffset(); });
	cl_CameraWrapper.def("SetHorizontalSplitscreenHeightOffset", [](CameraWrapper& cls_, float newHorizontalSplitscreenHeightOffset) { return cls_.SetHorizontalSplitscreenHeightOffset(newHorizontalSplitscreenHeightOffset); }, pybind11::arg("newHorizontalSplitscreenHeightOffset"));
	cl_CameraWrapper.def("GetHorizontalSplitscreenFOVOffset", [](CameraWrapper& cls_) { return cls_.GetHorizontalSplitscreenFOVOffset(); });
	cl_CameraWrapper.def("SetHorizontalSplitscreenFOVOffset", [](CameraWrapper& cls_, float newHorizontalSplitscreenFOVOffset) { return cls_.SetHorizontalSplitscreenFOVOffset(newHorizontalSplitscreenFOVOffset); }, pybind11::arg("newHorizontalSplitscreenFOVOffset"));
	cl_CameraWrapper.def("GetVerticalSplitscreenFOVOffset", [](CameraWrapper& cls_) { return cls_.GetVerticalSplitscreenFOVOffset(); });
	cl_CameraWrapper.def("SetVerticalSplitscreenFOVOffset", [](CameraWrapper& cls_, float newVerticalSplitscreenFOVOffset) { return cls_.SetVerticalSplitscreenFOVOffset(newVerticalSplitscreenFOVOffset); }, pybind11::arg("newVerticalSplitscreenFOVOffset"));
	cl_CameraWrapper.def("GetClipRate", [](CameraWrapper& cls_) { return cls_.GetClipRate(); });
	cl_CameraWrapper.def("SetClipRate", [](CameraWrapper& cls_, float newClipRate) { return cls_.SetClipRate(newClipRate); }, pybind11::arg("newClipRate"));
	cl_CameraWrapper.def("GetCurrentSwivel", [](CameraWrapper& cls_) { return cls_.GetCurrentSwivel(); });
	cl_CameraWrapper.def("SetCurrentSwivel", [](CameraWrapper& cls_, Rotator newCurrentSwivel) { return cls_.SetCurrentSwivel(newCurrentSwivel); }, pybind11::arg("newCurrentSwivel"));
	cl_CameraWrapper.def("GetDemolisher", [](CameraWrapper& cls_) { return cls_.GetDemolisher(); });
	cl_CameraWrapper.def("SetDemolisher", [](CameraWrapper& cls_, RBActorWrapper newDemolisher) { return cls_.SetDemolisher(newDemolisher); }, pybind11::arg("newDemolisher"));
	cl_CameraWrapper.def("GetbDemolished", [](CameraWrapper& cls_) { return cls_.GetbDemolished(); });
	cl_CameraWrapper.def("SetbDemolished", [](CameraWrapper& cls_, long unsigned int newbDemolished) { return cls_.SetbDemolished(newbDemolished); }, pybind11::arg("newbDemolished"));
	cl_CameraWrapper.def("ClipToField", [](CameraWrapper& cls_, float CameraLocationZ) { return cls_.ClipToField(CameraLocationZ); }, pybind11::arg("CameraLocationZ"));
	cl_CameraWrapper.def("Demolished2", [](CameraWrapper& cls_, RBActorWrapper InDemolisher) { return cls_.Demolished2(InDemolisher); }, pybind11::arg("InDemolisher"));
	cl_CameraWrapper.def("GetDesiredSwivel", [](CameraWrapper& cls_, float LookUp, float LookRight) { return cls_.GetDesiredSwivel(LookUp, LookRight); }, pybind11::arg("LookUp"), pybind11::arg("LookRight"));
	cl_CameraWrapper.def("UpdateSwivel", [](CameraWrapper& cls_, float DeltaTime) { return cls_.UpdateSwivel(DeltaTime); }, pybind11::arg("DeltaTime"));
	cl_CameraWrapper.def("GetDefaultFOVOffset", [](CameraWrapper& cls_) { return cls_.GetDefaultFOVOffset(); });
	cl_CameraWrapper.def("GetDefaultViewHeightOffset", [](CameraWrapper& cls_) { return cls_.GetDefaultViewHeightOffset(); });
	cl_CameraWrapper.def("UpdateFOV", [](CameraWrapper& cls_) { return cls_.UpdateFOV(); });
	cl_CameraWrapper.def("EventCameraTargetChanged", [](CameraWrapper& cls_, CameraWrapper Camera, ActorWrapper Target) { return cls_.EventCameraTargetChanged(Camera, Target); }, pybind11::arg("Camera"), pybind11::arg("Target"));
}