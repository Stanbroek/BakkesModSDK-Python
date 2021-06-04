void bind_ProductWrapper(pybind11::module& m)
{

	pybind11::class_<ProductWrapper, std::shared_ptr<ProductWrapper>, ProductTemplateWrapper> cl_ProductWrapper(m, "ProductWrapper");
	cl_ProductWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ProductWrapper.def(pybind11::init<ProductWrapper const &>(), pybind11::arg("other"));
	// cl_ProductWrapper.def(pybind11::del<>());
	cl_ProductWrapper.def("IsNull", [](ProductWrapper& cls_) { return cls_.IsNull(); });
	cl_ProductWrapper.def("GetAssetPackageName", [](ProductWrapper& cls_) { return cls_.GetAssetPackageName(); });
	cl_ProductWrapper.def("GetAssetPath", [](ProductWrapper& cls_) { return cls_.GetAssetPath(); });
	cl_ProductWrapper.def("GetLabel", [](ProductWrapper& cls_) { return cls_.GetLabel(); });
	cl_ProductWrapper.def("GetAsciiLabel", [](ProductWrapper& cls_) { return cls_.GetAsciiLabel(); });
	cl_ProductWrapper.def("GetLongLabel", [](ProductWrapper& cls_) { return cls_.GetLongLabel(); });
	cl_ProductWrapper.def("IsPaintable", [](ProductWrapper& cls_) { return cls_.IsPaintable(); });
	cl_ProductWrapper.def("GetDisplayLabelSlot", [](ProductWrapper& cls_) { return cls_.GetDisplayLabelSlot(); });
	cl_ProductWrapper.def("GetQuality", [](ProductWrapper& cls_) { return cls_.GetQuality(); });
	cl_ProductWrapper.def("IsContainerKey", [](ProductWrapper& cls_) { return cls_.IsContainerKey(); });
	cl_ProductWrapper.def("IsCurrency", [](ProductWrapper& cls_) { return cls_.IsCurrency(); });
	cl_ProductWrapper.def("IsBlueprint", [](ProductWrapper& cls_) { return cls_.IsBlueprint(); });
	cl_ProductWrapper.def("IsContainerUnlocked", [](ProductWrapper& cls_) { return cls_.IsContainerUnlocked(); });
	cl_ProductWrapper.def("IsContainer", [](ProductWrapper& cls_) { return cls_.IsContainer(); });
	cl_ProductWrapper.def("IsSchematic", [](ProductWrapper& cls_) { return cls_.IsSchematic(); });
	cl_ProductWrapper.def("IsPlatformExclusive", [](ProductWrapper& cls_) { return cls_.IsPlatformExclusive(); });
	cl_ProductWrapper.def("IsLicensed", [](ProductWrapper& cls_) { return cls_.IsLicensed(); });
	cl_ProductWrapper.def("GetAttributes", [](ProductWrapper& cls_) { return cls_.GetAttributes(); });
	cl_ProductWrapper.def("GetSortLabel", [](ProductWrapper& cls_) { return cls_.GetSortLabel(); });
	cl_ProductWrapper.def("GetThumbnailAssetPath", [](ProductWrapper& cls_) { return cls_.GetThumbnailAssetPath(); });
	cl_ProductWrapper.def("GetThumbnailPackageNameForLoad", [](ProductWrapper& cls_) { return cls_.GetThumbnailPackageNameForLoad(); });
	cl_ProductWrapper.def("GetThumbnailPackageName", [](ProductWrapper& cls_) { return cls_.GetThumbnailPackageName(); });
	cl_ProductWrapper.def("GetThumbnailAssetName", [](ProductWrapper& cls_) { return cls_.GetThumbnailAssetName(); });
	cl_ProductWrapper.def("GetTrademarkLabel", [](ProductWrapper& cls_) { return cls_.GetTrademarkLabel(); });
	cl_ProductWrapper.def("GetID", [](ProductWrapper& cls_) { return cls_.GetID(); });
}
