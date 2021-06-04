void bind_StatEventWrapper(pybind11::module& m)
{

	pybind11::class_<StatEventWrapper, std::shared_ptr<StatEventWrapper>, ObjectWrapper> cl_StatEventWrapper(m, "StatEventWrapper");
	cl_StatEventWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_StatEventWrapper.def(pybind11::init<StatEventWrapper const &>(), pybind11::arg("other"));
	// cl_StatEventWrapper.def(pybind11::del<>());
	cl_StatEventWrapper.def("IsNull", [](StatEventWrapper& cls_) { return cls_.IsNull(); });
	cl_StatEventWrapper.def("GetPoints", [](StatEventWrapper& cls_) { return cls_.GetPoints(); });
	cl_StatEventWrapper.def("GetCooldownSeconds", [](StatEventWrapper& cls_) { return cls_.GetCooldownSeconds(); });
	cl_StatEventWrapper.def("GetbAddToScore", [](StatEventWrapper& cls_) { return cls_.GetbAddToScore(); });
	cl_StatEventWrapper.def("GetbIsLeaderboardStat", [](StatEventWrapper& cls_) { return cls_.GetbIsLeaderboardStat(); });
	cl_StatEventWrapper.def("GetbNotifyTicker", [](StatEventWrapper& cls_) { return cls_.GetbNotifyTicker(); });
	cl_StatEventWrapper.def("GetbShowOnHUD", [](StatEventWrapper& cls_) { return cls_.GetbShowOnHUD(); });
	cl_StatEventWrapper.def("GetbPrimaryStat", [](StatEventWrapper& cls_) { return cls_.GetbPrimaryStat(); });
	cl_StatEventWrapper.def("GetbSkipReplication", [](StatEventWrapper& cls_) { return cls_.GetbSkipReplication(); });
	cl_StatEventWrapper.def("GetbCanMute", [](StatEventWrapper& cls_) { return cls_.GetbCanMute(); });
	cl_StatEventWrapper.def("GetbCountMultiplied", [](StatEventWrapper& cls_) { return cls_.GetbCountMultiplied(); });
	cl_StatEventWrapper.def("GetLabel", [](StatEventWrapper& cls_) { return cls_.GetLabel(); });
	cl_StatEventWrapper.def("GetPluralLabel", [](StatEventWrapper& cls_) { return cls_.GetPluralLabel(); });
	cl_StatEventWrapper.def("GetDescription", [](StatEventWrapper& cls_) { return cls_.GetDescription(); });
	cl_StatEventWrapper.def("GetNextCooldownTime", [](StatEventWrapper& cls_) { return cls_.GetNextCooldownTime(); });
	cl_StatEventWrapper.def("GetGroupName", [](StatEventWrapper& cls_) { return cls_.GetGroupName(); });
	cl_StatEventWrapper.def("GetEventName", [](StatEventWrapper& cls_) { return cls_.GetEventName(); });
}
