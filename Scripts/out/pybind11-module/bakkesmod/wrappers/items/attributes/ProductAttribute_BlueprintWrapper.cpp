void bind_ProductAttribute_BlueprintWrapper(pybind11::module& m)
{

	pybind11::class_<ProductAttribute_BlueprintWrapper, std::shared_ptr<ProductAttribute_BlueprintWrapper>, ProductAttributeWrapper> cl_ProductAttribute_BlueprintWrapper(m, "ProductAttribute_BlueprintWrapper");
	cl_ProductAttribute_BlueprintWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ProductAttribute_BlueprintWrapper.def(pybind11::init<ProductAttribute_BlueprintWrapper const &>(), pybind11::arg("other"));
	// cl_ProductAttribute_BlueprintWrapper.def(pybind11::del<>());
	cl_ProductAttribute_BlueprintWrapper.def("GetProductID", [](ProductAttribute_BlueprintWrapper& cls_) { return cls_.GetProductID(); });
	cl_ProductAttribute_BlueprintWrapper.def("GetCachedBlueprintSeriesID", [](ProductAttribute_BlueprintWrapper& cls_) { return cls_.GetCachedBlueprintSeriesID(); });
	cl_ProductAttribute_BlueprintWrapper.def("GetSortLabel", [](ProductAttribute_BlueprintWrapper& cls_) { return cls_.GetSortLabel(); });
}
