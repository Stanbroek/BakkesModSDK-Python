void bind_ProductSlotWrapper(pybind11::module& m)
{

	pybind11::class_<ProductSlotWrapper, std::shared_ptr<ProductSlotWrapper>, ObjectWrapper> cl_ProductSlotWrapper(m, "ProductSlotWrapper");
	cl_ProductSlotWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ProductSlotWrapper.def(pybind11::init<ProductSlotWrapper const &>(), pybind11::arg("other"));
	// cl_ProductSlotWrapper.def(pybind11::del<>());
	cl_ProductSlotWrapper.def("IsNull", [](ProductSlotWrapper& cls_) { return cls_.IsNull(); });
	cl_ProductSlotWrapper.def("GetLabel", [](ProductSlotWrapper& cls_) { return cls_.GetLabel(); });
	cl_ProductSlotWrapper.def("GetPluralLabel", [](ProductSlotWrapper& cls_) { return cls_.GetPluralLabel(); });
	cl_ProductSlotWrapper.def("GetDescription", [](ProductSlotWrapper& cls_) { return cls_.GetDescription(); });
	cl_ProductSlotWrapper.def("GetOnlineLabel", [](ProductSlotWrapper& cls_) { return cls_.GetOnlineLabel(); });
	cl_ProductSlotWrapper.def("GetSlotIndex", [](ProductSlotWrapper& cls_) { return cls_.GetSlotIndex(); });
}
