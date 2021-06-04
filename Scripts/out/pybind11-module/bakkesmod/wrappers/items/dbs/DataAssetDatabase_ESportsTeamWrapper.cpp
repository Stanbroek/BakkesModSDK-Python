void bind_DataAssetDatabase_ESportsTeamWrapper(pybind11::module& m)
{

	pybind11::class_<DataAssetDatabase_ESportsTeamWrapper, std::shared_ptr<DataAssetDatabase_ESportsTeamWrapper>, DataAssetDatabaseWrapper> cl_DataAssetDatabase_ESportsTeamWrapper(m, "DataAssetDatabase_ESportsTeamWrapper");
	cl_DataAssetDatabase_ESportsTeamWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_DataAssetDatabase_ESportsTeamWrapper.def(pybind11::init<DataAssetDatabase_ESportsTeamWrapper const &>(), pybind11::arg("other"));
	// cl_DataAssetDatabase_ESportsTeamWrapper.def(pybind11::del<>());
}
