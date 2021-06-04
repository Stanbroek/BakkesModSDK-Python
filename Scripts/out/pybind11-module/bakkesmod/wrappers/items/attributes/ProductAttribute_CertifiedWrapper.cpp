void bind_ProductAttribute_CertifiedWrapper(pybind11::module& m)
{

	pybind11::class_<ProductAttribute_CertifiedWrapper, std::shared_ptr<ProductAttribute_CertifiedWrapper>, ProductAttributeWrapper> cl_ProductAttribute_CertifiedWrapper(m, "ProductAttribute_CertifiedWrapper");
	cl_ProductAttribute_CertifiedWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ProductAttribute_CertifiedWrapper.def(pybind11::init<ProductAttribute_CertifiedWrapper const &>(), pybind11::arg("other"));
	// cl_ProductAttribute_CertifiedWrapper.def(pybind11::del<>());
	cl_ProductAttribute_CertifiedWrapper.def("GetValueKeyName", [](ProductAttribute_CertifiedWrapper& cls_) { return cls_.GetValueKeyName(); });
	cl_ProductAttribute_CertifiedWrapper.def("GetStatId", [](ProductAttribute_CertifiedWrapper& cls_) { return cls_.GetStatId(); });
	cl_ProductAttribute_CertifiedWrapper.def("GetStatValue", [](ProductAttribute_CertifiedWrapper& cls_) { return cls_.GetStatValue(); });
	cl_ProductAttribute_CertifiedWrapper.def("GetSortLabel", [](ProductAttribute_CertifiedWrapper& cls_) { return cls_.GetSortLabel(); });
	cl_ProductAttribute_CertifiedWrapper.def("GetDescription", [](ProductAttribute_CertifiedWrapper& cls_) { return cls_.GetDescription(); });
	cl_ProductAttribute_CertifiedWrapper.def("GetRankLabel", [](ProductAttribute_CertifiedWrapper& cls_) { return cls_.GetRankLabel(); });
	cl_ProductAttribute_CertifiedWrapper.def("GetRank", [](ProductAttribute_CertifiedWrapper& cls_) { return cls_.GetRank(); });
}
