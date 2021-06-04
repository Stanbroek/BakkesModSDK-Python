void bind_canvaswrapper(pybind11::module& m)
{

	pybind11::class_<CanvasWrapper, std::shared_ptr<CanvasWrapper>> cl_CanvasWrapper(m, "CanvasWrapper");
	cl_CanvasWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_CanvasWrapper.def(pybind11::init<CanvasWrapper const &>(), pybind11::arg("other"));
	// cl_CanvasWrapper.def(pybind11::del<>());
	cl_CanvasWrapper.def("SetPosition", [](CanvasWrapper& cls_, Vector2F pos) { return cls_.SetPosition(pos); }, pybind11::arg("pos"));
	cl_CanvasWrapper.def("GetPositionFloat", [](CanvasWrapper& cls_) { return cls_.GetPositionFloat(); });
	cl_CanvasWrapper.def("SetColor", [](CanvasWrapper& cls_, char Red, char Green, char Blue, char Alpha) { return cls_.SetColor(Red, Green, Blue, Alpha); }, pybind11::arg("Red"), pybind11::arg("Green"), pybind11::arg("Blue"), pybind11::arg("Alpha"));
	cl_CanvasWrapper.def("SetColor", [](CanvasWrapper& cls_, LinearColor color) { return cls_.SetColor(color); }, pybind11::arg("color"));
	cl_CanvasWrapper.def("GetColor", [](CanvasWrapper& cls_) { return cls_.GetColor(); });
	cl_CanvasWrapper.def("DrawBox", [](CanvasWrapper& cls_, Vector2F size) { return cls_.DrawBox(size); }, pybind11::arg("size"));
	cl_CanvasWrapper.def("FillBox", [](CanvasWrapper& cls_, Vector2F size) { return cls_.FillBox(size); }, pybind11::arg("size"));
	cl_CanvasWrapper.def("FillTriangle", [](CanvasWrapper& cls_, Vector2F p1, Vector2F p2, Vector2F p3) { return cls_.FillTriangle(p1, p2, p3); }, pybind11::arg("p1"), pybind11::arg("p2"), pybind11::arg("p3"));
	cl_CanvasWrapper.def("FillTriangle", [](CanvasWrapper& cls_, Vector2F p1, Vector2F p2, Vector2F p3, LinearColor color) { return cls_.FillTriangle(p1, p2, p3, color); }, pybind11::arg("p1"), pybind11::arg("p2"), pybind11::arg("p3"), pybind11::arg("color"));
	cl_CanvasWrapper.def("DrawString", [](CanvasWrapper& cls_, std::string text) { return cls_.DrawString(text); }, pybind11::arg("text"));
	cl_CanvasWrapper.def("DrawString", [](CanvasWrapper& cls_, std::string text, float xScale, float yScale) { return cls_.DrawString(text, xScale, yScale); }, pybind11::arg("text"), pybind11::arg("xScale"), pybind11::arg("yScale"));
	cl_CanvasWrapper.def("DrawString", [](CanvasWrapper& cls_, std::string text, float xScale, float yScale, bool dropShadow, bool wrapText=false) { return cls_.DrawString(text, xScale, yScale, dropShadow, wrapText); }, pybind11::arg("text"), pybind11::arg("xScale"), pybind11::arg("yScale"), pybind11::arg("dropShadow"), pybind11::arg("wrapText"));
	cl_CanvasWrapper.def("GetStringSize", [](CanvasWrapper& cls_, std::string text, float xScale=1, float yScale=1) { return cls_.GetStringSize(text, xScale, yScale); }, pybind11::arg("text"), pybind11::arg("xScale"), pybind11::arg("yScale"));
	cl_CanvasWrapper.def("DrawLine", [](CanvasWrapper& cls_, Vector2F start, Vector2F end) { return cls_.DrawLine(start, end); }, pybind11::arg("start"), pybind11::arg("end"));
	cl_CanvasWrapper.def("DrawLine", [](CanvasWrapper& cls_, Vector2F start, Vector2F end, float width) { return cls_.DrawLine(start, end, width); }, pybind11::arg("start"), pybind11::arg("end"), pybind11::arg("width"));
	cl_CanvasWrapper.def("DrawRect", [](CanvasWrapper& cls_, Vector2F start, Vector2F end) { return cls_.DrawRect(start, end); }, pybind11::arg("start"), pybind11::arg("end"));
	cl_CanvasWrapper.def("DrawTexture", [](CanvasWrapper& cls_, ImageWrapper * img, float scale) { return cls_.DrawTexture(img, scale); }, pybind11::arg("img"), pybind11::arg("scale"));
	cl_CanvasWrapper.def("DrawRect", [](CanvasWrapper& cls_, float RectX, float RectY, ImageWrapper * img) { return cls_.DrawRect(RectX, RectY, img); }, pybind11::arg("RectX"), pybind11::arg("RectY"), pybind11::arg("img"));
	cl_CanvasWrapper.def("DrawTile", [](CanvasWrapper& cls_, ImageWrapper * img, float XL, float YL, float U, float V, float UL, float VL, LinearColor Color, unsigned int ClipTile, unsigned char Blend) { return cls_.DrawTile(img, XL, YL, U, V, UL, VL, Color, ClipTile, Blend); }, pybind11::arg("img"), pybind11::arg("XL"), pybind11::arg("YL"), pybind11::arg("U"), pybind11::arg("V"), pybind11::arg("UL"), pybind11::arg("VL"), pybind11::arg("Color"), pybind11::arg("ClipTile"), pybind11::arg("Blend"));
	cl_CanvasWrapper.def("DrawRotatedTile", [](CanvasWrapper& cls_, ImageWrapper * img, Rotator & Rotation, float XL, float YL, float U, float V, float UL, float VL, float AnchorX, float AnchorY) { return cls_.DrawRotatedTile(img, Rotation, XL, YL, U, V, UL, VL, AnchorX, AnchorY); }, pybind11::arg("img"), pybind11::arg("Rotation"), pybind11::arg("XL"), pybind11::arg("YL"), pybind11::arg("U"), pybind11::arg("V"), pybind11::arg("UL"), pybind11::arg("VL"), pybind11::arg("AnchorX"), pybind11::arg("AnchorY"));
	cl_CanvasWrapper.def("SetPosition", [](CanvasWrapper& cls_, Vector2 pos) { return cls_.SetPosition(pos); }, pybind11::arg("pos"));
	cl_CanvasWrapper.def("GetPosition", [](CanvasWrapper& cls_) { return cls_.GetPosition(); });
	cl_CanvasWrapper.def("DrawBox", [](CanvasWrapper& cls_, Vector2 size) { return cls_.DrawBox(size); }, pybind11::arg("size"));
	cl_CanvasWrapper.def("FillBox", [](CanvasWrapper& cls_, Vector2 size) { return cls_.FillBox(size); }, pybind11::arg("size"));
	cl_CanvasWrapper.def("FillTriangle", [](CanvasWrapper& cls_, Vector2 p1, Vector2 p2, Vector2 p3) { return cls_.FillTriangle(p1, p2, p3); }, pybind11::arg("p1"), pybind11::arg("p2"), pybind11::arg("p3"));
	cl_CanvasWrapper.def("FillTriangle", [](CanvasWrapper& cls_, Vector2 p1, Vector2 p2, Vector2 p3, LinearColor color) { return cls_.FillTriangle(p1, p2, p3, color); }, pybind11::arg("p1"), pybind11::arg("p2"), pybind11::arg("p3"), pybind11::arg("color"));
	cl_CanvasWrapper.def("DrawLine", [](CanvasWrapper& cls_, Vector2 start, Vector2 end) { return cls_.DrawLine(start, end); }, pybind11::arg("start"), pybind11::arg("end"));
	cl_CanvasWrapper.def("DrawLine", [](CanvasWrapper& cls_, Vector2 start, Vector2 end, float width) { return cls_.DrawLine(start, end, width); }, pybind11::arg("start"), pybind11::arg("end"), pybind11::arg("width"));
	cl_CanvasWrapper.def("DrawRect", [](CanvasWrapper& cls_, Vector2 start, Vector2 end) { return cls_.DrawRect(start, end); }, pybind11::arg("start"), pybind11::arg("end"));
	cl_CanvasWrapper.def("Project", [](CanvasWrapper& cls_, Vector location) { return cls_.Project(location); }, pybind11::arg("location"));
	cl_CanvasWrapper.def("ProjectF", [](CanvasWrapper& cls_, Vector location) { return cls_.ProjectF(location); }, pybind11::arg("location"));
	cl_CanvasWrapper.def("GetSize", [](CanvasWrapper& cls_) { return cls_.GetSize(); });
}
