void bind_GameEditorSaveDataWrapper(pybind11::module& m)
{

	pybind11::class_<GameEditorSaveDataWrapper, std::shared_ptr<GameEditorSaveDataWrapper>, SaveDataWrapper> cl_GameEditorSaveDataWrapper(m, "GameEditorSaveDataWrapper");
	cl_GameEditorSaveDataWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_GameEditorSaveDataWrapper.def(pybind11::init<GameEditorSaveDataWrapper const &>(), pybind11::arg("other"));
	// cl_GameEditorSaveDataWrapper.def(pybind11::del<>());
	cl_GameEditorSaveDataWrapper.def("GetLoadedSaveName", [](GameEditorSaveDataWrapper& cls_) { return cls_.GetLoadedSaveName(); });
	cl_GameEditorSaveDataWrapper.def("GetTrainingData", [](GameEditorSaveDataWrapper& cls_) { return cls_.GetTrainingData(); });
	cl_GameEditorSaveDataWrapper.def("SetTrainingData", [](GameEditorSaveDataWrapper& cls_, TrainingEditorSaveDataWrapper newTrainingData) { return cls_.SetTrainingData(newTrainingData); }, pybind11::arg("newTrainingData"));
	cl_GameEditorSaveDataWrapper.def("GetPlayerTeamNumber", [](GameEditorSaveDataWrapper& cls_) { return cls_.GetPlayerTeamNumber(); });
	cl_GameEditorSaveDataWrapper.def("SetPlayerTeamNumber", [](GameEditorSaveDataWrapper& cls_, int newPlayerTeamNumber) { return cls_.SetPlayerTeamNumber(newPlayerTeamNumber); }, pybind11::arg("newPlayerTeamNumber"));
	cl_GameEditorSaveDataWrapper.def("GetbUnowned", [](GameEditorSaveDataWrapper& cls_) { return cls_.GetbUnowned(); });
	cl_GameEditorSaveDataWrapper.def("SetbUnowned", [](GameEditorSaveDataWrapper& cls_, long unsigned int newbUnowned) { return cls_.SetbUnowned(newbUnowned); }, pybind11::arg("newbUnowned"));
	cl_GameEditorSaveDataWrapper.def("GetShotsCompleted", [](GameEditorSaveDataWrapper& cls_) { return cls_.GetShotsCompleted(); });
	cl_GameEditorSaveDataWrapper.def("SetShotsCompleted", [](GameEditorSaveDataWrapper& cls_, int newShotsCompleted) { return cls_.SetShotsCompleted(newShotsCompleted); }, pybind11::arg("newShotsCompleted"));
	cl_GameEditorSaveDataWrapper.def("GetFavoritesFolderPath", [](GameEditorSaveDataWrapper& cls_) { return cls_.GetFavoritesFolderPath(); });
	cl_GameEditorSaveDataWrapper.def("GetMyTrainingFolderPath", [](GameEditorSaveDataWrapper& cls_) { return cls_.GetMyTrainingFolderPath(); });
	cl_GameEditorSaveDataWrapper.def("GetDownloadedFolderPath", [](GameEditorSaveDataWrapper& cls_) { return cls_.GetDownloadedFolderPath(); });
	cl_GameEditorSaveDataWrapper.def("GetTrainingSaveType", [](GameEditorSaveDataWrapper& cls_, long unsigned int bOwned, long unsigned int bFavorited) { return cls_.GetTrainingSaveType(bOwned, bFavorited); }, pybind11::arg("bOwned"), pybind11::arg("bFavorited"));
	cl_GameEditorSaveDataWrapper.def("Init", [](GameEditorSaveDataWrapper& cls_) { return cls_.Init(); });
}
