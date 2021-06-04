void bind_SampleHistoryWrapper(pybind11::module& m)
{

	pybind11::class_<SampleHistoryWrapper, std::shared_ptr<SampleHistoryWrapper>, ObjectWrapper> cl_SampleHistoryWrapper(m, "SampleHistoryWrapper");
	cl_SampleHistoryWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_SampleHistoryWrapper.def(pybind11::init<SampleHistoryWrapper const &>(), pybind11::arg("other"));
	// cl_SampleHistoryWrapper.def(pybind11::del<>());
	cl_SampleHistoryWrapper.def("IsNull", [](SampleHistoryWrapper& cls_) { return cls_.IsNull(); });
	cl_SampleHistoryWrapper.def("GetRecordSettings", [](SampleHistoryWrapper& cls_) { return cls_.GetRecordSettings(); });
	cl_SampleHistoryWrapper.def("SetRecordSettings", [](SampleHistoryWrapper& cls_, SampleRecordSettingsWrapper newRecordSettings) { return cls_.SetRecordSettings(newRecordSettings); }, pybind11::arg("newRecordSettings"));
	cl_SampleHistoryWrapper.def("GetTitle", [](SampleHistoryWrapper& cls_) { return cls_.GetTitle(); });
	cl_SampleHistoryWrapper.def("GetYMin", [](SampleHistoryWrapper& cls_) { return cls_.GetYMin(); });
	cl_SampleHistoryWrapper.def("SetYMin", [](SampleHistoryWrapper& cls_, float newYMin) { return cls_.SetYMin(newYMin); }, pybind11::arg("newYMin"));
	cl_SampleHistoryWrapper.def("GetYMax", [](SampleHistoryWrapper& cls_) { return cls_.GetYMax(); });
	cl_SampleHistoryWrapper.def("SetYMax", [](SampleHistoryWrapper& cls_, float newYMax) { return cls_.SetYMax(newYMax); }, pybind11::arg("newYMax"));
	cl_SampleHistoryWrapper.def("GetGoodValue", [](SampleHistoryWrapper& cls_) { return cls_.GetGoodValue(); });
	cl_SampleHistoryWrapper.def("SetGoodValue", [](SampleHistoryWrapper& cls_, float newGoodValue) { return cls_.SetGoodValue(newGoodValue); }, pybind11::arg("newGoodValue"));
	cl_SampleHistoryWrapper.def("GetBadValue", [](SampleHistoryWrapper& cls_) { return cls_.GetBadValue(); });
	cl_SampleHistoryWrapper.def("SetBadValue", [](SampleHistoryWrapper& cls_, float newBadValue) { return cls_.SetBadValue(newBadValue); }, pybind11::arg("newBadValue"));
	cl_SampleHistoryWrapper.def("GetBaseValue", [](SampleHistoryWrapper& cls_) { return cls_.GetBaseValue(); });
	cl_SampleHistoryWrapper.def("SetBaseValue", [](SampleHistoryWrapper& cls_, float newBaseValue) { return cls_.SetBaseValue(newBaseValue); }, pybind11::arg("newBaseValue"));
	cl_SampleHistoryWrapper.def("GetSamples", [](SampleHistoryWrapper& cls_) { return cls_.GetSamples(); });
	cl_SampleHistoryWrapper.def("GetSampleIndex", [](SampleHistoryWrapper& cls_) { return cls_.GetSampleIndex(); });
	cl_SampleHistoryWrapper.def("SetSampleIndex", [](SampleHistoryWrapper& cls_, int newSampleIndex) { return cls_.SetSampleIndex(newSampleIndex); }, pybind11::arg("newSampleIndex"));
	cl_SampleHistoryWrapper.def("GetAccumTime", [](SampleHistoryWrapper& cls_) { return cls_.GetAccumTime(); });
	cl_SampleHistoryWrapper.def("SetAccumTime", [](SampleHistoryWrapper& cls_, float newAccumTime) { return cls_.SetAccumTime(newAccumTime); }, pybind11::arg("newAccumTime"));
	cl_SampleHistoryWrapper.def("GetPendingSample", [](SampleHistoryWrapper& cls_) { return cls_.GetPendingSample(); });
	cl_SampleHistoryWrapper.def("SetPendingSample", [](SampleHistoryWrapper& cls_, RecordedSample newPendingSample) { return cls_.SetPendingSample(newPendingSample); }, pybind11::arg("newPendingSample"));
	cl_SampleHistoryWrapper.def("GetbHasPendingSample", [](SampleHistoryWrapper& cls_) { return cls_.GetbHasPendingSample(); });
	cl_SampleHistoryWrapper.def("SetbHasPendingSample", [](SampleHistoryWrapper& cls_, long unsigned int newbHasPendingSample) { return cls_.SetbHasPendingSample(newbHasPendingSample); }, pybind11::arg("newbHasPendingSample"));
	cl_SampleHistoryWrapper.def("Tick", [](SampleHistoryWrapper& cls_, float DeltaTime) { return cls_.Tick(DeltaTime); }, pybind11::arg("DeltaTime"));
	cl_SampleHistoryWrapper.def("AddSample", [](SampleHistoryWrapper& cls_, float NewValue) { return cls_.AddSample(NewValue); }, pybind11::arg("NewValue"));
	cl_SampleHistoryWrapper.def("GetSummaryValue", [](SampleHistoryWrapper& cls_, unsigned char Type, float MaxSampleAge, long unsigned int bAbsoluteValue) { return cls_.GetSummaryValue(Type, MaxSampleAge, bAbsoluteValue); }, pybind11::arg("Type"), pybind11::arg("MaxSampleAge"), pybind11::arg("bAbsoluteValue"));
	cl_SampleHistoryWrapper.def("SetBaseValue2", [](SampleHistoryWrapper& cls_, float InBaseValue) { return cls_.SetBaseValue2(InBaseValue); }, pybind11::arg("InBaseValue"));
	cl_SampleHistoryWrapper.def("SetGoodBadValues", [](SampleHistoryWrapper& cls_, float InGoodValue, float InBadValue) { return cls_.SetGoodBadValues(InGoodValue, InBadValue); }, pybind11::arg("InGoodValue"), pybind11::arg("InBadValue"));
	cl_SampleHistoryWrapper.def("SetGraphMaxMin", [](SampleHistoryWrapper& cls_, float MaxValue, float MinValue) { return cls_.SetGraphMaxMin(MaxValue, MinValue); }, pybind11::arg("MaxValue"), pybind11::arg("MinValue"));
	cl_SampleHistoryWrapper.def("SetTitle", [](SampleHistoryWrapper& cls_, std::string InTitle) { return cls_.SetTitle(InTitle); }, pybind11::arg("InTitle"));
}
