void bind_ProductAttribute_CurrencyWrapper(pybind11::module& m)
{

	pybind11::class_<ProductAttribute_CurrencyWrapper, std::shared_ptr<ProductAttribute_CurrencyWrapper>, ProductAttributeWrapper> cl_ProductAttribute_CurrencyWrapper(m, "ProductAttribute_CurrencyWrapper");
	cl_ProductAttribute_CurrencyWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ProductAttribute_CurrencyWrapper.def(pybind11::init<ProductAttribute_CurrencyWrapper const &>(), pybind11::arg("other"));
	// cl_ProductAttribute_CurrencyWrapper.def(pybind11::del<>());
	cl_ProductAttribute_CurrencyWrapper.def("GetCurrencyID", [](ProductAttribute_CurrencyWrapper& cls_) { return cls_.GetCurrencyID(); });
	cl_ProductAttribute_CurrencyWrapper.def("GetSortLabel", [](ProductAttribute_CurrencyWrapper& cls_) { return cls_.GetSortLabel(); });
}
