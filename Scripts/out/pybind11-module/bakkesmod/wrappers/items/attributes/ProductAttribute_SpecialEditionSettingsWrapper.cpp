void bind_ProductAttribute_SpecialEditionSettingsWrapper(pybind11::module& m)
{

	pybind11::class_<SpecialEdition, std::shared_ptr<SpecialEdition>> cl_SpecialEdition(m, "SpecialEdition");
	cl_SpecialEdition.def_property("productId", [](const SpecialEdition& cls_) { return cls_.productId; }, [](SpecialEdition& cls_, int const& prop_) { cls_.productId = prop_; });
	cl_SpecialEdition.def_property("editionId", [](const SpecialEdition& cls_) { return cls_.editionId; }, [](SpecialEdition& cls_, int const& prop_) { cls_.editionId = prop_; });
	cl_SpecialEdition.def_property("label", [](const SpecialEdition& cls_) { return cls_.label; }, [](SpecialEdition& cls_, std::string const& prop_) { cls_.label = prop_; });
	cl_SpecialEdition.def(pybind11::init<SpecialEdition const &>(), pybind11::arg("arg0"));
	// cl_SpecialEdition.def(pybind11::del<>());
	cl_SpecialEdition.def(pybind11::init<>());

	pybind11::class_<ProductAttribute_SpecialEditionSettingsWrapper, std::shared_ptr<ProductAttribute_SpecialEditionSettingsWrapper>, ProductAttributeWrapper> cl_ProductAttribute_SpecialEditionSettingsWrapper(m, "ProductAttribute_SpecialEditionSettingsWrapper");
	cl_ProductAttribute_SpecialEditionSettingsWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ProductAttribute_SpecialEditionSettingsWrapper.def(pybind11::init<ProductAttribute_SpecialEditionSettingsWrapper const &>(), pybind11::arg("other"));
	// cl_ProductAttribute_SpecialEditionSettingsWrapper.def(pybind11::del<>());
	cl_ProductAttribute_SpecialEditionSettingsWrapper.def("GetEditions", [](ProductAttribute_SpecialEditionSettingsWrapper& cls_) { return cls_.GetEditions(); });
}
