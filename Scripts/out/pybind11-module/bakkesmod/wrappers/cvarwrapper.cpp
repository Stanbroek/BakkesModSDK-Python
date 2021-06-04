void bind_cvarwrapper(pybind11::module& m)
{

	pybind11::class_<CVarWrapper, std::shared_ptr<CVarWrapper>> cl_CVarWrapper(m, "CVarWrapper");
	cl_CVarWrapper.def(pybind11::init<uintptr_t, std::type_index>(), pybind11::arg("mem"), pybind11::arg("pluginIdx"));
	cl_CVarWrapper.def(pybind11::init<CVarWrapper const &>(), pybind11::arg("other"));
	// cl_CVarWrapper.def(pybind11::del<>());
	cl_CVarWrapper.def("getCVarName", [](CVarWrapper& cls_) { return cls_.getCVarName(); });
	cl_CVarWrapper.def("getIntValue", [](CVarWrapper& cls_) { return cls_.getIntValue(); });
	cl_CVarWrapper.def("getFloatValue", [](CVarWrapper& cls_) { return cls_.getFloatValue(); });
	cl_CVarWrapper.def("getBoolValue", [](CVarWrapper& cls_) { return cls_.getBoolValue(); });
	cl_CVarWrapper.def("getColorValue", [](CVarWrapper& cls_) { return cls_.getColorValue(); });
	cl_CVarWrapper.def("getStringValue", [](CVarWrapper& cls_) { return cls_.getStringValue(); });
	cl_CVarWrapper.def("getDescription", [](CVarWrapper& cls_) { return cls_.getDescription(); });
	cl_CVarWrapper.def("GetDefaultValue", [](CVarWrapper& cls_) { return cls_.GetDefaultValue(); });
	cl_CVarWrapper.def("HasMinimum", [](CVarWrapper& cls_) { return cls_.HasMinimum(); });
	cl_CVarWrapper.def("HasMaximum", [](CVarWrapper& cls_) { return cls_.HasMaximum(); });
	cl_CVarWrapper.def("GetMinimum", [](CVarWrapper& cls_) { return cls_.GetMinimum(); });
	cl_CVarWrapper.def("GetMaximum", [](CVarWrapper& cls_) { return cls_.GetMaximum(); });
	cl_CVarWrapper.def("IsHidden", [](CVarWrapper& cls_) { return cls_.IsHidden(); });
	cl_CVarWrapper.def("ShouldSaveToCfg", [](CVarWrapper& cls_) { return cls_.ShouldSaveToCfg(); });
	cl_CVarWrapper.def("ResetToDefault", [](CVarWrapper& cls_) { return cls_.ResetToDefault(); });
	cl_CVarWrapper.def("notify", [](CVarWrapper& cls_) { return cls_.notify(); });
	cl_CVarWrapper.def("setValue", [](CVarWrapper& cls_, std::string value) { return cls_.setValue(value); }, pybind11::arg("value"));
	cl_CVarWrapper.def("setValue", [](CVarWrapper& cls_, int value) { return cls_.setValue(value); }, pybind11::arg("value"));
	cl_CVarWrapper.def("setValue", [](CVarWrapper& cls_, float value) { return cls_.setValue(value); }, pybind11::arg("value"));
	cl_CVarWrapper.def("setValue", [](CVarWrapper& cls_, LinearColor value) { return cls_.setValue(value); }, pybind11::arg("value"));
	cl_CVarWrapper.def("addOnValueChanged", [](CVarWrapper& cls_, std::function<void (std::basic_string<char>, CVarWrapper)> changeFunc) { return cls_.addOnValueChanged(changeFunc); }, pybind11::arg("changeFunc"));
	cl_CVarWrapper.def("removeOnValueChanged", [](CVarWrapper& cls_) { return cls_.removeOnValueChanged(); });
	//cl_CVarWrapper.def("bindTo", [](CVarWrapper& cls_, std::shared_ptr<int> var) { return cls_.bindTo(var); }, pybind11::arg("var"));
	//cl_CVarWrapper.def("bindTo", [](CVarWrapper& cls_, std::shared_ptr<float> var) { return cls_.bindTo(var); }, pybind11::arg("var"));
	//cl_CVarWrapper.def("bindTo", [](CVarWrapper& cls_, std::shared_ptr<std::basic_string<char> > var) { return cls_.bindTo(var); }, pybind11::arg("var"));
	//cl_CVarWrapper.def("bindTo", [](CVarWrapper& cls_, std::shared_ptr<bool> var) { return cls_.bindTo(var); }, pybind11::arg("var"));
	//cl_CVarWrapper.def("bindTo", [](CVarWrapper& cls_, std::shared_ptr<LinearColor> var) { return cls_.bindTo(var); }, pybind11::arg("var"));
	cl_CVarWrapper.def("IsNull", [](CVarWrapper& cls_) { return cls_.IsNull(); });
}
