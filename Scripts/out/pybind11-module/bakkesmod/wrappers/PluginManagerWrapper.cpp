void bind_PluginManagerWrapper(pybind11::module& m)
{

	pybind11::class_<PluginManagerWrapper, std::shared_ptr<PluginManagerWrapper>, ObjectWrapper> cl_PluginManagerWrapper(m, "PluginManagerWrapper");
	cl_PluginManagerWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_PluginManagerWrapper.def(pybind11::init<PluginManagerWrapper const &>(), pybind11::arg("other"));
	// cl_PluginManagerWrapper.def(pybind11::del<>());
	cl_PluginManagerWrapper.def("GetLoadedPlugins", [](PluginManagerWrapper& cls_) { return cls_.GetLoadedPlugins(); });
}
