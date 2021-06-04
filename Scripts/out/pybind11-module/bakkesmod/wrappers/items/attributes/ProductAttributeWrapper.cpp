void bind_ProductAttributeWrapper(pybind11::module& m)
{

	pybind11::class_<ProductAttributeWrapper, std::shared_ptr<ProductAttributeWrapper>, ObjectWrapper> cl_ProductAttributeWrapper(m, "ProductAttributeWrapper");
	cl_ProductAttributeWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ProductAttributeWrapper.def(pybind11::init<ProductAttributeWrapper const &>(), pybind11::arg("other"));
	// cl_ProductAttributeWrapper.def(pybind11::del<>());
	cl_ProductAttributeWrapper.def("IsNull", [](ProductAttributeWrapper& cls_) { return cls_.IsNull(); });
	cl_ProductAttributeWrapper.def("GetAttributeType", [](ProductAttributeWrapper& cls_) { return cls_.GetAttributeType(); });
	cl_ProductAttributeWrapper.def("GetTypename", [](ProductAttributeWrapper& cls_) { return cls_.GetTypename(); });
	cl_ProductAttributeWrapper.def("GetLabel", [](ProductAttributeWrapper& cls_) { return cls_.GetLabel(); });
}
