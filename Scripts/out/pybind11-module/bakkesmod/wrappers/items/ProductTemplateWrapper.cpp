void bind_ProductTemplateWrapper(pybind11::module& m)
{

	pybind11::class_<ProductTemplateWrapper, std::shared_ptr<ProductTemplateWrapper>, ObjectWrapper> cl_ProductTemplateWrapper(m, "ProductTemplateWrapper");
	cl_ProductTemplateWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ProductTemplateWrapper.def(pybind11::init<ProductTemplateWrapper const &>(), pybind11::arg("other"));
	// cl_ProductTemplateWrapper.def(pybind11::del<>());
	cl_ProductTemplateWrapper.def("IsNull", [](ProductTemplateWrapper& cls_) { return cls_.IsNull(); });
	cl_ProductTemplateWrapper.def("GetSlot", [](ProductTemplateWrapper& cls_) { return cls_.GetSlot(); });
	cl_ProductTemplateWrapper.def("GetUnlockMethod", [](ProductTemplateWrapper& cls_) { return cls_.GetUnlockMethod(); });
	cl_ProductTemplateWrapper.def("GetQuality", [](ProductTemplateWrapper& cls_) { return cls_.GetQuality(); });
	cl_ProductTemplateWrapper.def("GetRequiredProduct", [](ProductTemplateWrapper& cls_) { return cls_.GetRequiredProduct(); });
	cl_ProductTemplateWrapper.def("GetbLicensed", [](ProductTemplateWrapper& cls_) { return cls_.GetbLicensed(); });
}
