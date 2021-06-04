void bind_ReplayServerWrapper(pybind11::module& m)
{

	pybind11::class_<ReplayServerWrapper, std::shared_ptr<ReplayServerWrapper>, ServerWrapper> cl_ReplayServerWrapper(m, "ReplayServerWrapper");
	cl_ReplayServerWrapper.def(pybind11::init<uintptr_t, uintptr_t, uintptr_t>(), pybind11::arg("server"), pybind11::arg("gameinfo"), pybind11::arg("replaydirector"));
	cl_ReplayServerWrapper.def(pybind11::init<ReplayServerWrapper const &>(), pybind11::arg("other"));
	// cl_ReplayServerWrapper.def(pybind11::del<>());
	cl_ReplayServerWrapper.def("GetViewTarget", [](ReplayServerWrapper& cls_) { return cls_.GetViewTarget(); });
	cl_ReplayServerWrapper.def("GetReplay", [](ReplayServerWrapper& cls_) { return cls_.GetReplay(); });
	cl_ReplayServerWrapper.def("GetReplayTimeElapsed", [](ReplayServerWrapper& cls_) { return cls_.GetReplayTimeElapsed(); });
	cl_ReplayServerWrapper.def("GetReplayFPS", [](ReplayServerWrapper& cls_) { return cls_.GetReplayFPS(); });
	cl_ReplayServerWrapper.def("GetCurrentReplayFrame", [](ReplayServerWrapper& cls_) { return cls_.GetCurrentReplayFrame(); });
	cl_ReplayServerWrapper.def("AddKeyFrame", [](ReplayServerWrapper& cls_, int frame, std::string name) { return cls_.AddKeyFrame(frame, name); }, pybind11::arg("frame"), pybind11::arg("name"));
	cl_ReplayServerWrapper.def("RemoveKeyFrame", [](ReplayServerWrapper& cls_, int frame) { return cls_.RemoveKeyFrame(frame); }, pybind11::arg("frame"));
	cl_ReplayServerWrapper.def("SkipToFrame", [](ReplayServerWrapper& cls_, int frame) { return cls_.SkipToFrame(frame); }, pybind11::arg("frame"));
	cl_ReplayServerWrapper.def("SkipToTime", [](ReplayServerWrapper& cls_, float time) { return cls_.SkipToTime(time); }, pybind11::arg("time"));
	cl_ReplayServerWrapper.def("StartPlaybackAtFrame", [](ReplayServerWrapper& cls_, int frame) { return cls_.StartPlaybackAtFrame(frame); }, pybind11::arg("frame"));
	cl_ReplayServerWrapper.def("StartPlaybackAtTime", [](ReplayServerWrapper& cls_, float time) { return cls_.StartPlaybackAtTime(time); }, pybind11::arg("time"));
}
