void bind_UniqueIDWrapper(pybind11::module& m)
{

	pybind11::class_<UniqueIDWrapper, std::shared_ptr<UniqueIDWrapper>> cl_UniqueIDWrapper(m, "UniqueIDWrapper");
	cl_UniqueIDWrapper.def(pybind11::init<>());
	cl_UniqueIDWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_UniqueIDWrapper.def(pybind11::init<UniqueIDWrapper const &>(), pybind11::arg("other"));
	// cl_UniqueIDWrapper.def(pybind11::del<>());
	cl_UniqueIDWrapper.def("GetPlatform", [](UniqueIDWrapper& cls_) { return cls_.GetPlatform(); });
	cl_UniqueIDWrapper.def("GetEpicAccountID", [](UniqueIDWrapper& cls_) { return cls_.GetEpicAccountID(); });
	cl_UniqueIDWrapper.def("GetUID", [](UniqueIDWrapper& cls_) { return cls_.GetUID(); });
	cl_UniqueIDWrapper.def("GetSplitscreenID", [](UniqueIDWrapper& cls_) { return cls_.GetSplitscreenID(); });
	cl_UniqueIDWrapper.def("str", [](UniqueIDWrapper& cls_) { return cls_.str(); });
	cl_UniqueIDWrapper.def("GetIdString", [](UniqueIDWrapper& cls_) { return cls_.GetIdString(); });
	cl_UniqueIDWrapper.def_static("FromEpicAccountID", [](std::string epicAccountID, long long unsigned int uid, OnlinePlatform platform, unsigned char splitscreenID=0) { return UniqueIDWrapper::FromEpicAccountID(epicAccountID, uid, platform, splitscreenID); }, pybind11::arg("epicAccountID"), pybind11::arg("uid"), pybind11::arg("platform"), pybind11::arg("splitscreenID"));
	cl_UniqueIDWrapper.def("__lt__", [](UniqueIDWrapper& cls_, UniqueIDWrapper const & rhs) { return cls_ < rhs; }, pybind11::arg("rhs"));
	cl_UniqueIDWrapper.def("__eq__", [](UniqueIDWrapper& cls_, UniqueIDWrapper const & rhs) { return cls_ == rhs; }, pybind11::arg("rhs"));
	cl_UniqueIDWrapper.def("__ne__", [](UniqueIDWrapper& cls_, UniqueIDWrapper const & rhs) { return cls_ != rhs; }, pybind11::arg("rhs"));
}
