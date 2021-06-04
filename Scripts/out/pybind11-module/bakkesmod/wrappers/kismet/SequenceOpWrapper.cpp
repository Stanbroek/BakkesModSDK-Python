void bind_SequenceOpWrapper(pybind11::module& m)
{

	pybind11::class_<SequenceOpWrapper, std::shared_ptr<SequenceOpWrapper>, SequenceObjectWrapper> cl_SequenceOpWrapper(m, "SequenceOpWrapper");
	cl_SequenceOpWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_SequenceOpWrapper.def(pybind11::init<SequenceOpWrapper const &>(), pybind11::arg("other"));
	// cl_SequenceOpWrapper.def(pybind11::del<>());
}
