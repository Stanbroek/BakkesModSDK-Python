void bind_ProductAttribute_TeamEditionWrapper(pybind11::module& m)
{

	pybind11::class_<ProductAttribute_TeamEditionWrapper, std::shared_ptr<ProductAttribute_TeamEditionWrapper>, ProductAttributeWrapper> cl_ProductAttribute_TeamEditionWrapper(m, "ProductAttribute_TeamEditionWrapper");
	cl_ProductAttribute_TeamEditionWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ProductAttribute_TeamEditionWrapper.def(pybind11::init<ProductAttribute_TeamEditionWrapper const &>(), pybind11::arg("other"));
	// cl_ProductAttribute_TeamEditionWrapper.def(pybind11::del<>());
	cl_ProductAttribute_TeamEditionWrapper.def("GetId", [](ProductAttribute_TeamEditionWrapper& cls_) { return cls_.GetId(); });
	cl_ProductAttribute_TeamEditionWrapper.def("GetSortLabel", [](ProductAttribute_TeamEditionWrapper& cls_) { return cls_.GetSortLabel(); });
}
