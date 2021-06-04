void bind_DataAssetDatabaseWrapper(pybind11::module& m)
{

	pybind11::class_<DataAssetDatabaseWrapper, std::shared_ptr<DataAssetDatabaseWrapper>, ObjectWrapper> cl_DataAssetDatabaseWrapper(m, "DataAssetDatabaseWrapper");
	cl_DataAssetDatabaseWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_DataAssetDatabaseWrapper.def(pybind11::init<DataAssetDatabaseWrapper const &>(), pybind11::arg("other"));
	// cl_DataAssetDatabaseWrapper.def(pybind11::del<>());
	cl_DataAssetDatabaseWrapper.def("IsNull", [](DataAssetDatabaseWrapper& cls_) { return cls_.IsNull(); });
	cl_DataAssetDatabaseWrapper.def("GetName", [](DataAssetDatabaseWrapper& cls_, int DataAssetID) { return cls_.GetName(DataAssetID); }, pybind11::arg("DataAssetID"));
	cl_DataAssetDatabaseWrapper.def("GetID", [](DataAssetDatabaseWrapper& cls_, std::string & DataAssetName) { return cls_.GetID(DataAssetName); }, pybind11::arg("DataAssetName"));
}
