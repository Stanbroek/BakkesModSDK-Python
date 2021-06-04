void bind_LoadoutWrapper(pybind11::module& m)
{

	pybind11::class_<LoadoutWrapper, std::shared_ptr<LoadoutWrapper>, ObjectWrapper> cl_LoadoutWrapper(m, "LoadoutWrapper");
	cl_LoadoutWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_LoadoutWrapper.def(pybind11::init<LoadoutWrapper const &>(), pybind11::arg("other"));
	// cl_LoadoutWrapper.def(pybind11::del<>());
	cl_LoadoutWrapper.def("IsNull", [](LoadoutWrapper& cls_) { return cls_.IsNull(); });
	cl_LoadoutWrapper.def("GetLoadout", [](LoadoutWrapper& cls_) { return cls_.GetLoadout(); });
	cl_LoadoutWrapper.def("GetOnlineLoadout", [](LoadoutWrapper& cls_) { return cls_.GetOnlineLoadout(); });
	cl_LoadoutWrapper.def("GetPrimaryPaintColorId", [](LoadoutWrapper& cls_) { return cls_.GetPrimaryPaintColorId(); });
	cl_LoadoutWrapper.def("GetAccentPaintColorId", [](LoadoutWrapper& cls_) { return cls_.GetAccentPaintColorId(); });
	cl_LoadoutWrapper.def("GetPrimaryFinishId", [](LoadoutWrapper& cls_) { return cls_.GetPrimaryFinishId(); });
	cl_LoadoutWrapper.def("GetAccentFinishId", [](LoadoutWrapper& cls_) { return cls_.GetAccentFinishId(); });
}
