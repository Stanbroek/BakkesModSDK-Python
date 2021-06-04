void bind_VehicleSimWrapper(pybind11::module& m)
{

	pybind11::class_<VehicleSimWrapper, std::shared_ptr<VehicleSimWrapper>, ObjectWrapper> cl_VehicleSimWrapper(m, "VehicleSimWrapper");
	cl_VehicleSimWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_VehicleSimWrapper.def(pybind11::init<VehicleSimWrapper const &>(), pybind11::arg("other"));
	// cl_VehicleSimWrapper.def(pybind11::del<>());
	cl_VehicleSimWrapper.def("IsNull", [](VehicleSimWrapper& cls_) { return cls_.IsNull(); });
	cl_VehicleSimWrapper.def("GetWheels", [](VehicleSimWrapper& cls_) { return cls_.GetWheels(); });
	cl_VehicleSimWrapper.def("GetDriveTorque", [](VehicleSimWrapper& cls_) { return cls_.GetDriveTorque(); });
	cl_VehicleSimWrapper.def("SetDriveTorque", [](VehicleSimWrapper& cls_, float newDriveTorque) { return cls_.SetDriveTorque(newDriveTorque); }, pybind11::arg("newDriveTorque"));
	cl_VehicleSimWrapper.def("GetBrakeTorque", [](VehicleSimWrapper& cls_) { return cls_.GetBrakeTorque(); });
	cl_VehicleSimWrapper.def("SetBrakeTorque", [](VehicleSimWrapper& cls_, float newBrakeTorque) { return cls_.SetBrakeTorque(newBrakeTorque); }, pybind11::arg("newBrakeTorque"));
	cl_VehicleSimWrapper.def("GetStopThreshold", [](VehicleSimWrapper& cls_) { return cls_.GetStopThreshold(); });
	cl_VehicleSimWrapper.def("SetStopThreshold", [](VehicleSimWrapper& cls_, float newStopThreshold) { return cls_.SetStopThreshold(newStopThreshold); }, pybind11::arg("newStopThreshold"));
	cl_VehicleSimWrapper.def("GetIdleBrakeFactor", [](VehicleSimWrapper& cls_) { return cls_.GetIdleBrakeFactor(); });
	cl_VehicleSimWrapper.def("SetIdleBrakeFactor", [](VehicleSimWrapper& cls_, float newIdleBrakeFactor) { return cls_.SetIdleBrakeFactor(newIdleBrakeFactor); }, pybind11::arg("newIdleBrakeFactor"));
	cl_VehicleSimWrapper.def("GetOppositeBrakeFactor", [](VehicleSimWrapper& cls_) { return cls_.GetOppositeBrakeFactor(); });
	cl_VehicleSimWrapper.def("SetOppositeBrakeFactor", [](VehicleSimWrapper& cls_, float newOppositeBrakeFactor) { return cls_.SetOppositeBrakeFactor(newOppositeBrakeFactor); }, pybind11::arg("newOppositeBrakeFactor"));
	cl_VehicleSimWrapper.def("GetbUseAckermannSteering", [](VehicleSimWrapper& cls_) { return cls_.GetbUseAckermannSteering(); });
	cl_VehicleSimWrapper.def("SetbUseAckermannSteering", [](VehicleSimWrapper& cls_, long unsigned int newbUseAckermannSteering) { return cls_.SetbUseAckermannSteering(newbUseAckermannSteering); }, pybind11::arg("newbUseAckermannSteering"));
	cl_VehicleSimWrapper.def("GetbWasAttached", [](VehicleSimWrapper& cls_) { return cls_.GetbWasAttached(); });
	cl_VehicleSimWrapper.def("SetbWasAttached", [](VehicleSimWrapper& cls_, long unsigned int newbWasAttached) { return cls_.SetbWasAttached(newbWasAttached); }, pybind11::arg("newbWasAttached"));
	cl_VehicleSimWrapper.def("GetOutputThrottle", [](VehicleSimWrapper& cls_) { return cls_.GetOutputThrottle(); });
	cl_VehicleSimWrapper.def("SetOutputThrottle", [](VehicleSimWrapper& cls_, float newOutputThrottle) { return cls_.SetOutputThrottle(newOutputThrottle); }, pybind11::arg("newOutputThrottle"));
	cl_VehicleSimWrapper.def("GetOutputSteer", [](VehicleSimWrapper& cls_) { return cls_.GetOutputSteer(); });
	cl_VehicleSimWrapper.def("SetOutputSteer", [](VehicleSimWrapper& cls_, float newOutputSteer) { return cls_.SetOutputSteer(newOutputSteer); }, pybind11::arg("newOutputSteer"));
	cl_VehicleSimWrapper.def("GetOutputBrake", [](VehicleSimWrapper& cls_) { return cls_.GetOutputBrake(); });
	cl_VehicleSimWrapper.def("SetOutputBrake", [](VehicleSimWrapper& cls_, float newOutputBrake) { return cls_.SetOutputBrake(newOutputBrake); }, pybind11::arg("newOutputBrake"));
	cl_VehicleSimWrapper.def("GetOutputHandbrake", [](VehicleSimWrapper& cls_) { return cls_.GetOutputHandbrake(); });
	cl_VehicleSimWrapper.def("SetOutputHandbrake", [](VehicleSimWrapper& cls_, float newOutputHandbrake) { return cls_.SetOutputHandbrake(newOutputHandbrake); }, pybind11::arg("newOutputHandbrake"));
	cl_VehicleSimWrapper.def("GetVehicle", [](VehicleSimWrapper& cls_) { return cls_.GetVehicle(); });
	cl_VehicleSimWrapper.def("SetVehicle", [](VehicleSimWrapper& cls_, VehicleWrapper newVehicle) { return cls_.SetVehicle(newVehicle); }, pybind11::arg("newVehicle"));
	cl_VehicleSimWrapper.def("GetCar", [](VehicleSimWrapper& cls_) { return cls_.GetCar(); });
	cl_VehicleSimWrapper.def("SetCar", [](VehicleSimWrapper& cls_, CarWrapper newCar) { return cls_.SetCar(newCar); }, pybind11::arg("newCar"));
	cl_VehicleSimWrapper.def("GetSteeringSensitivity", [](VehicleSimWrapper& cls_) { return cls_.GetSteeringSensitivity(); });
	cl_VehicleSimWrapper.def("SetSteeringSensitivity", [](VehicleSimWrapper& cls_, float newSteeringSensitivity) { return cls_.SetSteeringSensitivity(newSteeringSensitivity); }, pybind11::arg("newSteeringSensitivity"));
}
