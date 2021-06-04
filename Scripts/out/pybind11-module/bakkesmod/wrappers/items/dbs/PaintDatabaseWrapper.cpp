void bind_PaintDatabaseWrapper(pybind11::module& m)
{

	pybind11::class_<PaintDatabaseWrapper, std::shared_ptr<PaintDatabaseWrapper>, ObjectWrapper> cl_PaintDatabaseWrapper(m, "PaintDatabaseWrapper");
	cl_PaintDatabaseWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_PaintDatabaseWrapper.def(pybind11::init<PaintDatabaseWrapper const &>(), pybind11::arg("other"));
	// cl_PaintDatabaseWrapper.def(pybind11::del<>());
	cl_PaintDatabaseWrapper.def("IsNull", [](PaintDatabaseWrapper& cls_) { return cls_.IsNull(); });
	cl_PaintDatabaseWrapper.def("GetPaintName", [](PaintDatabaseWrapper& cls_, int PaintID) { return cls_.GetPaintName(PaintID); }, pybind11::arg("PaintID"));
	cl_PaintDatabaseWrapper.def("GetPaintID", [](PaintDatabaseWrapper& cls_, std::string & PaintName) { return cls_.GetPaintID(PaintName); }, pybind11::arg("PaintName"));
}
