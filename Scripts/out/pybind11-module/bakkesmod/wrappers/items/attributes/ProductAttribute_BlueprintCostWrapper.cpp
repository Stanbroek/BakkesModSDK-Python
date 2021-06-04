void bind_ProductAttribute_BlueprintCostWrapper(pybind11::module& m)
{

	pybind11::class_<ProductAttribute_BlueprintCostWrapper, std::shared_ptr<ProductAttribute_BlueprintCostWrapper>, ProductAttributeWrapper> cl_ProductAttribute_BlueprintCostWrapper(m, "ProductAttribute_BlueprintCostWrapper");
	cl_ProductAttribute_BlueprintCostWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ProductAttribute_BlueprintCostWrapper.def(pybind11::init<ProductAttribute_BlueprintCostWrapper const &>(), pybind11::arg("other"));
	// cl_ProductAttribute_BlueprintCostWrapper.def(pybind11::del<>());
	cl_ProductAttribute_BlueprintCostWrapper.def("GetCost", [](ProductAttribute_BlueprintCostWrapper& cls_) { return cls_.GetCost(); });
}
