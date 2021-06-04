void bind_ProductAttribute_QualityWrapper(pybind11::module& m)
{

	pybind11::class_<ProductAttribute_QualityWrapper, std::shared_ptr<ProductAttribute_QualityWrapper>, ProductAttributeWrapper> cl_ProductAttribute_QualityWrapper(m, "ProductAttribute_QualityWrapper");
	cl_ProductAttribute_QualityWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ProductAttribute_QualityWrapper.def(pybind11::init<ProductAttribute_QualityWrapper const &>(), pybind11::arg("other"));
	// cl_ProductAttribute_QualityWrapper.def(pybind11::del<>());
	cl_ProductAttribute_QualityWrapper.def("GetQuality", [](ProductAttribute_QualityWrapper& cls_) { return cls_.GetQuality(); });
	cl_ProductAttribute_QualityWrapper.def("ProductQualityToString", [](ProductAttribute_QualityWrapper& cls_, unsigned char InQuality) { return cls_.ProductQualityToString(InQuality); }, pybind11::arg("InQuality"));
}
