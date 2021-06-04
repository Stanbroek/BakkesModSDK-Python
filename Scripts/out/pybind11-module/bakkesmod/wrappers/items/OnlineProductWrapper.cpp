void bind_OnlineProductWrapper(pybind11::module& m)
{

	pybind11::class_<OnlineProductWrapper, std::shared_ptr<OnlineProductWrapper>, ObjectWrapper> cl_OnlineProductWrapper(m, "OnlineProductWrapper");
	cl_OnlineProductWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_OnlineProductWrapper.def(pybind11::init<OnlineProductWrapper const &>(), pybind11::arg("other"));
	// cl_OnlineProductWrapper.def(pybind11::del<>());
	cl_OnlineProductWrapper.def("IsNull", [](OnlineProductWrapper& cls_) { return cls_.IsNull(); });
	cl_OnlineProductWrapper.def("SeriesIdToSeriesName", [](OnlineProductWrapper& cls_, int seriesID) { return cls_.SeriesIdToSeriesName(seriesID); }, pybind11::arg("seriesID"));
	cl_OnlineProductWrapper.def("GetProductID", [](OnlineProductWrapper& cls_) { return cls_.GetProductID(); });
	cl_OnlineProductWrapper.def("GetSeriesID", [](OnlineProductWrapper& cls_) { return cls_.GetSeriesID(); });
	cl_OnlineProductWrapper.def("GetTradeHold", [](OnlineProductWrapper& cls_) { return cls_.GetTradeHold(); });
	cl_OnlineProductWrapper.def("GetProductSeries", [](OnlineProductWrapper& cls_) { return cls_.GetProductSeries(); });
	cl_OnlineProductWrapper.def("GetQuality", [](OnlineProductWrapper& cls_) { return cls_.GetQuality(); });
	cl_OnlineProductWrapper.def("GetAttributes", [](OnlineProductWrapper& cls_) { return cls_.GetAttributes(); });
	cl_OnlineProductWrapper.def("GetLongLabel", [](OnlineProductWrapper& cls_) { return cls_.GetLongLabel(); });
	cl_OnlineProductWrapper.def("GetBlueprintSeriesID", [](OnlineProductWrapper& cls_) { return cls_.GetBlueprintSeriesID(); });
	cl_OnlineProductWrapper.def("GetBlueprintType", [](OnlineProductWrapper& cls_) { return cls_.GetBlueprintType(); });
	cl_OnlineProductWrapper.def("IsBlueprint", [](OnlineProductWrapper& cls_) { return cls_.IsBlueprint(); });
	cl_OnlineProductWrapper.def("GetProduct", [](OnlineProductWrapper& cls_) { return cls_.GetProduct(); });
	cl_OnlineProductWrapper.def("GetIsUntradable", [](OnlineProductWrapper& cls_) { return cls_.GetIsUntradable(); });
	cl_OnlineProductWrapper.def("GetInstanceID", [](OnlineProductWrapper& cls_) { return cls_.GetInstanceID(); });
}
