void bind_CertifiedStatDatabaseWrapper(pybind11::module& m)
{

	pybind11::class_<CertifiedStatDatabaseWrapper, std::shared_ptr<CertifiedStatDatabaseWrapper>, ObjectWrapper> cl_CertifiedStatDatabaseWrapper(m, "CertifiedStatDatabaseWrapper");
	cl_CertifiedStatDatabaseWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_CertifiedStatDatabaseWrapper.def(pybind11::init<CertifiedStatDatabaseWrapper const &>(), pybind11::arg("other"));
	// cl_CertifiedStatDatabaseWrapper.def(pybind11::del<>());
	cl_CertifiedStatDatabaseWrapper.def("IsNull", [](CertifiedStatDatabaseWrapper& cls_) { return cls_.IsNull(); });
	cl_CertifiedStatDatabaseWrapper.def("GetStatName", [](CertifiedStatDatabaseWrapper& cls_, int StatId) { return cls_.GetStatName(StatId); }, pybind11::arg("StatId"));
	cl_CertifiedStatDatabaseWrapper.def("GetStatId", [](CertifiedStatDatabaseWrapper& cls_, std::string & StatName) { return cls_.GetStatId(StatName); }, pybind11::arg("StatName"));
}
