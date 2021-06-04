void bind_AttachmentPickup(pybind11::module& m)
{

	pybind11::class_<AttachmentPickup, std::shared_ptr<AttachmentPickup>, RumblePickupComponentWrapper> cl_AttachmentPickup(m, "AttachmentPickup");
	cl_AttachmentPickup.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_AttachmentPickup.def(pybind11::init<AttachmentPickup const &>(), pybind11::arg("other"));
	// cl_AttachmentPickup.def(pybind11::del<>());
	cl_AttachmentPickup.def("PickupEnd", [](AttachmentPickup& cls_) { return cls_.PickupEnd(); });
	cl_AttachmentPickup.def("PickupStart", [](AttachmentPickup& cls_) { return cls_.PickupStart(); });
}
