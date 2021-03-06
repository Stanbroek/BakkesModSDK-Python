void bind_BaseCameraWrapper(pybind11::module& m)
{

	pybind11::class_<BaseCameraWrapper, std::shared_ptr<BaseCameraWrapper>, ActorWrapper> cl_BaseCameraWrapper(m, "BaseCameraWrapper");
	cl_BaseCameraWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_BaseCameraWrapper.def(pybind11::init<BaseCameraWrapper const &>(), pybind11::arg("other"));
	// cl_BaseCameraWrapper.def(pybind11::del<>());
	cl_BaseCameraWrapper.def("GetDefaultFOV", [](BaseCameraWrapper& cls_) { return cls_.GetDefaultFOV(); });
	cl_BaseCameraWrapper.def("SetDefaultFOV", [](BaseCameraWrapper& cls_, float newDefaultFOV) { return cls_.SetDefaultFOV(newDefaultFOV); }, pybind11::arg("newDefaultFOV"));
	cl_BaseCameraWrapper.def("GetbLockedFOV", [](BaseCameraWrapper& cls_) { return cls_.GetbLockedFOV(); });
	cl_BaseCameraWrapper.def("SetbLockedFOV", [](BaseCameraWrapper& cls_, long unsigned int newbLockedFOV) { return cls_.SetbLockedFOV(newbLockedFOV); }, pybind11::arg("newbLockedFOV"));
	cl_BaseCameraWrapper.def("GetbConstrainAspectRatio", [](BaseCameraWrapper& cls_) { return cls_.GetbConstrainAspectRatio(); });
	cl_BaseCameraWrapper.def("SetbConstrainAspectRatio", [](BaseCameraWrapper& cls_, long unsigned int newbConstrainAspectRatio) { return cls_.SetbConstrainAspectRatio(newbConstrainAspectRatio); }, pybind11::arg("newbConstrainAspectRatio"));
	cl_BaseCameraWrapper.def("GetbEnableFading", [](BaseCameraWrapper& cls_) { return cls_.GetbEnableFading(); });
	cl_BaseCameraWrapper.def("SetbEnableFading", [](BaseCameraWrapper& cls_, long unsigned int newbEnableFading) { return cls_.SetbEnableFading(newbEnableFading); }, pybind11::arg("newbEnableFading"));
	cl_BaseCameraWrapper.def("GetbFadeAudio", [](BaseCameraWrapper& cls_) { return cls_.GetbFadeAudio(); });
	cl_BaseCameraWrapper.def("SetbFadeAudio", [](BaseCameraWrapper& cls_, long unsigned int newbFadeAudio) { return cls_.SetbFadeAudio(newbFadeAudio); }, pybind11::arg("newbFadeAudio"));
	cl_BaseCameraWrapper.def("GetbForceDisableTemporalAA", [](BaseCameraWrapper& cls_) { return cls_.GetbForceDisableTemporalAA(); });
	cl_BaseCameraWrapper.def("SetbForceDisableTemporalAA", [](BaseCameraWrapper& cls_, long unsigned int newbForceDisableTemporalAA) { return cls_.SetbForceDisableTemporalAA(newbForceDisableTemporalAA); }, pybind11::arg("newbForceDisableTemporalAA"));
	cl_BaseCameraWrapper.def("GetbEnableColorScaling", [](BaseCameraWrapper& cls_) { return cls_.GetbEnableColorScaling(); });
	cl_BaseCameraWrapper.def("SetbEnableColorScaling", [](BaseCameraWrapper& cls_, long unsigned int newbEnableColorScaling) { return cls_.SetbEnableColorScaling(newbEnableColorScaling); }, pybind11::arg("newbEnableColorScaling"));
	cl_BaseCameraWrapper.def("GetbEnableColorScaleInterp", [](BaseCameraWrapper& cls_) { return cls_.GetbEnableColorScaleInterp(); });
	cl_BaseCameraWrapper.def("SetbEnableColorScaleInterp", [](BaseCameraWrapper& cls_, long unsigned int newbEnableColorScaleInterp) { return cls_.SetbEnableColorScaleInterp(newbEnableColorScaleInterp); }, pybind11::arg("newbEnableColorScaleInterp"));
	cl_BaseCameraWrapper.def("GetbUseClientSideCameraUpdates", [](BaseCameraWrapper& cls_) { return cls_.GetbUseClientSideCameraUpdates(); });
	cl_BaseCameraWrapper.def("SetbUseClientSideCameraUpdates", [](BaseCameraWrapper& cls_, long unsigned int newbUseClientSideCameraUpdates) { return cls_.SetbUseClientSideCameraUpdates(newbUseClientSideCameraUpdates); }, pybind11::arg("newbUseClientSideCameraUpdates"));
	cl_BaseCameraWrapper.def("GetbDebugClientSideCamera", [](BaseCameraWrapper& cls_) { return cls_.GetbDebugClientSideCamera(); });
	cl_BaseCameraWrapper.def("SetbDebugClientSideCamera", [](BaseCameraWrapper& cls_, long unsigned int newbDebugClientSideCamera) { return cls_.SetbDebugClientSideCamera(newbDebugClientSideCamera); }, pybind11::arg("newbDebugClientSideCamera"));
	cl_BaseCameraWrapper.def("GetbShouldSendClientSideCameraUpdate", [](BaseCameraWrapper& cls_) { return cls_.GetbShouldSendClientSideCameraUpdate(); });
	cl_BaseCameraWrapper.def("SetbShouldSendClientSideCameraUpdate", [](BaseCameraWrapper& cls_, long unsigned int newbShouldSendClientSideCameraUpdate) { return cls_.SetbShouldSendClientSideCameraUpdate(newbShouldSendClientSideCameraUpdate); }, pybind11::arg("newbShouldSendClientSideCameraUpdate"));
	cl_BaseCameraWrapper.def("GetLockedFOV", [](BaseCameraWrapper& cls_) { return cls_.GetLockedFOV(); });
	cl_BaseCameraWrapper.def("SetLockedFOV", [](BaseCameraWrapper& cls_, float newLockedFOV) { return cls_.SetLockedFOV(newLockedFOV); }, pybind11::arg("newLockedFOV"));
	cl_BaseCameraWrapper.def("GetConstrainedAspectRatio", [](BaseCameraWrapper& cls_) { return cls_.GetConstrainedAspectRatio(); });
	cl_BaseCameraWrapper.def("SetConstrainedAspectRatio", [](BaseCameraWrapper& cls_, float newConstrainedAspectRatio) { return cls_.SetConstrainedAspectRatio(newConstrainedAspectRatio); }, pybind11::arg("newConstrainedAspectRatio"));
	cl_BaseCameraWrapper.def("GetDefaultAspectRatio", [](BaseCameraWrapper& cls_) { return cls_.GetDefaultAspectRatio(); });
	cl_BaseCameraWrapper.def("SetDefaultAspectRatio", [](BaseCameraWrapper& cls_, float newDefaultAspectRatio) { return cls_.SetDefaultAspectRatio(newDefaultAspectRatio); }, pybind11::arg("newDefaultAspectRatio"));
	cl_BaseCameraWrapper.def("GetOffAxisYawAngle", [](BaseCameraWrapper& cls_) { return cls_.GetOffAxisYawAngle(); });
	cl_BaseCameraWrapper.def("SetOffAxisYawAngle", [](BaseCameraWrapper& cls_, float newOffAxisYawAngle) { return cls_.SetOffAxisYawAngle(newOffAxisYawAngle); }, pybind11::arg("newOffAxisYawAngle"));
	cl_BaseCameraWrapper.def("GetOffAxisPitchAngle", [](BaseCameraWrapper& cls_) { return cls_.GetOffAxisPitchAngle(); });
	cl_BaseCameraWrapper.def("SetOffAxisPitchAngle", [](BaseCameraWrapper& cls_, float newOffAxisPitchAngle) { return cls_.SetOffAxisPitchAngle(newOffAxisPitchAngle); }, pybind11::arg("newOffAxisPitchAngle"));
	cl_BaseCameraWrapper.def("GetFadeColor", [](BaseCameraWrapper& cls_) { return cls_.GetFadeColor(); });
	cl_BaseCameraWrapper.def("SetFadeColor", [](BaseCameraWrapper& cls_, UnrealColor newFadeColor) { return cls_.SetFadeColor(newFadeColor); }, pybind11::arg("newFadeColor"));
	cl_BaseCameraWrapper.def("GetFadeAmount", [](BaseCameraWrapper& cls_) { return cls_.GetFadeAmount(); });
	cl_BaseCameraWrapper.def("SetFadeAmount", [](BaseCameraWrapper& cls_, float newFadeAmount) { return cls_.SetFadeAmount(newFadeAmount); }, pybind11::arg("newFadeAmount"));
	cl_BaseCameraWrapper.def("GetCamOverridePostProcessAlpha", [](BaseCameraWrapper& cls_) { return cls_.GetCamOverridePostProcessAlpha(); });
	cl_BaseCameraWrapper.def("SetCamOverridePostProcessAlpha", [](BaseCameraWrapper& cls_, float newCamOverridePostProcessAlpha) { return cls_.SetCamOverridePostProcessAlpha(newCamOverridePostProcessAlpha); }, pybind11::arg("newCamOverridePostProcessAlpha"));
	cl_BaseCameraWrapper.def("GetColorScale", [](BaseCameraWrapper& cls_) { return cls_.GetColorScale(); });
	cl_BaseCameraWrapper.def("SetColorScale", [](BaseCameraWrapper& cls_, Vector newColorScale) { return cls_.SetColorScale(newColorScale); }, pybind11::arg("newColorScale"));
	cl_BaseCameraWrapper.def("GetDesiredColorScale", [](BaseCameraWrapper& cls_) { return cls_.GetDesiredColorScale(); });
	cl_BaseCameraWrapper.def("SetDesiredColorScale", [](BaseCameraWrapper& cls_, Vector newDesiredColorScale) { return cls_.SetDesiredColorScale(newDesiredColorScale); }, pybind11::arg("newDesiredColorScale"));
	cl_BaseCameraWrapper.def("GetOriginalColorScale", [](BaseCameraWrapper& cls_) { return cls_.GetOriginalColorScale(); });
	cl_BaseCameraWrapper.def("SetOriginalColorScale", [](BaseCameraWrapper& cls_, Vector newOriginalColorScale) { return cls_.SetOriginalColorScale(newOriginalColorScale); }, pybind11::arg("newOriginalColorScale"));
	cl_BaseCameraWrapper.def("GetColorScaleInterpDuration", [](BaseCameraWrapper& cls_) { return cls_.GetColorScaleInterpDuration(); });
	cl_BaseCameraWrapper.def("SetColorScaleInterpDuration", [](BaseCameraWrapper& cls_, float newColorScaleInterpDuration) { return cls_.SetColorScaleInterpDuration(newColorScaleInterpDuration); }, pybind11::arg("newColorScaleInterpDuration"));
	cl_BaseCameraWrapper.def("GetColorScaleInterpStartTime", [](BaseCameraWrapper& cls_) { return cls_.GetColorScaleInterpStartTime(); });
	cl_BaseCameraWrapper.def("SetColorScaleInterpStartTime", [](BaseCameraWrapper& cls_, float newColorScaleInterpStartTime) { return cls_.SetColorScaleInterpStartTime(newColorScaleInterpStartTime); }, pybind11::arg("newColorScaleInterpStartTime"));
	cl_BaseCameraWrapper.def("GetViewTarget", [](BaseCameraWrapper& cls_) { return cls_.GetViewTarget(); });
	cl_BaseCameraWrapper.def("SetViewTarget", [](BaseCameraWrapper& cls_, ViewTarget newViewTarget) { return cls_.SetViewTarget(newViewTarget); }, pybind11::arg("newViewTarget"));
	cl_BaseCameraWrapper.def("GetPendingViewTarget", [](BaseCameraWrapper& cls_) { return cls_.GetPendingViewTarget(); });
	cl_BaseCameraWrapper.def("SetPendingViewTarget", [](BaseCameraWrapper& cls_, ViewTarget newPendingViewTarget) { return cls_.SetPendingViewTarget(newPendingViewTarget); }, pybind11::arg("newPendingViewTarget"));
	cl_BaseCameraWrapper.def("GetBlendTimeToGo", [](BaseCameraWrapper& cls_) { return cls_.GetBlendTimeToGo(); });
	cl_BaseCameraWrapper.def("SetBlendTimeToGo", [](BaseCameraWrapper& cls_, float newBlendTimeToGo) { return cls_.SetBlendTimeToGo(newBlendTimeToGo); }, pybind11::arg("newBlendTimeToGo"));
	cl_BaseCameraWrapper.def("GetFreeCamDistance", [](BaseCameraWrapper& cls_) { return cls_.GetFreeCamDistance(); });
	cl_BaseCameraWrapper.def("SetFreeCamDistance", [](BaseCameraWrapper& cls_, float newFreeCamDistance) { return cls_.SetFreeCamDistance(newFreeCamDistance); }, pybind11::arg("newFreeCamDistance"));
	cl_BaseCameraWrapper.def("GetFreeCamOffset", [](BaseCameraWrapper& cls_) { return cls_.GetFreeCamOffset(); });
	cl_BaseCameraWrapper.def("SetFreeCamOffset", [](BaseCameraWrapper& cls_, Vector newFreeCamOffset) { return cls_.SetFreeCamOffset(newFreeCamOffset); }, pybind11::arg("newFreeCamOffset"));
	cl_BaseCameraWrapper.def("GetFadeTime", [](BaseCameraWrapper& cls_) { return cls_.GetFadeTime(); });
	cl_BaseCameraWrapper.def("SetFadeTime", [](BaseCameraWrapper& cls_, float newFadeTime) { return cls_.SetFadeTime(newFadeTime); }, pybind11::arg("newFadeTime"));
	cl_BaseCameraWrapper.def("GetFadeTimeRemaining", [](BaseCameraWrapper& cls_) { return cls_.GetFadeTimeRemaining(); });
	cl_BaseCameraWrapper.def("SetFadeTimeRemaining", [](BaseCameraWrapper& cls_, float newFadeTimeRemaining) { return cls_.SetFadeTimeRemaining(newFadeTimeRemaining); }, pybind11::arg("newFadeTimeRemaining"));
	cl_BaseCameraWrapper.def("StopAllCameraAnims", [](BaseCameraWrapper& cls_, long unsigned int bImmediate) { return cls_.StopAllCameraAnims(bImmediate); }, pybind11::arg("bImmediate"));
	cl_BaseCameraWrapper.def("ClearAllCameraShakes", [](BaseCameraWrapper& cls_) { return cls_.ClearAllCameraShakes(); });
	cl_BaseCameraWrapper.def("CalcRadialShakeScale", [](BaseCameraWrapper& cls_, BaseCameraWrapper Cam, Vector & Epicenter, float InnerRadius, float OuterRadius, float Falloff) { return cls_.CalcRadialShakeScale(Cam, Epicenter, InnerRadius, OuterRadius, Falloff); }, pybind11::arg("Cam"), pybind11::arg("Epicenter"), pybind11::arg("InnerRadius"), pybind11::arg("OuterRadius"), pybind11::arg("Falloff"));
	cl_BaseCameraWrapper.def("ClearCameraLensEffects", [](BaseCameraWrapper& cls_) { return cls_.ClearCameraLensEffects(); });
	cl_BaseCameraWrapper.def("ApplyAudioFade", [](BaseCameraWrapper& cls_) { return cls_.ApplyAudioFade(); });
	cl_BaseCameraWrapper.def("UpdateFade", [](BaseCameraWrapper& cls_, float DeltaTime) { return cls_.UpdateFade(DeltaTime); }, pybind11::arg("DeltaTime"));
	cl_BaseCameraWrapper.def("DoUpdateCamera", [](BaseCameraWrapper& cls_, float DeltaTime) { return cls_.DoUpdateCamera(DeltaTime); }, pybind11::arg("DeltaTime"));
	cl_BaseCameraWrapper.def("eventUpdateCamera", [](BaseCameraWrapper& cls_, float DeltaTime) { return cls_.eventUpdateCamera(DeltaTime); }, pybind11::arg("DeltaTime"));
	cl_BaseCameraWrapper.def("SetDesiredColorScale2", [](BaseCameraWrapper& cls_, Vector & NewColorScale, float InterpTime) { return cls_.SetDesiredColorScale2(NewColorScale, InterpTime); }, pybind11::arg("NewColorScale"), pybind11::arg("InterpTime"));
	cl_BaseCameraWrapper.def("GetCameraRotation", [](BaseCameraWrapper& cls_) { return cls_.GetCameraRotation(); });
	cl_BaseCameraWrapper.def("SetFOV", [](BaseCameraWrapper& cls_, float NewFOV) { return cls_.SetFOV(NewFOV); }, pybind11::arg("NewFOV"));
	cl_BaseCameraWrapper.def("GetFOVAngle", [](BaseCameraWrapper& cls_) { return cls_.GetFOVAngle(); });
	cl_BaseCameraWrapper.def("eventDestroyed", [](BaseCameraWrapper& cls_) { return cls_.eventDestroyed(); });
	cl_BaseCameraWrapper.def("PostBeginPlay", [](BaseCameraWrapper& cls_) { return cls_.PostBeginPlay(); });
}
