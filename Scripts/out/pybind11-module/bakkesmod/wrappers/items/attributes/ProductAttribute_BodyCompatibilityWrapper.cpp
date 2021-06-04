void bind_ProductAttribute_BodyCompatibilityWrapper(pybind11::module& m)
{

	pybind11::class_<ProductAttribute_BodyCompatibilityWrapper, std::shared_ptr<ProductAttribute_BodyCompatibilityWrapper>, ProductAttributeWrapper> cl_ProductAttribute_BodyCompatibilityWrapper(m, "ProductAttribute_BodyCompatibilityWrapper");
	cl_ProductAttribute_BodyCompatibilityWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ProductAttribute_BodyCompatibilityWrapper.def(pybind11::init<ProductAttribute_BodyCompatibilityWrapper const &>(), pybind11::arg("other"));
	// cl_ProductAttribute_BodyCompatibilityWrapper.def(pybind11::del<>());
	cl_ProductAttribute_BodyCompatibilityWrapper.def("GetCompatibleBodies", [](ProductAttribute_BodyCompatibilityWrapper& cls_) { return cls_.GetCompatibleBodies(); });
}
