void bind_CVarManagerWrapper(pybind11::module& m)
{

	pybind11::class_<CVarManagerWrapper, std::shared_ptr<CVarManagerWrapper>> cl_CVarManagerWrapper(m, "CVarManagerWrapper");
	cl_CVarManagerWrapper.def(pybind11::init<uintptr_t, std::type_index>(), pybind11::arg("mem"), pybind11::arg("pluginIdx"));
	cl_CVarManagerWrapper.def(pybind11::init<CVarManagerWrapper const &>(), pybind11::arg("other"));
	// cl_CVarManagerWrapper.def(pybind11::del<>());
	cl_CVarManagerWrapper.def("executeCommand", [](CVarManagerWrapper& cls_, std::string command, bool log=true) { return cls_.executeCommand(command, log); }, pybind11::arg("command"), pybind11::arg("log"));
	//cl_CVarManagerWrapper.def("registerNotifier", [](CVarManagerWrapper& cls_, std::string cvar, commandNotifier notifier, std::string description, unsigned char permissions) { return cls_.registerNotifier(cvar, notifier, description, permissions); }, pybind11::arg("cvar"), pybind11::arg("notifier"), pybind11::arg("description"), pybind11::arg("permissions"));
	//cl_CVarManagerWrapper.def("registerNotifier", [](CVarManagerWrapper& cls_, std::string cvar, std::function<void (std::vector<std::basic_string<char>, std::allocator<std::basic_string<char> > >)> notifier, std::string description, unsigned char permissions) { return cls_.registerNotifier(cvar, notifier, description, permissions); }, pybind11::arg("cvar"), pybind11::arg("notifier"), pybind11::arg("description"), pybind11::arg("permissions"));

	cl_CVarManagerWrapper.def("registerNotifier", 
		[](CVarManagerWrapper& cls_, std::string cvar, std::function<void (std::vector<std::basic_string<char>, std::allocator<std::basic_string<char> > >)> notifier, std::string description, unsigned char permissions) {
			return cls_.registerNotifier(cvar, [=](std::vector<std::basic_string<char>> args) { CATCH_PYTHON_EXCEPTIONS(notifier(args);) }, description, permissions);
		}, pybind11::arg("cvar"), pybind11::arg("notifier"), pybind11::arg("description"), pybind11::arg("permissions"));

	cl_CVarManagerWrapper.def("removeNotifier", [](CVarManagerWrapper& cls_, std::string cvar) { return cls_.removeNotifier(cvar); }, pybind11::arg("cvar"));
	cl_CVarManagerWrapper.def("registerCvar", [](CVarManagerWrapper& cls_, std::string cvar, std::string defaultValue, std::string desc="", bool searchAble=true, bool hasMin=false, float min=0, bool hasMax=false, float max=0, bool saveToCfg=true) { return cls_.registerCvar(cvar, defaultValue, desc, searchAble, hasMin, min, hasMax, max, saveToCfg); }, pybind11::arg("cvar"), pybind11::arg("defaultValue"), pybind11::arg("desc"), pybind11::arg("searchAble"), pybind11::arg("hasMin"), pybind11::arg("min"), pybind11::arg("hasMax"), pybind11::arg("max"), pybind11::arg("saveToCfg"));
	cl_CVarManagerWrapper.def("removeCvar", [](CVarManagerWrapper& cls_, std::string cvar) { return cls_.removeCvar(cvar); }, pybind11::arg("cvar"));
	cl_CVarManagerWrapper.def("log", [](CVarManagerWrapper& cls_, std::string text) { return cls_.log(text); }, pybind11::arg("text"));
	cl_CVarManagerWrapper.def("log", [](CVarManagerWrapper& cls_, std::wstring text) { return cls_.log(text); }, pybind11::arg("text"));
	cl_CVarManagerWrapper.def("getCvar", [](CVarManagerWrapper& cls_, std::string cvar) { return cls_.getCvar(cvar); }, pybind11::arg("cvar"));
	cl_CVarManagerWrapper.def("getBindStringForKey", [](CVarManagerWrapper& cls_, std::string key) { return cls_.getBindStringForKey(key); }, pybind11::arg("key"));
	cl_CVarManagerWrapper.def("setBind", [](CVarManagerWrapper& cls_, std::string key, std::string command) { return cls_.setBind(key, command); }, pybind11::arg("key"), pybind11::arg("command"));
	cl_CVarManagerWrapper.def("removeBind", [](CVarManagerWrapper& cls_, std::string key) { return cls_.removeBind(key); }, pybind11::arg("key"));
	cl_CVarManagerWrapper.def("getAlias", [](CVarManagerWrapper& cls_, std::string alias) { return cls_.getAlias(alias); }, pybind11::arg("alias"));
	cl_CVarManagerWrapper.def("setAlias", [](CVarManagerWrapper& cls_, std::string key, std::string script) { return cls_.setAlias(key, script); }, pybind11::arg("key"), pybind11::arg("script"));
	cl_CVarManagerWrapper.def("backupCfg", [](CVarManagerWrapper& cls_, std::string path) { return cls_.backupCfg(path); }, pybind11::arg("path"));
	cl_CVarManagerWrapper.def("backupBinds", [](CVarManagerWrapper& cls_, std::string path) { return cls_.backupBinds(path); }, pybind11::arg("path"));
	cl_CVarManagerWrapper.def("loadCfg", [](CVarManagerWrapper& cls_, std::string path) { return cls_.loadCfg(path); }, pybind11::arg("path"));
}
