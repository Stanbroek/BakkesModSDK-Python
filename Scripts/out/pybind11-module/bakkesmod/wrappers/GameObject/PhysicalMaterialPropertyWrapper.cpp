void bind_PhysicalMaterialPropertyWrapper(pybind11::module& m)
{

	pybind11::class_<PhysicalMaterialPropertyWrapper, std::shared_ptr<PhysicalMaterialPropertyWrapper>, ObjectWrapper> cl_PhysicalMaterialPropertyWrapper(m, "PhysicalMaterialPropertyWrapper");
	cl_PhysicalMaterialPropertyWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_PhysicalMaterialPropertyWrapper.def(pybind11::init<PhysicalMaterialPropertyWrapper const &>(), pybind11::arg("other"));
	// cl_PhysicalMaterialPropertyWrapper.def(pybind11::del<>());
	cl_PhysicalMaterialPropertyWrapper.def("IsNull", [](PhysicalMaterialPropertyWrapper& cls_) { return cls_.IsNull(); });
	cl_PhysicalMaterialPropertyWrapper.def("GetTireFrictionScale", [](PhysicalMaterialPropertyWrapper& cls_) { return cls_.GetTireFrictionScale(); });
	cl_PhysicalMaterialPropertyWrapper.def("SetTireFrictionScale", [](PhysicalMaterialPropertyWrapper& cls_, float newTireFrictionScale) { return cls_.SetTireFrictionScale(newTireFrictionScale); }, pybind11::arg("newTireFrictionScale"));
	cl_PhysicalMaterialPropertyWrapper.def("GetbStickyWheels", [](PhysicalMaterialPropertyWrapper& cls_) { return cls_.GetbStickyWheels(); });
	cl_PhysicalMaterialPropertyWrapper.def("SetbStickyWheels", [](PhysicalMaterialPropertyWrapper& cls_, long unsigned int newbStickyWheels) { return cls_.SetbStickyWheels(newbStickyWheels); }, pybind11::arg("newbStickyWheels"));
	cl_PhysicalMaterialPropertyWrapper.def("GetbConsiderForGround", [](PhysicalMaterialPropertyWrapper& cls_) { return cls_.GetbConsiderForGround(); });
	cl_PhysicalMaterialPropertyWrapper.def("SetbConsiderForGround", [](PhysicalMaterialPropertyWrapper& cls_, long unsigned int newbConsiderForGround) { return cls_.SetbConsiderForGround(newbConsiderForGround); }, pybind11::arg("newbConsiderForGround"));
}
