void bind_bot_loadout_structs(pybind11::module& m)
{

	pybind11::class_<BotLoadoutData, std::shared_ptr<BotLoadoutData>> cl_BotLoadoutData(m, "BotLoadoutData");
	cl_BotLoadoutData.def_property("products", [](const BotLoadoutData& cls_) { return cls_.products; }, [](BotLoadoutData& cls_, std::map<int, int, std::less<int>, std::allocator<std::pair<const int, int> > > const& prop_) { cls_.products = prop_; });
	cl_BotLoadoutData.def_property("product_attributes", [](const BotLoadoutData& cls_) { return cls_.product_attributes; }, [](BotLoadoutData& cls_, std::map<int, std::vector<BotLoadoutData::Attribute, std::allocator<BotLoadoutData::Attribute> >, std::less<int>, std::allocator<std::pair<const int, std::vector<BotLoadoutData::Attribute, std::allocator<BotLoadoutData::Attribute> > > > > const& prop_) { cls_.product_attributes = prop_; });
	cl_BotLoadoutData.def_property("team", [](const BotLoadoutData& cls_) { return cls_.team; }, [](BotLoadoutData& cls_, unsigned char const& prop_) { cls_.team = prop_; });
	cl_BotLoadoutData.def_property("team_finish_id", [](const BotLoadoutData& cls_) { return cls_.team_finish_id; }, [](BotLoadoutData& cls_, int const& prop_) { cls_.team_finish_id = prop_; });
	cl_BotLoadoutData.def_property("custom_finish_id", [](const BotLoadoutData& cls_) { return cls_.custom_finish_id; }, [](BotLoadoutData& cls_, int const& prop_) { cls_.custom_finish_id = prop_; });
	cl_BotLoadoutData.def_property("team_color_id", [](const BotLoadoutData& cls_) { return cls_.team_color_id; }, [](BotLoadoutData& cls_, unsigned char const& prop_) { cls_.team_color_id = prop_; });
	cl_BotLoadoutData.def_property("custom_color_id", [](const BotLoadoutData& cls_) { return cls_.custom_color_id; }, [](BotLoadoutData& cls_, unsigned char const& prop_) { cls_.custom_color_id = prop_; });
	cl_BotLoadoutData.def(pybind11::init<BotLoadoutData const &>(), pybind11::arg("arg0"));
	// cl_BotLoadoutData.def(pybind11::del<>());
	cl_BotLoadoutData.def(pybind11::init<>());

	pybind11::class_<BotLoadoutData::Attribute, std::shared_ptr<BotLoadoutData::Attribute>> cl_BotLoadoutData_Attribute(cl_BotLoadoutData, "Attribute");
	cl_BotLoadoutData_Attribute.def_property("type", [](const BotLoadoutData::Attribute& cls_) { return cls_.type; }, [](BotLoadoutData::Attribute& cls_, BotLoadoutData::Attribute::Type const& prop_) { cls_.type = prop_; });
	cl_BotLoadoutData_Attribute.def_property("value", [](const BotLoadoutData::Attribute& cls_) { return cls_.value; }, [](BotLoadoutData::Attribute& cls_, int const& prop_) { cls_.value = prop_; });
	cl_BotLoadoutData_Attribute.def(pybind11::init<>());
	cl_BotLoadoutData_Attribute.def(pybind11::init<BotLoadoutData::Attribute const &>(), pybind11::arg("arg0"));
	// cl_BotLoadoutData_Attribute.def(pybind11::del<>());

	pybind11::enum_<BotLoadoutData::Attribute::Type> cl_BotLoadoutData_Attribute_Type(cl_BotLoadoutData_Attribute, "Type");
	cl_BotLoadoutData_Attribute_Type.value("PAINT", BotLoadoutData::Attribute::Type::PAINT);
	cl_BotLoadoutData_Attribute_Type.value("ESPORTWHEEL", BotLoadoutData::Attribute::Type::ESPORTWHEEL);
	cl_BotLoadoutData_Attribute_Type.value("SPECIALEDITION", BotLoadoutData::Attribute::Type::SPECIALEDITION);
	// cl_BotLoadoutData_Attribute_Type.export_values();
}
