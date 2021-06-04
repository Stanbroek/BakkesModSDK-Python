void bind_StatGraphSystemWrapper(pybind11::module& m)
{

	pybind11::class_<StatGraphSystemWrapper, std::shared_ptr<StatGraphSystemWrapper>, ObjectWrapper> cl_StatGraphSystemWrapper(m, "StatGraphSystemWrapper");
	cl_StatGraphSystemWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_StatGraphSystemWrapper.def(pybind11::init<StatGraphSystemWrapper const &>(), pybind11::arg("other"));
	// cl_StatGraphSystemWrapper.def(pybind11::del<>());
	cl_StatGraphSystemWrapper.def("IsNull", [](StatGraphSystemWrapper& cls_) { return cls_.IsNull(); });
	cl_StatGraphSystemWrapper.def("GetGraphSampleTime", [](StatGraphSystemWrapper& cls_) { return cls_.GetGraphSampleTime(); });
	cl_StatGraphSystemWrapper.def("SetGraphSampleTime", [](StatGraphSystemWrapper& cls_, float newGraphSampleTime) { return cls_.SetGraphSampleTime(newGraphSampleTime); }, pybind11::arg("newGraphSampleTime"));
	cl_StatGraphSystemWrapper.def("GetGraphLevel", [](StatGraphSystemWrapper& cls_) { return cls_.GetGraphLevel(); });
	cl_StatGraphSystemWrapper.def("SetGraphLevel", [](StatGraphSystemWrapper& cls_, unsigned char newGraphLevel) { return cls_.SetGraphLevel(newGraphLevel); }, pybind11::arg("newGraphLevel"));
	cl_StatGraphSystemWrapper.def("GetPerfStatGraph", [](StatGraphSystemWrapper& cls_) { return cls_.GetPerfStatGraph(); });
	cl_StatGraphSystemWrapper.def("SetPerfStatGraph", [](StatGraphSystemWrapper& cls_, PerfStatGraphWrapper newPerfStatGraph) { return cls_.SetPerfStatGraph(newPerfStatGraph); }, pybind11::arg("newPerfStatGraph"));
	cl_StatGraphSystemWrapper.def("GetNetStatGraph", [](StatGraphSystemWrapper& cls_) { return cls_.GetNetStatGraph(); });
	cl_StatGraphSystemWrapper.def("SetNetStatGraph", [](StatGraphSystemWrapper& cls_, NetStatGraphWrapper newNetStatGraph) { return cls_.SetNetStatGraph(newNetStatGraph); }, pybind11::arg("newNetStatGraph"));
	cl_StatGraphSystemWrapper.def("GetInputBufferGraph", [](StatGraphSystemWrapper& cls_) { return cls_.GetInputBufferGraph(); });
	cl_StatGraphSystemWrapper.def("SetInputBufferGraph", [](StatGraphSystemWrapper& cls_, InputBufferGraphWrapper newInputBufferGraph) { return cls_.SetInputBufferGraph(newInputBufferGraph); }, pybind11::arg("newInputBufferGraph"));
	cl_StatGraphSystemWrapper.def("GetStatGraphs", [](StatGraphSystemWrapper& cls_) { return cls_.GetStatGraphs(); });
	cl_StatGraphSystemWrapper.def("GetVisibleStatGraphs", [](StatGraphSystemWrapper& cls_) { return cls_.GetVisibleStatGraphs(); });
	cl_StatGraphSystemWrapper.def("GetPreallocGraphLines", [](StatGraphSystemWrapper& cls_) { return cls_.GetPreallocGraphLines(); });
	cl_StatGraphSystemWrapper.def("SetPreallocGraphLines", [](StatGraphSystemWrapper& cls_, int newPreallocGraphLines) { return cls_.SetPreallocGraphLines(newPreallocGraphLines); }, pybind11::arg("newPreallocGraphLines"));
	cl_StatGraphSystemWrapper.def("__StatGraphSystem_TA__SetGraphLevel", [](StatGraphSystemWrapper& cls_, StatGraphWrapper G) { return cls_.__StatGraphSystem_TA__SetGraphLevel(G); }, pybind11::arg("G"));
	cl_StatGraphSystemWrapper.def("PacketReceived", [](StatGraphSystemWrapper& cls_, float Latency) { return cls_.PacketReceived(Latency); }, pybind11::arg("Latency"));
	cl_StatGraphSystemWrapper.def("Graphtime", [](StatGraphSystemWrapper& cls_, float Seconds) { return cls_.Graphtime(Seconds); }, pybind11::arg("Seconds"));
	cl_StatGraphSystemWrapper.def("StatGraphNext", [](StatGraphSystemWrapper& cls_) { return cls_.StatGraphNext(); });
	cl_StatGraphSystemWrapper.def("GetGraphSampleTime2", [](StatGraphSystemWrapper& cls_, unsigned char Level) { return cls_.GetGraphSampleTime2(Level); }, pybind11::arg("Level"));
	cl_StatGraphSystemWrapper.def("SetGraphLevel2", [](StatGraphSystemWrapper& cls_, unsigned char Level) { return cls_.SetGraphLevel2(Level); }, pybind11::arg("Level"));
}
