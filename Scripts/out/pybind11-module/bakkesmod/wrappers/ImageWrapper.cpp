void bind_ImageWrapper(pybind11::module& m)
{

	pybind11::class_<ImageWrapper, std::shared_ptr<ImageWrapper>> cl_ImageWrapper(m, "ImageWrapper");
	cl_ImageWrapper.def(pybind11::init<std::string, bool, bool>(), pybind11::arg("path"), pybind11::arg("canvasLoad"), pybind11::arg("ImGuiLoad"));
	cl_ImageWrapper.def(pybind11::init<std::wstring, bool, bool>(), pybind11::arg("path"), pybind11::arg("canvasLoad"), pybind11::arg("ImGuiLoad"));
	// cl_ImageWrapper.def(pybind11::del<>());
	cl_ImageWrapper.def("LoadForCanvas", [](ImageWrapper& cls_) { return cls_.LoadForCanvas(); });
	cl_ImageWrapper.def("IsLoadedForCanvas", [](ImageWrapper& cls_) { return cls_.IsLoadedForCanvas(); });
	cl_ImageWrapper.def("GetCanvasTex", [](ImageWrapper& cls_) { return cls_.GetCanvasTex(); });
	cl_ImageWrapper.def("LoadForImGui", [](ImageWrapper& cls_, std::function<void (bool)> onLoaded) { return cls_.LoadForImGui(onLoaded); }, pybind11::arg("onLoaded"));
	cl_ImageWrapper.def("IsLoadedForImGui", [](ImageWrapper& cls_) { return cls_.IsLoadedForImGui(); });
	cl_ImageWrapper.def("GetImGuiTex", [](ImageWrapper& cls_) { return cls_.GetImGuiTex(); });
	cl_ImageWrapper.def("GetPath", [](ImageWrapper& cls_) { return cls_.GetPath(); });
	cl_ImageWrapper.def("GetPathW", [](ImageWrapper& cls_) { return cls_.GetPathW(); });
	cl_ImageWrapper.def("GetSize", [](ImageWrapper& cls_) { return cls_.GetSize(); });
	cl_ImageWrapper.def("GetSizeF", [](ImageWrapper& cls_) { return cls_.GetSizeF(); });
}
