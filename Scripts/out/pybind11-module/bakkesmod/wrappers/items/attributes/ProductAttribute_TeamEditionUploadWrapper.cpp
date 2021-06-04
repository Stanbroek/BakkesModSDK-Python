void bind_ProductAttribute_TeamEditionUploadWrapper(pybind11::module& m)
{

	pybind11::class_<ProductAttribute_TeamEditionUploadWrapper, std::shared_ptr<ProductAttribute_TeamEditionUploadWrapper>, ProductAttributeWrapper> cl_ProductAttribute_TeamEditionUploadWrapper(m, "ProductAttribute_TeamEditionUploadWrapper");
	cl_ProductAttribute_TeamEditionUploadWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ProductAttribute_TeamEditionUploadWrapper.def(pybind11::init<ProductAttribute_TeamEditionUploadWrapper const &>(), pybind11::arg("other"));
	// cl_ProductAttribute_TeamEditionUploadWrapper.def(pybind11::del<>());
	cl_ProductAttribute_TeamEditionUploadWrapper.def("GetSupportedTeamEditions", [](ProductAttribute_TeamEditionUploadWrapper& cls_) { return cls_.GetSupportedTeamEditions(); });
}
