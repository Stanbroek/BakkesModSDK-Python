void bind_bakkesmodplugin(pybind11::module& m)
{

	pybind11::class_<BakkesMod::Plugin::BakkesModPlugin, std::shared_ptr<BakkesMod::Plugin::BakkesModPlugin>> cl_BakkesMod_Plugin_BakkesModPlugin(m, "BakkesModPlugin");
	cl_BakkesMod_Plugin_BakkesModPlugin.def_property("cvarManager", [](const BakkesMod::Plugin::BakkesModPlugin& cls_) { return cls_.cvarManager; }, [](BakkesMod::Plugin::BakkesModPlugin& cls_, std::shared_ptr<CVarManagerWrapper> const& prop_) { cls_.cvarManager = prop_; });
	cl_BakkesMod_Plugin_BakkesModPlugin.def_property("gameWrapper", [](const BakkesMod::Plugin::BakkesModPlugin& cls_) { return cls_.gameWrapper; }, [](BakkesMod::Plugin::BakkesModPlugin& cls_, std::shared_ptr<GameWrapper> const& prop_) { cls_.gameWrapper = prop_; });
	cl_BakkesMod_Plugin_BakkesModPlugin.def("onLoad", [](BakkesMod::Plugin::BakkesModPlugin& cls_) { return cls_.onLoad(); });
	cl_BakkesMod_Plugin_BakkesModPlugin.def("onUnload", [](BakkesMod::Plugin::BakkesModPlugin& cls_) { return cls_.onUnload(); });
	cl_BakkesMod_Plugin_BakkesModPlugin.def(pybind11::init<BakkesMod::Plugin::BakkesModPlugin const &>(), pybind11::arg("arg0"));
	// cl_BakkesMod_Plugin_BakkesModPlugin.def(pybind11::del<>());
	cl_BakkesMod_Plugin_BakkesModPlugin.def(pybind11::init<>());

	pybind11::class_<BakkesMod::Plugin::PluginInfo, std::shared_ptr<BakkesMod::Plugin::PluginInfo>> cl_BakkesMod_Plugin_PluginInfo(m, "PluginInfo");
	cl_BakkesMod_Plugin_PluginInfo.def_property("apiBuildVersion", [](const BakkesMod::Plugin::PluginInfo& cls_) { return cls_.apiBuildVersion; }, [](BakkesMod::Plugin::PluginInfo& cls_, short int const& prop_) { cls_.apiBuildVersion = prop_; });
	cl_BakkesMod_Plugin_PluginInfo.def_property("fileName", [](const BakkesMod::Plugin::PluginInfo& cls_) { return cls_.fileName; }, [](BakkesMod::Plugin::PluginInfo& cls_, char const * const& prop_) { cls_.fileName = prop_; });
	cl_BakkesMod_Plugin_PluginInfo.def_property("className", [](const BakkesMod::Plugin::PluginInfo& cls_) { return cls_.className; }, [](BakkesMod::Plugin::PluginInfo& cls_, char const * const& prop_) { cls_.className = prop_; });
	cl_BakkesMod_Plugin_PluginInfo.def_property("pluginName", [](const BakkesMod::Plugin::PluginInfo& cls_) { return cls_.pluginName; }, [](BakkesMod::Plugin::PluginInfo& cls_, char const * const& prop_) { cls_.pluginName = prop_; });
	cl_BakkesMod_Plugin_PluginInfo.def_property("pluginVersion", [](const BakkesMod::Plugin::PluginInfo& cls_) { return cls_.pluginVersion; }, [](BakkesMod::Plugin::PluginInfo& cls_, char const * const& prop_) { cls_.pluginVersion = prop_; });
	cl_BakkesMod_Plugin_PluginInfo.def_property_readonly("pluginType", [](const BakkesMod::Plugin::PluginInfo& cls_) { return cls_.pluginType; });
    //cl_BakkesMod_Plugin_PluginInfo.def_property("initializeFunc", [](const BakkesMod::Plugin::PluginInfo& cls_) { return cls_.initializeFunc; }, [](BakkesMod::Plugin::PluginInfo& cls_, BakkesMod::Plugin::GetPluginFunc const& prop_) { cls_.initializeFunc = prop_; });
	//cl_BakkesMod_Plugin_PluginInfo.def_property("delFunc", [](const BakkesMod::Plugin::PluginInfo& cls_) { return cls_.delFunc; }, [](BakkesMod::Plugin::PluginInfo& cls_, BakkesMod::Plugin::deleteFunc const& prop_) { cls_.delFunc = prop_; });
	cl_BakkesMod_Plugin_PluginInfo.def(pybind11::init<BakkesMod::Plugin::PluginInfo const &>(), pybind11::arg("arg0"));
	// cl_BakkesMod_Plugin_PluginInfo.def(pybind11::del<>());

	pybind11::class_<BakkesMod::Plugin::LoadedPlugin, std::shared_ptr<BakkesMod::Plugin::LoadedPlugin>> cl_BakkesMod_Plugin_LoadedPlugin(m, "LoadedPlugin");
	cl_BakkesMod_Plugin_LoadedPlugin.def_property("_details", [](const BakkesMod::Plugin::LoadedPlugin& cls_) { return cls_._details; }, [](BakkesMod::Plugin::LoadedPlugin& cls_, std::shared_ptr<BakkesMod::Plugin::PluginInfo> const& prop_) { cls_._details = prop_; });
	cl_BakkesMod_Plugin_LoadedPlugin.def_property("_plugin", [](const BakkesMod::Plugin::LoadedPlugin& cls_) { return cls_._plugin; }, [](BakkesMod::Plugin::LoadedPlugin& cls_, std::shared_ptr<BakkesMod::Plugin::BakkesModPlugin> const& prop_) { cls_._plugin = prop_; });
	cl_BakkesMod_Plugin_LoadedPlugin.def_property("_instance", [](const BakkesMod::Plugin::LoadedPlugin& cls_) { return cls_._instance; }, [](BakkesMod::Plugin::LoadedPlugin& cls_, HINSTANCE const& prop_) { cls_._instance = prop_; });
	cl_BakkesMod_Plugin_LoadedPlugin.def_property("_filename", [](const BakkesMod::Plugin::LoadedPlugin& cls_) { return cls_._filename; }, [](BakkesMod::Plugin::LoadedPlugin& cls_, std::string const& prop_) { cls_._filename = prop_; });
	cl_BakkesMod_Plugin_LoadedPlugin.def_property("_typeid", [](const BakkesMod::Plugin::LoadedPlugin& cls_) { return cls_._typeid; }, [](BakkesMod::Plugin::LoadedPlugin& cls_, std::shared_ptr<std::type_index> const& prop_) { cls_._typeid = prop_; });
	cl_BakkesMod_Plugin_LoadedPlugin.def(pybind11::init<std::shared_ptr<BakkesMod::Plugin::PluginInfo>, std::shared_ptr<BakkesMod::Plugin::BakkesModPlugin>, HINSTANCE, std::string>(), pybind11::arg("details"), pybind11::arg("plugin"), pybind11::arg("instance"), pybind11::arg("filename"));
	// cl_BakkesMod_Plugin_LoadedPlugin.def(pybind11::del<>());
	cl_BakkesMod_Plugin_LoadedPlugin.def(pybind11::init<BakkesMod::Plugin::LoadedPlugin const &>(), pybind11::arg("arg0"));
}
