void bind_UnrealStringWrapper(pybind11::module& m)
{

	pybind11::class_<UnrealStringWrapper, std::shared_ptr<UnrealStringWrapper>, ArrayWrapper<wchar_t>> cl_UnrealStringWrapper(m, "UnrealStringWrapper");
	cl_UnrealStringWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_UnrealStringWrapper.def(pybind11::init<UnrealStringWrapper const &>(), pybind11::arg("other"));
	// cl_UnrealStringWrapper.def(pybind11::del<>());
	cl_UnrealStringWrapper.def("ToString", [](UnrealStringWrapper& cls_) { return cls_.ToString(); });
	cl_UnrealStringWrapper.def("ToWideString", [](UnrealStringWrapper& cls_) { return cls_.ToWideString(); });
	cl_UnrealStringWrapper.def("IsNull", [](UnrealStringWrapper& cls_) { return cls_.IsNull(); });
}
