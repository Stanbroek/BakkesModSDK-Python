void bind_ModalWrapper(pybind11::module& m)
{

	pybind11::class_<ModalWrapper, std::shared_ptr<ModalWrapper>, ObjectWrapper> cl_ModalWrapper(m, "ModalWrapper");
	cl_ModalWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ModalWrapper.def(pybind11::init<ModalWrapper const &>(), pybind11::arg("other"));
	// cl_ModalWrapper.def(pybind11::del<>());
	cl_ModalWrapper.def("ShowModal", [](ModalWrapper& cls_) { return cls_.ShowModal(); });
	cl_ModalWrapper.def("CloseModal", [](ModalWrapper& cls_) { return cls_.CloseModal(); });
	cl_ModalWrapper.def("SetColor", [](ModalWrapper& cls_, float r, float g, float b) { return cls_.SetColor(r, g, b); }, pybind11::arg("r"), pybind11::arg("g"), pybind11::arg("b"));
	cl_ModalWrapper.def("SetIcon", [](ModalWrapper& cls_, std::string const & iconName) { return cls_.SetIcon(iconName); }, pybind11::arg("iconName"));
	cl_ModalWrapper.def("SetBody", [](ModalWrapper& cls_, std::string const & bodyHtml) { return cls_.SetBody(bodyHtml); }, pybind11::arg("bodyHtml"));
	cl_ModalWrapper.def("AddButton", [](ModalWrapper& cls_, std::string const & button_text, bool is_cancel_button, std::function<void ()> click_callback=nullptr) { return cls_.AddButton(button_text, is_cancel_button, click_callback); }, pybind11::arg("button_text"), pybind11::arg("is_cancel_button"), pybind11::arg("click_callback"));
}
