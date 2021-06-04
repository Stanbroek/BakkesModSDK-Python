void bind_ProductTradeInWrapper(pybind11::module& m)
{

	pybind11::class_<ProductTradeInWrapper, std::shared_ptr<ProductTradeInWrapper>, ObjectWrapper> cl_ProductTradeInWrapper(m, "ProductTradeInWrapper");
	cl_ProductTradeInWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ProductTradeInWrapper.def(pybind11::init<ProductTradeInWrapper const &>(), pybind11::arg("other"));
	// cl_ProductTradeInWrapper.def(pybind11::del<>());
	cl_ProductTradeInWrapper.def("GetProducts", [](ProductTradeInWrapper& cls_) { return cls_.GetProducts(); });
	cl_ProductTradeInWrapper.def("IsNull", [](ProductTradeInWrapper& cls_) { return cls_.IsNull(); });
}
