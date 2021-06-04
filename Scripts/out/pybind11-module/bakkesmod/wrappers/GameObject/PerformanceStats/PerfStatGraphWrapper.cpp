void bind_PerfStatGraphWrapper(pybind11::module& m)
{

	pybind11::class_<PerfStatGraphWrapper, std::shared_ptr<PerfStatGraphWrapper>, StatGraphWrapper> cl_PerfStatGraphWrapper(m, "PerfStatGraphWrapper");
	cl_PerfStatGraphWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_PerfStatGraphWrapper.def(pybind11::init<PerfStatGraphWrapper const &>(), pybind11::arg("other"));
	// cl_PerfStatGraphWrapper.def(pybind11::del<>());
	cl_PerfStatGraphWrapper.def("GetFPS", [](PerfStatGraphWrapper& cls_) { return cls_.GetFPS(); });
	cl_PerfStatGraphWrapper.def("SetFPS", [](PerfStatGraphWrapper& cls_, SampleHistoryWrapper newFPS) { return cls_.SetFPS(newFPS); }, pybind11::arg("newFPS"));
	cl_PerfStatGraphWrapper.def("GetFrameTime", [](PerfStatGraphWrapper& cls_) { return cls_.GetFrameTime(); });
	cl_PerfStatGraphWrapper.def("SetFrameTime", [](PerfStatGraphWrapper& cls_, SampleHistoryWrapper newFrameTime) { return cls_.SetFrameTime(newFrameTime); }, pybind11::arg("newFrameTime"));
	cl_PerfStatGraphWrapper.def("GetGameThreadTime", [](PerfStatGraphWrapper& cls_) { return cls_.GetGameThreadTime(); });
	cl_PerfStatGraphWrapper.def("SetGameThreadTime", [](PerfStatGraphWrapper& cls_, SampleHistoryWrapper newGameThreadTime) { return cls_.SetGameThreadTime(newGameThreadTime); }, pybind11::arg("newGameThreadTime"));
	cl_PerfStatGraphWrapper.def("GetRenderThreadTime", [](PerfStatGraphWrapper& cls_) { return cls_.GetRenderThreadTime(); });
	cl_PerfStatGraphWrapper.def("SetRenderThreadTime", [](PerfStatGraphWrapper& cls_, SampleHistoryWrapper newRenderThreadTime) { return cls_.SetRenderThreadTime(newRenderThreadTime); }, pybind11::arg("newRenderThreadTime"));
	cl_PerfStatGraphWrapper.def("GetGPUFrameTime", [](PerfStatGraphWrapper& cls_) { return cls_.GetGPUFrameTime(); });
	cl_PerfStatGraphWrapper.def("SetGPUFrameTime", [](PerfStatGraphWrapper& cls_, SampleHistoryWrapper newGPUFrameTime) { return cls_.SetGPUFrameTime(newGPUFrameTime); }, pybind11::arg("newGPUFrameTime"));
	cl_PerfStatGraphWrapper.def("GetFrameTimeHistories", [](PerfStatGraphWrapper& cls_) { return cls_.GetFrameTimeHistories(); });
	cl_PerfStatGraphWrapper.def("GetMaxFPS", [](PerfStatGraphWrapper& cls_) { return cls_.GetMaxFPS(); });
	cl_PerfStatGraphWrapper.def("SetMaxFPS", [](PerfStatGraphWrapper& cls_, float newMaxFPS) { return cls_.SetMaxFPS(newMaxFPS); }, pybind11::arg("newMaxFPS"));
	cl_PerfStatGraphWrapper.def("GetTargetFPS", [](PerfStatGraphWrapper& cls_) { return cls_.GetTargetFPS(); });
	cl_PerfStatGraphWrapper.def("SetTargetFPS", [](PerfStatGraphWrapper& cls_, float newTargetFPS) { return cls_.SetTargetFPS(newTargetFPS); }, pybind11::arg("newTargetFPS"));
	cl_PerfStatGraphWrapper.def("eventUpdateGraphRanges", [](PerfStatGraphWrapper& cls_) { return cls_.eventUpdateGraphRanges(); });
	cl_PerfStatGraphWrapper.def("CreateFrameTimeHistory", [](PerfStatGraphWrapper& cls_, std::string Title) { return cls_.CreateFrameTimeHistory(Title); }, pybind11::arg("Title"));
	cl_PerfStatGraphWrapper.def("CreateFpsHistory", [](PerfStatGraphWrapper& cls_, std::string Title) { return cls_.CreateFpsHistory(Title); }, pybind11::arg("Title"));
	cl_PerfStatGraphWrapper.def("eventConstruct", [](PerfStatGraphWrapper& cls_) { return cls_.eventConstruct(); });
}
