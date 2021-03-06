void bind_ReplayWrapper(pybind11::module& m)
{

	pybind11::class_<ReplayWrapper, std::shared_ptr<ReplayWrapper>, ObjectWrapper> cl_ReplayWrapper(m, "ReplayWrapper");
	cl_ReplayWrapper.def(pybind11::init<uintptr_t>(), pybind11::arg("mem"));
	cl_ReplayWrapper.def(pybind11::init<ReplayWrapper const &>(), pybind11::arg("other"));
	// cl_ReplayWrapper.def(pybind11::del<>());
	cl_ReplayWrapper.def("IsNull", [](ReplayWrapper& cls_) { return cls_.IsNull(); });
	cl_ReplayWrapper.def("GetReplayName", [](ReplayWrapper& cls_) { return cls_.GetReplayName(); });
	cl_ReplayWrapper.def("GetEngineVersion", [](ReplayWrapper& cls_) { return cls_.GetEngineVersion(); });
	cl_ReplayWrapper.def("SetEngineVersion", [](ReplayWrapper& cls_, int newEngineVersion) { return cls_.SetEngineVersion(newEngineVersion); }, pybind11::arg("newEngineVersion"));
	cl_ReplayWrapper.def("GetLicenseeVersion", [](ReplayWrapper& cls_) { return cls_.GetLicenseeVersion(); });
	cl_ReplayWrapper.def("SetLicenseeVersion", [](ReplayWrapper& cls_, int newLicenseeVersion) { return cls_.SetLicenseeVersion(newLicenseeVersion); }, pybind11::arg("newLicenseeVersion"));
	cl_ReplayWrapper.def("GetNetVersion", [](ReplayWrapper& cls_) { return cls_.GetNetVersion(); });
	cl_ReplayWrapper.def("SetNetVersion", [](ReplayWrapper& cls_, int newNetVersion) { return cls_.SetNetVersion(newNetVersion); }, pybind11::arg("newNetVersion"));
	cl_ReplayWrapper.def("GetReplayVersion", [](ReplayWrapper& cls_) { return cls_.GetReplayVersion(); });
	cl_ReplayWrapper.def("SetReplayVersion", [](ReplayWrapper& cls_, int newReplayVersion) { return cls_.SetReplayVersion(newReplayVersion); }, pybind11::arg("newReplayVersion"));
	cl_ReplayWrapper.def("GetReplayLastSaveVersion", [](ReplayWrapper& cls_) { return cls_.GetReplayLastSaveVersion(); });
	cl_ReplayWrapper.def("SetReplayLastSaveVersion", [](ReplayWrapper& cls_, int newReplayLastSaveVersion) { return cls_.SetReplayLastSaveVersion(newReplayLastSaveVersion); }, pybind11::arg("newReplayLastSaveVersion"));
	cl_ReplayWrapper.def("GetGameVersion", [](ReplayWrapper& cls_) { return cls_.GetGameVersion(); });
	cl_ReplayWrapper.def("SetGameVersion", [](ReplayWrapper& cls_, int newGameVersion) { return cls_.SetGameVersion(newGameVersion); }, pybind11::arg("newGameVersion"));
	cl_ReplayWrapper.def("GetBuildID", [](ReplayWrapper& cls_) { return cls_.GetBuildID(); });
	cl_ReplayWrapper.def("SetBuildID", [](ReplayWrapper& cls_, int newBuildID) { return cls_.SetBuildID(newBuildID); }, pybind11::arg("newBuildID"));
	cl_ReplayWrapper.def("GetChangelist", [](ReplayWrapper& cls_) { return cls_.GetChangelist(); });
	cl_ReplayWrapper.def("SetChangelist", [](ReplayWrapper& cls_, int newChangelist) { return cls_.SetChangelist(newChangelist); }, pybind11::arg("newChangelist"));
	cl_ReplayWrapper.def("GetBuildVersion", [](ReplayWrapper& cls_) { return cls_.GetBuildVersion(); });
	cl_ReplayWrapper.def("GetReserveMegabytes", [](ReplayWrapper& cls_) { return cls_.GetReserveMegabytes(); });
	cl_ReplayWrapper.def("SetReserveMegabytes", [](ReplayWrapper& cls_, int newReserveMegabytes) { return cls_.SetReserveMegabytes(newReserveMegabytes); }, pybind11::arg("newReserveMegabytes"));
	cl_ReplayWrapper.def("GetRecordFPS", [](ReplayWrapper& cls_) { return cls_.GetRecordFPS(); });
	cl_ReplayWrapper.def("SetRecordFPS", [](ReplayWrapper& cls_, float newRecordFPS) { return cls_.SetRecordFPS(newRecordFPS); }, pybind11::arg("newRecordFPS"));
	cl_ReplayWrapper.def("GetKeyframeDelay", [](ReplayWrapper& cls_) { return cls_.GetKeyframeDelay(); });
	cl_ReplayWrapper.def("SetKeyframeDelay", [](ReplayWrapper& cls_, float newKeyframeDelay) { return cls_.SetKeyframeDelay(newKeyframeDelay); }, pybind11::arg("newKeyframeDelay"));
	cl_ReplayWrapper.def("GetMaxChannels", [](ReplayWrapper& cls_) { return cls_.GetMaxChannels(); });
	cl_ReplayWrapper.def("SetMaxChannels", [](ReplayWrapper& cls_, int newMaxChannels) { return cls_.SetMaxChannels(newMaxChannels); }, pybind11::arg("newMaxChannels"));
	cl_ReplayWrapper.def("GetMaxReplaySizeMB", [](ReplayWrapper& cls_) { return cls_.GetMaxReplaySizeMB(); });
	cl_ReplayWrapper.def("SetMaxReplaySizeMB", [](ReplayWrapper& cls_, int newMaxReplaySizeMB) { return cls_.SetMaxReplaySizeMB(newMaxReplaySizeMB); }, pybind11::arg("newMaxReplaySizeMB"));
	cl_ReplayWrapper.def("GetFilename", [](ReplayWrapper& cls_) { return cls_.GetFilename(); });
	cl_ReplayWrapper.def("GetId", [](ReplayWrapper& cls_) { return cls_.GetId(); });
	cl_ReplayWrapper.def("GetDate", [](ReplayWrapper& cls_) { return cls_.GetDate(); });
	cl_ReplayWrapper.def("GetNumFrames", [](ReplayWrapper& cls_) { return cls_.GetNumFrames(); });
	cl_ReplayWrapper.def("SetNumFrames", [](ReplayWrapper& cls_, int newNumFrames) { return cls_.SetNumFrames(newNumFrames); }, pybind11::arg("newNumFrames"));
	cl_ReplayWrapper.def("GetPlayerName", [](ReplayWrapper& cls_) { return cls_.GetPlayerName(); });
	cl_ReplayWrapper.def("GetbFileCorrupted", [](ReplayWrapper& cls_) { return cls_.GetbFileCorrupted(); });
	cl_ReplayWrapper.def("SetbFileCorrupted", [](ReplayWrapper& cls_, long unsigned int newbFileCorrupted) { return cls_.SetbFileCorrupted(newbFileCorrupted); }, pybind11::arg("newbFileCorrupted"));
	cl_ReplayWrapper.def("GetbForceKeyframe", [](ReplayWrapper& cls_) { return cls_.GetbForceKeyframe(); });
	cl_ReplayWrapper.def("SetbForceKeyframe", [](ReplayWrapper& cls_, long unsigned int newbForceKeyframe) { return cls_.SetbForceKeyframe(newbForceKeyframe); }, pybind11::arg("newbForceKeyframe"));
	cl_ReplayWrapper.def("GetbLoadedNetPackages", [](ReplayWrapper& cls_) { return cls_.GetbLoadedNetPackages(); });
	cl_ReplayWrapper.def("SetbLoadedNetPackages", [](ReplayWrapper& cls_, long unsigned int newbLoadedNetPackages) { return cls_.SetbLoadedNetPackages(newbLoadedNetPackages); }, pybind11::arg("newbLoadedNetPackages"));
	cl_ReplayWrapper.def("GetbDebug", [](ReplayWrapper& cls_) { return cls_.GetbDebug(); });
	cl_ReplayWrapper.def("SetbDebug", [](ReplayWrapper& cls_, long unsigned int newbDebug) { return cls_.SetbDebug(newbDebug); }, pybind11::arg("newbDebug"));
	cl_ReplayWrapper.def("GetReplayState", [](ReplayWrapper& cls_) { return cls_.GetReplayState(); });
	cl_ReplayWrapper.def("SetReplayState", [](ReplayWrapper& cls_, unsigned char newReplayState) { return cls_.SetReplayState(newReplayState); }, pybind11::arg("newReplayState"));
	cl_ReplayWrapper.def("GetCurrentFrame", [](ReplayWrapper& cls_) { return cls_.GetCurrentFrame(); });
	cl_ReplayWrapper.def("SetCurrentFrame", [](ReplayWrapper& cls_, int newCurrentFrame) { return cls_.SetCurrentFrame(newCurrentFrame); }, pybind11::arg("newCurrentFrame"));
	cl_ReplayWrapper.def("GetNextKeyframe", [](ReplayWrapper& cls_) { return cls_.GetNextKeyframe(); });
	cl_ReplayWrapper.def("SetNextKeyframe", [](ReplayWrapper& cls_, int newNextKeyframe) { return cls_.SetNextKeyframe(newNextKeyframe); }, pybind11::arg("newNextKeyframe"));
	cl_ReplayWrapper.def("GetCurrentTime", [](ReplayWrapper& cls_) { return cls_.GetCurrentTime(); });
	cl_ReplayWrapper.def("SetCurrentTime", [](ReplayWrapper& cls_, float newCurrentTime) { return cls_.SetCurrentTime(newCurrentTime); }, pybind11::arg("newCurrentTime"));
	cl_ReplayWrapper.def("GetAccumulatedDeltaTime", [](ReplayWrapper& cls_) { return cls_.GetAccumulatedDeltaTime(); });
	cl_ReplayWrapper.def("SetAccumulatedDeltaTime", [](ReplayWrapper& cls_, float newAccumulatedDeltaTime) { return cls_.SetAccumulatedDeltaTime(newAccumulatedDeltaTime); }, pybind11::arg("newAccumulatedDeltaTime"));
	cl_ReplayWrapper.def("GetTimeToSkipTo", [](ReplayWrapper& cls_) { return cls_.GetTimeToSkipTo(); });
	cl_ReplayWrapper.def("SetTimeToSkipTo", [](ReplayWrapper& cls_, float newTimeToSkipTo) { return cls_.SetTimeToSkipTo(newTimeToSkipTo); }, pybind11::arg("newTimeToSkipTo"));
	cl_ReplayWrapper.def("GetFrameToSkipTo", [](ReplayWrapper& cls_) { return cls_.GetFrameToSkipTo(); });
	cl_ReplayWrapper.def("SetFrameToSkipTo", [](ReplayWrapper& cls_, int newFrameToSkipTo) { return cls_.SetFrameToSkipTo(newFrameToSkipTo); }, pybind11::arg("newFrameToSkipTo"));
	cl_ReplayWrapper.def("GetPlayersOnlyTicks", [](ReplayWrapper& cls_) { return cls_.GetPlayersOnlyTicks(); });
	cl_ReplayWrapper.def("SetPlayersOnlyTicks", [](ReplayWrapper& cls_, int newPlayersOnlyTicks) { return cls_.SetPlayersOnlyTicks(newPlayersOnlyTicks); }, pybind11::arg("newPlayersOnlyTicks"));
	cl_ReplayWrapper.def("GetPlaybackTime", [](ReplayWrapper& cls_) { return cls_.GetPlaybackTime(); });
	cl_ReplayWrapper.def("IsFromBeforeGameVersion", [](ReplayWrapper& cls_, unsigned char BeforeGameVersion) { return cls_.IsFromBeforeGameVersion(BeforeGameVersion); }, pybind11::arg("BeforeGameVersion"));
	cl_ReplayWrapper.def("IsFromBeforeReplayVersion", [](ReplayWrapper& cls_, unsigned char BeforeReplayVersion) { return cls_.IsFromBeforeReplayVersion(BeforeReplayVersion); }, pybind11::arg("BeforeReplayVersion"));
	cl_ReplayWrapper.def("SetReplayName", [](ReplayWrapper& cls_, std::string NewName) { return cls_.SetReplayName(NewName); }, pybind11::arg("NewName"));
	cl_ReplayWrapper.def("RemoveTimelineKeyframe", [](ReplayWrapper& cls_, int KeyframeIndex) { return cls_.RemoveTimelineKeyframe(KeyframeIndex); }, pybind11::arg("KeyframeIndex"));
	cl_ReplayWrapper.def("eventTrimData", [](ReplayWrapper& cls_, int FirstKeyframe, int FirstFrame) { return cls_.eventTrimData(FirstKeyframe, FirstFrame); }, pybind11::arg("FirstKeyframe"), pybind11::arg("FirstFrame"));
	cl_ReplayWrapper.def("CreateCopy", [](ReplayWrapper& cls_, float StartTime) { return cls_.CreateCopy(StartTime); }, pybind11::arg("StartTime"));
	cl_ReplayWrapper.def("ImportReplay", [](ReplayWrapper& cls_, std::string Path) { return cls_.ImportReplay(Path); }, pybind11::arg("Path"));
	cl_ReplayWrapper.def("ExportReplay", [](ReplayWrapper& cls_, std::string Path) { return cls_.ExportReplay(Path); }, pybind11::arg("Path"));
	cl_ReplayWrapper.def("SkipToFrame", [](ReplayWrapper& cls_, int frame, long unsigned int bFlush) { return cls_.SkipToFrame(frame, bFlush); }, pybind11::arg("frame"), pybind11::arg("bFlush"));
	cl_ReplayWrapper.def("SkipToTime", [](ReplayWrapper& cls_, float Time, long unsigned int bFlush) { return cls_.SkipToTime(Time, bFlush); }, pybind11::arg("Time"), pybind11::arg("bFlush"));
	cl_ReplayWrapper.def("GetReplayTimeSeconds", [](ReplayWrapper& cls_) { return cls_.GetReplayTimeSeconds(); });
	cl_ReplayWrapper.def("StopPlayback", [](ReplayWrapper& cls_) { return cls_.StopPlayback(); });
	cl_ReplayWrapper.def("StartPlaybackAtFrame", [](ReplayWrapper& cls_, int StartFrame) { return cls_.StartPlaybackAtFrame(StartFrame); }, pybind11::arg("StartFrame"));
	cl_ReplayWrapper.def("StartPlaybackAtTimeSeconds", [](ReplayWrapper& cls_, float StartTime) { return cls_.StartPlaybackAtTimeSeconds(StartTime); }, pybind11::arg("StartTime"));
	cl_ReplayWrapper.def("StopRecord", [](ReplayWrapper& cls_) { return cls_.StopRecord(); });
	cl_ReplayWrapper.def("StartRecord", [](ReplayWrapper& cls_) { return cls_.StartRecord(); });
	cl_ReplayWrapper.def("Tick2", [](ReplayWrapper& cls_, float DeltaTime) { return cls_.Tick2(DeltaTime); }, pybind11::arg("DeltaTime"));
	cl_ReplayWrapper.def("eventPreExport", [](ReplayWrapper& cls_) { return cls_.eventPreExport(); });
	cl_ReplayWrapper.def("EventPlayedFrame", [](ReplayWrapper& cls_, ReplayWrapper Replay) { return cls_.EventPlayedFrame(Replay); }, pybind11::arg("Replay"));
	cl_ReplayWrapper.def("EventPostTimeSkip", [](ReplayWrapper& cls_, ReplayWrapper Replay) { return cls_.EventPostTimeSkip(Replay); }, pybind11::arg("Replay"));
	cl_ReplayWrapper.def("EventPreTimeSkip", [](ReplayWrapper& cls_, ReplayWrapper Replay) { return cls_.EventPreTimeSkip(Replay); }, pybind11::arg("Replay"));
	cl_ReplayWrapper.def("EventSpawned", [](ReplayWrapper& cls_, ReplayWrapper Replay, ActorWrapper A) { return cls_.EventSpawned(Replay, A); }, pybind11::arg("Replay"), pybind11::arg("A"));
	cl_ReplayWrapper.def("EventPlaybackStopped", [](ReplayWrapper& cls_, ReplayWrapper Replay) { return cls_.EventPlaybackStopped(Replay); }, pybind11::arg("Replay"));
}
