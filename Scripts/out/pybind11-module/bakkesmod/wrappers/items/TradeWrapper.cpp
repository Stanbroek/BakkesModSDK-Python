void bind_TradeWrapper(pybind11::module& m)
{

	pybind11::class_<TradeWrapper, std::shared_ptr<TradeWrapper>, ObjectWrapper> cl_TradeWrapper(m, "TradeWrapper");
	cl_TradeWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_TradeWrapper.def(pybind11::init<TradeWrapper const &>(), pybind11::arg("other"));
	// cl_TradeWrapper.def(pybind11::del<>());
	cl_TradeWrapper.def("GetReceivingCurrency", [](TradeWrapper& cls_) { return cls_.GetReceivingCurrency(); });
	cl_TradeWrapper.def("GetSendingCurrency", [](TradeWrapper& cls_) { return cls_.GetSendingCurrency(); });
	cl_TradeWrapper.def("GetReceivingProducts", [](TradeWrapper& cls_) { return cls_.GetReceivingProducts(); });
	cl_TradeWrapper.def("GetSendingProducts", [](TradeWrapper& cls_) { return cls_.GetSendingProducts(); });
	cl_TradeWrapper.def("IsNull", [](TradeWrapper& cls_) { return cls_.IsNull(); });

	pybind11::class_<TradeWrapper::Currency, std::shared_ptr<TradeWrapper::Currency>> cl_TradeWrapper_Currency(cl_TradeWrapper, "Currency");
	cl_TradeWrapper_Currency.def_property("currency_id", [](const TradeWrapper::Currency& cls_) { return cls_.currency_id; }, [](TradeWrapper::Currency& cls_, int const& prop_) { cls_.currency_id = prop_; });
	cl_TradeWrapper_Currency.def_property("quantity", [](const TradeWrapper::Currency& cls_) { return cls_.quantity; }, [](TradeWrapper::Currency& cls_, int const& prop_) { cls_.quantity = prop_; });
	cl_TradeWrapper_Currency.def(pybind11::init<>());
	cl_TradeWrapper_Currency.def(pybind11::init<TradeWrapper::Currency const &>(), pybind11::arg("arg0"));
	// cl_TradeWrapper_Currency.def(pybind11::del<>());
}
