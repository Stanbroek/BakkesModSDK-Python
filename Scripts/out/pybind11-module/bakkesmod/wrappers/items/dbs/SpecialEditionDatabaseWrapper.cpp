void bind_SpecialEditionDatabaseWrapper(pybind11::module& m)
{

	pybind11::class_<SpecialEditionDatabaseWrapper, std::shared_ptr<SpecialEditionDatabaseWrapper>, ObjectWrapper> cl_SpecialEditionDatabaseWrapper(m, "SpecialEditionDatabaseWrapper");
	cl_SpecialEditionDatabaseWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_SpecialEditionDatabaseWrapper.def(pybind11::init<SpecialEditionDatabaseWrapper const &>(), pybind11::arg("other"));
	// cl_SpecialEditionDatabaseWrapper.def(pybind11::del<>());
	cl_SpecialEditionDatabaseWrapper.def("IsNull", [](SpecialEditionDatabaseWrapper& cls_) { return cls_.IsNull(); });
	cl_SpecialEditionDatabaseWrapper.def("GetSpecialEditionName", [](SpecialEditionDatabaseWrapper& cls_, int EditionID) { return cls_.GetSpecialEditionName(EditionID); }, pybind11::arg("EditionID"));
	cl_SpecialEditionDatabaseWrapper.def("GetSpecialEditionId", [](SpecialEditionDatabaseWrapper& cls_, std::string & EditionName) { return cls_.GetSpecialEditionId(EditionName); }, pybind11::arg("EditionName"));
}
