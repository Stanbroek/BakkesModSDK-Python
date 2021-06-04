void bind_NetStatGraphWrapper(pybind11::module& m)
{

	pybind11::class_<NetStatGraphWrapper, std::shared_ptr<NetStatGraphWrapper>, StatGraphWrapper> cl_NetStatGraphWrapper(m, "NetStatGraphWrapper");
	cl_NetStatGraphWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_NetStatGraphWrapper.def(pybind11::init<NetStatGraphWrapper const &>(), pybind11::arg("other"));
	// cl_NetStatGraphWrapper.def(pybind11::del<>());
	cl_NetStatGraphWrapper.def("GetPacketsOut", [](NetStatGraphWrapper& cls_) { return cls_.GetPacketsOut(); });
	cl_NetStatGraphWrapper.def("SetPacketsOut", [](NetStatGraphWrapper& cls_, SampleHistoryWrapper newPacketsOut) { return cls_.SetPacketsOut(newPacketsOut); }, pybind11::arg("newPacketsOut"));
	cl_NetStatGraphWrapper.def("GetPacketsIn", [](NetStatGraphWrapper& cls_) { return cls_.GetPacketsIn(); });
	cl_NetStatGraphWrapper.def("SetPacketsIn", [](NetStatGraphWrapper& cls_, SampleHistoryWrapper newPacketsIn) { return cls_.SetPacketsIn(newPacketsIn); }, pybind11::arg("newPacketsIn"));
	cl_NetStatGraphWrapper.def("GetLostPacketsOut", [](NetStatGraphWrapper& cls_) { return cls_.GetLostPacketsOut(); });
	cl_NetStatGraphWrapper.def("SetLostPacketsOut", [](NetStatGraphWrapper& cls_, SampleHistoryWrapper newLostPacketsOut) { return cls_.SetLostPacketsOut(newLostPacketsOut); }, pybind11::arg("newLostPacketsOut"));
	cl_NetStatGraphWrapper.def("GetLostPacketsIn", [](NetStatGraphWrapper& cls_) { return cls_.GetLostPacketsIn(); });
	cl_NetStatGraphWrapper.def("SetLostPacketsIn", [](NetStatGraphWrapper& cls_, SampleHistoryWrapper newLostPacketsIn) { return cls_.SetLostPacketsIn(newLostPacketsIn); }, pybind11::arg("newLostPacketsIn"));
	cl_NetStatGraphWrapper.def("GetBytesOut", [](NetStatGraphWrapper& cls_) { return cls_.GetBytesOut(); });
	cl_NetStatGraphWrapper.def("SetBytesOut", [](NetStatGraphWrapper& cls_, SampleHistoryWrapper newBytesOut) { return cls_.SetBytesOut(newBytesOut); }, pybind11::arg("newBytesOut"));
	cl_NetStatGraphWrapper.def("GetBytesIn", [](NetStatGraphWrapper& cls_) { return cls_.GetBytesIn(); });
	cl_NetStatGraphWrapper.def("SetBytesIn", [](NetStatGraphWrapper& cls_, SampleHistoryWrapper newBytesIn) { return cls_.SetBytesIn(newBytesIn); }, pybind11::arg("newBytesIn"));
	cl_NetStatGraphWrapper.def("GetLatency", [](NetStatGraphWrapper& cls_) { return cls_.GetLatency(); });
	cl_NetStatGraphWrapper.def("SetLatency", [](NetStatGraphWrapper& cls_, SampleHistoryWrapper newLatency) { return cls_.SetLatency(newLatency); }, pybind11::arg("newLatency"));
	cl_NetStatGraphWrapper.def("GetExpectedOutPacketRate", [](NetStatGraphWrapper& cls_) { return cls_.GetExpectedOutPacketRate(); });
	cl_NetStatGraphWrapper.def("SetExpectedOutPacketRate", [](NetStatGraphWrapper& cls_, float newExpectedOutPacketRate) { return cls_.SetExpectedOutPacketRate(newExpectedOutPacketRate); }, pybind11::arg("newExpectedOutPacketRate"));
	cl_NetStatGraphWrapper.def("GetExpectedInPacketRate", [](NetStatGraphWrapper& cls_) { return cls_.GetExpectedInPacketRate(); });
	cl_NetStatGraphWrapper.def("SetExpectedInPacketRate", [](NetStatGraphWrapper& cls_, float newExpectedInPacketRate) { return cls_.SetExpectedInPacketRate(newExpectedInPacketRate); }, pybind11::arg("newExpectedInPacketRate"));
	cl_NetStatGraphWrapper.def("GetMaxBytesRate", [](NetStatGraphWrapper& cls_) { return cls_.GetMaxBytesRate(); });
	cl_NetStatGraphWrapper.def("SetMaxBytesRate", [](NetStatGraphWrapper& cls_, float newMaxBytesRate) { return cls_.SetMaxBytesRate(newMaxBytesRate); }, pybind11::arg("newMaxBytesRate"));
	cl_NetStatGraphWrapper.def("eventUpdateGraphRanges", [](NetStatGraphWrapper& cls_) { return cls_.eventUpdateGraphRanges(); });
	cl_NetStatGraphWrapper.def("CreateBytesSummary", [](NetStatGraphWrapper& cls_, std::string Title) { return cls_.CreateBytesSummary(Title); }, pybind11::arg("Title"));
	cl_NetStatGraphWrapper.def("CreateLossSummary", [](NetStatGraphWrapper& cls_, std::string Title) { return cls_.CreateLossSummary(Title); }, pybind11::arg("Title"));
	cl_NetStatGraphWrapper.def("CreatePktSummary", [](NetStatGraphWrapper& cls_, std::string Title) { return cls_.CreatePktSummary(Title); }, pybind11::arg("Title"));
	cl_NetStatGraphWrapper.def("eventConstruct", [](NetStatGraphWrapper& cls_) { return cls_.eventConstruct(); });
}
