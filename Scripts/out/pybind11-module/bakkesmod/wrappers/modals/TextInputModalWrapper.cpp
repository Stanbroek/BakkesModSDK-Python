void bind_TextInputModalWrapper(pybind11::module& m)
{

	pybind11::class_<TextInputModalWrapper, std::shared_ptr<TextInputModalWrapper>, ModalWrapper> cl_TextInputModalWrapper(m, "TextInputModalWrapper");
	cl_TextInputModalWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_TextInputModalWrapper.def(pybind11::init<TextInputModalWrapper const &>(), pybind11::arg("other"));
	// cl_TextInputModalWrapper.def(pybind11::del<>());
	cl_TextInputModalWrapper.def("SetTextInput", [](TextInputModalWrapper& cls_, std::string const & defaultText, int32_t max_text_length, bool password, std::function<void (std::basic_string<char>, bool)> input_callback) { return cls_.SetTextInput(defaultText, max_text_length, password, input_callback); }, pybind11::arg("defaultText"), pybind11::arg("max_text_length"), pybind11::arg("password"), pybind11::arg("input_callback"));
}
