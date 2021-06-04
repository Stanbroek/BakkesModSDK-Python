void bind_ProductAttribute_AnimatedSkinLabelWrapper(pybind11::module& m)
{

	pybind11::class_<ProductAttribute_AnimatedSkinLabelWrapper, std::shared_ptr<ProductAttribute_AnimatedSkinLabelWrapper>, ProductAttributeWrapper> cl_ProductAttribute_AnimatedSkinLabelWrapper(m, "ProductAttribute_AnimatedSkinLabelWrapper");
	cl_ProductAttribute_AnimatedSkinLabelWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ProductAttribute_AnimatedSkinLabelWrapper.def(pybind11::init<ProductAttribute_AnimatedSkinLabelWrapper const &>(), pybind11::arg("other"));
	// cl_ProductAttribute_AnimatedSkinLabelWrapper.def(pybind11::del<>());
	cl_ProductAttribute_AnimatedSkinLabelWrapper.def("GetAnimatedLabel", [](ProductAttribute_AnimatedSkinLabelWrapper& cls_) { return cls_.GetAnimatedLabel(); });
}
