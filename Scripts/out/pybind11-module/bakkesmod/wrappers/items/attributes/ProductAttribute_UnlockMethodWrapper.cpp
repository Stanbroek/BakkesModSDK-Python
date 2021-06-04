void bind_ProductAttribute_UnlockMethodWrapper(pybind11::module& m)
{

	pybind11::class_<ProductAttribute_UnlockMethodWrapper, std::shared_ptr<ProductAttribute_UnlockMethodWrapper>, ProductAttributeWrapper> cl_ProductAttribute_UnlockMethodWrapper(m, "ProductAttribute_UnlockMethodWrapper");
	cl_ProductAttribute_UnlockMethodWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ProductAttribute_UnlockMethodWrapper.def(pybind11::init<ProductAttribute_UnlockMethodWrapper const &>(), pybind11::arg("other"));
	// cl_ProductAttribute_UnlockMethodWrapper.def(pybind11::del<>());
	cl_ProductAttribute_UnlockMethodWrapper.def("GetUnlockMethod", [](ProductAttribute_UnlockMethodWrapper& cls_) { return cls_.GetUnlockMethod(); });
}
