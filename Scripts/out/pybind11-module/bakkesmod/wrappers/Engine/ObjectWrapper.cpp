void bind_ObjectWrapper(pybind11::module& m)
{

	pybind11::class_<ObjectWrapper, std::shared_ptr<ObjectWrapper>> cl_ObjectWrapper(m, "ObjectWrapper");
	cl_ObjectWrapper.def_property("memory_address", [](const ObjectWrapper& cls_) { return cls_.memory_address; }, [](ObjectWrapper& cls_, uintptr_t const& prop_) { cls_.memory_address = prop_; });
	cl_ObjectWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ObjectWrapper.def(pybind11::init<ObjectWrapper const &>(), pybind11::arg("arg0"));
	// cl_ObjectWrapper.def(pybind11::del<>());
}
