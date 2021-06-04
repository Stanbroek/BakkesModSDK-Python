void bind_ItemsWrapper(pybind11::module& m)
{

	pybind11::class_<ItemsWrapper, std::shared_ptr<ItemsWrapper>, ObjectWrapper> cl_ItemsWrapper(m, "ItemsWrapper");
	cl_ItemsWrapper.def(pybind11::init<uintptr_t, uintptr_t>(), pybind11::arg("gamedata"), pybind11::arg("savedata"));
	cl_ItemsWrapper.def(pybind11::init<ItemsWrapper const &>(), pybind11::arg("other"));
	// cl_ItemsWrapper.def(pybind11::del<>());
	cl_ItemsWrapper.def("IsNull", [](ItemsWrapper& cls_) { return cls_.IsNull(); });
	cl_ItemsWrapper.def("GetAllProducts", [](ItemsWrapper& cls_) { return cls_.GetAllProducts(); });
	cl_ItemsWrapper.def("GetProduct", [](ItemsWrapper& cls_, int productId) { return cls_.GetProduct(productId); }, pybind11::arg("productId"));
	cl_ItemsWrapper.def("GetOnlineProduct", [](ItemsWrapper& cls_, long long unsigned int instanceID) { return cls_.GetOnlineProduct(instanceID); }, pybind11::arg("instanceID"));
	// [deprecated] cl_ItemsWrapper.def("GetUnlockedProducts", [](ItemsWrapper& cls_) { return cls_.GetUnlockedProducts(); });
	cl_ItemsWrapper.def("GetCachedUnlockedProducts", [](ItemsWrapper& cls_) { return cls_.GetCachedUnlockedProducts(); });
	cl_ItemsWrapper.def("GetOwnedProducts", [](ItemsWrapper& cls_) { return cls_.GetOwnedProducts(); });
	cl_ItemsWrapper.def("GetCertifiedStatDB", [](ItemsWrapper& cls_) { return cls_.GetCertifiedStatDB(); });
	cl_ItemsWrapper.def("GetEsportTeamDB", [](ItemsWrapper& cls_) { return cls_.GetEsportTeamDB(); });
	cl_ItemsWrapper.def("GetPaintDB", [](ItemsWrapper& cls_) { return cls_.GetPaintDB(); });
	cl_ItemsWrapper.def("GetSpecialEditionDB", [](ItemsWrapper& cls_) { return cls_.GetSpecialEditionDB(); });
	cl_ItemsWrapper.def("GetCurrentLoadoutName", [](ItemsWrapper& cls_) { return cls_.GetCurrentLoadoutName(); });
	cl_ItemsWrapper.def("GetCurrentLoadout", [](ItemsWrapper& cls_, int teamIndex) { return cls_.GetCurrentLoadout(teamIndex); }, pybind11::arg("teamIndex"));
	cl_ItemsWrapper.def("GetTradeWrapper", [](ItemsWrapper& cls_) { return cls_.GetTradeWrapper(); });
	cl_ItemsWrapper.def("GetProductTradeInWrapper", [](ItemsWrapper& cls_) { return cls_.GetProductTradeInWrapper(); });
}
