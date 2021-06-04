void bind_AIControllerWrapper(pybind11::module& m)
{

	pybind11::class_<AIControllerWrapper, std::shared_ptr<AIControllerWrapper>, ControllerWrapper> cl_AIControllerWrapper(m, "AIControllerWrapper");
	cl_AIControllerWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_AIControllerWrapper.def(pybind11::init<AIControllerWrapper const &>(), pybind11::arg("other"));
	// cl_AIControllerWrapper.def(pybind11::del<>());
	cl_AIControllerWrapper.def("DoNothing", [](AIControllerWrapper& cls_) { return cls_.DoNothing(); });
}
