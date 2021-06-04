void bind_http_structs(pybind11::module& m)
{

	pybind11::class_<FormField, std::shared_ptr<FormField>> cl_FormField(m, "FormField");
	cl_FormField.def_property("field_type", [](const FormField& cls_) { return cls_.field_type; }, [](FormField& cls_, FormField::Type const& prop_) { cls_.field_type = prop_; });
	cl_FormField.def_property("data", [](const FormField& cls_) { return cls_.data; }, [](FormField& cls_, std::string const& prop_) { cls_.data = prop_; });
	cl_FormField.def_property("name", [](const FormField& cls_) { return cls_.name; }, [](FormField& cls_, std::string const& prop_) { cls_.name = prop_; });
	cl_FormField.def(pybind11::init<FormField const &>(), pybind11::arg("arg0"));
	// cl_FormField.def(pybind11::del<>());
	cl_FormField.def(pybind11::init<>());

	pybind11::enum_<FormField::Type> cl_FormField_Type(cl_FormField, "Type");
	cl_FormField_Type.value("kString", FormField::Type::kString);
	cl_FormField_Type.value("kFile", FormField::Type::kFile);
	// cl_FormField_Type.export_values();

	pybind11::class_<CurlRequest, std::shared_ptr<CurlRequest>> cl_CurlRequest(m, "CurlRequest");
	cl_CurlRequest.def_property("url", [](const CurlRequest& cls_) { return cls_.url; }, [](CurlRequest& cls_, std::string const& prop_) { cls_.url = prop_; });
	cl_CurlRequest.def_property("verb", [](const CurlRequest& cls_) { return cls_.verb; }, [](CurlRequest& cls_, std::string const& prop_) { cls_.verb = prop_; });
	cl_CurlRequest.def_property("headers", [](const CurlRequest& cls_) { return cls_.headers; }, [](CurlRequest& cls_, std::map<std::basic_string<char>, std::basic_string<char>, std::less<std::basic_string<char> >, std::allocator<std::pair<const std::basic_string<char>, std::basic_string<char> > > > const& prop_) { cls_.headers = prop_; });
	cl_CurlRequest.def_property("body", [](const CurlRequest& cls_) { return cls_.body; }, [](CurlRequest& cls_, std::string const& prop_) { cls_.body = prop_; });
	cl_CurlRequest.def_property("form_data", [](const CurlRequest& cls_) { return cls_.form_data; }, [](CurlRequest& cls_, std::vector<FormField, std::allocator<FormField> > const& prop_) { cls_.form_data = prop_; });
	cl_CurlRequest.def_property("progress_function", [](const CurlRequest& cls_) { return cls_.progress_function; }, [](CurlRequest& cls_, CurlProgressFunction const& prop_) { cls_.progress_function = prop_; });
	cl_CurlRequest.def(pybind11::init<CurlRequest const &>(), pybind11::arg("arg0"));
	// cl_CurlRequest.def(pybind11::del<>());
	cl_CurlRequest.def(pybind11::init<>());
}
