void bind_ProductAttribute_PaintedWrapper(pybind11::module& m)
{

	pybind11::class_<ProductAttribute_PaintedWrapper, std::shared_ptr<ProductAttribute_PaintedWrapper>, ProductAttributeWrapper> cl_ProductAttribute_PaintedWrapper(m, "ProductAttribute_PaintedWrapper");
	cl_ProductAttribute_PaintedWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ProductAttribute_PaintedWrapper.def(pybind11::init<ProductAttribute_PaintedWrapper const &>(), pybind11::arg("other"));
	// cl_ProductAttribute_PaintedWrapper.def(pybind11::del<>());
	cl_ProductAttribute_PaintedWrapper.def("GetPaintID", [](ProductAttribute_PaintedWrapper& cls_) { return cls_.GetPaintID(); });
	cl_ProductAttribute_PaintedWrapper.def("GetSortLabel", [](ProductAttribute_PaintedWrapper& cls_) { return cls_.GetSortLabel(); });
}
