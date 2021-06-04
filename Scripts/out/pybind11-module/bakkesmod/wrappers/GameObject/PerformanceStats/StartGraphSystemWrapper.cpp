void bind_StartGraphSystemWrapper(pybind11::module& m)
{

	pybind11::class_<StartGraphSystemWrapper, std::shared_ptr<StartGraphSystemWrapper>, ObjectWrapper> cl_StartGraphSystemWrapper(m, "StartGraphSystemWrapper");
	cl_StartGraphSystemWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_StartGraphSystemWrapper.def(pybind11::init<StartGraphSystemWrapper const &>(), pybind11::arg("other"));
	// cl_StartGraphSystemWrapper.def(pybind11::del<>());
	cl_StartGraphSystemWrapper.def("IsNull", [](StartGraphSystemWrapper& cls_) { return cls_.IsNull(); });
	cl_StartGraphSystemWrapper.def("GetGraphSampleTime", [](StartGraphSystemWrapper& cls_) { return cls_.GetGraphSampleTime(); });
	cl_StartGraphSystemWrapper.def("SetGraphSampleTime", [](StartGraphSystemWrapper& cls_, float newGraphSampleTime) { return cls_.SetGraphSampleTime(newGraphSampleTime); }, pybind11::arg("newGraphSampleTime"));
	cl_StartGraphSystemWrapper.def("GetGraphLevel", [](StartGraphSystemWrapper& cls_) { return cls_.GetGraphLevel(); });
	cl_StartGraphSystemWrapper.def("SetGraphLevel", [](StartGraphSystemWrapper& cls_, unsigned char newGraphLevel) { return cls_.SetGraphLevel(newGraphLevel); }, pybind11::arg("newGraphLevel"));
	cl_StartGraphSystemWrapper.def("GetPerfStatGraph", [](StartGraphSystemWrapper& cls_) { return cls_.GetPerfStatGraph(); });
	cl_StartGraphSystemWrapper.def("SetPerfStatGraph", [](StartGraphSystemWrapper& cls_, PerfStatGraphWrapper newPerfStatGraph) { return cls_.SetPerfStatGraph(newPerfStatGraph); }, pybind11::arg("newPerfStatGraph"));
	cl_StartGraphSystemWrapper.def("GetNetStatGraph", [](StartGraphSystemWrapper& cls_) { return cls_.GetNetStatGraph(); });
	cl_StartGraphSystemWrapper.def("SetNetStatGraph", [](StartGraphSystemWrapper& cls_, NetStatGraphWrapper newNetStatGraph) { return cls_.SetNetStatGraph(newNetStatGraph); }, pybind11::arg("newNetStatGraph"));
	cl_StartGraphSystemWrapper.def("GetInputBufferGraph", [](StartGraphSystemWrapper& cls_) { return cls_.GetInputBufferGraph(); });
	cl_StartGraphSystemWrapper.def("SetInputBufferGraph", [](StartGraphSystemWrapper& cls_, InputBufferGraphWrapper newInputBufferGraph) { return cls_.SetInputBufferGraph(newInputBufferGraph); }, pybind11::arg("newInputBufferGraph"));
	cl_StartGraphSystemWrapper.def("GetStatGraphs", [](StartGraphSystemWrapper& cls_) { return cls_.GetStatGraphs(); });
	cl_StartGraphSystemWrapper.def("GetVisibleStatGraphs", [](StartGraphSystemWrapper& cls_) { return cls_.GetVisibleStatGraphs(); });
	cl_StartGraphSystemWrapper.def("Graphtime", [](StartGraphSystemWrapper& cls_, float Seconds) { return cls_.Graphtime(Seconds); }, pybind11::arg("Seconds"));
	cl_StartGraphSystemWrapper.def("StatGraphNext", [](StartGraphSystemWrapper& cls_) { return cls_.StatGraphNext(); });
	cl_StartGraphSystemWrapper.def("GetGraphSampleTime2", [](StartGraphSystemWrapper& cls_, unsigned char Level) { return cls_.GetGraphSampleTime2(Level); }, pybind11::arg("Level"));
	cl_StartGraphSystemWrapper.def("SetGraphLevel2", [](StartGraphSystemWrapper& cls_, unsigned char Level) { return cls_.SetGraphLevel2(Level); }, pybind11::arg("Level"));
}
