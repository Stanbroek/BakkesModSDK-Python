void bind_ProductAttribute_SpecialEditionWrapper(pybind11::module& m)
{

	pybind11::class_<ProductAttribute_SpecialEditionWrapper, std::shared_ptr<ProductAttribute_SpecialEditionWrapper>, ProductAttributeWrapper> cl_ProductAttribute_SpecialEditionWrapper(m, "ProductAttribute_SpecialEditionWrapper");
	cl_ProductAttribute_SpecialEditionWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ProductAttribute_SpecialEditionWrapper.def(pybind11::init<ProductAttribute_SpecialEditionWrapper const &>(), pybind11::arg("other"));
	// cl_ProductAttribute_SpecialEditionWrapper.def(pybind11::del<>());
	cl_ProductAttribute_SpecialEditionWrapper.def("GetEditionID", [](ProductAttribute_SpecialEditionWrapper& cls_) { return cls_.GetEditionID(); });
	cl_ProductAttribute_SpecialEditionWrapper.def("GetSortLabel", [](ProductAttribute_SpecialEditionWrapper& cls_) { return cls_.GetSortLabel(); });
	cl_ProductAttribute_SpecialEditionWrapper.def("GetOverrideProductID", [](ProductAttribute_SpecialEditionWrapper& cls_, int ProductID) { return cls_.GetOverrideProductID(ProductID); }, pybind11::arg("ProductID"));
}
