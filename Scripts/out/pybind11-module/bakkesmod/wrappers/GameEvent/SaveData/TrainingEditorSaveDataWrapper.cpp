void bind_TrainingEditorSaveDataWrapper(pybind11::module& m)
{

	pybind11::class_<TrainingEditorSaveDataWrapper, std::shared_ptr<TrainingEditorSaveDataWrapper>, ObjectWrapper> cl_TrainingEditorSaveDataWrapper(m, "TrainingEditorSaveDataWrapper");
	cl_TrainingEditorSaveDataWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_TrainingEditorSaveDataWrapper.def(pybind11::init<TrainingEditorSaveDataWrapper const &>(), pybind11::arg("other"));
	// cl_TrainingEditorSaveDataWrapper.def(pybind11::del<>());
	cl_TrainingEditorSaveDataWrapper.def("IsNull", [](TrainingEditorSaveDataWrapper& cls_) { return cls_.IsNull(); });
	cl_TrainingEditorSaveDataWrapper.def("GetCode", [](TrainingEditorSaveDataWrapper& cls_) { return cls_.GetCode(); });
	cl_TrainingEditorSaveDataWrapper.def("GetTM_Name", [](TrainingEditorSaveDataWrapper& cls_) { return cls_.GetTM_Name(); });
	cl_TrainingEditorSaveDataWrapper.def("GetType", [](TrainingEditorSaveDataWrapper& cls_) { return cls_.GetType(); });
	cl_TrainingEditorSaveDataWrapper.def("SetType", [](TrainingEditorSaveDataWrapper& cls_, unsigned char newType) { return cls_.SetType(newType); }, pybind11::arg("newType"));
	cl_TrainingEditorSaveDataWrapper.def("GetDifficulty", [](TrainingEditorSaveDataWrapper& cls_) { return cls_.GetDifficulty(); });
	cl_TrainingEditorSaveDataWrapper.def("SetDifficulty", [](TrainingEditorSaveDataWrapper& cls_, unsigned char newDifficulty) { return cls_.SetDifficulty(newDifficulty); }, pybind11::arg("newDifficulty"));
	cl_TrainingEditorSaveDataWrapper.def("GetCreatorName", [](TrainingEditorSaveDataWrapper& cls_) { return cls_.GetCreatorName(); });
	cl_TrainingEditorSaveDataWrapper.def("GetDescription", [](TrainingEditorSaveDataWrapper& cls_) { return cls_.GetDescription(); });
	cl_TrainingEditorSaveDataWrapper.def("GetNumRounds", [](TrainingEditorSaveDataWrapper& cls_) { return cls_.GetNumRounds(); });
	cl_TrainingEditorSaveDataWrapper.def("SetNumRounds", [](TrainingEditorSaveDataWrapper& cls_, int newNumRounds) { return cls_.SetNumRounds(newNumRounds); }, pybind11::arg("newNumRounds"));
	cl_TrainingEditorSaveDataWrapper.def("GetCreatedAt", [](TrainingEditorSaveDataWrapper& cls_) { return cls_.GetCreatedAt(); });
	cl_TrainingEditorSaveDataWrapper.def("SetCreatedAt", [](TrainingEditorSaveDataWrapper& cls_, long long unsigned int newCreatedAt) { return cls_.SetCreatedAt(newCreatedAt); }, pybind11::arg("newCreatedAt"));
	cl_TrainingEditorSaveDataWrapper.def("GetUpdatedAt", [](TrainingEditorSaveDataWrapper& cls_) { return cls_.GetUpdatedAt(); });
	cl_TrainingEditorSaveDataWrapper.def("SetUpdatedAt", [](TrainingEditorSaveDataWrapper& cls_, long long unsigned int newUpdatedAt) { return cls_.SetUpdatedAt(newUpdatedAt); }, pybind11::arg("newUpdatedAt"));
	// [deprecated] cl_TrainingEditorSaveDataWrapper.def("GetCreatorPlayerID", [](TrainingEditorSaveDataWrapper& cls_) { return cls_.GetCreatorPlayerID(); });
	cl_TrainingEditorSaveDataWrapper.def("SetCreatorPlayerID", [](TrainingEditorSaveDataWrapper& cls_, SteamID newCreatorPlayerID) { return cls_.SetCreatorPlayerID(newCreatorPlayerID); }, pybind11::arg("newCreatorPlayerID"));
	cl_TrainingEditorSaveDataWrapper.def("Init", [](TrainingEditorSaveDataWrapper& cls_) { return cls_.Init(); });
	cl_TrainingEditorSaveDataWrapper.def("GetCreatorPlayerUniqueID", [](TrainingEditorSaveDataWrapper& cls_) { return cls_.GetCreatorPlayerUniqueID(); });
}
